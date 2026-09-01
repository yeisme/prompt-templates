## 1. 阶段合同与官方样例

- [x] 1.1 更新中文 Prompt 与 task modules，明确 face、body、主视图、派生视图的依赖和单图 production 语义
- [x] 1.2 使用 Template Registry authoring 命令新增 face-master 与 body-master valid fixtures
- [x] 1.3 使用 Template Registry authoring 命令把 turnaround fixture 正规化为独立 artifacts，并保留旧 profile 兼容说明
- [x] 1.4 增加元 Prompt 直发、production grid、缺失 accepted upstream ref 等 invalid fixtures/reason codes

## 2. 文档与人工审稿

- [x] 2.1 更新 preset matrix、usage、review checklist 与 failure modes，写明“脸模先定版、主视图通过后再生成侧背图”
- [x] 2.2 更新 2026-08-31 测试指南，把旧三视图真实运行标记为执行设计失败证据，并给出新的逐阶段测试顺序
- [x] 2.3 同步英文 reviewed adaptation，保持 stable IDs 与约束等价

## 3. 验证与交接

- [x] 3.1 运行 Character contract/fixture 与 catalog provider-free validation
- [x] 3.2 运行 OpenSpec strict validation并记录 Eikona consumer 聚焦证据路径
- [x] 3.3 完成 content review，确认 Prompt正文、fixtures、日志与证据均不含 credential、Provider payload 或隐藏指令
