# style-scene-pairing-beta

全球"风格 × 场景 × 主题"配对编译模板：以 Southern Gothic 为参照方法论（风格必须扎根地方现实），把创作地理单元与场景事实编译为——合理性分级（NATIVE_OR_HISTORIC / REGIONAL_DERIVATIVE / TRANSCULTURAL_VISUAL）、敏感性检查（原住民信仰/殖民史/墓葬圣地不得恐怖化）、主提示词与混合风格变体、置信分级（A/B/C/Review）。固化 32 风格 × 4 族受控词表、匹配分公式（含文化误读硬门槛）、UNESCO 优先的扩展种子顺序与 S–D 来源分级。

- 编译模板（Agent/模型消费）：`../prompts/main.en.md`
- 中文阅读版（人工审阅，不进编译）：`template-zh-CN.md`
- 使用指南：`usage.zh-CN.md`
- 已知失败模式：`failure-modes.zh-CN.md`
- 绑定实例：`../examples/savannah-southern-gothic.zh-CN.md`

Exact ref：

```text
promptrepo://official/image/style-scene-pairing-beta@1.0.0-beta.1?locale=en
```

家族边界：风格已定时直接用各风格层模板（`southern-gothic-style-beta`、`xianxia-hazy-fantasy`…）渲染；视频侧把本模板产出的风格线索填入 `video-prompt-optimization-beta` 的 `style_requirements`。320 地理单元批量主表属数据层，参照 `iconic-landmark-poster` / `candid-portrait-matrix` 的 spec 模式另建，不在本模板。
