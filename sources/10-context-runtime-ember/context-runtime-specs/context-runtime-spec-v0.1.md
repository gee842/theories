# Context Runtime · 规范 v0.1（自足本）

> llm is operator, context is existence.
> 一个 store，一条递推，trigger 流驱动。系统里没有"改"，只有"生"。

**Abstract (EN).** This document specifies a context runtime built on a process ontology rather than the chat paradigm. Its primitives are: *moment* (the only constructor — an immutable, content-addressed node produced by one operator invocation), *lineage* (parent-child paths of moments; "context" is a fold over a lineage, not a mutable entity), *operator* (the LLM, identity-free and swappable), and *ref* (the only mutable thing — an atomically movable name). System prompts, skills, memory, agents, loops, and chat formats are all derived, compile-time constructs. Concurrency is fork-by-default; storage is a grow-only content-addressed set; provider wire formats (Messages / Responses / Harmony) are render dialects. The spec is self-contained: a reviewing agent can audit it and an implementing agent can build a reference kernel from it without further context. Normative language: **必须 (MUST)** / **不得 (MUST NOT)** / **应 (SHOULD)** / **可 (MAY)**.

**阅读契约。** 本文自足，不依赖任何对话或外部文档。§13 为评审代理须知，§14 为实现代理须知；两类代理均以 §10 的不变量与 §12 的验收测试为准绳。以《本体 v0.1.1》为内核重述并扩为可实现规格。

---

## 1. 动机与范式定位

当下所有主流 LLM 接口——Chat Completions 的 role/content 消息、Responses API 的 typed items、Harmony 的 role+channel——都是**线性序列**，且多为 schema-on-write：写入时即须决定内容"是什么"（system prompt、skill、memory、tool result），API 把这些写入时分类冻结为硬结构。三个后果：

1. **主体被焊死在协议里。** 每次计算被迫先构造一个 "assistant" 主体；无主体的过程（compaction、索引、合成）没有自然表达。
2. **user role 名存实亡。** 自主循环中 "user" 九成内容是环境反馈穿着用户的马甲；tool_result 塞进 user message 是公认的历史包袱。
3. **历史不可寻址。** "第 N 步模型到底看到了什么"在现行框架中普遍无法回答；分支、重放、审计皆无地基。

本规范把序列化倒置为投影：**本体是带版本的 moment-DAG，chat 格式只是 render 的方言之一**。核心递推：

```
node_new = moment(output_last, fold(lineage), input_new)
```

不存在"被更新的 context"：每个 moment 凝定后归入既定过去，context 是从某节点回望时 fold 出的**视野**。分类推迟到编译期（schema-on-read）："系统提示词"不是存储类型，而是 compile 时的一次角色分配。

**分叉规则内建于构造子：同一节点接到不同 input，即生两个孩子。这一句话就是全部并发模型。**

---

## 2. 本体：四个名词，两枚函数

### 2.1 moment（拍 · 因）

系统中唯一的构造子。一次生成：摄取既定过去（compile 出的窗口），接纳一个 input（event），operator 给出 output，runtime 将三者凝定为节点。

- **不可变**：凝定后永不改写。
- **内容寻址**：id = hash(规范化字节)（§3.1）。完全相同的重放收敛于同一节点（DAG 即递推的 memo table）；采样方差诚实地表现为兄弟节点。
- **对外原子**：内部过程——propose → interpret（逐 effect 权限检查）→ commit——不外泄。commit 边界 = moment 边界。
- **粒度**：一次 llm step = 一个 moment。最细寻址，可在工具链中途分叉。

### 2.2 lineage（相续）

moment 的结构父子路径。context = fold(lineage)。loop 不是机制，是 lineage 的时间结构本身——不存在站在 moments 之外的循环控制器。DAG = 全部 lineage 之并 = 递推的轨道图。**结构保持树**（每 moment 至多一个结构父），引用图才是 DAG（`refs` / `mergeOf`，§3.2）。

### 2.3 operator（算子）

