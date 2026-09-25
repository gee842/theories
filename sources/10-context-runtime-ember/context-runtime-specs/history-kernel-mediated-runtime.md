# 计划 · History Core、Continuation Pipeline 与 Mediated Runtime

状态：Phase 9 accepted architecture；实现与技术 gate 已对齐。Ren sign-off 已于 2026-08-20 记录，
independent final architecture/security/migration review 已于 2026-08-21 以 0 P0 / 0 P1 通过
（`specs/reviews/2026-08-21-phase-9-final-review.md`）。**ADR-031（2026-08-22）已废止 freeze
registry**：frozen surface 现在只由「published package 的 exports」定义，目前尚无 published
package，因此当前没有任何 frozen contract——这是 plugin adoption 实验期的预期状态。本文描述的
correctness invariants（canonical bytes、OCC、fencing、effect bracket、erasure、replay、tenancy）
不受影响。
用于取代 `plan-context-constitution-and-abstraction.md`；旧稿保留为推理记录。
执行 companion：[history-core-execution-plan.md](./history-core-execution-plan.md)。
范围：TypeScript runtime 与当前 monorepo；本轮不设计跨语言协议。
基线：当前 `specs/plan.md` v0.9、已实现的 Stages 0–11，以及 `context-runtime-spec-v0.1.md` 的抽象提案。
约束：不大爆炸重写，不破坏冻结的 canonical bytes，不牺牲已经获得的 crash、race、revocation、redaction 与 replay 语义。

---

## 0 · 结论

新的架构中心不是 Agent，也不是 Context DAG，更不是一个拥有所有能力的 Runtime object。

目标是：

> **一个无 agent 假设的 History Core；一条显式、可寻址的 Continuation Pipeline；一组 non-authoritative scoped decision actors；以及唯一能够中介 model/external-effect contact 与 canonical write/publication 的 Mediated Runtime。**

Phase 9 对这句话的 evidenced scope 是 active Product composition 与各 integration profile 明示为
supported/active 的部分。实验性的 agent semantic writer 仍作为 Stage-10 extension 保留，gate 将其逐
callsite 标为 `experimental-inactive`，并证明 Product 不依赖、不 import 它；它不被偷算进“fully
mediated”，也不扩大本轮 public freeze。

最短表达：

```text
History records what the runtime admitted as an occurrence, claim, or state transition.
Context derives what is relevant now.
Decision actors decide what to attempt next.
Runtime mediates what may actually happen.
```

顶层关系：

```text
                            Authority Provider
                                  │
                                  │ snapshots / decisions
                                  ▼
History Core ────→ Context Resolver ──→ Pure Compiler ──→ Renderer
      ▲                    │                  │               │
      │                    └──────── evidence / IR ───────────┘
      │                                                       │
      │                                                       ▼
      │                                                Decision Actor
      │                                          “下一步尝试什么？”
      │                                            │             │
      │                                      model intent     effect intent
      │                                            │             │
      │                                            ▼             ▼
      │                                       Scoped runtime ports
      │                                            │
      │                         authorize exact final product
      │                         contact · receipt · observation
      │                                            │
      │                                            ▼
      └──────────── admit proposal · commit transition · publish ref
```

第三方 framework 和 runtime 自带的 reference agent 在图中占同一个 logical position：scoped decision actor。Resident runner 可以实现 optional `DecisionDriver` profile；其他 adapter 直接组合所需 capabilities。它们可以拥有 control flow，可以决定下一步运行哪个 agent、model 或 effect，但不得获得：

- Store；
- credential；
- raw authority kernel；
- raw model provider；
- raw external-effect executor；
- canonical commit handle。

实际 model/effect contact、authority permit、effect bracket 与 canonical write/publication 始终由 runtime protocol 完成。

图中省略的一条 ingress 同样受控：external signal 先经 `IngressGateway` 形成 authenticated `InputEvidence`，其 InputEvidenceRef 才能成为 external Continuation cause。

---

## 1 · 优化目标与边界

不存在脱离目标函数的“绝对最优”。本计划针对以下目标寻找最小充分架构：

1. **Embeddability**：History 能作为独立 library 被非 agent 系统使用；Runtime 能承载其他 agentic framework。
2. **Ontology minimality**：底层不采用 agent、chat、prompt、provider role、tool loop 或具体权限模型作为本体。
3. **Boundary honesty**：History、Context、Authority、Decision、Execution 和 Operations 不互相冒充。
4. **Failure closure**：crash、race、revocation、redaction、replay、partial stream 和 unknown world outcome 都有明确语义。
5. **Non-amplification**：数据、引用、编译、framework hook 和组合都不能凭空增加权限。
6. **Replaceability**：Store、authority provider、compiler、renderer、driver、model provider、tool executor 与 durable backend 可独立替换。
7. **Executable claims**：每个架构保证都有 conformance test，不依赖文档自我声明。
8. **Migration economy**：保留当前正确资产；只有真实 coupling 或 correctness defect 才支付新抽象成本。

### 1.1 本轮明确不追求

- 不做跨语言 wire protocol；
- 不替换 PostgreSQL substrate；
- 不重写 StateId、NodeId、TransitionRecord 或现有历史数据；
- 不把所有模型调用、world effect 和 database commit 强行塞进同一事务状态机；
- 不为每个逻辑边界立即创建 npm package；
- 不把第三方 framework 当作不可信代码沙箱问题一次解决；先区分 API boundary 与 privilege boundary；
- 不以目录数量、interface 数量或术语新颖度衡量进步。

### 1.2 成功的反事实测试

五年后如果 agent 这个词失去意义、主流 framework 全部更换、model 不再接受 chat messages，这些层仍应成立：

```text
immutable history
resolved continuation circumstance
derived cognition input
unprivileged decision policy
mediated contact
admitted canonical becoming
```

若某个基础类型必须写入 `agentId`、`messages`、`systemPrompt`、`langgraph` 或 provider role 才能工作，它不属于宪法内核。

---

## 2 · 数据分类：正交轴，不把 role 冒充 bucket

Review 结论：`Semantic Canon / Causal Evidence / Derived / Operational` 不属于同一个互斥分类轴。一个 tool receipt 可以先作为 causal evidence，之后又被某个 semantic transition 接纳；同一 bytes 可以经不同 admitted edge 承担不同 role。反过来，仅仅上传到 CAS 的 object 还没有获得任何可信 role。

### 2.1 Storage/lifecycle class

| class | 例子 | 性质 |
|---|---|---|
| Canonical History | admitted State/Node/Transition、admitted evidence edges、publication facts | immutable record/edge 或受 protocol 约束的 publication；决定 runtime 接纳了什么 |
| Derived Materialization | 尚未被引用的 resolved context、candidate bundle、IR、indexes、projections | 可重建、版本化；不得成为隐式 semantic truth |
| Operational Protocol State | queues、leases、fences、attempts、retries、partial delivery、worker ownership | 不定义 semantic truth，但可以是 fail-closed safety gate；不得假定可无损重建 |
| Ephemeral | 未持久化 scratch、transport buffers、临时计算 | 可丢；一旦影响 contact/continuation，必须先晋升为 evidence 或 operational protocol state |

### 2.2 Canonical History 内的可重叠 role

```text
semantic         相对于 Node/basis/Ref 被接纳的 State、claim 或 observation
causal-evidence  解释 occurrence、contact、decision、refusal、publication 的 witness
both             同一 object 经不同 admitted edges 同时承担两种 role
```

Role 属于 **admitted occurrence/reference edge**，不是 payload schema、表名或 object bytes 的固有属性：

1. History 是 admitted runtime record，不宣称外部世界的绝对真理。
2. Semantic State 相对于 Node、basis 与 published Ref；branch 可以冲突，后续 transition 可以撤回先前 claim，而 canonical history 仍只增不改。
3. Derived artifact 一旦被 contact/transition 引用，就通过显式 evidence edge 晋升为 Canonical History；它仍不会自动成为 semantic State。
4. Causal evidence 不自动获得 cognitive standing 或 authority。
5. Operational state 不等于普通 cache：其丢失可以合法地留下 `unknown/manual-reconciliation`，不能自动重发 contact 或扩大权限。
6. “object bytes 已存在”不等于“已被 runtime 接纳”。

### 2.2 两个外部 sovereigns

**Authority** 与 **World** 有自己的状态、时间和治理，不属于 History 的子树。

```text
Authority sovereign
  principals · grants · revocations · budgets · credentials · policy state

World sovereign
  APIs · filesystems · services · people · physical/external state
```

Runtime History 只记录：

- 使用了哪个 authority snapshot identity；
- 对哪个 exact product 做了什么 decision；
- world contact 的 intent、receipt、observation 或 unknown outcome；
- 能够验证因果关系的公开 evidence。

Credential、完整 grant state、authoritative budget counter 和 raw world handle 不进入 History。

### 2.3 Canonicality、role、standing 与 authority 必须正交

```text
canonicality   是否成为不可变历史或 evidence
history role   以哪条 admitted edge 承担 semantic/evidence/both
standing       是否以及如何进入一次 cognition
authority      当前 binding 是否能做某事
availability   bytes 当前是否仍可读取
```

任何一个维度都不能从另一个维度推导：

- canonical record 可以不进入 cognition；
- instruction standing 不产生 write/tool 权限；
- State 中的 capability reference 不是 live grant；
- unavailable payload 的 hash 可以继续作为完整性证据；
- policy provenance 不等于 epistemic truth。

---

## 3 · History Core：最小宪法内核

### 3.1 Context DAG 更准确地是 History Graph

命名约束：仓库现有 `@context-runtime/kernel` / `NodeRecord.kernel` 指 Authority Kernel。为避免迁移歧义，新实现/package/public API 使用 `HistoryCore` / `HistoryEngine`；“History Kernel”只保留为本文的概念性描述，不创建第二个含糊的 `kernel` package。

产品名可以继续叫 Context Runtime，但 core API 中：

- `HistoryGraph` / `HistoryKernel` 指已经发生的 canonical causal graph；
- `ContinuationContext` 指某一次继续之前解析出的完整条件值；
- `ContextIR` 指 compiler 选择并赋予 standing 后的认知表示；
- `RenderedInput` 指具体 model/provider dialect 的最终输入。

Context 本身不是长期可变图；它是从 History 与外部 sovereign snapshots 解析出的 immutable value。

### 3.2 最小对象

History Core 只需要以下概念：

1. **CanonicalEnvelope**：不可变、内容寻址的 bytes 与 schema-neutral links；
2. **State**：一个完整 semantic value 的内容寻址 root；
3. **TransitionEvidence**：proposal、read witness、patch、decisions 与 implementation 等“如何产生”的 evidence；
4. **Node**：拥有 basis/causes/result State 的 causal occurrence，并引用 TransitionEvidence；
5. **PublicationBatch**：携带 turn、fence、dedupe、adjuncts 与 recovery 的 durable write protocol；
6. **Ref**：只能通过 PublicationBatch 或明确的 admin protocol 发布的可变 name；
7. **Universe**：causal、tenancy 与 export/GC scope；storage namespace 属于 address/adapter，不与 Universe 混称。

`Invocation`、`Effect`、`CompilationRecord`、`AgentRecord` 是由上层协议拥有的 canonical schemas，可以被 History 保存和引用，但不是 History Core 必须解释的对象。

#### Layer ownership rule

> **A lower layer may persist and address an upper layer's canonical bytes, but it must not interpret them, authorize from them, or depend on the upper layer's schema.**

所以 History 可以保存一个 `AgentRecord` 或 `CompilationRecord`，却不能：

- 根据 `AgentRecord.status` 决定调度；
- 根据 compilation placement 决定权限；
- import Agent/Compiler package 才能读取 graph；
- 对未知上层 record 拒绝 round-trip。

为了在“不解释 payload”时仍保证 reachability，History 拥有最小 envelope，而不是认识每个上层 schema：

```ts
type LegacyObjectAddress = {
  kind: "object"; profile: "legacy-record-v1"; universe: UniverseId; digest: Digest;
};
type EnvelopeAddress = {
  kind: "object"; profile: "envelope-v1"; universe: UniverseId; digest: Digest;
};
type BlobAddress = {
  kind: "blob"; profile: "legacy-blob-v1"; namespace: ErasureNamespace; digest: Digest;
};
type NodeReference = { kind: "node"; universe: UniverseId; id: NodeId };

type ObjectAddress = LegacyObjectAddress | EnvelopeAddress;
type ContentAddress = ObjectAddress | BlobAddress;
type CanonicalReference = ContentAddress | NodeReference;

interface CanonicalEnvelope {
  address: EnvelopeAddress;
  schema: { family: string; version: number };
  payloadDigest: Digest;
  bytes: CanonicalPayloadBytes;
  links: readonly CanonicalLink[];
}

type CanonicalLink =
  | { kind: "strong"; target: CanonicalReference }
  | { kind: "citation"; target: CanonicalReference };
```

