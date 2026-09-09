# 三方向视觉探索：从下载到复用

当前包是 `visual-exploration-starter-beta@1.0.0-beta.1`，本地编译可用，远端尚未发布，图片效果未实测。先使用本地目录或展示站下载包，不假设远程 main 已包含新包。

## 发给 Agent

请使用我提供的 visual-starter 本地模板库，检查 Registry CLI，读取真实输入合同，集中询问需求、受众、硬约束、比例与说明语言。等我答复后再确认、编译和导出。执行探索提示后给出三个方向与取舍，等待我选择，不自动出图或付费。最后换一个主体，建立新会话检验复用。

## 安装和本地来源

先按 Template Registry 公开说明安装 CLI。将免费 ZIP 解压为 `visual-starter`，在它的父目录运行：

```bash
template-registry prompt repository add --id visual-starter --source "file://$PWD/visual-starter" --trust user_trusted --json
template-registry prompt repository sync --id visual-starter --json
template-registry prompt inspect --ref 'promptrepo://visual-starter/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en' --json
```

来源名已存在时使用现有配置或另选名称，不能覆盖无关来源。`inspect` 返回 `partial` 表示必填输入待补齐，是正常下一步。输入合同为 `en`，中文资料仍可作为值。

在完整源码工作区中，也可以把 source 指向本内容仓的绝对 `file://` 路径。不要把本地未发布的新 ref 写成已经能从远程同步获得。

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

## 维护者验证

```bash
python3 scripts/author_visual_exploration.py
python3 scripts/check_visual_exploration.py
```

未安装 CLI 的源码工作区可先在 Registry owner 运行 `go build -o /tmp/template-registry ./cmd/template-registry`，再将 `--registry /tmp/template-registry` 传给脚本。验证会生成脱敏 evidence，私有会话和导出在临时目录中清理。
