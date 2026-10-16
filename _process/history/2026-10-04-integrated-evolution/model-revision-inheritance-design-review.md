# Model revision, inherited records, and endogenous capacity

5 October 2026. Design review of the proposed joint team experiment. No implementation or numerical trajectory experiment is reported here. The model family, communication vocabulary, and perfect current diagnostic are supplied isolation assumptions. They do not implement spontaneous concept formation or integrate every component of the earlier candidate-discovery experiment.

## A chronology that does not anticipate its own revision

The adopted small benchmark observes four historical transitions. A public final historical state \(Z=S_4\) survives through routine behavior or a record. A retention format is fixed before the private path is observed: last state only, total switch count \(K\), two time-block counts \((K_e,K_l)\), or the complete four-bit switch word. Nontrivial formats pay acquisition and retention charges.

At handoff, both parties receive the expanded model family. The sender sees only the retained statistic and public \(Z\), then chooses paid readiness and optional truthful publication of that statistic. This ordering prevents readiness from encoding historical distinctions already erased by the archive. It still permits readiness and silence to communicate distinctions that remain available.

Treat the earlier format as an externally fixed comparison unless a prior over forthcoming model revisions is specified. If the family is first revealed at handoff, minimizing the earlier format's cost using that family is an anticipatory benchmark, not a feasible policy chosen by an unaware predecessor. Two defensible reports are: the value of each inherited format after the supplied revision, and a separately labeled best-format benchmark for someone who anticipated the new family. A historically selected format under a known old family can also be evaluated after a specified surprise. Do not conflate those chronologies.

If historical observation is mandatory, its charge is real but the acquisition decision is not endogenous. Endogenous readiness and publication remain useful results. To claim endogenous acquisition, compare a pre-history purchase option with a no-purchase option using a declared prior over the information and models that the buyer expects to face. Do not optimize that purchase using a privately revealed future family that was unavailable at the time.

## Two families that separate model uncertainty from data loss

Take \(S_0\) fair and independent of the regime. A transition flips the state with its regime's probability. In the persistent family, the probability is either \(l=.05\) or \(h=.45\) throughout, each initially equally likely. Then

\[
P(S_4=z,K=k\mid\theta)
=\tfrac12 {4\choose k}\theta^k(1-\theta)^{4-k}.
\]

The total switch count determines the regime likelihood; \(Z\) identifies the latest state. Their combination is sufficient for future-state prediction under this family. Historical switch order carries no additional likelihood information. A last-state record is sufficient if the transition rate is known, but generally insufficient once uncertainty over that rate is introduced.

For example, with equal prior weights, \(K=0\) gives posterior probability approximately .100999 for the fast regime, whereas \(K=4\) gives .999848. With the same last state \(Z=0\), the next-state probabilities are approximately .090400 and .449939. A response cost .4 with unit untreated loss puts these beliefs on opposite sides of the no-diagnostic action threshold. This is an algebraic illustration of lost decision-relevant information, not a claim that a diagnostic or another channel cannot compensate.

In the ordered family, the two hypotheses are slow then fast versus fast then slow, with two historical transitions in each half. Specify that the next transition uses the terminal regime. Timed counts have likelihood

\[
P(K_e=a,K_l=b\mid l\!\to\!h)
={2\choose a}{2\choose b}
l^a(1-l)^{2-a}h^b(1-h)^{2-b},
\]

with the rates exchanged under the other hypothesis. Summing over \(a+b=k\) gives the same total-count likelihood in both hypotheses: the two convolution factors merely exchange places. Fair \(S_0\) makes \(Z\) independent of the switch word. Consequently \((Z,K)\) carries exactly zero information about regime orientation in this family.

Any readiness or publication rule based only on \((Z,K)\), with randomization independent of the hidden regime, preserves that indistinguishability. Better decoding cannot reconstruct the deleted temporal distinction. Readiness can nevertheless make a new current diagnostic available, supplying new evidence through a different route. Archive insufficiency is not impossibility of all recovery.

Timed counts restore the full switch word's likelihood for this family. Indeed the orientation likelihood ratio depends only on \(K_l-K_e\), so timed counts are sufficient but not minimal. A future model with a different change-point or dependence structure can require additional information. No finite summary here has been proved sufficient for unrestricted future revision.

At four transitions, fixed-length coding requires three bits for five total-count values, four bits for nine timed-count pairs, and four bits for sixteen switch words. Public \(Z\) need not be transmitted again; the format and transition count are also public. Thus the proposed timed and full formats have equal fixed-length payload size in this smallest example. A claim that timed counts save storage requires another coding assumption or a longer window. Report the coding convention explicitly rather than charging a presumed compression benefit.

