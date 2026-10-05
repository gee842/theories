# Assumption ledger: which universality claims survive removal of premises?

5 October 2026. Read-only audit of F03, F14–F28 and the inherited U register. No previous artifact, code, input, or result was modified; no new simulation was run.

**Finding.** The current mathematical results remain valid under their stated premises. Several premises can be weakened or replaced by a more general interface, but removing every substantive restriction makes the intended conclusions false. There is a useful universal-within-class theory here: accounting at every payment prefix, limits from indistinguishable observations, and preservation under controlled refinement. There is not yet a proof that every intended worldly process belongs to one measured class, or that these necessary constraints jointly suffice for correction. F07 already refutes the latter inference.

“An assumption is essential” below means removing it invalidates the general guarantee: a counterexample then exists. It does **not** mean every individual case violating it fails, or that it is the weakest possible assumption.

## 1. Do not treat all premises alike

| Type | Examples in this record | What can justify or change it |
|---|---|---|
| Definition / mathematical typing | State/action/kernel interface; total funds `N=b+t`; chosen protected predicate; distinction among formal, semantic and empirical completeness. | Declare its meaning and check consistency. A definition does not establish that its referent exists or that it predicts outcomes. |
| Mathematical premise | Equal action-conditioned successor sets; equal observation channels; a uniform shutdown hazard; bounded cumulative credits. | Prove it from a more primitive model, check a finite specification exhaustively, or replace it with a weaker premise and prove a different conclusion. Derivation relocates premises; it does not eliminate all of them. |
| Mechanism / measurement assumption | Repair efficacy, sensor likelihoods, account access, payment chronology, environmental process, relationship between stock and protected function. | Independent calibration, interventions, institutional records and implementation checks. In an empirical application these are fallible claims, not truths supplied by notation. |
| Scope / evaluation restriction | Horizon, available policy class, admitted initial states, loss coordinates, query family, memory/computation budget. | State it before evaluation. Extending scope is a new theorem or test; changing the objective changes the question. |
| Normative commitment | Which people and functions deserve protection; tolerable burden; legitimate revision; N01. | Explicit substantive ethical and political argument. Choosing a number in an optimizer demonstrates consequences of that choice, not its legitimacy. |

The same sentence can carry two roles: a specified sensor kernel is a mathematical input in the simulator and an empirical hypothesis if asserted about a real sensor. The code is evidence about the first role; calibration is needed for the second.

## 1a. State the main proof target before trying to remove assumptions

A substantive universal characterization would have the form

`For every M in an independently declared class 𝓜 and every admitted initial state/information state z: G(M,z) iff C(M,z).`

Here `G` must specify the property to be explained, rather than slide between three different targets:

- **Ongoing operation:** an executable policy keeps a declared operating predicate true at every future time, under a stated disturbance/probability criterion. In robust form: `∃π∈Π_real ∀ω∈Traj(M,z,π) ∀t: Operating(ω_t)`.
- **Recurring novelty:** in addition to operation, genuinely new declared achievements occur arbitrarily late. “New” needs an explicit history-relative criterion; repeatedly alternating two states is continued change but need not be novelty. An indefinitely operating static machine establishes the first property and refutes any automatic inference to the second.
- **Plural-agent protected capability:** continued operation also preserves specified persons' functional opportunities, refusal/revision rights or other protected relations. Which people, which capabilities, and what protection standard must be stated. Mere continued operation by a coercive institution does not establish this property.

The policy quantifier, horizon and risk criterion also matter: one installed policy, existence of an ideal policy and existence of a physically affordable policy are different; positive survival probability, almost-sure survival and safety on every allowed disturbance path are different. The H4 access study solves finite expected objectives. It does not establish any of these three infinite targets.

`C` should use independently specified dynamics, information, mechanisms and measurable conditions, or provide a nontrivial effective characterization of the specified model. Defining C as “all conditions necessary and sufficient for G” makes the biconditional empty. A greatest-fixed-point winning-region computation for a fully specified finite safety game is a legitimate effective characterization: it derives policy existence from the transition/action/observation table. That is established control/game theory; its empirical application still requires the table and the protected predicate to be appropriate.

