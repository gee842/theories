# 工程实现执行规格

## 0. 目标

这份文档定义“文明方法博物馆”第一版网页的工程实现方式。

目标不是只做一个静态 demo，而是建立一个可以长期迭代的前端工程骨架：内容可以继续扩写，展品可以继续增加，视觉系统可以继续成熟，未来可以迁移到 React、Next、CMS、后台或多语言，而不会因为第一版把数据、路由、状态、渲染和样式混在一起而大规模返工。

第一版必须做到：

- 能完整表达“从问题进入历史，从历史带走方法”的产品体验；
- 仍然是静态可部署网页；
- 不伪装成正式事实档案；
- 代码结构清楚，后续能持续开发；
- 每次内容和工程改动都有可运行的验证门禁。

## 1. 核心架构决策

### 1.1 技术选型

采用：

- Vite；
- TypeScript；
- 静态 SPA；
- 原生 DOM 渲染；
- CSS 分层；
- Playwright 做关键路径验证。

这条决策覆盖早期文档中 `index.html + styles.css + app.js` 的建议。Vite 在这里只是静态构建骨架，不改变“第一版是静态交互网页”的目标；它的作用是防止第一版退化成一个难维护的大脚本。

暂不采用：

- React；
- Next；
- 后端；
- CMS；
- 数据库；
- 用户账号；
- AI 推荐；
- 真实投稿审核系统。

原因：

- 当前项目需要比 `index.html + styles.css + app.js` 更强的模块边界；
- 但还没有复杂到需要 React/Next；
- Vite + TypeScript 可以保持静态部署，同时给内容模型、路由、状态、渲染和测试留下长期接口；
- 后续迁 React 或 Next 时，只替换视图层，不重做内容层和领域逻辑。

### 1.1.1 术语表

| 术语 | 含义 | 工程用途 |
| --- | --- | --- |
| `prototype` mode | 原型渲染模式 | v0.1 默认模式，允许展示未发布内容，但必须显示原型状态 |
| `public` mode | 正式公开模式 | 只允许 `publicationReady` 内容进入页面 |
| `publicationStatus` | 单个展品的流程状态 | 显示内容处于 prototype、draft、fact-checking 等阶段 |
| `publicationReady` | 单个展品或全站是否可正式发布 | 作为 public build 的硬门禁 |
| `published` | `publicationStatus` 的一种状态 | 不等于全站 `publicationReady` |

v0.1 默认：

```text
VITE_CONTENT_MODE=prototype
```

如果设置：

```text
VITE_CONTENT_MODE=public
```

而 `contentStatus.publicationReady !== true`，构建必须失败，不允许产出一个空站或带未审校内容的正式站点。

### 1.2 长期稳定边界

以下目录是长期核心，不应被 UI 框架绑定：

- `data/`
- `schemas/`
- `scripts/`
- `src/content/`
- `src/domain/`
- `src/routes/`
- `src/state/`

未来如果迁移 React，只替换：

- `src/views/`
- `src/components/`

未来如果迁移 Next/Astro，只把现有 `routePath` 映射到静态页面或动态路由，内容读取、索引、筛选、相似关系、收藏逻辑继续复用。

## 2. 推荐目录结构

```text
data/
  museum-content.json

schemas/
  museum-content.schema.json

scripts/
  validate-content.mjs

src/
  main.ts
  app.ts

  content/
    contentTypes.ts
    loadContent.ts
    normalizeContent.ts
    publication.ts

  domain/
    selectors.ts
    related.ts
    search.ts
    toolbox.ts

  routes/
    routes.ts
    router.ts
    link.ts

  state/
    store.ts
    localStorage.ts

  views/
    homeView.ts
    galleryView.ts
    exhibitView.ts
    methodsView.ts
    toolboxView.ts
    nominationView.ts
    livingMuseumView.ts
    notFoundView.ts

  components/
    appShell.ts
    problemIntake.ts
    problemMap.ts
    exhibitTile.ts
    exhibitDossier.ts
    dossierSection.ts
    methodCapsule.ts
    toolboxDrawer.ts
    similarTrail.ts
    nominationForm.ts
    statusBadge.ts
    formField.ts

  styles/
    tokens.css
    base.css
    layout.css
    components.css
    pages.css

tests/
  data/
  e2e/
```

