# 三方向视觉探索：从下载到复用

本指南使用 `visual-exploration-starter-beta@1.0.0-beta.1`，演示从需求输入到提示包导出，再到第二次复用。图片效果尚未实测。

本页尚未提供独立 ZIP 的公开下载链接。你需要已取得包含该方案的完整模板仓库或评估包；如果只有远程目录且找不到该版本，请先阅读示例，不要继续执行下面的命令。

开始前准备：

- 已安装的 Template Registry CLI；安装入口见[仓库首页](../../README.md)。
- Bash 或 Zsh，以及用于读取命令结果的 `jq`；Windows 可在 WSL 中运行本页示例。
- 包内的 `repository.json`、`catalog.json` 和 `solutions/image/visual-exploration-starter-beta/`；只有模板子目录不足以登记来源。
- 阅读本包的免费评估许可：`solutions/image/visual-exploration-starter-beta/docs/LICENSE.md`。它不包含模板转售或公开分发授权。

## 发给 Agent

请使用我提供的 visual-starter 本地模板库，检查 Registry CLI，读取真实输入合同，集中询问需求、受众、硬约束、比例与说明语言。等我答复后再确认、编译和导出。执行探索提示后给出三个方向与取舍，等待我选择，不自动出图或付费。最后换一个主体，建立新会话检验复用。

## 安装和本地来源

如果你收到独立评估 ZIP，将其解压为 `visual-starter`，并在它的父目录运行。若使用完整模板仓库，将下方 `file://$PWD/visual-starter` 替换为该仓库根目录的绝对 `file://` 地址；登记名称仍可使用 `visual-starter`：

```bash
template-registry prompt repository add --id visual-starter --source "file://$PWD/visual-starter" --trust user_trusted --json
template-registry prompt repository sync --id visual-starter --json
template-registry prompt inspect --ref 'promptrepo://visual-starter/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en' --json
```

来源名已存在时使用现有配置或另选名称，不能覆盖无关来源。`inspect` 返回 `partial` 表示必填输入待补齐，是正常下一步。输入合同为 `en`，中文资料仍可作为值。

先确认 `inspect` 返回的是上述方案与版本，再创建会话。找不到模板时，检查来源目录与版本是否匹配；不要覆盖其他已登记的来源。

## 用户确认后编译

```bash
session_ref=$(template-registry prompt session create --ref 'promptrepo://visual-starter/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en' --goal '为无品牌陶瓷杯探索视觉方向' --json | jq -r '.data.id')
printf '%s' '{"fields":{"main.brief":{"value":"为无品牌米白陶瓷杯探索宣传视觉","kind":"user","source":"user"},"main.audience":{"value":"关注日常器物的读者","kind":"user","source":"user"},"main.constraints":{"value":"单杯；不加 Logo、价格、认证或性能承诺","kind":"user","source":"user"},"main.aspect_ratio":{"value":"4:5","kind":"user","source":"user"},"main.output_language":{"value":"zh-CN","kind":"user","source":"user"}}}' | template-registry prompt session update --session "$session_ref" --expected-revision 1 --stdin --json
```

以上是公开虚构练习。实际私有资料用 stdin 或输入文件传递。用户明确确认这些选择之后，才执行：

```bash
template-registry prompt session confirm --session "$session_ref" --expected-revision 2 --confirm-goal --fields main.brief,main.audience,main.constraints,main.aspect_ratio,main.output_language --decision-ref user-confirmed-visual-brief --json
compile_ref=$(template-registry prompt compile --session "$session_ref" --expected-revision 3 --json | jq -r '.data.id')
template-registry prompt export --compile "$compile_ref" --output result --json
template-registry prompt bundle verify --path result --json
```

`result` 应是当前项目内尚不存在的路径。编译和包校验不是图片生成，也不代表图片已被用户接受。让宿主 Agent 处理导出提示并提出方向；是否用 Eikona 生成、预算多少，另行决定。

## 第二次使用

新建会话，将杯子换成玻璃花瓶，重新确认材质和约束。检查是否残留杯柄、陶瓷质感或旧事实。活动视觉和内容封面练习见包内 `docs/examples.md`。

## 完成后检查

`bundle verify` 应成功结束，导出的提示包位于 `result`。将提示包交给 Agent 后，检查它是否给出三个不同的视觉方向、各自取舍和独立英文出图提示词。此时仍未生成图片。

例如，陶瓷杯练习需要保留“无品牌、米白色、单杯”的条件，不添加价格或认证。换成玻璃花瓶后，结果不应残留杯柄或陶瓷材质。这些是检查标准，不是实测效果展示。

如果编译提示输入不完整，先补充并确认缺少的字段；如果提示版本冲突，先读取当前会话状态，不要直接重复旧的确认命令。模型执行和图片生成另行选择工具并确认费用。
