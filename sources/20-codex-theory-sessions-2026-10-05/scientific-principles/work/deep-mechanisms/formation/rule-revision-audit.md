# Independent audit of bounded rule revision

Audit date: 5 October 2026. Audited `revise_standard.py`, `standard-revision-results.json`, and `standard-transfer-results.json`. Independently derived arithmetic and bounds, replayed all recorded studies and transfer episodes, instrumented observation acquisition, and checked the relay example. Original code was not modified by this auditor. Reproducible audit code/results are `audit_rule_revision.py` and `rule-revision-audit-results.json`.

## Verified implementation

The learner's generation, edit, screening, and checking functions do not receive the task profile, hidden truth table, or true risk. The environment supplies observed labels through `observe`. Predictions, candidate nomination, local validation, and rule revision depend on observed records and supplied rules. World information is used by environment generation and external controls, as it should be.

The edit operator deletes a specific prefix-improvement requirement. The discovery phase compares paid observed loss in 32 paired task episodes. If the edit wins this screen, 256 independently generated checking task pairs assess it. Each pair shares a task type but has separately generated outcomes for the two policies. Full-grid training and local validation are separately paid. Routine deployment reveals new outcomes without additional acquisition charges, an explicit modeling assumption. Instrumented observation counts in the default pure-interaction run are 864 calls of eight labels and 576 calls of 64 routine outcomes. Thus no arm silently inherits the other arm's free training or local validation data.

The default experiment's independent exact arithmetic is:

- Incumbent pure-interaction episode: 8.75 expense + 32 prediction errors = 40.75 observed loss.
- Edited episode: 17.50 training/search/validation expense + 2.56 field-use expense + zero errors = 20.06 loss.
- Gain per episode: 20.69.
- 288 pairs, both arms paid: expense 8297.28.
- Conservative upfront reserve: 2×288×20.06 = 11554.56.

All ten current seeded study records and all five fresh transfer profiles replayed exactly. This is a reproducibility check, not independent empirical validation. Pure-interaction and simple-control arithmetic is exact; noisy records are seeded realizations, not exact probabilities.

## Statistical guarantee and its scope

For the stated default cost schedule, a policy episode's expense is at least 8.75 and at most 20.06, and prediction errors lie in [0,64]. Hence each incumbent-minus-edit difference D lies in [-75.31,75.31]. For n independent checking task pairs, a one-sided Hoeffding radius is

75.31 sqrt(2 log(1/alpha)/n).

At n=256 and alpha=.05 this is 11.52123836366077. The recorded 20.69 mean therefore has lower bound 9.168761636339232. The formula is correct. For one frozen edit, one check, a fixed configuration, and the declared IID task distribution, accepting only a positive lower bound bounds erroneous acceptance of an edit with nonpositive mean gain by alpha. Fresh checking makes conditioning on the discovery screen legitimate.

This is not a guarantee under distribution shift, dependent tasks, unknown cost bounds, repeated adaptively selected checks, or selection among many edits on the same checking outcomes. The 512-task transfer runs are diagnostic demonstrations of this limitation; the deployed rule remains frozen and can lose after a shift.

A sample-size extension was initially added at n=1024 for the mixed profile using the same checking stream as the n=256 failure. The audit flagged this as an optional-stopping risk. The formation agent then fixed the enlarged design and switched to seed 912867, generating new discovery and checking streams. The new fixed-design run passes with mean 8.76330078125 and lower bound about 3.00268. Its design was informed by the earlier result; it is not autonomous learner continuation or a combined lifetime-.05 procedure. The per-check theorem applies under the declared fresh-sampling assumptions. This repair and all regenerated records replayed correctly.

## Budget chronology issue found and fixed

The original incumbent-gate pilot generated its labels before checking whether pilot expense was affordable. An instrumented budget-zero case confirmed one observation call before return. The formation agent moved the affordability check and payment ahead of acquisition and regenerated results. The same instrumented boundary case now makes zero observation calls and returns `pilot_unfunded`. Default reported results were unaffected by this repair.

The remaining reserve discipline is conservative and coherent: it reserves enough for both full phases before starting, and actual expense stays under the cap. A study can be rejected as unfunded even when it might have ended early more cheaply; that is the specified policy, not a numerical error. Synthesis, aggregate arithmetic, context control, and meta-interpretation have no additional price in this small model. Therefore the ledger prices the named costs, not every conceivable cost of inquiry.

## What changes endogenously, and what remains supplied

The implemented object that changes is an admission/search requirement. It determines whether pair hypotheses may be examined when singleton fit does not improve. Calling it a methodological standard is defensible under this operational meaning. It is not a changed epistemic aim, loss function, meaning of truth, institutional constitution, or meta-validation standard.

The proposal grammar has exactly one permitted edit and explicitly protects the final-improvement and fresh-validation clauses. The learner assesses whether to adopt that supplied syntactic possibility. It does not discover which of arbitrary clauses should become revisable. The outcome-sensitive acceptance of the edit is endogenous; the edit grammar, evaluation objective, and means of opening a meta-probe are not.

The `incumbent_gate` branch truly implements lockout: it applies the incumbent singleton-improvement requirement to authorizing the meta-probe and returns before discovery on the noiseless interaction plateau. The `protected_probe` branch supplies a separate route around that gate. Thus the study demonstrates the difference between two implemented authorization arrangements. It does not show a wholly closed rule system spontaneously constructing its own external opening.

## Economic interpretation

A positive checked per-episode gain and a funded study are distinct from an unconditional return on research expenditure. The added matched-service ledger supplies an explicit counterfactual: the study delivers 576 prediction blocks, and these are valued as useful routine service. In pure interaction, actual loss is 17513.28, including expense 8297.28; providing the same 576 blocks with the incumbent costs 23472 in the same objective. Incremental loss is therefore -5958.72. These values independently checked exactly.

This supports a net gain in that matched-service comparison. If study forecasts have no service value, if their tasks are artificially duplicated, or if study tasks displace other valuable activities, a different counterfactual is required. For noisy cases, doubling the observed incumbent stream estimates the matched baseline; because those records participate in screening, it is not independently validated evidence of research-program profitability. The code records this limitation.

## Controls and transfer

Single-feature and constant environments reject the proposed edit because it adds search expense without improving prediction. The pure fair-label run rejects it in discovery. The noisy-interaction run can pass the discovery screen by chance and then fail fresh checking. The original mixed run has a positive observed mean but an insufficient lower bound; failure to adopt is not proof of no benefit. Higher field cost reverses the pure-interaction economic case. Transfer executes the actual frozen learned rule on newly generated tasks and shows that its benefit is domain-specific.

An added evaluator-only enumeration establishes true expected gain +8.8449609375 for the mixed profile, -3.000078125 for fair labels, and approximately -3.3718190062 for noisy interactions. These agree exactly with an independent reconstruction from the earlier fully enumerated policy results at the new 64-decision horizon. The learner never receives these evaluator values.

These are meaningful controls. They establish consequences of the declared implementation and show that the procedure does not mechanically adopt its sole candidate in every world. They do not establish how often real scientists revise standards this way, that the single supplied edit is representative, or that the entire proposed theory has been empirically confirmed.

## Independent relay check

With maintenance m=1 and reconstruction k=3, funding r=2 preserves installed capacity but cannot restore absent capacity. Starting with capacity 1, the funding sequence [0,2,3,2] produces capacity states [1,0,0,1,1]. Thus a zero-funding pulse loses capacity; return to 2 does not restore it; a startup grant of 3 does. The assertion is checked in the audit script. Permanent trapping remains conditional on the nonbanking/no-credit/no-substitute assumptions in the architecture memo.
