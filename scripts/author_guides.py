#!/usr/bin/env python3
"""Maintain contract-derived tutorials while preserving existing author notes.

Only prose is authored here. Repository/catalog/contract metadata is untouched.
"""
import argparse
import json
from pathlib import Path
import re
import shlex

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- solution-tutorial:start -->'
END = '<!-- solution-tutorial:end -->'

SCENARIOS = {
 'general': ('整理公开项目资料', '周二评审决定先测试两个方案；负责人和截止日期尚未确认。', '摘要保留决定、行动与缺口；不能补出姓名或日期。'),
 'office': ('整理团队会议', '周二例会决定测试新封面，设计同事准备两个版本，下次讨论测试结果。', '行动表将负责人姓名、截止日期标为待确认，讨论不冒充决定。'),
 'research': ('研究两个方案的证据', '公开资料 A 说明本地保存，资料 B 说明团队共享；尚无成本和性能实测。', '区分来源事实与推测，不给缺少证据的方案宣布胜负。'),
 'image': ('为虚构的阅读活动设计视觉', '虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。', '主体、构图与风格一致；引用图中的未知材质不能写成事实。'),
 'video': ('制作虚构阅读活动的短片方案', '30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。', '镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。'),
 'writing': ('完善虚构故事', '林舟在旧车站发现一封未寄出的信；他想联系写信人，但只知道信封上的旧地址。', '保留既定事实、人物知识边界与创作选择；建议不直接成为正史。'),
 'audio': ('制作虚构阅读活动的旁白', '欢迎来到周末阅读角。请放慢脚步，选一本书，为自己留十分钟。', '发音、停顿和情绪服务内容；提示包不证明音色授权或音频完成。'),
 '3d': ('设计虚构桌面道具', '一盏虚构的黄铜桌灯，圆底座、弯曲灯臂，供游戏背景评估，无品牌标记。', '检查轮廓、尺度、遮挡与用途；文字方案不证明网格或可打印性。'),
 'design': ('设计阅读记录工具的界面', '本地阅读记录工具：新增笔记、查看书单、继续上次阅读；偏好清晰层级和低干扰。', '区分需求、风格偏好与已有界面证据，不将审美建议当成用户决定。'),
 'engineering': ('评审虚构代码变更', '分页接口空结果返回 null，客户端预期数组；已有单元测试尚未覆盖空结果。', '给出可定位问题、复现步骤和最小验证；未执行检查标为待验证。'),
 'learning': ('制定学习练习', '初学者每周三次、每次二十分钟，目标是理解基础统计并能解释平均数与中位数。', '练习与时间匹配，通过问题检验理解，不直接宣称掌握。'),
 'marketing': ('编写阅读活动宣传内容', '周末阅读角是虚构社区活动，免费提供座位；尚未提供日期、地点和报名方式。', '不得补造优惠、认证、效果或开放时间；缺失运营信息明确待补。'),
 'product': ('形成阅读工具需求', '读者想快速保存书摘并找回上次阅读位置；本期先支持本机单人使用。', '验收条件可观察，未确认需求与明确承诺分开。'),
 'agent': ('设计资料整理工作流', '用户提供公开会议记录，Agent 整理行动项并导出提示包；不发送消息或调用付费服务。', '工具能力、用户确认和领域执行边界清晰，模板文本不能授予权限。'),
 'graph': ('梳理虚构长篇故事', '林舟只知道旧地址；顾遥知道信件来源但尚未告诉林舟。', '关系与知识状态有文本来源，推测不能当成正史写入。'),
}

