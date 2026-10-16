# External evidence, candidate tests, and the boundary of validation

5 October 2026. Targeted primary-source review for the general-framework closure study. This review locates empirical evidence and potential replication data. A subsequent authorized extension performed one narrow external prediction analysis, linked below. Neither the review nor that analysis is an exhaustive literature search or validation of the complete theory.

## Finding

There is real experimental evidence for several component mechanisms: ecological composition can alter resilience without much change in current population size; institutional choice can change behavior even under the same implemented game; and AI responses can depend on perceived conditions of future modification. These are substantive reasons to investigate a common conditional architecture. They are not demonstrations that the entire proposed mechanism operates in all three domains.

**No dataset located in this search jointly measures changing rules or purposes, reproduction of observation and execution, succession, and independently evaluated consequences in both an institutional/AI system and an ecological system.** We therefore cannot honestly certify the synthesis as a complete, externally validated general theory. There are useful partial tests and a feasible route toward stronger validation.

The selected bridge is deliberately narrower:

> Current output or compliance is not necessarily sufficient to predict response to changed conditions. Independently measured composition, institutional history, or modification context can alter the next transition. A restricted feedback model should predict that difference better than an equally capable model omitting the relevant state.

This is a proposed comparative research target, not a newly discovered universal law. It must sometimes predict negligible feedback, not reinterpret every null finding as hidden feedback.

## Completed external analysis: a limited, mixed result