The record's stock, payment and discrimination inequalities are mostly candidates for parts of C. They have not been proved jointly sufficient for G. F07 already gives an explicit failure of sufficiency even in a finite diagnostic subproblem. No proof here identifies one C that characterizes ongoing operation, recurring novelty and plural-agent protection simultaneously across all intended domains.

### The finite-to-infinite quantifier gap

`For every finite H there exists a policy π_H surviving H steps` does not generally imply `there exists one policy π surviving every H`.

**Countermodel.** At the initial state choose any positive integer N; no infinite choice is allowed. That action enters a deterministic countdown with exactly N safe future steps, followed by permanent failure. For every H choose N≥H, so a sufficiently long-lived policy exists for each finite horizon. Every single allowed initial choice nevertheless has finite life. A randomized choice supported on finite integers also fails eventually with probability one, even if a heavy tail gives infinite expected life. This counterexample is about continuation itself, with no financial mechanism required.

Finite branching/compactness and compatible closed safety constraints can supply the missing argument—for example a finitely branching tree of arbitrarily long safe strategy prefixes can have an infinite branch. They must be checked; they cannot be silently presumed from repeated finite optimization. Nor does infinite safety automatically deliver recurring novelty, fairness, or another liveness property. The current all-finite-H pooling theorem says the two systems preserve each declared finite operational problem; it does not itself assert either system survives every horizon or has an infinite viable controller. This is a standard quantifier/compactness issue, not a novelty claim.

## 2. Local F ledger

| IDs | Actual status | Load-bearing premises and scope | What removing them changes |
|---|---|---|---|
| **F03** | Finite safety-preservation theorem. | Every allowed action has matching projected successors, observation histories, availability and protected labels; a common implementable controller class; matched initial information. | Removing any of these generic guarantees can break safety transport. Exact stochastic probabilities additionally require matching pushed-forward probabilities, not just support. See §4. |
| **F14** | Existential counterexample, exactly calculated. | H2 stock2, prior1, readiness0, barred treasury, total5, cash0/1; inherited production/damage/repair chronology. | `.612` versus `0` is specific to this kernel. The general conclusion is only that equal totals and equal first menus **need not** imply equal future correction. One valid witness suffices for that negative claim; no universal claim that every split matters was made. |
| **F15** | Finite exact computational result. | H4 registered grid, seven directions, tie rule and exact kernel. | `24/63`, `15/63`, `0/63` are counts on that grid. They are neither empirical prevalence nor full-frontier equality. |
| **F16** | General conditional normalization/refinement theorem. | Free timely lossless access; round bill≤cash cap; account-neutral mechanisms, observations and criteria; observed balances; executable virtual-ledger policy. | Fees, delay, lost overflow, account-specific information/outcomes or controller restrictions defeat the general conclusion. Not every listed implementation detail is intrinsically necessary: a different transfer schedule can replace the once-per-round/cap condition. |
| **F17–F18** | Exact sufficient descriptions and model-expansion counterexample. | Same operational query; permanently barred, immediate or known delayed access; stock/readiness/posterior retained. | Cash alone suffices only while treasury cannot affect any queried future. Admission of later access makes treasury relevant. This is model-relative sufficiency, not a model of how a new institution is discovered. |
| **F19** | Policy-set inclusion theorem. | More access includes executable emulation of every old policy at unchanged costs/information/evaluation. | Forced spending, signaling, fees or altered production can destroy inclusion. Even when inclusion holds, every component of one selected vector need not improve, and an installed controller may act worse. |
| **F20** | Audit of selected policies. | All 1,134 registered optima; specified tie rule. | Establishes zero paid tests in those selections, not strict diagnostic dominance. F21 is an explicit counterexample to that stronger reading. |
| **F21–F23** | Exploratory exact decision calculation. | H1 stock1, ready1, cash6, prior1/2, original physical technology; new expense/burden ceilings or probe; prescribed sensor comparison. | Under common ceilings, best no-test failure `.36` versus test `.085`; actual expenses `.6` versus `4.5` differ. Sensor comparison F22 separately holds expected expense and repair frequency fixed. These are not derived ethical criteria or held-out transfer. |
| **F24** | Definition/source-status distinction. | Registered formal items, source semantics and witness/interface contracts. | Graph reachability does not establish empirical interpretation. Some finite/encodable representation witnesses are constructed; a generic theorem that takes a semantic witness does not construct that missing witness. No fresh full Lean build was performed. |
| **F25–F26** | Countermodels and general projection construction. | Same general schema permits separately supplied beneficial/ineffective/harmful dynamics; carriers can be appended to any plant kernel. | These refute “the schema/carriers alone select the dynamics.” They do not refute every possible extra dynamical law or every fundamental constraint theory. |
| **F27** | Logical counterexample to one implication. | Two distinguishable states, each with only a self-loop (or terminal semantics). | Distinguishability does not entail realizable strict change. An axiom of global inexhaustibility excludes this model by adding content; it is not deduced from distinction. Local closure does not prove cosmic exhaustion. |
| **F28** | Evidential assessment, not a physical theorem. | Current record of conditional results, supplied mechanisms, and unrun independently calibrated transport. | New evidence can change this assessment. It is not an impossibility theorem against ever achieving unification. |

