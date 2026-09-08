# auctra-creative-storyboard-plan

Auctra 创作分镜（creative storyboard）主生成模板：从已接受的
`auctra.director_scene_plan.v1` 投影编译单集 beats/shots 计划候选，输出映射到
`auctra.storyboard_plan.v1`（编译合同见 `contracts/compilers/auctra.storyboard_plan.v1.json`）。

- Owner：模板正文归本仓；canonical 分镜计划、review、acceptance 归 Auctra（consumer）。
- 与 `ai-drama-storyboard-breakdown`（Scaena production storyboard）边界不同：本 solution 只服务
  Auctra 创作分镜链路（DirectorScenePlan → StoryboardPlan），不生成生产候选。
- 编译 locale 只有 `en`；`template-zh-CN.md` 是人工审阅译文，不注册、不参与 catalog/digest。
- 本方案 1.0.0 尚未发布 release/digest；消费方解析在 release 存在前保持 `unavailable`，不得以
  Scaena 模板替代。