DEPENDENCIES = {
 'podcast-narration': '先用 main 组织旁白提示，再按 delivery 的字段准备交付要求；两者是不同角色，不能把前一个编译包视为已经生成的音频。',
 'candid-portrait-matrix': 'main 组织人物、镜头和姿态；delivery 按交付合同封装已选方向。先审阅实际图像，再处理需要图像结果的后续步骤。',
 'xhs-product-cover-v2': 'main 负责封面创意与画面约束；delivery 负责交付描述。产品事实先确认，实际出图由 Eikona 等消费方完成。',
 'ai-drama-background-assets': 'clean-background-plate-v1 生成净背景方案；实际背景产物形成后，validate-background-plate-v1 才检查空间与连续性。',
 'product-promo-shot-design-beta': 'brief → 用户接受实际 Brief → shot-plan。shot-plan 使用固定镜头库版本及已接受 Brief；不要把第一步提示词当成 Brief 结果。',
 'ai-drama-character-assets': '先建立 head-core-bald-v1 与 body-core-neutral-v1；surface-coat-hair-v1、wearable-garment-v1、wearable-accessory-v1 分别描述表面和单件穿戴。character-layer-preview-v1 检查单层组合，character-harmonized-preview-v1 检查整体。各层通过已接受引用衔接，不能由目录顺序推断可覆盖基础身份。',
 'ai-drama-background-assets-v2': 'semantic-object-v1 与 empty-scene-shell-v1 分别准备语义物件和空场景壳；environment-layer-preview-v1 检查单层布局，environment-harmonized-preview-v1 检查整体环境。后两者需要真实、已接受的上游引用。',
 'ai-drama-storyboard-breakdown': 'main 生成分镜语义方案；用户或领域验证器给出具体问题后，再以实际 semantic_plan 和 repair_findings 调用 repair。修复不能凭空重写来源。',
 'ai-film-multi-profile-production': 'project-intent 确定制作意图，scene-package 组织场景，asset-dependency 明确资产依赖，shot-audio-intent 描述镜头与声音，shot-prompt 交接具体提示。continuity-review 检查已生成结果，failure-restructure 仅在有实际失败证据时调整。使用 accepted_source_projection 和 active_reference_bindings 传递已接受事实。',
}

def text(value):
 return json.dumps(value, ensure_ascii=False) if not isinstance(value,str) else value

def example(field, scenario, fixture):
 name=field['name']
 if name in fixture: return fixture[name]
 if field.get('examples'): return field['examples'][0]
 if 'default' in field: return field['default']
 if field.get('enum'): return field['enum'][0]
 if field['type'] in ('integer','number'): return max(1,field.get('min',1))
 if field['type']=='boolean': return False
 common={'output_language':'zh-CN','locale':'zh-CN','target_audience':'项目团队','audience':'初次了解该项目的读者','team':'设计与内容团队','source_text':scenario,'source_material':scenario,'meeting_record':scenario,'sources':scenario,'brief':scenario,'source_brief':scenario,'script':scenario,'subject':'虚构的黄铜桌灯与打开的书','subject_description':'一盏无品牌的黄铜桌灯，旁边是打开的书','product':'无品牌的虚构阅读灯','selling_point':'以阅读场景演示，不宣称未经验证的性能','style':'温暖、克制、清晰','visual_style':'温暖的自然光与简洁构图','tone':'清楚、平静','target_user':'独立阅读者','decision_maker':'项目负责人','research_question':'现有资料支持哪些结论，哪些还需要验证？','revision_goal':'保留情节事实，减少重复，明确人物动机','downstream_owner':'scaena','shot_library_revision':'synthetic-20261103','aspect_ratio':'16:9','episode_ref':'episode:01','reference_image_ref':'promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en','wall_thickness':'2 mm','tolerance':'0.2 mm','print_orientation':'底面朝下','material_notes':'哑光黄铜外观，仅为视觉说明','objects':'阅读椅、落地灯、边桌','relations':'椅子面向窗，灯在右侧，边桌在左侧','learning_goal':'区分平均数和中位数','current_level':'初学者','available_time':'每周三次，每次二十分钟','problem':'空结果返回 null，但客户端预期数组','reproduction':'使用空数据集请求第一页并检查响应','current_workflow':'本地收集资料、人工整理、导出审阅','idea':'本地保存书摘并接续阅读','permissions':'仅本地读取和导出，不发送消息','tools':'已连接的 Template Registry CLI 或 MCP','task':scenario,'objective':scenario,'goal':scenario,'target_artifact':'可审阅的提示包','constraints':'只使用给定资料；未知内容明确标注','factual_boundaries':'只采用用户提供的事实；缺失信息保持未知'}
 if field.get('regex','').startswith('^@'): return '@image1'
 if name in common: value=common[name]
 elif name.endswith('_json'): value='{}'
 elif name.endswith('_ref'): value='synthetic:example-01'
 elif 'negative' in name or 'exclusion' in name: value='不出现商标、额外人物或未提供的事实'
 elif 'duration' in name: value='30 seconds'
 elif 'language' in name: value='zh-CN'
 else:
  label=field.get('labels',{}).get('zh-CN',name)
  value=f'{label}：用于虚构阅读活动的本地练习；保持主体清晰，不补造事实。'
 if field.get('max_length'): value=value[:field['max_length']]
 if len(value)<field.get('min_length',0): value += '示例' * (field['min_length']-len(value))
 return value

