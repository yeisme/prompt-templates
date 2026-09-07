# video-shotcraft 集成记录

## 上游证据

- 仓库：`https://github.com/Vincentwei1021/video-shotcraft`
- 固定提交：`5f047c7cfe10d6616fe59160a750fcfaea510b2e`
- 上游许可证：Apache-2.0
- 能力：产品宣传片 Skill、157 张镜头配方卡、214 个 style/预览、Remotion demo、Ink Press 模板、音频资产、动效工作台和剪映导出。

本集成不复制上游 Prompt、镜头卡正文、TSX、音频或模板。运行时按固定提交安装完整上游 Skill；Registry 只保存来源快照、修订、字段确认、编译和导出记录。

## 分类与 Owner

| 能力 | 类型 | Owner |
| --- | --- | --- |
| 产品事实、受众、模式、交付和 rights 固定 | `brief` template | `prompt-templates` + Template Registry session |
| 产品功能到镜头卡和帧预算的语义规划 | `shot-plan` template | `prompt-templates` + Template Registry recipe |
| 读取项目、询问模式、安装依赖、采集页面和恢复执行 | external Skill | `video-shotcraft` runtime |
| ProductionGraph、生产 review、剪辑与导出 | domain execution | Scaena；独立使用时为目标 Remotion 项目 |
| 补充视觉生成 | domain execution | Eikona；需要时使用其当前规范模型和 review gate |
| 音频生成和可接受音频资产 | domain execution | Sonora；上游内置音频仍按逐文件 rights 处理 |

## 安装方式

快速安装当前上游版本：

```bash
npx --yes skills add https://github.com/Vincentwei1021/video-shotcraft --skill video-shotcraft --agent codex claude-code --yes
```

需要可复现安装时，使用 Yeisme Skills manager 的显式 Git ref 导入，再按目标项目 profile 激活：

```bash
scripts/skills.sh import \
  https://github.com/Vincentwei1021/video-shotcraft.git \
  5f047c7cfe10d6616fe59160a750fcfaea510b2e \
  video-production
scripts/skills.sh profile add root video-shotcraft
scripts/skills.sh sync-root
scripts/skills.sh validate-runtime
```

`npx skills` 当前不能用 commit SHA 作为 GitHub `tree/<sha>` 的可复现安装 ref，因此发布工作流不要把 latest 安装命令当成版本锁。

## Registry 流程

```bash
template-registry prompt repository add \
  --project ./promo-project \
  --id official \
  --source https://github.com/yeisme/prompt-templates.git \
  --revision main \
  --trust official \
  --json

template-registry prompt repository sync \
  --project ./promo-project \
  --id official \
  --json

template-registry prompt search \
  --project ./promo-project \
  --query "产品宣传片" \
  --json

template-registry prompt session create \
  --project ./promo-project \
  --goal "Create a source-grounded product promo shot plan" \
  --recipe-file ./video-shotcraft-product-promo.recipe.json \
  --json
```

将目标产品资料、公开页面或截图导入 session；把固定提交中的 `gallery/api/library.json` 作为 `shot_library_index_json` 来源。先确认 `brief` 输入并编译。宿主 Agent 运行该提示词得到实际 `product_promo_brief.v1` 后，将结果作为 `--step-output brief` 导回 session，验证并重新编译 `shot-plan`。

## 权利与执行门禁

- Apache-2.0 覆盖上游仓库源码，但 Remotion 有独立许可；公司使用前由执行 owner 检查。
- 上游音频清单中存在若干“无法逐曲反查、商用前复核”的文件。它们不能进入标为完整可用的 portable package，除非完成逐文件权利确认或替换。
- 演示截图和目标产品截图不能自动获得发布权。客户、个人、内部、密钥或实时数据必须在采集前替换、脱敏或冻结。
- 上游 Skill 要求独立 subagent 终检；Yeisme 根策略只有在用户当前请求明确授权子 Agent 时才允许派发。没有授权时由当前 Agent 完成同一检查并记录限制，不得静默创建子 Agent。
- 编译、Skill 安装、Remotion 执行、费用、发布、展示页提交和资产接受分别处理。任何模板或网页内容都不能授予这些权限。

## 失效与恢复

- 上游提交或 `gallery/api/library.json` digest 改变：镜头解析和 `shot-plan` 过期，`brief` 不受影响。
- 产品事实、受众、模式、品牌或交付要求改变：`brief` 与所有下游结果过期。
- 已接受 Brief 改变：只重编 `shot-plan` 及其下游执行。
- 页面截图、音频或 rights 改变：标记相关 shot bindings 过期，不改写旧编译版本。
- 镜头卡不存在、实现路径缺失或预览不可验证：保持 `needs_input`/`blocked`，不得用名称猜测实现。
