# Independent review of the finite formation–succession join

5 October 2026. Sections 1–7 cover the six-arm baseline in [PROTOCOL.md](PROTOCOL.md), [analyze.py](analyze.py) and [analysis.json](analysis.json). The final addendum separately audits the subsequent reopening extension. This is AI-assisted implementation and model review, not independent human peer review or empirical validation.

**Finding: no remaining blocker in the stated baseline transition mechanism.** The join actually couples raw experience, uncertain nomination, ratification, execution, consequences, succession and retained skill. Two instrumentation weaknesses found during review were corrected without changing the transition kernel or primary endpoint values. The strongest remaining limits concern what is supplied by assumption and what happens after an incorrect representation is installed.

## 1. Ratification does not see the hidden answer

The candidate-feasibility function receives the experimental arm and uses the supplied noise level, proposed harm ceiling and burden ceiling. It does not receive the candidate's expression, true target, physical harm profile or correctness flag. Every expression is assessed under its own assumed response family. Consequently all four candidates can be ratified at burden ceiling .45, while none is ratified at .40. An incorrect frame remains capable of passing the ratification gate.

The actual physical target X1 appears where it belongs: in generating harm and in the analyst's independent outcome evaluation. It is not passed into the nomination or authorization decision. Nomination uses observed linked mismatches, including noise; it does not select the physically correct expression by name. Uniform tie handling is implemented.

This is not an absence of all epistemic assumptions. The learner is given the raw attributes, four-expression grammar, interpreters and structural response family, including the noise parameter. That family permits inversion of observed action/harm records into a noisy target label. This is a valid bounded learning construction, not a general causal-discovery method for unknown response laws. The ratification procedure also assumes the represented participants' endorsements once candidate-assumed feasibility holds. Their legitimacy, formation and preservation are not derived here.

## 2. Actual harm changes continuation

The portfolio uses installed practice, skill, a pending complaint and the presence of a frame. It does not inspect whether the frame is true. Ordinary actions use the installed expression when skill, ratification and execution authority are present. The physical environment then generates case-level harms.

Turnover depends on the realized number of harms divided by the number of cases in that round. Complaints also depend on realized harms. Thus adverse effects alter both the opportunity to undertake inquiry and the future skill/appointment distribution. The code retains the joint distribution of inquiry mismatches and harm rather than multiplying independent nomination and survival probabilities.

For two otherwise identical skill-2, adaptive states with a ratified frame, independent raw-case enumeration gives:

| Installed expression | Mean physical harm per ordinary case | Turnover probability |
|---|---:|---:|
| X1 | 3/20 = .15 | 2/25 = .08 |
| 1−X1 | 17/20 = .85 | 11/50 = .22 |
| X2 | 1/2 | 3/20 = .15 |
| 1−X2 | 1/2 | 3/20 = .15 |

This is a concrete feedback witness. Continuation depends on the actual consequences of inherited execution, not a bonus granted to a type labeled correct. Appointment weights remain stipulated, and the turnover law is a synthetic behavioral premise rather than an empirical estimate.

For ordinary F and T work, averaging the four contexts before drawing the number of harms is mathematically valid here: cases, action randomization and physical response noise are independent fresh draws. The marginal harm on each case is Bernoulli with the computed mean, so the number of harms has the binomial law used in the code. Context-specific means are retained separately for plural assessment. The simplification would need reconsideration with shared shocks, dependent cases or context-dependent future transitions not summarized by the recorded harm count.

## 3. The effort budget is real within the declared model

F uses both effort units for ordinary cases. T uses one for an ordinary case and one for delivered training; Q uses one for an experimental case and one for inquiry/record work. Both training and inquiry therefore displace ordinary service. At skill 1, training occurs before at most one carrier is lost; it does not create a mentor at zero skill. Inquiry requires skill 2.

The training-blocked arm deliberately reallocates its attempted T portfolio to F, as frozen in the protocol. It changes both regeneration and immediate ordinary output; it should not be read as a treatment that holds output effort fixed while removing only a costless training effect. Similarly, linked and aggregate arms match effort cost for a given portfolio, not realized cumulative effort histories after consequences begin to differ.

The ledger counts inquiry cases and inquiry slots separately, and includes physical harm from the experimental cases. Ordinary and inquiry harms are now reported separately as well as in total. Extra experimentation cannot appear harmless merely because it is excluded from the ordinary-service category. However, the two-unit budget covers the specified case, inquiry and training work; it is not an empirical costing of every political, measurement or computational function. The constitutional permission to admit the grammar is supplied.

