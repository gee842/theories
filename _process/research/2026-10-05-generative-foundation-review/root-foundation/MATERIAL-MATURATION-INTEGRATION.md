# Material growth and the return to a reproductive organization

**Continuation, 8 October 2026.** [Growth forms fragmentation possibilities](GROWN-FRAGMENTATION-INTEGRATION.md) now realizes the previously selected bounded partition-formation connection: actual development and cuts determine successor composition, with 31 new Lean theorems / 59 audits. This study's preparation result remains unchanged. The new prepared output is the common eight-slot recipe, not regeneration of the new grown architectures; their transmission and operative fracture law remain unresolved. Historical next-step wording below records the earlier scope.

8 October 2026. AI-authored continuation following Ren's “继续”. This advances the material preparation connection left by [contact reconstruction](CONTACT-RECONSTRUCTION-INTEGRATION.md). The local production, routing and population distinctions are differentiated relations within the same unfolding, following the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md).

**中文结论：重建成功的后继更多，不保证能再次形成亲代的繁殖组织。** 同一批后继沿不同的局部生成规律生长，会形成不同的组成分布，从而改变哪些后继能完成下一轮准备。本轮把“恢复成统一成熟亲代”推进为有材料与消耗记录的有限过程；原先分散接触机会的优势可以倒转。生成规律、运输装配配方、分割形成及持续供给仍明确给定，未宣告整个生命周期的起源已经解释。

The [new proof package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/material-maturation-verification/README.md) contains **28 new Lean theorems / 44 new declaration audits**; the rebuilt closure has 267 audits. The preceding 223 audits are inherited. The selected finite preparation connection is complete at the scope below.

## The missing relationship now tested

The preceding parent contains four A and four B components. One partition concentrates compatible contact opportunities; the other distributes them. Both produce two four-component seeds, but their compositions differ:

- The concentrated partition produces two seeds with 2 A and 2 B. Only one has a compatible opportunity and reconstructs.
- The distributed partition produces seeds with 3 A and 1 B, and 1 A and 3 B. Each reconstructs with probability 3/4 after two encounters.

The earlier expected reconstruction outputs, 1 and 3/2, are correct. They are not automatically expected numbers of prepared parents. A successful 3-A/1-B seed still lacks the original 4-A/4-B composition and slot arrangement. The previous population calculation supplied that return law; this continuation replaces it within a specified material process.

## Local production from the actual changing pool

A stock records the current component list, unconverted precursor, free support and spent support. A production event consumes one precursor and one support unit, retains its activating component, and adds one newly produced component. The precursor represents enough undifferentiated material for one modeled component; this is a declared coarse material accounting unit, not a molecular mass equation.

At each production event, a component is drawn uniformly from the **current** list. Two native local laws are compared:

| Law | Product of an A activation | Product of a B activation | Composition-dependent consequence |
|---|---|---|---|
| Same-type production | A | B | More abundant kinds receive more further production |
| Complementary production | B | A | The abundance of each kind promotes production of the other |

These laws do not inspect a target balance or a success score. Their difference is the product of the local interaction. The complementary rule is an ideal catalytic production rule, not faithful genetic copying. Neither its chemical realization nor the evolutionary change between these two laws is derived here.

Each seed receives four precursor units and four growth-support units. Growth begins only after its contact reconstruction succeeds and runs for four production events. Fresh production draws depend on the changing pool; the growth law does not depend on which contact succeeded or when it succeeded. Contact, growth and routing support are separately allocated. Sharing or reallocating leftover support would change the model.

`produce_accounts` and `run_accounts` conserve component count plus precursor, and free plus spent support. `supported_run` proves that any supported four-event history adds four components and spends four support units. Actual stochastic draws are from existing components; the more general accounting theorem also covers prescribed event words and by itself does not certify their membership in the draw pool.

For a count observable F, the exact finite expectation satisfies

\[
E_{n+1}(F;a,b)=\frac{b}{a+b}E_n(F;T_B(a,b))
+\frac{a}{a+b}E_n(F;T_A(a,b)).
\]

For same-type production, \(T_A(a,b)=(a+1,b)\) and \(T_B(a,b)=(a,b+1)\); complementary production exchanges these updates. `growth_projection` derives this recurrence by summing over the actual list of activating components. Its hypotheses require a nonempty pool and enough precursor and support for the horizon. `expected_mass` verifies unit mass in that domain. No independent maturation-success probability is fitted or assigned.