## 3. 模块职责

### 3.1 `src/content`

唯一可以直接读取 `data/museum-content.json` 的工程层。

职责：

- 读取内容数据；
- 建立索引；
- 做基本归一化；
- 支持 `prototype` 和 `public` 两种内容模式；
- 暴露给 `domain` 层使用。

禁止：

- 操作 DOM；
- 拼 HTML；
- 读取 localStorage；
- 根据当前页面做 UI 决策。

建议 API：

```ts
loadContent(mode: ContentMode): MuseumContentIndex
normalizeContent(dataset: MuseumContentDataset): MuseumContentIndex
isPublicationReady(exhibit: Exhibit): boolean
```

`ContentMode`：

```ts
type ContentMode = "prototype" | "public";
```

`prototype` 模式允许渲染当前原型内容，但必须显示未发布状态。

`public` 模式只能返回满足以下条件的展品：

- `publicationReady === true`
- `reviewStatus.facts === "approved"`
- `reviewStatus.sensitivity === "approved"`
- 至少两个可靠来源；
- 需要展示的主视觉有 `src`、`alt`、`credit`、`license`。

可靠来源定义为 `primary`、`secondary`、`reference`。`uncertain` 来源不能计入 `publicationReady` 门槛。

### 3.2 `src/domain`

领域逻辑层，只处理“博物馆如何组织内容”。

职责：

- 根据展厅查展品；
- 根据展品查方法；
- 根据方法查来源展品；
- 根据 `similarStructures` 查相似展品；
- 生成方法库；
- 生成搜索索引；
- 生成页面 view model。

禁止：

- 直接读取 JSON；
- 直接操作 DOM；
- 直接读写 localStorage。

建议 API：

```ts
getBrand()
getEntryPrompts()
listGalleries()
getGallery(id)
listExhibits(filters)
getExhibitBySlug(slug)
getExhibitByRoutePath(path)
listMethods()
getMethod(id)
getMethodsForExhibit(exhibitId)
getSourcesForExhibit(exhibitId)
getSimilarExhibits(exhibitId)
getNominationForm()
searchContent(query, filters)
```

### 3.3 `src/routes`

路由层负责 URL 和页面状态之间的转换。

v0.1 使用 hash route，保证静态部署和深链不白屏：

```text
#/
#/galleries/:id
#/exhibits/:slug
#/methods
#/toolbox
#/nomination
#/living-museum
```

数据中的 `routePath` 保持 canonical，例如：

```text
/exhibits/condom
```

`link.ts` 负责把 canonical path 转成当前运行模式可用的 URL，例如 `#/exhibits/condom`。组件不得自己拼路由字符串。

不存在的 gallery、exhibit、method 必须进入 `notFoundView`，不能白屏。

`entryPrompts.target` v0.1 只允许：

```ts
type EntryPromptTarget = "nomination";
```

target 到路由的映射集中放在 `routes.ts`，不要在首页组件里写字符串分支。

### 3.4 `src/state`

状态只分三类：

- URL 状态：当前 route、gallery、exhibit；
- localStorage 状态：收藏的方法 ID、表单草稿；
- 内存状态：当前搜索词、临时筛选、抽屉开关。

localStorage key 必须版本化：

```text
museum:favorites:methods:v1
museum:nomination-draft:v1
```

收藏对象只能是 `method.id`。不要收藏 DOM 文本、展品卡片快照或完整对象。

### 3.5 `src/views`

页面级渲染层。

每个 view 接收 view model，不直接解释原始 JSON。