## 3. Inherited ledger, retaining exact claim IDs

| IDs | Kind and essential content | Removal test / boundary |
|---|---|---|
| **U01, U04, U16** | Accounting and necessary affordability/timing constraints for independently identified stocks, receipts, costs, floors, deadlines and access. | A payment due now cannot be paid from tomorrow's receipt without credit. Conversely, admitted borrowing/substitution changes the constraint. Observing survival and defining its “support” afterward would be circular. Passing the bound does not prove the procedure works. |
| **U02** | Exact identification limit in a compatible pure-selection model class: common positive abundance scaling with matching rate shift preserves shares. | A fixed known total or specified density-dependent law can remove the ambiguity. Shares alone cannot distinguish total growth from total decline across the admitted class. This does not prove every selection process destroys support. |
| **U03, U06–U09** | Conditional dynamical results for specified maintenance, production, transmission and appropriation equations. | Alternative support production, different imitation/inheritance laws or enforcement can alter collapse, invasion and equilibria. The displayed thresholds cannot be retained after deleting the equations from which they were derived. Stable equilibria do not guarantee safe reachability. |
| **U05** | Finite partial-observation safety recursion and incompatible-action impossibility. | With the same observation and disjoint required actions there is no robust choice. Revealing the hidden condition or adding a common safe response changes the conclusion. Common safe first actions alone do not guarantee future safety. |
| **U10** | Exact maximum-deficit reserve for a declared delayed transition. | Retaining the predecessor until its replacement matures can remove the particular deficit, while adding overlap costs. Maturation reliability, demand and payment schedule must still be checked. No universal claim that slower adoption is better. |
| **U11** | Occupancy-time identity: cohort mass×duration, summed over completed cohorts. | If some cohorts never complete, are cancelled, or have different durations, the stated `L(1−ε)` expression changes; the integral identity with the actual occupancy remains. It does not supply financing or prove minimal duplicate service. |
| **U12–U14** | Supplied two-frame dynamics, local stability and protected-introduction thresholds. | Changing the frame-loss, uptake or origination law changes the attractors. Shared benefit alone does not force learning. The equality case of a linear stability threshold needs nonlinear analysis. An introduction rate is not automatically a cash expense or legitimate authority. |
| **U15** | Fresh-confirmation error bound under independent valid sampling, fixed groups and allocated attempt error. | Reusing nomination data or selecting on confirmation outcomes can invalidate the bound. A per-episode guarantee does not imply a fixed error cap across unlimited episodes. |
| **U17–U19** | Bellman option value, historical/predictive/decision distinctions, and inference from the full known disclosure protocol. | Readiness can lack value if no future useful question occurs; passive evidence can remove a test need; silence ceases to mean the same thing when its generating protocol changes. Free memory and fixed losses are inputs. Historical truth alone never fixes current decision value. |
| **U20–U21** | Model-relative sufficiency and support preservation by ordinary fixed-family Bayesian updating. | Two ordered histories with the same count predict `.44835` versus `.05165` in the enlarged family. Adding hypotheses or a discovery mechanism is not ordinary updating of a zero-prior finite atom. These claims do not require saving every raw record. |
| **U22** | Total-variation/data-processing bound for the complete allowed observation law. | A new informative cue invalidates a claimed equality of observation laws; without new information, postprocessing cannot produce the missing distinction. Exact general form is in §5. |
| **U23** | Expected-loss identity and preservation threshold for a fixed workflow, question-arrival distribution and costs. | Different future questions, information costs, candidate efficacy or branch budgets change the result. Averaging factors separately can be wrong when their worldwise variation is correlated. |
| **U24** | Survival bound given uniform conditional shutdown risk in each L-round block; absorbing interpretation requires no restart. | If hazards are summable, e.g. independent period hazards `2^(−t−1)`, survival forever has positive probability. If restart is available, first shutdown need not be permanent elimination. Positive uncapped mean income alone does not exclude ruin. |
| **U25** | Telescoping bound on total credits from bounded positive cumulative improvement. | A score alternating `0,1,0,1,…` is bounded but has unlimited positive increments; paying each rise defeats the bounded-credit conclusion if monotonicity/bounded cumulative gain is dropped. Royalties are a different funding rule. |
| **U26** | KL discrimination lower bound for full transcript under the same policy, with a valid per-test conditional information bound. | A perfect passive signal supplies information omitted by a test-only account. Two `.9` tests satisfy the coarse necessary count but reach only `.85` randomized power at size `.05`; the target `.9` is still impossible. Necessary information is not sufficient control. |
| **U27** | Exact cash-dip integration for its specified post-repair ODE and cap regime. | Different recovery dynamics or intervening cap losses alter the formula. Mature positive surplus does not ensure the early bills can be paid; all earlier repair costs remain separate. |
| **U28** | Nonnegative burden sum with each inquiry burden≥fixed `h0>0`. | Burdens `2^(−t)` permit infinitely many inquiries and finite total burden; discounting changes the criterion. The lower bound does not select which burdens are morally acceptable. |
| **S01–S06, H01–H05** | Synthetic constructed results versus still-open empirical mechanism hypotheses. | Programmed gates, finite grammars, known efficacy, fixed purposes and supplied funding/recognition rules are not discovered universal institutional laws. Held-out synthetic samples test the supplied generator. |
| **P01, N01** | Operational capacity-profile definition; explicit protection of shared agency and legitimate revision. | Persistent coercion and inventive exploitation satisfy many viability/generativity descriptions while violating the commitment. Removing the commitment does not leave an equation that uniquely restores it. |