## Preparation removes and places actual components

The specified reproductive arrangement has eight slots with labels

\[
(A,A,A,B,A,B,B,B),
\]

matching the previous parent. Its fixed contact opportunities are the adjacent slot pairs used in the preceding study. The slot apparatus and permitted opportunities remain supplied geometry; this study does not derive them from forces.

The routing operation attempts the slots in that order. For each slot it removes one matching component from the current pool, places that component, and spends one support unit. If the required kind or support is absent, it stops. It cannot manufacture a missing component, change its type, or count the same token twice.

`routing_trace_accounts` proves that the placed components together with the remaining pool are a permutation of the input, and that remaining support plus the number placed equals initial routing support. This includes failed preparation. For example, a pool with seven A and one B fills five slots, leaves three A unplaced, and retains three of its eight support units. `partial_routing_preserves_unused_components_and_work` checks that actual failed state.

`route_sound`, `route_complete` and `actual_preparation_iff` prove that, with eight routing-support units, complete preparation consumes the actual pool exactly when it contains four A and four B. `canonical_slots_match_parent` checks the resulting label arrangement against the preceding parent. Component instances are retained by multiplicity; genealogy, detailed geometry and the fate of the earlier bond are not represented by these label lists.

Thus the balanced-count predicate is derived as the condition for completing this **specific supplied slot recipe**. It is not introduced as a universal fitness function or a definition of biological maturity. Different reproductive arrangements can require different counts and relationships. Selecting, sensing and moving the requested kind are native capabilities of the routing operation; their apparatus and additional biochemical costs remain explanatory premises.

Every seed has at most two contact expenditures, four production expenditures and eight routing expenditures under its separately allocated stocks. Rejected preparations keep their residual components and support. Their failure to return to this prepared-parent class does not establish death, uselessness or loss of every future possibility.

## The changed prediction

The exact probabilities of completing the slot preparation after four production events are:

| Initial composition | Same-type production | Complementary production |
|---|---:|---:|
| 2 A, 2 B | 9/35 | 52/105 |
| 3 A, 1 B | 3/35 | 47/105 |
| 1 A, 3 B | 3/35 | 47/105 |

`return_from_composition` joins the paid pool process to these probabilities; `exact_maturation_rates` checks their rational values. The probabilities refer to the fixed four-event, eight-slot preparation. They are not measured biological rates.

The composed process follows the actual contact history first, then grows and routes that seed only after contact success. `pipeline_factorization` proves that its return is \(S_2(p_i)G_i\), where \(G_i\) is the growth-and-routing probability already derived from that seed's composition. The factorization is valid here because the growth stocks and law are the same after every successful contact history of that seed. It is not a license to multiply unrelated averages when those histories change growth resources or kinetics.

| Same parental pool and partition | Contact reconstruction only | Prepared-parent return with same-type production | Prepared-parent return with complementary production |
|---|---:|---:|---:|
| Concentrated opportunities | 1 | 9/35 | 52/105 |
| Distributed opportunities | 3/2 | 9/70 | 47/70 |

`exact_joint_returns` evaluates the joined contact, production and routing definitions. `maturation_reverses_contact_ranking` checks both ordering changes. Same-type production makes the concentrated partition yield **twice** the prepared return of the distributed partition, reversing the contact-only comparison. Complementary production changes the ranking back. The initial stocks, routing recipe and within-law production opportunities are matched; expected consumption need not match once more seeds enter growth. No claim of optimal output per unit cost is made.

All four prepared-parent expectations are below replacement under this finite protocol (`both_laws_below_replacement`). A universal favorable-growth conclusion is therefore unavailable even for the better partition in either regime. This is a statement about return to the designated parent class after this window. Continuing failed seeds, changing the preparation recipe or allowing more production could alter the outcome; none is ruled out by this count.

## What this changes in the evolutionary explanation

The earlier nonlinearity result concerned how inherited opportunities are distributed. The additional result concerns **what that distribution transmits into later production**. A partition can improve early reconstruction while transmitting compositions that are less likely to regenerate its reproductive organization. Changing the production relation changes the resulting comparison without changing the early contact process.

