#!/usr/bin/env python3
"""Author the starter through Registry; optionally export a minimal free repository."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOLUTION = "visual-exploration-starter-beta"
VERSION = "1.0.0-beta.1"
FIELDS = {"brief": "需求", "audience": "受众", "constraints": "硬约束", "aspect_ratio": "比例", "output_language": "说明语言"}


def author(binary, root):
    def call(*args):
        result = subprocess.run([binary, *args, "--repository", str(root), "--json"], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError("Registry authoring failed: " + " ".join(args[:2]))
        return json.loads(result.stdout)

    base = ["--package", "image", "--id", SOLUTION]
    call("solution", "add", *base, "--version", VERSION, "--category", "image", "--locale", "en",
         "--title", "Visual exploration starter", "--summary", "Explore, compare and reuse three visual directions with an Agent",
         "--prompt-path", f"solutions/image/{SOLUTION}/prompts/main.en.md", "--rights", "free-evaluation",
         "--maturity", "exploratory", "--capability", "text", "--capability", "structured_output",
         "--tag", "job:explore", "--tag", "artifact:visual_direction", "--tag", "modality:image")
    call("solution", "locale", "describe", *base, "--locale", "zh-CN", "--title", "三方向视觉探索入门包",
         "--summary", "让 Agent 帮你比较视觉方向并在新任务中复用", "--usage", "免费 beta；英文编译，中文指南，出图另行确认")
    contract = root / f"solutions/image/{SOLUTION}/contracts/main.en.json"
    if not contract.exists():
        call("contract", "init", *base, "--locale", "en", "--license", "LicenseRef-Yeisme-Free-Evaluation",
             "--permission", "preview", "--permission", "execute_requires_review")
    for field, label in FIELDS.items():
        args = ["contract", "input", "set", *base, "--name", field, "--required", "--type", "string",
                "--label-en", field.replace("_", " ").title(), "--label-zh-CN", label,
                "--min-length", "1", "--max-length", "8000" if field == "brief" else "2000"]
        if field == "aspect_ratio":
            args += ["--regex", "^(1:1|4:5|3:4|16:9|9:16)$"]
        call(*args)
    call("contract", "refresh", *base, "--locale", "en")
    call("contract", "validate", *base, "--locale", "en")
    call("catalog", "build")
    call("catalog", "validate")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="template-registry")
    parser.add_argument("--sample-output", type=Path)
    args = parser.parse_args()
    author(args.registry, ROOT)
    if args.sample_output:
        destination = args.sample_output.resolve()
        if destination.exists():
            raise SystemExit("Sample destination already exists; choose a new empty destination.")
        destination.mkdir(parents=True)
        subprocess.run([args.registry, "repository", "init", "--repository", str(destination), "--id", "official",
                        "--name", "Yeisme free visual exploration starter", "--default-locale", "en", "--json"],
                       stdout=subprocess.DEVNULL, check=True)
        relative = Path("solutions/image") / SOLUTION
        # Only author-owned public prose is copied; the CLI regenerates all metadata.
        for folder in ("prompts", "docs"):
            shutil.copytree(ROOT / relative / folder, destination / relative / folder)
        guide = Path("docs/visual-exploration/quickstart.md")
        (destination / guide).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / guide, destination / guide)
        author(args.registry, destination)
        with zipfile.ZipFile(destination.with_suffix(".zip"), "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(destination.rglob("*")):
                if path.is_file():
                    archive.write(path, Path("visual-starter") / path.relative_to(destination))
        print("sample_export=ready")
    print("starter_catalog=valid")


if __name__ == "__main__":
    main()
