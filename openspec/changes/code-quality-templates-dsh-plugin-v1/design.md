# 设计

## Owner

- `data/yeisme-prompt-templates`：内容与公共 promptrepo contract。
- `backend-server/template-registry`：复用现有 discovery、session、compile、recipe 和 recovery，不新增领域状态。
- `cli/dsh-code-quality`：独立 DSH JavaScript 插件和本地只读检查适配器。

## 安全边界

插件以当前 workspace 为根，拒绝路径穿越、隐藏敏感目录、symlink escape 和任意 shell 字符串。检查命令使用参数数组，默认禁用网络，缺失依赖返回 `unavailable`。默认输出只包含相对路径、行号、摘要、证据 ID、digest 和命令状态，不包含源码正文、凭据、Provider payload 或完整推理。

## 模板数据流

`code-quality-review-beta` 生成 findings；`code-quality-test-gap-beta` 通过 `step_output` 消费 review；`code-quality-refactor-plan-beta` 消费 review 与 test-gap。每个模板都以 `en` 注册，中文只作人工审阅译文。

## 插件行为

插件注册 `code_quality_status`、`code_quality_review`、`code_quality_verify` 和 `code_quality_fix_plan`。review 和 verify 只读；fix-plan 只生成需要确认的计划。v1 不提供 apply。
