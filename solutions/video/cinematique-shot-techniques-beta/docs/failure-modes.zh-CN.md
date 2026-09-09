# 失败模式

| 模式 | 症状 | 处置 |
| --- | --- | --- |
| 技术堆叠 | 一个 prompt 里出现两种运镜/布光语言，模型输出混乱 | 回到单主技术约束；第二条技术的需求拆到下一镜头 |
| 主体空洞 | `[Subject]` 绑成形容词堆砌（"a beautiful scene"） | 重写为具体可拍主体（谁、在哪、做什么） |
| 擅自改写 | 绑定时顺手"润色"了镜头/灯光段 | 恢复 spec 原文；改动走 spec 版本变更 |
| 难度错配 | Advanced 技术（Vertigo/One-er）在弱模型上塌成普通镜头 | 降级同意图的 Basic/Intermediate 技术，或换执行模型 |
| image/video 语义冲突 | 静图投递仍带 dolly/pan 运动词 | `target=image` 时丢弃运动语言 |
| enum 漂移 | 新增 spec 后未重放 contract enum，投递被拒 | 跑 reindex 脚本 + `contract input set` 重放 + sync |
| 署名剥离 | 再导出丢 source 块 | 按 provenance 恢复署名再分发 |
