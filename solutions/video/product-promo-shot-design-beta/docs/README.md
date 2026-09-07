# 产品宣传片镜头设计 beta

本方案补充“真实产品资料和页面 → 已确认产品宣传片 Brief → 镜头卡映射与镜头计划”的语义层。它不负责页面采集、Remotion 编码、渲染、剪辑、费用、发布或资产接受。

可编译模板只有英文：

- `brief`：固定产品事实、受众、创作模式、品牌、交付、数据和 rights，生成 `product_promo_brief.v1`。
- `shot-plan`：消费已接受 Brief、固定版本的镜头库索引和资产映射，生成 `product_promo_shot_plan.v1`。

中文译文只在 `template-zh-CN.md` 中供人工审阅。中文产品资料可以通过英文 contract 注入，`output_language` 决定模型产物语言。

## 与 video-shotcraft 的集成

首个 canary 使用 `Vincentwei1021/video-shotcraft` 的提交 `5f047c7cfe10d6616fe59160a750fcfaea510b2e`。该仓库是完整外部 Skill 和 Remotion 生产工具包，不是 Promptrepo 模板仓，因此：

- Template Registry 不把它加入 `prompt repository`；
- Agent runtime 单独安装并固定外部 Skill；
- `gallery/api/library.json` 作为带修订号的公开镜头库来源导入当前 Registry session；
- 本方案的 `brief` 与 `shot-plan` 通过 recipe 串联；
- 生成的语义镜头计划交给 `video-shotcraft` 或 Scaena/Remotion owner 执行。

详细边界、安装和恢复见 `video-shotcraft-integration.md`。CLI 生成的 recipe 位于 `examples/video-shotcraft-product-promo.recipe.json`。

公开合成 example 由 Registry fixture 命令生成，可直接查看或复制为自己的输入文件：

- `fixtures/brief.en/video-shotcraft-guided.input.json`
- `fixtures/brief.en/video-shotcraft-guided.output.json`
- `fixtures/shot-plan.en/video-shotcraft-guided.input.json`
- `fixtures/shot-plan.en/video-shotcraft-guided.output.json`

这些 example 不含真实产品资料、凭据或 Provider payload。替换字段后仍需在自己的 session 中导入、确认和编译，不能把 fixture 的确认状态带入真实任务。
