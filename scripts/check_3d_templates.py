#!/usr/bin/env python3
"""Provider-free acceptance for the 3d beta package: compile dry-runs, locale discipline,
recipe DAG validation, and zh-CN translation variable parity. Evidence is redacted."""
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
VERSION = "1.0.0-beta.1"
REF = "promptrepo://official/3d/{id}@" + VERSION + "?locale=en"
RECIPE_PATH = "recipes/concept-to-3d-asset-beta.json"

# id -> (required fields with sample values, optional fields with sample values,
#        reuse swap {field: (first, replacement)}, invalid case description (field, bad value))
CASES = {
    "text-to-3d-object-beta": (
        {"subject": "A fictional brass desk lantern", "purpose": "game", "style": "clean stylized low-poly",
         "poly_budget": "low", "symmetry": "bilateral"},
        {"material_notes": "matte painted metal"},
        "subject", ("A fictional brass desk lantern", "A fictional glass desk globe"),
        ("purpose", "sculpture"),
    ),
    "image-to-3d-refine-beta": (
        {"reference_image_ref": "promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en",
         "view_strategy": "multi_view", "occlusion_policy": "inference_marked",
         "consistency_targets": "silhouette, handle attachment, base footprint"},
        {},
        "consistency_targets", ("silhouette, handle attachment, base footprint", "spout curve, lid seat, engraving band"),
        ("reference_image_ref", "https://example.com/lantern.png"),
    ),
    "3d-scene-layout-beta": (
        {"objects": "reading chair; floor lamp; side table",
         "relations": "chair faces the window wall; lamp stands right of the chair; table sits left of the chair"},
        {"scale_anchor": "chair seat height as shared reference", "camera_seeds": "entry-door wide shot framing chair and lamp"},
        "objects", ("reading chair; floor lamp; side table", "dining table; bench; pendant lamp"),
        ("relations", None),  # None = omit a required field entirely
    ),
    "3d-printable-design-beta": (
        {"wall_thickness": "2 mm", "support_strategy": "minimal", "tolerance": "0.2 mm",
         "print_orientation": "flat on the back face"},
        {"material": "PLA"},
        "print_orientation", ("flat on the back face", "upright on the build plate"),
        ("support_strategy", "maybe"),
    ),
    "3d-asset-review-beta": (
        {"asset_ref": REF.format(id="text-to-3d-object-beta"), "intended_use": "game background prop"},
        {},
        "intended_use", ("game background prop", "physical display print"),
        ("asset_ref", None),
    ),
}

PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z][A-Za-z0-9_]*)\s*\}\}")


