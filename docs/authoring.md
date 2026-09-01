# 内容编写指南

每个 solution 是可执行方案包，不是孤立 Prompt。正文应明确：

1. 角色和目标；
2. 必填输入变量；
3. 不可放宽的约束；
4. 输出结构；
5. 自检清单；
6. 无法满足时的诚实回退。

变量使用 `{{variable_name}}`。不要要求模型输出隐藏思维过程；需要解释时，只要求结论、关键证据、风险、权衡和下一步。

成熟度：

- `exploratory`：结构完整但验证有限；
- `first-support`：fixture render、人工评审、rights 和已知失败齐全；
- `mature`：有真实脱敏使用证据和稳定修复记录。

Prompt Markdown 可人工编辑。完成正文后运行 `template-registry solution add ...` 生成或更新 `solution.json`，再运行 catalog build/validate。

需要让 inspect 告诉用户“填什么”时，为实际占位符生成 companion contract。不得手写 JSON；先初始化，再逐字段维护：

```bash
template-registry contract init --repository . --package image --id xhs-product-cover --role main --locale zh-CN --license internal --permission preview --permission execute_requires_review --json
template-registry contract input set --repository . --package image --id xhs-product-cover --role main --locale zh-CN --name product --type string --required --example '便携咖啡杯' --label-zh-CN '产品' --label-en 'Product' --description-zh-CN '需要展示的真实产品' --description-en 'The real product to feature' --json
template-registry contract validate --repository . --package image --id xhs-product-cover --role main --locale zh-CN --json
```

contract input 必须与正文中的 `{{name}}` 一致。example 只能使用公开、虚构、非敏感内容；敏感字段不能声明 default、example 或 enum。