Identity 必须在 Phase 0 golden vector 前闭合：

```text
payloadDigest  = H(domain-payload || canonical payload bytes)
envelopeDigest = H(domain-envelope-v1 || schema family/version || payloadDigest
                   || canonically ordered unique links)
EnvelopeAddress.digest = envelopeDigest
```

`bytes` 只指 payload bytes；完整 envelope bytes 由 frozen canonical encoding 产生，EnvelopeAddress.digest 必须等于重新计算的 envelopeDigest，existing address 下 schema/bytes/links 任一不同都拒绝。Links 使用明确的 encoded-link byte comparator，禁止 duplicate；self-link 非法；object/blob/node 使用不同 domain separation。`strong` link 必须在本 owning GC/universe scope 已存在或同 batch 原子写入，并参与 reachability；cross-universe `citation` 只记录 provenance，不 root 另一 universe。Unavailable/redacted lookup 始终以 exact address/profile/erasure namespace 判定。

Legacy object/blob identity 不重算、不改写：`legacy-record-v1` 保持现有 record-byte digest，`legacy-blob-v1` 保持现有 `(namespace,payloadHash)` redaction key。若 legacy payload 需要新 schema/links，写一个 immutable `CompanionEnvelope/v1`（EnvelopeAddress）并 link 到 legacy address；历史 ref 原样保留。NodeReference 只是 occurrence link target，不参与 envelope digest 等式。Phase 0 golden vectors 同时覆盖 legacy object、legacy blob、envelope-v1 与 companion mapping。

History Core 验证这些 mechanics；extension-owned validator 验证 payload semantics。任何 load-bearing ref 都必须出现在 envelope `links` 或单独的 core-readable admitted edge 中，不能只藏在 opaque payload。未产生 semantic Node 的 invocation/refusal 通过 `EvidenceAnchor` / contact journal 成为 GC/retention root。

概念形状，不是立即替换现有 ABI：

```ts
interface HistoryNode {
  id: NodeId;
  state: StateId;
  transition: ObjectAddress;

  // 冻结映射：parents[0] 是 primary basis；parents.slice(1) 是 secondary causes。
  basis: NodeId | null;
  causes: readonly NodeId[];
}
```

这样保留两件事：

- continuation 有一个明确的 primary basis，fold/walk 语义不含糊；
- merge、assimilation 或综合可以显式引用其他 causal parents，不必假装它们只是普通 payload link。

本轮不修改现有 `NodeRecord.parents` bytes；reader 必须按 `basis = parents[0] ?? null`、`causes = parents.slice(1)` 往返，禁止重复 parents。Primary walk 与 all-causal traversal 是不同 API。TransitionEvidence 不再重复拥有另一个 authoritative basis/result；engine 只验证它可导出 Node 所声明的 State。

### 3.3 Kernel operations

逻辑能力：

```ts
interface HistoryReader {
  readonly universe: UniverseId;
  object(ref: ObjectAddress): Promise<CanonicalEnvelope | LegacyCanonicalPayload | Unavailable>;
  blob(ref: BlobAddress): Promise<CanonicalBlob | Unavailable>;
  node(id: NodeId): Promise<HistoryNode>;
  state(id: StateId): Promise<StateReader>;
  walk(id: NodeId, direction: "primary-basis" | "primary-descendants" | "all-causes"): AsyncIterable<NodeId>;
  diff(left: StateId, right: StateId): Promise<StateDiff>;
  outgoing(ref: CanonicalReference): AsyncIterable<CanonicalReference>;
  incoming(ref: CanonicalReference): AsyncIterable<CanonicalReference>;
}

interface PublicationBatchPort {
  open(input: {
    ref: PublishedRef;
    expected: PublishedHead | null;
    operationKey: OperationKey;
  }): Promise<{ batch: BatchId; base: PublishedHead | null; fence: FenceToken }>;

  commitStep(input: {
    batch: BatchId;
    fence: FenceToken;
    operationKey: OperationKey;
    product: FinalizedTransitionWriteProduct;
    transition: AdmittedTransition;
    envelopes: readonly CanonicalEnvelope[];
    occ: ReadWriteWitness;
    admission: AdmissionProofRef;
    guards: readonly GuardWitness[];
    adjuncts: readonly TransactionAdjunctEnvelope[];
  }): Promise<CommitStepResult>;

  publish(input: {
    batch: BatchId;
    fence: FenceToken;
    product: RefPublicationProduct;
    admission: AdmissionProofRef;
    guards: readonly GuardWitness[];
  }): Promise<"published" | "branched" | "stale" | { blockedByGuards: readonly GuardRef[] }>;

  recover(key: OperationKey | BatchId): Promise<RecoveredBatchOutcome | null>;
}

interface RefAdmin {
  readonly universe: UniverseId;
  read(ref: Ref): Promise<PublishedHead | null>;
  create(input: AdmittedRefCreation): Promise<CreateRefResult>;
}

interface AdmittedRefCreation {
  product: {
    universe: UniverseId;
    ref: Ref;
    expected: null;
    initial: PublishedHead;
    purpose: "genesis" | "import" | "admin";
    retention: RetentionClass;
  };
  admission: AdmissionProofRef;
  root: RootAttestationRef | ImportEvidenceRef;
}

interface AdmissionProofRef {
  address: EnvelopeAddress;
  subject: ProductDigest;
  scheme: AdmissionSchemeId;
}

interface FinalizedTransitionWriteProduct {
  universe: UniverseId;
  batch: BatchId;
  base: PublishedHead | null;
  transitionDigest: Digest;
  writeSetDigest: Digest;
  evidenceRootsDigest: Digest;
  plannedEffectsDigest: Digest;
}

interface RefPublicationProduct {
  universe: UniverseId;
  ref: Ref;
  expected: PublishedHead | null;
  next: PublishedHead;
  batch: BatchId;
  fenceGeneration: bigint;
  mode: "advance" | "fork" | "bootstrap" | "import";
}
```

`PublicationBatchPort` 是 runtime publication primitive；裸 CAS 不是。它保留现有 durable turn、monotonic per-ref fence、lost-ACK recovery、operation idempotency、guard gate、transactional adjunct 原子性与 publication attribution。History Core 只验证 proof/guard/adjunct 的 registered schema、identity、epoch/CAS 与 transaction participation，不解释它们是 authority、effect resolution 还是 host event；runtime-owned `PublicationCoordinator` 负责这些 meanings，并把 exact RefPublication permit 投影为 `AdmissionProofRef`。Lease rows 丢失不得重置 fence。`RefAdmin` 只服务 bootstrap/受权管理操作。两者都不注入 compiler、driver 或 framework。

Admission binding 对每个 write 都机械执行，不只用于 admin create：

```text
H(domain-final-transition-write || canonical(FinalizedTransitionWriteProduct))
  == commitStep.admission.subject

H(domain-ref-publication || canonical(RefPublicationProduct))
  == publish.admission.subject
```

Core 从 actual transition/envelopes/OCC/batch/base 重新计算 transition-write product；从 actual universe/ref/base/next/batch/fence generation/mode 重新计算 publication product。任一字段替换都会使 proof subject 不匹配。Core 只解释这条 schema-neutral equality，不解释 proof 的 authority meaning。

OCC 不是实现细节：batch 必须验证 exact reads、prefix-membership reads、writes、observed base 与 generic guard epochs。是否允许 re-reduce/linearize 由 runtime admission proof 声明并验证；History Core 不理解 “pure/effect-free” domain meaning。Runtime policy 只允许显式 pure、single-parent、无 unresolved effect 的 transition linearize；其他工作 branch/refuse。

每个 `HistoryReader` / `RefAdmin` instance immutable-scoped 到一个 Universe；`node/state/ref` 的 bare ids 只在该 instance 内解析。Cross-universe import 使用显式 citation/import protocol，不能让同 StateId/NodeId 在不同 availability namespace 间串读。`HistoryReader` 是 library capability，不自行声称 principal authorization。Mediated Runtime 把它与 Authority scope 相交后，才构造给 Resolver/Reducer 的 `ScopedHistoryView`。Raw `HistoryReader` 不注入 Driver，也不注入 pure Compiler。

`AdmittedRefCreation.product` 的 canonical digest 与 `AdmissionProofRef` subject 必须机械相等；Core 不解释谁授权。Genesis/import 原子追加 publication + RootAttestation/ImportEvidence。Ordinary fork ref 优先通过 PublicationBatch 创建；RefAdmin 保留给显式 bootstrap/import/admin。

这里必须区分“package export”与“runtime capability injection”：History 作为 library 当然要向采用它的系统暴露 reader/publication batch；采用方因此承担 admission owner 的角色。完整 Context Runtime deployment 则只把 batch port 注入 Mediated Runtime。第三方 framework 即使能在依赖树中 import 类型，也不会因此获得已配置的 Store connection、authority binding 或 port instance；若需要抵御主动绕过，使用 §7.3 的 egress-contained tier。

History engine 自身验证 canonical bytes、hash、parent/state consistency、CAS 与 transaction invariants；它不判断 agent policy、tool permission 或 cognitive standing。Standalone adopter 可以提供自己的 semantic admission policy，但不能因此宣称 Context Runtime 的 mediation coverage。

History Core 不提供：

- `compile`；
- `render`；
- `invokeModel`；
- `runAgent`；
- `executeTool`；
- `authorize`；
- agent/session lifecycle；
- credential 或 provider registry。

### 3.4 `moment` 的重新定位

`context-runtime-spec-v0.1.md` 的 `moment` 很有表现力，但“一次 LLM step = 一个 moment”把 operator 粒度写进了 ontology。

新定位：

```text
MomentProfile = 一种基于 History Transition 的 reference protocol
```

LLM step、workflow superstep、human decision、deterministic reducer、compaction 都可以定义自己的 profile。History 只看 admitted transition，不要求每个 transition 都有 LLM input/output 对。

### 3.5 Store 与 History 的区别

Store 是 persistence adapter；History 是语义协议。

```text
History contract
    ├── Postgres adapter   当前 production implementation
    ├── in-memory adapter  unit/conformance implementation
    └── future adapters    只在真实 consumer 出现时实现
```

`PostgresStore` 中的 canon/proj/ops 三分仍然有价值，但不得作为上层 public contract：

- `canon` 实现 History 与 durable evidence；
- `proj` 实现可重建 view；
- `ops` 实现 control state；
- 上层通过 purpose-scoped ports 使用它们，而不是拿整个 Store。

### 3.6 Availability / retention 是 History protocol，不是 `object()` 的模糊错误

```ts
type Availability =
  | { status: "full" | "replayable" | "audit-only"; epoch: bigint }
  | { status: "redacted" | "expired"; epoch: bigint; evidence: CanonicalReference };
```

Unavailable read 必须返回 original exact address、typed status 与 monotonic epoch。Ledger/tombstone 在 bytes/cache 之前判定；同 namespace 下 reinsertion 不能复活已抹除 bytes；restore 必须先 reconciliation。GC roots 至少覆盖 published history、open/closed publication batches、generic evidence anchors、unresolved contacts、retention holds 与 transitive envelope links。相同 digest 在不同 erasure namespace 下不得互相复活或连带抹除。

---

## 4 · Continuation Pipeline：Context 从哪里来

### 4.1 Pipeline artifacts，不是 History ontology nouns

```text
ContinuationRequest
    请求从何处、以何 binding 继续

ResolvedContinuation
    本次 continuation 的全部已冻结条件与 snapshot identities

MaterializedCandidates
    resolver/materializer 实际取得、可供 compiler 选择的内容与 evidence

ContextIR
    compiler 选择、分组、赋予 standing 后的 provider-neutral 结果

RenderedInput
    某一 dialect 的 exact final model input + loss record
```

不再用一个 `Frame` 同时承担 provenance、candidate materialization、compile cache key 与 provider bytes。

这些名字描述 protocol stage，不进入 History Core ontology。`ContextIR` 先作为 private/versioned compiler-renderer seam；至少两个真实 renderer/handoff 证明形状后才冻结为公共 schema。

### 4.2 ContinuationRequest

概念合同：

```ts
interface ContinuationRequest {
  basis: {
    universe: UniverseId;
    node: NodeId;
  };
  cause: ContinuationCauseRef;
  binding: {
    principal: Principal;
    realm: ExecutionRealm;
    attestation: BindingAttestationRef;
  };
  requested: {
    contextPolicy: ContextPolicyRef;
    modelProfile?: ModelProfileRef;
    toolProfile?: ToolProfileRef;
  };
}

type ContinuationCauseRef =
  | InputEvidenceRef
  | ContactObservationRef
  | CommittedTransitionRef
  | TimerResumptionRef
  | ExplicitRefusalRef;
```

