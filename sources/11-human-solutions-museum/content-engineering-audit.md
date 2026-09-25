# 内容与工程审计报告

## 审计结论

四份核心文档和内容数据的方向是成立的：项目不是发明百科，而是围绕“问题、误解、洞察、机制、扩散、副作用、可迁移方法”的文明方法库。

但审计前的内容资产更接近静态 demo 文案，不足以支撑长期活博物馆。主要瓶颈是：

- 缺少机器可执行的数据契约；
- 缺少来源、审核、敏感性和发布状态；
- `mvpReady` 容易被误读成公开发布可用；
- 展品路由、详情页结构、展厅归属、相似关系和搜索字段不够稳定；
- MVP 范围容易从“原型完整”滑向“完整产品愿景”；
- 馆藏结构还偏窄，长期需要补制度、治理、经济、照护和权利类案例。

## 已加固事项

### 1. 数据合同

新增：

- `schemas/museum-content.schema.json`
- `scripts/validate-content.mjs`
- `package.json` 中的 `validate:content` 脚本

运行方式：

```bash
npm run validate:content
```

脚本会检查：

- ID 唯一性；
- 展厅、展品、方法、来源引用完整性；
- 展品是否有统一 `sections`；
- 相似展品关系是否有 `relationType`、`dimension`、`confidence`；
- 投稿表单是否保留治理字段；
- `publicationReady` 是否满足来源和审核门槛。

### 2. 内容治理字段

`data/museum-content.json` 已升级到 `schemaVersion: 0.2.0`，并增加：

- `publicationPolicy`
- `sources`
- `publicationStatus`
- `publicationReady`
- `reviewStatus`
- `evidence`
- `timeline`
- `assets`
- `sensitivity`
- `search`

这使内容可以先用于原型，同时为正式发布、事实校对、视觉授权、敏感议题处理和后续检索保留接口。

### 3. 路由与详情页

每个展品现在都有：

- `slug`
- `routePath`
- `primaryGalleryId`
- `galleryAppearances`
- `sections`

前端不需要为 anchor 展品和 seed 展品写两套详情页渲染逻辑。

### 4. 原型与发布边界

`contentStatus` 已改成：

- `prototypeReady: true`
- `publicationReady: false`

文档也同步明确：当前内容可以支撑原型，但未完成来源、事实校对和视觉授权前，不能以正式事实档案口吻公开发布。

### 5. 投稿治理

入馆申请表已补充：

- 来源链接；
- 可观察影响证据；
- 争议或伤害；
- 版权和授权；
- 利益关系；
- 敏感类别。

## 仍需后续处理

### P1：来源和事实校对

正式公开前，每个展品至少需要两个可靠来源。敏感展品还需要限制、争议和措辞边界。

优先处理：

1. 避孕套；
2. 疫苗；
3. 无障碍设计；
4. 科学方法。

### P1：馆藏结构扩展

当前 10 个种子展品适合 MVP，但长期偏窄。后续应补：

- 法律；
- 合同；
- 货币；
- 医院；
- 心理治疗；
- 学校；
- 工会；
- 人权；
- 公共卫生制度；
- 污水处理。

### P1：方法库去口号化

方法目前可读，但仍需补：

- `steps`
- `antiPatterns`
- `notApplicableWhen`
- `failureSignals`
- 现代迁移案例

一个核心方法最好由多个不同领域展品支撑，避免方法从单一案例过度抽象。

### P2：搜索与推荐

v0.1 只做预设入口和静态相似跳转。自由文本搜索、AI 推荐、语义检索和推荐权重都不进入第一版。

如果以后升级，需要先扩充：

- `search.problemPatterns`
- `search.methodPatterns`
- `similarStructures.dimension`
- `similarStructures.confidence`

## 工程执行建议

第一版工程应按以下边界执行：

1. 直接读取 `data/museum-content.json`；
2. 用 `brand` 和 `entryPrompts` 渲染首页；
3. 用 `galleries` 渲染问题星图；
4. 用 `exhibits[].sections` 渲染详情页；
5. 用 `methods` 做方法库和本地收藏；
6. 用 `nominationForm.fields` 渲染入馆申请；
7. 每次改内容都跑 `npm run validate:content`。

不进入第一版：

- 真实后台；
- 真实审核工作流；
- 自由文本搜索；
- AI 推荐；
- 多语言；
- 完整历史考据系统；
- 每个展品的完整长文。
