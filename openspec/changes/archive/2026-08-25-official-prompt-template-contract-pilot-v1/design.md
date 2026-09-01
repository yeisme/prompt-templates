## Pilot boundary

首个 image pilot 选择 `xhs-product-cover`，因为它同时覆盖三个必填 string、两个有默认值的 enum、中文优先正文和英文同步适配。随后加入 `podcast-narration` 作为 Sonora 首个 audio canary，覆盖五个必填 string、一个 sensitive 长文本输入和 provider-free preview output。

sidecar 路径：

```text
solutions/image/xhs-product-cover/contracts/main.zh-CN.json
solutions/image/xhs-product-cover/contracts/main.en.json
solutions/audio/podcast-narration/contracts/main.zh-CN.json
solutions/audio/podcast-narration/contracts/main.en.json
```

字段合同：

| name | type | required/default | purpose |
| --- | --- | --- | --- |
| `product` | string | required | 真实产品 |
| `audience` | string | required | 目标受众 |
| `selling_point` | string | required | 可核实卖点 |
| `visual_style` | enum | default `clean_commercial` | 视觉方向 |
| `aspect_ratio` | enum | default `3:4` | 封面画幅 |

Template Registry CLI 从 Prompt 文件计算 `template_digest`，再为 sidecar 计算独立 digest。正文变化会使 `contract validate` fail closed；新增 sidecar 不参与 catalog build，因此 catalog digest 不漂移。

音频字段合同：

| name | type | required | sensitivity | purpose |
| --- | --- | --- | --- | --- |
| `audience` | string | yes | public | 目标听众 |
| `duration` | string | yes | public | 目标时长 |
| `script` | string | yes | sensitive | 原始旁白稿件 |
| `show_positioning` | string | yes | public | 节目主题与价值定位 |
| `tone` | string | yes | public | 表达语气 |

## i18n

machine name、type、enum 和 permission 保持英文稳定值。中文 sidecar 是 source contract；英文 sidecar 使用相同字段合同和英文 example，但保留中英文 labels/descriptions，便于中文用户切换英文模板时继续获得中文填空说明。

## Safety

- sidecar 不包含真实用户输入。
- sensitive `script` 不声明 default、example 或 enum；Sonora canary 只输出 `provided/missing/invalid` 状态。
- example 是公开、虚构、非敏感内容。
- `execute_requires_review` 只是 metadata；Eikona 等领域 owner 仍负责模型、费用、权限、run evidence 和资产生命周期。
- Prompt body 不进入 maintainer JSON 输出、测试 evidence 或 catalog。
