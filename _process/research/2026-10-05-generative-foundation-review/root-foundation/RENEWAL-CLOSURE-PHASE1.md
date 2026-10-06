# Renewal and closure: claim, prior work and Phase 1 results

6 October 2026 (UTC). AI-authored, following Ren's goal recorded in the [roadmap](RENEWAL-CLOSURE-ROADMAP.md). It covers Phase 0 (the claim, conventions and prior-art check) and Phase 1 (constructive necessity in Lean). It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). Here, "constraint" and "flow" are articulations relative to timescale within one activity; Phase 4 is where they are derived.

## Phase 0: the claim and its conventions

**Transition addressed.** Organization → its own continuation, under the [whole-unfolding center](RENEWAL-CLOSURE-ROADMAP.md#11-what-this-serves-the-whole-unfolding).

**Claim fixed before testing.** Under finitely many kinds, bounded support reach, positive formation demand, arrival only through live constraints and no imported organization, endless renewal requires both of the following:
1. a realized closure of support kinds;
2. a kind whose tokens bring in at least what their formation demands.

The exact iff, with the balanced and excess cases, remains the Phase 2 target.

**Conventions, as implemented in `RenewalAccounting.channelProcess`:**
- A token formed on a tick starts with `span` remaining. It opens arrival on each of its `span` ticks, so it brings in at most `rate·span` in all.
- What live tokens open during a tick can meet formation demands on that same tick: `reserve' + formation ≤ reserve + opened`. This matches the preliminary enumerations.
- A formed token needs a support token that survives aging, so the supporter existed before the tick and is still alive.
- Any number of formations may occur per tick. Arrival is bounded only by what live tokens open, which keeps the necessity results strong.
- In `OccurrenceSupport`, a positive-time occurrence needs a supporting occurrence at an earlier time `s` with `t ≤ s + reach`. For episode systems, `reach` is the lifetime bound `duration`.

**Montévil and Mossio's definitions.** These were still not checked against the paper's text in this session: HAL, arXiv and montevil.org refused or blocked access. The closure notion formalized here is the published one as commonly stated: each constraint depends on a member and supports a member. `DependenceClosed` makes it explicit at the level of kinds.

## Phase 0: prior-art check

These four works were read through fetched summaries, not full texts. That is enough to set direction, but must be re-read before publication.

| Work | What it establishes | Relation to the claim |
|---|---|---|
| Blokhuis, Lacoste & Nghe, [PNAS 117 (2020) 25230](https://pmc.ncbi.nlm.nih.gov/articles/PMC7568248) | Stoichiometric autocatalysis: an autonomous submatrix with a flux of strictly positive net production; five minimal core motifs. Degradation enters only through kinetic viability (branching-process thresholds) | Catalysts must be net-produced, and there is no separation of constraint from flow and no finite lifetimes of unconsumed constraints. Their decay thresholds concern growth probabilities, not the renewal inequality |
| Unterberger & Nghe, [arXiv:2109.01130](https://ar5iv.labs.arxiv.org/html/2109.01130) | For diluted networks: a strongly connected component containing a reaction with several products ⇔ stoichiometric autocatalysis; dynamical autocatalysis follows when degradation is small enough | **The strongly-connected-component condition parallels our cycle condition.** No exact threshold of our kind is stated. Their growth condition (several products) is not needed here, because an unconsumed constraint can support any number of formations; the limit is the flow account |
| Golnik, Gatter, Hordijk, Stadler & Vassena, [arXiv:2605.25523](https://arxiv.org/html/2605.25523) | Every RAF that is not a CAF contains a well-formed semipositive submatrix, so it is stoichiometrically autocatalytic | No degradation or lifetimes |
| Hordijk, Steel & Dittrich, [New J. Phys. 2018](https://iopscience.iop.org/article/10.1088/1367-2630/aa9fcd) | Relation between RAF sets and chemical organization theory | Steady-state and structural; no lifetimes |

**Verdict.** No published exact threshold was found that combines finite constraint lifetimes, the constraint/flow separation and arrival through constraints. The qualitative half (a cycle or strongly connected component is necessary) overlaps existing work, and the exposition must say so. The roadmap's main risk is reduced but not removed: the full texts and the COT literature on decay still need checking in Phase 3.

## Phase 1: what is proved

The package is at [`lean/conditional/renewal/`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md). The checker passed with 32 new audits: 8 with empty axiom reports, and the rest depending only on `propext` and `Quot.sound`. There is no `sorry` and no warning. The inherited modules match their receipts.

1. **Late activity descends from a realized closure** (`late_occurrence_descends_from_realized_closure`). Any occurrence later than `n·D` comes through support edges from a closed walk of kinds. Every kind on that walk occurred within the preceding `n·D`, so the closure is realized, not merely permitted. Its kinds are dependence-closed (`closed_walk_dependence_closed`).
2. **Acyclic support has a deadline without a supplied rank** (`acyclic_support_deadline`, `episode_acyclic_deadline`). This closes the gap that `SupportNecessity.lean` states explicitly.
3. **Constraints that fall short end, whatever their closure** (`short_renewal_depletes`, `short_renewal_deadline`, `short_kinds_cannot_renew_forever`). If every kind satisfies `rate·span < demand`, the potential below strictly falls on each live tick:

   remaining life + D × (reserve + what live tokens can still open)

   It reuses the core `Depletion` theorems, so this regime is a depleting process in the existing sense.
4. **Closure plus openness is not sufficient** (`closed_open_short_cannot_renew_forever`). A closed, open, self-supporting kind with rate 1, span 3 and demand 4 executes a renewing tick, yet cannot renew forever.

**Correction to the roadmap.** §3.3 said the main theorems "can keep empty axiom reports". In practice, `omega`, `simp` and core list lemmas bring in `propext` and `Quot.sound`. The package therefore uses the conditional package's allowance; `Classical.choice` was avoided by writing the pigeonhole lemma here.

## What remains (Phase 2)

Sufficiency and the link between the two models are now done; see the [Phase 2 note](RENEWAL-CLOSURE-PHASE2.md). The list below is kept as it was written.

- **The mixed case.** Some kinds fall short and some do not. The target: endless renewal ⇔ a cycle whose kinds are all balanced, or an excess kind reachable from a cycle. Necessity needs the charge argument split by kind, together with item 1's chain.
- **Sufficiency.** Explicit periodic schedules with initial-reserve bounds, including the balanced timing buffer the enumerations showed.
- **Linking the two models.** Prove that `channelProcess` histories are an `OccurrenceSupport`. This needs formation times tracked through ticks, so that items 1 and 3 apply to the same histories.

These results do not show which history occurs, that continuation is favorable, or that any real system meets the premises. They are possibility constraints on renewal of the conditions of activity, at the stated scope.