页面：

- `homeView`：问题入口和问题星图预览；
- `galleryView`：问题展厅；
- `exhibitView`：展品档案；
- `methodsView`：方法库；
- `toolboxView`：文明工具箱；
- `nominationView`：入馆申请；
- `livingMuseumView`：活博物馆机制；
- `notFoundView`：错误路由。

### 3.6 `src/components`

小组件只负责局部 UI。

组件不得：

- 读取 JSON；
- 读写 localStorage；
- 发起路由解析；
- 包含展品、展厅、方法的硬编码文案。

## 4. 数据合同

工程实现必须以 `data/museum-content.json` 为唯一内容源。

禁止在组件里硬编码：

- 展品标题；
- 展品详情；
- 展厅映射；
- 方法文案；
- 表单字段；
- 相似跳转；
- 审核状态文案之外的业务事实。

### 4.1 索引结构

内容加载后建立：

```ts
galleriesById
methodsById
exhibitsById
exhibitsBySlug
exhibitsByRoutePath
sourcesById
exhibitsByGalleryId
methodsByExhibitId
similarExhibitsByExhibitId
```

组件不允许在渲染时重复全表扫描来临时推导这些关系。

### 4.2 详情页

展品详情统一渲染：

```ts
exhibit.sections
```

不要为 `anchor` 和 `seed` 写两套详情模板。`depth` 只决定内容厚度和 UI 强调，不决定数据结构。

每个展品必须有 8 个 canonical section key：

```ts
[
  "problem",
  "misreading",
  "insight",
  "mechanism",
  "diffusion",
  "solved",
  "new-problems",
  "method"
]
```

如果未来内容编辑只补了顶层 `whatItSolved` 或 `newProblems`，`normalizeContent` 必须补齐对应 view model；校验脚本也必须阻止缺 section 的展品进入工程实现。

### 4.3 原型与正式发布

当前内容状态：

```ts
contentStatus.prototypeReady === true
contentStatus.publicationReady === false
```

UI 必须在全站或关键页面显示原型/未发布边界。

措辞原则：

- 可以说“原型内容”“种子展品”“待补来源”；
- 不要说“权威档案”“已考据”“正式馆藏”；
- 敏感展品必须使用克制的公共讨论语言。

## 5. 页面规格

### 5.1 首页

目标：让用户立刻进入问题，而不是进入品牌宣传页。

必须展示：

- `brand.name`
- `brand.subtitle`
- `brand.openingQuestion`
- `entryPrompts`
- 问题星图预览或问题节点列表
- 原型状态提示

禁止：

- 营销页式 hero；
- 大段项目说明；
- “欢迎来到...”式被动参观入口。

### 5.2 问题星图 / 展厅页

展厅来自 `galleries`。

桌面端可呈现节点和连接线；移动端必须有等价的列表视图。

展厅页必须展示：

- 展厅名称；
- 展厅问题句；
- 该展厅展品；
- 关联方法；
- 相邻展厅或可继续旅行的路径。

v0.1 不新增 `adjacentGalleryIds`。相邻路径由 domain 层推导：

- 共享 method 的展厅优先；
- 共享 exhibit 的展厅其次；
- 展品 `similarStructures` 连接到其他展厅时作为第三层候选。

如果后续这个推导不够稳定，再新增显式 `adjacentGalleryIds` 字段。

### 5.3 展品档案页

展品页必须像“可操作档案”，不是百科词条，也不是博客文章。

必须展示：

- `ui.stamp`
- `title`
- `oneLine`
- `ui.tags`
- `publicationStatus` / `reviewStatus` / `evidence`
- `sections`
- `borrowableMethodIds` 对应方法胶囊；
- `similarStructures` 对应相似跳转。

状态徽标中文文案允许硬编码，但必须集中在一个 status label map 中，例如：