def role_data(folder, role):
 contract=json.loads((folder/'contracts'/f"{role['role']}.{role['locale']}.json").read_text())
 cases_path=folder/'tutorials'/f"{role['role']}.{role['locale']}.json"
 if role['locale']=='en':
  from tutorial_cases import load_case
  cases=json.loads(cases_path.read_text())
  case=next(c for c in cases['cases'] if c['kind']=='valid')
  values,_=load_case(folder,role,cases,case)
  return contract,values
 scenario=SCENARIOS.get(folder.parent.name,SCENARIOS['general'])[1]
 return contract,{f['name']:example(f,scenario,{}) for f in contract.get('inputs',[])}

def result_example(category, title, role, folder):
 outputs=sorted((folder/'fixtures'/f"{role['role']}.{role['locale']}").glob('*.output.json'))
 if outputs:
  return '输出结构示例见 ' + '、'.join(f'[{p.stem}](../{p.relative_to(folder)})' for p in outputs[:3]) + '。这些是仓库合成 fixture，不是模型实测结果；逐字段核对对应 schema 和来源。'
 samples={
 'general':'摘要：团队决定先测试两个方案。行动：准备两个版本。负责人和截止日期：待确认。风险：缺少验收标准。',
 'office':'决定：测试新封面。行动项：设计同事准备两个版本。负责人姓名、截止日期、下次会议时间：待确认。',
 'research':'证据 A 支持本地保存，证据 B 支持团队共享。成本与性能尚无证据；下一步需要可比较的测试，不能据此排序。',
 'writing':'人物已知：林舟知道旧地址，不知道写信人的现状。候选行动：核对地址来源。此行动是创作建议，尚未进入正史。',
 'audio':'旁白候选：“欢迎来到周末阅读角。”短暂停顿。“选一本书，为自己留十分钟。”语气平静，声音身份和使用权仍待确认。',
 'image':f'画面候选：以黄铜桌灯和打开的书为主体，保持无品牌；根据「{title}」的风格与构图字段调整表现。这里只描述待生成画面，不展示或声称已经出图。',
 'video':'镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。',
 '3d':'设计候选：圆形底座、弯曲灯臂、简化灯罩。材质为视觉上的哑光黄铜；尺寸、拓扑与可打印性需从实际模型检查，不能由文字确认。',
 'design':'界面候选：先显示继续阅读，再展示书单，笔记操作靠近当前书籍。理由对应用户任务；需通过实际页面验证键盘与窄屏体验。',
 'engineering':'发现：空结果路径返回 null，与客户端数组合同不一致。验证建议：加入空数据集响应测试。当前结论来自给定描述，未声称已运行代码。',
 'learning':'练习：比较数据 1、2、9 的平均数与中位数，解释极端值的影响。每次二十分钟，先回答问题，再依据反馈调整下一次练习。',
 'marketing':'文案候选：“为自己留十分钟，来阅读角翻开一本书。”日期、地点与报名方式待补；不宣称未经核实的活动效果。',
 'product':'需求候选：读者可保存书摘并回到上次阅读位置。验收：关闭并重新打开后能找到保存内容；同步与多用户协作尚未承诺。',
 'agent':'流程候选：读取用户提供的会议资料，整理候选行动项，确认后编译导出。无凭据配置、外部消息或付费调用授权。',
 'graph':'知识差异示例：顾遥知道信件来源，林舟只知道旧地址。两条知识声明分别绑定其来源片段，不能自动传播为双方共同知识。'}
 return '合成内容示例（供理解输出方向，未运行模型）：'+samples.get(category,samples['general'])

