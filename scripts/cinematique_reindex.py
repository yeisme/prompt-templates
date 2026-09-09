#!/usr/bin/env python3
"""Rebuild solutions/video/cinematique-shot-techniques-beta/assets/index.json
from the per-technique spec files, and print the refreshed technique_id enum
values for `template-registry contract input set`.

The spec files under assets/techniques/ are human-editable source content
(vendored from vvsvs.pro/cinematique); this index is derived and must be
regenerated after any spec add/remove/rename. Run from repository root.
"""
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOL = ROOT / "solutions" / "video" / "cinematique-shot-techniques-beta"
TECH = SOL / "assets" / "techniques"

CATEGORY_ORDER = [
    "Camera Work",
    "Lighting",
    "Composition",
    "Editing",
    "Storytelling",
    "Visual Effects & Promptable FX",
    "Genres & Styles",
]

def main() -> int:
    specs = []
    for path in sorted(TECH.glob("*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        if path.stem != spec["id"]:
            print(f"spec id mismatch: {path.name} has id {spec['id']}", file=sys.stderr)
            return 1
        for field in ("id", "name", "category", "difficulty", "summary", "prompt_template",
                      "when_to_use", "directing_the_ai", "common_mistakes", "source"):
            if not spec.get(field):
                print(f"spec {spec['id']} missing field {field}", file=sys.stderr)
                return 1
        if "[Subject]" not in spec["prompt_template"]:
            print(f"spec {spec['id']} prompt_template missing [Subject] placeholder", file=sys.stderr)
            return 1
        specs.append(spec)

    categories: dict[str, int] = {}
    for spec in specs:
        categories[spec["category"]] = categories.get(spec["category"], 0) + 1

    index = {
        "schema_version": "cinematique.index.v1",
        "solution_id": "cinematique-shot-techniques-beta",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(specs),
        "categories": {c: categories.get(c, 0) for c in CATEGORY_ORDER if c in categories},
        "techniques": [
            {
                "id": s["id"],
                "name": s["name"],
                "category": s["category"],
                "difficulty": s["difficulty"],
                "moods": s.get("moods", []),
                "has_video": s.get("has_video", False),
            }
            for s in specs
        ],
    }
    out = SOL / "assets" / "index.json"
    out.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"index written: {out} ({len(specs)} techniques)")
    print("technique_id enum values for contract input set:")
    print(",".join(s["id"] for s in specs))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
