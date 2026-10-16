# Independent review of causal diagnosis and the institutional reanalysis

5 October 2026. AI-assisted review in a separate agent context. This is an implementation and mathematical audit, not independent human peer review or a new empirical study. No production implementation or result files were modified.

## Causal construction: no substantive blocker found

I inspected [CAUSAL.md](CAUSAL.md), its [protocol](CAUSAL-PROTOCOL.md), [implementation](causal-checks.py), saved results, and the unchanged parent transition mechanism.

### Full path equivalence has a valid coupling proof

The stated initial routine and record are both zero. With admission blocked, the routine remains zero because the retained record is either zero or absent. With execution blocked, the routine remains zero regardless of the admitted record. At equal context, routine, criterion and skill, this gives equal current adequacy and therefore equal turnover probabilities. Inquiry and teaching decisions also coincide because they depend on criterion and skill. Shared draws for physical changes, inquiry error, turnover, appointment and forgetting consequently preserve equality of the projected state and the declared event channels at every step.

This is an induction on actual coupled histories, not an inference from equal means. Admitted records are allowed to differ. Including them in the observation would invalidate the claimed observational equivalence, as the text explicitly acknowledges. Inspection of a raw inquiry report need not itself distinguish the systems, because the reports can agree while their admission differs.

The code compares joint projected next-state/event distributions over 48 related reachable-state pairs, rather than just reward expectations. Its event tuple excludes admission and memory events and includes the events covered by the claim. This matches the stated scope. A diagnostic intervention that repairs one gate can distinguish the systems even though their prior operating histories have identical laws.

### Factorial interventions and adverse-information controls are correctly interpreted

Each restoration changes only its named gate. Starting with both gates blocked, either isolated restoration retains the original operating law, while restoring both permits current evidence to change routines. The reported 200-period interaction of approximately .08764735 is therefore a genuine complementarity within the supplied mechanism. It does not establish that the actual institution can enact the intervention, because enactment is externally supplied in this diagnostic experiment.

The adverse-information controls matter. At report accuracy zero and one half, the two-gate interaction is negative. The initially inherited routine carries information about the initial context; a useless report can replace that useful starting condition with a random routine. There is no theorem here that every added observation or response channel improves retention.

Setting failure-induced attrition to zero disconnects adequacy from skill loss. Then the projected criterion/skill process is independent of admission and execution, while routine adequacy can still change. The survival endpoint becomes uninformative about those interventions for a specific mechanistic reason; it does not show that admission or execution has ceased to affect every outcome.

The continuous example with a product term and zero coordinate gradients at the origin is mathematically sound. It demonstrates a possible limitation of isolated local adjustments. It is not an exact continuous fit to the finite factorial results and makes no claim that all alignment problems have that geometry.

### Delayed restoration uses the correct absolute horizon

The simulation evolves the full distribution before restoration, including systems that have already lost their final skilled carrier. It then restores the baseline gates for 200 additional transitions. In this no-entry construction, zero skill remains absorbing. Thus mass already lost cannot reenter the surviving distribution, and current positive-capacity mass equals the probability of never having lost capacity before restoration.

The implementation's initialization of the post-restoration survival calculation is valid for this absorbing-loss model. A generic version with re-entry would need to carry a never-failed monitor or explicitly kill previously failed mass before applying a recovery-capable kernel. That extension is not claimed here.

For restoration at period 100, the endpoint is period 300. The recorded admission-blocked and execution-blocked outcomes differ slightly after restoration because their memory histories differ. This is consistent with the earlier equivalence, which excluded memory and held the original gates fixed. The text correctly avoids treating these as equal-total-horizon comparisons against intervention at time zero.

### Independent numerical reconstruction

I reused the separately written [rational event enumerator](../closure-study/verify_independent.py), which does not call the production event builder or decision functions. From its rational transition rows, I formed independent double-precision matrices and propagated them for the declared horizons.

All 16 combinations of four report accuracies and two binary gates agree with the saved survival results within 1.28×10⁻¹⁵. The reconstructed interactions are:

| Report accuracy | Survival interaction |
|---|---:|
| 0 | −.006664496776939673 |
| .5 | −.004647747192972642 |
| .95 | .08764735146148767 |
| 1 | .1430624035609958 |

All eight delayed-restoration endpoints also agree within 1.28×10⁻¹⁵. At period 100, both blocked systems have survival approximately .097776873751. Their period-300 survival after restoration is .007355959293 for blocked admission and .007378651434 for blocked execution.

These are independently reconstructed transition calculations. The long matrix propagations use floating-point arithmetic; exhaustive finite support should not be described as making every displayed decimal an exact rational calculation. The original parent kernels assert nonnegative probabilities and stochastic row sums, and the independent rational rows sum exactly to one.

## The transfer bound is valid under its stated strong premises

The proposed bound

\[
\delta_D(H)=1-(1-\epsilon_{D,0})(1-\epsilon_D)^H
\]

