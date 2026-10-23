# 代码质量模板与 DSH 插件 v1

本变更增加三类代码质量模板和一个本地优先的 DSH 原生插件。模板仓库只拥有可编译 Prompt、contract、schema、fixture 与 recipe；插件只拥有 workspace 探测、只读检查、证据整理和模板编排。插件不自动修改源代码、不调用 Provider、不默认联网。

首版支持 Go、TypeScript/React 和 Python 的安全只读检查；未知语言返回通用审查输入和明确的 `unavailable` 状态。
