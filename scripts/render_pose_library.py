#!/usr/bin/env python3
"""Render standardized English pose clauses from grounded-pose-library specs.

Each pose spec (assets/poses/<id>.json) carries five slots: pose_lead plus four
body-section sentences (lower limbs, upper limbs, torso & head, weight &
silhouette). The renderer validates every spec fail-closed, assembles the
copy-paste clause, and writes examples/<id>/pose-clause.en.md plus a machine
index at examples/index.json. Specs are source content; examples are generated.

Direction contract: frame-left / frame-right are camera-relative. Subject-owned
left/right, camera/lens/light/wardrobe vocabulary, missing sections and missing
terminal punctuation all fail the run.

Examples:
  python3 scripts/render_pose_library.py
  python3 scripts/render_pose_library.py --pose p01-mermaid-side-sit
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOLUTION_DIR = REPO_ROOT / "solutions" / "image" / "grounded-pose-library"
POSES_DIR = SOLUTION_DIR / "assets" / "poses"
EXAMPLES_DIR = SOLUTION_DIR / "examples"

BODY_FIELDS = ["lower_limbs", "upper_limbs", "torso_head", "weight_silhouette"]

BANNED_PATTERNS = [
    (re.compile(r"\b(his|her|their|its)\s+(left|right)\b", re.I),
     "subject-owned left/right"),
    (re.compile(r"\bsubject's\s+(left|right)\b", re.I),
     "subject-owned left/right"),
    (re.compile(r"\b(camera|lens|lighting|wardrobe|outfit|style)\b", re.I),
     "non-pose vocabulary"),
]


def load_specs(only=None):
    paths = sorted(POSES_DIR.glob("*.json"))
    if only:
        paths = [p for p in paths if p.stem == only]
        if not paths:
            raise SystemExit(f"unknown pose: {only} (looked in {POSES_DIR})")
    specs = []
    for path in paths:
        try:
            spec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"cannot read pose spec {path.name}: {exc}") from exc
        spec["_file"] = path.name
        specs.append(spec)
    specs.sort(key=lambda s: s["no"])
    return specs


def validate(spec):
    errors = []
    for field in ["id", "no", "family", "label", "pose_lead"] + BODY_FIELDS:
        if not str(spec.get(field, "")).strip():
            errors.append(f"missing field: {field}")
    lead = spec.get("pose_lead", "")
    if lead and not lead.rstrip().endswith(":"):
        errors.append("pose_lead must end with ':'")
    for field in BODY_FIELDS:
        text = spec.get(field, "")
        if text and not text.rstrip().endswith("."):
            errors.append(f"{field} must end with '.'")
        for pattern, reason in BANNED_PATTERNS:
            if pattern.search(text) or (lead and pattern.search(lead)):
                errors.append(f"{field or 'pose_lead'}: {reason}")
    return errors


def render_clause(spec):
    parts = [spec["pose_lead"].strip()] + [spec[f].strip() for f in BODY_FIELDS]
    return " ".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pose", help="render a single pose id")
    args = parser.parse_args()

    specs = load_specs(args.pose)

    failures = 0
    for spec in specs:
        errors = validate(spec)
        if errors:
            failures += 1
            print(f"[FAIL] {spec.get('id', spec.get('_file', '?'))}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
    if failures:
        raise SystemExit(f"{failures} pose spec(s) failed validation; nothing written")

    index_poses = []
    families = {}
    for spec in specs:
        clause = render_clause(spec)
        out_dir = EXAMPLES_DIR / spec["id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "pose-clause.en.md").write_text(clause + "\n", encoding="utf-8")
        index_poses.append({
            "no": spec["no"],
            "id": spec["id"],
            "family": spec["family"],
            "label": spec["label"],
            "file": f"examples/{spec['id']}/pose-clause.en.md",
        })
        families.setdefault(spec["family"], []).append(spec["id"])

    index = {
        "schema_version": "grounded-pose-library-examples/1.0",
        "generated_by": "scripts/render_pose_library.py",
        "pose_count": len(index_poses),
        "poses": index_poses,
        "families": {k: {"count": len(v), "members": v} for k, v in sorted(families.items())},
    }
    EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    (EXAMPLES_DIR / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"rendered {len(index_poses)} pose clause(s) -> {EXAMPLES_DIR}")


if __name__ == "__main__":
    main()
