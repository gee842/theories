# Observation interfaces and noticing an omitted possibility

Independent audit, 5 October 2026. Scope: the copied `questions-without-anomalies`, `inherited-evidence-under-model-revision`, their mathematical memos, and implementation files. Original theory files were not changed. This audit independently verifies two exact witnesses; it does not rerun every source experiment or treat AI-generated research notes as empirical evidence.

## Answer this evidence supports

An inquirer can notice a possibility absent from its current account by **preserving or acquiring a distinction its current account discards, making a candidate connection between that distinction and a consequential outcome, and allowing that connection to receive an independent test even when the old records show no anomaly**.

This is a constructive mechanism with a precise limit. A new feature by itself does not show relevance; an anomaly does not establish useful action; a useful candidate does not automatically justify its investigation costs; and these sources supply the candidate language rather than explaining unrestricted concept invention. The evidence supports changing the conditions under which a possibility can become testable, not a guaranteed procedure for conceiving every important possibility.

## Exact information constraint

Let D contain everything the admission procedure can inspect, including public actions, silence, retained histories, outcomes, and side channels. For an admission probability g(D) between zero and one,

    | E_U g(D) - E_E g(D) | <= TV(P_U^D, P_E^D).

Proof: write g(D) as the integral over t in [0,1] of the indicators of g(D)>t, then bound each probability difference by total variation. Identical observation laws give identical admission probabilities for every rule, including arbitrary computation and independent randomization. If the entire D-law is identical, more samples from that same interface remain identical in law. For nearly identical laws, the bound must use the joint experiment actually available; one-sample total variation is not automatically the many-sample bound.

Consequences:

- Requiring a low false-admission rate in E necessarily gives a low admission rate in indistinguishable U. This does **not** prohibit investigating both. It prohibits reliably targeting U on that information alone.
- A richer observation channel may break the equivalence. Nothing in this theorem prevents experiments, linked outcomes, testimony, or public actions from doing so; all usable channels must enter D.
- A randomized challenge route can finance an inquiry despite indistinguishability. Randomization itself supplies neither the missing information nor the missing concept.

Source locators: `sources/15-codex-theory-conversations/2026-10-05-questions-without-anomalies.md:11-22`; `_process/research/2026-10-04-integrated-evolution/prospective-revision-math.md:32-64`. Both are under `source-snapshots/` in this directory.

## Independently verified witness: identical routine success, different valuable action

The source constructs four-switch words B, total K, a fair endpoint Z, and one subsequent binary need Y per independent window. Let d be late switches minus early switches. In worlds E and U the entire word B is iid Bernoulli(1/4), so there is no historical anomaly distinguishing them. In E, the next-switch probability is 1/4 in every context. In U it is 9/20 when d>0, 1/20 when d<0, and 1/4 otherwise. For Z=0, this is the need probability; for Z=1, need is its complement.

The routine policy responds only when Z=1, paying 3/10; response prevents a unit need loss. The candidate additionally responds when Z=0 and d>0. Maintaining ordering for candidate use costs 1/500 per future decision, including ineligible decisions.

I independently enumerated all 64 (B,Z,Y) atoms in each world using exact rational arithmetic, without importing the source implementation. The resulting witness is in `interface-witness.py` and `interface-witness-results.json`.

| Quantity | Exact result |
|---|---:|
| Total variation of routine (K,Z,Y) between E and U | 0 |
| Total variation of archived (B,Z), without its linked future Y | 0 |
| Total variation of linked (B,Z,Y) between E and U | 69/640 |
| Routine expected operating loss, E and U | 11/40 = .275 |
| Candidate eligibility probability, E and U | 69/512 |
| Candidate net gain per decision in E, including continuing record cost | -2237/256000 = -.00873828125 |
| Candidate net gain per decision in U, including continuing record cost | 4663/256000 = .01821484375 |

