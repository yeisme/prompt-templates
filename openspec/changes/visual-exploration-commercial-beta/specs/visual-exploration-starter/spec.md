## ADDED Requirements

### Requirement: 可编译的免费视觉探索包
系统 SHALL 以新的 beta exact ref 提供英文模板与中文人类指南，并保留现有引用。

#### Scenario: 新用户完成并复用
- **WHEN** 用户提供并确认需求、受众、约束、比例与说明语言
- **THEN** Registry 能在零 provider 调用下编译、导出和验证提示包，替换主题后可建立独立会话复用

### Requirement: 证据和内容隔离
系统 SHALL 将付费候选正文留在独立私有内容源，并将未执行的图片与商业实验标记为待验证。

#### Scenario: 公开展示尚无实测
- **WHEN** 尚未运行图片模型或完成真实用户购买
- **THEN** 页面及文档不宣称已验证效果、销量或节省比例