llm。无历史、无跨时同一性、可替换：mid-lineage 换模型是同一存在换了推动者。moment 的 provenance 记录它；lineage 的同一性从不住在它里。脚注（诚实的渗漏）：operator 不空——权重携带倾向、价值、文风；compile 出的 subject 会与权重中潜伏的 subject 干涉（§15 未决）。

### 2.4 ref（名 · 假名）

系统中**唯一可变**的东西：指向某节点的名字。移动必须原子（compare-and-swap）。同一性住在 ref，连续性住在 lineage，两者皆约定。agent、session、branch、HEAD 全是 ref 层用法。

### 2.5 两枚纯函数

```
compile(prefix, trigger, budget, policy) → window   // 可复现、结果可寻址
render(window, dialect)                  → wire     // 方言 backend
```

event / input 不是第五原语：它是 moment 的构成成分——凝定前是触发，凝定后是内容。

---

## 3. 数据模型（规范性）

### 3.1 规范化与寻址

- 一切可寻址对象（Moment、Window、Tombstone）**必须**以 RFC 8785（JSON Canonicalization Scheme）规范化：UTF-8、键名升序、无空白、数字规范形。
- `id = sha256(canonical_bytes)`，十六进制小写。
- 可寻址字段中**不得**出现浮点数（以字符串或整数表示），避免规范化歧义。
- 幂等：向 store 写入同 id 对象是 no-op。

### 3.2 类型定义（TypeScript，规范性）

```ts
export type Hash = string; // sha256 hex over RFC 8785 canonical bytes

export type Source = 'human' | 'operator' | 'environment' | 'runtime' | 'policy';

export interface Prov {
  source: Source;
  authority: 0 | 1 | 2 | 3 | 4;  // 默认格：environment 0 < operator 1 < human 2 < policy 3 < runtime 4（可配置，见 §7）
  operator?: string;             // source='operator' 时必填：产出该内容的算子标识
  providerScope?: string;        // 不透明物件所属方言（如加密推理块）；跨方言降级（§6.3）
}

export type EventKind =
  | 'input' | 'output' | 'observation'
  | 'reference' | 'synthesis' | 'compaction' | 'effect';

export interface Ev {
  kind: EventKind;
  payload: unknown;              // 参与寻址；遵守 §3.1 数字约束
  prov: Prov;
  refs?: Hash[];                 // 引用图之边（非结构父）
}

export interface OperatorRec { id: string; params: Record<string, unknown>; seed?: string }

export interface EffectRec {
  kind: string;                  // 如 'memory.write' | 'policy.bind' | 'workspace.commit' | 'env.action'
  target: string;
  allowed: boolean;              // 权限检查结果；拒绝亦须留痕
  by: Prov;
  note?: string;
}

export interface Meta {
  ts: string;                    // ISO 8601 UTC
  operator?: OperatorRec;        // 本拍 output 的产出者
  window?: Hash;                 // 本拍所依 Window 之址（§6）
  effects?: EffectRec[];
  mergeOf?: Hash[];              // synthesize 之引用（§5）
  compactOf?: { from: Hash; to: Hash }; // compact 覆盖的原路径端点
  transplant?: true;             // 移植标记（§5，默认关闭）
  workspace?: { repo: string; commit: string }; // 环境状态之 pin（§8）
}

export interface Moment {
  parent: Hash | null;           // 结构单亲；null = 创世
  input: Ev;
  output: Ev;
  meta: Meta;
}

export interface WindowItem {
  ev: Ev;
  origin: Hash | 'trigger';      // 携带该内容的 moment；trigger 表示本次触发事件
  region: 'instruction' | 'history' | 'workingset';
}

export interface Window {
  basis: Hash;                   // 前缀之末（所立足的 moment）
  trigger: Ev;
  policyVersion: string;
  budget: number;                // token 预算
  items: WindowItem[];
  composition: { pinned: number; live: number }; // token 计；重放性由此直接读出
}

export interface Tombstone {
  erased: Hash;
  ts: string;
  reason: string;
  by: Prov;                      // authority 必须为 4（§9.3）
}
```

