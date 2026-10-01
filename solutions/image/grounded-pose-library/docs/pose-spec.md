# Pose Spec 字段说明

每个姿势一个 `assets/poses/<id>.json`，`schema_version: grounded-pose-library/1.0`。新增姿势 = 复制现有 spec 修改。spec 由 agent/人编辑（源内容）；`examples/` 下的成句提示词与索引由 `scripts/render_pose_library.py` 生成，禁止手写。

## 字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | string | 姿势 slug，`p<两位编号>-<名称>`，进索引与文件名 |
| `no` | int | 原表编号 1–25，排序用 |
| `family` | string | 姿势家族 machine id（见下表） |
| `label` | string | 中文审阅名，不进提示词 |
| `pose_lead` | string | 英文引导短语，以冒号结尾，如 `Grounded pose, mermaid side-sit with rear support:` |
| `lower_limbs` | string | 下肢完整英文句，句号结尾 |
| `upper_limbs` | string | 上肢完整英文句，句号结尾 |
| `torso_head` | string | 躯干与头部完整英文句，句号结尾 |
| `weight_silhouette` | string | 重心与轮廓完整英文句，句号结尾 |

## 方向约定

- 一律 **camera-relative**：`frame-left` / `frame-right` 指画面左/右（观众视角），绝不使用主体自身的左右。
- 原表中「一侧/另一侧」「同一侧」等模糊方向保留为 one side / the other 的中性表述。
- 渲染脚本 fail-closed 检查：四个部位句缺失、句尾无句号、出现 `his/her/their/subject's left|right`、出现 `camera/lens/light/wardrobe` 词，任一命中即报错。

## 姿势家族

| family | 中文 | 成员 |
| --- | --- | --- |
| `side-sit-rear-support` | 侧坐后撑 | 1、7、10、14、17、25 |
| `quadruped-kneeling-support` | 四足/跪撑 | 4、8、11、19、22（+2） |
| `frontal-wide-knee-kneel` | 正面开膝跪姿 | 9、23 |
| `prone-side-lying-rest` | 俯卧/侧卧休息 | 5、6、13、21 |
| `supine` | 仰卧 | 18、24 |
| `independent-grounded` | 独立坐/跪/蜷缩 | 3、12、15、16、20 |

> 归组备注：原始分组未归置 2 号（跪姿回身），按形状最接近归入 `quadruped-kneeling-support`（跪撑 + 回身扭转）。

## 渲染

```bash
python3 scripts/render_pose_library.py            # 全部 25 个
python3 scripts/render_pose_library.py --pose p01-mermaid-side-sit
```

输出：`examples/<id>/pose-clause.en.md`（单段可直接复制的动作提示词）与 `examples/index.json`（机器索引：编号、family、label、文件、家族统计）。
