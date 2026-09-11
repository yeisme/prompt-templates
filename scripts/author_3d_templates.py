#!/usr/bin/env python3
"""Author the 3d beta package through Registry CLI commands only."""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0-beta.1"

# (id, en title, en summary, en usage, zh title, zh summary, capabilities, tags)
SOLUTIONS = [
    ("text-to-3d-object-beta", "Text to 3D object",
     "Compile a confirmed subject, purpose, style, and constraints into a provider-neutral text-to-3D prompt package",
     "English-compiled beta; human-reviewed Chinese translation ships separately; any 3D execution is a separately authorized step",
     "文生 3D 单物体", "把确认后的主体、用途、风格与约束编译为 provider-neutral 文生 3D 提示包",
     ["model3d", "structured_output", "text"],
     ["category:3d", "modality:3d", "artifact:model_3d", "job:generate"]),
    ("image-to-3d-refine-beta", "Image to 3D refine",
     "Compile a reference-image exact ref with view, occlusion, and consistency decisions into an image-to-3D prompt package",
     "English-compiled beta; references are pointers, never copied; 3D execution is a separately authorized step",
     "图生 3D 精修", "把参考图 exact ref 与视角、遮挡、一致性决策编译为图生 3D 提示包",
     ["model3d", "structured_output", "reference_image"],
     ["category:3d", "modality:3d", "artifact:model_3d", "constraint:multi_view_consistency", "job:generate"]),
    ("3d-scene-layout-beta", "3D scene layout",
     "Compose a provider-neutral multi-object spatial layout with relative placement, a scale statement, and optional camera placeholders",
     "English-compiled beta; generic spatial fields only, no downstream scene schema coupling",
     "3D 场景布局", "输出通用空间字段的多物体布局：相对位置、尺度声明与相机占位",
     ["scene_spatial", "structured_output"],
     ["category:3d", "modality:3d", "artifact:scene_layout", "constraint:scale_anchored", "job:design"]),
    ("3d-printable-design-beta", "3D printable design constraints",
     "Compile confirmed manufacturability constraints into a decidable checklist-style 3D printing prompt package",
     "English-compiled beta; every constraint is a decidable item; printing is a separately authorized step",
     "3D 打印约束", "把可制造性硬约束编译为逐条可判定的打印检查清单",
     ["model3d", "structured_output"],
     ["category:3d", "modality:3d", "artifact:model_3d", "constraint:manifold_geometry", "job:design"]),
    ("3d-asset-review-beta", "3D asset review checklist",
     "Review a candidate 3D asset across geometry integrity, UV and texture, scale consistency, and rights with pass/fail/unknown items",
     "English-compiled beta; reviews report findings and never issue execution instructions",
     "3D 资产评审", "覆盖几何完整性、UV/贴图、比例与使用权的 pass/fail/unknown 评审清单",
     ["model3d", "review", "structured_output"],
     ["category:3d", "modality:3d", "artifact:model_3d", "constraint:rights_aware", "job:critic_review"]),
]

ZH_USAGE = "beta 试点：仅英文可编译；本中文条目为人工审阅说明，完整译文见包内 docs/template-zh-CN.md；任何 3D 执行均需另行授权"

