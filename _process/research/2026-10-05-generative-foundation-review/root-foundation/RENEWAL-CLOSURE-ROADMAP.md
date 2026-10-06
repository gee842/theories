# Roadmap: a formal theory of renewal, stated against closure of constraints

6 October 2026 (UTC). AI-authored research plan at [Ren's request](https://claude.ai/code/project/chan_01BmDYbw7RxNp2ZVVDiux7Jc?thread=cmsg_01BmDYbw7RxNp2ZVVDiux7JcW1djCJrogufe4WCn4RRkXk). Ren set the goal as: *a formal theory of renewal, with one nontrivial theorem characterizing when a process renews its own provision instead of importing it, stated against Montévil and Mossio's closure of constraints.* This document proposes the theorem, the route to it and the tests that could defeat it. It adds no proof. The two small enumerations in §4 are preliminary bounded-horizon checks, not results.

It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). The constraint/flow distinction used below is a timescale-relative articulation of one activity. It is not a split into two kinds of being; §6 Phase 4 is where it gets derived instead of supplied.

## 1. The transition addressed

In the derivation map of [generative grounding](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md), this is the link **organization → its own continuation** (续生): when does activity renew the conditions of further activity, and when must those conditions come from outside?

The existing results bound continuation but do not characterize renewal.