## A small exact joint optimization

For each fixed format and public \(Z\), let private retained type \(i\) have probability \(w_i\) and next-state probability \(p_i\). The sender chooses readiness \(u\in\{0,1\}\) and publication \(P\in\{0,1\}\). Publication reveals the complete retained statistic truthfully; its cost is fixed by the chosen format. Readiness costs \(m\). The receiver sees \(Z\), format, readiness, publication status, and any content, as well as the agreed prescription.

For unit untreated loss, response cost \(c\), and perfect current diagnostic cost \(d\), the receiver's undominated one-period actions have conditional costs

\[
g_A(p)=p,\qquad g_B(p)=c,
\qquad g_T(p)=d+cp.
\]

The last action requires readiness and means diagnose, then respond only to a positive result. If the loss scale is \(L\), replace the first expression by \(Lp\). Treatment has a separate supplied operating budget. Acquisition, retention, readiness, publication, and a possible diagnostic must fit the inquiry budget on each realized branch. Because historical acquisition is included, this is a total episode budget per realized path, not a per-period procurement cap.

Complete sender enumeration is unnecessary. Published content identifies the retained type, so its best feasible receiver response can be precomputed. Only silent messages pool types. Enumerate two possible responses to silent absent-capacity and three to silent ready-capacity: six decoder combinations **for each public \(Z\)**, or thirty-six joint combinations if optimized together. For each decoder, independently choose the cheapest feasible \((u,P)\) for every private type. Sum \(w_i\) times those costs and minimize over the six decoders.

This is exact because the finite common-interest optimization can minimize jointly over sender and receiver policies in either order. With a fixed decoder and additive expected cost, sender choices separate by private type. The branch budget is enforced inside each choice. An additional shared expected-expenditure constraint would couple types and require a constrained program or a valid dual treatment; the independent minimization would then be insufficient.

Verify the optimum by reconstructing the induced posterior in every positive-probability public signal cell. The receiver's selected action must be optimal and feasible for that posterior. A decoder can be arbitrary on an unreachable cell. Do not reset a silent cell to the unconditional prior: its likelihood depends on which types the agreed sender prescription leaves there.

## Which comparisons isolate which mechanism

- **Fixed readiness before data** removes readiness as a private signal and separates the archive's direct information value from information encoded in capacity choice. Fixed zero and fixed one also change the physical ability to diagnose, so report that resource difference.
- **No payload** removes the explicit statistic message, but endogenous readiness can still communicate. It is not a no-communication control.
- **Current diagnostic unavailable** removes new measurement. If readiness remains privately chosen and visible, it can still function as a costly signal even though it has no measurement use. Either retain and name that signaling role or forbid it explicitly for a separate no-channel control.
- **Last-state-only retention** means the sender has no private switch information after compression. Its capacity choice cannot secretly use the raw path. This is an information-set restriction, not merely deleting a payload field.
- **Equal-cost format comparisons** can isolate the information effect of finer records; the realistic fee comparison adds storage and transmission economics. Equal feasible budgets alone do not imply equal expenditure. Under appropriately nested information and equal feasible costs, the richer team can ignore extra detail; this supplies a consistency check, not a surprising empirical result.

Capacity signaling may shrink or remove the value of an explicit archive in some parameter settings. That is an informative result, not evidence that the successor forgot. Likewise, cheaper coarse instructions can be adequate for one fully specified future decision. Their adequacy does not establish that they preserve evidence for other questions. The present truthful-statistic vocabulary restricts the coding problem; it is not an optimum over every possible recommendation language or future task.

All charges that the receiver can see are part of its signal. Fixed format costs and observed readiness/publication make the proposed bill inferable without leaking an additional private variable. Private variable-length record costs, a state-contingent acquisition duration, or an itemized failed transmission bill would require an expanded observation interface. If silence is perfectly reliable, describe that supplied communication assumption; do not borrow robustness to message loss from the preceding separate handoff module.

## Checks before interpreting a result

Enumerate all sixteen switch words under each regime and verify normalization, public-state independence, the persistent total-count likelihood, and ordered-family reversal symmetry. Check full-word and sufficient-statistic conditional predictions directly, not merely their average losses. Confirm that the pre-diagnostic signals of a capacity or publication policy under total-count retention cannot separate ordered regimes. Fresh measurements are a different information source. These are exact properties of the chosen family.

For optimization, check all branch costs, silence posteriors, published-type posteriors, and the Bayes optimality of every used receiver response. On a smaller type space, compare the six-decoder method with brute-force joint sender/receiver enumeration. Preserve examples where costly richer records lose, a fresh diagnostic makes them unnecessary, or all channels are unaffordable. An endogenous financing example should display the resulting readiness/publication prescription, not only an average objective value.

