# Causal diagnosis, complementary repairs, and transfer

5 October 2026 task date. AI-generated research under Ren's direction. These are conditional mathematical results and a computed extension of the unchanged nonfinancial model, not measured properties of all institutions.

## 1. A failure outcome does not identify the failed mechanism

Consider two versions of the [closure model](../closure-study/PROTOCOL.md):

- **A:** raw inquiry occurs but new evidence cannot enter the operative record; execution is available.
- **E:** evidence enters the record but cannot change the implemented routine.

Both start with routine and record zero. Couple their context changes, reports, turnover, appointments, and forgetting using the same random draws. Neither system changes its routine: in A the record is zero or absent, and in E execution is blocked. They therefore have identical adequacy, consequent turnover probabilities, installed practices, training, and skill on every coupled path. Their admitted records differ.

**Proposition.** The entire path distributions of `(context, routine, practice, skill)` and the inquiry, task, training, and turnover events are identical in A and E. Every estimator based solely on those histories has the same distribution under the two mechanisms, at every observation horizon. More data from these channels cannot distinguish them.

The coupling proves the claim by induction. This is stronger than equal average performance. It is relative to the specified observation channels: inspecting admitted records, admission events, or implementation decisions can break the equivalence. It does not mean the mechanisms are unknowable.

The computation checks the joint projected next-state/event distributions for all 48 related reachable-state pairs; the maximum numerical difference is zero. Restoring admission changes A to the baseline while leaving E blocked. Restoring execution does the reverse. Observationally equivalent systems can therefore require different remedies.

## 2. Testing components one at a time can miss a necessary combination

Let `A,E` indicate whether admission and execution are enabled. With all other original parameters fixed, the probability of never losing the specified skilled capacity over 200 periods is:

| Admission | Execution | Capacity retention through period 200 |
|---|---|---:|
| Blocked | Blocked | 0.0067218 |
| Enabled | Blocked | 0.0067218 |
| Blocked | Enabled | 0.0067218 |
| Enabled | Enabled | 0.0943692 |

Starting from both gates blocked, either isolated restoration has zero effect on this endpoint. The joint restoration adds 0.0876474, or 8.765 percentage points. These are enumerated model probabilities, not empirical estimates. Even the restored system remains vulnerable to eventual skill depletion; enabling these gates does not repair every mechanism.

The elementary smooth example `F(a,e)=F0+c a e`, with `c>0`, makes the optimization implication explicit: at `(0,0)` both partial derivatives vanish although the joint change to `(1,1)` improves F. With positive separate setup costs, either isolated change can even worsen net performance while the combination improves it. This is a local example of complementary conditions, not a proposed universal welfare function or an exact continuous parametrization of the finite study.

Consequently, **a local improvement signal need not point toward a viable coordinated change**. The theory needs experiments on combinations and feasible transition paths, as well as gradients. A zero marginal effect does not establish irrelevance when a complementary mechanism is missing.

This argument has limits. In the model, jointly enabling misleading evidence and execution can worsen retention. The same factorial interaction at report accuracy 0, .5, .95, and 1 is respectively −0.0066645, −0.0046477, +0.0876474, and +0.1430624. At .5 a useless report can erase the initially informative inherited routine; admission is not intrinsically beneficial. No universal monotonicity of openness or responsiveness follows.

Removing the assumed pathway from inadequate work to increased attrition makes capacity survival equal across all admission/execution interventions. Routine adequacy can still differ. A proposed test must therefore measure the outcome through which the hypothesized mechanism operates. Survival alone is not a sufficient diagnostic endpoint.

## 3. The time and history of restoration matter

In the no-entry model, zero skilled capacity is absorbing. Switching admission, execution, or training on at a later date cannot recreate a lost carrier: apprenticeship requires an existing carrier. For any restoration time t and later horizon H,

\[
\Pr(k_s>0\text{ for every }s\le t+H)
\le \Pr(k_s>0\text{ for every }s\le t).
\]

This follows by event inclusion; no independence assumption is needed. It is a restriction on these interventions, not on all conceivable reconstruction technologies. The earlier external-entry model supplies a distinct reconstruction mechanism.

After 100 periods with admission blocked, only 0.0977769 of systems retain capacity. Restoring all three gates then yields 0.0073560 retention through absolute period 300. The corresponding execution-blocked case has the same pre-restoration survival but 0.0073787 afterward: its preserved evidence now matters. Delayed restoration follows **200 additional periods** in both cases; these numbers must not be compared as equal-total-horizon treatment effects against intervention at time zero.