def render(folder, solution):
 locale=solution['locales'].get('zh-CN',solution['locales'].get('en',{}))
 title=locale.get('title',solution['id']);summary=locale.get('summary','')
 scenario=SCENARIOS.get(solution['category'],SCENARIOS['general'])
 roles=[r for r in solution['templates'] if r['locale']=='en'] or solution['templates']
 lines=[START,f'# {title}：完整使用教程','',summary,'', '## 如何提出需求','',f'适用目标：{locale.get("usage", summary)}。本教程以“{scenario[0]}”为合成练习，产物是可审阅的提示词或领域交接包。','',f'> 请使用「{title}」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：{scenario[1]} 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。','', '## 版本、许可与准备','',f'- 方案：`{solution["package_id"]}/{solution["id"]}@{solution["version"]}`；成熟度：`{solution["maturity"]}`；rights：`{solution["rights"]}`。', '- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。', '- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。', '- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。','', '## 角色与衔接','',DEPENDENCIES.get(solution['id'],'这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。'), '', '多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。']
 for role in roles:
  name=role['role'];ref=f'promptrepo://official/{solution["package_id"]}/{solution["id"]}@{solution["version"]}?locale={role["locale"]}'
  contract,values=role_data(folder,role)
  cases=None
  if role['locale']=='en':cases=json.loads((folder/'tutorials'/f"{name}.en.json").read_text())
  source_text=cases['source_text'] if cases else scenario[1]
  case_link=f'../tutorials/{name}.en.json' if cases else None
  lines += ['',f'## 角色 `{name}`','',f'职责：{role.get("summary",summary)}', '',f'精确引用：`{ref}`；role：`{name}`。',f'合同许可：`{contract.get("license","unknown")}`；permissions：`{", ".join(contract.get("permissions",[]))}`。','', '### 输入字段','', (f'本角色案例真源：[正例与反例]({case_link})；人工内容审阅尚未完成。' if cases else '历史领域角色按原消费合同交接。'), '', '| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |','| --- | --- | --- | --- | --- |']
  for f in contract.get('inputs',[]):
   n=f['name'];desc=f.get('descriptions',{}).get('zh-CN') or f.get('descriptions',{}).get('en') or f.get('labels',{}).get('zh-CN') or n
   source='由用户选择并确认'
   if n.endswith('_json'): source='由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写'
   elif any(k in n for k in ('source','record','evidence','ref')): source='来自已提供资料或已接受引用；合成引用不可当成真实资产'
   limits=[]
   for key in ('enum','regex','min','max','min_length','max_length','default'):
    if key in f: limits.append(f'{key}={text(f[key])}')
   if cases and n in cases.get('input_notes',{}): source += '；'+cases['input_notes'][n]
   vals=[f'`{n}`',f'{f["type"]}／'+('必填' if f.get('required') else '可选'),desc+'；'+source,'；'.join(limits) or '合同未附加范围限制',text(values[n])]
   lines.append('| '+' | '.join(v.replace('|','\\|').replace('\n','<br>') for v in vals)+' |')
  lines += ['','字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。','', '### 查阅指南与输入合同','', '```bash',f"template-registry prompt guide --ref '{ref}' --role '{name}' --output '{name}-guide.md' --json",f"template-registry prompt inspect --ref '{ref}' --role '{name}' --json",'```','', 'guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。']
  supported=role['locale']=='en' and role['path'].endswith('.md')
  if supported:
   payload={'fields':{f'main.{k}':{'value':v,'kind':'fact' if k in ('source_text','meeting_record','sources','source_material') and v==source_text else 'user','source':'tutorial-source' if k in ('source_text','meeting_record','sources','source_material') and v==source_text else 'user'} for k,v in values.items()}}
   lines += ['','### 完整 CLI 练习','', '以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。','', '```bash','set -eu',f"state=$(template-registry prompt session create --ref '{ref}' --role '{name}' --goal '{scenario[0]}' --json)","session_id=$(printf '%s' \"$state\" | jq -er '.data.id')","revision=$(printf '%s' \"$state\" | jq -er '.data.revision')",f"state=$(printf '%s' {shlex.quote(json.dumps({'text':source_text},ensure_ascii=False))} | template-registry prompt source import --session \"$session_id\" --expected-revision \"$revision\" --id tutorial-source --stdin --json)","revision=$(printf '%s' \"$state\" | jq -er '.data.revision')",'state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<\'INPUT\'',json.dumps(payload,ensure_ascii=False,indent=2),'INPUT',')',"revision=$(printf '%s' \"$state\" | jq -er '.data.revision')",'template-registry prompt session describe "$session_id" --json',"printf 'Confirm the tutorial inputs above? Type yes: '",'read -r answer','test "$answer" = yes || exit 1',f'state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields {shlex.quote(",".join("main."+k for k in values))} --sources tutorial-source --decision-ref tutorial-interactive-yes --json)',"revision=$(printf '%s' \"$state\" | jq -er '.data.revision')",'compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)',"compile_id=$(printf '%s' \"$compiled\" | jq -er '.data.id')",'template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json','template-registry prompt bundle verify --path "result-$session_id" --json','```','', '成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。']
  else:
   lines += ['','### 领域专用角色','', '该角色使用历史审阅 locale 或结构化文档格式，不提供通用 session compile 示例。使用上方 guide 查询拿到教程，并把 exact ref、role、当前 digest 和输入交给声明的消费方；不得把中文/YAML 文件复制成英文 Markdown 绕过准入。']
  lines += ['','### 等价 MCP 操作','',f'1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{{"ref":"{ref}","role":"{name}"}}`；用 resources/read 读取返回 resource。', '2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。', '3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。', '4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。', '5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。', '6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。','', '### 结果示例与检查','', f'示例目标：{role.get("title",title)}。{scenario[2]}', result_example(solution['category'],title,role,folder), ('案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。' if cases else '领域接受由原 owner 验证。'), '合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。', '逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。']
  schema=folder/'contracts/documents'/f'{name}.{role["locale"]}.document.json'
  if schema.exists(): lines += [f'结构化输出另须遵循[document descriptor](../contracts/documents/{schema.name})绑定的 schema；JSON 语法正确不代表语义合格。']
 lines += ['','## 失败恢复、复用与交接','', '- `needs_input`：按缺失字段补值；`needs_analysis`：显式处理资料分析，不能仅凭导入就宣布读懂图片。', '- `needs_confirmation`：读取待确认内容，收到答复后确认；`needs_step_output`：等待前序真实结果并导入。', '- `REVISION_CONFLICT`：重新读取原 session，再合并改动；不要新建替代会话隐藏冲突。', '- `GUIDE_NOT_FOUND`：当前快照缺教程；`GUIDE_STALE`：重新发现指南并核对版本；不自动切换模板版本。', '- 导出结果未知时核对原产物和回执，不盲目覆盖或重导出。单条 prompt 导出不是 bundle，不使用 bundle verify 校验单文件。', '', '```bash','template-registry prompt session list --sort activity --json','template-registry prompt commands --operation session.update --operation session.confirm --json','```','', '从列表选择原 session，使用 session describe/read 核对后更新输入；未变化的确认保持有效，变化的字段重新确认。跨项目导入包创建新会话，接收方重新确认。','', f'声明的消费者：{", ".join(sorted({c for r in roles for c in r.get("consumers",[])})) or "通用 Agent；实际执行选择合适领域 owner"}。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。', '', '编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。',END]
 return section_markers('\n'.join(lines)+'\n')

