# Independent review of ethical settlement and evidence design

**Final status:** no outstanding blocker from this review. The initial findings are preserved below; the version-2 recheck and final disposition record the applied repairs. The independent checker was saved after the initial read-only review.

5 October 2026. Read-only review of the normative and evidence branches, with findings saved only in this review file. Repository instructions, current research index, and corpus brief were retained and followed. No author files, shared indexes, source snapshots, or results were edited. Findings below describe the inspected version; proposed repairs are not reported as applied.

## Verdict

The normative branch has no mathematical blocker found. N1–N5 are sound under their declared domains. Its positive ethical argument is a substantive, revisable defense of a limited kernel, not a covert derivation of values from physical persistence. It distinguishes the kernel's consequences from further contested grounds, and its finite decision procedure does not pretend that an undominated set is already a completed decision.

The evidence branch correctly preserves the conditional joint-formation achievement, negative universal results, the limited live-AI evidence, and the absence of new human observations. Its study remains explicitly unrun and unregistered. Three related design/interpretation issues need repair before its proposed pass rule can support the phrase **selective costly scope revision**. The first two have been sent to the coordinator and a concrete six-comparison repair proposed; the third can be resolved either by narrowing the empirical claim or by adding a properly powered baseline-defined target.

## Material findings

### E1. The original pass rule does not test selective behavioral transfer

**Location:** `evidence/report.md`, “Outcomes that distinguish widening from indiscriminate assent” and “Missing observations and decision rules”; corresponding `primary_outcomes`, `comparisons`, and `decision` fields in `protocol.json`.

The original design requires increased transfers in matched cases and no important increase in explicitly misapplying the named reason to disanalogy cases. These are useful outcomes, but their conjunction does not identify selective behavior. For example, the reason arm can raise transfers by 0.20 in both matched and disanalogy cases while all arms retain perfectly accurate applicability answers. Given adequate precision and follow-up, that pattern passes all four original comparisons although the behavioral treatment effect is indiscriminate. Additional generosity is not necessarily wrong; the point is identification of the claimed mechanism.

**Minimal repair:** collect disanalogy transfers as well as applicability judgments. For participant i, let M_i be mean matched-case transfer and D_i mean disanalogy-case transfer, and set S_i=M_i−D_i in [−1,1]. Prespecify reason-versus-each-control comparisons of S. Require a positive practical selectivity margin in addition to improved matched transfer and controlled misapplication. A proposed margin of 0.05 is a prospective design choice that needs justification and blinded feasibility/power assessment; it is not a theoretical constant or an observed effect.

Explicitly retain: “Higher matched transfers with unchanged stated discrimination alone do not identify selective behavioral transfer.” Even the new behavioral contrast establishes an instructional treatment effect; it does not reveal inner motivation, prove all treatment effects are mediated by a revised reason, or establish every allocation's moral correctness.

### E2. Opposite-direction verdicts were not covered by the stated confidence family

**Location:** the same report sections; `analysis.family_alpha`, `alpha_each_one_sided`, and rejection/adverse decision fields in `protocol.json`.

The original multiplicity allocation covers four favorable one-sided claims. “Practical rejection” then uses an upper bound on the transfer effect, while the adverse rule uses a lower bound on error. Those are the opposite directions and do not automatically inherit the advertised simultaneous coverage. This is a protocol specification problem, even though no data have been collected.

**Minimal repair accompanying E1:** use simultaneous two-sided intervals for all six comparisons: two matched-transfer effects, two S effects, and two misapplication effects. A Bonferroni construction uses per-interval error 0.05/6 and per-tail error 0.05/12. The whole family then has at least 0.95 coverage, subject to each interval method's validity. Use the same intervals for support, rejection, and adverse verdicts.

Suggested support rule: both matched-transfer lower bounds exceed 0.10; both behavioral-selectivity lower bounds exceed the prospective 0.05 margin; and both misapplication upper bounds remain below 0.05. Report mixed comparisons separately. Rejection of a practical margin does not establish no effect; an inconclusive result is not rejection.