```ts
const STATUS_LABELS = {
  prototype: "原型内容",
  draft: "草稿",
  "fact-checking": "事实校对中",
  "sensitivity-review": "敏感性审阅中",
  published: "已发布",
  revised: "已修订"
};
```

不要在多个组件里分散翻译状态。

`condom` 是 v0.1 anchor 展品，应作为视觉和信息密度的质量基准。

### 5.4 方法库

方法库的主对象是 `methods`，不是展品。

必须展示：

- 方法标题；
- 原则；
- 适用场景；
- 来源展品；
- 收藏按钮。

方法中的 `steps`、`antiPatterns`、`notApplicableWhen`、`failureSignals` 当前可以为空，但 UI 结构要预留后续扩展位置。

空数组不渲染占位标题。只有字段有内容时，才显示“步骤”“常见误用”“不适用场景”“失败信号”等模块。

### 5.5 文明工具箱

v0.1 只做本地收藏。

必须：

- 收藏 `method.id`；
- 支持移除；
- 刷新后保留；
- 数据变更后自动过滤不存在的 method id；
- 不需要账号。

### 5.6 入馆申请

表单从 `nominationForm.fields` 渲染。

v0.1 行为：

- 不真实提交；
- 不存服务器；
- 不承诺审核；
- 可以保存本地草稿；
- 可以提供“复制为草稿 JSON”或“下载草稿”的本地能力。

UI 必须明确：这是思考工具式表单，不是正式投稿系统。

### 5.7 活博物馆机制

展示：

- 开放提名；
- 公共讨论；
- 策展审核；
- 持续修订；
- 当前 v0.1 的限制。

必须避免让用户误以为真实审核后台已经存在。

## 6. 搜索与筛选

v0.1 不做自由文本搜索框、语义检索或 AI 推荐。

允许：

- 首页预设问题入口；
- 展厅筛选；
- 标签/关键词筛选；
- 点击式问题/标签导航。

下面的搜索索引设计是为后续扩展保留，不要求 v0.1 暴露自由输入搜索框。

搜索索引可来自：

- `exhibit.name`
- `exhibit.title`
- `exhibit.oneLine`
- `exhibit.coreProblem`
- `exhibit.keyInsight`
- `exhibit.sections[].body`
- `exhibit.search.aliases`
- `exhibit.search.keywords`
- `exhibit.search.facets`
- `method.title`
- `method.principle`
- `method.useWhen`

排序建议：

1. alias / exact match；
2. title / name；
3. keywords / facets；
4. gallery 或 method overlap；
5. section body。

## 7. 美学系统

### 7.1 气质

目标气质：

- 博物馆的庄重感；
- 工具箱的实用感；
- 探险地图的发现感。

不要做成：

- 营销官网；
- 普通卡片列表；
- 学术数据库；
- 卡通游戏；
- 复古仿古页面；
- SaaS 科技蓝紫渐变界面。

### 7.2 布局语言

推荐概念：

```text
档案桌 + 问题地图 + 方法工具箱
```

桌面端：

- 左侧：问题入口 / 展厅导航；
- 中间：地图或档案主区；
- 右侧：工具箱抽屉。

移动端：

- 问题入口；
- 展厅节点列表；
- 展品档案；
- 底部工具箱抽屉。

### 7.3 视觉元素

可用：

- 细线连接；
- 展品编号；
- 入馆印章；
- 方法胶囊；
- 档案标签；
- 问题节点；
- 轻量状态徽标；
- 时间刻度。

避免：

- 大面积卡片嵌套；
- 装饰性渐变球；
- 无意义插画；
- 重度 canvas 地图；
- 过度动画。

### 7.4 色彩与字体

CSS token 初始建议：

```css
:root {
  --paper: #f4efe3;
  --ink: #1f241f;
  --museum-green: #2f5d50;
  --stamp-red: #a63a2c;
  --annotation-gold: #b98c3a;
  --line: #cfc6b4;
  --muted: #6f746c;
}
```

字体：