## 4. Claimed and actual satisfaction are distinct

The endpoint evaluates the enabled policy's four context-specific expected harms and expected action-1 burden using the physical environment. Ratification is an independent state variable. Skill loss and blocked execution prevent success even if a correct expression had previously been represented. The infeasible-burden control does not invent a relaxation to generate a successful endpoint.

These are properties of a current policy's expected responses to fresh cases. They are not the probability of zero realized harms, of meeting a quota in every sample, or of maintaining the constraints throughout the whole preceding history. Cumulative realized-case consequences are separately integrated over the event branches.

At round 25, the recorded unconditional probabilities include:

| Arm | Actual plural satisfaction | Ratified but actually violating |
|---|---:|---:|
| Linked inquiry | .55288825 | .07270725 |
| Aggregate nomination | .16640940 | .34701666 |
| Protected succession/retention benchmark | .85107159 | .14888622 |

The separation is substantive: improving preservation can preserve an incorrect judgment too. The protected arm guarantees the relevant skill within this supplied initial condition and work schedule, but does not guarantee correct interpretation or actual plural satisfaction.

## 5. The baseline does not reopen an installed frame directly

Once a frame exists, a skilled adaptive institution does not query it again, even when new harms generate complaints. Inquiry requires `frame == none`. A frame can be reconsidered only after archival loss removes it; the resulting loss also erases other parts of the package. In the protected benchmark, that erasure is disabled. A mistaken frame is then retained indefinitely within the unchanged baseline environment.

The benchmark's approximately .8511 endpoint satisfaction is therefore consistent with the finite-batch nomination probability; it must not be described as eventual guaranteed learning. Nor does the baseline establish an ongoing cycle of reviewing the most recent frame against new evidence. A separate reopening mechanism would be a substantive new intervention with its own inquiry costs and opportunities to replace a correct frame with a worse one.

The aggregate comparison has another important scope boundary. Under the specified randomized Q portfolio, omitted attribute-to-outcome links make nomination uniform across the four expressions. But ordinary deployment under those expressions has the different mean harms listed above. Another learner could compare deployment-level aggregate outcomes to learn about candidate quality without retaining every raw linked record. Thus this experiment supports the advantage of linked inquiry under the declared portfolios and nomination rules. It does not prove that all aggregate representations are uninformative, that raw-record retention is universally necessary, or that the linked procedure is the best feasible learner.

## 6. Independent raw-case verification and repaired metrics

The saved [independent checker](verify_independent.py) starts from binary context, action, response-noise and complaint draws using rational arithmetic. It does not call production functions for portfolio choice, expression evaluation, physical profiles, inquiry observations, nomination or candidate feasibility to construct its rows. It then enumerates nomination, training, turnover, appointment and package transmission itself.

Sixty representative transition rows were checked: ten states under each of the six arms. These cover initial operation, one-carrier training, a volume incumbent losing its final carrier, correct and incorrect installed frames, empty and nearly complete query archives, tied candidate scores and zero capacity. Some checks intentionally cover valid boundary states beyond those reached under a particular arm's supplied initial state.

- Rational row sums and the two-unit effort ledger equal their targets exactly.
- Transition supports match production for every checked row.
- The maximum transition-probability difference is 2.22×10⁻¹⁶ after converting rational results to doubles.
- All eleven reward fields match; the largest difference is 8.33×10⁻¹⁷.

The [machine-readable report](independent-verification.json) records all checked states, the consequence witnesses, and source/checker/protocol hashes. It is reproducible by running the checker. This is a targeted independent check, not a second exhaustive enumeration of every 25-round path distribution. Production performs the full reachable-state propagation; its floating-point mass checks do not make every displayed endpoint an exact rational number.

Two weaknesses were corrected during this audit. First, the original aggregate-nomination check was a numerical identity that did not call nomination; it now tests uniform nomination across every complete-batch mismatch-count pair. Second, an archive-loss reward originally counted only failed transmission even when loss of the final carrier necessarily erased the package. The corrected metric counts terminal package loss with probability one at that turnover and does not manufacture archival-loss events for an already skill-zero system. Independent reward reconstruction confirms the correction. These changes improve verification and accounting without changing successor probabilities or primary endpoint values.

## 7. Scope of the integration achieved

This is a real finite join: nomination uncertainty, admitted representation, an adopted plural commitment, executable response, realized harm, inquiry/training effort and successor preservation share one state transition system. Incorrect candidates can be adopted; their consequences affect subsequent institutional histories; and the realized endpoint is computed from the joint kernel rather than a product of unrelated module success rates.

