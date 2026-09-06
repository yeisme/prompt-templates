# ICONIC LANDMARK SERIES 城市地标海报

> 本文档是人工审阅译文，不进入编译。编译与投递只使用 `main.en.md`。

本模板生成一张「上半真实摄影 + 下半矢量解构 + 建筑档案排版」的城市地标海报 Prompt，属于固定视觉系统 ICONIC LANDMARK SERIES。城市差异全部通过变量绑定注入；消费方在渲染前完成全部变量绑定，渲染结果是最终 Prompt 正文，不经过二次改写。城市 spec、变体合并与系列索引由消费侧渲染器（Eikona iconic-landmark 海报导演技能）负责，本模板只定义单张海报正文结构。

创建一张竖版 {{aspect}} 高级城市地标建筑艺术海报，主题为{{city_name}}，核心地标为 {{landmarks_line}}。

延续统一的 ICONIC LANDMARK SERIES 视觉系统：上半部分真实城市摄影 + 下半部分极简二维矢量建筑解构插画。上下两部分必须表现同一组地标，并具有明显的视觉对应关系。

## 上半部分｜真实摄影（约占 45%）

{{viewpoint}}。
{{hero_placement}}。
清晰表现标志性的：{{hero_features}}。
{{skyline}}。
{{river}}。
{{scale_reference}}。
{{background}}。
时间设定：{{time}}。天空形成{{sky_gradient}}。{{clouds}}。{{rim_light}}。
{{lens}}。
{{quality}}。

## 下半部分｜建筑矢量解构（约占 55%）

背景转换成温暖象牙白、奶油白高级艺术纸张，大面积干净负空间。将上半部分真实建筑重新设计成极简二维矢量插画。hero 地标仍位于视觉中心偏右，与上方真实摄影保持相似视觉轴线。

必须严格保留最核心的识别元素：{{hero_identity}}。
{{hero_simplification}}。
主体使用：{{hero_palette}}。

{{supporting}}。使用低饱和：{{supporting_palette}}。

{{sun}}。

{{river_lines}}。
{{easter_egg}}。
{{feel}}。

## Typography｜建筑档案排版

左下方使用大写英文：

{{title_line1}}

第二行：

{{title_line2}}

使用高级现代主义无衬线字体，细字重，明显增加字母间距。主标题使用深海军蓝 / Charcoal Navy。下方极细短横线。小字号：{{subtitle}}。

左上角极小字号：

ICONIC
LANDMARK
SERIES

—

No.{{series_no}}

右上角：

EST.
{{est}}

右下角：

{{coordinates}}

最下方极小字号：{{footer}}。

所有字体遵循建筑事务所档案、博物馆展览图录式排版。

## 最终风格

Swiss International Style + British modernism + Bauhaus + Mid-century travel poster + architectural editorial illustration + museum exhibition graphic design + Japanese minimalism + Scandinavian graphic design。

温暖象牙白纸张，大面积留白，精准网格系统，超细线条，低饱和莫兰迪配色，建筑比例准确。上半真实摄影，下半二维矢量解构，上下地标严格对应。高级、克制、安静、建筑杂志感、博物馆收藏海报质感。4K，ultra clean vector edges，premium print design，museum quality，collector's architectural poster。

## 负面提示词

赛博朋克、未来城市、3D渲染、黏土风、油画、水彩、粗黑描边、过度饱和、强HDR、建筑透视错误、密集游客、大量汽车、杂乱背景、文字乱码、{{negative_extra}}。

## 自检清单

- 上下两半表现同一组地标，hero 视觉轴线一致。
- 矢量半保留 hero 全部核心识别元素，无粗黑描边。
- supporting 建筑高度明显低于 hero。
- 排版五个槽位齐全（系列编号、城市大字、EST、坐标、脚注）。