- 标题：`Noto Serif SC`, `Songti SC`, serif；
- 正文：`PingFang SC`, `Noto Sans SC`, system-ui, sans-serif；
- 编号：`ui-monospace`, `SFMono-Regular`, monospace。

字号：

- 首页问题：桌面 34-42px，移动 28-32px；
- 正文：16-18px；
- 档案标签：12-13px。

不要使用 viewport width 缩放字体。

### 7.5 动效

动效只服务关系发现和反馈。

允许：

- 120-220ms hover/focus 过渡；
- 地图节点显露连接；
- 收藏方法的轻量反馈。

必须支持：

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none;
    transition-duration: 0.01ms;
  }
}
```

## 8. 可访问性

v0.1 必须满足：

- `html lang="zh-CN"`；
- 每个页面一个明确 `h1`；
- 使用 `header`、`main`、`nav`、`footer`；
- 所有交互元素使用真实 `button` 或 `a`；
- 键盘可完成首页入口、星图选择、展品跳转、收藏、表单填写；
- focus 样式可见；
- 正文对比度达到 WCAG AA；
- 地图必须有列表等价视图；
- 连接关系不能只靠颜色表达；
- 表单字段有 label、required、错误提示；
- 收藏/移除用 `aria-live` 简短反馈；
- 支持 200% zoom；
- 移动端无横向滚动；
- 图片上线前必须有 alt、credit、license。

## 9. 测试与质量门禁

### 9.1 当前已有

```bash
npm run validate:content
```

### 9.2 v0.1 必须补齐

建议脚本：

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "validate:content": "node scripts/validate-content.mjs",
    "validate:schema": "ajv validate -s schemas/museum-content.schema.json -d data/museum-content.json --spec=draft2020",
    "test:data": "tsx --test tests/data/*.test.ts",
    "test:e2e": "playwright test",
    "check": "npm run validate:content && npm run validate:schema && npm run test:data && npm run test:e2e"
  }
}
```

`validate:schema` 必须真正运行 JSON Schema。当前 `validate-content.mjs` 是引用和发布门槛检查，不能替代 schema 校验。

建议首次搭工程时安装：

```bash
npm install -D vite typescript ajv-cli playwright @axe-core/playwright tsx
```

如果使用 TypeScript 编写 `node:test`，数据测试命令应使用 `tsx`：

```bash
tsx --test tests/data/*.test.ts
```

### 9.3 数据测试

必须覆盖：

- slug 唯一；
- routePath 唯一；
- routePath 能解析到展品页；
- `entryPrompts` 都能进入存在的 gallery 或 nomination；
- `entryPrompts.target` 只能是已知静态目标；
- 每个展品都有 8 个 canonical section key；
- 相似跳转不自链；
- 相似跳转不重复；
- `publicationReady` 展品的来源不能是 `uncertain`；
- method 引用不悬空；
- 收藏数据去重；
- 不存在 ID 时返回空状态，不抛白屏。

### 9.4 浏览器测试

Playwright v0.1 测 Chromium 即可。

关键路径：

1. 首页显示品牌、主问题、入口；
2. 点击问题入口进入展厅；
3. 展厅进入展品；
4. 打开 `condom` 展品详情；
5. 收藏一个方法；
6. 刷新后收藏仍在；
7. 进入方法库；
8. 打开工具箱；
9. 打开入馆申请；
10. 表单字段由数据渲染；
11. 进入活博物馆说明；
12. 不存在路由显示 not found。

视口：

- `375x667`
- `768x1024`
- `1440x900`

必须检查：

- 无 console error；
- 无 404 资源；
- 无横向滚动；
- 长中文不溢出；
- 关键按钮可点击；
- axe 无 critical/serious 问题。

## 10. v0.1 实施阶段

### Phase 0：工程脚手架

任务：

- 引入 Vite + TypeScript；
- 建立 `src/` 目录；
- 接入 CSS 分层；
- 接入 `validate:schema`；
- 保留现有 `validate:content`；
- 配置 `check`。