| Existing result | What it gives | What it leaves open |
|---|---|---|
| [U1/U2](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md) (`conditional/ResourceContinuation.lean`) | Unbounded demand needs unbounded provision; with unit demand, provision must arrive in every long enough window | Whether provision is imported or internally renewed (the README says so explicitly) |
| `conditional/SupportNecessity.lean` | Bounded lifetimes plus a supplied strict type rank give a finite deadline; there are also checked examples of a renewing cycle, an infinite acyclic chain and external arrivals | The file states "No finite-graph cycle-extraction theorem is claimed here." The rank is supplied, not derived from acyclicity |
| `NativePortContinuation.lean` (branch `claude/project-thread-x1q9hl`) | The native port obeys U1 with equality; on its own source a potential strictly falls, so it cannot continue indefinitely | The non-renewing baseline. Its contact and gate are fixed, so nothing in it is renewed |
| `FormationClosure.lean` (branch `claude/project-thread-mlqbun`) | A coordinate retained by every step changes only through formation events (`law_constant`, `change_requires_formation`). A contact can form from the port's own recorded failures | Formation of one constraint from waste. The forming mechanism is not itself renewed, so there is no closure |
| `PhaseCycleDerivation.lean` (branch `claude/ground-process-law-za6m9z`) | A change that keeps a finite configuration's distinctions closes into cycles. Three is the smallest period that supports diagnosis. The phase returns after three steps | The phase recurs but the configuration does not, because each step draws on sustaining capacity. **Recurrence is not renewal**, and this is the precise baseline for that distinction |
| `AcquiredInitiationConstraint.lean`; `InitiationFixtures.same_protected_completion_different_generated_relation` ([NONINSTRUMENTAL-CONCERN §15](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONINSTRUMENTAL-CONCERN.md#15-整体积分与局部启动的边界)) | One new start can remove a completion that was reachable (`one_unit_start_forecloses_B`). Two endpoints with the same protected completion and the same final support differ in what they generated: in one, a formed A can never continue | The local projection does not represent the whole. What is missing is a property of the whole configuration: which of its formed conditions can still continue or be renewed |

The gap is exact. We can prove that continuation needs provision, and that an acyclic dependency structure dies. We cannot yet say what *suffices*, or what the precise boundary between renewing and non-renewing organization is.

### 1.1 What this serves: the whole unfolding

Ren has set the research center ([NONINSTRUMENTAL-CONCERN §15](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONINSTRUMENTAL-CONCERN.md#15-整体积分与局部启动的边界); [the whole-integral correction](../../../../sources/15-codex-theory-conversations/2026-10-06-yiti-ren-coformation-completion.md#整体积分的纠正)): **how the whole unfolding generates or damages the conditions of its later realization, renewal and correction.** The object of appraisal is the whole process. Purposes, understanding and evaluation form and change within it. No single expectation, and no sum of expectations, is fixed in advance as the whole's unit of value. An assumption-free universal account of this whole quality is not finished.

研究中心：**整个展开怎样生成或损害其后续实现、更新与纠正的条件。** 评价对象是整个生成历程；目的、理解和评价本身也在其中形成和改变。

The renewal theorem serves this center in a specific, limited way:

- **It supplies a property of whole configurations, not of goals.** Phase 2b defines when a whole configuration (every formed constraint, reserve and stalled structure together) can still renew the conditions of its activity from within. The §15 counterexample shows that no goal-projection captures this. Two endpoints with the same protected completion differ exactly in what they leave able to continue.
- **It covers the conditions of correction too.** Records, readers and other means of correction are constraints in this model: retained coordinates that enable a process and wear over a longer span. So whether correction can continue is decided by the same theorem. This connects the result to the formulation of 智慧 in [THEORY.md §1](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THEORY.md#1-the-foundation): sustaining the conditions under which discernment and correction can continue.
- **It separates generation from damage.** A history step can move a configuration into the renewable region (a closure forms) or out of it (a closure breaks, or a reserve falls below threshold). That gives constructive and destructive regimes a precise, checkable form at this scope.
- **It does not supply the whole quality.** §15.4 rejects maximizing continuation, activity counts or future branches as substitutes for the whole comparison. Renewability is a necessary structural ingredient of that comparison, not the appraisal itself. Proper ending, completion and rest are not failures of renewal. The theorem says which conditions remain possible, not which of them should be kept.

## 2. Closure of constraints, as the comparison point

These are Montévil and Mossio's definitions as published in [*J. Theor. Biol.* 372 (2015) 179–191](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/). They are restated here from memory. The paper's text could not be retrieved in this session (HAL and arXiv refused access), so Phase 0 must check the wording against the paper.

- **Constraint.** An entity C is a constraint on a process A→B at timescale τ when it changes that process and is conserved (symmetric) with respect to it at τ.
- **Dependence.** A constraint Cᵢ depends on Cⱼ when Cⱼ constrains a process that produces or maintains Cᵢ, typically at a longer timescale over which Cᵢ degrades.
- **Closure.** A set 𝒞 of constraints realizes closure when every member depends on at least one other member (it is *dependent*), and at least one other member depends on it (it is *generative*).
- **Openness.** Closure concerns constraints. The processes and flows they constrain stay thermodynamically open.

The account is conceptual and schematic. Rider, ["Closure of Constraints as a Theoretical Model"](https://www.cambridge.org/core/journals/philosophy-of-science/article/closure-of-constraints-as-a-theoretical-model/66F5B26F146D1DF12CB1B3019B50734A) (*Philosophy of Science*, 2024), defends it as a general, schematic model rather than a definition. That leaves room for a precise theorem saying exactly when closure plus openness brings about self-maintenance.

## 3. The target theorem

### 3.1 Model: constraint–flow systems

Discrete time `t : Nat`. The model extends the `EpisodeSystem` of `SupportNecessity.lean`; it does not replace it.

- **Kinds.** Finitely many constraint kinds `Fin n`, with a dependence relation `edge j k`, read "a live j-token can take part in forming a k-token".
- **Tokens (episodes).** Each token has a kind, a birth and an expiry. Its alive span is at most `ℓ(k) ≥ 1` ticks.
- **Formation.** A token born at `t > 0` needs a parent born earlier and still alive at `t`, with an edge from the parent's kind. Forming a k-token makes a demand `m(k) ≥ 1` on the reserve. This is the existing `parent` premise, now paired with a demand.
- **Channel premise (openness through organization).** Provision arrives only through live tokens: arrival at tick t ≤ Σ over live tokens of `a(kind)`. Here `a(k)` is the arrival rate a k-token opens, and non-channel kinds have `a = 0`. The surroundings are an unbounded source (the open case). A finite source is the closed-surroundings boundary already shown in `NativePortContinuation`.
- **Reserve law (U1).** `R(t+1) + m·(births at t+1) ≤ R(t) + arrival(t)`.
- **No imported organization.** After the initial configuration, every token has an internal parent. Raw flow may arrive without limit through channels; organized constraints may not arrive from outside.

**Renewal** means a history from a finite initial configuration in which some token is alive at every tick.

### 3.2 Statement

**Renewal–closure theorem (target).** Assume finitely many kinds, finite spans, positive formation demand, the channel premise and no imported organization. Then renewal is possible from some finite initial configuration **if and only if** the dependence graph contains a cycle C whose kinds have span at least 2, and at least one of the following holds:

- **(E) Excess channel.** Some kind q reachable from C has `a(q)·ℓ(q) > m(q)`: over its life, a q-token brings in more than its formation demands.
- **(B) Balanced closure.** Every kind on C has `a(k)·ℓ(k) ≥ m(k)`.

If neither holds, every history ends by an explicit deadline computed from n, the largest span, the initial reserve and the initial tokens.

Two consequences follow, and they are what makes the result worth stating:

1. **Closure plus openness is not sufficient.** Take a single self-dependent channel kind with `a = 1`, `ℓ = 3`, `m = 4`. It is closed and open to an unbounded flow, and it still ends. M&M's two conditions need a third, quantitative one: the **renewal inequality** `a·ℓ ≥ m`, which links the closure of constraints to the openness of flows.
2. **The timescale separation becomes quantitative.** In M&M, a constraint must be conserved at the timescale of the process it constrains and degrade at a longer one. Here this shows up twice. A kind with span 1 can never be a parent: nothing outlasts the tick in which it acts. And the renewal inequality says a constraint must last long enough, relative to its formation demand and the flow it opens, to bring in its own replacement. So the separation M&M treat as definitional becomes a necessary and sufficient condition.

Two boundary cases are already checked in `SupportNecessity.lean`, and the theorem must keep them. If spans are unbounded, closure is not necessary (an eternal channel suffices). If there are infinitely many kinds, an acyclic chain can continue forever. So **closure is necessary because components degrade and kinds are finite**. That matches M&M's own reason for introducing it.

### 3.3 Why this is the right target

- **It answers Ren's question directly.** Provision as flow is always imported in an open system; U2 already shows unbounded demand needs unbounded arrival. What can be renewed internally is the **channel**, the organized conditions through which provision arrives. The theorem characterizes when that channel is renewed from within, rather than when flow is created from nothing.
- **It is one theorem, not parallel results.** U2 supplies the necessity accounting. `SupportNecessity` becomes its acyclic special case. `NativePortContinuation` is the case where no channel kind is formed at all. `FormationClosure` supplies the notion of a constraint as a retained coordinate.
- **It is exact.** It is an "if and only if" with explicit witnesses on both sides, not just a bound.
- **It can be proved constructively.** Every step is either a finite pigeonhole over `Fin n` with decidable equality, a telescoping sum, or an explicit periodic schedule. The main theorems can therefore keep empty axiom reports. Statements in "born infinitely often" form need classical logic; they become separately labeled corollaries.

## 4. Preliminary evidence (bounded horizon only)

Exhaustive search over strategies (up to 2 births per kind per tick, 60–70 ticks, capped reserve) in `experiments/integrated-correction/general-framework/generative-basis/renewal-closure/preliminary/`:

- **One self-dependent channel kind.** Every tested triple behaves as the theorem says. With `a·ℓ < m` it ended for every initial reserve tried. With `a·ℓ = m` it persisted, provided the initial reserve was at least `a`, a timing buffer that the exact statement must include. With `a·ℓ > m` it persisted from a zero reserve. With `ℓ = 1` it never renewed. This last case is what fixed the "span at least 2" clause.
- **Two kinds** (a non-channel P and a channel Q depending on each other). With `aQ·ℓQ > mQ` it persisted from every reserve tried. With `aQ·ℓQ = mQ` it ended: from reserves 0 and 5 within 70 ticks, and from reserve 20 by tick 100. A balanced channel cannot also cover P, so this closed and open system still ends, as the theorem predicts. See the [README](../../../../experiments/integrated-correction/general-framework/generative-basis/renewal-closure/preliminary/README.md).

A finite horizon cannot certify that a history continues forever. These runs only guard the conventions (inclusive expiry, when arrival can meet a formation demand, span counting) before any Lean work starts.

## 5. Nearest formal work, and what must be new

| Work | Overlap | What this theorem must add, or else concede |
|---|---|---|
| RAF theory (Hordijk & Steel 2004 onward; maxRAF by iterative pruning, unique and computable in polynomial time) | The largest dependence-closed set is the analogue of maxRAF, with constraints as catalysts and flows as food | Degradation spans, the deadline dichotomy and the renewal inequality. RAF has no lifetimes and no flow accounting |
| Chemical organization theory (Dittrich & Speroni di Fenizio 2007) | "Closed and self-maintaining" sets, with self-maintenance as a flux condition | Conditions on histories with lifetimes, instead of a steady-state flux. Phase 3 must show how the renewal inequality reduces to, or differs from, COT self-maintenance |
| Stoichiometric autocatalysis (Blokhuis, Lacoste & Nghe, PNAS 2020; Unterberger & Nghe 2022; to verify in Phase 0) | Flux conditions for net self-production | The constraint/flow separation and degradation timescale. **This is the most likely source of an overlap claim, so it is checked first** |
| Petri nets (repetitive nets and self-covering runs; Karp–Miller; siphons and traps, Commoner) | Decidability of infinite runs; sets that, once empty, stay empty | Read arcs for constraints, lifetimes, and an exact characterization for this class |
| Rosen's (M,R) systems; Letelier et al.; Hofmeyr; Mossio, Longo & Stewart's λ-calculus closure (2009) | Closure to efficient causation, formalized | A quantitative, temporal criterion. These treat closure as a structural or logical property |
| Montévil & Mossio 2015; Moreno & Mossio 2015 (*Biological Autonomy*); Rider 2024 | The concept being made precise | The third condition and the exact iff. The theorem is offered as a precise model of their thesis, not a refutation |

**Honest risk.** The qualitative half (cycle extraction, the largest closed set) is close to standard RAF and graph theory. The contribution has to stand on the exact quantitative threshold under degradation, on the separation counterexample (closure plus openness is insufficient), and on deriving the constraint notion from timescale retention, all machine-checked. If Phase 0 finds the threshold already proved in one of these frameworks with lifetimes, the target shifts to what remains new, and the overlap is recorded.

## 6. Phases

Each phase has a deliverable, an exit test, and a result that would change the plan. Following AGENTS.md, work runs in three lanes around this one connection: **proof** (P), **counterexamples and assumption review** (C), and **comparators and identification** (I).

### Phase 0 — Fix the claim and check prior art (I, C)

- Retrieve and quote the M&M 2015 definitions. Read the stoichiometric-autocatalysis papers, the COT papers on decay and the RAF papers on dynamics with degradation.
- Fix every convention in writing: inclusive expiry, whether arrival at a tick can fund a birth at that tick, span counting, and multiple births per tick.
- **Exit:** a one-page claim note with the exact statement and a prior-art verdict.
- **Changes the plan if:** the threshold already exists with degradation. Then reposition onto the deadline dichotomy, the derivation of constraint from retention, and the machine-checked unification.

### Phase 1 — Necessity, constructively (P)

New package `lean/conditional/renewal/`, importing `GenerativeCore`, `ResourceContinuation` and `SupportNecessity`.

1. **Cycle extraction (closes the gap `SupportNecessity` names).** Any token alive after `(n+1)·L` has a parent chain long enough to repeat a kind. So the realized dependence contains a cycle, and every kind born that late is reachable from a realized cycle. As a corollary, an acyclic edge relation on `Fin n` has the deadline without a supplied rank.
2. **Ending without the renewal inequality.** Sum U1 along the history and charge each channel token at most `a·ℓ`. Kinds with `a·ℓ < m` then have finitely many births, bounded by the initial reserve plus the initial tokens' arrivals. Combined with step 1, if neither (E) nor (B) holds, every history ends by an explicit deadline.
3. **M&M closure is realized.** Restricted to a minimal realized cycle, every member is both dependent and generative in their sense.

- **Exit:** these theorems have empty axiom reports and a checker and receipt in the repository's existing style.
- **Changes the plan if:** off-by-one conventions make the necessity bound differ from sufficiency at equality. Then state the exact equality case as its own theorem, or keep it as a characterized gap.

### Phase 2 — Sufficiency and the counterexamples (P, C)

1. **Explicit schedules.** For (E), keep each kind on the cycle and on the path to q alive by replacing every token at its expiry tick, and form enough q-tokens to cover the rest. Give an explicit bound on the initial reserve. For (B), use a balanced relay around the cycle with a timing buffer of at least `a`.
2. **The separation counterexample** (closed, open, still ends) and the boundary cases: span 1, unbounded spans, infinitely many kinds, a finite source.
3. **Assembly** into the single iff, with the deadline dichotomy.

- **Exit:** the renewal–closure theorem proved, plus a short note mapping each hypothesis to the result that fails without it.
- **Changes the plan if:** sufficiency needs extra hypotheses (for example, a limit on births per tick). Those then enter the statement explicitly.

### Phase 2b — Renewability of whole configurations (P, C)

This phase connects the theorem to the research center in §1.1.

1. **Define `Renewable(s)`.** A configuration s is renewable when some renewing history starts from it, with no imported organization. Characterize this set using the main theorem plus reserve thresholds that depend on the configuration.
2. **Projection is insufficient.** Two configurations can agree on any goal projection (protected completions, final support) and still differ in renewability. Do this first as a constructed instance in constraint–flow form. Then, as a separate interface to prove rather than assume, map the §15 pair from `AcquiredInitiationConstraint`/`InitiationFixtures` into it.
3. **Generation and damage.** Classify transitions by whether they enter or leave `Renewable`, and prove the local conditions for each: a closure forms, a closure breaks, or a reserve crosses its threshold.
4. **Conditions of correction.** Include record and reader kinds as constraints, and show when correction capacity is renewable along with the rest of the organization, and when it is not.

- **Exit:** `Renewable` as a predicate on whole configurations, with a characterization, the projection-insufficiency instance and the transition classification. A written statement says it does not rank histories ethically.
- **Changes the plan if:** the §15 model cannot be mapped into constraint–flow form without losing the relation that distinguishes its two endpoints. That loss would then be recorded as what the constraint–flow representation omits.

### Phase 3 — Generalize toward realistic organization (P, I)

- **AND-dependence.** Forming a kind can require several constraints at once (hyperedges, like RAF reactions with multiple catalysts). The largest closed set becomes a greatest fixed point over hyperedges.
- **Several flows.** Use componentwise accounts, as U2 already does coordinate by coordinate, without merging unlike supports into one number. The renewal inequality becomes a linear feasibility condition, which is exactly where the comparison with COT self-maintenance and stoichiometric autocatalysis is made formally.
- **Canonical organization.** Prove there is a unique largest renewing set, show it can be computed, and show that every renewing history eventually lives within it.
- **Exit:** a stated reduction showing which existing frameworks are special or limiting cases (for example, infinite spans or no channel premise), with the remaining differences named.

### Phase 4 — Join the generative core (P, C)

- **Derive the constraint notion.** Using `FormationClosure.law_constant`, a coordinate retained by every fast step *is* a constraint relative to that process; it changes only through formation events. Build constraint–flow systems from a `Process` whose retained coordinates and formation events satisfy stated conditions. Kinds and spans then come from the dynamics instead of being primitives. This is the nondual step: the constraint/flow distinction is shown to be timescale-relative within one process.
- **Place the native port.** Show the native port plus contact formation has no closure, since the forming mechanism is not renewed. By the theorem it must end or import organization, which matches `port_cannot_continue_indefinitely`. Then build the smallest extension that satisfies (E) or (B) and check it executes.
- **Depends on:** merging the `mlqbun` and `x1q9hl` branches, or importing their modules.
- **Exit:** the renewal–closure theorem instantiated on a process derived inside the core.

### Phase 5 — Identification and exposition (I)

- Translate one or two published minimal models (an (M,R) or chemoton-style model and a small RAF) into constraint–flow form. Compute closure and the renewal inequality, and compare with what those literatures report.
- Write a short paper-form exposition: the statement, the separation counterexample, the timescale reading, the comparison table and the Lean artifact. Integrate the result into `CONDITIONAL-UNIVERSALITY.md`, `GENERATIVE-GROUNDING.md` and `RESEARCH.md`.
- **Exit:** an outward-facing draft that a theoretical biologist can check without reading the rest of the corpus.

## 7. What stays supplied

| Premise | Status after Phase 2 | Where it could be grounded |
|---|---|---|
| Kinds, edges, spans | Supplied | Phase 4, from retained coordinates and formation events |
| Channel premise (arrival only through live constraints) | Supplied law | The native port's contact gate is one instance. The general form is a modeling choice to defend |
| Unbounded surroundings | Supplied (openness) | The finite-source case is the proved boundary |
| Demand and arrival quantities | Supplied numbers per kind | Identification evidence, Phase 5 |
| Which history occurs | Not derived: the theorem is about possibility | Selection and learning are later bridges in the accepted sequence |

The theorem does not say renewal is good, that systems choose to renew, or that any real organism satisfies the premises. It says exactly when renewal of the conditions of activity is possible under them. Renewability of the whole configuration (Phase 2b) is one ingredient of the whole-unfolding appraisal Ren has set as the center. It is not that appraisal, and it is not an assumption-free universal proof of it.

## 8. What would change the account

- **A defeat.** A system satisfying closure and the renewal inequality, under the stated premises, that cannot renew; or one that renews without them. Either would refute the target as stated, and would be preserved as a counterexample.
- **Prior art proving the same threshold.** The contribution then narrows to the derivation and the machine-checked unification.
- **Phase 3 showing the renewal inequality is just COT self-maintenance with decay terms.** Then the new content is the temporal deadline dichotomy and the constraint/flow derivation, and the exposition says so.

## 9. Coordination

Suggested allocation; the coordinator assigns.

- **Phases 1–2:** the Lean thread on the generative core (lane P), with a separate counterexample pass (lane C).
- **Phase 0 and Phase 5 comparators:** a separate identification thread (lane I).
- **Phase 4:** after the formation and native-port branches land. It touches the process-law closure, so it must coordinate with the dependency-map and process-law threads.

Before the next central connection is selected, each phase's result goes into this file's status line and into `RESEARCH.md`.

**Status, 6 October 2026:** planned. Phase 0 not started. Revised the same day to serve the whole-unfolding center (§1.1, Phase 2b) after Ren's correction, and to add the phase-cycle and initiation baselines to §1.
