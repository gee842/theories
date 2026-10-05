# Mathematical learning: evidence, comparators and the claim boundary

6 October 2026. AI-authored evidence review for Ren's request to investigate how far the relationship between the theory and mathematics can be claimed. This is a supporting empirical/comparator strand for [Mathematics and generative grounding](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATHEMATICS-AND-GENERATIVITY.md), within the [governing derivation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md). It addresses **acquired prediction → reusable mathematical abstraction → warranted inference**. It is a literature and assumption review, not a new experiment, replication, systematic review or claim of priority.

## What the evidence permits

The evidence supports treating mathematical competence as a family of acquired, scaffolded capacities whose components can come apart. Making an exact match, retaining a cardinal value, extending a counting rule, manipulating mathematical notation, composing unfamiliar instructions, and supplying a proof are different achievements. A model that explains one should state which further capacities it assumes.

This gives the generative programme a concrete explanatory target. It does **not** independently confirm the programme's proposed root. Established developmental, cultural, Bayesian and neural accounts already explain parts of this progression. None of the studies reviewed below tests Ren's theory against a competing explanation. No distinctive empirical prediction follows yet from the general description “consequential distinctions are retained and composed.”

The evidence is compatible with a stronger, testable local programme: identify how a particular learner obtains representations and operations, what makes a representation fail under transfer, how the learner acquires a correction, and which actual supports allow the corrected procedure to remain usable. Mathematical warrant then requires a further account of what was proved or checked and why the represented interpretation is appropriate.

## Primary evidence inspected

The following are separate task families, not independent measurements of one latent quantity. Sample sizes and results are those in the cited primary reports; no pooled estimate is warranted. The summaries deliberately distinguish observed performance from a claim about every possible representation a participant could possess.

### E1. Exact matching can succeed without a reusable exact-number representation