这里没有必填 `agent`。Agent host 可以在 cause、semantic State 或 policy reference 中加入自己的 canonical identity，但 generic worker/human/workflow 不需要伪造 AgentId。

Binding 不能由 framework 任意拼装。Ingress/host coordinator 从 authenticated subject、tenant/universe、audience 与 realm ceiling 产生 `BindingAttestationRef`；Resolver 验证 attestation、cause 与 basis universe 一致。不同 cause variant 各自有 admission law，不能把所有内部 observation 假装成 raw ingress。

### 4.3 ResolvedContinuation

Resolver 是 effectful 的：它需要读 History、Authority、availability ledger、retrieval/index 和 host binding。它必须把读到的外部条件冻结为可引用 snapshots：

```ts
interface ResolvedContinuation {
  id: ResolutionId;
  request: ContinuationRequest;
  basis: {
    node: NodeId;
    state: StateId;
  };
  snapshots: {
    authority: AuthoritySnapshotRef;
    availability: AvailabilitySnapshotRef;
    retrieval: RetrievalSnapshotRef;
    tools: ToolSetSnapshotRef;
    model: ModelProfileSnapshotRef;
    policy: ResolvedContextPolicyRef;
  };
  implementation: {
    resolver: ImplementationDigest;
    sourceComposition: BundleDigest;
    runtime: BundleDigest;
  };
}
```

`ResolutionId` 只表达 materialization 之前已经冻结的 resolution basis：

```text
ResolutionId = H(request + resolved basis + all snapshot identities + complete implementation block)
```

相同 State、不同 Node、principal、realm、revocation epoch 或 availability snapshot 必须得到不同 ResolutionId。它不宣称覆盖 materializer 之后才取得的 retrieval results。

### 4.4 Candidate materialization

Resolver 之后、pure compiler 之前有一个 effectful materialization seam：

```ts
interface ContextSource {
  readonly descriptor: { id: SourceId; implementation: ImplementationDigest; config: Digest };
  materialize(input: {
    context: ResolvedContinuation;
    ports: {
      history: ScopedHistoryView;
      retrieval: ScopedRetrievalPort;
      artifacts: ScopedArtifactReader;
    };
  }): Promise<SourceObservationBundle>;
}
```

这些 ports 由 Resolver/Runtime 按 snapshot 绑定；它们不是 raw Store/index/network handle。若 materialization 需要新的 live external fetch，该 fetch 必须先经过 runtime world gateway，形成 recorded observation/snapshot，再作为 materialization input；ContextSource 不能旁路 contact law。

所有非确定输入在这里被捕获为 exact result evidence；`RetrievalSnapshotRef` 必须明确表示可 time-travel 的 index version，不能用一个普通 ref 假装查询结果已经冻结：

- retrieval results 与 ranking inputs；
- current availability；
- state reads/prefix membership；
- 已接纳的 observation evidence；
- tool/model catalogue snapshot；
- agent semantic profile（若 host 使用 agent extension）。

Compiler 不直接读取 Store、clock、network、retrieval index 或 authority provider。

`SourceObservationBundle` 只提交 raw observation、content address、read trace 与 source evidence。它不能自报可信 provenance、availability、instruction eligibility 或 authorization decision。Runtime-owned `CandidateAdmission` 根据 authenticated evidence、resolved policy 与 availability snapshot 生成最终 `MaterializedCandidates`：

```text
MaterializationId = H(ResolutionId + ordered source runs + exact result evidence
                      + omissions/errors + candidate-admission implementation)
```

每个 source run 记录 source id/implementation/config、snapshot/read trace、result/omission/error 与 candidate ids。Invocation/Compilation evidence 必须引用 MaterializationId，而不是用较早的 ResolutionId 为实际 candidates 背书。

### 4.5 Candidate 的正交维度

当前 `authority` enum 同时表达来源、位置与权限，必须拆开：

```ts
interface ContextCandidate {
  id: CandidateId;
  content:
    | { status: "available"; address: ContentAddress; digest: Digest }
    | { status: "unavailable"; address: ContentAddress; digest: Digest; evidence: CanonicalReference };
  source: CanonicalReference | StatePath;

  provenance: AdmittedProvenance;
  epistemic: EpistemicStatus & { component?: EpistemicComponentId; partners: readonly CandidateId[] };
  stability: StabilityHint;
  availability: AvailabilityStatus;

  placement: {
    eligible: readonly Standing[];
    decision: PlacementDecisionRef;
  };

  features: Readonly<Record<string, CanonicalScalar>>;
  estimatedCost: CanonicalNonNegativeInteger;
}
```

`MaterializedCandidates` 是有 schema/version、stable ordering 与 digest 的 immutable descriptor bundle。Compiler 不 hydrate，也不接 lazy callback；它只观察 admitted metadata、component topology、availability 与 cost。Unavailable member 保留在 omission/epistemic explanation 中并被 deterministic reject。选择完成后，coordinator 只 hydrate selected available addresses，形成逐一校验的 `SelectedContentBundle` 交给 renderer，避免为了拒绝一个大对象先加载全部 bytes。

至少保持以下正交性：

```text
provenance       从哪里来
epistemic        以何种知识身份存在
standing         进入哪种 cognition channel
stability        对排序/缓存的提示
availability     bytes 是否可用
capability       principal 对行为能做什么（不属于 candidate）
```

### 4.6 Pure compiler 与 renderer

```ts
interface ContextCompiler {
  compile(input: {
    canonical: CompilerInputV1;
  }): CompilationOutput;
}

interface CompilationOutput {
  ir: ContextIR;
  record: CompilationRecord;
}

interface ContextRenderer<D extends Dialect> {
  render(input: {
    ir: ContextIR;
    artifacts: SelectedContentBundle;
    dialect: D;
    profile: ModelProfileSnapshot;
  }): RenderOutput<D>;
}
```

`CompilerInputV1` 必须正好包含 compiler 可观察的全部字段：resolution projection、MaterializationId/candidate descriptors、verified policy bundle、budget、standing floor 与 compiler implementation。不能把未进入 key 的隐藏字段传给 compiler。

`ContextIR` 可以引用 content addresses 而不重复嵌入大 bytes；`SelectedContentBundle` 是与这些 addresses 一一校验的 exact byte bundle。Resolved policy/profile 不能只传 ref：coordinator 必须提供 `{address,digest,verified bytes}` 并验证与 ResolvedContinuation pinned identity 相同。`compile` 与 `render` 都是纯函数：它们不能在内部 hydrate。Artifact persistence 由 coordinator 在函数返回后完成；compiler/renderer 不接 `FilesystemBlobStore`。

Identity 分工：

```text
ResolutionId    materialization 前冻结的 resolution basis
MaterializationId exact source runs/results/admission 的 identity
CompilationKey  H(versioned exact CompilerInputV1)
RenderKey       ContextIR + selected content digests + dialect/profile + renderer implementation
ConditioningId  Resolution + Materialization + Compilation + Render + recorded augmentation
```

必须满足：

```text
CompilationKey 相等 ⇒ ContextIR 与 CompilationRecord 逐字相等
RenderKey 相等      ⇒ rendered bytes 与 loss record 逐字相等
```

反方向不要求成立；允许安全的过度区分，禁止错误共享。所有 canonical ordering 使用明确的 UTF-8 byte/code-point comparator，不使用 process locale 的 `localeCompare`。每次 model contact 绑定 runtime-issued `ConditioningEvidenceRef/ConditioningId`；framework 在 IR/render 后添加的任何内容必须产生新的 placement/render evidence，不能复用旧 resolution identity。

---

## 5 · Agent 与 framework：non-authoritative、scoped decision actors

### 5.1 Agent 不是 runtime core noun

从 Runtime 角度，以下对象属于同一抽象：

- 单 agent loop；
- multi-agent scheduler；
- LangGraph graph；
- AI SDK ToolLoopAgent/custom Agent；
- ADK Runner/custom Agent；
- deterministic workflow；
- event-driven worker。

它们都可以从 continuation view 产生下一组 intent/proposal，但不因此必须实现一个万能 interface。Human UI 要按行为拆角色：semantic choice 进入 ingress/decision actor；grant/approval/revocation 是 Authority Provider client；实际 world action 经过 ExternalEffect gateway。同一个 UI 可以组合这些 contracts，不能把它们焊成 Driver 权限。

### 5.2 Driver contract

`DecisionDriver` 是 runtime-resident reference profile，不是 History ontology，也不强迫 checkpointer、human approval 或简单 reducer 伪造 model/tool ports。Adapter 可以直接组合独立 scoped capabilities；只有 resident runner 需要统一 profile：

```ts
interface DecisionDriver {
  readonly descriptor: DriverDescriptor;

  run(
    input: DriverInput & { activationId: ActivationId; attemptId: AttemptId },
    ports: {
      steps: StepCoordinator;
      proposals: ProposalSink;
      control: ScopedControlPort;
      signal: AbortSignal;
    },
  ): AsyncIterable<DriverEvent>;
}

interface StepCoordinator {
  beginStep(input: {
    activation: ActivationId;
    previousResolution: ResolutionId;
    acceptedObservations: readonly CanonicalReference[];
    frameworkInputDigest: Digest;
    placementEvidence?: ContentAddress;
  }): Promise<{
    resolution: ResolutionId;
    conditioning?: ConditioningEvidenceRef;
    model: SingleGenerationModelLease;
  }>;

  beginEffectBatch(input: {
    activation: ActivationId;
    resolution: ResolutionId;
    calls: readonly ExactEffectIntentDescriptor[];
  }): Promise<EffectBatchLease>;
}

interface SingleGenerationModelLease {
  generate(intent: ModelIntent): Promise<{
    observation: ModelObservation;
    declaredEffects: readonly ExactEffectIntentDescriptor[];
    effectBatch?: EffectBatchLease;
  }>;
}

interface EffectBatchLease {
  invoke(input: { operationId: OperationId; intent: ExactEffectIntentDescriptor }): Promise<EffectObservation>;
  suspend(): Promise<EffectBatchCheckpoint>;
  close(): Promise<"closed" | { unknown: readonly OperationId[] }>;
}
```

`ScopedControlPort` 只能表达 `schedule/yield/suspend/spawn-request` 等 control intent；它不是 queue、lease、worker registry 或 scheduler admin handle。Runtime/host 决定 intent 是否变成实际调度。

`DriverDescriptor` 是 implementation/control identity，不是 Principal，也不是 grant。所有 leases 绑定 activation、resolution、principal、realm、scoped authority、audience、expiry 与 catalogue。Model lease 在一次 generation 后失效；其 output 可为 exact declared calls 产生 effect-batch lease。Batch 内每个 call 使用独立、由 `(activation, framework path/task, local ordinal, product digest)` 派生且 resume-stable 的 `OperationId`，可以并行；一个 call terminal 不关闭其他 calls。Batch 只有在全部 calls terminal/unknown/abort 后 close，或显式 suspend；在此之前不能签发下一 model lease。Yield/abort/completion 时 server-side revoke 未 suspended lease。这些是窄 facade/RPC endpoint，不是可转交 credential；每次调用仍由 runtime 对最终 product 独立授权。

`DriverInput` 根据 integration contract 可以是：

```text
structured       ResolvedContinuation + materialized candidates
ir               runtime-owned ContextIR
rendered         runtime-owned exact provider input
```

保证随 handoff level 改变，不能因为都实现 `DecisionDriver` 就宣称同样的 context coverage。

### 5.3 Driver 能做什么

- 决定下一步调用哪个 agent/model/tool；
- 保持自己的 ephemeral loop/control state；
- 请求 model/tool；
- 产生 semantic proposal；
- suspend、yield、request human input；
- 报告 framework-local telemetry。

#### Driver activation 不是 mutable context

一次 `DecisionDriver.run` 接收一个 immutable `DriverInput`。Model/tool result 不会回填并修改它：

```text
DriverInput(Resolution A)
  → intent/contact
  → RecordedObservation
  → new ContinuationRequest
  → Resolution B / next step lease
  → next cognition
```

Framework 仍可以拥有 loop：它保存 control cursor，决定哪个 observation 触发哪个 driver；Runtime 只要求每次新的 cognition 有新的 step lease 和 conditioning identity。并行 tool results 可以先形成一个 canonical cause bundle，再 resolve 一次。

Integration 明确声明 `continuationMode = driver-reentry | enclosed-loop`。Re-entry profile 在 observation 后退出再激活；AI SDK/ADK/LangGraph 等 enclosed loop 必须在每个后续 model step 调用 `beginStep()`，或配置成单步停止。Framework 若在内部把 tool result 拼进下一次 model request，可以保持 configured-path mediation，但只有新增内容形成完整 placement/render evidence、获得新 ConditioningId，才能声明 cognition captured/governed。

