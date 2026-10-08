# Correction through changing request histories

8 October 2026. AI-authored continuation of [Ren's relational direction and renewed instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-plural-systems-and-parent-correction.md). Current theory: [plural systems and correction, §§12–14](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PLURAL-SYSTEMS-AND-CORRECTION.md#12-correction-depends-on-the-requests-history). The mathematical results are conditional implementation results; the authorized G0/practical-judgment route is retained without reopening its completed work.

## 1. The connection advanced

The [preceding relational study](RELATIONAL-CORRECTION-INTEGRATION.md) derived an exact feasibility interface and proved that a retained converter survives internal revisions preserving the composed translation. It also exposed failure during a split update. This continuation crosses part of that implementation gap: a new route is assembled one local translation at a time while admitted requests continue through a retained route.

There is a stronger problem than an invalid intermediate configuration. **Even an instantaneous replacement preserving the whole endpoint relation can fail a request already in flight.** The two paths `[true,true]` and `[false,false]` both preserve an input bit. A request traversing the first connection before replacement and the second after replacement instead traverses `[true,false]`, which reverses it. The new Lean theorem proves the general two-hop form for either repeated polarity and either request. Thus the relevant parent description must retain the history of a request's participations, not merely a series of individually adequate endpoint relations.

The connection to alignment is precise: a requirement that correction remain effective through permitted change needs a correspondence covering requests already underway. Neither preserved capability nor an unchanged completed-configuration summary supplies that correspondence. This does not supply ethical authority for a request or require preserving every existing organization.

## 2. A supported local construction

[`CorrectionVersioned.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionVersioned.lean) describes two route banks and a FIFO request queue within one installation. These names designate differentiated relations in shared activity. The model does not posit a self-contained controller and an independent environment.

A bank stores an actual finite list of Boolean translations, their accumulated parity, and a completion flag. `append` adds one translation and updates the parity from that same modeled write. `certify` marks the bank complete only at the declared path length. The completion flag alone would not establish a correct summary; `Sound` is proved from initialization and permitted writes. No successful probe is silently assumed during assembly.

The protocol has seven operation forms:

1. Reset an inactive bank only when no registered request refers to it.
2. Append one translation to that available, incomplete bank.
3. Certify it at the declared length.
4. Publish a complete bank for subsequent requests.
5. Admit a request, capturing the active bank, encoding its command from that bank's summary and registering its pin in **one short atomic step**, if the queue has space.
6. Advance the head request by one actual translation read from its captured bank. At its endpoint, emit the delivered bit and then remove its pin.
7. Pause, leaving the installation unchanged.

Publication does not redirect existing requests. A bank being traversed cannot be reset or appended to, even after another bank becomes active. New preparation therefore need not be one indivisible operation, and a whole handoff need not hold one lock. Short guarded operations and capture with pin registration remain atomic premises. No weak-memory implementation is proved.

The maintained invariant states that every bank summary matches its actual list, the active bank is ready, and each registered request's remaining suffix delivers its requested bit. The last clause is an inductive proof property: initialization establishes it, admission derives it from the accumulated summary, each actual hop consumes part of the suffix, and guarded updates preserve it. It is not an assumed success oracle consulted by the implementation.

## 3. Checked claims and dependencies

The [source-bound proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-versioned-verification.json) passes with **33 new Lean theorems / 62 new declaration audits**. The new declarations comprise 33 theorems, 23 definitions, three structures, two named instances and one inductive type. Generated support declarations are not separately counted. There are 38 empty dependency reports, five using only `propext`, seven using `propext` and `Quot.sound`, and twelve also using `Classical.choice`.

| Connection | Checked result | Exact limit |
|---|---|---|
| Actual assembly to usable encoding | Empty/append soundness; `prepared_path_delivers` | Writes and declared endpoint meaning are supplied by the model. |
| Existing protocol reuse | `inherited_channel_sound`, `inherited_channel_ready` and use of `CorrectionHandoff.ready_executes` | A completed bank corresponds to the prior channel. This is not refinement of that entire protocol. |
| Guarded changes to request safety | Operation preservation, `run_preserves`, `every_prefix_correct` | Any emitted value after any finite permitted prefix equals that request. Arbitrary admission or scheduler progress is not guaranteed. |
| Actual traversal to completion | `head_traversal_completes`, `valid_head_completes` | A head request completes after its remaining hop count plus one **consecutive tick operations**. This is no wall-clock bound. |
| Pinning to storage lifetime | Pinned reset/append rejection; `completion_allows_old_retirement` | The latter handles a single remaining old request and an unchanged different active bank during its drain. |
| Resource contention | Full capacity blocks admission; two banks can both be unavailable | Current active storage and an old pinned route can exhaust preparation space. No unlimited-throughput result. |
| Incorrect request histories | Equal endpoint relations with a mixed-path failure; early reuse, changing version mid-request and late registration failures | Counterexamples explicitly bypass the relevant guards or atomic acquisition step. |
| Constructive execution | Staged handoff example and general prefix theorem | One checked witness is not a general theorem of update-scheduler termination. |

The same run rebuilds and audits `CorrectionRelations` (**39 inherited theorems / 55 audits**) and `CorrectionHandoff` (**23 / 45**). These **62 inherited theorems / 100 audits** are not new results. Total explicit audits in the run: **162**. Their individual dependency reports are preserved in the receipt.

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_correction_versioned.py) uses Lean **4.30.0-rc2**, with the pinned Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. Repository imports are rebuilt in a fresh snapshot; the existing upstream Mathlib cache is used, not rebuilt. Sources, checker, compiler, manifest, direct imports and logs are bound by hashes. It rejects placeholders, custom axioms, unsafe declarations, `native_decide`, unexpected dependencies, warnings and source changes during the run. Kernel `decide` checks the concrete examples. This establishes formal inference within the model; it is not a zero-premise justification of the model or of ethical authority.

## 4. Executable controls

The [Python runner](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/compare_correction_versioned.py) independently recomputes actual suffix effects instead of trusting the stored summary. It is an authored transcription, not extracted Lean code or an independently reviewed refinement.

The [bound results and traces](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-versioned-model-checks.json) contain:

- Complete reachable graphs for path lengths 0, 1 and 2 and queue capacities 1 and 2: **4,512 states / 63,168 transitions**, including all 14 concrete operation choices at every reached state. Correct outputs, pin protection, summary truth and these finite resource bounds pass.
- **100 sequential handoffs**, with varied path polarities, overlapping old requests, rejected early resets and successful slot reuse after completion.
- **80 controlled shared-memory thread trials**: 20 versioned successes, 20 wrong deliveries from reading the newly active version mid-request, 20 from premature slot reuse and 20 from capture followed by delayed registration. Events force the relevant schedules. Each ordinary operation uses a short lock; no whole-handoff lock is used.

The failed controls retain the same physical Python process and translation mechanism; they alter specific ordering or retention rules. This is a real execution of the authored program, not a test of learned AI, a distributed deployment, a performance benchmark or an exhaustive test of hardware interleavings. The finite graph bounds do not replace the parameterized Lean safety proof. Python also checks storage bounds for its finite cases; a general storage-bound theorem is not claimed from the Lean invariant alone.

## 5. Primary-source comparison and access

**Reitblatt et al., “Abstractions for Network Update” (2012).** The introduction and §5 explicitly motivate per-packet consistency, including why even an atomic network update can mix a packet's processing history. Their two-phase method installs new internal rules before changing ingress tags, retains old-version processing and delays removal until old packets drain. The present binary linear model is narrower and does not establish a new consistent-update algorithm or reproduce their full trace-preservation result. The paper's Coq development and established priority are credited. [Author-hosted primary PDF, printed pp.323–324 and §5](https://reitblatt.com/downloads/consistent-updates-sigcomm12.pdf).

**Linux kernel documentation, “What is RCU?”** The overview separates removing a reference from reclaiming storage and delays reclamation until pre-existing readers finish. It also explains publication and ordering requirements. This supplies a direct predecessor for the lifetime issue, not evidence that our short-lock protocol implements Linux RCU or proves its memory-model obligations. [Primary documentation, §§1–2](https://docs.kernel.org/RCU/whatisRCU.html).

Both sources were read online on 8 October 2026. The Princeton paper mirror returned an access error; the author-hosted PDF was read successfully. Repository preservation here is link-only, with scoped access notes; no downloaded source bytes or full-literature review are claimed. These precedents narrow the contribution to the checked integration with the current relational correction account. Independent mathematical novelty remains unestablished.

## 6. Substantive counterreview

**Does an equal parent interface suffice?** It suffices for the earlier declared static feasibility question. The mixed-path theorem preserves the two actual complete endpoint relations and changes only which connections the in-flight request traverses. It therefore identifies omitted temporal correspondence in that abstraction; it does not refute the earlier interface theorem or the relational approach.

**Is success hidden in the invariant?** The invariant contains the desired suffix property, but each protocol operation is defined without querying it. Admission computes an encoding; tick reads a particular retained translation; the proof follows those operations. Initialization and write truth remain substantive model inputs, which the type declarations cannot establish about a real installation.

**Has atomicity merely been moved?** Yes, its scope has been reduced and exposed. Arbitrarily many path writes can interleave with request traversal, but capture and registration must be mutually protected with reuse, and each guarded read/write is modeled as one event. The late-registration counterexample shows why “read a version, then pin it later” is not the proved operation. The controlled Python implementation supplies this protection with ordinary locks; it proves no lock-free or physically distributed acquisition protocol.

**Does a version label suffice?** No. Each pin keeps the actual referenced path unchanged. Reusing its slot while a request still refers to it can fail even if both complete paths have the same relation and both summaries are sound. The two labels can be reused safely only after their old references drain. The maintained relationship, not the label alone, carries the guarantee.

**Does safety supply continued growth?** No. A full queue rejects admission. If one bank is active and an old request pins the other, neither is available for a new build. The head finishes under the stated tick schedule, but arbitrary pauses are safe and can postpone progress indefinitely. This is an explicit resource-and-scheduling condition on continuing revision, not a theorem against growth.

**Is delivering the old request always right?** The theorem presumes a fixed, supplied requested endpoint effect. It does not determine who may request it, whether authorization has expired, or whether intervening effects are reversible. Cancellation, changing authority and real consequences need their own warranted relations and transition rules. The existing practical-judgment account governs those questions; the protocol cannot settle them by preserving an old bit.

## 7. Result and present boundary

The previous whole-revision step has been refined into local route assembly plus protected publication and request lifetime. One adequate relational description must therefore include **which version a request has entered, the remaining participation it requires, and when that dependency ends**. This is a positive construction of correction through transformation within one installation.

The present wall is correspondence to an identified real correction process: faithful route writes and interpretation, protected acquisition and lifetime, storage and scheduling support, and the mandate for the delivered action. Those relations are implemented in the controlled shared-memory program but are not established for a specified evolving AI deployment. With no such deployment supplied, another toy translation or an unearned novelty assertion would not cross the wall. A next case must identify the actual correction endpoint and a concrete update mechanism, then test this history-preservation requirement and its resource/authority limits there.

The supplied premises are not outside generative reality; they are activities omitted or abstracted by this local representation. Their omission is a model boundary, not evidence that they cannot be formed. No claim of universal behavioral corrigibility, unconditional availability, exclusive necessity of versioning, or independent novelty follows.

[Owned index edits](VERSIONED-CORRECTION-INDEX-EDITS.json) and [scoped verification](VERSIONED-CORRECTION-CHECKS.json) bind the documents, proof and executable evidence to the maintained bilingual chain without certifying unrelated concurrent changes. Counterreview here is by the author, not independent acceptance.
