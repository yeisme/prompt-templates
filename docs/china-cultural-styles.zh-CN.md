# 中国地方文化视觉提示词：首批 20 条

本批是具体风格与场景模板，不是另一份概括性研究框架。每条包含地方与时间范围、详细场景、调色板、光线、构图、材料细节、文化与历史边界、输出要求及评审清单。英文用于 Agent 编译，中文为待人工校对的阅读草稿。

## 直接入口

以下目录均在 `solutions/image/` 下；打开每条的 `docs/template-zh-CN.md` 查看完整中文提示词。

| 序号 | 地方与内容 | 模板目录 |
| --- | --- | --- |
| 1 | 凤凰苗绣：黑底彩线与手作空间 | [fenghuang-miao-embroidery-beta](../solutions/image/fenghuang-miao-embroidery-beta/docs/template-zh-CN.md) |
| 2 | 凤凰银匠：锤纹、银丝与冷暖金属光 | [fenghuang-miao-silversmith-beta](../solutions/image/fenghuang-miao-silversmith-beta/docs/template-zh-CN.md) |
| 3 | 吉首苗鼓：鼓面、脚步与公共节庆 | [jishou-miao-drum-dance-beta](../solutions/image/jishou-miao-drum-dance-beta/docs/template-zh-CN.md) |
| 4 | 花垣苗绣：当代工坊与女性协作 | [huayuan-contemporary-embroidery-beta](../solutions/image/huayuan-contemporary-embroidery-beta/docs/template-zh-CN.md) |
| 5 | 保靖西兰卡普：斜织机与几何经纬 | [baojing-xilankapu-weaving-beta](../solutions/image/baojing-xilankapu-weaving-beta/docs/template-zh-CN.md) |
| 6 | 老司城：雨后遗迹与考古空间 | [laosicheng-rainy-archaeology-beta](../solutions/image/laosicheng-rainy-archaeology-beta/docs/template-zh-CN.md) |
| 7 | 永顺摆手舞：队列、手势与节序 | [yongshun-baishou-dance-beta](../solutions/image/yongshun-baishou-dance-beta/docs/template-zh-CN.md) |
| 8 | 里耶秦简：县政文书与历史再构 | [liye-qin-administration-beta](../solutions/image/liye-qin-administration-beta/docs/template-zh-CN.md) |
| 9 | 捞车河：溪谷木构与生活型遗产 | [laochehe-living-village-beta](../solutions/image/laochehe-living-village-beta/docs/template-zh-CN.md) |
| 10 | 石堰坪：山坡吊脚楼与结构摄影 | [shiyanping-stilt-houses-beta](../solutions/image/shiyanping-stilt-houses-beta/docs/template-zh-CN.md) |
| 11 | 丹寨蜡染：工序分层与蓝白蜡裂 | [danzhai-miao-batik-beta](../solutions/image/danzhai-miao-batik-beta/docs/template-zh-CN.md) |
| 12 | 侗族大歌：无伴奏、无指挥的鼓楼歌唱 | [dong-grand-song-drum-tower-beta](../solutions/image/dong-grand-song-drum-tower-beta/docs/template-zh-CN.md) |
| 13 | 龙胜红瑶：地方服饰与梯田环境肖像 | [longsheng-red-yao-portrait-beta](../solutions/image/longsheng-red-yao-portrait-beta/docs/template-zh-CN.md) |
| 14 | 喜德彝漆：红黄黑漆面与木胎工艺 | [xide-yi-lacquerware-beta](../solutions/image/xide-yi-lacquerware-beta/docs/template-zh-CN.md) |
| 15 | 靖西壮锦：彩纬节奏与织造层次 | [jingxi-zhuang-brocade-beta](../solutions/image/jingxi-zhuang-brocade-beta/docs/template-zh-CN.md) |
| 16 | 蒙古长调：当代草原与长线条构图 | [mongolian-long-song-steppe-beta](../solutions/image/mongolian-long-song-steppe-beta/docs/template-zh-CN.md) |
| 17 | 拉萨堆绣唐卡：丝层、缝线与宗教工艺 | [lhasa-applique-thangka-beta](../solutions/image/lhasa-applique-thangka-beta/docs/template-zh-CN.md) |
| 18 | 喀什木卡姆：庭院音乐与地域乐器核验 | [kashgar-uyghur-muqam-beta](../solutions/image/kashgar-uyghur-muqam-beta/docs/template-zh-CN.md) |
| 19 | 固原砖雕：黄土墙、青砖与雕刻过程 | [guyuan-brick-carving-beta](../solutions/image/guyuan-brick-carving-beta/docs/template-zh-CN.md) |
| 20 | 敦煌启发：矿物色与当代再诠释 | [dunhuang-tang-reinterpretation-beta](../solutions/image/dunhuang-tang-reinterpretation-beta/docs/template-zh-CN.md) |

## 怎样使用

每条三个变量：
- `medium_clause`：必填，例如 `contemporary painting`；指定媒介，不指定模型。
- `composition_notes`：可选，补充取景与构图，不改变固定地区、社区或时间范围。
- `reference_notes`：可选，提供已核验参考、纹样来源、具体地域和使用限制。留空不是授权或史实确认。

例如凤凰苗绣的引用：

```text
promptrepo://official/image/fenghuang-miao-embroidery-beta@1.0.0-beta.1?locale=en
```

模板编译得到可交给 Agent 使用的详细创作指令，Agent 再输出英文视觉提示词与简短审阅说明；它不是最终生成图片，也不是文化事实数据库或图像真实性证明。生成与实地拍摄仍由相应工具及授权流程负责。所有条目为 `internal` / `exploratory`，仅英文注册模板。

## 证据和缺口

来源是用户本次提供的研究正文，首批 20 行完整对应。未读取其 sandbox Excel/CSV，未解析 search 引用标记，未独立访问所列机构网页。机构名只作为核验线索，不视为已核实引用；不编造原文 URL 或访问日期。具体来源说明随各条目的 `docs/sources.zh-CN.md` 保存。

蒙古长调尚缺旗县和地方流派；里耶服饰、灯具和文字需秦代证据；唐卡尊像、固原神圣文字及敦煌具体图像须有获准参考。资料缺失时回退到工艺、材料或非特定细节，不能用生成式想象填成“真实文化”。

## 已执行验证与边界

- 20 个 contract 验证及 catalog build/validate。
- EN/ZH/contract 变量集合、英文正文 digest、仅英文注册检查。
- 每条 exact ref 的 inspect、未确认／缺必填项拒绝编译、中文 locale 拒绝编译。
- 每条两个媒介绑定的 provider-free compile、export、bundle verify；输出无遗留占位符且保留当地时间语境。
- 验证是编译链路验收，不是文化史事实核验、社区审阅或实际出图测试。

在模板仓根目录可复跑：

```bash
python3 scripts/check_china_cultural_styles.py --registry ../../backend-server/template-registry/temp/china-style-authoring/template-registry
```

所用二进制由当前 Registry 源码构建（从 Registry 仓运行）：

```bash
go build -o temp/china-style-authoring/template-registry ./cmd/template-registry
```

一次性入库脚本 `scripts/author_china_cultural_styles.py` 通过 Registry CLI 创建 metadata；发现目标目录存在即停止，不用于覆盖现有版本。修改已登记正文后须走正常 contract refresh 与 catalog 验证，不重新执行一次性脚本。
