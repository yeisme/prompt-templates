# AI 做剧官方模板测试与今日状态（2026-08-31）

最后核对时间：2026-08-31 04:50 UTC。

## 今日结论

当前工作区里的两套官方模板可以用于本地集成、合同校验和 provider-free consumer 测试：

- `video/ai-drama-character-assets@1.0.0`：角色资产 Prompt、JSON/YAML 任务和模块化模板可由 Eikona、Scaena 确定性消费；
- `video/ai-drama-storyboard-breakdown@1.0.0`：主分镜与 bounded repair 可由 Scaena 确定性编译和校验；
- 两项 OpenSpec change 均为 `Complete`；
- catalog 含 14 个 solution，当前 digest 为 `sha256:f2ee99e6316530669753907f603a72bffaeb8d3d4d8178c3d7384d837c355122`；
- 两套 solution 均保持 `rights=internal`、`maturity=exploratory`。

2026-08-31 已完成两次 Eikona 真实 Provider 调用：通用 character-reference canary 成功；旧版官方 Character canary 也生成了 1 张候选图。两次成功调用的已确认费用合计为 0.054645 美元。

这不等于已经 production-ready。复盘确认，旧版官方 Character canary 把要求输出 Prompt Bundle JSON 的编译元 Prompt 直接发送给了图片 Provider，绕过了 `views[]` 的单图语义。该 run 只能证明 Provider 链路可调用，不能证明官方角色资产执行设计正确。候选图也没有通过三视图资产验收。Scaena 真实分镜模型仍未配置；项目没有完成 commit、tag、push 或 publish。其他环境不能把这个工作区状态当成已发布的 immutable `1.0.0`。

## 今日证据

| 检查项 | 结果 | 关键数据 |
| --- | --- | --- |
| OpenSpec | 通过 | 两项 change 均为 `Complete` |
| Template Registry catalog | 通过 | 14 solutions；digest 为 `sha256:f2ee…5122` |
| Character fixture | 通过 | 29 cases：6 valid、23 invalid；新增 face master、body master、独立 turnaround，以及元 Prompt 直发/多宫格/缺主视图负例；provider calls=0 |
| Eikona character canary | 通过 | 旧三视图拆为 3 个单图 jobs；face/body stage gate、表情矩阵、repair 和本地 contact sheet 顺序通过 |
| Scaena character canary | 通过 | 6 modules；single/modular task 与 bundle digest 相等；provider calls=0 |
| Scaena storyboard main | 通过 | 16 cases：6 valid、10 invalid；provider calls=0 |
| Scaena storyboard repair | 通过 | 3 cases：2 valid、1 invalid；bounded repair=true |
| Eikona 本地 main preview | 通过 | `ready=true`；7294 bytes；provider calls=0；durable writes=0 |
| Scaena exact-address inspect | 通过 | `ready=true`；rights=`internal`；provider calls=0 |
| Eikona 通用真实 canary | 通过 | 1 image；模型 `openai/gpt-5.4-image-2`；费用 0.0246 美元 |
| Eikona 旧版官方 Character canary | Provider 调用成功、执行设计与质量均未通过 | 元 Prompt 被错误直发；1 artifact；1024×1024；费用 0.030045 美元；第三格不是背面 |
| Scaena 真实分镜模型 | 未执行 | `storyboard_model=disabled`；token source 缺失；owner adapters disconnected |

标准证据目录：

- Eikona Character：`cli/eikona/temp/integration-test-runs/integration-20260831T014141.617746981Z/`；
- Eikona staged Character：`cli/eikona/temp/integration-test-runs/integration-20260831T045023.103995218Z/`；
- Eikona 通用真实 canary：`cli/eikona/temp/integration-test-runs/integration-20260831T033811.072375199Z/`；
- Eikona 官方 Character 失败尝试：`cli/eikona/temp/integration-test-runs/integration-20260831T034836.828176950Z/`；
- Eikona 官方 Character 成功尝试：`cli/eikona/temp/integration-test-runs/integration-20260831T034934.031397588Z/`；
- Scaena Character：`agent/scaena/temp/integration-test-runs/20260831-013932.027586444-system-3318703-1/`；
- Scaena Storyboard：`agent/scaena/temp/integration-test-runs/20260831-014817.682201358-system-3378671-1/`。