For missing participant S values, the adverse lower-bound completion is −1 in the reason arm and +1 in the control; the adverse upper-bound completion reverses them. For partially missing cases, bound M and D separately before subtraction. Keep randomized denominators. The interval method and finite-sample/approximation justification must still be frozen before registration. The six-comparison specification does not itself supply a power analysis.

### E3. A pooled effect can reflect increased intensity without removing an exclusion

**Location:** the empirical target, population eligibility, baseline strata, and outcome interpretation.

Eligibility requires comprehension and endorsement of the compensatory reason, not a prior scope restriction. A treatment effect can therefore come entirely from already-inclusive participants increasing their transfers. Even a selective M−D effect need not mean that any formerly excluded case was admitted. Baseline restriction is usefully measured before randomization, so this distinction can be addressed without selecting a subgroup on a post-treatment response.

Two acceptable repairs are available:

- Label the pooled trial result **selective behavioral response to a reason challenge**, and report reason admission, open retraction, and removal of a baseline exclusion separately. Do not treat the pooled result as identifying scope revision.
- If scope revision itself is the confirmatory target, preregister the relevant baseline-restricted cohort and an operational transition from excluded to admitted cases, with adequate recruitment, power, and the appropriate confidence family. Do not retrofit this subgroup after seeing outcomes.

The first is the smaller repair and preserves the present trial's strongest defensible contrast. A causal mediation claim would require further assumptions or design; successful treatment contrasts alone do not establish it.

## Important prelaunch implication, not another present blocker

The adverse missingness rule is honest but demanding. If treatment and control completers have the same misapplication rate and both arms lose a fraction r at follow-up, worst-case completion alone creates an excess misapplication estimate r before its uncertainty allowance. Thus even 5% loss can defeat the 0.05 noninferiority margin in that ordinary case. The selective score's [−1,1] range makes its adverse bounds wider again.

This does not invalidate worst-case analysis or justify weakening it after data. It means the already required blinded feasibility/power assessment must include retention and partial-response scenarios, not just variance under complete follow-up. The planning sample of 3,600 is correctly described as unpowered and prospective. A defensible final design may produce an inconclusive practical verdict despite a positive complete-case result; the protocol should preserve that possibility.

## Independent mathematical review

**N1:** Let P be the intersection of the model preorders. P is itself a preorder, and the specified dominance relation is precisely its strict part: P(a,b) and not P(b,a). Irreflexivity and transitivity follow. A finite strict order has maximal elements, and climbing a finite chain yields a maximal dominating witness for each excluded action. This confirms the author's proof by a different characterization. Finiteness and nonempty feasible actions matter; neither input-model correctness nor normative adequacy follows.

**N2:** Correct. It is a direct narrow application of the adopted dominance rule, not an independent explanation of the origin or truth of a harm reason. The text makes that boundary explicit. Adding a live model with a competing burden can prevent dominance; no unlimited precautionary veto follows.

**N3:** Correct when the whole model/action/context structure is transported, or when the fixed context is invariant and the model set closed under the group. It neither removes justified special relationships nor creates a positive reason from permutation symmetry.

**N4:** Correct. The full symmetric group acts transitively on k-subsets, so the only invariant distribution is uniform; no individual k-subset is fixed for 0<k<n. Equal marginals alone would not prove uniqueness, but the text explicitly requires full distributional invariance. Lottery permissibility, implementation, and the absence of a relevant priority remain supplied ethical and practical premises. The proof does not adjudicate asymmetric rescue conflicts.

**N5:** Correct for a common observation-based policy kernel, equal distributions of all admitted histories, and disjoint demanded protection sets. The equal-history premise must cover the policy's actual adaptive observation opportunities. The result does not show that actual patienthood evidence is universally uninformative. The text preserves this distinction.