is correct when the error bounds are in \([0,1]\), mapped initial laws can be coupled accordingly, and the one-step bound holds uniformly for every underlying reachable state and admitted action. Equal mapped histories permit coupling the same randomized history-dependent policy action. Conditional on agreement so far, the next disagreement probability is at most \(\epsilon_D\). Induction gives the product bound without assuming independence of physical disturbances.

A non-Markov mapped process is not a problem under the uniform underlying-state condition: conditional mixtures over compatible underlying states satisfy the same total-variation bound. Replacing that condition with an average error measured under one observational policy would not justify the theorem. Interventions can change which hidden states are visited.

Observation and action preservation are indispensable. A policy allowed to use hidden distinctions in only one domain is not the same abstract policy. Event monitors must be included when the transferred outcome concerns a history, a deadline or an event not determined by the plain mapped state. The text names these requirements.

The bound can be attained by a simple failure process. Let the reference process remain in a safe state forever, and let the compared process start failed with probability \(\epsilon_{D,0}\) and move from safe to an absorbing failed state with probability \(\epsilon_D\) each step. The event of failure through step H has exactly the displayed discrepancy. Thus a small one-step error need not remain small over arbitrary horizons.

The two-domain and two-intervention contrast bounds follow by triangle inequalities. They establish conditional transfer criteria, not empirical transfer between the institutional and microbial datasets. Neither analysis estimates the required uniform intervention-kernel discrepancies. Similar directions of effect cannot substitute for that missing evidence.

## Institutional reanalysis: design and arithmetic audit

I also inspected the new [empirical protocol](empirical/PROTOCOL.md), implementation, source files and saved outputs. The published Methods confirm the timing and probabilities used here: the first experiment's accuracy lottery follows investment and precedes the enforcement choice, while the second experiment's fair compensation lottery follows the authority's choices and precedes citizens' contributions. See [Dickson, Gordon and Huber (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8856613/).

### Main comparisons

For Experiment 1, `accuracy − investment` correctly identifies the fair higher-versus-lower accuracy draw. Keeping all enforcement rules avoids conditioning on a response that occurs after this treatment. The effect therefore includes changes in enforcement choice and material incentives; it is not an isolated estimate of intrinsic legitimacy. It is a contemporaneous effect averaged over the experiment's naturally generated histories, not a long-run effect of assigning higher accuracy in every period.

For Experiment 2, the beneficiary assignment is correctly distinct from its accuracy assignment. Using a fair probability for beneficiary status does not incorrectly apply the first experiment's accuracy probabilities to the second experiment. The all-rule boundary contrast is likewise a contemporaneous effect under the installed process.

An independent reconstruction read the raw records, grouped them by session/period/group, recovered each outcome from the four citizen decisions, checked it against every group record, and calculated session contrasts with rational arithmetic. It reproduced:

| Contrast | Exact equal-session estimate | Approximate session-t interval |
|---|---:|---:|
| Experiment 1 higher accuracy | 29/288 = .100694444444 | [.015706684112, .185682204777] |
| Experiment 2 authority beneficiary | −163/3360 = −.048511904762 | [−.119276937334, .022253127810] |

The primary result is approximately +10.07 percentage points in the group contribution proportion. The boundary result is approximately −4.85 points and its interval crosses zero. It does not establish equivalence or absence of a reciprocity mechanism.

### Independence and remaining inferential limits

The full-session centered Horvitz–Thompson statistic has the appropriate known-probability form. Centering by .5 adds a mean-zero assignment term under the fair randomization. Equal session weighting is the declared target; it differs from equal weighting of all group-periods. Repeated participants and within-session history do not become independent observations merely because new group assignments occur. Using six and seven session estimates respects that clustering, although a Student-t interval with so few potentially heterogeneous sessions has only approximate coverage.

The secondary investment and rule subgroups deserve an additional qualification. Their current values precede the current treatment, so they do not create the primary post-treatment-conditioning error. But subgroup membership in later rounds may respond to earlier treatments, making the total number of eligible rounds in a session random and history-dependent. Dividing by that realized number produces a ratio-type sequential summary. It should not be advertised as exactly finite-sample unbiased Horvitz–Thompson estimation for a fixed eligibility population. This qualification does not affect the full-sample primary or full-sample boundary contrast, whose denominators are the fixed complete session sizes.

The matched-material investment comparison remains explicitly descriptive/identification-qualified. The missing investment cell in one session is disclosed and not imputed; its five-session summary is not the six-session primary. Chosen investment is not independently randomized simply because participants were assigned roles.

The protocol was frozen before this reanalysis's outcome inspection but after the published results and author code were known. These results are therefore an exploratory secondary reanalysis with transparent choices, not a new blind confirmation. They establish a bounded component response in the experiment and leave succession, self-maintenance, changing goals and quantitative cross-domain transfer untested. No new subgroup search, additional model fit or outcome exclusion was introduced by this review.
