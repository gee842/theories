# Transmission and the reconstruction of evolutionary organization

**Material continuation completed at a finite scope, 8 October 2026.** [Actual growth and paid routing](MATERIAL-MATURATION-INTEGRATION.md) now realize preparation of this parent arrangement and derive its composition-dependent return probabilities, with 28 new checked theorems / 44 audits. This narrows the earlier supplied-reset premise and can reverse the contact-only ranking. The slot recipe, routing apparatus, partition formation and continued provision remain supplied; the contact and conditional population theorems below keep their original hypotheses.

8 October 2026. AI-authored continuation of Ren's evolutionary-organization investigation. **30 new Lean theorems / 57 new declaration audits pass**, with 223 audits in the rebuilt dependency closure. The [preceding assembly result](ASSEMBLY-DERIVED-SELECTION.md) is reused. The [developmental-memory result](EVOLUTION-DEVELOPMENTAL-MEMORY.md) remains a completed parallel connection.

**中文结论：亲代拥有的组织，不会自动成为后继可重建的组织。传递哪些组成、哪些接触机会仍然存在、这些机会怎样分配到不同后继，共同决定重建。即使亲代相同、后继大小相同、平均成键率和平均重建消耗相同，重建产出仍可能不同。** 本轮把局部成功率接回实际组成及接触，并取消新构造中“把亲代成功标记复制给后继”的做法；没有宣告全部复制、发育或分割规律已经导出。

## The explanatory connection

The completed assembly model computed reconstruction, cost and selection from joint developmental histories, but supplied an encounter probability and a terminal copying law. This continuation explains a narrower physical interface:

**component allocation → retained encounter opportunities → paid contact formation in each successor → reconstruction and its cost.**

A parental component pool is partitioned. An opportunity survives into a successor only when both its endpoints are transmitted there. Every successor begins with no formed bond. A paid encounter can form a specific bond between its actual components. No parental `linked` flag determines the successor's organization.

Components, contact geometry, available support and the partition are different relations in this same modeled history, following the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Holding some relations fixed does not make them independent substances. Their formation remains an explanatory obligation where the scope includes it.

## Model and supplied premises

A seed contains a finite list of component positions and a list of possible contacts. Each position has one of two local labels. An encounter can form a bond exactly when both endpoints are present and their labels differ. The labels represent complementary local states; they are neither species nor moral categories. Reconstruction here means forming at least one such bond. It does not mean connecting every component or realizing a full biological organism.

`transmit` filters the parental opportunity list by membership in the transmitted set. It retains opportunities, **not formed bonds**. This is a stipulated geometry-preserving transmission law. It does not derive folding, diffusion, new contact formation or the physical forces selecting a partition. Lists describe equiprobable encounter slots; duplicate entries, when present, represent repeated slots, not extra independent physical bonds. The concrete example has no duplicates.

Each unbonded seed with positive support draws an opportunity uniformly, with replacement. Every attempted encounter spends one support unit. A compatible encounter records the actual endpoint pair and stops further expenditure. An incompatible encounter leaves the components and opportunity list unchanged. Once support is exhausted, no further change occurs. These rules explain why the encounter probability stays constant during a seed's development; sampling without replacement or changing geometry would require a different recurrence.

| Relation | Status in this continuation |
|---|---|
| Components allocated to each seed and retained opportunity list | Explicitly realized for the checked partitions; origin and cost of partitioning are supplied |
| Local compatibility | Binary complementary-label rule supplied; no molecular derivation |
| Single-attempt success probability | Derived from the seed's actual compatible slots and all slots |
| Bond in the successor | Formed by its own paid encounter, with transmitted endpoints; no bond copying |
| Reconstruction budget | Finite stock supplied; every encounter and replay preserves free plus spent support |
| Further synthesis, component division, exchange and maturation | Outside this development window; no automatic repeated reproduction |

## Exact correspondence to the earlier assembly process

For a nonempty opportunity list, let \(M_i\) be its length and \(K_i\) its compatible-slot count. Then

\[
p_i=K_i/M_i.
\]

`total_binary` derives the sum over the actual slots. `draw_reduction` proves that averaging the contact-level transition gives exactly the two branches weighted by \(p_i\) and \(1-p_i\). `rate_bounds` establishes \(0\le p_i\le1\); `expected_mass` verifies unit mass. `expectation_projection` and `binary_is_tree` join every finite encounter horizon to the earlier assembly tree for any observable depending on free support, expenditure and whether a bond exists. The projection forgets endpoint identity; it is adequate for these observables, not a complete representation of the contact state.

With \(n\) allowed attempts and at least \(n\) support units, `reconstruction_from_contacts` and `cost_from_contacts` derive the earlier quantities \(S_n(p_i)\) and \(C_n(p_i)\) for this seed. `encounter_accounts` and `replay_accounts` check support conservation. `formed_bond_has_transmitted_endpoints` ties a newly formed bond to present, differently labeled components.

This composition reuses the earlier **attempt and success process**, not its terminal reproduction operation. The new census counts at most one reconstructed successor per transmitted seed. It does not use remaining support to produce copies of its final bond. Accordingly, the old assembly output formulas \(A_n,D_n\) are not silently reused for this new census.