This audit has not rerun or independently reproved every U theorem. It carries forward the frozen claim register's status and the earlier targeted mathematical checks, while giving explicit removal tests for the attempted universalization.

## 4. Concrete premise-removal countermodels

### F03: what makes safety transport work

1. **Successors.** Keep the observation and safe/failure labels identical. One model's only action goes from a safe state to safe forever; the other's goes to failure. Removing transition correspondence breaks transport immediately.
2. **Observations.** Both models first branch from a known safe start to hidden states `a` or `b`. Action A is safe only at `a`; B only at `b`. Dynamics, state names and protected labels are identical. In one model the next observation reveals `a/b`; in the other it is constant. The former has a two-step safe policy; the latter does not. This isolates observation correspondence without changing the initial information set.
3. **Action realization.** Keep potential repair dynamics unchanged but deny permission to execute repair in one implementation. A safe abstract instruction is then not an executable concrete policy.
4. **Protected labels.** With identical static dynamics, call the initial state protected in one specification and prohibited in the other. Safety differs because the question differs. An ethical predicate cannot be silently discarded as “just a label.”
5. **Probabilities.** Failure probabilities `.01` and `.99` have the same support. The support theorem preserves robust possibility claims, not these probabilities.

Some hypotheses can be relaxed. Global surjectivity can be restricted to the reachable image. Overapproximating concrete successors can give one-way controller guarantees (F04), not the original two-way equivalence. Infinite settings can admit related results with their appropriate measurability/existence conditions; this ledger does not promote the finite proof into an unrestricted infinite-horizon theorem. Extra observations can be ignored for one-way emulation, but losing them can destroy equivalence.

