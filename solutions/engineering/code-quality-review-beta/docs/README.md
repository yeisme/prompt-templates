# 代码质量审查（beta）

本 solution 面向变更审查。它只生成 provider-neutral 的结构化审查结果，不执行代码修改，也不代表 CI、部署或生产验收已经通过。

入口：

```text
promptrepo://official/engineering/code-quality-review-beta@1.0.0-beta.1?locale=en
```

需要提供变更范围、项目上下文、变更文件或 diff，以及可用的验证观察。没有证据的判断必须保留为未知。