### 5.4 Driver 不能做什么

- 读取任意 History/Store；
- 取得 credential；
- 直接调用 provider SDK；
- 直接执行 external-effect action；
- 构造 authorization decision；
- 直接修改 canonical State 或 Ref；
- 把 framework state update 冒充 runtime transition；
- 通过 callback 自报“已授权”或“已记录”。

### 5.5 Agent state 必须拆词

| agent-related state | owner | History semantics |
|---|---|---|
| identity、goals、memory、semantic configuration | Agent extension schema | 可作为 generic canonical records；History 不解释 |
| active/paused/completed 等长期语义状态 | Agent reducer/transition | 可进入 History，必须显式 transition |
| runnable、queued、lease、retry、backoff | Agent host control plane | operational，不进入 semantic State |
| selected context、prompt、working set | Context pipeline | derived；使用时可保存 evidence |
| partial stream、in-flight tool loop、scratch | Driver/runtime operations | ephemeral/ops；不得自动 canonicalize |
| grants、credentials、authoritative budgets | Authority Provider | History 只记录 snapshot/decision evidence |

因此“Agent state 与 History 分开”不禁止 agent bytes 进入 graph；它禁止 History 拥有 Agent ontology，也禁止 Agent lifecycle/control state侵入 History kernel。

### 5.6 内部实现没有特权

Runtime 自带 reference agent 必须通过同一 `StepCoordinator`、scoped contact ports 与 `ProposalSink`。不同 actor 可以获得不同 capability set；parity 指 origin-independent mediation/no ambient bypass，不是所有 principal 同权，也不是所有 adapter 同 interface。

不得保留：

```text
internal agent fast path
internal compiler Store handle
internal direct ModelDispatcher access
internal direct TransitionEngine.execute
```

如果内部 agent 需要某个能力，先把它表达为所有 driver 可使用的 scoped port；否则不提供。

---

## 6 · Mediated Runtime：统一 law，不伪造统一事务

### 6.1 Contact 是共同抽象，failure protocol 不是

“Mediated Runtime”表示 TCB ownership 与协议边界，不要求实现为一个 class、package 或 process。实际应保持为 `ModelGateway`、`ToolGateway`、`AdmissionCoordinator`、`EvidenceCoordinator` 等小 coordinator；它们共享 exact-product/decision/evidence law，不共享一个巨大状态机。

Model call、external-effect action 与 canonical commit/publication 都是受控 contact：它们消耗成本、触碰外部 sovereign 或改变 admitted canonical history。

共同 envelope：

```text
prepare exact product
    → authorize
    → revalidate adjacent to contact/commit
    → perform through scoped adapter
    → capture result/evidence
    → admit downstream consequence
```

但三者的故障模型不同，不能强行实现为一个 `GenericEffectEngine`。

### 6.2 Inbound observation profile

External ingress 必须先成为 accepted evidence，不能让未经认证的 host payload 直接携带 provenance/authority：

```text
raw signal / user input / webhook / peer response
  → authenticate source and binding
  → freshness/replay claim + normalize + size/schema/tenant admission
  → secret-free evidence projection
  → immutable InputEvidence
  → optional semantic proposal/transition
  → InputEvidenceRef used by ContinuationRequest.cause
```

`InputEvidence/v1` 绑定 universe/tenant、authenticated subject/principal、route/audience、realm ceiling、raw-body digest、verifier/key version、timestamp/nonce/provider event id 与 atomic replay claim。Runtime 从它构造或验证 continuation binding；framework 不能把 Alice 的 evidence 换绑为 admin。`IngressGateway` 不把输入内容升级为权限，也不保证它为真；它只保证“某个 secret-free projection 通过某 route、以某 authenticated provenance 被收到”。Credential、cookie、signed URL、Authorization header 与 token hash 不进入 History；需要保留的 raw audit material 进入独立加密设施，不对 driver/compiler 暴露。

### 6.3 Model contact profile

```text
logical ModelIntent
  → finish all framework/middleware transformations
  → normalize exact provider request
  → authorize exact request + atomic budget reservation
  → durable InvocationAttempt(call key + exact product + decision)
  → one-use contact/egress-read permit
  → provider contact
  → durable ordered stream/outcome capture
  → idempotent usage settle/release/reconcile
  → immutable terminal or unknown Invocation evidence
  → idempotent delivery/ack to driver
```

要求：

- authorization 在产生付费 contact 之前；
- exact request 包含 resolved model、rendered bytes、sampling、realm 与 binding；
- middleware 后修改 request 的对抗场景仍会重新计算 product digest；
- durable attempt 必须先于 contact；自动重试只允许 definite pre-contact failure 或 provider-enforced idempotency；ambiguous timeout 是 `unknown`；
- partial stream、provider refusal/failure、cancel-after-contact 与 paid/unknown usage 不因最终 transition 被拒绝而消失；
- completed-but-undelivered attempt 在 resume 时返回已有 outcome，不重新 contact；
- rendered sensitive bytes 绑定 availability/read witness；redaction 在 adapter send 前使 egress permit 失效；
- model output 不直接成为 State change。

新的通用 invocation evidence 不再要求 AgentId：

```ts
interface InvocationEvidenceV2 {
  id: InvocationId;
  attempt: InvocationAttemptId;
  activation: ActivationId;
  callKey: StableCallKey;
  conditioning: ConditioningEvidenceRef;
  driver: DriverDescriptorRef;
  binding: { principal: Principal; realm: ExecutionRealm };
  product: FinalModelProductRef;
  authorization: AuthorizationDecisionRef;
  renderedInput: EvidenceRef;
  outcome:
    | { kind: "completed"; response: EvidenceRef; usage: UsageRecord }
    | { kind: "refused-before-contact" | "provider-refused" | "failed-definite"; evidence: EvidenceRef }
    | { kind: "unknown" | "cancelled-after-contact"; partial?: EvidenceRef; usage?: UsageRecord };
}
```

现有 legacy `InvocationRecord` 保持可读且 bytes 不变；新 family 以 version discriminator、generic driver/binding identity 写入，并保留 current indexing 所需的 InvocationId、input basis、attempt/contact times。V1/V2 reader、Store common-field index 与 Transition citation 必须在 no-Agent driver 前落地。

### 6.4 External effect contact profile

保留当前已实现的强语义：

```text
exact EffectIntent (tool call / read-only fetch / other world egress)
  → authorize + approval validation
  → durable intent + idempotency key + causal reservation
  → revalidate/fence at executor seam
  → dispatch
  → receipt / failed / unknown
  → durable observation
  → explicit continuation or reconciliation
```

保证必须按 executor class 表达：provider-idempotent、queryable、non-idempotent、reversible。不得承诺一般意义的 exactly-once。

Effect evidence 使用 versioned secret-free projection：语义 observation 与 transport exchange 分开；response headers、cookies、OAuth material、signed URLs、echoed credentials 不得进入 History、logs、RPC 或 cognition bundle。

本计划不再把 `world` 声明为没有 port 的第四种神秘 contact：所有 outbound world contact 都必须映射为 typed external effect，并使用同一 intent/observation envelope；tool 只是 catalogue/UI profile。若未来出现不能合理映射的第二 consumer，再新增独立 WorldGateway。

### 6.5 Canonical commit profile

```text
Proposal
  → validate kind/input/preconditions
  → reduce through ScopedHistoryView
  → derive exact patch + planned effects
  → authorize exact transition product
  → verify StateId/read witness/invariants
  → revalidate authority + availability
  → PublicationBatch.commitStep (fence + OCC + evidence + adjuncts)
  → authorize exact RefPublicationProduct
  → PublicationBatch.publish or explicit branch/race/unresolved outcome
```

Framework 只能把 proposal 送到第一步；不能拿到最后两步。

### 6.6 ProposalSink

```ts
interface ProposalSink {
  submit(input: SemanticProposal): Promise<ProposalReceipt>;
}
```

`ProposalReceipt` 只表示 runtime 已接收或已裁定，不是可写 Store handle。任何裁定（包括 refusal）先形成 durable `AdmissionDecisionEvidence`，receipt 携带 evidence ref；它是否进入下一 cognition 是独立 standing policy。Receipt 必须区分：

```text
accepted-for-admission
committed
branched
refused
deferred
failed-before-decision
```

### 6.7 Hooks 不是 hard boundary

Framework callback/plugin/middleware 可以用于 capture、telemetry 和 intent conversion，但不能独自承担 authorization，因为后续 hook 仍可能修改 payload，另一条执行路径也可能绕过它。

硬边界必须邻接真实接触点：

```text
final provider request → runtime model gateway → credential-bearing provider adapter
final tool action      → runtime tool gateway  → raw executor
final transition       → runtime committer     → History transaction
```

---

## 7 · Authority Plane

### 7.1 Authority 不属于 History，也不属于 Driver

Provider-neutral contract：

```ts
interface AuthorityProvider {
  snapshot(binding: AuthorityBinding): Promise<AuthoritySnapshotRef>;

  scope(
    snapshot: AuthoritySnapshotRef,
    binding: AuthorityBinding,
    request: ScopeRequest,
  ): Promise<ScopedAuthorityRef>;

  attenuate(
    parent: ScopedAuthorityRef,
    child: AuthorityBinding,
    constraints: AttenuationRequest,
  ): Promise<{ scope: ScopedAuthorityRef; witness: AuthorityDerivationRef }>;

  intersect(
    parents: readonly ScopedAuthorityRef[],
    child: AuthorityBinding,
  ): Promise<{ scope: ScopedAuthorityRef; witness: AuthorityDerivationRef }>;

  authorizeAndReserve(
    scope: ScopedAuthorityRef,
    product: ExactProductDescriptor,
    attempt: AttemptId,
  ): Promise<{ decision: AuthorizationDecision; reservation?: ReservationId }>;

  issuePermit(
    decision: AuthorizationDecision,
    product: ExactProductDescriptor,
    attempt: AttemptId,
    availability?: EgressReadWitness,
  ): Promise<ContactPermit | CommitPermit | RefPublicationPermit>;

  settle(reservation: ReservationId, usage: UsageRecord): Promise<SettlementResult>;
  release(reservation: ReservationId, proof: DefiniteNoContactEvidence): Promise<ReleaseResult>;
  reconcile(reservation: ReservationId): Promise<ReservationStatus>;
}
```

Provider 内部可以采用 ACL、RBAC、ABAC、capability tokens、policy engine 或组合；这些模型不进入 History ontology。

`ScopedAuthorityRef` 是唯一能进入 authorize 的 authority input；不能生成 scope 后又用 raw snapshot 绕过它。Delegation 只能 `attenuate(parent)`，merge 默认 `intersect(parents)`；expansion 必须是 Authority sovereign 的独立新 decision。

Permit 是 one-use、audience/attempt/product-bound、短时且带 authority generation 的 protocol token。Permit issuance 与 revocation 在 Authority sovereign 内有明确定义的 linearization order；credential-bearing adapter/History transaction guard 消费 permit。精确保证是：revocation preempts 尚未取得 permit 的 operation；已线性化 permit 按其 one-use/expiry contract 处理。不能提供这一性质的外部 provider 必须降低 coverage，不得声称“即时 revocation”。

### 7.2 Exact product

最小 union：

```ts
type ExactProductDescriptor =
  | FinalModelProduct
  | FinalEffectProduct
  | FinalTransitionProduct
  | RefPublicationProduct;
```

“Exact”不等于把 credential、HTTP nonce 或 transport timestamp 放进 hash。它指一个 versioned authorization projection：所有会改变语义、成本、资源目标、world outcome 或 write set 的 finalized fields 都必须进入；纯 transport/secret fields 必须排除。每个 provider/tool adapter 要有 conformance fixture，证明从 authorized projection 到实际 contact 不存在可扩大行为的未绑定字段。

Decision 必须绑定：

- principal/binding；
- universe/realm；
- authority snapshot；
- exact product digest；
- capability/budget class；
- decision implementation/policy version；
- expiry/revalidation basis。

在可配置 Authority 之前还有不可覆盖的 realm guard：simulation/counterfactual/fork binding 不能接触 live world，除非通过一个显式、独立、记录过的 realm-promotion decision。普通 provider grant 不能绕过该隔离。

### 7.3 TypeScript boundary 与 privilege boundary

不给 Driver 暴露 raw handle 是必要条件，不是恶意代码隔离的充分条件。

定义三个 conformance tier：

```text
API-contained
  trusted same-process driver；只通过类型/API wiring 获得 scoped ports

address-space-separated
  child process + serialized RPC + sanitized env；减少意外泄漏，
  但不声称阻止 filesystem/network/local-socket/subprocess bypass

egress-contained
  独立 OS security principal/container/sandbox；default-deny network/filesystem，
  无继承 FD，isolated cwd/env，resource limits；唯一外联是 authenticated scoped RPC
```