### F16: total wealth is not always spendable capacity

- **Fee:** total1, repair cost1, transfer fee1. `(cash,treasury)=(1,0)` can repair; `(0,1)` cannot.
- **Delay:** cash0 and cash3 at total5, one round left, stock1 and known fault. Next-round unlock is too late: minimum collapse `.8` versus `0`.
- **One normalization with a small cap:** cap1, total2, two consecutive mandatory bills1, no intervening transfer. Total covers the bill sum but the prescribed payment interface cannot pay both. Repeated free transfers would remove this particular obstruction; the general premise is timely executable liquidity, not specifically cap8.
- **Account-specific query:** “retain one unit in treasury” distinguishes `(1,0)` and `(0,1)` even if all production outcomes agree.
- **Account information:** if split is correlated with fault, discarding it without updating the retained posterior erases useful evidence.
- **A fixed controller:** a controller that needlessly spends any available cash can do worse after automatic normalization. Policy-set emulation, rather than the assertion that every controller improves, is required.

Lossless pooling can be generalized to multiple freely connected accounts with adequate transfer/payment scheduling. If fees, interest or restrictions are retained as state and costs, a richer model can remain exact, but the specific quotient to one scalar total generally cannot.

## 5. Existing unconditional results *inside explicit mathematical classes*

No application is assumption-free. The useful distinction is that these conclusions need no particular repair technology, evolutionary story or sensor accuracy once their elementary objects and interfaces are fixed.

**Pathwise cash-prefix identity (U01/U16/U27).** For a declared realized sequence of bills `c₁,…,c_m`, let `r_j` be resources actually made spendable after bill `j−1` and before bill `j`; include admissible credit as a receipt and its repayment as a later bill. With initial cash `b`, no hidden source and no overdraft,

`balance after bill k = b + Σ(j≤k) r_j − Σ(j≤k) c_j`.

Consequently all bills in that fixed sequence are financially feasible iff

`b ≥ max(0, max_k [Σ(j≤k)c_j − Σ(j≤k)r_j])`.

This follows by telescoping and checking each prefix. It is necessary and sufficient for the **financial sequence**, not for successful diagnosis, a legal action, protected production or a physically implementable policy. If the receipt/bill path depends on initial cash or policy, the identity holds on each induced path; one may not hold its future receipts fixed while changing initial cash and then claim a globally optimized reserve. With several nonfungible accounts it applies to the appropriate account/transfer ledger, not an unjustified scalar sum.

**Indistinguishability / data processing (U22).** Let `P₀,P₁` be the laws of the entire information available before a decision. A common randomized decision is represented by `g(d)∈[0,1]`, with private randomization independent of the world. Then

`|E₁g(D) − E₀g(D)| ≤ TV(P₁,P₀)`.

In particular equal laws imply equal decision probabilities. This follows directly from the variational definition of total variation (or integrating threshold events of `g`). It does not require iid observations or a particular likelihood. It does require the **complete** interface, including informative timing, history, silence and visible actions. Acquiring a new observation changes that interface. Indistinguishability forbids reliable discrimination, not safe action when the same action works in both worlds.

