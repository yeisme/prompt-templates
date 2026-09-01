# Provider-free 语义示例

以下是 transport 形状示例，不是可直接提交给模型或 provider 的 prompt，也不创建任何 Owner 状态。

```json
{
  "profile_id": "cinematic_live_action",
  "accepted_source_projection_json": "{\"scene_fact\":\"two characters contest one decision\",\"rights\":\"internal\",\"readiness\":\"candidate\"}",
  "active_reference_bindings_json": "{\"identity_source\":{\"inherit\":[\"face_geometry\",\"hairline\"],\"forbid\":[\"source_expression\",\"wardrobe\"]},\"location_source\":{\"inherit\":[\"anchors\",\"light_logic\"],\"forbid\":[\"accidental_people\"]}}",
  "task_delta_json": "{\"task\":\"compile_one_scene_closure\",\"change_scope\":[\"scene_coverage\"]}",
  "output_schema_version": "ai_film_semantic_proposal_v1",
  "continuity_constraints_json": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
  "retry_policy_json": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}"
}
```

合格的语义结果只说明 first-frame lock、可观察表演、SceneGEO 风险、fallback coverage、finding 和 uncertainty。它不会声称镜头已接受、不会生成 digest/ref/receipt，也不包含 provider/model 参数。