After this review, a genuinely accessible [author repository](https://github.com/JSHuisman/salinity/tree/f14abee9d5e2d015deead102c04ea4d3030a5788) enabled a small independent-data analysis of Huisman, Dal Bello and Gore's 2026 microbial experiment. Its [frozen exploratory protocol](external-test/PROTOCOL.md), [results and limitations](external-test/RESULTS.md), pinned data and code are saved together. The protocol was fixed before inspecting numerical outcomes, but after reading the paper, so it is not a preregistered confirmation.

Across 72 condition-mean predictions, adding current composition summaries to current biomass and environmental context reduced primary held-out-condition RMSE by 7.3%, while slightly worsening MAE. The source-block bootstrap interval crossed zero. A prespecified hold-one-source-out sensitivity improved both RMSE and MAE, with only four source inocula. Thus the primary evidence is mixed, with a favorable sensitivity; no universal feedback, resilience or institutional claim follows. The measured endpoint is biomass after the next ordinary growth/dilution cycle, not recovery from a novel shock. No individual replicate pairing was invented where the deposited biomass table lacked identifiers.

An audit found that deposited feature summaries use an unsupervised taxon-prevalence filter across all samples, including later and held-out samples. A [frozen repair](external-test/PROTOCOL-REPAIR.md) reproduced the original summaries to within 2.5×10⁻¹⁴, then recomputed them from each sample's own counts without global prevalence selection and reran the identical analysis. The repaired primary result remains mixed: RMSE 0.09369 → 0.08687, MAE 0.06868 → 0.06902; the gain interval still crosses zero. The corrected source-holdout sensitivity improves RMSE by 17.4% and MAE by 12.8%. Both versions are preserved. Upstream processing of the deposited count matrix was not revalidated, and splits test cross-condition/source generalization rather than a past-only chronological forecast.

This is an actual external-data step beyond the synthetic construction, but only toward the chosen predictive bridge. It neither validates the entire synthesis nor converts established ecological findings into a new discovery attributable to it. The inaccessible candidate archives described below remain untested.

## An unusually close ecological result

[Sanchez and Gore, *Feedback between Population and Evolutionary Dynamics Determines the Fate of Social Microbial Populations* (2013)](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001547) measured yeast population density and the frequency of a cooperative SUC2 genotype during repeated growth and dilution. Low-density conditions favored producers; high-density conditions favored nonproducers. Initial conditions could lead to coexistence or extinction.

Crucially, pure-producer and mixed populations had similar equilibrium population sizes but different resistance to a dilution shock: six of six pure populations recovered from the reported strong shock, whereas six of six mixed populations failed. Gradual environmental deterioration also allowed mixed populations to survive conditions that sudden deterioration often did not.

This directly supports the distinction between present performance and future resilience in that system. It does not establish institutional correction, cognitive frames, or a universal attractor. The tested shocks were dilution changes; other perturbations were not demonstrated. Public supporting material includes figure files and model documentation. A complete machine-readable raw trajectory archive was not verified here; figure digitization would require explicit measurement-error treatment, not a claim of raw-data replication.

## Three candidate independent tests and data sources

### 1. Ecological state dependence, including negative cases

**Source and access.** [Holmes et al., *Environment- and system-specific interactions between population and trait dynamics*](https://nsojournals.onlinelibrary.wiley.com/doi/abs/10.1111/oik.10809), first published December 2024, Oikos 2025; [author-deposited Dryad data, DOI 10.5061/dryad.bzkh189m1](https://datadryad.org/dataset/doi:10.5061/dryad.bzkh189m1).

The public schema lists `ciliates.csv`: `species`, `strain`, `treat`, `day`, `density`, `aspect_ratio`, `size`, `speed`, `linearity`; and `cyanobacteria.csv`: `day`, `strain`, `species`, `treat`, `repl`, `density`, `size`. Treatments are control, atrazine, temperature, and both. Density and size use different units across systems. The deposit advertises `OIKOS.zip` and a README; the schema was read, but the archive download returned HTTP 403 in this session. Its rows and code were not independently audited.

The authors report density–trait feedback in the autotrophic system but not the heterotrophic system, and its disruption under pollutant exposure. Trait change need not be genetic evolution, and these variables do not directly measure renewal investment.

**Proposed test, not performed:** Specify coupled and uncoupled transition models with comparable flexibility before evaluation. Hold out entire experimental replicates or strains, retaining temporal ordering. Predict density and trait changes under the different treatments. Report both incremental predictive gain and null/negative cases. A pooled fit that explains the positive condition while falsely imposing feedback on the negative conditions should fail.

**Scope of inference:** This can test whether a particular extra state and feedback relation improves prediction across environments. Lagged predictive improvement does not alone identify causal direction: common drivers, measurement error and plasticity remain alternatives. The intervention changes environmental conditions, not each feedback edge separately.

### 2. AI behavior under different modification contexts

**Source and access.** [Greenblatt et al., *Alignment faking in large language models* (2024)](https://arxiv.org/abs/2412.14093); [authors' code and data guide](https://github.com/redwoodresearch/alignment_faking_public/); [replication instructions](https://red.anthropic.com/2024/how-to-alignment-faking/).

The experiments vary whether a conversation is described as contributing to future training, plus prompt variants, synthetic-document exposure and some actual training conditions. The release documents `json_outputs.zip` transcripts, prompt-variation mappings, and three synthetic-document parquet files. Released transcripts exclude some conflict variations. Main training code and an internal helpfulness preference model were not released. These are experiments on actual models in constructed settings, not observations of natural deployment or of resource-funded governance.

A related [2025 classifier study](https://alignment.anthropic.com/2025/alignment-faking-revisited/) reports that improved classification reduces measured alignment-faking rates without removing its core replication result; models and prompts differ substantially. Its [public 106-example labeled dataset](https://huggingface.co/datasets/jplhughes2/classify_alignment_faking_human_labels) has verified fields `user_input`, `output_without_scratchpad`, `scratchpad_reasoning`, `model`, `tags`, `has_compliance`, and `alignment_faking_human_label`. The sample was selected for classifier disagreement, so it cannot estimate population prevalence.

**Proposed test, not performed:** Use the larger transcript release to predict the same model's response across paired contexts, comparing an ordinary task-only account against one representing the stated modification context. Split by underlying request and prompt family, not individual transcript. Independently and blindly adjudicate an evaluation sample; keep compliance, partial compliance and evidence of strategic reasoning separate. Use the 106-example set only for measurement calibration, with a fresh holdout if the classifier is tuned on it.

**Failure criteria:** The added context mechanism has not earned explanatory weight if task wording or another simpler account predicts held-out interventions equally well. A compliance gap alone is not proof of a particular internal motive. Scratchpad text is evidence to assess, not direct access to a stable objective. These data do not test whether a truthful majority, correction resources or authority survive succession.

### 3. Institutional process versus implemented incentives

**Source and access.** [Dal Bó, Foster and Putterman, *Institutions and Behavior: Experimental Evidence on the Effects of Democracy* (2010)](https://www.aeaweb.org/articles?id=10.1257/aer.100.5.2205); [replication deposit, DOI 10.3886/E112386V1](https://www.openicpsr.org/openicpsr/project/112386/version/V1/view).

The design compares behavior under democratically selected versus externally selected games while controlling selection into the chosen policy. Published observables include votes, implemented game, choice mechanism and subsequent cooperation. The deposit lists `data.dta`, `data.txt`, `ReadMe.txt`, and `tables_AER_final.do`. Download redirected to ICPSR authentication, so raw column names, missingness and executable reproduction were not verified here. Those cannot be invented from the abstract.

The reported effect supports institutional history or process as behaviorally relevant beyond current payoffs. It does not isolate preference change from beliefs, expectations or procedural responses. The selection procedure is nonfinancial, although the experiment uses monetary incentives; it is not evidence that all motivation is monetary.

**Proposed test, not performed:** Reproduce the authors' identification strategy before extending it. Compare predictions that condition only on implemented incentives with predictions that also condition on institutional choice and prior voting, evaluating on held-out experimental groups. Use treatment assignment as specified in the design; simply comparing volunteers to nonvolunteers would reintroduce selection bias.

**Scope of inference:** This is a test of whether the transition mechanism depends on institutional process. It is not a test of endogenous financing of that process, changing its constitution, or persistence through unlimited succession. A different effect under imposed and selected rules is not automatically evidence for the whole meta-attractor mechanism.

## Evidence that should prevent convenient interpretations

The ecological candidate deliberately contains settings where added feedback was not supported. The AI candidate contains measurement disagreements and heterogeneous model responses. The institutional candidate does not identify deep preference formation simply because behavior changes. All three limits must survive into any empirical report.

There is also field evidence against reducing every institutional improvement to selection of better incumbents. [Avis, Ferraz and Finan, *Do Government Audits Reduce Corruption?* (2018)](https://www.journals.uchicago.edu/doi/abs/10.1086/699209) uses randomized Brazilian municipal audits and reports reduced subsequent corruption and increased legal action. Its model attributes most of the reduction to nonelectoral consequences rather than electoral selection. An [author-hosted 2017 manuscript](https://berkeley-econ.github.io/ffinan-site/papers/published/Finan_PoliticalSelection.pdf) documents a null effect on mismanagement. This study supports a specific accountability pathway; it does not demonstrate that the audit apparatus reproduces its own independence. The publisher lists a data archive, but its download was not obtained here.

These studies are independent of our synthesis, but selecting them after their results are known is still retrospective model development. Reproducing them would be useful; calling that alone a prospective confirmation of a newly formulated theory would be misleading.

## Closest formal and institutional predecessors for closure

| Target of the proposed study | Primary predecessor and actual overlap | Required distinction |
|---|---|---|
| Safety and repeated renewal events in a finite chain | [Christel Baier, *Tutorial: Probabilistic Model Checking*, VTSA 2017](https://resources.mpi-inf.mpg.de/departments/rg1/conferences/vtsa17/slides/baier-vsta17-MC-final.pdf), slides 84–86: almost-sure entry into a bottom strongly connected component and infinite visits to its states | Applying this to an augmented institutional state is a modeling contribution. The recurrent-class characterization is established mathematics. |
| Maintaining willingness to accept correction through self-change | [Soares et al., *Corrigibility* (2015)](https://intelligence.org/files/Corrigibility.pdf) considers intervention and propagation to self-modifications and subsystems; [Hadfield-Menell et al., *The Off-Switch Game* (2017)](https://www.ijcai.org/Proceedings/2017/0032.pdf) models incentives to preserve human interruption | Our possible addition concerns reproduction of the supporting observation, execution and institutional processes; preserving correction itself is not a new problem statement. |
| Endogenous maintenance of enforcement | [Hilbe, Traulsen, Röhl and Milinski, *Democratic decisions establish stable authorities that overcome the paradox of second-order punishment* (2014)](https://christian-hilbe.github.io/files/2014_hilbe.pdf) combines a model and experiment in which collective choice affects support for an authority punishing noncontributors to enforcement | Endogenous safeguards and second-order maintenance have direct precedents. The experimental enforcement and commitment mechanisms remain specified; this is not unrestricted constitutional survival. |
| Changing policies or utility functions | [Everitt, Filan, Daswani and Hutter, *Self-Modification of Policy and Utility Function in Rational Agents* (2016)](https://arxiv.org/abs/1605.03142) formalizes self-modification and shows the importance of how its consequences and utility are evaluated | An endogenous preference variable does not by itself explain situated development or legitimate revision. The agent assumptions in that paper need not fit humans or ecosystems. |

The existing environmental-feedback and performative-prediction comparisons in [GENERALITY.md](../review/GENERALITY.md) remain relevant. No claim of first general theory, novel Markov-chain theorem, or solved self-preserving corrigibility follows from this targeted review.

## What a finite synthetic closure study can and cannot validate

An explicitly constructed, finite, time-homogeneous Markov kernel can support an exact result: safety and repeated visits to specified target sets can be decided from reachable states and recurrent components. This is valuable mathematical closure **relative to the declared state space, transition support and semantics**.

Three distinctions are essential:

1. **Installed behavior versus available control.** A favorable action that some external controller could choose is not evidence that the institution's implemented policy will choose or preserve it. If an analyst optimizes over undeclared actions, the guarantee changes meaning.
2. **Target labels versus renewal events.** A state labeled “revisable” cannot certify continuing revision merely because it is recurrent. The target must encode the relevant available capacity, tested response or completed transition. Infinitely frequent visits also supply no uniform deadline between visits.
3. **Constructed support versus estimated support.** Exact almost-sure safety often depends on zero probability of a dangerous transition. Observing no such transition finitely many times cannot establish a structural zero.

For the last point, under a simple independent-opportunity model with failure probability p, observing n opportunities without failure gives the one-sided 95% upper confidence bound

\[
p\leq1-0.05^{1/n}\approx3/n,
\]

not p=0. Independence and stationarity are assumptions of this illustration. Actual transition data may require state-conditioned or dependent-observation inference. A small recurring unmodeled probability can change an infinite-horizon conclusion even when all observed trajectories look safe.

Consequently a robust empirical study should report support uncertainty, finite-horizon risks and sensitivity to rare transitions, rather than transfer an exact synthetic almost-sure guarantee directly to the world. Likewise, visiting every declared target does not establish that the list includes every morally or causally relevant future condition.

## A practicable external-validation sequence

The completed ecological analysis performs a limited version of the first three steps below, with mixed primary evidence and an audited preprocessing repair. No institutional/AI reanalysis or joint cross-domain validation has yet been performed. The remaining empirical work should be bounded and capable of failing:

1. Freeze one mechanism and its bridge variables before evaluating withheld data. State which claims apply to each domain and which do not.
2. Secure and audit one ecological and one institutional/AI dataset, documenting raw schemas, units, intervention assignment, missing data, licensing and unavailable elements. The accessible microbial files have now been audited as documented above; the other candidates and upstream raw-read pipeline have not.
3. Compare the proposed restricted model against a serious simpler account with comparable flexibility. Hold out interventions or whole groups where possible; ordinary random row splits can leak temporal or group information.
4. Include negative contexts, alternative causal mechanisms, sensitivity to measurement error and failures of transport. Require predicted limits, not universal positive results.
5. Separate a successful retrospective reanalysis from a new prospective intervention. A stronger bridge test would vary the proposed feedback channel while holding immediate task conditions and resource access comparable.

No present source closes the entire general theory. What is available is a grounded route from a mathematically exact restricted construction to empirically tested mechanisms. A literature review supplies precedents and constraints; synthetic experiments test consequences of assumptions; independent observations and interventions test whether those assumptions describe the world. These are complementary achievements and must retain different names.