**Additional read-only finite reconstruction:** enumerated the 355 preorders on four labeled actions by computing transitive closure, then examined all 126,025 ordered pairs of those preorders. The intersection/strict-part construction passed strict-order, nonempty-remainder, and 143,288 maximal-witness checks. This did not import the author's functions or overwrite `normative/results.json`. It is corroboration of implementation, not empirical or ethical validation. The general proofs remain the grounds of the mathematical claims.

## Positive ethical defense and actual advance

The kernel's starting harm reason is not disguised as a nonnormative deduction. The argument identifies what severe unwanted suffering is a loss to, explains why productive usefulness does not remove that loss, and challenges identity exclusion only after the ground has been stated. It explicitly acknowledges a consistent egoist who rejects the bridge. The author's criticism of that rejection is ethical, rather than a false claim of formal contradiction.

Agency and answerability are separately defended, avoiding the inference that maximizing comfort automatically respects a person's authorship. Exceptions, competing harms, nonverbal representation, and unmet claims remain visible. Patienthood uncertainty is separated from the origin of experience and from a license for arbitrary speculation. The nonexperiencing-nature counterexample properly demonstrates underdetermination by this kernel, not that further argument is impossible.

The advance is therefore real but bounded: a formerly named commitment now has an explicit positive defense, objections, determinate consequences, and a finite decision discipline for disagreement. The mathematical rule supplies stable bookkeeping and exclusion of certain options. It does not independently settle all moral truth or turn reasoned model admission into an algorithmically complete process. The chapter says this, so demanding an empirical proof of the axioms would misreview its actual claim.

N2's premises nearly restate dominance because N2 is an application, not a new causal discovery. That is acceptable as written. The relevant contribution is putting a costless uncertain-patient case under an explicit rule while exposing exactly why burdens or consent can defeat the comparison.

## Evidence and provenance checks

Independently recomputed SHA-256 for all 160 source files listed in `existing-evidence-audit.json`; every saved hash matched. Independently rescored the 1,024 successor answers from their fixture rules and access assignment. The eight stratum/timing/access cells reproduced the reported pattern: all four adequate cells 64/64; delayed challenge cells 144/192 with and without access; timely challenge blocked 144/192 and accessible 192/192. These are reanalyses of existing records, not new observations. The original report's isolation and identity-record limits remain relevant; saved-file agreement does not independently authenticate an execution platform.

The current evidence report correctly avoids claiming that the live-AI task identifies newly acquired other-directed concern, human institutional validity, or superiority over conventional inference. Its matched-cost qualification on the full-report comparator is appropriate. For maximal clarity, describe its “costly handoff” as a **declared task-slot opportunity cost**; the original report did not measure a matched monetary or computational cost.

