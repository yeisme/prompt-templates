# 使用说明：贴地姿势库（25 个参考姿势）

## 适用目标

坐、跪、卧及其过渡姿态的**姿势槽位**供给库。产物是与风格无关（style-neutral）的英文动作提示词单句，可直接拼进任何图像提示词的 pose 槽：南部哥特/新英格兰哥特纪实层、仙侠风格层、抓拍镜头模板等。不做镜头、光线、服装、风格描述。

## 两种用法

1. **直接复制**：`examples/<id>/pose-clause.en.md`，每姿势一条成句提示词，复制即用。
2. **变量编译**：按 `prompts/main.en.md` 五槽位（`pose_lead` + 四个部位句）绑定，渲染结果同样是成句动作提示词。

## 与风格层组合示例

```text
<southern-gothic-documentary 的 setting>
+ examples/p20-knees-hugged-sit/pose-clause.en.md（抱膝坐姿句）
+ <风格层的其余固定段>
```

## 渲染与维护

```bash
python3 scripts/render_pose_library.py          # 全量渲染 examples/ + index.json
python3 scripts/render_pose_library.py --pose p06-side-lying-elbow-support
```

spec 源数据在 `assets/poses/*.json`，字段与方向约定见 `docs/pose-spec.md`。

## 审阅

对照自检清单：四段齐全且顺序固定（下肢→上肢→躯干头→重心轮廓）；方向只有 frame-left / frame-right，无主体左右；无镜头/光线/服装/风格词混入。