### 3.3 约束

- `Moment.output.prov.source` **必须** ∈ {operator, runtime}。观测永远作为下一拍的 input 归来，**不得**回填已凝定的拍。
- 每拍恰含一个 input 与一个 output。并行工具调用：提案在同一 output 内，多个回声各自成为后续拍的 input（顺序由抵达序决定，见 §15 R9）。
- `refs` / `mergeOf` **不得**指向自身或后代（无环由内容寻址天然保证：id 依赖内容，环不可构造）。

---

## 4. 内核 API（八式，规范性）

组织律：**每个操作必属三类之一——生（构造 moment）、名（移动 ref，全系统唯一 mutation）、观（纯查询）。** 并发成本由类直接读出：观零成本，生免协调，名为唯一 CAS 点。权限亦然：生过写权限（逐 effect），名过命名权限，观过读权限。

```ts
export interface Kernel {
  // 生
  moment(m: Moment): Promise<Hash>;            // 唯一构造；幂等
  // 观
  get(id: Hash): Promise<Moment | Tombstone>;
  walk(from: Hash, dir: 'anc' | 'desc',
       filter?: (m: Moment) => boolean): AsyncIterable<Hash>;
  compile(prefix: Hash, trigger: Ev,
          budget: number, policy: string): Promise<Hash /* Window 之址 */>;
  render(window: Hash,
         dialect: 'messages' | 'responses' | 'harmony'): Promise<unknown>;
  // 名
  refSet(name: string, id: Hash, expected: Hash | 'ABSENT'):
    Promise<{ ok: true } | { ok: false; current: Hash | null }>;
  refGet(name: string): Promise<Hash | null>;
  refList(prefix?: string): Promise<Array<{ name: string; id: Hash }>>;
  refDrop(name: string, expected: Hash): Promise<{ ok: boolean }>;
  // 界
  missing(theirHaves: Hash[]): Promise<Hash[]>; // 对象集差（v0 用朴素 have-list）
}
```

语义细则：

- `moment` 写入前**必须**执行 effect 解释与权限检查（§7），检查结果落入 `meta.effects`；随后规范化、寻址、幂等入库。
- `walk('desc')` 依赖派生的 children 索引；适配器**必须**维护之（索引可重建，非本体）。
- `refSet` 失败**必须**返回当前值；败者**可**改为分叉而非重试（fork-by-default）。
- `compile` **必须**纯：只读已定内容与 trigger。一切非确定查找（检索、时钟、网络）**必须**先落为事件（成为已定内容或 trigger 本身）再入编译。Window 内容寻址、可缓存；产出的拍以 `meta.window` 指向之。
- `get` 命中墓碑时返回 Tombstone（§9.3）。

---

## 5. 标准库（派生动词，信息性；分解为规范性）

每个动词以内核分解给出——分解即语义。

| 动词 | 类 | 内核分解 / 语义 |
|---|---|---|
| fork | 名 | **非操作**：第二个 input 抵达即自然分叉；作为动词 = `refSet(name, node, 'ABSENT')` |
| branch / tag | 名 | 可动的名 / 冻结的名（tag 之 expected 永不放行）|
| checkout / attend | 名 | session 绑定到节点；宿主之事，不入内核 |
| clone | 名 | 同一对象集上的新名空间；物理复制只是缓存策略 |
| synthesize（merge）| 生 | 于 A 支构造一拍：input.kind='synthesis'，`refs`/`mergeOf` 指 B 支；结构单亲 |
| compact | 生 | 构造摘要拍：input.kind='compaction'，`compactOf` 记原路径端点；**原谱系永存** |
| regenerate（rebase / cherry-pick）| 生 | 取原 input 序列在新基座逐拍重跑 operator；窗口已变，输出必新 |
| transplant | 生（默认禁）| 原样搬运旧 output——声称了一个从未见过的窗口；若开放**必须** `meta.transplant=true` |
| revert | —— | **不存在**：fork 于坏拍之前 + 移名。无正操作可逆，故无需逆元 |
| sync | 名 | `missing` 交换（集合并集，结构上无冲突）+ ref 对账（唯一需策略处）|
| fold / view | 观 | `walk('anc')` 聚合出视野 |
| diff(a, b) | 观 | 先公共祖先，再比视野 |
| blame | 观 | walk + provenance：内容系于哪一拍、何来源、何 operator |
| fidelity(n) | 观 | 读 `Window.composition`：pinned/(pinned+live)，重放性即查即得 |
| bisect | 观 | 谱系上对谓词二分："它是在哪一拍学坏的" |
| search | 观 | 内容 / 来源 / 向量检索（参考实现用 pgvector）|