## 一、五分钟离线验收

这些命令不调用图片或文本 Provider。

先确认本机已有 Go、Task、jq 和 OpenSpec CLI：

```bash
go version
task --version
jq --version
openspec --version
```

### 1. 查看 OpenSpec 状态

```bash
cd /workspaces/yeisme-agent/data/yeisme-prompt-templates
openspec list
openspec validate --all --strict
```

预期看到：

```text
Changes:
  official-ai-drama-storyboard-breakdown-templates-v1     ✓ Complete
  official-ai-drama-character-asset-templates-v1          ✓ Complete
```

### 2. 验证 catalog

当前 Template Registry 需要同时绑定本地 `shared/promptrepo`。下面的临时 Go workspace 只用于本次命令，不修改仓库配置：

```bash
cd /workspaces/yeisme-agent

REGISTRY_WORK=$(mktemp -d)
(
  cd "$REGISTRY_WORK"
  go work init \
    /workspaces/yeisme-agent/backend-server/template-registry \
    /workspaces/yeisme-agent/shared/promptrepo
)

(
  cd /workspaces/yeisme-agent/backend-server/template-registry
  GOWORK="$REGISTRY_WORK/go.work" \
    go run ./cmd/template-registry catalog validate \
      --repository ../../data/yeisme-prompt-templates \
      --json
)
```

预期：`status=success`、`solution_count=14`，digest 与本页记录一致。

### 3. 测试 Eikona Character consumer

```bash
cd /workspaces/yeisme-agent/cli/eikona
task test:integration:official-character-asset-canary
```

该测试覆盖：

- single-file JSON/YAML canonical 等价；
- Character、Wardrobe、Task、Layout、QC 与 plan 模块化编译；
- 三视图、表情矩阵和 3×2 contact sheet 顺序；
- duplicate YAML key、YAML alias、身份漂移、服装漂移等稳定错误码；
- provider calls=0。

查看最新证据：

```bash
cd /workspaces/yeisme-agent/cli/eikona
ls -dt temp/integration-test-runs/integration-* | head -1
```

### 4. 测试 Scaena Character 与 Storyboard consumer

```bash
cd /workspaces/yeisme-agent/agent/scaena

task test:integration:official-character-asset-canary
task test:integration:storyboard-breakdown
```

Storyboard 测试应得到：

- main：6 valid、10 invalid；
- repair：2 valid、1 invalid；
- `unknown-fact` 精确返回 `CLAIM_EVIDENCE_MISSING`；
- bounded repair 不改写未受影响的 shots；
- provider calls=0。

查看最新证据：

```bash
cd /workspaces/yeisme-agent/agent/scaena
ls -dt temp/integration-test-runs/* | head -3
```

## 二、实际加载并预览 Character Prompt

下面的 smoke 使用临时 XDG 目录，不会覆盖现有 Promptrepo 用户配置。它读取官方 fixture，为 main contract 填充 11 个输入，并执行只返回 digest/size 的本地 preview。