Empty opportunity lists stop without expense. They cannot be represented by a nonempty list with \(p=0\) for cost observables: the latter still permits paid failures. `empty_contacts_stay_unbonded` covers the empty case separately. A singleton seed cannot reconstruct under the fixed complementary-label law, as checked by `singleton_no_reconstruction`. This is a theorem about a window without synthesis, division or incoming partners, not about single-cell biological propagules in general.

## A restriction on averaging inherited capacities

For two seeds with rates \(p,q\), give each two supported attempts. Write \(\bar p=(p+q)/2\). The checked identities are

\[
S_2(p)+S_2(q)=2S_2(\bar p)-\frac{(p-q)^2}{2},
\qquad
C_2(p)+C_2(q)=2C_2(\bar p).
\]

The expected reconstruction deficit relative to equal rates is exactly the variation term. It is strictly positive when \(p\ne q\), while expected encounter cost is unchanged. With just one attempt the mean does suffice: \(S_1(p)+S_1(q)=2S_1(\bar p)\). These are `two_attempt_heterogeneity`, `two_attempt_cost_equal`, `strict_heterogeneity_loss` and `one_attempt_mean_suffices`.

Thus a mean contact rate is not generally enough to predict what repeated development reconstructs. This is distinct from the preceding assembly result's correlation between early success and offspring number. Here each seed contributes at most one reconstructed unit; the loss arises from variation **between transmitted substrates** under nonlinear reconstruction.

## Same parent and conserved components

The parent has eight positions, labeled A at 0, 1, 2, 4 and B at 3, 5, 6, 7. Its four possible contacts are (0,1), (2,3), (4,5), (6,7). The first and last are incompatible; the middle two are compatible.

| Transmission | Components in the two seeds | Rates derived from their retained contacts | Expected reconstructed successors after two attempts each | Expected total encounter cost |
|---|---|---|---:|---:|
| Concentrated compatible opportunities | {0,1,6,7}; {2,3,4,5} | 0; 1 | 1 | 3 |
| Distributed compatible opportunities | {0,1,2,3}; {4,5,6,7} | 1/2; 1/2 | 3/2 | 3 |
| All listed opportunities severed | {0,2,4,6}; {1,3,5,7} | No retained opportunities | 0 | 0 |

The first two partitions preserve every component and every parental opportunity exactly once, produce two four-component seeds, and retain two opportunities per seed. Both have two compatible slots in total, the same mean rate 1/2, the same initial support of four units, and the same expected remaining support of one unit. With one attempt per seed both yield one expected reconstructed successor. The second attempt distinguishes them. These checks evaluate the actual contact histories, not just the rate formula: `actual_partitions`, `actual_rates`, `same_first_different_second`.

The third partition conserves all components but cuts every listed opportunity. It demonstrates why component conservation does not guarantee conserved reconstruction. The zero cost is inactivity, not an improvement in efficiency; no successor reconstructs. The result does not exclude later formation of new opportunities under additional developmental operations.

Against a declared cycle-return reference of 5/4, the first two reconstruction outputs lie on opposite sides (`opposed_cycle_comparison`). This is an exact comparison of **one developmental return**, not an independently derived invasion theorem. Interpreting it as repeated lineage advantage additionally requires comparable partition and maturation costs, actual preparation of later component pools, a defined fate for failed seeds, and a common cycle duration. Those relations are not supplied by equal encounter costs alone.

## The population interface must retain the relevant differences

One cannot generally collapse both seed types into a single interchangeable P stage. If their return probabilities differ, no coefficient \(r\) satisfies

\[
S_2(p)u+S_2(q)v=r(u+v)
\]

for all counts \(u,v\). `no_aggregate_return_coefficient` proves this by preserving both actual seed responses. An aggregate coefficient is legitimate only under an additional mixture restriction, or when the response coefficients coincide. A fixed cohort average must not be applied to arbitrary evolving mixtures.

The checked continuation also constructs a legitimate restricted population interface. Distinguish mature units O and two unbonded seed types U and V. Under the **additional** law that each prepared mature unit produces one seed of each type, each seed returns according to its derived reconstruction probability, and failed seeds leave this cycle, the expectation operator is

\[
O'=S_2(p)U+S_2(q)V,\qquad U'=O,\qquad V'=O.
\]

`typed_two_step` derives both the balanced seed mixture and the two-step return \(O''=R O\), where \(R=S_2(p)+S_2(q)\). Starting at a mature census, `conditional_cycle_return` proves \(O_{2t}=R^t O_0\) for every finite t under that stipulated operator. The checked contact examples give R=1 and R=3/2. This connects reconstruction to conditional expected continuation without falsely making all seed types interchangeable. It does not produce the stocks needed to prepare every new mature unit; actual repeated realization must supply those stocks and account for maturation and partition costs. In the distributed example, successful seeds contain three A and one B, or one A and three B. Forming a bond does not turn either into the parental four-A/four-B pool. Their return to a common prepared O type is therefore an additional maturation/reset law, not an already derived consequence of contact success.

