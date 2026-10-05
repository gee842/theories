# Prior art: inheriting constructions and the capacity to construct

Prepared 5 October 2026 for the bounded constructive-succession study. This memo reads five targeted primary sources and distinguishes their findings from design implications. It does not certify the study's implementation or results.

The relevant prior finding is conditional: **inherited structure can shorten the work needed to construct another solution, while the same inheritance can consume resources or channel search away from better solutions**. Neither products nor reusable means are inherently generative. Their effect depends on what a successor can recover, recombine, test, and afford in the later task.

## Five primary anchors

### 1. Learned libraries change feasible synthesis

Kevin Ellis and colleagues, *DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning*, PLDI 2021. [Author PDF](https://people.csail.mit.edu/asolar/papers/EllisWNSMHCST21.pdf), [DOI](https://doi.org/10.1145/3453483.3454080). Read §§2–2.3, 5–6.

DreamCoder alternates solving tasks, extracting reusable abstractions from solved programs, and training a search policy using replay and sampled programs. The library reduces search depth; the policy reduces search breadth. Evaluation includes held-out synthesis tasks and ablations. Crucially, the input language must already express the training solutions, and easier and harder tasks must share useful structure. Learned functions therefore alter practical accessibility under bounded search without establishing new underlying expressibility. The authors explicitly leave fuller acquisition of data types, idioms, and design patterns open. This is direct prior art for carrying forward compositional means rather than only reusing a complete answer.

### 2. More active library content can make learning worse

Andrew Cropper, *Forgetting to Learn Logic Programs*, AAAI 2020. [Author PDF](https://andrewcropper.com/pubs/aaai20-forgetgol.pdf), [publisher](https://ojs.aaai.org/index.php/AAAI/article/view/5776). Read §§3.2–3.4, 4.3, 5–6.

Forgetgol controls the predicates available to later program search. Its successful syntactical method removes duplicate search entries. Importantly, it retains their underlying program definitions: restricting the active vocabulary is not deleting all stored knowledge. In the Lego domain, remembering everything eventually worsened task completion, whereas syntactical forgetting maintained performance; the robot domain showed little completion loss. Statistical forgetting did not deliver the hoped-for improvement, and concept drift remained a limitation. The formal reductions require retaining the target hypothesis in the reduced space. The lesson is selective accessibility, not a general theorem that forgetting or smaller archives improve future performance.

### 3. A product can itself transmit constructive information

Christine A. Caldwell and Ailsa E. Millen, *Social Learning Mechanisms and Cumulative Cultural Evolution: Is Imitation Necessary?*, Psychological Science 2009. [Accepted manuscript](https://cognitionandculture.net/wp-content/uploads/Social_Learning_Mechanisms_and_Cumulativ.pdf), [DOI](https://doi.org/10.1111/j.1467-9280.2009.02469.x). Read Methods, Table 1, Results, Discussion.

Seven hundred participants built paper airplanes in seventy ten-person transmission chains. Conditions separately provided observed construction, completed planes with performance information, or teaching. Performance improved along chains in every condition, including results-only access without observing construction or receiving teaching. Consequently, inherited products cannot generally be treated as informationally inert. Participants already possessed abilities sufficient to learn from the visible artifacts. The authors caution that complicated actions difficult to reverse-engineer may behave differently. This is evidence against a universal product-versus-process dichotomy, not evidence that process transmission never helps.

### 4. Losing production information can sharply limit cumulative construction

Maxime Derex and Robert Boyd, *The Foundations of the Human Cultural Niche*, Nature Communications 2015. [Author PDF](https://maximederex.github.io/assets/pdf/derex2015b.pdf), [DOI](https://doi.org/10.1038/ncomms9398). Read Results, Discussion, Methods.

Participants discovered nested combinations in a computer game. Access to others' innovations helped even without their recipes, but access to production combinations produced substantially better outcomes. The authors emphasize transparency: missing recipes made reconstructing successive innovations harder. This complements Caldwell rather than refuting it. The game supplied all possible successful combinations, unlimited basic resources, and a fixed scoring system; complexity was rewarded by design. It therefore demonstrates effects of information access in a bounded compositional task, not spontaneous creation of purposes or a general equation between complexity and health. Its larger social groups are not equivalent to a serial predecessor-removal intervention.

### 5. Inherited explanations can preserve unproductive restrictions despite improvement

Maxime Derex, Jean-François Bonnefon, Robert Boyd, Richard McElreath, and Alex Mesoudi, *Social Learning Preserves Both Useful and Useless Theories by Canalizing Learners' Exploration*, Proceedings B 2025. [Author PDF](https://maximederex.github.io/assets/pdf/derex2025.pdf), [DOI](https://doi.org/10.1098/rspb.2024.2499). Read experimental design, Results §§c–e, Discussion.

Two hundred participants received correct, partial, misleading, or no theories about a wheel before repeated rewarded trials with accurate feedback. Received theories shaped attempted configurations and persisted, including misleading ones. Exploration was channelled rather than necessarily reduced in total extent. All treatments improved; the misleading treatment did not reliably underperform control on the final bonus trial. This supports inherited restrictions on exploration, not an unconditional performance penalty. It used written information, isolated Western participants, and a short trial horizon. Transfer of purported understanding can preserve blind spots even while local performance improves.

## Design consequences inferred from these sources

These are proposed controls and interpretations, not findings already established for the new experiment.

1. **Give the product baseline legitimate access.** A source program exposes subexpressions. Permit extraction and reuse, charging any declared work. Distinguish intermediates absent from the winning source from components already recoverable within it. If the product is opaque, name and justify that interface rather than treating opacity as an intrinsic property of products.
2. **Separate storage, access, search, and use.** Preserving definitions, offering a root as a search primitive, retaining computed semantics, and making something executable are distinct interventions. A library arm does not by itself test maintenance of an experimental institution. Clearing only some predecessor fields can silently transfer unpriced search history.
3. **Count the complete inherited object.** Charge dependencies and shared structure under an explicit representation. Root count alone can conceal arbitrarily different source sizes. Preserve only with information available before the realized later challenge. Distinguish initial available resources from expenditure and carried balances.
4. **Include adverse and neutral task relationships.** Related challenges test useful reuse; independent challenges and repetitions test different reasons to retain or discard. An irrelevant, equally costly library or excessive active library can diagnose overhead. A biased proposal rule can test channelled search, but a misleading-theory mechanism must not be claimed from storage costs alone.
5. **Measure construction separately from retrieval.** Record whether the later target was already computed by an inherited root or a recoverable subexpression. Direct reuse can be valuable succession; it is not a new composite constructed by the successor. Report correct installation, uninstalled validated candidates, costs, and continued operation separately.

## What this study could add—and what it cannot claim

The potentially useful contribution is the **joint causal accounting**: construction occurs through a generic interface; paid retention precedes the next challenge; predecessor-private state is removed; a successor reconstructs or combines what actually survives; testing and installation draw on the remaining budget. This joins mechanisms already investigated separately. It is not a claim of priority for reusable libraries, cumulative learning, product-versus-process comparisons, or generate-and-test discovery. This targeted review cannot establish publication novelty.

For three-input NAND synthesis, there are only 256 Boolean target functions. New source syntax, a newly realized truth table, and a newly installed capability must therefore be distinguished. If the target truth table is openly supplied, success is synthesis from a specification and finite verification. It does not demonstrate empirical discovery of the target, statistically independent experimental confirmation, creation of primitive actions, or invention of new purposes. Even a function absent from the inherited repertoire remains expressible within the supplied primitive semantics.

A favorable result can establish that particular paid inheritance policies change **which specified functions become executable within the available work**. It cannot alone show indefinite open-ended evolution, self-renewal of the external resource supply, maintenance of the synthesis machinery itself, universal health, or fair access among participants. A one-handoff result is a bounded succession result; repeated handoffs strengthen its horizon without removing those assumptions.

This also differs from the project's existing [situated-discovery](../../../../experiments/situated-discovery/PROTOCOL.md) and [prospective-revision](../../../../experiments/prospective-revision/PROTOCOL.md) studies, which already contain paid inquiry, constrained candidate formation, and retention tradeoffs. Interpret the new execution together with the [design review](DESIGN-REVIEW.md), not as the discovery of those earlier mechanisms.