```bash
SMOKE_ROOT=$(mktemp -d)
export XDG_CONFIG_HOME="$SMOKE_ROOT/config"
export XDG_CACHE_HOME="$SMOKE_ROOT/cache"

CONTENT_ROOT=/workspaces/yeisme-agent/data/yeisme-prompt-templates
EIKONA_ROOT=/workspaces/yeisme-agent/cli/eikona
FIXTURE="$CONTENT_ROOT/solutions/video/ai-drama-character-assets/fixtures/main.zh-CN/wuxia-female-turnaround.input.json"

cd "$EIKONA_ROOT"

go run ./cmd/eikona --json --output-root "$SMOKE_ROOT/evidence" \
  prompt-asset repository add \
  --id official \
  --source "file://$CONTENT_ROOT" \
  --trust trusted

go run ./cmd/eikona --json --output-root "$SMOKE_ROOT/evidence" \
  prompt-asset repository sync --id official

go run ./cmd/eikona --json --output-root "$SMOKE_ROOT/evidence" \
  prompt-asset catalog resolve \
  'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=zh-CN' \
  > "$SMOKE_ROOT/character-resolve.json"

CHARACTER_ADDRESS=$(jq -r \
  '.data.solution.templates[] | select(.role=="main" and .locale=="zh-CN") | .address' \
  "$SMOKE_ROOT/character-resolve.json")

go run ./cmd/eikona --json --output-root "$SMOKE_ROOT/evidence" \
  prompt-asset catalog preview "$CHARACTER_ADDRESS" \
  --set "asset_profile_id=$(jq -r '.asset_profile_id' "$FIXTURE")" \
  --set "continuity_constraints_json=$(jq -c '.continuity_constraints' "$FIXTURE")" \
  --set "locale=$(jq -r '.locale' "$FIXTURE")" \
  --set "output_schema_version=$(jq -r '.output_schema_version' "$FIXTURE")" \
  --set "reference_bindings_json=$(jq -c '.reference_bindings' "$FIXTURE")" \
  --set "schema_version=$(jq -r '.schema_version' "$FIXTURE")" \
  --set "style_lens_summary=$(jq -r '.style_lens_summary' "$FIXTURE")" \
  --set "subject_json=$(jq -c '.subject' "$FIXTURE")" \
  --set "subject_version_ref=$(jq -r '.subject_version_ref' "$FIXTURE")" \
  --set "task_json=$(jq -c '.task' "$FIXTURE")" \
  --set "wardrobe_json=$(jq -c '.wardrobe' "$FIXTURE")" \
  > "$SMOKE_ROOT/character-preview.json"

jq '{
  status,
  ready: .data.preview.ready,
  rendered_digest: .data.preview.rendered_digest,
  rendered_bytes: .data.preview.rendered_bytes,
  provider_calls: .data.preview.provider_calls,
  durable_writes: .data.preview.durable_writes
}' "$SMOKE_ROOT/character-preview.json"
```

2026-08-31 实测结果：

```json
{
  "status": "success",
  "ready": true,
  "rendered_digest": "sha256:4f9450c508dcc002f20491d4fa05ec8e98548a3f109c385a824cd7a20620cf4d",
  "rendered_bytes": 7294,
  "provider_calls": 0,
  "durable_writes": 0
}
```

这一步只证明 Prompt 可解析、输入完整且渲染确定，不会生成图片。

## 三、用 Scaena 检查 Storyboard 模板

继续使用上一节的临时 XDG 配置。Eikona 当前可以把 solution ref 解析成含 path、digest 与 snapshot 的 exact address；Scaena 再以该地址执行只读 inspect。

```bash
CONTENT_ROOT=/workspaces/yeisme-agent/data/yeisme-prompt-templates
EIKONA_ROOT=/workspaces/yeisme-agent/cli/eikona
SCAENA_ROOT=/workspaces/yeisme-agent/agent/scaena

cd "$EIKONA_ROOT"

go run ./cmd/eikona --json --output-root "$SMOKE_ROOT/evidence" \
  prompt-asset catalog resolve \
  'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=zh-CN' \
  > "$SMOKE_ROOT/storyboard-resolve.json"

STORYBOARD_ADDRESS=$(jq -r \
  '.data.solution.templates[] | select(.role=="main" and .locale=="zh-CN") | .address' \
  "$SMOKE_ROOT/storyboard-resolve.json")

cd "$SCAENA_ROOT"

go run ./cmd/scaena \
  prompt-asset catalog inspect "$STORYBOARD_ADDRESS" \
  --json \
  > "$SMOKE_ROOT/storyboard-inspect.json"

jq '{
  status,
  ready: .data.ready,
  rights: .data.rights,
  trust: .data.trust,
  digest: .data.digest,
  provider_calls: .data.provider_calls
}' "$SMOKE_ROOT/storyboard-inspect.json"
```