完成标准：

- `npm run dev` 可启动；
- `npm run build` 可产出静态文件；
- `npm run validate:content` 通过；
- `npm run validate:schema` 通过。

### Phase 1：内容访问层

任务：

- 定义 `contentTypes.ts`；
- 实现 `loadContent`；
- 实现 `normalizeContent`；
- 建立内容索引；
- 实现 `prototype` / `public` 模式；
- 实现 publication guard。

完成标准：

- UI 不直接 import JSON；
- 数据测试覆盖索引和空状态；
- 所有引用由 selector 层解析。

### Phase 2：路由与状态

任务：

- 实现 hash router；
- 实现 `link.ts`；
- 实现 not found；
- 实现 localStorage wrapper；
- 实现方法收藏状态。

完成标准：

- 深链不白屏；
- 不存在 slug 有 not found；
- 收藏只保存 method id；
- 数据变化后过滤失效收藏。

### Phase 3：首页与问题星图

任务：

- `AppShell`
- `ProblemIntake`
- `ProblemMap`
- 首页 view
- 展厅 view

完成标准：

- 首页不是营销页；
- 第一屏问题入口明确；
- 展厅来自数据；
- 移动端有星图等价列表。

### Phase 4：展品档案

任务：

- `ExhibitTile`
- `ExhibitDossier`
- `DossierSection`
- `StatusBadge`
- `SimilarTrail`

完成标准：

- 所有展品详情用 `sections`；
- `condom` 展品完整可读；
- 相似展品可跳转；
- 未发布/未审校状态可见；
- 不使用未授权图片。

### Phase 5：方法库与工具箱

任务：

- `MethodCapsule`
- 方法库页；
- 工具箱抽屉或页面；
- 收藏/取消收藏；
- `aria-live` 反馈。

完成标准：

- 收藏对象是方法；
- 刷新后保留；
- 无重复收藏；
- 方法能回到来源展品。

### Phase 6：入馆申请与活博物馆

任务：

- `NominationForm`
- 表单本地草稿；
- 复制或下载草稿；
- 活博物馆机制页。

完成标准：

- 表单字段来自数据；
- 不真实提交；
- 不承诺审核；
- 治理流程和原型边界明确。

### Phase 7：视觉收束与浏览器验证

任务：

- 完成 CSS token；
- 完成响应式；
- 完成可访问性；
- 跑 Playwright；
- 根据截图修正重叠、溢出、断点和交互问题。

完成标准：

- 三个视口通过；
- 无 console error；
- axe 无 critical/serious；
- 视觉气质接近“档案桌 + 问题地图 + 方法工具箱”。

## 11. v0.1 不做

明确排除：

- 真实后台；
- 用户账号；
- 数据库；
- CMS；
- 投稿入库；
- 审核队列；
- 管理员界面；
- 邮件通知；
- 反垃圾；
- 隐私政策完整流程；
- 自由文本搜索；
- 语义检索；
- AI 推荐；
- 推荐权重；
- 多语言；
- 每个展品完整长文；
- 每个展品真实历史图片；
- 全量机制图；
- 复杂 canvas 星图；
- 重动画；
- 游戏化地图。

## 12. v0.1 完成定义

第一版完成必须同时满足：

- 内容校验通过；
- schema 校验通过；
- build 通过；
- 数据逻辑测试通过；
- Playwright 关键路径通过；
- 首页、展厅、展品、方法库、工具箱、入馆申请、活博物馆机制都可访问；
- `condom` 详情页达到 anchor 样例质量；
- 本地方法收藏可用；
- 表单不伪装成真实提交；
- UI 明确原型内容边界；
- 移动端和桌面端都可用；
- 无 console error；
- 无 404 资源；
- 无严重可访问性问题；
- 没有硬编码展品、方法、展厅或表单字段。