**Controlled preservation (F03/F16).** A verified transition/observation/action/predicate contract transports the corresponding finite safety problem. This is a mathematical universal statement over all members satisfying the contract, with an inductive proof. The contract is local and stronger than equality of final optimum values: it can be checked without presupposing those final values. For a real application it still needs a measurement bridge. This sits within established abstraction/refinement theory; for example [Reissig, Weber and Rungger](https://arxiv.org/abs/1503.03715) study conditions enabling implementation of abstract controllers. No claim of a new general control theorem is warranted here.

**Unrestricted transformation obstruction.** For any nonconstant property P on a class containing both a P-model and a non-P-model, invariance under *all replacements* is false. Replacing the first by the second proves it. Thus a meaningful invariant must name its transformation class. A universal sentence such as “every model has the same representation signature” can survive broader transformations, but says less about which protected futures are possible.

## 6. Strongest useful next conjecture without a definitional circle

The empirical conjecture should be **prospective closure and compositional transport of a fixed measured interface**, not “systems that preserve correction preserve correction.”

Freeze an independently described application class and a candidate state/interface before integrated outcomes: for example specified bounded task-processing devices with declared payment/restart interfaces, queues, deadlines and fault processes. Do not define class membership by successful prediction. Declare which measured quantities are retained, which are omitted, the intervention menu, physically affordable controllers, horizon H and protected outcomes. Independently calibrate local transition/observation/payment laws, using trials separate from the integrated recovery runs. Estimate within-fiber differences across deliberately varied omitted histories, backlogs and pending work. These are measurable hypotheses, not an assumption that the final attainable sets are already equal.

**Candidate empirical claim:** throughout the registered class, the frozen retained state closes the local controlled dynamics within a prespecified error δ, and composition of those calibrated local mechanisms predicts held-out integrated recovery under the declared policies within the resulting bound. A disagreement from a omitted queue/deadline distinction rejects that registered abstraction. A repaired state is a new hypothesis requiring untouched evaluation.

One transparent mathematical guarantee is available if the local contract actually holds. Suppose the joint kernel of next retained state, observation and all outcome-relevant labels differs by TV at most δ at every matched reachable state/action; actions and their execution match; initial states/laws can be coupled with mismatch probability δ₀. Couple matched transitions maximally at each round and use the same observation policy and private random seed. Then the chance of any mismatch by H is at most

`ε_H = 1 − (1−δ₀)(1−δ)^H ≤ δ₀ + Hδ`.

For any declared trace score between0 and1, including a failure event, the difference in expected score is at most `ε_H`. The same bound transfers optimum values when every policy has its matched executable counterpart. The proof is simply that identical histories choose identical actions and retain probability at least `1−δ` of matching one more step; a bounded score differs only on a mismatched trace. For δ=δ₀=0 this reduces to exact preservation. Unbounded losses need additional moment or boundedness conditions, not this statement unchanged.

This implication is elementary controlled coupling/simulation mathematics, **not a newly discovered universal physical law**. The new scientific content would be that independently measured mechanisms and one fixed interface meet its premises across substantively different targets, with useful small bounds and reduced calibration burden. Finite calibration cannot prove a uniform claim over infinitely many hidden histories; restrict to a checkable finite class or give justified statistical/regularity bounds, then retain held-out challenges. Mere average one-step fit does not establish the required uniform bound.

Compare with a serious domain control model given the same calibration information. Matching its performance with comparable assumptions supports useful organization; predicting across targets with fewer independent mechanisms would support stronger unification. The proposed two-gate product law in F11 is also testable only with independently justified modularity and no alternative recovery route; present direct repair violates the strict route assumption. Banning that route merely to force factorization would not establish a law of correction.

## 7. Exact reference scope

- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/outputs/research-record.md` — F03, F14–F28, inherited map and evidence boundaries.
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/outputs/access-proof.md` — normalization assumptions, coupling, boundary countermodels, sufficient descriptions, access inclusion.
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/access-study/model.py` — actual kernel, costs, chronology, normalization, observations, outcomes and tie rule.
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/reference-snapshots/CLAIMS.md` — frozen U01–U28, S01–S06, H01–H05, P01, N01; this snapshot is authoritative for the inherited audit.
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/research/formal-core.md` — exact F03 statement and stochastic counterpart.
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/research/prior-results.md` — earlier independent elementary calculations and transformation distinctions.
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/fundamental-audit/formal-audit.md` — independent formal-source audit of F24–F27. This ledger relies on that source audit; it does not claim another Lean repository audit or build.

The cash-prefix and indistinguishability proofs above re-express established results. The bounded-error coupling argument is supplied as a candidate next test contract, not a completed new experimental result, a novelty claim, or evidence that the target class already satisfies it.