# solution id -> list of input dicts (contract input set flags)
INPUTS = {
    "text-to-3d-object-beta": [
        {"name": "subject", "type": "string", "required": True, "min-length": 1, "max-length": 2000,
         "label-en": "Subject", "label-zh-CN": "主体",
         "description-en": "One object and its distinguishing features", "description-zh-CN": "单一物体及其区分特征"},
        {"name": "purpose", "type": "enum", "required": True, "enum": ["game", "print", "background"],
         "label-en": "Purpose", "label-zh-CN": "用途",
         "description-en": "Intended use driving topology decisions", "description-zh-CN": "驱动拓扑决策的用途"},
        {"name": "style", "type": "string", "required": True, "min-length": 1, "max-length": 2000,
         "label-en": "Style anchor", "label-zh-CN": "风格锚点",
         "description-en": "Verifiable style reference traits", "description-zh-CN": "可验证的风格参考特征"},
        {"name": "poly_budget", "type": "enum", "required": True, "enum": ["low", "mid", "high", "unspecified"],
         "label-en": "Polygon budget", "label-zh-CN": "面数级别",
         "description-en": "Topology density level", "description-zh-CN": "拓扑密度级别"},
        {"name": "symmetry", "type": "enum", "required": True, "enum": ["none", "bilateral", "radial", "unspecified"],
         "label-en": "Symmetry", "label-zh-CN": "对称性约束",
         "description-en": "Symmetry constraint for decomposition", "description-zh-CN": "结构分解的对称性约束"},
        {"name": "material_notes", "type": "string", "required": False, "max-length": 2000,
         "label-en": "Material notes", "label-zh-CN": "材质说明",
         "description-en": "Advisory surface and material look", "description-zh-CN": "参考性的表面与材质观感"},
    ],
    "image-to-3d-refine-beta": [
        {"name": "reference_image_ref", "type": "string", "required": True, "min-length": 1, "max-length": 500,
         "regex": "^promptrepo://[A-Za-z0-9][A-Za-z0-9._-]*/.+",
         "label-en": "Reference image ref", "label-zh-CN": "参考图 exact ref",
         "description-en": "Pointer to the reference image; content is never copied", "description-zh-CN": "参考图指针；正文永不复制"},
        {"name": "view_strategy", "type": "enum", "required": True, "enum": ["multi_view", "single_view_infer"],
         "label-en": "View strategy", "label-zh-CN": "视角策略",
         "description-en": "Committed views or single-view inference", "description-zh-CN": "承诺多视角或单视角推测"},
        {"name": "occlusion_policy", "type": "enum", "required": True,
         "enum": ["inference_marked", "conservative_infer", "visible_only"],
         "label-en": "Occlusion policy", "label-zh-CN": "遮挡推测策略",
         "description-en": "How hidden faces are treated", "description-zh-CN": "不可见面的处理策略"},
        {"name": "consistency_targets", "type": "string", "required": True, "min-length": 1, "max-length": 4000,
         "label-en": "Consistency targets", "label-zh-CN": "一致性特征",
         "description-en": "Features that must survive across views", "description-zh-CN": "必须在各视角保持的特征清单"},
    ],
    "3d-scene-layout-beta": [
        {"name": "objects", "type": "string", "required": True, "min-length": 1, "max-length": 4000,
         "label-en": "Objects", "label-zh-CN": "物体清单",
         "description-en": "Named objects and their scene roles", "description-zh-CN": "具名物体及其场景角色"},
        {"name": "relations", "type": "string", "required": True, "min-length": 1, "max-length": 4000,
         "label-en": "Relations", "label-zh-CN": "相对位置关系",
         "description-en": "Relative placement and orientation between named objects", "description-zh-CN": "具名物体间的相对位置与朝向"},
        {"name": "scale_anchor", "type": "string", "required": False, "max-length": 2000,
         "label-en": "Scale anchor", "label-zh-CN": "尺度锚点",
         "description-en": "Real-world scale reference; empty means relative proportions only", "description-zh-CN": "真实尺度参照；留空表示仅相对比例"},
        {"name": "camera_seeds", "type": "string", "required": False, "max-length": 2000,
         "label-en": "Camera seeds", "label-zh-CN": "相机占位",
         "description-en": "Optional named viewpoints with framing intent", "description-zh-CN": "可选的具名视点与取景意图"},
    ],
    "3d-printable-design-beta": [
        {"name": "wall_thickness", "type": "string", "required": True, "min-length": 1, "max-length": 200,
         "label-en": "Wall thickness", "label-zh-CN": "壁厚",
         "description-en": "Minimum wall thickness with unit", "description-zh-CN": "带单位的最小壁厚"},
        {"name": "support_strategy", "type": "enum", "required": True, "enum": ["none", "minimal", "standard", "dense"],
         "label-en": "Support strategy", "label-zh-CN": "支撑策略",
         "description-en": "Support approach for overhangs and bridges", "description-zh-CN": "悬垂与桥接的支撑策略"},
        {"name": "tolerance", "type": "string", "required": True, "min-length": 1, "max-length": 200,
         "label-en": "Tolerance", "label-zh-CN": "公差",
         "description-en": "Mating tolerance with unit", "description-zh-CN": "带单位的配合公差"},
        {"name": "print_orientation", "type": "string", "required": True, "min-length": 1, "max-length": 500,
         "label-en": "Print orientation", "label-zh-CN": "成型方向",
         "description-en": "Confirmed orientation for printing", "description-zh-CN": "确认的打印成型方向"},
        {"name": "material", "type": "string", "required": False, "max-length": 200,
         "label-en": "Material", "label-zh-CN": "材料",
         "description-en": "Optional material for material-driven checks", "description-zh-CN": "可选材料，用于材料相关检查"},
    ],
    "3d-asset-review-beta": [
        {"name": "asset_ref", "type": "string", "required": True, "min-length": 1, "max-length": 500,
         "label-en": "Asset reference", "label-zh-CN": "资产引用",
         "description-en": "Pointer to the candidate asset under review", "description-zh-CN": "被评审的候选资产引用"},
        {"name": "intended_use", "type": "string", "required": True, "min-length": 1, "max-length": 2000,
         "label-en": "Intended use", "label-zh-CN": "预期用途",
         "description-en": "Use the asset is being reviewed for", "description-zh-CN": "评审所针对的用途"},
        {"name": "scene_context_ref", "type": "string", "required": False, "max-length": 500,
         "label-en": "Scene context ref", "label-zh-CN": "场景上下文引用",
         "description-en": "Optional scene the asset must fit", "description-zh-CN": "可选：资产需适配的场景"},
    ],
}