The relevant return coefficient is consequently constrained by the whole declared path:

**transmitted composition and opportunities → reconstructed contact → composition-dependent production → feasible preparation of the next reproductive arrangement.**

The actual material realization of one common-parent return is now supplied by local production and paid routing, rather than an unexplained state reset. Repeating it still requires the partition and routing apparatus to recur, stocks to be provided, and all relevant successor types and failures to be handled. The earlier conditional population theorems cannot turn a finite stock into indefinite renewal. No new invasion, fixation or open-ended evolution theorem is asserted.

This also clarifies the explanatory target: a faithful theory must recover which changes in the organization of production and transmission alter the capacity for subsequent reproduction. It need not predict that every increase in an early capacity improves continuation, or that one scalar “organization quality” ranks every regime.

## Primary comparison and author counterreview

The [original 1987 stochastic-corrector abstract](https://pubmed.ncbi.nlm.nih.gov/2451771/) already connects within-compartment composition, stochastic replication and fission, and selection among compartments. This priority credit is based on the primary abstract, not a reproduction of its full equations.

[Bianconi and colleagues 2013](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003051) give a stronger inspected comparator. Their protocell model tracks two sequence types, composition-dependent replication, mutation and division. They compare catalytic effects and fragmentation modes rather than assuming a universally superior transmission pattern. Their transition rates and maximum division size remain model inputs. Our same-type and complementary rules are not their four replicase cases, and their equations have not been reproduced here. [Preserved primary XML and reading scope](../../../../sources/evolutionary-selection/material-maturation/README.md).

**Has a conventional theory been surpassed?** No. A conventional stochastic compartment model given the same contact, production and routing laws yields the same expectations. The same-type rule is a familiar reinforced sampling process. The achievement is the checked removal of our own independent maturation/reset coefficient and the consequential correction of an earlier comparison. Greater connectedness of our explanation is not yet comparative economy or empirical superiority.

**Has the desired balance been hidden in an evaluator?** No reward directs production toward 4:4. Complete placement into an independently declared eight-slot recipe is the operational return event, and its count condition is proved. But the recipe itself is supplied. The result cannot establish a universal preference for balanced composition or the origin of that recipe.

**Is routing an unexplained reset under a new name?** Its selection and movement capabilities are premises, but it has an explicit token-removal sequence, a material-preserving trace, finite work costs and genuine failures. It therefore makes restrictions that an unrestricted reset lacks. It does not explain the biochemical implementation or formation of the routing apparatus. This is a bounded refinement, not a complete theory of morphogenesis.

**Does one law's greater return show that evolution acquires it?** No. The laws are compared as alternatives. Their formation, variation, retention and competition are not derived by switching a Boolean parameter. These new causal results also confer no ethical warrant on reproductive success; G0 and the completed normative arguments retain their own premises.

## Completion and next connection

The finite connection from transmitted composition, through actual component production and paid preparation, to a changed return comparison is complete. Existing contact reconstruction, assembly selection, connectionist recovery, memory and [updater replacement](EVOLUTION-UPDATER-CONSEQUENCES.md) remain completed results at their own scopes.

The next precise connection is **formation and inheritance of the reproductive recipe itself**: how local growth, contact mechanics and differential access produce or revise the partition, slot arrangement or routing relation, including their costs. A continuation must change an actual operative relation and follow its effects through the already checked preparation process. Selecting a free “better recipe” label, assigning a mature-state reset, or repeating these completed composition calculations would leave that question untouched. Continued support is a further realization requirement, not an automatic consequence of a positive comparison.

## Verification

The [source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/MaterialMaturation.lean), [fresh-build checker and receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/material-maturation-verification/README.md), and [integration checks](MATERIAL-MATURATION-CHECKS.json) separate proof validity from biological correspondence. Lean 4.29.1 checks every new declaration and rebuilds the five actual predecessor modules. Only standard logical axiom dependencies are permitted; placeholders, new axioms, unsafe shortcuts and warnings are rejected. The receipt binds source snapshots, toolchain, checker and logs.

The documentary check covers owned links, preserved primary bytes, paired C14 changes and the six unchanged broader completion requirements. This study adds no biological experiment or independent-agent acceptance and does not complete the general theory of evolution.