## 13. v0.1 完成后的 review 流程

第一版实现完成后，不直接宣布完成。必须进入 review-and-fix 循环：

### 13.1 自检

执行：

```bash
npm run check
```

并手动检查：

- 首页第一眼是否是“你现在想解决什么问题？”；
- 是否像问题地图，而不是官网；
- 展品详情是否像档案，而不是百科词条；
- 方法库是否让用户带走方法，而不是只看知识；
- 原型/未发布边界是否清楚。

### 13.2 工程 review

检查：

- UI 是否直接 import JSON；
- selector 是否承担了内容关系推导；
- route 是否统一从 `link.ts` 生成；
- localStorage 是否版本化；
- 组件是否有业务硬编码；
- 详情页是否统一用 `sections`；
- public/prototype 模式是否可切换。

### 13.3 视觉 review

用 Playwright 截图检查：

- `375x667`
- `768x1024`
- `1440x900`

检查：

- 文字是否溢出；
- 按钮是否稳定；
- 星图在移动端是否退化为可用列表；
- 工具箱是否遮挡正文；
- 状态提示是否清楚但不压倒内容；
- 是否过度像营销页、数据库或游戏。

### 13.4 对抗 review

按失败模式检查：

- 是否把未审校内容包装成权威事实；
- 是否做了假的投稿系统；
- 是否提前做了 AI/语义搜索；
- 是否出现大而全的 `app.ts`；
- 是否出现无法迁移的样式和组件耦合；
- 是否为了视觉牺牲问题路径。

### 13.5 修正

所有 P0/P1 问题必须修正后再交付。

P2 问题可以进入后续 backlog，但必须写明：

- 问题是什么；
- 为什么不阻塞 v0.1；
- 后续触发条件是什么。

## 14. 后续迁移触发条件

### 14.1 迁 React within Vite

触发条件：

- 组件状态变复杂；
- 工具箱、表单、搜索交互明显增多；
- 原生 DOM 渲染开始产生重复模板；
- 页面局部更新成本过高。

迁移方式：

- 保留 `content`、`domain`、`routes`、`state`；
- 替换 `views` 和 `components`。

### 14.2 迁 Astro / Next SSG

触发条件：

- 需要每个展品稳定 SEO；
- 需要每个展品独立 meta；
- 公开版本需要搜索引擎索引；
- 内容规模扩大但仍主要静态。

迁移方式：

- `routePath` 成为 canonical route；
- 内容 selector 继续复用；
- 页面生成层替换当前 SPA router。

### 14.3 引入后端 / CMS

触发条件：

- 真实投稿；
- 审核工作流；
- 用户账号；
- 管理后台；
- 权限；
- 多人编辑。

迁移方式：

- CMS collection 对齐 `galleries`、`exhibits`、`methods`、`sources`；
- 关系字段只用 ID reference；
- `schemaVersion` 保留；
- 导出 JSON 继续兼容前端内容访问层。

### 14.4 引入 AI 推荐

触发条件：

- 人工维护相似关系成本过高；
- 展品数量超过人工浏览可管理规模；
- 有明确审核机制。

约束：

- AI 只能生成候选关系；
- 输出必须包含 `relationType`、`dimension`、`confidence`、`reason`；
- 低置信度不公开展示；
- 人工审核后写回 `similarStructures`。

## 15. 工程红线

任何实现都不能违反：

- 不得绕过 `data/museum-content.json` 做内容私有副本；
- 不得绕过内容访问层直接在组件解释原始 JSON；
- 不得用中文标题当稳定路由；
- 不得把展品收藏做成主收藏对象；
- 不得把 prototype copy 包装成正式事实档案；
- 不得让表单看起来已经接入真实审核；
- 不得让星图只有视觉版本、没有可访问列表版本；
- 不得引入未授权图片作为正式馆藏视觉；
- 不得在 v0.1 引入后台、账号、AI 推荐、CMS 或真实投稿。