def flag(value):
    return str(value).lower() if isinstance(value, bool) else str(value)


def author(binary, root):
    def call(*args):
        result = subprocess.run([binary, *args, "--repository", str(root), "--json"], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError("Registry authoring failed: " + " ".join(args[:3]) + ": " + result.stdout.strip()[:400])
        return json.loads(result.stdout)

    for solution_id, title, summary, usage, zh_title, zh_summary, capabilities, tags in SOLUTIONS:
        base = ["--package", "3d", "--id", solution_id]
        prompt = f"solutions/3d/{solution_id}/prompts/main.en.md"
        add = ["solution", "add", *base, "--version", VERSION, "--category", "3d", "--locale", "en",
               "--title", title, "--summary", summary, "--usage", usage, "--prompt-path", prompt,
               "--rights", "internal", "--maturity", "exploratory"]
        for capability in capabilities:
            add += ["--capability", capability]
        for tag in tags:
            add += ["--tag", tag]
        call(*add)
        call("solution", "locale", "describe", *base, "--locale", "zh-CN",
             "--title", zh_title, "--summary", zh_summary, "--usage", ZH_USAGE)
        contract = root / f"solutions/3d/{solution_id}/contracts/main.en.json"
        if not contract.exists():
            call("contract", "init", *base, "--role", "main", "--locale", "en",
                 "--license", "internal", "--permission", "execute_requires_review", "--permission", "preview")
        for spec in INPUTS[solution_id]:
            args = ["contract", "input", "set", *base, "--role", "main", "--locale", "en",
                    "--name", spec["name"], "--type", spec["type"]]
            args += ["--required"] if spec.get("required") else []
            for key in ("regex",):
                if spec.get(key):
                    args += [f"--{key}", spec[key]]
            for key in ("min-length", "max-length"):
                if spec.get(key) is not None:
                    args += [f"--{key}", str(spec[key])]
            for value in spec.get("enum", []):
                args += ["--enum", value]
            args += ["--label-en", spec["label-en"], "--label-zh-CN", spec["label-zh-CN"]]
            if spec.get("description-en"):
                args += ["--description-en", spec["description-en"]]
            if spec.get("description-zh-CN"):
                args += ["--description-zh-CN", spec["description-zh-CN"]]
            call(*args)
        call("contract", "refresh", *base, "--role", "main", "--locale", "en")
        call("contract", "validate", *base, "--role", "main", "--locale", "en")
    call("catalog", "build")
    call("catalog", "validate")
    print("three_d_package=valid solutions=" + str(len(SOLUTIONS)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="template-registry")
    parser.add_argument("--repository", type=Path, default=ROOT)
    args = parser.parse_args()
    author(args.registry, args.repository)


if __name__ == "__main__":
    main()
