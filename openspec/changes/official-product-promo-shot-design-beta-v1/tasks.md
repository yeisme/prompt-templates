# 实施与验收任务

由 scripts/openspec-tasks.py 维护状态。

- [x] content Author English brief/shot-plan templates, Chinese review document and video-shotcraft canary guide | evidence: English brief/shot-plan templates, Chinese review docs and pinned video-shotcraft integration guide authored
- [x] metadata Generate the solution, contracts, output schemas, document descriptors, tags, capabilities and recipe through Template Registry CLI | evidence: Registry CLI generated two contracts, two schemas/descriptors, tags, capabilities, two valid fixtures and recipe digest sha256:7f7fe74c6faecb1a9c9ea0c8586ed96839f8a547c923d805b3684ea84fde177f
- [x] validation Build/validate the catalog and run a provider-free two-step session canary | evidence: 41-solution catalog sha256:d87c97fc8a3cedebeb23f5138ee0d288bbdd41f41db3ddd2f8f34289e2d279f3, 19 strict OpenSpec items and zero-provider two-step package canary passed