When U=V, `balanced_stage_reduction` proves that a single P=U+V stage *is* sufficient, with coefficient \(r=[S_2(p)+S_2(q)]/2\). The valid coefficient averages **developed responses**, whereas applying development to the mean contact rate gives \(S_2(\bar p)\) and loses the variation term. Thus the restriction is constructive: retain seed types until a proved mixture relation licenses their aggregation. A conventional structured-population model gives the same operator and result.

## Primary evidence and strong comparison

Ratcliff and colleagues' [2015 snowflake-yeast study](https://www.nature.com/articles/ncomms7102), already [preserved in the repository](../../../../sources/evolutionary-selection/evolutionary-organization/README.md), connects division rules, genealogical fragmentation and collective inheritance. It also shows why the restricted singleton result must not be generalized: cell division can rebuild a multicellular organization. Our two-label contact rule is not a calibrated yeast model.

[Pichugin and colleagues 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005860) already compare fragmentation life cycles through their growth consequences. Their explanatory target includes the evolution of reproductive organization; it cannot be described as fixed-individual theory unable to ask this question. The [previous assessment](RECONSTRUCTIVE-SELECTION-INTEGRATION.md) retains the corresponding model assumptions and cost comparison.

[Oszoli and Zachar 2024](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012107) provide a stronger spatial comparator. Their model distinguishes aggregate-based sampling from preservation of spatial arrangements after transfer. In the reported regime without predation, aggregate-based dispersion supports cooperators more reliably than intact propagule transfer, which also intensifies local competition. Their study fixes two cell types and excludes mutation; association, division and resource-reset rules remain supplied. This is a substantive counterweight to any universal claim that retaining more structure must improve continuation. It also establishes that conventional accounts already investigate structural transmission and reconstruction-relevant composition. [Preserved primary text and reading record](../../../../sources/evolutionary-selection/contact-reconstruction/README.md).

| Comparison on the same declared contact history | Assessment |
|---|---|
| One mean rate substituted for different seeds | Loses the checked variation term and can reverse a benchmark comparison |
| Parental organization copied into successors | Fails when endpoints or compatible opportunities are not jointly transmitted |
| Conventional model retaining seed membership, contact sampling and support | Gives the same expectations; no predictive advantage over it is established |
| Full spatial or developmental biological model | Addresses additional movement, competition and formation mechanisms absent here; no ranking is warranted without matched evidence and targets |

## Author counterreview and next connection

**Is a success parameter merely concealed in initial data?** Each contact list and component label remains an input, but it has independently specified relational content. The same inputs now constrain actual endpoint formation, support use, singleton failure, partition effects and both one- and two-attempt outcomes. Success probability is no longer independently adjustable. This is a useful conditional restriction, not an explanation of all underlying laws or fewer assumptions than an equally detailed rival.

**Is the variation penalty a new mathematical law?** No. It is the elementary consequence of nonlinear two-attempt success. The contribution here is its checked connection to actual component partitions, paid endpoint formation and a valid conditional population interface. A mechanistic rival retaining those relations obtains the same restriction.

**Does dispersed opportunity always win?** The equal-cost result assumes two supported attempts, fixed per-seed output and the declared encounter law. Sharing unused support, preserving several required bonds, competition, different maturation times or different partition costs can alter the comparison. Retaining all opportunities is insufficient even in the checked example; their distribution matters. No general prescription to maximize dispersal or connectivity follows.

**What is complete?** The selected interface from actual transmitted components and contact opportunities to paid reconstruction is complete at this finite scope, including the correspondence, failure cases, averaging restriction and primary-source assessment. The earlier assembly theorem, connectionist recovery and developmental memory results remain completed results to reuse.

**Next precise connection:** explain how growth and contact mechanics generate or revise the partition and opportunity distribution, and join those events to the supplied maturation and preparation law in the checked population interface. In this model the candidate partitions are still supplied. A continuation must show an actual operation producing their difference, account for its cost and subsequent replenishment, and check whether the reconstruction gain survives those additional relations. Adding another free partition-quality scalar would leave this connection unexplained.

This causal connection informs generative alignment by specifying how apparently retained constituents can lose or regain a capacity through changed relationships. It confers no ethical authority on reproductive output. G0 and the completed normative arguments retain their separate justificatory roles.

## Verification

The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContactReconstruction.lean) and [fresh-build package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/contact-reconstruction-verification/README.md) bind these claims to Lean 4.29.1. All 57 new declarations are audited; 18 have empty axiom dependencies. Other dependencies are limited to standard `propext`, `Classical.choice` and `Quot.sound`. The rebuilt 166 predecessor audits are inherited, not new results. No `sorry`, custom axiom, unsafe proof shortcut or compiler warning is accepted.

[Scoped integration checks](CONTACT-RECONSTRUCTION-CHECKS.json) cover source and log bindings, primary-source preservation, owned links, paired C14 maintenance and preservation of the broader theory's six completion requirements. No new biological experiment, independent-agent review or demonstrated broad theoretical superiority is claimed.