Worker thread 不是 privilege boundary，不能满足 address-space-separated 或 egress-contained。TypeScript-first 不妨碍 OS/process boundary；本轮不要求跨语言。

`runtime-resident` 若对 hostile/untrusted code 声称 secret isolation 或 complete egress mediation，必须达到 egress-contained；address-space-separated 只能声明更弱的 exposure reduction。TCB 明示包含 ingress verifier、authority adapter、final normalizers/gateways、credential-bearing adapters、evidence/publication coordinators、IPC validation 与 composition root。

---

## 8 · Framework integration：不用一个 enum 隐藏多维事实

`IntegrationMode = hosted | resident | peer` 可以作为人类可读 shorthand，但不应成为 foundational contract。它把 loop ownership、context custody 和 enforcement coverage 压成了一个标签。

新的 executable contract 使用正交轴：

```ts
interface IntegrationContract {
  framework: {
    package: string;
    version: string;
    adapterVersion: string;
    apiSurfaceDigest: Digest;
    experimentalFeatures: readonly string[];
  };

  controlOwner: "framework" | "runtime" | "shared" | "peer";
  continuationMode: "driver-reentry" | "enclosed-loop";
  contextHandoff: "structured" | "ir" | "rendered";

  persistence: {
    controlCheckpoint: "none" | "external" | "scoped" | "evidence";
    semanticState: "external" | "proposal-only" | "canonical-mapped";
    longTermMemory: "none" | "external" | "scoped-runtime";
    outOfBandMutation: "disabled" | "captured" | "external";
  };

  contacts: {
    model: "external" | "runtime-port";
    externalEffect: "external" | "runtime-port";
  };

  canonicalWrite: "external" | "proposal-only";
  authority: "external" | "snapshotted" | "permit-at-contact";
  isolation: "api-contained" | "address-space-separated" | "egress-contained";
  replay: {
    supportedModes: readonly ("verification" | "evidence-resume" | "re-execution" | "reconciliation")[];
    interruptResume: "none" | "restart-node";
    crashResume: "none" | "checkpoint-superstep" | "task-cache";
    timeTravel: "none" | "reexecute-after-checkpoint";
    supportedContactReuse: readonly ("none" | "terminal-outcome" | "full-tape")[];
  };
  streaming: {
    modelCapture: "none" | "final-only" | "provider-parts";
    abortOutcome: "opaque" | "typed";
    consumerDisconnect: "cancel" | "detach";
    frameworkEvents: "external" | "recorded";
  };
}
```

Phase 9 vocabulary reconciliation: `shared` is the explicit control-owner value for a framework loop
whose cognition crosses a runtime-owned step protocol. `contextHandoff: "rendered"` is the frozen
`DriverHandoffLevel` spelling for a runtime-rendered handoff; the coverage condition remains named
`handoff-runtime-rendered`. These are the executable `IntegrationContract` values, not aliases to be
accepted on the wire.

Manifest 只声明 capabilities。每次 activation/attempt 的实际 replay mode、resume boundary 与 contact-reuse decision 写入 attempt evidence，并作为 gateway input；同一个 adapter 可以在普通执行、interrupt resume、crash resume、time-travel re-execution 与 reconciliation 中选择不同合法 mode。LangGraph Graph/Functional API 若语义不同，使用不同 API profile/manifest。

### 8.1 不再使用含糊的 “full coverage”

先区分 claim strength，再区分 coverage dimension：

```text
DeclaredCoverage  adapter/wiring 声称配置了什么
ObservedCoverage  runtime 实际看到了哪些 contact/write
EnforcedCoverage  isolation/permit 机械阻止了哪些 bypass

MediationGoverned  model/effect contact 与 canonical write 经 runtime permit/protocol
CognitionCaptured  selection/render/augmentation 被完整记录
CognitionGoverned  placement/render/augmentation 由 runtime policy 产生并绑定
HistoryCaptured    所有已知会影响后续语义的 state/evidence 有 admitted edge
```

Configured-path `MediationGoverned` 的必要条件是：

```text
model contact     = runtime-port + permit-at-contact
external effect  = runtime-port + permit-at-contact
canonical write   = proposal-only
ref publication   = authorized publication batch
```

`CognitionCaptured` 要求 framework 的每次 post-IR/post-render 修改都重新形成可寻址 placement/render evidence，并在 contact 前绑定新的 ConditioningId；`CognitionGoverned` 还要求这些 placement 由 runtime policy 决定。

`HistoryCaptured` 要求 semantic reads/writes、long-term memory 与 out-of-band mutation surfaces 都被 manifest 分类；一个 History-backed checkpointer 本身不够。

API-contained/address-space-separated 只能声称 Declared/Observed configured-path coverage；对 untrusted code，只有 egress-contained 才能把无旁路提升为 EnforcedCoverage。`controlOwner` 可以是 framework，也可以是 runtime；谁拥有 loop 不决定谁拥有 cognition、truth 与 effects。

### 8.2 Framework-hosted

Framework 可以拥有 loop/session/state machine，只要：

- 其 model client 是 runtime wrapper；
- 其 tools 是 runtime wrappers；
- semantic State change 通过 ProposalSink；
- framework-local state 与 canonical State 明确分开。

若 framework 仍持有旁路 provider credential、raw effect handle、global network/filesystem service 或未分类的 memory/store，manifest 必须机械降级。API-contained wiring 不能证明 absence of ambient bypass。

### 8.3 Runtime-resident

Framework 作为 optional resident runner/decision actor 运行在 runtime 提供的 scoped environment 中。它拥有 orchestration decision，不拥有 contact/commit。

这是 reference agent、LangGraph resident graph、ADK custom runner 和 AI SDK agent loop 应共享的目标路径。

### 8.4 Peer

双方各有自己的 History、authority 与 loop，通过授权的 egress/request 协议交换消息或 artifacts：

- 不共享 Store；
- 不隐式继承 authority；
- response 以 observation/evidence 进入本地 continuation；
- remote peer 的 claim 不自动成为本地 semantic truth。

### 8.5 三个 reference mappings

**LangGraph**

```text
hosted/checkpointer:
  thread/checkpoint 通过 History adapter 保存；coverage 诚实停在 checkpoint/state
  Store、pending writes、updateState/out-of-band mutation 单独分类

hosted/full:
  graph owns control flow；wrapped model/tools；state update 通过 ProposalSink 映射

resident:
  graph 是 resident decision actor；graph state 是 driver-local/control state；
  interrupt/restart-node 使用 stable activation/operation ids；
  canonical change 仍由 runtime admission
```

**AI SDK**

```text
facade:
  runtime-backed Agent 保留 generate/stream API

resident:
  ToolLoopAgent/custom Agent 每 step 使用 runtime-supplied model/effect wrappers
  adapter 拥有最终 prepareStep；动态 model substitution 只接受 runtime-branded capability

hard boundary:
  middleware 用于 capture；final LanguageModel/tool wrapper 用于 authorization/contact
```

**ADK**

```text
hosted:
  Runner owns loop/session；plugin 转换 lifecycle；final model/effect wrapper 执行硬边界
  使用 restricted profile：scoped SessionService，禁用 credentialService，
  memory/artifact services 必须 scoped-runtime 或显式 external

resident:
  custom agent/runner 使用同一 restricted services + StepCoordinator

peer:
  A2A 等价路径作为 authorized egress；结果记录为 observation/evidence
```

具体 framework 名只存在 adapter package 与 conformance fixture，不进入 domain ontology。

---

## 9 · 七条宪法 Laws

这些是最小 invariants。现有 Twenty Laws 中的其他内容移为 protocol rules、construction principles 或 review checklist。

### Law 1 · Canonical becoming

> Canonical history 只能通过 admitted occurrence 增长；semantic State 只能通过 admitted transition 改变；已有 Node、State 与 record 不可改写；Ref 只能通过受权、fenced、可恢复的 publication protocol 改变。

推论：

- Store update 不等于 semantic transition；
- framework state update 不等于 canonical write；
- no-op 不制造虚假 State；
- redaction 必须明示 availability 改变，不能在 hash 下偷偷换 bytes。

攻击测试：driver 获得一个看似 state object 的引用并修改，History/StateId/Ref 均不得变化。

### Law 2 · Explanation closure

> 在声明的 adoption/verification coverage 内，每个 Node、State change、invocation attempt、effect observation 与 refusal 都能追溯到 basis/root、input/proposal、implementation 和 decision evidence。

推论：

- provenance 覆盖所有 canonical content；
- paid model evidence 不因后续拒绝而丢失；
- unknown world outcome 不能伪装为 failed 或 succeeded；
- replay 能区分重新计算、复用 evidence 与重新接触 world。
- genesis 使用 `RootAttestation`；外部 import/sync 使用 `ImportEvidence`，只能按实际 witness 声称 integrity、transport provenance 或完整 explanation。

攻击测试：删除任一必要 witness，验证器必须拒绝声称完整解释。

### Law 3 · Derived non-sovereignty

> Context、IR、prompt、projection、index、cache 与 operational state 都不能成为隐式 semantic truth 或 authority source。

推论：

- `proj` 可删可重建；
- compile output 只有经过显式 proposal/transition 才能改变 State；
- prompt 中的 grant 描述不能授权；
- Agent scratch 不因被持久化就成为 memory。
- operational fence/attempt 可以作为 fail-closed contact/admission gate；它不产生 truth/capability，也不保证丢失后可精确重建。

攻击测试：只修改 projection/index/cache，canonical history 与 authorization outcome 不得改变。

### Law 4 · Accountable conditioning

> 一次 cognition 中所有 runtime-observable、runtime-selected 或 adapter 声称可固定的 conditioning inputs 必须冻结、可引用；materialization 可以 effectful，compile/render 必须对 exact versioned input 纯。

推论：

- ResolutionId、MaterializationId、CompilationKey、RenderKey 与 ConditioningId 分工；
- retrieval/availability/authority/tool/model snapshot 都进入 witness；
- “第 N 次模型看到了什么、为什么”可回答；
- dialect loss 必须显式。

攻击测试：在相同 CompilationKey 下改变候选、policy 或 implementation 必须被检测；相同 key 的输出逐字相同。

### Law 5 · Authority non-amplification

> History content、Context placement、framework composition、fork、merge 与 delegation 都不能产生 Authority Provider 未授予的能力。

推论：

- effective authority 不属于 State；
- references 只能请求或收窄；
- fork/delegation attenuate；
- merge 不并集权限；
- standing 与 capability 正交。
- authorize 只能消费 ScopedAuthorityRef；permit issuance 给 revocation 一个可检验的 linearization point。

攻击测试：在 State、prompt、agent profile、framework checkpoint 中伪造 grant，live contact 仍被拒绝。

### Law 6 · Mediated contact

> 每次越过 runtime 边界都必须按其 contact profile 被中介：external ingress 经 authenticated admission；model/external-effect egress 与 canonical write/publication 经 exact-final authorization、protocol execution 和 evidence；decision actor 只能使用 scoped capability 提出 intent/proposal。

推论：

- external payload 未接纳为 InputEvidence 不能成为 Continuation cause；
- hooks 不是硬边界；
- middleware 后修改必须重新绑定 digest；
- world effect 使用 intent/receipt bracket 与 fence；
- counterfactual/simulation binding 不得接触 live world，除非经过显式 realm promotion；
- model contact 使用 durable attempt/outcome bracket；
- canonical commit/publication 只接受 admitted transition + authorized publication batch；
- internal agent 无旁路。

攻击测试：callback 授权后修改 tool args/model request，final gateway 必须拒绝或重新授权。

### Law 7 · Origin-independent mediation

> Internal agent、第三方 framework、deterministic workflow 与 human-facing decision actor 都不能因 origin 获得 ambient bypass；替换 actor 不改变 History/Authority/Effect ontology。实际 capability set、handoff 与 isolation 由 binding/IntegrationContract 显式决定，不要求同权或同 interface。

推论：

- 新 framework 只增加 adapter/driver；
- runtime core 无必填 AgentId；
- manifest 从实际 wiring 生成；
- internal fast path 是架构违规。

攻击测试：reference actor 与第三方 fixture 运行相同 gateway/admission attacks；内部实现不得取得其显式 binding 未授予的 raw handle。不同 principal 拥有不同 capability 是合法结果。

### 9.1 当前 Twenty Laws 如何降解