The distinction is practical: a proposed destination, a feasible route to it, and a mechanism that keeps it operating are different research objects. Recommending a final configuration does not establish that depleted institutions can reach it with their current means.

## 4. A precise cross-domain transfer test

The [earlier formal bridge](../closure-study/FORMAL.md) requires a state map and an error bound, not an analogy. Make the intervention requirement explicit. For each domain D, let:

- `s` be its adequately specified physical/institutional state;
- `φD(s)` be the proposed common state;
- `ιD(a)` be a physically implementable version of common intervention a;
- `KD^ιD(a)` be its actual transition law under that intervention;
- `K^a` be the proposed shared transition law.

Suppose, with error bounds in `[0,1]`, uniformly on the stated reachable region and interventions,

\[
\operatorname{TV}\!\left(
\phi_{D\#} K_D^{\iota_D(a)}(s,\cdot),
K^a(\phi_D(s),\cdot)\right)\le\epsilon_D.
\]

The symbol `φ#` means the distribution after mapping domain outcomes into the common state. Require preserved observations and action constraints, and include any event/constraint monitors whose probabilities are being transferred. Use the same abstract, possibly randomized history-dependent intervention policy in both systems; it may not consult hidden information excluded by the map.

**Conditional transfer bound.** With mapped initial-distribution error `εD,0`, the error in the probability of any mapped H-step path event is at most

\[
\delta_D(H)=1-(1-\epsilon_{D,0})(1-\epsilon_D)^H.
\]

Couple initial states with failure probability at most `εD,0`. While histories agree, choose the same policy action and couple next mapped states with disagreement probability at most `εD`. Multiplying conditional agreement bounds proves the result; no independent physical disturbances are required. A projected process need not itself be Markov if the bound holds for every underlying state, hence every conditional mixture given the mapped history.

Two mapped domains can differ on the same intervention's event probability by at most `δD1(H)+δD2(H)`, clipped at one. A **treatment-effect contrast** between interventions a and b has error at most `δD(a,H)+δD(b,H)` relative to the shared model, by the triangle inequality. Similar baseline performance or a similar effect direction does not supply these bounds.

This belongs to established causal-abstraction research, including [Rubenstein and colleagues (2017)](https://arxiv.org/abs/1707.00819), [Beckers and Halpern (2019)](https://ojs.aaai.org/index.php/AAAI/article/view/4117), and [Beckers, Eberhardt and Halpern (2020)](https://proceedings.mlr.press/v115/beckers20a.html). Our contribution here is specifying the requirement for this alignment programme and its intervention tests, not inventing causal abstraction or the coupling inequality.

The new institutional analysis estimates one bounded-domain intervention contrast. The previous microbial analysis tests prediction of next-cycle biomass. They do not estimate the uniform transition discrepancies above. Accordingly, there is now a testable definition of the transfer claim, but no validated equivalence between these two systems.

## 5. Existing ecological causal evidence and its boundary

[Sanchez and Gore (2013)](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001547) studied yeast populations with feedback between producer frequency and population density. At equilibrium, pure-producer and mixed populations had similar densities. After a one-time 32,000-fold dilution, all six pure populations survived and all six mixed populations became extinct. Under an abrupt increase in sustained dilution, one of six mixed populations survived; all six survived a two-step deterioration. These are the authors' published intervention results, not a new analysis of raw trajectories. They support the restricted claim that current output can conceal different capacities to withstand a specified change. They do not identify evidence admission, political legitimacy, or AI corrigibility as biological mechanisms, and cannot validate a shared institutional intervention kernel.

## 6. What this closes

The diagnostic gap is closed **within the supplied finite model**: distinct hidden failure mechanisms, their observational equivalence, discriminating interventions, complementary restoration, adverse information, and delayed restoration are now explicitly derived and checked. The cross-domain claim has a mathematical acceptance condition. Estimating it in real systems remains work requiring the appropriate data and interventions.

Reproduction: [protocol](CAUSAL-PROTOCOL.md), [calculation](causal-checks.py), [full results and hashes](causal-results.json), and [completed independent review](CAUSAL-REVIEW.md). The review reconstructed all 16 factorial arms and eight delayed endpoints through a separately implemented event model. A coupled collection of descriptive equations alone is not an identified causal theory.