2026-08-31 实测得到 `ready=true`、`rights=internal`、`provider_calls=0`。

## 四、真实 Provider 实测

### 1. Eikona 就绪检查

以下检查不会生成图片：

```bash
cd /workspaces/yeisme-agent/cli/eikona

go build -trimpath -o dist/eikona ./cmd/eikona
./dist/eikona config inspect --agent
./dist/eikona auth check openai --agent
./dist/eikona providers doctor \
  --channel openai \
  --model openai/gpt-5.4-image-2 \
  --probe \
  --agent
```

本轮 `provider doctor` 返回 `provider_readiness=ready`、`provider_model_present=true`、`provider_auth_status=channel_secret_resolved`。凭据正文没有写入仓库、文档或测试证据。

### 2. 通用 Provider canary

```bash
cd /workspaces/yeisme-agent/cli/eikona
task test:canary
```

本轮结果：

- run：`run_20260831_033812_289547694`；
- artifact count：1；
- 模型：`openai/gpt-5.4-image-2`；
- 实际费用：0.0246 美元；
- 标准证据：`temp/integration-test-runs/integration-20260831T033811.072375199Z/`。

这个 canary 使用通用角色参考提示词，只证明 Eikona Provider 链路，不证明本仓库新增的官方 Character 模板质量。

### 3. 官方 Character fixture 真实出图

显式付费 Task 已改为只加载官方 `wuxia-female-face-master.output.json`，在内存中编译一个 `face_master` 单图 job，再进入既有 cost/auth/provider gate。它不会再渲染或直发仓库 `main` 编译元 Prompt，也不会在首轮请求三视图。持久证据只保留 Prompt digest，不保存模板正文。普通 `task test` 和 `task test:integration` 不会自动调用它。

```bash
cd /workspaces/yeisme-agent/cli/eikona
task test:canary:official-character-asset
```

下面是修正前旧版 canary 的历史结果，保留用于解释失败，不是新流程的验收证据。旧版先以 1536×1024 尝试，Provider 返回 HTTP 422：当时的兼容 Images 路径不支持该 native 2K size。该 run 没有制品，`actual_usd=null`。随后改用 1024×1024，得到：

- run：`run_20260831_034934_909308527`；
- artifact handle：`img_36aaa942397b`；
- artifact digest：`36aaa942397b0ed4d740b35d947b1c07d7e5b9c9ba0ae2446eabff0f72646ffa`；
- Prompt digest：`sha256:4f9450c508dcc002f20491d4fa05ec8e98548a3f109c385a824cd7a20620cf4d`；
- rendered bytes：7294；
- 图片：1024×1024 PNG，3,152,661 bytes；
- 实际费用：0.030045 美元；
- review state：`waiting_review`，没有执行 accept、freeze 或 handoff。

图片位置：

```text
/workspaces/yeisme-agent/cli/eikona/temp/official-ai-drama-character-live-runs/runs/run_20260831_034934_909308527/outputs/openai_001.png
```

人工烟雾检查：

- 基本符合：成年女性主体、月白与浅烟紫配色、服装层次、全身构图、中性背景，三格主体整体接近同一角色；
- 关键失败：第三格仍是正面，不是合同要求的背面；左侧身份标记没有清晰呈现；
- 结论：Provider 执行链路可调用，但官方角色资产执行设计错误，三视图资产质量验收也不通过，不能 accept。

修正后的下一次付费 canary 尚未执行。它应只生成一张 1024×1536 的正面中性 face master；人审通过后，才能分别进入 body master、基础服装正面主视图、侧面和背面。任何一步失败都只返修当前单图，不重抽已接受图片。

### 4. Scaena 真实分镜检查

```bash
cd /workspaces/yeisme-agent/agent/scaena
go run ./cmd/scaena doctor --agent
go run ./cmd/scaena production doctor --project . --agent
```

本轮结果为 `storyboard_model=disabled`、`token_source=missing`、`owner_adapters_disconnected`。Scaena 没有 Codex 会话回退，真实分镜模型要求显式 `env:NAME` credential ref；本轮没有复制 Eikona 凭据，也没有绕过配置门，因此未产生 Scaena Provider 调用或费用。

