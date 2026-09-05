# Locale 政策：英文编译模板与中文审阅译文

## 统一规则

- 官方仓库的 `default_locale` 为 `en`。
- 所有新建、可由 Agent 编译或投递给模型的 solution，只注册 `prompts/<role>.en.md`，只为 `en` 维护 companion contract。
- 中文翻译放在 `docs/template-zh-CN.md`，用于产品、内容和领域 owner 的人工审阅。它不是模板，不注册进 `solution.json` 的 `templates`，不进入 catalog template 列表，也不参与编译结果或内容 digest。
- `solution.json.locales.zh-CN` 可以保留中文标题、摘要、用法和搜索别名；这些是 catalog 展示文本，不代表存在中文可编译模板。
- 已发布的双语 exact ref 保留解析兼容性。新文档、Skill、CLI 默认值和示例只使用 `locale=en`，不得继续把旧 `zh-CN` ref 当作推荐入口。

## 三层语言分别处理

1. **模板骨架语言**固定为英文，即注册的 `prompts/<role>.en.md`。
2. **变量内容语言**由消费方填入的值决定。英文骨架可以绑定中文资料、中文产品事实或日文场景描述。
3. **最终产物语言**由 `output_language`、`dialogue_language`、`voiceover_script` 等显式输入决定，与模板 locale 分离。

因此，“Agent 使用英文模板”不等于“产物必须是英文”。模板负责稳定指令和结构，字段负责真实内容及目标语言。

## 新建方案

推荐目录：

```text
solutions/<package>/<solution>/
  prompts/
    main.en.md
  contracts/
    main.en.json
  docs/
    template-zh-CN.md
    README.md
  solution.json
```

结构化 metadata 必须由 Template Registry CLI 生成：

```bash
template-registry solution add --repository . --package <package> --id <solution> --version 1.0.0 --category <category> --locale en --title '<English title>' --summary '<English summary>' --prompt solutions/<package>/<solution>/prompts/main.en.md --role main --json
template-registry solution locale describe --repository . --package <package> --id <solution> --locale zh-CN --title '<中文标题>' --summary '<中文摘要>' --usage '<中文用法>' --json
template-registry contract init --repository . --package <package> --id <solution> --role main --locale en --license <license> --permission preview --json
template-registry catalog build --repository . --json
template-registry catalog validate --repository . --json
```

`docs/template-zh-CN.md` 头部必须包含：

```markdown
> 人工审阅译文。编译与 Agent 投递以 `../prompts/main.en.md` 为准；本文件不注册为模板、不进入 catalog，也不参与编译。
```

## 译文等价性

中文译文应逐节对应英文模板，并保持变量名、约束、输出结构、安全边界和失败条件一致。英文正文变化后，应同步更新中文审阅文档；中文译文不能反向改变 contract、稳定 ID 或编译语义。

自动翻译只能作为待审草稿。未完成人工校对时，应明确标注，不得把它写成已验证的正式译文。

## 旧双语方案迁移

移除已发布 locale 属于兼容变更，必须先确认消费记录和替代版本。未发布方案可以在首次发行前使用 CLI 收口：

```bash
template-registry solution locale remove --repository . --package <package> --id <solution> --locale zh-CN --json
template-registry solution locale describe --repository . --package <package> --id <solution> --locale zh-CN --title '<中文标题>' --summary '<中文摘要>' --usage '<中文用法>' --json
```

随后把孤立的 `prompts/<role>.zh-CN.md` 移到 `docs/template-zh-CN.md`，删除孤立中文 contract，再运行 `catalog build` 和 `catalog validate`。已发布旧版本不原地删改，改由新版本采用统一结构。

## 例外

结构化 Graph Kit、UI review fragment 或历史 fixture 可能仍以 `zh-CN` 表示来源资料或展示界面。这些专用合同不自动获得 Agent 提示词编译资格。若要进入通用提示词编译链，必须提供并注册等价的 `en` 模板。