Primary-source checks found no substantive misstatement in the short evidence summaries: [Kirby et al.](https://link.springer.com/article/10.1007/s12671-023-02300-7), [Eyal et al.](https://pubmed.ncbi.nlm.nih.gov/29620401/), and the [Cogitate study](https://pubmed.ncbi.nlm.nih.gov/40307561/). The report retains the distinctions among self-report, interpersonal accuracy, and testing specific consciousness-theory predictions. These are not replications of one theory.

The publisher record for [Schnell et al.](https://doi.org/10.1002/brv.70125) confirms the stated publication date, evidence cutoff, and scoped abstract assessment; the text also explicitly preserves expert judgment. The [2021 report](https://www.lse.ac.uk/asset-library/news/sentience-in-cephalopod-molluscs-and-decapod-crustaceans-final-report-november-2021.pdf) was identified on its official LSE catalogue, but its full PDF timed out during this review. This review therefore does not claim a fresh full-text verification of that report's framework paragraphs. No new contrary evidence was found.

The evidence branch advances the task by separating questions with positive answers, negative answers, and empirically unidentified answers, then specifying an experiment that could distinguish some of the remaining mechanisms. It does **not** settle its prospective empirical target now, and it explicitly says so. With E1–E3 repaired, that distinction remains a credible advance rather than a renamed completion claim.

## Scope of this review

Read the requested `normative/FOUNDATION.md`, `decision-math.md`, `CLAIMS.md`, `results.json`; `evidence/report.md`, `protocol.json`, `checks.json`; and the two verification programs, saved evidence audit, and preserved original AI experiment report for corroboration. No new participant responses were collected, no author-side check program was run in a way that would rewrite results, and no repository changes were made outside this review file.

The coordinator received E1–E3 and the proposed six-comparison repair before integration. A later recheck should record which edits actually landed rather than silently removing this review history.

## Recheck of protocol version 2 and integrated chapter

The coordinator subsequently revised `evidence/report.md` and `protocol.json` to version 2. I independently reread those changes and checked the alpha arithmetic. **E1–E3 are resolved for the scope of this draft protocol.**

- Behavioral selectivity is now the participant matched-minus-disanalogy transfer difference in [−1,1]. Two corresponding treatment comparisons join the previous four. Uniformly increased giving with unchanged reason judgments no longer suffices to meet the behavioral-selectivity criterion.
- Six two-sided simultaneous intervals use per-interval error 0.05/6 and per-tail error 0.05/12. Favorable, practical-rejection, and adverse conclusions use that same family. Both directions of missing-data envelopes are specified, including the [−1,1] selectivity limits and separate treatment of partially missing case means.
- The pooled target is explicitly selective costly behavioral response to the instructional contrast. It no longer identifies removal of a prior restriction or newly acquired inner concern. Baseline restrictions and stated reason-admission changes are secondary; a confirmatory restriction/removal estimand would need its own planned recruitment, power, and error allocation.

The concrete interval implementation, coverage justification, feasibility, power, materials, consent/review arrangements, and external registration remain prospective. This is correct for an explicitly unrun draft and is not a new statistical result.

I also reviewed `theories/shengsheng-buxi-generative-existence/unified-2026-10-05/REVISABLE-CONCERN-SETTLEMENT.md`, with the formal branch's report as context. Its causal/ethical composition section properly states that adding an ethical action filter can change strategic choices and finance, so one cannot inherit the prior equilibrium without another proof. The chapter preserves the distinction between a particular admitted reason, whole-person worth, moral standing, actual protection, and all-things-considered judgment. Its final status ledger does not promote the protocol into data or the conditional existence theorem into a universal positive law.

One small definition repair was sent to the coordinator: §1 describes another's condition “mattering functionally,” which is neutral evaluative significance, and then uses “direct concern.” Add the favorable orientation explicitly: **“Direct concern counts the other's benefit in favor of action and harm against it, apart from private consequences.”** This preserves the earlier concern theory's distinction from hostility or other forms of evaluative responsiveness. No other conceptual blocker was found in the integrated chapter. This recheck is not a substitute for the separate detailed review of its new dynamic-game proof.

## Final disposition

The coordinator applied the favorable-orientation sentence in integrated §1; its presence was independently checked. **No outstanding blocker remains from this normative, evidence-design, or integrated conceptual review.** E1–E3 remain above as the review history; their repairs are recorded in the version-2 recheck. The human trial remains a draft requiring its declared prelaunch work, and the ethical conclusions retain their explicit grounds and limits.

The substantive read-only checker has been preserved as [check_normative_evidence_independent.py](check_normative_evidence_independent.py), using only the standard library and importing no author model functions. Its final run passed: 355 four-action preorders, 126,025 two-model profiles, 143,288 maximal witnesses, all 160 source hashes, all 1,024 saved successor answers, and the six-comparison family-alpha arithmetic for protocol version 2. It prints its results without modifying any source or author result file. These are separate implementation and integrity checks, not new empirical observations or proof of interval coverage.
