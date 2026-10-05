# Audit: an implemented route for noticing a missing possibility

5 October 2026. Prepared for the root-of-wisdom synthesis from a read-only copy of work produced in another research session. This is an audit of a synthetic mechanism, not independent empirical evidence about people or institutions.

## Answer supported by this source

We can notice something absent from our current working model when our encounters and retained records preserve distinctions that the working model does not yet use. A candidate-making procedure can then turn those distinctions into a testable proposal; a fresh intervention can establish whether the proposal matters for action. Neither retrospective confidence in the current model nor unrestricted speculation supplies this route by itself.

The implemented sequence is concrete:

1. Retain case-level attributes and identifiers, although the active decision rule treats all cases alike. Preserve the join to delayed outcomes.
2. Construct subgroup predicates from those attributes and ask whether failures concentrate in a subgroup. This generates a possible distinction, without yet claiming a causal explanation.
3. Convert the candidate into an actionable contrast: use B in that subgroup, compared with A.
4. Freeze the candidate and test it on new randomized cases. Deduct intervention cost and uncertainty before accepting it.
5. Keep the evidence, admit it to the decision process, and authorize a response in time. The implementation makes these separate gates.

The working model can thus be smaller than the records and exploratory language available to challenge it. That difference is the opening through which this particular discovery enters. The experiment begins inquiry on a schedule; it does not require an aggregate anomaly first. It also does not choose its own inquiry grammar or prove that every important omission will become visible.

## What is supplied and what is generated

All line locators below refer to preserved source snapshots under `work/model-adequacy/source-snapshots/`, unless a different location is specified.

| Element | Supplied or produced? | Exact source |
|---|---|---|
| Six binary attributes, two available actions, endpoint, costs, iid stationary cases | Supplied by analyst | `experiments/situated-discovery/PROTOCOL.md:7–19` |
| Active model initially lacks contextual distinctions | Supplied initial condition | `PROTOCOL.md:9` |
| Hidden two-attribute conjunction | Chosen by simulator; not directly passed to nomination | `experiment.py:90–104` |
| Representation language: all, 12 one-literal predicates, 60 two-literal conjunctions | Supplied finite grammar | `experiment.py:40–46` |
| First candidate | Produced from observed, linked discovery records by ranking inside/outside failure-rate differences | `experiment.py:48–61`, `205–214` |
| Conditional action proposal | Fixed template: B in candidate subgroup, A elsewhere | `PROTOCOL.md:27`, `experiment.py:143–155`, `216–235` |
| Fresh confirming evidence | New qualifying cases, 128 actions A and 128 B in shuffled order | `experiment.py:150–155`, `216–251` |
| Candidate acceptance | Lower bound on failure reduction exceeds B's .25 cost | `experiment.py:63–70`, `178–197` |
| Institutional standing and deployment | Analyst-set gates after validation | `experiment.py:186–196` |
| True policy gain and exact feature match | Scientist-only evaluation after trajectory | `experiment.py:265–276` |

The learner's selected proposal is not an injected correct answer. The larger representational opportunity is nevertheless supplied. Calling this unrestricted concept creation would be false. Calling it merely choosing among explicitly described final hypotheses also misses a real distinction: the script constructs and ranks predicate expressions from records rather than receiving a nominated correction. Both qualifications matter.

The environment object is passed to the simulation; the implementation does not enforce a security boundary preventing arbitrary access. The actual executed code uses current attributes, a separate trial randomization stream, and observed outcomes for the learning stages; its hidden predicate enters `outcome` and later scoring. This is an inspected algorithmic separation, not a claim about adversarial isolation.

## The strongest illustrative result

Under the planted two-attribute hazard, always choosing B is worse than always choosing A: population failure reduction .1875 is less than B's .25 cost. A subgroup policy improves expected loss by .125 per population case. An aggregate choice between A and B therefore misses the useful conditional response. See `sources/15-codex-theory-conversations/2026-10-05-discovery-before-demonstrated-returns.md:11–21` and `test_experiment.py:17–24`.

In the inherited held-out evaluation, protected inquiry validated and deployed a useful policy by the cutoff in all 256 hazard seeds. Removing timely linking records, allowing only the unconditional model, or imposing the severe funding schedule prevented validation. Denying standing or authority preserved the same first validation evidence while preventing deployment. These are strongly separated controls in this particular synthetic world, not estimates of real institutional causation. Sources: conversation synthesis `:53–73`; protocol `:43–58`.

The story is not that thought alone overcomes a narrow model. The observed route requires richer records, an adequate candidate language, causal testing, and maintained practical access to correction. The model-restricted arm shows why optimizing an impoverished policy space can miss an improvement; the short-record arm shows why no later cleverness repairs an unavailable join without collecting new information.

## What was independently checked here

The checks ran only under `work/model-adequacy/discovery-checks/`; the original project was never modified.

- Source SHA256 values for `experiment.py`, `PROTOCOL.md`, and `test_experiment.py` match the inherited evaluation freeze manifest exactly.
- All four inherited mechanism tests passed in the copied directory. They check all 60 planted pair predicates on an exact diagnostic distribution; useful policy versus exact feature recovery; confidence and cost handling; and retention, accounting, and gate separation.
- All 7,168 saved trajectory records were read. There are 256 seed clusters, with fourteen paired arms and two hazard conditions; these are not 7,168 independent replications.
- Recomputing the full saved summary reproduced it exactly. Every saved seed passed the gate-pairing assertions.
- The first and last evaluation seeds, 10000 and 10255, were replayed for both hazard conditions and all fourteen arms: 56 trajectories matched every saved JSON value exactly. This is reproducibility using the same implementation, not an independent implementation of the scientific model.
- An additional exact enumeration tested the representational limitation below. It is a diagnostic counterexample, not a new participant benchmark or an additional held-out performance claim.