| 当前 law | 新归属 | 处理 |
|---|---|---|
| 1 One semantic source of truth | Laws 1、3、4 | 改写：semantic State、causal evidence、continuation condition 分开，不再用 “State or Frame” 兜底 |
| 2 A node is not a state | History structural rule + Law 1 | 保留为 core construction rule |
| 3 Same canonical content, same identity | History conformance | 保留；属于 encoding/addressing protocol，不升格为跨层 law |
| 4 Compiled context is a view | Laws 3、4 | 加强为 resolved/materialized/IR/rendered 四段 |
| 5 History is immutable | Law 1 | 直接吸收 |
| 6 Preserve provenance | Law 2 | 直接吸收并扩到 decisions/contacts |
| 7 Evidence is canonical, not cognition | Laws 2、3、4 | 修正 canonicality/standing 的正交关系 |
| 8 Compaction does not destroy | Law 1 + retention protocol | 保留原 history/evidence reference；受合法 erasure/availability 限制 |
| 9 Effects are not transactions | Law 6 + Tool contact profile | 保留为 world failure protocol |
| 10 Forking state does not fork world | Laws 5、6 + realm protocol | 保留 |
| 11 Parallelism is not branching | concurrency/OCC protocol | 不是所有实现的本体 law |
| 12 Conflict is information | merge/domain protocol | 保留为 semantic construction rule |
| 13 Models propose; runtime commits | Law 6 | 泛化到所有 Decision Drivers 与 contacts |
| 14 Authority is attested, never authored | Law 5 | 直接吸收 |
| 15 Power only narrows | Law 5 | 直接吸收；expansion 只能来自 Authority Provider 新 decision |
| 16 Approvals bind to what was seen | Laws 5、6 + approval protocol | exact product 的特例 |
| 17 Frameworks are adapters | Law 7 | 加强为 internal/external driver parity |
| 18 Derived state is disposable | Law 3 | **修正**：rebuildable projection 可丢；已被 contact 引用的 exact artifact 是 causal evidence，不可当 cache 丢弃 |
| 19 Reachable is forever | Law 1 + retention/availability protocol | **修正**：logical identity/provenance 保留，payload 受 redaction/erasure；不再绝对承诺 bytes forever |
| 20 Prefer structural simplicity | construction principle | 留在 review checklist，不作为 semantic invariant |

这会把“law”从二十条记忆清单收缩为七个能攻击的 invariant，同时不丢掉现有工程纪律。

---

## 10 · 目标依赖图

逻辑模块先于物理 package：

```text
history-contracts        authority-contracts       context-contracts
       │                         │                        │
       ▼                         ▼                        ▼
history-engine             authority-adapter       context-resolver
       │                         │                        │
       │                         └─────────┬──────────────┘
       │                                   ▼
       │                           compiler / renderers
       │                                   │
       └──────────────┐                    ▼
                      │        scoped-capability contracts
                      │                    │
                      ▼                    ▼
                 mediated-runtime / execution coordinator
                      │                    │
             ┌────────┴───────┐      ┌─────┴────────┐
             ▼                ▼      ▼              ▼
       model adapters   tool adapters agent-host  framework adapters
             └──────────────────┬───────────────────┘
                                ▼
                         product composition root
```

严格规则：

- `history-contracts` 不依赖 agent/context/compiler/authority/provider/session/product；
- compiler 不依赖 Store、runtime、agent、model provider；
- scoped actor/capability contracts 不依赖 Store、kernel implementation 或 raw executors；
- mediated runtime 依赖 ports，不依赖 `PostgresStore` concrete type；
- agent-host 与 framework adapters 位于 scoped capabilities 之上；
- product composition root 可以高 fan-in，但依赖不得反流。

### 10.1 当前 coupling 与目标 seam

| 当前 coupling | 问题 | 目标 |
|---|---|---|
| `packages/domain` 导出 Agent、Frame、Invocation、Effect schemas | 一个 package 同时承担 History core 与上层协议 ownership | 先用 subpath/internal ownership 分区；最后再决定物理拆包 |
| `compiler → FilesystemBlobStore/ScopedStateView` | gather、compile、artifact persistence 混合 | `ContextSource` + pure compiler + `ArtifactSink` coordinator |
| runtime `DomainModule.compilerSources` 复制 compiler category/authority/stability | transition/domain registry 拥有 cognition taxonomy | generic context-source contribution 由 context layer 解释 |
| `runtime → PostgresStore` | engine contract 绑定 persistence concrete | `PublicationBatchPort` / `ScopedHistoryView` adapter |
| `ai → kernel + Store/blob` | provider contact、authority、evidence persistence 混合 | runtime-owned `ModelGateway` + scoped model port；artifact/evidence sink 注入 |
| `tools → runtime + kernel + Store` | world bracket 与 concrete backend 纠缠 | 保留 execution protocol；通过 effect/dispatch ports 注入 |
| `agents → compiler + kernel + runtime + store` | AgentGraph 成为第二 composition root | Agent semantic extension、Agent control host、scoped capabilities 分离；DecisionDriver 只作 resident profile |
| `host/langgraph adapter → PostgresStore` | adapter 获得比其 semantic contract 更大的能力 | `HostCheckpointPort` / `HistoryPublicationPort` |
| `product` 高 fan-in | 本身不是问题 | 明确它是唯一 composition root，不把 dependencies 下推 |

### 10.2 不立即做 package rename

先做到：

1. interfaces 只引用允许的 contracts；
2. architecture import test 通过；
3. 至少两个 consumer 使用同一 seam；
4. concrete import 被 composition root 吸收。

然后才决定新 package。否则只会把循环依赖搬成跨 package 循环。

---

## 11 · 对两个现有设计的取舍

### 11.1 当前 v0.9 应保留的资产

- State 与 Node 分离；
- State content addressing、canonical encoding 与 golden vectors；
- immutable Transition/Invocation/Effect evidence；
- scoped reads、read traces、OCC 与 merge semantics；
- Postgres canon/proj/ops 与 transactional publication；
- intent/receipt effect bracket、executor classes、fencing、reconciliation；
- authority state 在 tree 之外，self-grant 防线；
- availability ledger、redaction/retention honesty；
- replay nondeterminism seam；
- Context Frame、compilation witness 和 exact compiled bytes 的审计意识；
- host adoption coverage 的诚实原则；
- Temporal 只承载 operational execution，不成为 semantic history。

这些不因术语重构而重开。

### 11.2 `context-runtime-spec-v0.1.md` 应吸收的部分

- Context 是从 history fold/project 出来的，不是 mutable container；
- provider wire format 是 render dialect；
- content-addressed immutable history 与 fenced publication protocol；
- schema-on-read / compile-time placement；
- agent/session 是上层构造，不是本体；
- compile 结果可寻址且可审计；
- operator 可替换，lineage identity 不住在 model 中。

### 11.3 必须修改的部分

| v0.1 提案 | 新决定 |
|---|---|
| `Kernel.compile/render` | 移出 History Core，进入 Context Pipeline |
| `moment = one LLM step` | 降为 optional MomentProfile；Transition 不假定 LLM |
| total authority lattice | 拆为 provenance、standing、epistemic、capability；effective authority 外置 |
| effect decisions 写入 Moment meta | 上层 execution evidence 引用；History 不解释 effect schema |
| structure 强制单亲 | 保留 primary basis + secondary causal parents；不破坏现有 merge |
| store 是绝对 grow-only set | semantic immutability 保留；availability/redaction/tombstone 由已有协议处理 |
| compile 纯性要求所有 retrieval 先变成 event | 改为 effectful materialization + frozen snapshot；不必污染 semantic State |
| agent/session 都是 ref 用法 | 可以是 host profile，不是 universal ontology |

---

## 12 · 迁移计划

原则：每一 phase 都必须可单独合并、验证和停止；不得要求“大重构完成后才恢复正确性”。

### Phase 0 · Protocol baseline，不冻结未经证明的 interface

产出：

1. ADR：Context 不是 History Graph；agent/framework 是 scoped decision actor；runtime owns contact/publication protocol。
2. 将 Seven Laws 写成 **proposed constitutional baseline**；所有 adversarial tests 落地后才 freeze。
3. 写术语表与冲突映射：`HistoryCore/HistoryEngine` 对现有 Authority `Kernel`；Resolution/Materialization/Conditioning identities；contact/permit/publication batch。
4. 写 storage/lifecycle class、overlapping history role、standing/authority/availability 轴与两个 sovereigns。
5. 冻结 `ContentAddress/CanonicalReference` profiles、generic envelope/links、legacy companion mapping、schema ownership/version inventory 与 public export owner。
6. 生成 **全 package** landing/allowed-edge matrix，覆盖 memory、terminal、session、host、workers，而不只列已知 coupling。
7. 把 predecessor plans/spec 放入 durable workspace 或 pin immutable source；生成 claim-by-claim supersession appendix。
8. 为每个 phase 创建可执行 acceptance command/file；pending/TODO fixture 使 gate 失败。

第一批 forbidden edges：

```text
history-core  -X→ agents/compiler/ai/tools/session/product
compiler      -X→ PostgresStore/FilesystemBlobStore/runtime/agents
driver        -X→ Store/kernel implementation/raw providers/raw executors
```

验收：

- 每条准备冻结的 law 至少有一个正在执行的 adversarial fixture；
- 所有 current schemas 被分配 owner；
- address/version/package inventories 无空项；
- 不发生 canonical ABI、SQL migration 或 runtime behavior change；
- 旧 plan 与 v0.1 中被 supersede 的断言有明确映射。

### Phase 1 · History perimeter

产出：

1. `HistoryReader`、`ScopedHistoryView`、`PublicationBatchPort`、`RefAdmin` contracts；
2. 当前 `PostgresStore` 的 thin adapters；
3. generic `CanonicalEnvelope/links`、EvidenceAnchor/contact journal、extensible evidence kind/retention registry；
4. `HistoryNode` primary-basis/causal-parent view 与 availability protocol；
5. history-only supported subpath/package 与 in-memory conformance adapter；
6. 无 agent、compiler、model、session 的 micro-host fixture。

迁移：

- 本 phase 只交付 contracts/adapters/micro-host；Runtime/Host constructor inversion 留给 Phase 6；
- Store concrete 仍存在于 product composition root；
- 不改 frozen Store migrations；
- `PublicationBatchPort` 适配而不简化现有 durable turn/fence/recovery transaction logic。

验收：

- micro-host 能 bootstrap/create-ref、open/commit/recover/publish/branch、fork 与 diff；semantic merge 由 adopter-supplied service 负责，不由 opaque History Core 解释；
- lost ACK、stale worker、kill-between-step-and-publish、unresolved effect、prefix OCC 与 host adjunct 原子性 drills 通过；
- unknown upper-layer schema 在 refusal 后仍经 envelope/anchor survive GC/transitive redaction；
- redaction/restore/identical-digest-different-namespace drills 通过；
- 删除所有 projections 后仍从 History 重建；
- History contracts 中没有 AgentId、ContextIR、model/tool/provider 类型；
- Postgres 与 in-memory adapter 通过同一 semantic conformance suite。

### Phase 2A · Authority、Invocation 与 ingress compatibility bridge

产出：

1. Authority v2：binding-scoped snapshot、ScopedAuthorityRef attenuation/intersection、exact-product decision、one-use permits、reserve/settle/release/reconcile；
2. `authority-port/v3` RPC、legacy adapter、v1/v2 decision readers，并更新 agent/store 中重复的 strict parsers；
3. 新的 versioned `InvocationRecordV2` family：common index fields、driver/binding/conditioning/product、attempt/outcome union；
4. `InvocationRecordAny` reader、Store indexing/Transition citation、legacy replay vectors；
5. `InputEvidence/v1`、BindingAttestation、freshness/replay claim 与 secret-free projection；
6. `LegacyContinuationEnvelope`，显式组合 `{frame, universe, inputNode, binding, cause, contextPolicy}`。

验收：

- 两个并发 model attempts 不能超卖一个 budget reservation；crash 后 settle/release/reconcile idempotent；
- attenuation 后 authorize 不能回到 raw snapshot；merge authority 是 intersection；
- Alice evidence 不能绑定 admin/其他 tenant/更高 realm；
- legacy records bytes 不变；缺 companion evidence 的 historical frame 解码为 partial/unresolvable，不伪造完整 provenance；
- no-Agent invocation 可以被 Store index、Transition citation、replay/verify 正确读取。

### Phase 2B · Continuation Resolver

产出：

1. `ContinuationRequest/v1` 与 `ResolvedContinuation/v1`；
2. provider-neutral `AuthoritySnapshotRef` / `ScopedAuthorityRef`；
3. availability、retrieval、effect catalogue、model profile、resolved policy snapshot refs；
4. `ContextResolver` 与完整性校验；
5. `LegacyContinuationEnvelope → ResolvedContinuation` compatibility adapter；
6. ResolutionId golden vectors。

策略：