The strongest justified conclusion would be conditional: what an inherited record permits a successor to infer depends on the revised model family, while the cost and signaling effects of preserving intervention capacity change which information is worth transmitting. The experiment remains a small common-interest team with supplied purposes, model families, current diagnostic, and communication semantics. It does not establish that more historical data is always better, that all revision is justified, or that one scalar captures human coordination or alignment.

## Implementation audit: endogenous inspection before private information

5 October 2026. Reviewed `experiments/revisable-inheritance/model.py`, `PROTOCOL.md`, `test_model.py`, and the control definitions in `analyze.py`. This section supersedes the initial design's references to a historical acquisition charge: the implemented experiment charges sunk retention and optional later **inspection**, rather than implementing the earlier collection decision. No substantive mathematical or information-flow defect was found in the reviewed implementation.

The actual chronology has an additional public choice. Conditional on public final state \(Z\), fixed archive format, and the supplied model family and prior, the caretaker chooses inspection \(q\) and channel opening before reading private contents. With \(q=0\), the implementation uses a single private type containing only the correctly computed \(Z\)-conditioned prior. With \(q=1\), it uses the inspected retained statistic. Thus neither the inspection flag nor channel opening selects on unobserved archive contents; they do not introduce an unmodeled signal. Readiness and payload are chosen afterward and may legitimately depend on the resulting private type.

The posterior calculations are consistent with the generating model. An independent fair initial state makes \(Z\) independent of both the switch word and the model index. Therefore the code's conditional word mass is the prior mixture of word likelihoods, without an additional \(Z\)-dependent likelihood factor. Aggregating those masses and conditional predictions by the retained statistic yields the correct type posteriors. The expanded family is the union of the two constant-rate and two ordered hypotheses with its explicitly supplied uniform prior; admitting that family is an exogenous change of representational support, not discovery by this optimizer.

For each fixed public context, inspection choice, and channel-opening choice, the six-decoder argument is sound. A truthful payload identifies the complete available private type, so its optimal receiver action can be computed immediately. Only silent absent-capacity and silent ready-capacity signals require joint decoder enumeration. Conditional on a decoder, all sender choices separate by type because costs add in expectation and feasibility is imposed on each realized branch. Minimizing over the finite decoder set and then over the pre-private inspection/channel choices therefore gives the finite-team optimum within the stated action and message vocabulary. There is no shared expected-cost constraint that would invalidate this separation. Randomizing complete feasible policies cannot lower this unconstrained expected objective below the best deterministic policy.

The implementation's posterior consistency check appropriately compares the **values** of the selected and Bayes-optimal actions, rather than requiring the same action index at a tie. Unreachable silent cells need no posterior restriction. For positive-probability silent cells, the posterior is reconstructed from the types that the selected sender prescription actually pools there. Full-type publication cannot change the posterior within the already revealed type. The selected actions also pass their realized-branch affordability checks.

As an additional independent execution beyond the repository's four-type \(N=2\) tests, I compared the decoder solution with exhaustive sender-prescription enumeration for the five total-count types at \(N=4\), for all three model families, inquiry caps .06 and .4, and diagnostic cost .08. All six comparisons had zero difference in reported floating-point total loss. This checks the two enumeration orders on a larger type space; it is conditional numerical verification, not empirical evidence about social coordination. No implementation files were edited for this audit.

Costs are charged once. Retention is paid on every branch, including skipped inspection; inspection and channel setup are paid when their public choices are selected; readiness and truthful payload fees depend on visible actions; the diagnostic fee is paid only when exercised. Consequently an itemized inquiry bill conveys no extra private signal omitted from the decoder. The diagnostic's response cost is accounted separately from its inquiry fee. An unavailable current diagnostic does not remove readiness's signaling role, and the no-payload control likewise does not remove all communication; the protocol and tests preserve those distinctions.

Interpretation must retain four limits. First, endogenous inspection is inquiry into an already retained record, not endogenous historical acquisition, preservation across repeated succession, or model admission. Second, the fixed-zero and fixed-one readiness controls each impose that constant; a claim about the **best** readiness policy chosen after public \(Z\) but before private contents would additionally minimize those alternatives separately for each \(Z\). Third, a format comparison after a supplied revision is a conditional value calculation, not a retrospectively feasible earlier format choice. Fourth, the sufficiency and equal-price equivalence of timed counts and raw words apply to the specified model families and one future decision, not unrestricted future questions. None of these limits invalidates the implemented joint optimization.