## 五、何时算“真实可用”

目前可以确认的是合同、离线工作流和 Eikona 真实 Provider 路径可用。若目标是进入可接受的真实生产试用，还需要额外完成：

1. 为 Scaena 配置用户级 storyboard Provider credential 和 owner adapters；不得把 credential 写入仓库、fixture、日志或本页；
2. 按 face master → body master → 基础服装正面主视图 → 独立侧面/背面的顺序逐级验证，每个 Provider job 只生成一张图；
3. 用独立 canary 验证真实分镜忠实度和 bounded repair；
4. 通过人工评审后再 accept 候选，不得用“Provider 调用成功”替代资产验收；
5. 固定 Git commit/tag 与 catalog digest 后再发布 immutable 版本。

先运行只读诊断：

```bash
cd /workspaces/yeisme-agent/agent/scaena
go run ./cmd/scaena production doctor --project . --agent
```

Eikona 的两个真实图片 canary 都会产生费用：

```bash
cd /workspaces/yeisme-agent/cli/eikona
task test:canary
task test:canary:official-character-asset
```

没有明确的 Provider、credential、预算和费用授权时，不应运行这些命令。仓库规定的默认 Eikona 图片模型是 `openai/gpt-5.4-image-2`。

## 六、今日已知缺口

1. **尚未正式发布。** 当前 solution 只在本工作区可用，没有 commit、tag、push 或 publish。
2. **Character live 候选未过质量门。** 旧 run 同时存在元 Prompt 直发和背面缺失问题，只能作为失败证据；修正后的 face-master-only canary 尚未执行。
3. **Scaena 没有 live evidence。** storyboard model credential 与 owner adapters 尚未配置。
4. **Eikona 模型聚合就绪快照不一致。** `models readiness` 对目标 ref 返回 `not_found`，但独立 `providers doctor --probe` 与两次真实调用均证明 Provider 路径可用，需要继续排查模型目录聚合逻辑。
5. **Scaena catalog 路由仍有缺口。** `prompt-asset catalog inspect` 可以消费 exact address，但当前 `prompt-asset catalog resolve` 返回尚未落地的 routing 提示；因此本页先用 Eikona 获取 exact address。
6. **Scaena 帮助发现性不完整。** `prompt-asset repository|catalog` 由兼容分派入口处理，当前 `prompt-asset --help` 没有完整列出这两个子组。
7. **Registry 本地依赖需要显式绑定。** 当前 checkout 运行 Template Registry 时应使用本页的临时 Go workspace，把 Registry 与本地 `shared/promptrepo` 绑定后再验证。

## 七、建议的下一步

- 日常开发：运行三条 provider-free task，并检查 `temp/integration-test-runs/` 证据；
- 准备试用：先执行 Character preview 和 Storyboard inspect；
- 继续 Character：先对新增 face master fixture 做一次明确授权的单图 canary；接受后再生成 body 和正面主视图，最后逐张验证侧面、背面与身份 marker；
- 继续 Storyboard：先配置 Scaena storyboard model credential 与 owner adapters，再运行一次限额 live canary；
- 准备发布：提交各子仓改动，固定 tag/catalog digest，再运行 release checklist；
- 暂时不要把 `exploratory` 改成 `first-support` 或 `mature`，除非已有对应 profile 的独立 live evidence 和人工评审。

相关文档：

- [Character 1.0.0 release candidate](../solutions/video/ai-drama-character-assets/docs/release-1.0.0.zh-CN.md)
- [Storyboard 1.0.0 release candidate](../solutions/video/ai-drama-storyboard-breakdown/docs/release-1.0.0.zh-CN.md)
- [Character preset matrix](../solutions/video/ai-drama-character-assets/docs/preset-matrix.zh-CN.md)
- [Storyboard preset matrix](../solutions/video/ai-drama-storyboard-breakdown/docs/preset-matrix.zh-CN.md)