- 现有 `ContinuationFrame` bytes 不改；
- new InvocationV2 可同时记录 legacy frame digest 与 new resolution ref；
- 先 shadow-resolve，不改变 compile/model path；
- snapshot 不包含 secret。

验收：

- 同 State、不同 Node/binding/snapshot 得不同 ResolutionId；
- revocation 不改变 StateId，但新 Context 使用新 authority snapshot；
- DAG 中伪造 grant 不影响 resolved live authority；
- replay 可读取历史 snapshot/decision evidence，无需恢复 credential。

### Phase 3 · Effectful gather、candidate admission 与 pure compiler core

产出：

1. `ContextSource` / `SourceObservationBundle` / runtime-owned `CandidateAdmission` / `MaterializedCandidates` ports；
2. provenance、epistemic、standing、stability、availability 的独立 contracts；
3. `ResolutionId` / `MaterializationId` / exact `CompilerInputV1`；
4. private/versioned ContextIR seam；有第二 renderer/handoff 前不冻结 public IR；
5. 新 family 或 current monotonic next version 的 `CompilationRecord`，记录 selected/rejected/demoted、feature、budget、placement decision；不得倒退使用已被 v4/v5 占用的 `v2`；
6. pure `compile()`；
7. pure renderers 与 dialect loss record；
8. coordinator-owned ArtifactSink。

迁移：

- 把 `ScopedStateView` reads 移到 materializer；
- 把 `FilesystemBlobStore.put` 移到 compiler 调用者；
- 在同一 phase 把 agent profile/scoped gathering 移成 ContextSource contribution；先 gate `compiler/core` pure subpath，legacy root 保持 facade；
- 现有 compiler 与新 compiler 只在 no-contact shadow mode dual-run：消费 captured/taped inputs，写隔离 derived namespace，不做 fetch/预算 reservation；
- 用 compatibility renderer 比较 final provider projection + allow-listed semantic delta，不比较不同 schema 的 raw record bytes；
- `DomainModule.compilerSources` 兼容映射为 context-source contributions。

验收：

- `compiler/core` 不 import Store/runtime/agent/provider；
- 相同 CompilationKey 逐字产生相同 IR/record；
- cross-locale golden 使用固定 UTF-8/code-point ordering，禁止 `localeCompare`；
- standing 不由 stability 或 provenance 单独推导；
- source 自报 provenance/eligibility/decision 无效；低 provenance 内容不能未经 runtime-owned placement decision 进入 instruction standing；
- contested component 保持 epistemic completeness；
- unavailable partner 进入 omission/explanation 而不伪造 replacement bytes；只 hydrate selected content；
- demotion/refusal 后 budget accounting 正确；
- renderer 对 unsupported standing/opaque item 给出稳定 loss record。

### Phase 4 · Exact-product gateways 与 publication admission

产出：

1. exact `FinalModelProduct` / `FinalEffectProduct` / `FinalTransitionProduct` / `RefPublicationProduct` descriptors；
2. runtime-owned ModelGateway：final transform 后 authorize/reserve，durable attempt 后 contact，ordered partial/outcome capture；
3. runtime-owned EffectGateway facade，复用当前 durable effect bracket并承载 read-only world fetch；local contact 在 Store guard 后消费 permit，durable contact 传输 frozen request、exact product 与 permit admission，由 worker 重新绑定后执行 Store guard → consume → driver，caller 只接受 shared-ledger attestation；
4. Proposal admission + PublicationBatch coordinator；
5. durable admission/contact refusal evidence、EvidenceAnchor 与 navigable trace；
6. replay mode 作为 gateway input，而不是 manifest label；
7. no-contact verification/evidence-resume 与 fresh-identity re-execution paths。

迁移：

- Authority/Invocation bridge 已在 Phase 2A 落地，本 phase 才切换实际 contact；
- 保留当前 tool/effect 与 publication transaction SQL，通过 protocol adapter 暴露，不重写成 GenericEffectEngine；
- 先迁移 HostPublisher 或把它机械标记为 external coverage；不得在“only ProposalSink commits”下保留 silent direct-write exception。

验收：

- middleware/callback/prepareStep 修改 payload 会触发新 product/decision；
- durable model attempt 前零 provider contacts；所有 crash windows 返回 completed/definite/unknown，不盲目重复付费；
- abort before token、mid-stream、after paid usage、after evidence before delivery 都有 typed durable outcome；
- redaction after render/before send 使 egress permit 失效；
- effect contact 在 durable intent/fence 之后；
- production outbox recovery 只能启动 permit-bearing mediated workflow；旧 direct Activity 在配置 worker permit ledger 时 fail closed；
- staged effect 的 decision 必须绑定 effect 自己的 kind/audience，而不是继承 command publication audience；
- transition commit 与 ref publication 分别精确受权并由同一 batch protocol关联；
- verification replay 断言 provider/executor 零调用；re-execution 使用新 identity/authority/budget；
- semantic refusal durable，但不自动获得 cognitive standing。

### Phase 5 · Scoped decision actors 与 step protocol

产出：

1. independent `SingleGenerationModelLease`、`EffectBatchLease`（scoped effect capability）、`ProposalSink`、`ScopedControlPort` capabilities；registered framework tool wrapper 只是 `EffectBatchLease.invoke` 的窄 adapter；
2. activation/attempt/stable operation identities、port audience/expiry/revocation；
3. `StepCoordinator` 与 `driver-reentry | enclosed-loop` profiles；
4. deterministic resident reference driver（`DecisionDriver` 保持 optional profile）；
5. current reference agent/terminal adapter 与至少一个 external fixture；
6. compile-time negative fixtures + API-contained conformance suite。

验收：

- actor public types 不引用 raw Store/Authority implementation/provider/executor/credential；
- framework state update 只能成为 local state、captured persistence fact 或 Proposal；
- internal reference agent 无 direct dispatcher/engine access；
- deterministic workflow 可不提供 AgentId 或未使用的 fake ports；
- one-step port 在 observation/yield/abort/completion 后 server-side 失效；
- LangGraph restart、AI SDK/ADK enclosed step 用 stable operation id 返回已有 outcome，不重复 effect；
- internal/external 经过同一 gateway/admission attacks，但 capability sets 可以不同。

### Phase 6 · Runtime 与 concrete Store/kernel 解耦

产出：

1. `TransitionEngine` 构造函数改依赖 History/Authority/Evidence ports；
2. HostPublisher、LangGraph saver、memory、session、terminal 等改依赖 purpose-scoped ports；
3. model/effect execution workers 只持有其需要的 worker-side capability；
4. product 成为明确的 composition root；
5. package dependency guard 覆盖 source 与 built exports。

迁移：

- 逐构造函数替换，不改变 transaction SQL；
- concrete adapters 保留在 Store/runtime integration package；
- 旧 constructors 暂用 deprecated compatibility factory；
- 每替换一条 path，跑原 crash/tenancy/recovery suite。

验收：

- core TransitionEngine 单测通过 protocol-faithful port fixture 运行；in-memory adapter 不得因缺少 fence/OCC/recovery 而降低语义；
- framework adapter constructor 不接收 raw Store；
- Runtime coordinator 不持有 credential；credential 只在 provider/executor adapter；
- 当前 Postgres/Temporal conformance 全绿；
- 无新 dual-write seam。

### Phase 7 · Agent semantic extension 与 control host 分离

产出：

1. Agent semantic schemas/reducers 的明确 owner；
2. Agent control repository：queue/lease/retry/status projection；
3. `AgentDecisionDriver` optional resident profile；
4. Agent profile 作为 ContextSource contribution；
5. spawn/delegation 通过 AuthorityProvider attenuation；
6. current `AgentStore` 分成 canonical adapter 与 control adapter。

迁移：

- 保留历史 AgentRecord/SpawnEdge bytes；
- 从 `packages/domain` 的 core export 面移除 agent 假设时采用兼容 subpath；
- `AgentGraph` 不再直接组合 compiler/kernel/runtime/store concrete；
- scheduling 与 semantic lifecycle 分开测试。

验收：

- History library 在完全不安装/引用 agent-host 时工作；
- agent semantic bytes 可在 generic history 中 round-trip；
- 丢失 control DB rows 可从 canonical history/host policy 恢复调度，而不改变 semantic State；
- agent spawn 不能通过 State 自授权限；
- reference agent 与 external actor 保持 origin-independent mediation；显式 capability 可不同。

### Phase 8 · Framework adapters 与 executable coverage

产出：

1. `IntegrationContract` schema；
2. version/feature-pinned conformance suite 生成 Declared/Observed/Enforced coverage，不接受手写夸大；
3. LangGraph：现有 Level 0 + full hosted spike + resident driver spike；
4. AI SDK：runtime-backed facade + resident tool loop spike；
5. ADK：hosted wrapper mapping + resident driver mapping；
6. peer fixture；
7. address-space-separated child-process spike；
8. egress-contained hostile-driver spike（OS sandbox/default-deny egress，不以 worker thread 代替）。

验收：

- 同一 framework 可拥有不同 control ownership，而 ontology 不变；
- loop owner 与 effect/canonical owner 可独立表达；
- LangGraph checkpointer/Store/updateState/pending-writes 分别分类；interrupt restart 不重复 operation；
- AI SDK dynamic prepareStep model/message/tool substitution 受最终 adapter 控制；
- ADK restricted Runner 无 credentialService，memory/artifact/session services 明确 scoped/external；
- 未包装的 model/effect 或 ambient service 自动降低 coverage；
- ContextIR 后追加未记录 prompt 时不得声称 `rendered`；
- peer response 不继承 caller authority；
- address-space-separated 不虚报 hostile-code isolation；
- egress-contained fixture 无 ambient filesystem/network/socket/FD/credential/Store access，只能 authenticated scoped RPC。

### Phase 9 · Compatibility retirement 与规范冻结

只有前八 phase 的 conformance 通过后：

1. 决定除已支持 history-only export 之外，是否进一步物理拆分 `domain`、`runtime`、`agents` packages；
2. 只冻结已有两个真实 consumer + golden/conformance 的 Context/IR/Integration schemas；未满足者保持 internal/experimental；
3. 更新 `specs/plan.md`，将旧 Final Architecture 替换为新结构；
4. deprecate `Kernel.compile/render` 类叙述、旧 authority enum 与 raw constructors；
5. 删除 dual-run/shadow paths；
6. 保留旧 canonical readers，禁止改写历史 bytes。

验收：

- 所有 public compatibility removals 有迁移说明；
- historical replay/verify 全绿；
- 新 architecture dependency graph 无逆向边；
- 删除 reference agent 后，History + Context + Runtime conformance 仍可独立运行；
- 替换 framework、compiler、authority adapter 之一不修改 History schemas。

---

## 13 · Conformance matrix

### 13.1 History

- 相同 semantic content 得相同 StateId；
- Node 与 State identity 不混淆；
- primary basis/secondary causes round-trip、same-universe、unique、acyclic；
- publication batch 的 fence/OCC/dedupe/recover/effect gate/adjunct 原子性可验证；
- ref publication 只有一个赢家，败者显式 branch/race；
- opaque evidence links/anchors 在无 semantic Node 时保持可达；
- projection 全删可重建；
- unavailable/redacted bytes 不在 exact namespace/address 下复活。

### 13.2 Context

- ResolutionId 覆盖 resolver input，MaterializationId 覆盖 exact source results，ConditioningId 覆盖实际 model input；
- resolver 捕获每个 effectful dependency；
- policy/profile hydrated bytes 与 pinned refs 一致；source 不能伪造 provenance/placement；
- compile/render 对冻结输入纯；
- selected/rejected/demoted 与 budget 可解释；
- placement、epistemic completeness 与 dialect loss 可测试；
- compile cache 不跨 authority/availability/model profile 错误共享。

### 13.3 Authority

- State/self-authored grant 不生效；
- revocation 无需修改 History；
- exact product mutation 使旧 decision 失效；
- authorize 只消费 scoped authority；delegation attenuate、merge intersect；
- permit issuance/consumption 与 revocation 的 linearization 可验证；
- budget reserve/settle/release/reconcile crash-safe；
- redaction 在 egress 前使 stale read permit 失效；
- replay 使用 decision evidence，不恢复 secret；
- credentials 不出 provider/executor process。

### 13.4 Decision actor

- 无 raw Store/kernel/provider/executor types；
- internal 与 third-party fixture 同 gateway/admission attack suite，capability set 可不同；
- driver-local state 不自动 canonicalize；
- model/effect output 只能成为 observation/proposal material；
- activation/operation identity 在 restart/resume 下稳定；late port call 被拒；
- abort、failure、suspend 有 typed outcome；
- controlOwner 改变不改变 History ontology。

### 13.5 Contact/Execution

