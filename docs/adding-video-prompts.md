# 添加视频提示词内容：决策指南

面向所有 Agent：往模板仓库加视频生成类内容时，先选对层级，再按对应食谱执行。不要新建平行的提示词存放点。图像侧对应文档见 `adding-image-prompts.md`。

## 决策树

```text
要加什么？
├─ 现有模板的一次具体使用（人物/场景/技能都确定的实例）
│   → 不写模板：在对应 solution 的 examples/ 加一个绑定实例文档
├─ 现有模板对新 Provider 的兼容（横幅、引用语法、槽位规则）
│   → 只改 examples/ 和该 solution 的 usage「Provider 兼容」节
├─ 现有模板缺一个参数维度（如帧率、平台横幅）
│   → 给模板加 {{variable}} + contract input set（enum 收束取值）
├─ 一种结构上不同的新场景（约束模型/声音模型/人物数量不同）
│   → 新 solution：solutions/video/<id>/，食谱见下文
└─ 跨图片+视频+剪辑的联动工作流
    → 先用 template-registry-integration-designer 分类，再决定进模板/Skill/recipe
```

「结构上不同」的判据（本仓库已验证的拆分裂点）：声音模型（无台词 / 画外 VO / 出镜台词）、人物数量与身份锁（单人 / 双人锁定）、约束核心（特效配比 / 物理攻防 / 唇形同步 / 一致性锁定）。仅风格、场景、时长不同不构成新 solution。

## 现有视频生成家族（复用前先查这张表）

| 需求 | Solution | 结构特征 |
| --- | --- | --- |
| 特效/法阵/大招清屏镜头 | `ai-drama-shot-video-generation` | 蓄力-爆发两层约束、特效配比、安全协议 |
| 无台词纯环境音抓拍 vlog | `realistic-vlog-shot-generation` | 一致性锁定 + 节拍序列 + 不完美质感 |
| 画外 VO 自述 + 音乐弧线 | `realistic-docu-vlog-generation` | VO 绑定键、音乐弧线、混合机位 |
| 出镜口播 + 唇形同步 | `realistic-diary-vlog-generation` | 台词脚本、声学空间、服装逻辑链 |
| 双人物写实格斗 | `realistic-fight-scene-generation` | 双参考图锁、攻防物理、行动轴线 |
| 穿搭拼贴首帧 + 卡点换装 | `outfit-collage-transition-director` | 图为视频母图、机制库、五节输出协议 |

## 食谱 A：新实例（最常用）

在 `solutions/video/<id>/examples/<case>.zh-CN.md` 写绑定实例：完整变量值表 + 时间线/节拍 + 渲染与投递注意点。实例不进 catalog，可人工编辑。参照 `realistic-vlog-shot-generation/examples/friend-travel-day.zh-CN.md`。

## 食谱 B：Provider 兼容

1. 只改 `examples/` 和 usage 的「Provider 兼容」节。
2. 平台标识行走 `provider_banner` 变量；资产引用语法差异用 contract regex 兼容（`@uuid` 与 `@image1` 位置引用都接受）。
3. 不复制 solution，不新建带 Provider 名的模板 ID。

## 食谱 C：模板加变量

1. 改 `prompts/main.en.md` 加入 `{{variable}}`。
2. `contract refresh`（重建正文绑定）→ `contract input set`（新变量，enum 只收稳定 machine ID）→ `contract validate`。
3. 同步 `docs/template-zh-CN.md` 阅读版（变量集合必须与英文正文一致）。
4. 涉及移除/改义的变量按 `yeisme-evolutionary-change-policy` 处理。

## 食谱 D：新 solution

前置确认：裂点符合「结构上不同」判据，且家族表中没有可复用项。

1. 按 `template-registry-template-author` skill 的新建流程：`prompts/main.en.md`（唯一注册模板）+ `docs/template-zh-CN.md`（阅读版）+ `docs/README.md`。
2. CLI 链：`solution add`（en）→ `solution locale describe`（zh-CN 显示文本）→ `solution tag set` / `solution capability set` → `contract init` + 逐变量 `contract input set` + `contract validate`。
3. tags 遵循 `taxonomy.md`：`category:video` + `job:generate` + `stage:*` + `artifact:*` + `constraint:*`；新 namespace 值只在确有需要时引入，模型名/Provider 名不进 tag。
4. 文档三件套：usage（含家族选择矩阵更新）、review-checklist、failure-modes；一个 examples 绑定实例。
5. 更新本文件的家族表与各 solution usage 里的选择矩阵。

## 通用硬规则

- 模板正文只注册 `en`；中文阅读版放 `docs/template-zh-CN.md`，不注册、不进 digest、不被 render。
- 结构化元数据（solution.json、contract、catalog.json）一律由 template-registry CLI 生成，禁止手写。
- 编译器对未绑定变量和残留 `{{}}` 必须 fail-closed；新增 solution 后跑占位符冒烟（正文与阅读版变量集合一致）。
- 非正式版本带 `beta`/`alpha` 标识；正式版本无后缀、从 `1.0.0` 起版。

## 验证闭环

```bash
(cd backend-server/template-registry && go run ./cmd/template-registry catalog build --repository ../../data/yeisme-prompt-templates --json)
(cd backend-server/template-registry && go run ./cmd/template-registry catalog validate --repository ../../data/yeisme-prompt-templates --json)
(cd data/yeisme-prompt-templates && openspec validate --all --strict --no-interactive)
```