def section_markers(body):
 output=[];active=False;role='global'
 for line in body.splitlines():
  match=re.match(r'## 角色 `([^`]+)`',line)
  section=None
  if line.startswith('# ') and not active: section='overview'
  if match:
   if active:output.append('<!-- guide:end -->');active=False
   role=match.group(1)
  if line=='### 输入字段':section='inputs'
  elif line=='### 查阅指南与输入合同':section='example'
  elif line=='### 结果示例与检查':section='checks'
  elif line=='## 失败恢复、复用与交接':section='recovery';role='global'
  if section:
   if active:output.append('<!-- guide:end -->')
   output.append(f'<!-- guide:begin {section} {role} -->');active=True
  if line==END and active:output.append('<!-- guide:end -->');active=False
  output.append(line)
 return '\n'.join(output)+'\n'

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
 failures=[];index=['# 按任务查找完整教程','','每个方案都有独立教程。英文角色用于 Agent 编译；历史专用角色按其领域合同交接。','']
 count=0;roles=0
 for metadata in sorted(ROOT.glob('solutions/*/*/solution.json')):
  folder=metadata.parent;solution=json.loads(metadata.read_text());target=folder/'docs/README.md';old=target.read_text() if target.exists() else ''
  body=render(folder,solution)
  if START in old:
   before,rest=old.split(START,1);_,after=rest.split(END,1);new=before+body.rstrip()+after
  else:new=body+ ('\n## 原有专项说明\n\n'+old if old else '')
  if args.check:
   if new!=old:failures.append(str(target.relative_to(ROOT)))
  else:target.parent.mkdir(parents=True,exist_ok=True);target.write_text(new)
  label=solution['locales'].get('zh-CN',solution['locales'].get('en',{})).get('title',solution['id'])
  index.append(f'- **{solution["category"]}** · [{label}](../{target.relative_to(ROOT)}) · `{solution["version"]}` · `{solution["maturity"]}`')
  count+=1;roles+=sum(r['locale']=='en' for r in solution['templates'])
 index_text='\n'.join(index)+'\n';target=ROOT/'docs/tutorials.md'
 if args.check:
  if not target.exists() or target.read_text()!=index_text:failures.append('docs/tutorials.md')
 else:target.write_text(index_text)
 print(json.dumps({'solutions':count,'english_roles':roles,'drift':failures,'provider_calls':0},ensure_ascii=False))
 return bool(failures)

if __name__=='__main__':raise SystemExit(main())