def variables(body):
    return sorted(set(PLACEHOLDER.findall(body)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="template-registry")
    parser.add_argument("--repository", type=Path, default=ROOT)
    parser.add_argument("--repository-id", default="official")
    args = parser.parse_args()
    invocation = shlex.join(["python3", "scripts/check_3d_templates.py", *sys.argv[1:]])
    start = datetime.now(timezone.utc)
    run = ROOT / "temp/integration-test-runs" / (start.strftime("%Y%m%dT%H%M%S") + "-three-d-" + uuid.uuid4().hex[:8])
    (run / "artifacts").mkdir(parents=True)
    rows = []
    code = 0
    failure = ""
    tick = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="three-d-templates-") as workspace:
        env = {**os.environ, "TEMPLATE_REGISTRY_CONFIG_ROOT": str(Path(workspace) / "config")}
        project = str(Path(workspace) / "project")

        def call(name, payload, reject=False):
            result = subprocess.run([args.registry, "prompt", *name.split(), "--project", project, "--stdin", "--json"],
                                    input=json.dumps(payload), text=True, capture_output=True, env=env)
            data = json.loads(result.stdout)
            accepted = {"success", "partial"} if name in {"inspect", "session create", "session update", "session confirm"} else {"success"}
            success = result.returncode == 0 and data.get("status") in accepted
            rows.append({"operation": name, "expected": "rejected" if reject else "success", "matched": success != reject})
            if success == reject:
                raise RuntimeError("Unexpected outcome: " + name + " (" + data.get("error", {}).get("code", "unknown") + ")")
            return data.get("data", {})

        def cli(maintainer, payload, reject=False, project_dir=None):
            result = subprocess.run([args.registry, *maintainer.split(), "--stdin", "--json", "--project", str(project_dir or project)],
                                    input=json.dumps(payload), text=True, capture_output=True, env=env)
            data = json.loads(result.stdout)
            success = result.returncode == 0 and data.get("status") == "success"
            rows.append({"operation": maintainer, "expected": "rejected" if reject else "success", "matched": success != reject})
            if success == reject:
                raise RuntimeError("Unexpected outcome: " + maintainer)
            return data.get("data", {})

        try:
            # Locale policy: only en templates/contracts are registered; zh-CN must not compile.
            catalog = json.loads((args.repository / "catalog.json").read_text())
            for entry in catalog["solutions"]:
                if entry["package_id"] == "3d":
                    locales = [t["locale"] for t in entry["templates"]]
                    if locales != ["en"]:
                        raise RuntimeError("3d solution registers non-en template locale")
                    if any(t["locale"] == "zh-CN" for t in entry["templates"]):
                        raise RuntimeError("zh-CN translation entered catalog template list")

            call("repository add", {"id": args.repository_id, "source": args.repository.resolve().as_uri(), "trust": "user_trusted"})
            call("repository sync", {"id": args.repository_id})

            for solution_id, (required, optional, swap_field, (first, replacement), (bad_field, bad_value)) in CASES.items():
                ref = REF.format(id=solution_id)
                inspected = call("inspect", {"ref": ref, "role": "main"})
                # zh-CN is human-review only: locale=zh-CN session creation must be rejected.
                call("session create", {"ref": ref.replace("locale=en", "locale=zh-CN"), "role": "main", "goal": "Synthetic invalid locale"}, True)
                # Unconfirmed and empty sessions must refuse to compile.
                session = call("session create", {"ref": ref, "role": "main", "goal": "Synthetic 3d dry-run"})
                sid, revision = session["id"], session["revision"]
                call("compile", {"session_id": sid, "expected_revision": revision}, True)
                session = call("session update", {"session_id": sid, "expected_revision": revision,
                              "fields": {f"main.{k}": {"value": v, "kind": "user", "source": "user", "confirmed": False} for k, v in required.items()}})
                call("compile", {"session_id": sid, "expected_revision": session["revision"]}, True)
                session = call("session confirm", {"session_id": sid, "expected_revision": session["revision"],
                              "goal": True, "fields": [f"main.{k}" for k in required], "decision_ref": "synthetic-fixture-consent"})
                compiled = call("compile", {"session_id": sid, "expected_revision": session["revision"]})
                if compiled.get("provider_calls") != 0:
                    raise RuntimeError("Compile must remain provider-free")
                output = str(Path(project) / ("export-" + uuid.uuid4().hex))
                call("export", {"compile_id": compiled["id"], "output": output})
                call("bundle verify", {"path": output})
                bodies = [p.read_text() for p in (Path(output) / "prompts").glob("*.txt")]
                if not bodies or any(PLACEHOLDER.search(body) for body in bodies):
                    raise RuntimeError("Export unresolved variable check failed")
                if first not in "".join(bodies):
                    raise RuntimeError("Export binding check failed")
                # Invalid value (enum or regex) or missing required field: a fresh session must fail compile.
                negative = dict(required)
                if bad_value is None:
                    negative.pop(bad_field)
                else:
                    negative[bad_field] = bad_value
                session = call("session create", {"ref": ref, "role": "main", "goal": "Synthetic negative dry-run"})
                session = call("session update", {"session_id": session["id"], "expected_revision": session["revision"],
                              "fields": {f"main.{k}": {"value": v, "kind": "user", "source": "user", "confirmed": False} for k, v in negative.items()}})
                session = call("session confirm", {"session_id": session["id"], "expected_revision": session["revision"],
                              "goal": True, "fields": [f"main.{k}" for k in negative], "decision_ref": "synthetic-invalid-case"})
                call("compile", {"session_id": session["id"], "expected_revision": session["revision"]}, True)
                # Optional fields: unset optionals must not block a fresh compile.
                if optional:
                    session = call("session create", {"ref": ref, "role": "main", "goal": "Synthetic optional-omitted dry-run"})
                    sid2, revision2 = session["id"], session["revision"]
                    session = call("session update", {"session_id": sid2, "expected_revision": revision2,
                                  "fields": {f"main.{k}": {"value": v, "kind": "user", "source": "user", "confirmed": False} for k, v in required.items()}})
                    session = call("session confirm", {"session_id": sid2, "expected_revision": session["revision"],
                                  "goal": True, "fields": [f"main.{k}" for k in required], "decision_ref": "synthetic-fixture-consent"})
                    compiled2 = call("compile", {"session_id": sid2, "expected_revision": session["revision"]})
                    if compiled2.get("provider_calls") != 0:
                        raise RuntimeError("Optional-omitted compile must remain provider-free")
                # Reuse: swap one field, rebuild independently, no leakage of the first value.
                session = call("session create", {"ref": ref, "role": "main", "goal": "Synthetic reuse dry-run"})
                sid3, revision3 = session["id"], session["revision"]
                values = dict(required)
                values[swap_field] = replacement
                session = call("session update", {"session_id": sid3, "expected_revision": revision3,
                              "fields": {f"main.{k}": {"value": v, "kind": "user", "source": "user", "confirmed": False} for k, v in values.items()}})
                session = call("session confirm", {"session_id": sid3, "expected_revision": session["revision"],
                              "goal": True, "fields": [f"main.{k}" for k in values], "decision_ref": "synthetic-fixture-consent"})
                compiled3 = call("compile", {"session_id": sid3, "expected_revision": session["revision"]})
                output3 = str(Path(project) / ("reuse-" + uuid.uuid4().hex))
                call("export", {"compile_id": compiled3["id"], "output": output3})
                bodies3 = [p.read_text() for p in (Path(output3) / "prompts").glob("*.txt")]
                if not any(replacement in body for body in bodies3) or any(first in body for body in bodies3):
                    raise RuntimeError("Reuse replacement or leakage check failed")

            # Recipe: CLI validation, exact-ref resolution, and cycle rejection.
            recipe = json.loads((args.repository / RECIPE_PATH).read_text())
            validated = cli("prompt recipe validate", {"path": RECIPE_PATH}, project_dir=args.repository)
            if not validated.get("valid") or validated.get("steps") != ["image-to-3d", "asset-review"]:
                raise RuntimeError("Recipe DAG validation failed")
            known = {(s["package_id"], s["id"], s["version"]) for s in catalog["solutions"]}
            for step in recipe["steps"]:
                match = re.match(r"promptrepo://([^/]+)/([^/]+)/([^@?]+)@([^?]+)", step["ref"])
                if not match or (match.group(2), match.group(3), match.group(4)) not in known:
                    raise RuntimeError("Recipe step ref does not resolve: " + step["id"])
                if "locale=en" not in step["ref"]:
                    raise RuntimeError("Recipe step ref is not exact locale=en")
            cyclic = {"schema_version": recipe["schema_version"], "id": "cyclic-probe", "steps": [
                {"id": "a", "ref": recipe["steps"][0]["ref"], "depends_on": ["b"]},
                {"id": "b", "ref": recipe["steps"][1]["ref"], "depends_on": ["a"]}]}
            (Path(project) / "recipes").mkdir(parents=True, exist_ok=True)
            (Path(project) / "recipes/cyclic-probe.json").write_text(json.dumps(cyclic))
            cli("prompt recipe validate", {"path": "recipes/cyclic-probe.json"}, reject=True)
            # Recipe session pins both templates; compile before any confirmation must refuse.
            session = call("session create", {"goal": "Synthetic recipe dry-run", "recipe": recipe})
            call("compile", {"session_id": session["id"], "expected_revision": session["revision"]}, True)

            # zh-CN translation variable parity (docs/template-zh-CN.md per solution).
            for solution_id in CASES:
                en = variables((args.repository / f"solutions/3d/{solution_id}/prompts/main.en.md").read_text())
                zh = variables((args.repository / f"solutions/3d/{solution_id}/docs/template-zh-CN.md").read_text())
                if en != zh:
                    raise RuntimeError("Translation variable parity failed: " + solution_id)
            print("three_d_templates=passed solutions=" + str(len(CASES)) + " provider_calls=0")
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