It remains a bounded construction with fixed raw categories, grammar, environment, nomination process, response law, rights of admission and ratification procedure. Endorsements are stipulated, constitutional replacement is not modeled, and endogenous preservation of those constitutional mechanisms is not established. The no-reopening limit and aggregate-learning alternative above are especially relevant to claims about general revisability. The model advances internal integration; it does not complete the general theory or validate its empirical transfer.

## Addendum: the separately frozen reopening extension

I inspected [REOPENING-PROTOCOL.md](REOPENING-PROTOCOL.md), [reopening.py](reopening.py) and its [saved results](reopening-analysis.json). The extension implements the two stated changes: a skill-2 adaptive institution can query while retaining a frame, and completion consumes the pending complaint. The baseline source and results are preserved, and their hashes match the extension's recorded inputs.

### Mechanism and raw-case verification

The wrapper changes the portfolio hook before constructing extension transitions and clears the original transition cache. It preserves baseline comparison rows before that change. Thus cached rows from the old portfolio rule do not silently survive into the new process.

On Q rounds the case remains a randomized experiment; the old frame is retained in the state while the inquiry is incomplete. When skill or installed practice requires ordinary F/T work, that work can continue to use the old ratified frame. On the fifth record, the new nominee replaces the old expression regardless of which is physically better. The separate constraint test remains candidate-assumed feasibility, not a correctness oracle. The wrapper consumes the complaint after completion, including a complaint from the final experimental case, exactly as the extension protocol specifies.

The independent checker was extended with those two explicit rule changes. It reconstructs ten representative transition rows across the two new arms from raw context/action/noise/ticket draws: incomplete inquiry with a correct incumbent, completion that can correct a reversed incumbent, misleading completion that can corrupt a correct incumbent, ordinary work by a volume incumbent, and training with retained incomplete inquiry. All successor supports match. The maximum transition and baseline-reward differences are each 2.78×10⁻¹⁷. The saved verification report records extension hashes and verifies preservation of the baseline files.

The distinction from baseline is literal. For a skilled adaptive state with a retained frame and pending complaint, inquiry now advances the counters; the baseline performs ordinary cases and leaves them unchanged. Conversely, the unchanged F/T boundary rows confirm that retaining a partial new inquiry does not automatically disable the incumbent's ordinary-service response.

The extra improvement/deterioration labels compare the old and proposed physical harm vectors at equal expected burden, before subsequent turnover may erase the new package. This is an analyst classification of a replacement event, not an input to institutional choice and not a count of improvements guaranteed to remain installed. Componentwise comparisons permit incomparable changes. The true X1 expression dominates the reversed and wrong-attribute responses in this particular outcome table; the two wrong-attribute responses need not dominate each other.

### The endpoint requires a precise label

The reused `physical_profile` and `metrics` functions evaluate the retained response **conditional on ordinary service**. They do not inspect which work portfolio the institution will perform next. A correct retained frame with a pending complaint is consequently counted as `plural_success` even though its next Q case is randomized and has expected harm .5 in each context, exceeding the .2 ceiling.

The extension endpoint must therefore be read as **the probability of possessing an enabled retained ordinary-service response that satisfies the proposed expected constraints**. It is not the probability that the actual Q-inclusive policy currently meets those constraints, nor that every prior or future period is safe. This is stronger than the usual caution about expected versus realized harm: the experimental portfolio itself has a different expected response profile. The frozen endpoint remains useful, but reports must retain the ordinary/inquiry distinction and the separately recorded inquiry harms.

### The mixed results are informative, not a universal improvement claim

With endogenous succession, reopening changes retained-response satisfaction from .55288825 to .54588364 and positive-skill probability from .67930889 to .66370897. Ratified-but-violating probability falls from .07270725 to .05610547, but frame presence also falls. That lower error-state probability cannot be interpreted entirely as successful correction; loss of records or skill also removes ratified frames from the count.

Under protected selection and retention, retained-response satisfaction rises from .85107159 to .89897459, while skill remains preserved. The extension can both correct wrong incumbents and corrupt correct ones. It increases inquiry work and its physical harms in both arms; the protected increase in response quality is not a dominance result over every service and harm measure.

This closes the baseline's missing *specified reopening transition*. It does not establish that unrestricted revisability always helps, that the reopening rule remains protected endogenously, or that every consequential error is discovered and corrected on time. The supplied grammar, fixed commitment menu and empirical response family remain the boundaries of the construction.