---

## 6. compile 与 render 规范

### 6.1 compile 流水线

parse（收前缀事件流）→ resolve（按"最近绑定优先"解析配置性内容）→ link（环境引用已以 observation 在流中）→ optimize（预算内选择：优先压缩谱系，全保真谱系永远可寻址）→ 出 Window。

- **区域分配**：item 归入 instruction / history / workingset 三区。instruction 区有最低权限门槛（默认 authority ≥ 3）；**injection 的精确定义：低来源权限的内容取得了高编译位置或高写权限**。compile 遇违例**必须**拒绝或降区并留痕。
- **来源加权**：operator 自产内容（source='operator'）**必须**可与 human/environment 区分——这是自我调节回路（模型把自己的输出洗成既定事实）唯一的刹车。
- **可复现**：同 (prefix, trigger, budget, policyVersion) **必须**得同 Window（同 id）。

### 6.2 render 方言映射

| 本体 | messages 方言 | responses 方言 | harmony 方言 |
|---|---|---|---|
| instruction 区 | system message | instructions / developer | system + developer role |
| human input | user message | message(user) item | user role |
| observation | user 内 tool_result 块（目标格式之疣，如实为之）| function_call_output item | tool role |
| output.思维 | assistant thinking 块 | reasoning item | assistant · analysis channel |
| output.提案 | assistant tool_use 块 | function_call item | assistant · commentary channel |
| output.文本 | assistant text 块 | message(assistant) item | assistant · final channel |

### 6.3 不透明物件

带 `providerScope` 的 payload（加密推理、签名思维块）：render 回同方言**必须**原样携带；跨方言**必须**降级（丢弃或以摘要占位并留痕）。

---

## 7. 权限格（capability lattice）

默认格（可配置，配置本身为 policy 内容、版本化）：

```
environment 0 < operator 1 < human 2 < policy 3 < runtime 4
```

双点执行：

1. **写权限（生之路上）**：effect 之目标区域各有 minAuthority；`by.authority ≥ minAuthority` 方 allowed。operator（1）默认**不得**写 policy 区（3）——升格须经 runtime 仪式（如人批），仪式本身落为事件。
2. **位置权限（compile 时）**：instruction 区默认要求 authority ≥ 3。类型消失，保护环留下。

---

## 8. 环境与膜

- 膜内只有记录：inbound 为 observation / signal（用户消息、cron、webhook、文件变更、另一条 lineage 的输出，一律同级），outbound 为 action。tool 的**定义**是膜内内容（被 compile 进窗口）；tool 的**执行**在膜外；回声作为下一拍 input 归来。
- workspace（如 repo）自有历史宇宙，不随 moment-DAG 前进。对齐：拍之 `meta.workspace` pin 其 commit；反向以 commit trailer `Context-Node: <id>` 回指。环境可在 agent 之外前进；runtime **应**能报告观测相对漂移（drift）。

---

## 9. 存储、并发与抹除

### 9.1 两条底座性质

1. **内容寻址 + 不可变** → 对象层是只增集合：副本合并 = 集合并集，结构上不可能冲突；跨机同步 = 交换缺失对象；对象层协调成本为零。
2. **唯一可变者为 ref，且移动原子** → 系统仅有的协调点；fork-by-default 使 CAS 稀少，败者可分叉而非重试。

