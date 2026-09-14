# 模板发现与数量口径

本地基线为 52 个方案、111 个语言文档。一个方案可以有多个角色，一个角色也可以保留多个历史语言版本，因此不能用 image 分类的方案数代表全部图像模板。

```bash
template-registry prompt list --media image --locale zh-CN
template-registry prompt list --category image
template-registry prompt list --consumer eikona
template-registry prompt repository list
template-registry catalog audit --repository . --json
python3 scripts/annotate-discovery.py
```

本仓库的 `scripts/annotate-discovery.py` 通过 Template Registry authoring CLI 重放角色用途和适用产品标注，不直接修改 JSON。标注覆盖全部注册文档；人物、服装、背景与环境预览等 video 包角色声明 image 用途。`catalog.discovery` 保存发现信息，不改变英文可编译／中文人工审阅的既有政策。

TemplateRole 与 Solution 旧结构、内容 digest 和精确引用保持不变。用途与 consumer 是目录导航信息，不证明 provider 实拍、生产成熟度、编译资格或费用授权。

`catalog audit` 报告有正文但无注册、有注册但无索引，以及角色发现标注未重建的差异。正文扫描限于 solutions 下 prompts 目录的 Markdown/TXT，docs 中中文译文与 examples 不当作遗漏模板。

本地 build、已同步快照与远端发行是不同状态。列表显示来源和更新时间；未同步、权限不足、旧服务缺能力时必须保留具体原因，不能以本地源码数量宣称远端已发布。