All four source worlds E/P/T/U have exactly the same routine (K,Z,Y) law. E/U have identical archive (B,Z) laws; P/T have identical archive laws. These equalities were checked exactly, not within floating-point tolerance.

The practical missing distinction is a **relationship**, not merely a missing raw field. Archiving B without linking its subsequent outcome cannot distinguish E from U. Collecting linked B,Z,Y observations can: within the pre-outcome eligible stratum, the need probabilities are .25 versus .45. With independent repeated linked observations, positive eligibility, and these fixed distinct hypotheses, a consistent statistical test exists. No finite sample is guaranteed to identify the world without error because both assign positive mass to every possible atom in E/U.

The equalities for the routine and archive interfaces are separate equalities. They must not be combined into a claim that matched (K,Z,Y) and (B,Z) records from the same cases remain uninformative: matching them reconstructs the informative (B,Z,Y) channel. The actual prospective protocol gives historical routine K,Z and retained B; the linked future outcome is bought in fresh validation (`experiments/prospective-revision/PROTOCOL.md:20-25`).

The source's paid validation calculation reports adoption of U's useful candidate with probability .9383754 under direct validation, versus .0271941 when first gated by a 28-window historical-anomaly audit. Those are source-model results, not independently rerun in this audit; the underlying observational equivalence and value sign reversal are independently verified. Their interpretation requires the specified sample sizes, independent cohorts, known response effectiveness, fixed candidate, fixed thresholds, and costs. The source explicitly does not infer that direct testing is universally preferable.

Source locators: `questions-without-anomalies.md:24-43` defines the worlds/interface; `:61-92` gives validation assumptions and results; `prospective-revision-math.md:111-171` distinguishes deployment-benefit certification from research-cost recovery and unknown causal effect; `:273-279` records numerical results. Implementation locators: `experiments/prospective-revision/model.py:12-59` defines the atoms; `:101-120` gives costs; `test_model.py:31-60` contains the original observation-equivalence tests.

## Independently verified witness: an old sufficient statistic can erase a new question

Histories 00010 and 01000 both end at zero and contain two switches. Under a homogeneous switching-rate family, every member assigns them identical likelihoods. Their shared unknown-rate posterior prediction is 8857/20324 = .4357901988 for the equal prior on rates .05/.45.

Under equal prior on slow-then-fast and fast-then-slow, with two transitions per regime and the last regime persisting, their first-versus-second-model likelihood ratios are (171/11)^2 and its reciprocal. Their next-need probabilities become:

| History | Ordered two-model family | Nested union of ordered and homogeneous families |
|---|---:|---:|
| 00010 | 26329/58724 = .4483516109 | 73/164 = .4451219512 |
| 01000 | 3033/58724 = .0516483891 | 145/964 = .1504149378 |

At response cost .3 for preventing unit loss, these recommend opposite actions in both the ordered family and its nested union with the old family. The same independent Fraction program checked all these values. This is actual expansion of the old model family in the union example, not merely a switch between unrelated families.

The candidate question is usable: **Did the system become more volatile or less volatile?** It arises by asking whether a distinction discarded by the summary—early versus late changes—could alter a future decision. Retaining two timed counts answers this question as well as retaining the full word in the declared families. There is no implication that every omitted detail matters or that full raw storage is optimal. Free richer information cannot worsen optimized loss under the same model/actions/losses, but paid recording can have negative net value.

Source locators: `sources/15-codex-theory-conversations/2026-10-05-inherited-evidence-under-model-revision.md:9-50` specifies the witness and provenance; `:54-76` states the decision-relative sufficiency result; `experiments/revisable-inheritance/test_model.py:20-29` checks the witness in the original implementation. Exact independent results are retained in this directory.

## Distinct operations that the answer should preserve

