<!-- review-only: 本文件是 prompts/main.en.md 的人工审阅译文，不注册、不参与编译与 digest。变量集合与英文正文一致。 -->

# Cinematique 镜头技术提示词（单技术）

本模板把 Cinematique 技术库（`assets/techniques/`，150 条）中的一条渲染为可直接投递 AI 图像/视频生成器的镜头提示词。消费方选技术、把库内提示词绑定到主体后渲染；渲染结果即最终生成提示词正文，投递后不得改写。

库来源：vvsvs.pro/cinematique（Free Tool — Open Source；上游 grokfilm.app by Tetsuo Corp，VVSVS 混编扩充）。再导出技术内容时保留 `source` 署名块。

## 怎么用

1. 每镜头选一条技术。按分类（运镜/布光/构图/剪辑/叙事/特效/风格）、mood 与叙事意图选；索引在 `assets/index.json`，每条 spec 的 `when_to_use` 与 `common_mistakes` 是选型护栏。`technique_id` 必须是合同 enum 值之一。
2. 绑定主体：取 spec 的 `prompt_template`，把 `[Subject]` 占位替换为 `{{subject}}`（角色/物体/场景描述）。绑定文本即 `technique_prompt_bound`。除替换外不得改动库内提示词——镜头、胶片与灯光语言就是技术本身。
3. 审阅渲染结果时应用 spec 的 `directing_the_ai` 与 `common_mistakes`；它们是本镜头的验收标准，不是装饰。
4. `{{target}}` 声明投递面：`image` 保持单帧静图方向；`video` 额外遵守技术内含的运动语言。

## 技术

技术：`{{technique_name}}`（id：`{{technique_id}}`，分类见索引）。难度与 mood 在技术 spec 中；选型理由应引用 spec 的 `when_to_use`。

## 提示词正文（绑定后的库内提示词）

{{technique_prompt_bound}}

## 消费方指令

投递面：`{{target}}`。附加逐镜头指令：{{extra_directives}}

默认指令（除非 `extra_directives` 覆盖）：逐字保留技术声明的镜头、灯光语言；每镜头一个主导视觉装置；不得把第二条技术的 prompt 片段叠进同一次投递。

## 负面提示词

{{negative_prompts}}

默认负面（除非 `negative_prompts` 覆盖）：杂乱画面、多余肢体、面部畸变、文字、水印、logo、UI 覆盖层；与技术声明的灯光或镜头语言相矛盾的内容。

## 渲染后自检

1. `technique_id` 存在于 `assets/index.json`；绑定提示词与 spec `prompt_template` 逐字一致，仅 `[Subject]` 替换不同。
2. `{{subject}}` 是具体可拍描述；渲染结果中无 `[Subject]` 占位、无未解析模板变量。
3. 恰好一条技术驱动本镜头；`extra_directives` 只调投递参数，绝不是第二条技术的 prompt 文本。
4. 渲染结果仍携带技术的镜头/胶片/灯光语言；未被改写稀释。
5. `target=video` 时技术隐含的运动只声明一次且一致；`target=image` 时丢弃纯运动语言而非与之矛盾。

诚实回退：`technique_id` 不在索引中，或 spec 提示词无法绑定到具体主体时，停止渲染并列出缺口；不得发明技术，不得投递未绑定的 `[Subject]`。
