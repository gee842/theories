<a id="the-theory-of-becoming--生成变化之论"></a>
<a id="the-theory-of-becoming"></a>
# The Theory of Becoming

Begun 9 October 2026 (Asia/Bangkok); restructured 20 October 2026 so that each thing is said once (the earlier edition is [kept in history](../history/THE-THEORY-OF-BECOMING-2026-10-20.md)). Direction: Yongxu Ren. The organization and wording are the AI's (Claude), from Ren's [priority proposal](../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md), his [whole and manifold](../../../sources/15-codex-theory-conversations/2026-10-09-becoming-whole-generative-manifold.md), his [direction of 生生](../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) (shēngshēng, “life giving rise to life”) and his instruction to [unify everything as one theory](../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md). These are provenance; the argument is given here. Ren's own words are marked as quotations; everything else is the AI's.

This chapter is the canonical entry to the theory. It states every premise once (§0), the argument once (§1–§7), each result once in [the theorem map](#the-theorem-map), what is open once (§8) and the Lean artefact once (§9). Earlier chapters keep their own arguments at their original scope (§11).

<a id="一句话--in-one-sentence"></a>
<a id="in-one-sentence"></a>
<a id="preface"></a>
## Preface

**In one sentence.** The Theory of Becoming explains how relations form, persist, transform, degenerate and dissolve within one relational unfolding, and how life, evolution, knowing and evaluation differentiate within it, without first assuming that becoming is good.

**Four kinds of standing.** Every statement below carries one of these:

- **theorem without premise**: holds of every world so represented, with no premise about the unfolding; any local hypothesis it needs (finiteness, enclosure, listing, decidedness) is written into it, and the representation's commitments are those of §0, block A;
- **theorem under stated premises**: holds where the premises it names hold (a World premise of §0, block C, a correspondence of block D, or a practical premise of block F);
- **the condition**: the continuation condition (`Unrestricted`, §6.4), which the theory states and does not assert;
- **reading**: an interpretation of checked content, adopted with its argument and marked **[AI reading, Dn]**, D*n* being its entry in the [decision register](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md). A reading changes no theorem, and a better argument revises it.

What is neither is **open** (§8). Every theorem is checked in Lean with an empty axiom report (§0, block A; §9).

**Where the ethics lies.** The ethics rests on two premises with two roles, and neither is asserted.
- *Scope: the continuation condition.* For anything, its continuation has significance. It fixes whose losses count, and by itself it orders nothing: mixed parts stay unordered, and every narrowing loses something (§6.4).
- *Order: C, the widening comparison.* Widening what can form is better. C is the only premise that ranks courses (§6.5). That widening is an order needs no premise (§6.1); that it is better is C.
- *The step of invariance.* The condition is exactly the self's presupposition joined to the step that significance stops at no boundary. That step is the condition's content beyond the self, and it extends the scope to losses that return to no one; it ranks nothing (§6.5).
So no ethical result follows from the condition alone: what counts comes from the condition, what ranks from C, and their warrant is open (§8.5).

<a id="central-results"></a>
**Central results.** Ten results carry the argument; each is stated in the section given and listed in the theorem map.

1. *One change, three readings, and keeping pace* (§1.2). Arising and ceasing, a dependence forming and dissolving, and a condition coming to stand and ceasing to stand are one change; in a finite family coming to be and ceasing keep pace, with no premise.
2. *Recurrence and attraction* (§1.2). Within finitely many configurations a law merges nothing exactly where every configuration returns; a configuration is drawn into an absorbing region exactly where it does not return; keeping one's history needs an open world.
3. *Premises carve parts* (§1.3). The eight World premises are each met by some worlds and failed by others; read off one exchange, five hold by construction and three are states of the law of exchange.
4. *Rest needs a least loss* (§1.3). Rest follows from a least loss per change and a stock within finitely many of them; approach to rest needs only Archimedean amounts; a law that merges nothing returns rather than rests.
5. *The order of what can form* (§6.1). With no premise, a part widens, narrows, keeps or is mixed; it closes something only by a net draw beyond its margin and opens something only by a net give.
6. *Closures and selection* (§2.6, §3.4). Feeding, influence, reach and system are nested closures; a selection through couplings reaches exactly what couples in, and a pool selects through the union of its members' couplings.
7. *Joint excess and relative position* (§2.3, §4.3). Takers each within what is given can together exceed it and end the renewers they depend on; relative position sums to zero by counting.
8. *Learning and identification* (§3.3). No finite prefix fixes the next value; within a bound of N states a prefix of 2N − 1 steps fixes the course; learning through a map is tracking in the limit.
9. *Significance is not in the dynamics* (§5, §6.4–§6.5). No law of the dynamics fixes significance; the condition is the self's presupposition with the step of invariance, and it orders nothing.
10. *Loops* (§2.6). The most difference that can arrive grows faster than every polynomial only through a loop of couplings that go on, and such a loop need not.

**Two targets, kept apart.** *The deductive necessity of the whole*: that the whole's determinations are internally related moments of one unfolding, with no added substantive premise. A theorem of every world so represented is not thereby necessary; this target is open (§8.1, items 1 and 12). *The ethical orientation within the whole*: how 生生 (life in the whole and its continuing generation) acquires normative significance, through C under the continuation condition, with the practical premises disclosed. Under its premises this target is complete in a thin sense: they are stated and what follows is checked, and much of it unfolds a definition (`Web.paths_comparison_widens`, `livingSignificance_of_unrestricted`); the warrant of the two premises is open. Neither target substitutes for the other: an absence of ethical axioms is not an absence of substantive premises, and an empty axiom report is not an absence of premises. Objections not yet answered are in §8.9.

**Scope.** The theory counts the whole space of becoming, generative and degenerative alike. Generation is one part of it, not a condition every change must meet; degeneration, ending and mixed change are in the same unfolding and are not renamed generation ([the foundation's scope](BECOMING-FOUNDATION.md#whole-and-manifold)).

<a id="0-前提卡--premise-card"></a>
## 0. Premise card

Every premise is named here and nowhere else explained. In Lean each is a definition or a hypothesis, never an axiom. The first two blocks are not premises about the unfolding: they are how it is represented, and the local hypotheses individual theorems carry. Block C carves parts of the space; blocks D–F bear on application, ethics and practice.

**A. Commitments of the representation**

| Commitment | Content | Lean | Standing |
|---|---|---|---|
| Proof language | Lean 4.29.1 kernel. The core imports only Lean's `Init` (the prelude); the checker strips the foundation's `import Std` and recompiles the core closure without it. Every source declaration has an empty axiom report: no `propext`, `Quot.sound` or `Classical.choice`. Constructivity needs only the absence of `Classical.choice` (propositional extensionality and quotient soundness are constructively acceptable), so the core is **stricter than constructive**: no excluded middle, choice, propositional or function extensionality is assumed. A theorem that needs a classical principle names it as a hypothesis (excluded middle, LPO, WLPO, LLPO, Markov's principle, double-negation elimination, dependent choice), and §8.6 says what each need means for the unfolding. **The axiom report concerns logic only.** It shows that no logical axiom is used; it does not show that the rows below hold of any actual unfolding, and the substantive assumptions lie there. The periphery may use Lean's standard axioms, each result with its own receipt (§9). The provenance of the requirement is [Ren's pure-core request](../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md). | `check_becoming.py` (prelude-only step) | method commitment |
| Discrete steps, one shared index | Every relatum's activity, level and exchange is indexed by one sequence of natural-number steps. No definite causal order beyond it is assumed (§1.4). For exchanges acting locally the index is read off the relata's own courses; beyond them it orders only exchanges sharing no relatum, which changes no configuration (§1.4). | `World`, `Web`, `Flow` | representation |
| Natural-number amounts | Levels, needs, takes and gives are natural numbers; a positive amount is at least one unit. Dissipation's least loss, the doubling of loops and novelty needing gain depend on it. The rest theorems (`World.comes_to_rest_unrefuted`, `World.rests_unrefuted_enclosed`, `World.rests_unrefuted`), feeding from beyond (`Flow.fed_from_beyond`), and three theorems with no premise about the unfolding (`rising_recurs`, `falls_not_recurring`, `Flow.excess_bounded`) sum falls of at least one; over dense amounts a stock halving at every step falls for ever and never rises (`Halving.approaches_without_reaching`). Their general form is the least-loss law (`Amounts.rests`), of which `falls_not_recurring` is the whole-number instance (§1.3). The second law supplies no least loss per step. | `Web.level`, `Flow.take`, `Flow.give` | representation; finer units in `Becoming.Units`, `Becoming.Resolution`; dense amounts in `Becoming.Amounts`, each premise needed (`Becoming.LeastLoss`) |
| Prop-valued activity | Activity is a proposition, `active : Nat → F → Prop`. Laws that count or name a step need it decided; asked of every world without decidedness some laws are exactly excluded middle, a calibration of this commitment (§8.6). | `Web.active` | representation |
| One kind of relatum | A world is relata of one kind, with a flow (`present`, `take`, `give`) and a web (`level`, `active`, `requires`, `need`, `draws`). Formations and conditions are two roles of one relatum. | `World`, `World.ofRoles`, `Becoming.Roles` | representation |
| The shared index | Which condition is which relatum is given by the representation, not derived from the dynamics. | `relabel` | representation premise |
| Requirements as thresholds | What a formation requires at a step, and how much, is given in advance for every relatum of the world's type. Support is meeting every requirement: `need ≤ level`. | `Web.requires`, `Web.need`, `Web.Supported` | representation |
| Context-free claims (frames only) | A frame reads what is shown of a claim as independent of what is shown with it. What quantum states show does not meet this. | `Becoming.Context` | commitment of the frame view (§3.3) |
| Identity across steps | Which formation continues which is fixed by the naming. | `Becoming.Identity` | representation (§2.2) |
| Pointwise properties | The decided counting laws are stated for properties of counts that respect their values at each step, since the core does not assume function extensionality. Over counted censuses no such condition is needed: counts taken as relations are unique where they exist (`Counts.unique`, `Becoming.CensusCounts`). | `Pointwise` | hypothesis of the decided counting laws |

**B. Local hypotheses carried by individual theorems**

| Hypothesis | Content | Lean | Where it is used |
|---|---|---|---|
| Finite | Finitely many relata, each listed once | `World.Finite` | finite-world theorems; a finite world has a census where its activity is decided, and every step of it is enclosed |
| Enclosed | Across a step, the exchange of the formations taking part lies within some finite family without repetition; around a family or around what stands, the same with that family included | `Flow.Enclosed`, `Flow.Around`, `AroundStanding` | rest, change-bound and drawing-in theorems |
| Listed | What holds at each step is listed once; a family is without repetition | `Listed`, `Web.Census`, `Distinct` | census, counting and loop theorems |
| Decided | What a theorem counts or names is decided where it needs it. A count exists exactly where what it counts is decided (`counts_iff_decided`); listing once is decided identity (`listsOnce_iff_decided`). The counting laws of `Becoming.Counting` take `[∀ t x, Decidable (w.web.active t x)]`, global decidability of activity; over counted censuses (`Becoming.CensusCounts`, `Becoming.CensusBinding`) the laws under the premises, each premise subset, enclosure, finite worlds and where the premises bind take none, a ceasing or coming count across a step existing exactly where being listed at the other end is weakly decided (`World.ceasings_exist_iff_listed`). | `Becoming.Decidedness`, `Becoming.Listing` | counting, recurrence and naming-a-step theorems |

**C. The World premises**

| Premise | Content | Lean |
|---|---|---|
| Activity needing support | A relatum is active only where the levels meet everything it then requires | `World.Dependent` (`Web.Dependent`) |
| Balance | Every change of a level is exactly what is taken from it and given to it | `World.Balanced` (`Flow.Balances`) |
| Only active relata give | Whatever gives across a step is active there | `World.Acting` (`Flow.Acting`) |
| Only active relata take, and only from what they draw on | Whatever takes across a step is active there and draws on what it takes from | `World.Taking` (`Flow.Taking`) |
| Dissipation | On every family without repetition closed across a step, each formation taking part gives it no more than it takes from it, and at least one unit less when it takes: a least loss of one whole unit per taking step (block A); over dense amounts the least loss is a premise of the rest law | `World.Dissipative` (`Flow.Dissipative`, `Flow.DissipatesOn`) |
| Embodiment | Every relatum stands as a condition exactly while it is active | `World.Embodied` |
| A census | The relata active at each step are listed, each once | `World.Counted` |
| Bounded transmission | Descent transmits every dependence within one bound | `World.Transmitting` |

Two weaker forms are used: a reserve carrying activity (`World.Carried`) and embodied arising (`World.ArisingEmbodied`). Activity needing support gives the zero reserve; embodiment gives embodied arising; a finite world with decided activity has a census; with only active taking and dissipation, only active relata give across an enclosed step (`World.acting_across`).

- *Contingent and independent.* Seven premises (the first six and the reserve) are each met by some worlds and failed by others (`World.contingent`); the eight of the table are independent, each failed by a world meeting the other seven (`World.independent`, `World.none_follows`). Finiteness, enclosure and decidedness are not among them. In `hatch` all eight hold and each binds, binding meaning only that the premise's condition has an instance (`World.hatch_binds`); no finite world binds the census, by definition (`World.Finite.not_binds`).
- *What the independence measures.* The freedom of `World`'s separately chosen fields, not contingency in becoming. Read off one exchange, with the rest of the whole counted as one relatum, the eight divide in two (`Becoming.Reading`, `Becoming.ExchangePremises`).
  - *Five hold by construction.* Balance, only active giving and only active taking hold of a world read off an exchange; for a law of exchange, so does activity needing support (`World.withRest`, `ExchangeLaw.readWorld_glue`). This does not remove the premise: with the rest counted, balance holds exactly where the rest is never active (`World.withRest_closed_iff`), and under a law of what has stood the rest is idle exactly where the course is feasible, no exchange taking from a condition more than stands on it and is given to it (`ExchangeLaw.readWorld_closed_iff`, `ExchangeLaw.course_balances_iff`). Nothing comes from nothing is then a premise located in the law, feasibility. A census holds wherever a named family closes each step's exchange, with no decision procedure (`World.withRest_counted`, `World.Finite.withRest_counted`); without enclosure no world read off an exchange fails a census at any step, but asking one at every step of every flow over `Nat` is exactly LPO (`Flow.not_not_listed_at`, `Flow.listed_iff_lpo`).
  - *Three are states of the law of exchange.* Worlds read off laws, with the rest counted and idle and the four tying premises holding, meet and fail each (`ExchangeLaw.contingent`). Dissipation is loss (`responsive`); embodiment is no dormancy (`still`; with the rest counted, embodiment is exactly balance and each relatum exchanging exactly while it stands, `World.withRest_embodied_iff`); bounded transmission is heredity of response (`sprouting`). As closure is feasibility, enclosure is the law's reach (`ExchangeLaw.spreading_not_enclosed`, `ExchangeLaw.spreading_counted`).
  - *Requirement over open exchanges.* Where a relation leaves several exchanges open, requirement read as necessary response gives activity needing support on every run (`ExchangeRelation.reading_glue`); read as possible response it does not (`ExchangeRelation.free_unsupported`). For a law of exchange the two readings are the law's (`ExchangeLaw.relation_readWeb_requires`, `ExchangeLaw.relation_readWeb_may`).

Records: [map-of-premises](../results/records/map-of-premises.md), [premises-read-off-the-exchange](../results/records/premises-read-off-the-exchange.md), [census-read-off-the-exchange](../results/records/census-read-off-the-exchange.md), [premises-that-are-states-of-the-law](../results/records/premises-that-are-states-of-the-law.md), [requirement-over-open-exchanges](../results/records/requirement-over-open-exchanges.md).

**D. Dynamics and correspondence**

| Layer | Premise | Content | Lean | Standing |
|---|---|---|---|---|
| Dynamics | Process | Admissible changes `step s a t` | `Generative.Process` | a view of the one unfolding, the move read within the configuration (§1.1); in an application, which process is read is part of the correspondence |
| Correspondence | Observables | Claims realized, condition levels, dependence and drawing correspond to actual histories | `Frame.realized`, `Conditions` | application obligation |
| Correspondence | Formation E | The lives and relations evaluated actually form within the unfolding | — | application obligation |
| Correspondence | Connection | Living claims are joined through formed relations | `Valuation.Connected` | given by common conditions under the discipline of correspondence between conditions and participation; interaction (one draws on a condition and the other depends on it at a positive level) gives connection in the declared class (§6.2) |
| Correspondence | Readings of `living` | Whole-run (active and not consuming), stepwise (active and not undermining) and relation level, each relative to a run. They read activity compatible with others' dependence, not further generation. | `Conditions.valuation`, `Web.valuation`, `Web.relations` | a disclosed choice; no comparison uses it. 生生 is read as generation generating generation, compared by widening [AI reading, D1]; the `living` readings do not read 生生 |
| Correspondence | Held | Every living claim lies in some standpoint's own region (always, on the stepwise reading where each formation's region is its own events); that holding is decided is `Valuation.significant_iff_reached`'s own hypothesis | `Valuation.Held` | the formal reading of “what wants its continuation”; self-significance reads “wanting” [AI reading, D11] (§6.2) |

**E. Ethics** (none asserted)

| Premise | Content | Lean | Standing |
|---|---|---|---|
| **The continuation condition** | For anything, its continuation at every step has significance from every standpoint. The wording is Ren's proposal, kept as provenance: “for anything, its continuation into the future has significance” ([source](../../../sources/15-codex-theory-conversations/2026-10-10-wanting-continuation-one-axiom.md)). | `Unrestricted` (`∀ p t f, sig p t f`) | **Stated, not asserted** (§6.4). It fixes scope: whose losses count. It gives significance, not a positive valence, and orders nothing. Living significance, the seed, self-significance and the two neutralities follow from it by restriction; each such theorem is an instantiation of a universal statement (§6.4). C does not follow from it [AI reading, D16]. |
| **Living significance** | Every living claim has significance from every standpoint; on a frame, realized living content falls under the relevance read from significance | `LivingSignificance`, `Valuation.Significant` | A condition, not an axiom. Characterized exactly with no premise (`Valuation.significant_iff`, `Valuation.significant_iff_held`; §6.2); not entailed by the dynamics (`Web.significance_undetermined`; §5); the condition restricted to living claims (§6.4). Its binder `relevance` is a parameter, not a valence (`relevance_least`). |
| Self-significance | A standpoint's own living claims have significance from it | `SelfSignificance` → `Seed` | A normative premise reading “wanting one's continuation” [AI reading, D11]; living claims only; everywhere under the condition (§6.4). It is not the seed, which any standpoint holding self-significance with its own living content supplies. |
| Relational neutrality | Significance passes along formed relations to living content (the side of the claim reached) | `transmits` | a boundary-neutrality premise; follows from the condition |
| Standpoint neutrality | What has significance from any standpoint has it from every standpoint (the side of the standpoint) | `shares` | a boundary-neutrality premise; follows from the condition. Where every living claim is held, living significance is exactly self-significance with standpoint neutrality; on a connected whole where every standpoint holds a living claim, self-significance with relational neutrality also gives it (§6.2) [AI reading, D11] |
| A (articulation) | Access, together with securing positive content from one's own standpoint over one's scope, gives a supporting reason (the side of the position addressed) | `articulates` | an externalist articulation premise; under the condition it must be read on living content, since on bare significance it would give a reason for any new content [AI reading, D16] |

**F. Practice**

| Premise | Content | Lean | Standing |
|---|---|---|---|
| C (the widening comparison) | An extension with no loss that realizes more is better; with “better” read as widening what can form, C's no-loss extension is exactly widening (`Web.paths_comparison_widens`, definitional) | `Comparison` | **The order premise, the only one that ranks courses** (§6.5). Courses are compared on possibilities: extension on possibilities ranks the absence of an overdrawing formation above its presence and withholds no event (`Ranking.possible_extends_iff`). Under the condition widening is retaining and adding what has significance (`Web.widens_iff_retains_adds`); reading “better” that way is a reading, not a consequence of the condition. That widening is better is the open warrant. |
| L (lifting) | Lifting the comparison of outcomes to responses with many outcomes; the conservative default is “every outcome is better than every outcome” | `LiftBetter` | a substantive commitment (§6.5) |
| J1–J4, the practical commitments | Complete comparison and retained losses; priority of basic conditions; bounded responsibility; legitimate feasible choice | `Lexical.BasicPriority`, `Lexical.Frame.Above` (J1/J2), `Requirement.Frontier`, `Required` (J3/J4); on a frame `FrontierFrames.Priority`, `FrontierFrames.Options`; J3 on a world's moves by `FrontierWorlds` | commitments proposed by the AI, conditions of the practical theorems; a choice at every step needs weak excluded middle (`FrontierFrames.choice_exists_iff_weakly`, §8.6) |
| FR | Finite responsiveness: within an independently specified family of recoverable basic losses of one kind, a fixed graver loss does not keep sufficient priority over arbitrarily many fixed lesser basic protections by its gravity alone | `Becoming.LossMatching` (the formal content of strict loss matching, not the warrant) | an additional, revisable comparison commitment with affirmative defence and counter-review; neither theorem nor axiom ([finite-aggregation-within-restorable-basic-losses](../results/records/finite-aggregation-within-restorable-basic-losses.md)) |

Other named commitments of the practical line (BC1, BC2, LC, LR, CP, NP) are stated with their records in §6.5.

**Not assumed.** That becoming is good; inevitable improvement or universal growth; a fixed common utility; independent owners of value; that every change is generative; a definite global causal order at every interface (the representation has one shared index of steps, and what the theorems use of it is the order of change, §1.4).

