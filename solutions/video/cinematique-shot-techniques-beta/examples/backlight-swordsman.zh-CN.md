# 绑定实例：Backlight × 雨夜剑客（竖屏短剧 EP 开场镜）

选型：EP01 首镜需要「神秘 + 神圣感」的情绪进入，人物尚未露脸。Backlight 的 `when_to_use`（主体从背景分离、光环化）命中；`common_mistakes` 三条（曝光失控/轮廓糊/背景吞没）列入验收。

变量表：

| 变量 | 值 |
| --- | --- |
| technique_id | `backlight` |
| technique_name | `Backlight` |
| subject | a wandering swordsman in a patched rain cloak, standing still in light rain |
| technique_prompt_bound | Backlit a wandering swordsman in a patched rain cloak, standing still in light rain with brilliant rim of white-gold light tracing every contour, hair transformed into a luminous halo of individually backlit strands, atmospheric dust and particles lit up like a galaxy of floating stars, god rays streaming past the figure, shot on a Cooke S4 with gentle halation on the overexposed highlights, the ethereal separation of backlight turning form into something divine |
| target | `video` |
| extra_directives | 4 seconds, 9:16 vertical, slow push-in ending as the subject lifts his head; practical streetlamp as the motivating source |
| negative_prompts | （用默认） |

渲染要点：

- 绑定仅替换了 `[Subject]`；Cooke S4、halation、god rays 原样保留。
- `directing_the_ai` 要求轮廓光来自一个可交代的光源 → extra_directives 指定街灯为 motivated source。
- 验收对照 `common_mistakes`：无全画面过曝、轮廓清晰可辨、背景未吞没人物。

回执：模板 beta 阶段实例；真实出片回执落地后随转正归档。
