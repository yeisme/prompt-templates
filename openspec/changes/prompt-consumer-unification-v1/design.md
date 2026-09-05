## Context

五个 Go 消费者已使用 promptrepo，但兼容能力和文档入口不一致。Digital Human 是 Python Persona Package owner，适合消费 Registry 导出的提示词文件，不应复制 promptrepo 或 Registry 编译器。

## Goals / Non-Goals

提供缺失的官方消费方案；不移动领域运行时提示、provider instruction、镜头语法或 Persona 生命周期。

## Decisions

修订模板声明 `revision,text,writing`，输出仍进入 Auctra review。Persona 模板声明 `agent,dialogue,persona,text`，由 Template Registry 完成确认和编译，再以单提示词文件进入 Persona 源目录。两个模板均为 internal rights、execute_requires_review、exploratory。

`xhs-product-cover@1.0.0` 已有公开精确引用，不能原地扩大能力声明。因此新增 `xhs-product-cover-v2@2.0.0`，声明 `generation,image,visual,visual_composition`；Eikona 使用新引用，旧引用继续可验证和回滚。

## Risks / Trade-offs

结构和离线渲染通过不证明所有文体、模型或实时数字人场景有效。英文内容保持适配稿，后续以领域效果证据晋级。

## Migration Plan

只新增 immutable solution，无旧引用迁移。消费者显式选择新 ref；回滚时停止选择即可，v1 仍保留。