- inbound payload 的 authenticated source/binding、normalization 与 admission 可追溯；
- authorize final product；
- authorize 与 contact 之间 mutation 被检测；
- durable model attempt 先于 contact；completed/failed/unknown/partial evidence 与 delivery recovery 可验证；
- effect intent-before-dispatch；
- executor-class-specific reconciliation；
- stale fence/revoked decision 拒绝；
- canonical commit 经 reduce/authorize/verify/PublicationBatch；RefPublication 独立受权；
- verification replay 零 contact，re-execution 使用新 identity；
- crash drills在 local 与 Temporal backend 语义等价。

### 13.6 Integration

- manifest 绑定 framework/adapter/version/features，并区分 Declared/Observed/Enforced coverage；
- bypass fixture 自动降级；
- LangGraph/AI SDK/ADK adapter 不引入 core types；
- hosted 与 resident 可以达到 configured-path governance；untrusted actor 只有 egress-contained 才能声称 enforced no-bypass；
- Level 0 checkpointer 不虚报 invocation/effect/authority coverage；
- persistence、streaming、resume/replay surfaces 逐项声明；
- address-space-separated 不冒充 sandbox；egress-contained actor 无 ambient egress/credential。

---

## 14 · Rollout 与兼容原则

### 14.1 先 shadow，后切流

Context Resolver、new compiler/IR、integration manifest 都先 shadow-run，但 effectful shadow 只能使用 captured/taped inputs：

```text
old path executes
new path consumes captured inputs in isolated derived namespace
no network/effect contact and no authority budget reservation
compare compatibility-rendered provider projection / decisions / allow-listed loss
record mismatch
do not affect live outcome
```

达到 golden + production trace equivalence 后才切换。

### 14.2 Canonical schema 只增不改

- 历史 v1 records 保持原 bytes；
- 新语义需要新 format/version；
- adapter 可以读旧写新；
- 不给旧 schema 添加 optional field 后假装 identity 未变；
- frozen migration policy 继续有效。

### 14.3 Ports 先于 packages

同一个 concrete class 可以暂时同时实现旧/new interfaces；先改变依赖方向，再决定目录位置。

### 14.4 每 phase 的 stop rule

出现以下任一情况则停止该 abstraction：

- 只有一个 consumer，且没有 correctness/security gate；
- port 只是把 concrete methods 原样搬运；
- 需要破坏 frozen bytes 才能证明价值；
- 新 interface 不能生成更强 conformance claim；
- 新层增加了第二个 authority/commit/effect path。

---

## 15 · 已决与仍需实验的问题

### 15.1 已决

1. Context 不是 DAG；DAG 是 History substrate。
2. History Core 不含 compile/render、Agent、tool loop 或 authority policy；仓库不新建第二个含糊的 Kernel noun。
3. Effective authority 永远不属于 State/History。
4. Agent/framework 是 non-authoritative scoped decision actors；`DecisionDriver` 只是 optional resident profile。
5. Internal reference agent 不得旁路 scoped ports。
6. Framework 可以拥有 loop，但每个 model/effect step、canonical commit 与 ref publication 仍经过 runtime protocol。
7. Resolver/materializer 可以 effectful；compiler/renderer 必须 pure。
8. Model、external effect 与 canonical commit 共享 contact law，但保留不同 failure protocol。
9. ResolutionId、MaterializationId、CompilationKey、RenderKey 与 ConditioningId 分开。
10. 本轮 TypeScript-only，不做跨语言设计。
11. 当前 OCC、merge、effect bracket、fencing、replay、availability/redaction 语义保留。
12. `IntegrationMode` 只作 shorthand；保证由正交 wiring contract 表达。
13. History write boundary 保留 durable publication batch/fence/OCC/recovery protocol，不退化为 `commit + CAS` CRUD。
14. Opaque upper-layer evidence 通过 kernel-readable envelope links/anchors 保持可达，History 不解释 payload semantics。

### 15.2 需要 probe，不靠审美决定

1. 新逻辑 modules 最终是否需要物理拆包；
2. 第二 renderer/handoff 是否证明 public ContextIR 及其最小 standing vocabulary；
3. 哪些 exact rendered bytes 长期保存，哪些只存 recipe + digest；
4. CompilerInput 在第二实现后能安全删除哪些字段；在此之前只允许过度区分；
5. egress-contained TypeScript driver 的可移植 OS/container sandbox 机制；worker thread 已明确不合格；
6. framework-added prompt/message 如何转换为完整 placement evidence；
7. semantic refusal 默认是否进入下一 Resolution，还是只在显式 selection 时进入；
8. Agent control state 的最小可恢复集合；
9. 何时把 `NodeRecord.parents` 的 primary/secondary distinction 升为新 schema，而非 reader convention。
10. model provider 能否提供 idempotency/query/reconciliation；不能时哪些 crash outcome 必须保持 unknown/manual。

每个问题必须以 fixture、trace 或第二 consumer 作答。

---

## 16 · Definition of Done

这轮重构完成的判断不是“代码移动完了”，而是以下反事实全部成立：

1. 一个非 agent 系统只安装 History contracts/adapter，就能使用 immutable state、transition evidence、publication batch、branch、diff、refs，并注入自己的 semantic admission/merge policy。
2. Runtime 在没有 reference AgentGraph 的情况下，能运行 deterministic scoped decision actor；无需 AgentId 或 fake model/tool ports。
3. LangGraph、AI SDK 或 ADK 可以决定 control flow；configured integration 拿不到 Store、credential、raw AuthorityKernel 或 raw executor，hostile code 只有 egress-contained 才声明 enforced no-bypass。
4. 每次实际 model/external-effect contact 都能导航到 stable attempt/operation、ConditioningId/exact product、scope/permit、partial/terminal/unknown outcome 与 usage/reservation。
5. 每个 external Continuation cause 都引用 accepted InputEvidence；internal contact/transition/timer/refusal 使用相应 typed cause；每次 canonical State change 都从 Proposal 经 admission 产生。
6. Revocation 与 permit issuance 有明确 linearization：未取得 permit 的 next contact 被阻止；已线性化 permit 按 one-use/expiry contract 处理。
7. 删除 projection/index/cache 可精确重建；operational fence/attempt/lease 丢失只能 fail closed 或 executor-specific reconcile，绝不未经证明自动重发或赋予权限。
8. Compiler 在无 Store、network、clock、authority provider 的纯测试中运行。
9. Reference agent 与第三方 actor 通过同一 gateway/admission attacks；不同 binding 的 capability set 可以不同。
10. 新 framework 只新增 adapter/driver，不修改 History ontology。
11. 新 authority provider 只新增 adapter，不修改 State/Node/Transition ABI。
12. 新 model dialect 只新增 renderer/gateway adapter，不修改 Context/History ontology。
13. 当前所有 crash、race、effect reconciliation、redaction、replay 与 tenancy acceptance 继续通过。
14. Unknown upper-layer schema 与无 downstream State transition 的 paid/refusal evidence 经 generic links/anchors 在 GC、retention、redaction 后仍可解释。

最终架构不再是：

```text
Host → giant Runtime → giant Store/Kernel
```

而是：

```text
                     ┌──────── History Library ────────┐
                     │ immutable state · causality     │
                     │ transitions · refs · evidence   │
                     └──────────────┬───────────────────┘
                                    │
                     ┌──────────────▼───────────────────┐
                     │ Continuation Pipeline             │
                     │ resolve → materialize → compile   │
                     │ → Context IR → render             │
                     └──────────────┬───────────────────┘
                                    │
        framework/reference agent ─▼─ Decision Driver
                                    │ intents/proposals only
                     ┌──────────────▼───────────────────┐
                     │ Mediated Runtime                  │
                     │ exact authorization · contact    │
                     │ effect protocol · admission      │
                     └──────┬───────────────┬───────────┘
                            │               │
                      model/effect       canonical commit
                            │               │
                     external sovereign  History Library
```

这个结构的最优性不来自统一一切，而来自只统一真正共有的 law，并让不可约的差异——semantic history、authority state、world failure、cognition policy、framework control——保持显式。

---

## 17 · Independent review decision log

本稿在开始实现前由八个互不改稿的 reviewer 分别攻击：ontology/laws、History atomicity、Context/compiler、Authority/security、framework interop、effects/replay、migration feasibility、architecture minimality。原始 draft 被判定为“方向正确，但不可 freeze”；本轮修订接受了所有跨 reviewer 重复出现的 P0/P1。

### 17.1 Accepted

1. **保留 protocol-bearing History write boundary**：删除裸 `commit + CAS` 目标，改为 durable PublicationBatch + fence/OCC/dedupe/recovery/effect gate/adjunct atomicity。
2. **Model contact 也必须 crash-closed**：加入 durable attempt、stable call identity、partial/outcome union、budget lifecycle、delivery recovery 与 executable replay modes；仍不与 world effect 共用一个状态机。
3. **History opacity 需要 schema-neutral mechanics**：加入 tagged address、generic envelope links、EvidenceAnchor、availability/retention rules；History 不解释 upper payload。
4. **Identity 分段**：用 ResolutionId、MaterializationId、CompilationKey、RenderKey、ConditioningId 取代过度承诺的单一 ContextId。
5. **Candidate trust boundary 外移**：ContextSource 只能提供 source observations；provenance/availability/placement 由 runtime-owned admission 决定；compiler key 等于 exact observable input。
6. **Authority scope/permit 可执行化**：authorize 只消费 ScopedAuthorityRef；delegation attenuate、merge intersect；reserve/settle/release/reconcile 与 revocation/permit linearization 显式。
7. **Framework contract 覆盖真实 surfaces**：加入 step/enclosed-loop、checkpoint vs semantic/memory、dynamic model substitution、ADK services、restart operation identity、streaming/version/feature axes。
8. **隔离 claim 降噪**：child process 只算 address-space separation；只有 OS-sandboxed default-deny egress 才能对 hostile code 声明 enforced no-bypass。
9. **迁移关键路径重排**：Authority/Invocation/Ingress bridge 前置；final gateways 先于 decision actors；Runtime/Host constructor inversion 不再在 Phase 1/6 重复声称。

### 17.2 Accepted with narrowing

- `DecisionDriver` 保留为 optional resident profile，不再是所有 framework/human/checkpointer 的 universal object。
- 五段 Context pipeline 保留为 protocol artifacts，不进入 History ontology；public ContextIR 等第二真实 consumer 后才冻结。
- History library 提供 structural diff/branch/publication；semantic merge 由 adopter policy/service 提供。
- “complete” guarantee 拆成 Declared/Observed/Enforced 与 Mediation/Cognition/History dimensions；trusted same-process 只能声明 configured-path coverage。
- History 不记录世界真理，只记录 runtime admitted occurrence、claim、observation 与 state transition。

### 17.3 Deliberately not accepted

- 不因 model 也需要 durable attempt，就把 model、world effect、database publication 合成 `GenericEffectEngine`；failure/recovery protocol 仍分别定义。
- 不删除 Resolved/Materialized/Rendered 等 pipeline distinctions；问题是过早本体化和 identity 混用，不是这些 stage 没有价值。
- 不因 in-memory fixture 容易实现，就降低 Postgres 已有的 fencing/OCC/publication/redaction semantics。

### 17.4 Delta re-review verdict

修订后由 ontology、History atomicity、framework interop 三位 reviewer 再做两轮 blocker-only review。最后一轮裁定：各自范围均无剩余 P0/P1；address profiles/legacy companion mapping、ordinary commit/publish proof binding、model/effect batch lifetime、per-attempt replay 与 framework port consistency 已闭合。

At that pre-implementation review, 本稿的状态是：

```text
approved to begin Phase 0 as a non-frozen implementation plan
not approved to freeze public contracts or constitutional claims yet
```

That historical review exit condition required Phase 0–2A executable gates、P0 crash drills 和
source-document supersession mapping before the Seven Laws and public contracts could leave
“proposed”. Those prerequisites were later satisfied, and Phase 9 governance accepted/froze only the
exact machine-registry scope recorded at the top of this document.

---

## 不做什么

- 不把 Agent 重新写进 History core；
- 不把 ContextIR 或 prompt 当 State；
- 不把 authority snapshot 当 grant 本体；
- 不把 provenance、standing、epistemic、stability、capability 合成一个 rank；
- 不让 compiler 读取 Store；
- 不让 driver 直接 model/tool/commit；
- 不让 internal agent 享有隐藏能力；
- 不从 `hosted/resident/peer` 标签推断 coverage；
- 不把 callback/plugin 当 privilege boundary；
- 不用一个 GenericEffectEngine 抹平 model、world 和 database 的故障差异；
- 不把所有 host/framework state 强制 canonicalize；
- 不用 package rename 代替 dependency repair；
- 不重开当前已经解决且有 conformance evidence 的 operational semantics。