Frank, Everett, Fedorenko and Gibson (2008), *Number as a cognitive technology: Evidence from Pirahã language and cognition*. Experiment 2 tested 14 adult Pirahã speakers, seven women and seven men; nine also completed the sequential hidden-container task. Participants matched objects under direct, uneven, orthogonal, concealed and sequential conditions. The authors report successful large exact matching when correspondence was accessible and worsening performance as quantities increased in orthogonal, hidden and sequential tasks. Training demonstrations clarified the matching procedure. These task contrasts establish neither an unlimited exact cardinal representation nor the impossibility of nonverbal exact matching. They identify a gap between arranging a correspondence and carrying a quantity across transformations. The small community sample, fixed task order and combined perceptual/memory demands limit the causal separation of language, memory and strategy. [Author-hosted paper, Experiment 2 and discussion, pp. 821–824](https://web.stanford.edu/~mcfrank/papers/old/FEFG-cognition.pdf).

### E2. Practical consequence sensitivity does not automatically produce flexible exact number

Spaepen, Coppola, Spelke, Carey and Goldin-Meadow (2011), *Number without a language model*. Four Nicaraguan adult homesigners, ages 20–29, were compared with four unschooled Spanish speakers and two deaf ASL users. Tasks covered money, numerical gestures, transformations and matching across modalities. Homesigners identified currency and relative value; three exceeded chance on every monetary task. On the untimed card task, their first responses were exact on 44% of trials with more than three objects. Across matching tasks, corresponding large-set accuracy was 33%, versus 91% and 94% for the comparison groups. Yet they usually preserved a supplied gesture after number-preserving transformations and changed it after number-changing transformations. This combination separates some sensitivity to exactness from a reliable procedure for generating or transporting cardinal values. The tiny, nonrandom groups and different language histories preclude assigning the whole effect to a single isolated mechanism. The authors explicitly leave nonlinguistic symbolic scaffolds possible. [Primary paper, participant description, Results and Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044352/).

### E3. The usable symbolic range can bound exact performance within one population

Pitt, Gibson and Piantadosi (2022), *Exact Number Concepts Are Limited to the Verbal Count Range*. Thirty Tsimane’ adults comprised 15 low counters and 15 high counters. After successful parallel-matching checks, participants matched orthogonally arranged arrays that remained visible. A Bayesian psychophysical model estimated the switch from exact-like to approximate responses. Low counters' estimated switch points fell at or below their highest verbal count in 14 of 15 cases. The association persisted in analyses controlling schooling and restricted to unschooled participants. This is stronger than comparing whole cultures, but it remains observational: groups differed in age and schooling, the switch point depends on a specified model, and symbolic knowledge was not randomly manipulated. The result supports a functional constraint on this task; it does not prove that spoken words are the only possible carrier of large exact cardinality or that all forms of mathematical thought require language. [Primary paper, Method, Results and Discussion](https://journals.sagepub.com/doi/10.1177/09567976211034502).

### E4. Productive operational knowledge and formal arithmetic expressions can dissociate

Schneider, Sullivan, Guo and Barner (2021), *What Counts? Sources of Knowledge in Children’s Acquisition of the Successor Function*. The final sample contained 136 cardinal-principle-knowing children, ages 3½–6, from 230 recruits after screening and exclusions. Tasks measured productive counting, the next number, an object-addition “Unit Task,” and verbal “+1” arithmetic. Mean performance was .66 on Unit, .67 on Next Number and .27 on Math Facts. Productive counting measures predicted Unit performance; children could succeed operationally while failing the corresponding arithmetic expression. The authors favour productive counting knowledge as a precursor, but this cross-sectional design does not identify the learning intervention that causes the transition. Task formats differed, and the study did not establish that successful children understood numerical infinity. Operational use, notation and an explicit universal principle therefore need separate measures. [Primary paper, Method, Results and limitations](https://academic.oup.com/chidev/article/92/4/e476/8254910).

### E5. A conventional learned system can acquire substantial compositional transfer

Lake and Baroni (2023), *Human-like systematic generalization through a meta-learning neural network*. Twenty-five adults received 14 pseudolanguage instruction/output examples and answered ten compositional queries; 80.7% of responses matched the intended algebraic interpretation. A transformer trained by meta-learning could closely model systematic responses and errors. Its instruction-learning preparation used 100,000 training episodes; behavioural error biases were incorporated into a variant's training targets. This is a substantive conventional comparator, not acquisition from unstructured interaction. The paper also reports 100% error on the SCAN length split and three COGS structural-generalization categories, despite strong lexical transfer. It distinguishes novel combinations within the learned task family from unrestricted productivity. The tasks test generated outputs, not mathematical proof or the physical origin of the training curriculum. [Primary paper, Behavioural results, benchmark results, Methods and Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620072/).

## Computational antecedent: the proposed bridge is already partly modelled

Piantadosi, Tenenbaum and Goodman (2012) implement numerical-concept learning as Bayesian inference over compositions of cognitive primitives. Their model supplies set operations, conditional logic, operations on an already ordered count list, recursion, a hypothesis grammar and statistical assumptions. It can learn a recursive enumeration procedure from noisy examples with frequencies informed by child-directed language. The supplied recursion operator is not itself a numerical successor function, so it would be unfair to dismiss the result as literally supplying the final learned procedure. Nonetheless, its representational resources make that procedure expressible before learning. The paper notes that transition timing depends on primitive choices and a free recursion-penalty parameter. This is already a serious model of learning reusable structure from simpler operations, with an explicit premise ledger. [Author-hosted manuscript, primitive table, learning model and discussion](https://web.stanford.edu/~ngoodman/papers/PTG-Number.pdf); [published bibliographic record](https://pubmed.ncbi.nlm.nih.gov/22284806/).

Rips, Asmuth and Bloomfield (2013) challenge whether that model adds expressive power, matches children's actual procedures, or establishes the unrestricted natural numbers rather than finite-range-compatible alternatives. These are objections from a primary theoretical response, not settled disproofs of statistical learning. Their relevance here is methodological: a successful implementation needs separate audits of its initial primitives, psychological fidelity and scope of generalization. [Response](https://www.sciencedirect.com/science/article/abs/pii/S0010027713000760).

Our inference from these comparators is that naming learning “generative” does not establish a new learning mechanism. A useful contribution would have to supply an input their models leave external, explain an additional boundary they do not predict, or connect acquisition to other independently specified mechanisms with fewer total assumptions. The wider foundation may make such an integration useful even when its local learner is a conventional algorithm.

## What must remain separate

The following distinctions are our analysis of the explanatory task, not additional reported experimental findings.

| Achievement | Evidence that would bear on it | What the achievement alone does not establish |
|---|---|---|
| Exact successful response | Correct answer on a specified trial | Retention, portability, an explicit cardinal concept or proof |
| Stable representation | Repeatable access across delay and interference | Correct application to every new operation |
| Reusable operation | Transfer to held-out instances and compositions | Unlimited extension beyond the tested range |
| Acquired rule | Change caused by identified learning inputs | Creation of every primitive used by the learner |
| Universal mathematical claim | A sound argument from explicitly quantified premises | Empirical fidelity of the interpretation |
| Retained method | Continued transmission and use | Truth, optimality or moral value |

There is no empirical contradiction between E1's accessible matching and E3's range bound on a different task. A physical pairing procedure may establish an exact relation between two displayed sets without maintaining a symbol for their cardinality. Equally, E2's recognition that a transformation changes number need not provide a procedure to calculate the resulting number. These distinctions prevent an explanatory schema from acquiring apparent universality by switching the target capacity mid-argument.

The phrase “learning which differences can be ignored” needs an explicit question and operation set. An abstraction may preserve parity and fail to preserve exact count; it may support addition and lose order; it may support a finite benchmark while failing longer compositions. The result can still be useful. Its mathematical status depends on the preservation actually claimed.

Nor should mathematics be identified with prediction alone. A learner can investigate an invented formal structure by stipulating rules, posing consequences and checking derivations, without claiming that its objects describe an observed physical process. The material formation of that activity remains an explanatory question; its internal validity is assessed relative to the stipulated formal setting.

## Does this theory make a distinctive prediction yet?

**No distinctive prediction is established by the present mathematics extension.** Its current components admit conventional explanations:

| Proposed generative description | Established alternative or comparator | What would add explanatory content |
|---|---|---|
| A failed prediction leads to a richer representation | Hypothesis testing, active learning and ordinary feedback correction | Derive the evidence/update machinery instead of supplying it, or predict a new boundary with it |
| Reuse compresses experience into composable operations | Bayesian program learning and compositional meta-learning | Predict which representation emerges under matched data and resources, including failures |
| Symbols preserve distinctions across delay and transfer | Cultural cognitive tools and developmental symbol learning | Identify formation, acquisition and maintenance of the specific symbolic interface |
| More costly representations may be inaccessible | Bounded computation and ordinary resource constraints | Derive and independently measure the actual cost and availability law |
| Reliable checking supports mathematical practice | Standard logic, formal verification and error correction | Join the actual acquired representation to a sound checker with interpreted premises |

These are not reasons to abandon the framework. They locate its potential contribution accurately: a connected account of the formation, support, use and revision of mathematical practices, with exact interfaces and explicit failure modes. That is a substantive research aim. It is not yet an empirically identified alternative to the mechanisms above.

The theory should not claim that mathematics evolves toward truth merely because it is useful, reproducible or retained. Those predicates are compatible with a mistaken extrapolation that happens to work on the encountered cases. Conversely, the destruction of a proof token need not invalidate the theorem. Formation, application, retention and warrant have different truth conditions.

## A discriminating next study

The immediate bridge can be made concrete without pretending to derive all mathematics. The following is a proposed design, not completed work.

1. **Name the target capacity.** A finite learner must acquire a representation of event histories that correctly predicts a specified family of continuations, retain it, and revise it after a demonstrated composition failure. Initially distinguish acquisition of a representation from acquisition of the procedures that update or check it.
2. **Declare what is supplied.** Record event identities, observation calibration, candidate representation language, available update operations, interpretation of success, costs, memory capacity, initial state and access to diagnostic continuations. A generated curriculum is still a supplied input unless its formation is separately explained.
3. **Require a genuine failure witness.** Histories initially treated alike must admit an available continuation producing different relevant outcomes. Repeating easy examples or merely adding more observations need not expose the lost distinction. Measure whether the learner finds and uses the witness.
4. **Separate four outcomes.** Score operational prediction, representation revision, retention/transmission and validity of any certificate separately. Held-out accuracy assesses sampled transfer; a proof or exhaustive finite audit has a different scope. A correct learned rule can be unaffordable to run; an inexpensive false rule can survive.
5. **Use competitive controls.** Compare a fixed abstraction, an equal-budget memorizer, a conventional active state-learning/refinement algorithm and a compositional learner with matched observations and training opportunity. An oracle may supply an upper bound but should not be the sole comparator. Charge all models for external evidence and storage on the same declared account.
6. **Intervene on the proposed mechanism.** Independently vary access to distinguishing continuations, cost of refinement, fidelity of stored labels, and the availability of a successor reader. Observe predicted failures even when training performance or survival is unchanged. Test restored operation after repairing the exact missing interface.
7. **Make model comparison decisive.** Specify a quantitative local law and its predictions before viewing results. If a conventional learner matches the output and support history with equal or fewer assumptions, accept local equivalence. If the proposed mechanism predicts a measured threshold or transfer pattern that the matched comparator misses, state that limited improvement. Neither outcome completes the root-to-mathematics derivation.

The likely initial contribution is a conditional construction with accountable inherited supports. To call it a psychological explanation would require evidence that people use the identified mechanism, not merely that the program produces similar answers. To call it an explanation of mathematical warrant would additionally require a sound checking relation and an account of how the actual record is interpreted by it.

## Claim ceiling and unresolved bridge

**Supported as an empirical research direction:** operational distinctions, usable symbols, compositional rules and formal expressions have different acquisition conditions; they can be studied within a generative account of formation and revision.

**Supported as a comparative requirement:** the account must compete with existing learning mechanisms and preserve their successes and counterexamples. The observational human studies do not isolate a single necessary carrier of all mathematical concepts. The computational studies establish conditional capabilities under supplied learning architectures and curricula.

**Not established:** that consequences alone generate exact number; that the theory uniquely predicts human abstraction; that mathematical truth is survival; that finite learning fixes every intended infinite interpretation; that all mathematics is direct abstraction from observed reality; or that the mathematics extension derives the foundations of logic, arithmetic or value without additional premises.

The next unresolved connection is **an actually formed learner acquiring and revising a reusable representation, then transmitting an interpreted record to a warranted checking procedure**. The open issue is whether this can reduce supplied premises relative to the conventional comparators while preserving the distinction between a useful finite rule, a justified general claim and its physical realization. This branch supports the ongoing path from learning to reasons and wisdom; it does not replace that path or announce completion of the unified foundation.

## Read and verification boundary

Inspected repository orientation: `README.md`, `_process/BRIEF.md`, the mathematics exploration, and relevant learning/abstraction entries in `RESEARCH.md`. Inspected primary source methods/results or model sections at the links above. E1 was checked against the author-hosted paper's task description; E2–E5 against primary full-text sections. The computational critique was checked in its primary abstract and publisher excerpt, not a full replication of its argument. External content is paraphrased and linked; no original source bytes were imported or replaced. This note introduces no new scientific computations and makes no claim of having rerun the cited analyses.