**语义上是 Git，物理上不必是 git**：底座可为内存 Map、Postgres、对象存储、KV——两条性质带走，模型一行不改。

### 9.2 记忆化

同 (parent, input, output, meta) 收敛于同 id：完全相同的重放自动去重；采样方差 = 兄弟节点。

### 9.3 erase（行政性抹除，代数之外）

语义层无 delete / gc——名可亡，对象不灭，至多冷热分层。唯一例外为法务与隐私的被遗忘权：以 Tombstone 顶替对象（`by.authority` **必须**为 4），hash 链保留，完整性破坏为**明示**。同步时墓碑随对象传播并覆盖之。

---

## 10. 不变量（五条，验收之纲）

1. **只生不改**：除 ref 移动与墓碑顶替外，不存在任何 mutation。
2. **Models propose, runtime commits**：output 是提案；解释为 effects 时逐项过权限检查，拒绝亦留痕。
3. **Provenance 全覆盖**：一切内容带来源与权限；operator 自产必须可辨；compile 按来源加权。
4. **Compile 可复现、可寻址**："第 N 拍模型看到了什么"一行可查（`get(n).meta.window`）。
5. **权限格双点执行**：写权限在生之路上，位置权限在 compile 时。

---

## 11. 与现行范式的位置（信息性）

Chat Completions 把一切粘进 role/content 对象，是 schema-on-write 之极；Responses API 走到类型化事件但仍线性；Harmony 以 role+channel 显影 agentic 原生格式而仍为线性渲染；MemGPT / Letta 的 virtual context 是 "output updates C" 的两级内存硬编码特例。本模型将四者收为其泛化：compile 外置、存在为带版本宇宙、上述格式全部降为 §6.2 的 render 方言。

---

## 12. 验收测试（规范性）

### T1 · 寻址向量

创世拍：

```json
{"input":{"kind":"input","payload":"genesis","prov":{"authority":4,"source":"runtime"}},"meta":{"ts":"2026-08-10T00:00:00Z"},"output":{"kind":"output","payload":"","prov":{"authority":4,"source":"runtime"}},"parent":null}
```

上行即其 RFC 8785 规范形。**必须**得
`id = 52d9c093aa403c84122267c466d995c8ff8aaf3414ba22405d109f05ed30700c`。

### T2 · fork-by-default
given 节点 n；when 两进程各携不同 input 于 n 构造；then 得兄弟 n₁ ≠ n₂，零错误零协调。

### T3 · 记忆化
given 同 (parent,input,output,meta)；when 重复构造；then 同 id，store 尺寸不增。

### T4 · CAS
given `main → n`；when 两进程同以 expected=n 移名至各自新拍；then 恰一者成功，败者收到 current，且可 `refSet(name', ·, 'ABSENT')` 成支。

### T5 · fidelity
given 纯对话 lineage（无 observation）；then 各拍 composition.live = 0。given 含环境观测之拍；then live > 0 且 pinned/live 可读。

### T6 · compaction
given 路径 a→…→z；when compact(a,z) 得摘要拍 s；then fold(经 s) ≠ fold(经原路径) 而 `s.compactOf` 可达原谱系，原拍俱在。

### T7 · injection 谓词
given authority=0 之内容企图入 instruction 区；then compile 拒绝或降区，并留痕。

### T8 · 三拍相续（端到端）
1. 用户消息 e₁ 抵 `main`→n₀：compile 得窗口，operator 提案 `bash: ls`，审权限、凝定 n₁（input、提案、window 址俱在），`main` CAS → n₁。
2. 膜外执行，回声 o₁ 作 input 抵 n₁，凝定 n₂。
3. 同时另进程携 e₂ 抵 n₁，凝定 n₂′——兄弟，无冲突。
4. `get(n₂).meta.window` 一行答"那一步它看到了什么"；fidelity(n₂) 报 live 占比。

---

## 13. 评审代理须知