1. **Candidate formation:** articulate a relation the old account did not admit. Neither audited experiment generates unrestricted new concepts; alternatives are analyst supplied. Examining erased distinctions is a useful proposed procedure, not an experimentally established complete generator.
2. **Admission to investigation:** grant a finite route to collect evidence, including for candidates that cannot first pass the old archive's anomaly criterion. Admission is not acceptance of the claim.
3. **Identification/validation:** buy an observation channel on which the consequential alternatives differ. A positive result has only the scope of the tested relation and sampling design. If response effectiveness is unknown, untreated need labels alone do not identify treatment benefit; a causal design is required.
4. **Decision and feasibility:** compare action changes against operating cost, inquiry cost, timing, and available resources. A discovered difference can be real yet action-irrelevant or too costly to use.
5. **Revision of model support:** admit the candidate into the account. For a finite family, ordinary conditioning cannot assign positive posterior probability to an excluded zero-prior member with positive likelihoods. This is distinct from small positive prior probability and from a zero-mass singleton under a continuous prior.

Source locators for the support distinction: `inherited-evidence-under-model-revision.md:78-84`; `_process/research/2026-10-04-integrated-evolution/model-revision-inheritance-math.md:193-219`. Source locators for institution-level implication: `questions-without-anomalies.md:113-119` and `:131-135`.

## Recommended synthesis language and limits

Supported synthesis: **Do not wait only for the current model to fail on its own measurements. Keep a route for someone to propose a missing distinction, preserve or obtain evidence that could reveal its connection to consequential outcomes, and test it before deciding whether to change action.** A useful operational prompt is: **Which different situations do our records treat as identical, and what future observation would make that merger matter?** The first witness adds: **Which relationships have we failed to link, even among fields we already possess?**

The source evidence does not justify a universal exploration rate, guarantee discovery of unconceived alternatives, determine whose testimony deserves standing, or settle which outcomes ought to count. Its loss functions, truthful observations, shared purposes, causal efficacy, query language, resource prices, and continuation opportunities are assumptions. It does refute the general claim that useful omissions must first manifest as anomalies in incumbent records, and it gives an exact, affordable-within-the-stated-model way to reopen learning.

Evidence status: the information bound is a standard exact inequality with a proof inspected here; both finite witnesses were independently reproduced exactly; published numerical adoption figures were read but not rerun by this audit; institutional recommendations are conditional design inferences; candidate generation beyond a supplied language remains unestablished by these sources.

## Narrow independent review of the new two-bit teaching example

Reviewed root-owned `check_joint_distinction.py` and its delivered `outputs/missing-possibility-check.json`. Verdict: the probability and operating-loss claims are correct under the recorded observation boundary.

In the interaction world, fair independent X,Z produce Y=X xor Z. Every pair among X,Z,Y is uniform on its four outcomes, exactly as in the null world with three independent fair bits. The complete joint laws differ: four parity-consistent atoms have mass 1/4 versus 1/8 and the other four have mass zero versus 1/8, giving total variation 1/2. Independent-case samples from any of the three pair projections therefore have the same observation law. Simultaneously computed aggregate tables from the same finite cohort can have cross-table dependence, so equality of their joint sampling laws must not be asserted; the saved output explicitly avoids this error.

For either world, without a joint relation or with only either attribute, need probability is 1/2. Always protect costs .3 and minimizes operating loss. In the interaction world, protecting the half with X!=Z costs .5*.3=.15 and prevents every failure. In the null world, that same policy costs .15 for protection plus .5*.5=.25 untreated loss, totalling .4. These agree with the exhaustive 16-policy code enumeration. Randomized policies cannot improve these finite fully specified optima because expected loss is linear in action probabilities, so a deterministic minimizer exists.

The .15 saving is an operating saving before any data collection, linkage, testing, or continued feature-use expense. It must not by itself be described as positive net value of discovery. The illustration also stipulates perfect protective effectiveness; it does not learn a causal intervention effect from outcomes. Its grammar and parity candidate are supplied, so it demonstrates a candidate available through feature recombination, not observed spontaneous concept generation. Minor wording precision: the initial code docstring says "conjunction"; "joint refinement" or "combination" is more exact, because XOR is not itself a single Boolean conjunction.