`discovery-checks/audit-check-results.json` records results; `audit.py` makes the recount, replay, and new enumeration reproducible. `discovery-checks/inherited-evidence/copy-manifest.json` gives original paths, copy paths, byte lengths, and SHA256 hashes for the copied saved evidence. The raw record file hash is `5ebfebbd2d87632469d90d2b0e070d5d0c2c4f3c23d91394c381b2d63692a963`.

Two execution errors were procedural rather than findings: an initial unittest call used the workspace root instead of the copied module directory; an initial replay equality compared internal tuples with their serialized list forms. Correct-directory tests and JSON-normalized exact replay comparisons passed. These events are preserved in the check-results notes.

## A concrete limit: a candidate language can hide a useful correction

Keep the same six recorded binary attributes, two actions, costs, and outcome effect, but define the hazardous context by four specified literals instead of two. Its frequency is 1/16. The exact four-literal policy would improve population expected loss by

\[
\frac1{16}(.75-.25)=.03125.
\]

However, any available two-literal predicate covers at best a group of frequency 1/4, only a quarter of which lies inside this four-literal hazard. Its net population gain is therefore at best

\[
\frac14\left(\frac14(.75)-.25\right)=-.015625.
\]

One-literal and unconditional proposals also have negative gain. Exact rational enumeration of all 64 attribute combinations confirms that the best of all 73 inherited candidates has gain −1/64 (−.015625), while the unavailable four-literal policy has gain +1/32 (+.03125). Always A remains a zero-gain baseline. The independent exact calculation is saved in `discovery-checks/grammar-witness.py` and `grammar-witness-results.json`, including all 64 supports and every candidate's gain. It is explicitly labeled **new-this-cycle synthetic witness**, separate from the inherited held-out experiment. Its policy class uses B in one supplied predicate and A outside; composing several predicates into a deeper conjunction would enlarge that implemented class and remove this particular limitation.

This is not a claim that the world is entirely unobservable. Raw records contain enough information to identify the four-literal context if the generator is expanded. It demonstrates that successful calibration and rejection of every *available* proposal can coexist with a valuable omitted policy. More confidence or more data within the same proposal grammar does not create the missing expression. It also sharpens the necessary distinction between missing from the active model, missing from the candidate language, and missing from what can be observed at all.

## Statistical and practical limits

The confirming test's mathematical protection is conditional and narrower than discovery success. With a frozen candidate, fresh independent observations, 128 cases per action, and alpha .05/4 per attempt, the one-sided Hoeffding radius is about .185026. Acceptance requires an observed reduction greater than .435026, including the .25 action cost. A union bound controls any false acceptance across at most four attempts by .05 under the stated sampling assumptions. Source: `experiment.py:63–70`; `PROTOCOL.md:27–37`; inherited mathematical memo, now copied to `discovery-checks/inherited-evidence/candidate-discovery-math.md:318–329`.

This protects against accepting a nonbeneficial available policy. It does not ensure that the generator proposes the best possibility, that a useful rare context is encountered, that a negative result proves absence, or that an accepted explanation identifies the true causal moderator. A coarse subgroup may yield a beneficial policy without matching the simulator's named feature. Randomization inside that group establishes the action contrast under its assumptions, not a complete account of why the group matters.

Fresh confirmation permits exploratory search without an additional penalty for all 73 discovery candidates. It does not license repeated adaptive reuse of one confirmation set or repeated uncorrected significance peeking. Cash-based scheduling is valid here because it uses group membership, fixed action order, and cash, not unseen outcomes or other within-group attributes. Drift, dependence, informative loss, or population changes require a new argument.

The severe funding arm supplies only 23 units against a first full-test bill of 42.97. Its failure is forced accounting, not an emergent epistemic attractor. The absent-hazard world yields no accepted proposal in 256 protected runs but spends 150.49 units per run. Protected inquiry can incur real costs without finding a benefit. Source: conversation synthesis `:75–105`, `131–147`.

## Transferable answer and remaining boundary

The supported answer is a maintained process, not a magic faculty: preserve encounters that exceed the present summary; construct alternative distinctions; seek evidence that could distinguish their practical consequences; protect fresh checking from the selection process; and keep correction possible before the opportunity closes. Give those stages resources before their eventual payoff is known, while accounting for the cost of fruitless searches.

It is essential to add a boundary check: *what distinctions does this procedure have no way to express or encounter?* The four-literal counterexample shows why. Expanding instruments, variables, composition rules, intervention types, or sources of testimony can extend that boundary. Those extensions themselves remain finite and contestable; this source does not derive a guaranteed method for choosing every useful extension.

An elementary identification example in the inherited mathematical memo `:245–270` states the exact impossibility: two worlds have identical stored `(action, outcome)` distributions yet require different context-sensitive policies when context `X` was discarded. No amount of those same compressed records distinguishes them. Retaining `X` in new trials breaks the equivalence. Thus the need for a channel beyond the current compression is not merely a motivational slogan; it follows for this explicit pair of worlds.

This result gives a substantive partial answer to the user's question. We can create repeatable conditions under which particular omitted possibilities become noticeable and testable. We cannot certify that no important possibility remains outside every channel and grammar we currently possess. The appropriate conclusion after success is a warranted correction with stated scope, not a certificate of model completeness.
