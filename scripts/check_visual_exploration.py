#!/usr/bin/env python3
"""Provider-free CLI acceptance with isolated state and body-free evidence."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import shlex
import sys
import tempfile
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
REF = "promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en"
FIELDS = ["brief", "audience", "constraints", "aspect_ratio", "output_language"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="template-registry")
    parser.add_argument("--repository", type=Path, default=ROOT)
    parser.add_argument("--repository-id", default="official")
    parser.add_argument("--ref", default=REF)
    parser.add_argument("--role", default="main")
    args = parser.parse_args()
    invocation = shlex.join(["python3", "scripts/check_visual_exploration.py", *sys.argv[1:]])
    start = datetime.now(timezone.utc)
    run = ROOT / "temp/integration-test-runs" / (start.strftime("%Y%m%dT%H%M%S") + "-visual-" + uuid.uuid4().hex[:8])
    (run / "artifacts").mkdir(parents=True)
    rows = []
    code = 0
    failure = ""
    tick = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="visual-exploration-") as workspace:
        env = {**os.environ, "TEMPLATE_REGISTRY_CONFIG_ROOT": str(Path(workspace) / "config")}
        project = str(Path(workspace) / "project")

        def call(name, payload, reject=False):
            result = subprocess.run([args.registry, "prompt", *name.split(), "--project", project, "--stdin", "--json"],
                                    input=json.dumps(payload), text=True, capture_output=True, env=env)
            # Never persist raw CLI output, arguments or input bodies.
            data = json.loads(result.stdout)
            accepted = {"success", "partial"} if name in {"inspect", "session create", "session update", "session confirm"} else {"success"}
            success = result.returncode == 0 and data.get("status") in accepted
            rows.append({"operation": name, "expected": "rejected" if reject else "success", "matched": success != reject})
            if success == reject:
                error_code = data.get("error", {}).get("code", "unknown")
                raise RuntimeError("Unexpected outcome: " + name + " (" + error_code + ")")
            return data.get("data", {})

        try:
            call("repository add", {"id": args.repository_id, "source": args.repository.resolve().as_uri(), "trust": "user_trusted"})
            call("repository sync", {"id": args.repository_id})
            inspected = call("inspect", {"ref": args.ref, "role": args.role})
            call("session create", {"ref": args.ref.replace("locale=en", "locale=zh-CN"), "role": args.role, "goal": "Synthetic invalid locale"}, True)
            call("session create", {"ref": args.ref.replace("@1.0.0-beta.1", "@99.0.0"), "role": args.role, "goal": "Synthetic invalid version"}, True)
            for brief, replacement in (("Unbranded ceramic cup", "Unbranded glass vase"),
                                       ("Fictional plant exchange", "Fictional book exchange"),
                                       ("Beginner desk organization cover", "Beginner backpack organization cover")):
                for subject in (brief, replacement):
                    session = call("session create", {"ref": args.ref, "role": args.role, "goal": "Synthetic visual exploration"})
                    sid, revision = session["id"], session["revision"]
                    call("compile", {"session_id": sid, "expected_revision": revision}, True)
                    values = dict(zip(FIELDS, [subject, "Beginner creators", "No brand, claims or invented facts", "4:5", "zh-CN"]))
                    session = call("session update", {"session_id": sid, "expected_revision": revision,
                                  "fields": {f"main.{k}": {"value": v, "kind": "user", "source": "user", "confirmed": False} for k, v in values.items()}})
                    call("compile", {"session_id": sid, "expected_revision": session["revision"]}, True)
                    session = call("session confirm", {"session_id": sid, "expected_revision": session["revision"],
                                   "goal": True, "fields": [f"main.{k}" for k in FIELDS], "decision_ref": "synthetic-fixture-consent"})
                    compiled = call("compile", {"session_id": sid, "expected_revision": session["revision"]})
                    if compiled.get("provider_calls") != 0:
                        raise RuntimeError("Compile must remain provider-free")
                    output = str(Path(project) / ("export-" + uuid.uuid4().hex))
                    call("export", {"compile_id": compiled["id"], "output": output})
                    call("bundle verify", {"path": output})
                    bodies = [p.read_text() for p in (Path(output) / "prompts").glob("*.txt")]
                    if not any(subject in body for body in bodies) or any(re.search(r"{{\s*\w+\s*}}", body) for body in bodies):
                        raise RuntimeError("Export binding or unresolved variable check failed")
                    if subject == replacement and any(brief in body for body in bodies):
                        raise RuntimeError("Previous subject leaked into reused export")
                    if subject == brief:
                        session = call("session update", {"session_id": sid, "expected_revision": session["revision"],
                                       "fields": {"main.aspect_ratio": {"value": "7:0", "kind": "user", "source": "user", "confirmed": False}}})
                        session = call("session confirm", {"session_id": sid, "expected_revision": session["revision"],
                                       "fields": ["main.aspect_ratio"], "decision_ref": "synthetic-invalid-ratio"})
                        call("compile", {"session_id": sid, "expected_revision": session["revision"]}, True)
                        call("export", {"compile_id": compiled["id"], "output": str(Path(project) / ("stale-" + uuid.uuid4().hex))}, True)
            print("visual_exploration=passed scenarios=3 reuse_runs=3 provider_calls=0")
        except Exception as error:
            code = 1
            failure = str(error) if isinstance(error, RuntimeError) else type(error).__name__
        finally:
            end = datetime.now(timezone.utc)
            (run / "stdout.log").write_text("\n".join(f"{r['operation']}: {'passed' if r['matched'] else 'failed'}" for r in rows) + "\n")
            (run / "stderr.log").write_text(failure + "\n" if failure else "")
            (run / "command.txt").write_text(invocation + "\n")
            (run / "env.json").write_text(json.dumps({"state": "isolated-temporary", "provider_calls": 0}) + "\n")
            (run / "artifacts/checks.json").write_text(json.dumps(rows, indent=2) + "\n")
            summary = {"schema_version": "yeisme.integration_test_evidence.v1", "project": "data/yeisme-prompt-templates",
                       "run_id": run.name, "layer": "e2e", "command": invocation,
                       "status": "passed" if code == 0 else "failed", "exit_code": code, "started_at": start.isoformat(),
                       "finished_at": end.isoformat(), "duration_ms": round((time.monotonic() - tick) * 1000),
                       "evidence": {"stdout": "stdout.log", "stderr": "stderr.log", "command": "command.txt", "env": "env.json", "artifacts": "artifacts/"},
                       "redaction": {"enabled": True, "policy": "operation-and-outcome-only; private exports deleted"}}
            (run / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print("evidence=" + str(run.relative_to(ROOT)))
    if failure:
        print("failure=" + failure)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