产出四件：
1. **逐节发现表**：{节, 等级 blocker/major/minor, 断言, 反建议}。
2. **不变量攻击**：为 §10 五条各构造至少一个对抗场景，判定规范是否封死。
3. **R 问题作答**（§15 R1–R10），允许"规范不足以回答"并指出缺口。
4. **可实现性裁定**：一名中等水平工程代理按 §14 能否在无追问的情况下通过 T1–T8。

### R1–R10（开放问题）
R1 RFC 8785 + 禁浮点是否足以封死跨实现寻址歧义（unicode 归一化？）
R2 结构树 + 引用 DAG 是否足够，抑或存在必须结构多亲的场景？
R3 默认权限格 human(2) < policy(3) 是否该颠倒？何种治理下 policy 可高于其作者？
R4 Window 全量落库的存储成本；何时改存重建配方（policy+prefix）而非实体？
R5 compile 纯性 vs 流式检索：检索先落事件的时延代价与缓解。
R6 children 索引在亿级节点下的维护策略。
R7 墓碑同步语义：晚到的墓碑与已扩散对象的最终一致。
R8 §6.2 三方言映射的信息损耗审计（何者不可逆？）。
R9 并行工具调用的多回声抵达序：是否需要序号约定入 payload？
R10 共享名空间的治理：多写者对同名 lineage 的礼仪（协作场景）。

---

## 14. 实现代理须知

**目标**：TypeScript 参考内核，core 目录 < 1000 LOC（简洁是设计压力，不是巧合）。**非目标**：无 loop、无工具执行、无 UI、无网络同步实现（`missing` 用朴素 have-list）、Postgres 仅留适配器接口（首个适配器为内存 Map）。

里程碑：
- **M0**：canonical 序列化 + sha256 寻址 + 内存 store + `moment/get/refSet/refGet` → 过 T1–T4。
- **M1**：children 索引 + `walk` + fold → 过 T6。
- **M2**：`compile`（平凡 policy：全历史、无压缩）+ 区域与权限门槛 + composition 记账 → 过 T5、T7。
- **M3**：`render` 之 messages 方言 + 端到端 → 过 T8。

约定：适配器接口 `Store { put(bytes)→Hash; get(Hash); has(Hash) }` 与 `Refs { cas(name, id, expected) }`；内核只依赖这两个接口。测试即 §12 直译，不得删减。

---

## 15. 已决与未决

**已决**：moment 粒度 = 每 llm step；结构树 + 引用 DAG，不设结构性 merge node；不变量取可查询而非可复现；并发取 fork-by-default；TypeScript-first；语义 Git、物理可换底座；操作三类律与内核八式；revert 不存在；transplant 默认禁；erase 立于代数之外。

**未决**：R1–R10；operator 干涉的度量（compile 之 subject × 权重之 subject）；compaction policy 默认参数与预算函数。

---

## 附 · 词表与思想对应

| 术语 | 英 | 一句话 |
|---|---|---|
| 拍 / 时刻 | moment | 唯一构造子；不可变、内容寻址、对外原子 |
| 相续 | lineage | 结构父子路径；context = 其 fold |
| 算子 | operator | llm；无同一性、可替换 |
| 名 | ref | 唯一可变物；原子移动 |
| 视野 | fold / view | 从节点回望的既定过去 |
| 膜 | membrane | 环境边界；inbound 观测、outbound 行动 |
| 墓碑 | tombstone | 行政抹除的明示残迹 |

| 本体 | Whitehead | 佛家 | 生生语汇 |
|---|---|---|---|
| moment | actual occasion（prehension → concrescence → objective immortality）| 刹那；缘起 | 因生因之一拍 |
| lineage | route of inheritance | 相续 | 生生 |
| agent | society of occasions | 假名（无我）| 像，非体 |
| 递推式 | "The many become one, and are increased by one." | 轮回为结构 | signal set → selector → 新 signal 回流 |
| 不可变可分叉存储 | objective immortality | —— | 护未：已定节点之"未" = 其 forkability |

---

*规范 v0.1（自足本）· 承本体 v0.1.1；供评审代理攻击、实现代理施工。*
