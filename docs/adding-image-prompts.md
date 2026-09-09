# 添加图像提示词内容：决策指南

面向所有 Agent：往这套体系里加图像提示词内容时，先选对层级，再按对应食谱执行。不要新建平行的提示词存放点。

## 决策树

```text
要加什么？
├─ 一个具体镜头（人物/场景/机位/光线都确定，一次性内容）
│   → shot spec：.skills/yeisme/eikona-image/eikona-precision-candid-director/assets/shots/<id>.json
│   → 渲染器绑定 precision-candid-shot 模板出 prompt
├─ 一个可复用风格层（风格段固定，只换人物/场景等少数变量）
│   → 模板仓库新包：solutions/image/<id>/（参考 xianxia-hazy-fantasy）
├─ 一个系列视觉系统下的新成员（城市/主题变体，版式固定）
│   → 系列 spec：如地标海报的 assets/cities/<city>.json 或 variants
├─ 一个批量候选池的新维度取值
│   → 矩阵取值：candid-photo 技能的 scripts/matrix.json + 模板仓库 contract 枚举同步
└─ 一种全新结构（现有槽位都装不下）
    → 模板仓库新包 + 必要时新 director 技能；先读 docs/authoring.md
```

## 通用硬规则

- 模板正文只注册 `en`（Agent 编译/投递用）；中文译文放包内 `docs/template-zh-CN.md`，不注册、不进 digest。
- `solution.json`、`catalog.json`、contract、fixture 等结构化元数据一律由 template-registry CLI 生成，禁止手写。
- 镜头/城市/矩阵数据 spec 是 JSON 源内容，可以人工编辑；manifest、tags、runbook、系列索引由技能脚本生成，禁止手写。
- 编译器对未绑定变量和残留 `{{}}` 必须 fail-closed。
- 非正式版本必须带 `beta`/`alpha` 标识；正式版本无后缀、从 `1.0.0` 起版（见根 AGENTS.md 版本命名条）。

## 食谱 A：新镜头（最常用）

1. 复制 `assets/shots/` 下任一现有 spec，改写字段；schema 见技能 `references/shot-spec.md`。
2. 语法规则：description 以主体名词收尾时 pose 用分词（standing/leaning…），否则 pose 用 `as she …` 从句。
3. tags：`use`（用途）、`mood`（情绪）、`theme`（资产组，如 xianxia/headshot/ritual/street）必填前两类，theme 尽量复用既有值。
4. 渲染验证：

   ```bash
   python3 .skills/yeisme/eikona-image/eikona-precision-candid-director/scripts/render_shot.py \
     --shot <id> --out <skill>/examples/<id>
   ```

5. 出图必须 dry-run 确认后再真实生成；交付走 `feedback accept` → `assets apply`。

## 食谱 B：可复用风格层

参考 `solutions/image/xianxia-hazy-fantasy`：固定风格段 + 极少变量（persona/scene/可选增强段）。

```bash
template-registry solution add --repository data/yeisme-prompt-templates --package image \
  --id <style-id> --version 1.0.0 --category image --rights internal --maturity exploratory \
  --locale en --title '<English title>' --summary '<summary>' --usage '<usage>' \
  --role main --prompt-path solutions/image/<style-id>/prompts/main.en.md --json
template-registry contract init --repository data/yeisme-prompt-templates --package image \
  --id <style-id> --role main --locale en --license internal \
  --permission execute_requires_review --permission preview --json
template-registry contract input set ...   # 每个变量一次
template-registry contract refresh ... && catalog build && catalog validate
```

## 食谱 C：地标系列新城市 / 变体

- 新城市：复制 `eikona-iconic-landmark-poster-director/assets/cities/london.json`，改内容，跑 `render_poster.py --reindex`（检查 series.no 冲突）。
- 同城变体：在城市 spec 的 `variants` 数组加条目（dict 深合并，negative_extra 追加合并）。

## 食谱 D：矩阵新取值

1. 改 `eikona-candid-photo-director/scripts/matrix.json`（取值池 + 兼容规则键值同步）。
2. 同步 `references/matrix.md` 与 `compatibility.md`（人类审阅文档）。
3. 用 `contract input set` 重刷模板仓库 candid-portrait-matrix 的对应枚举。
4. `sample_matrix.py --dry-run` 验证采样与兼容约束。
