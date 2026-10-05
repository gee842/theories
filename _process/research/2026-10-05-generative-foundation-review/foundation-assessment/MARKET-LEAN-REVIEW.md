# Independent semantic review of the market Lean interface

6 October 2026. AI-assisted internal review by a separate agent. Read-only inspection of [MarketGenerativity.lean](../../../../experiments/market-generativity/formal/MarketGenerativity.lean), its [README](../../../../experiments/market-generativity/formal/README.md), [verification record](../../../../experiments/market-generativity/formal/verification.json), checker and saved compiler output against the [mathematical study](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MARKET-DYNAMICS-MATH.md) and [Python transition](../../../../experiments/market-generativity/model.py). No compiler rerun or new empirical validation was performed. The [identification note](MARKET-IDENTIFICATION.md) governs the empirical interpretation.

## Judgment and artifact integrity

No blocking semantic mismatch was found within the formal README's stated scope. Independently recomputed SHA-256 hashes of the current Lean source, checker, toolchain specification, compiler binary and saved compiler output all match `verification.json`. The source declares 39 theorems; the saved output contains exactly their 39 dependency audits. The recorded dependencies are the disclosed standard Lean axioms. The checker rejects unchecked proof placeholders, added axioms, native evaluation shortcuts, warnings and missing audits, and freezes source bytes in a fresh build directory. This review inspected that procedure and its matching artifacts; it does not claim an independent compilation.

## Nonvacuity and what the certificate supplies

`Certificate` supplies parameter signs, nonnegative payoff advantage at the accountability floor, an update-size bound, influence/correction boundary inequalities, recurring funding and one inequality per support. It does **not** assume `Safe` is preserved. `rectangle_one_step` derives preservation of each coordinate from those conditions, and `rectangle_all_times` lifts this result by induction to every natural-number time and every admitted disturbance history.

The numerical certificate is nonvacuous: `example_certificate` and `example_safe` exhibit one essential support with positive floor 5, a nonempty initial state, paid correction and a strictly positive profit gap. `example_worst_admissible` supplies an admitted shock, while the generic theorem admits arbitrary histories. The collar proof covers its whole stated interval, not only a sampled corner.

The generic rational theorem is weaker in interpretation and broader in admissible inputs than the paper's physical model: it permits zero selection rate and non-strict payoff advantage, lacks some physical nonnegativity assumptions, and requires only upper bounds on disturbances. It proves invariance, not generic strict growth, affordable production, or physical realism. The standard example satisfies the paper's stronger conditions. Favorable signed disturbances in Lean do not contradict Python's restriction to nonnegative adverse shocks. The README makes these scope differences explicit.

## Guard and accounting

`safe_history_never_fails` is substantive: it establishes equality of the guarded history with `some` of the operating history. The guard checks essential supports both before and after a step. Safety protects every represented support, so induction supplies both checks; `none` is separately proved absorbing. The exclusion witness instead shows that a nonessential recipient can fall below its floor without triggering market failure.

Payment depends on beginning funds. `reserve_accounting` separately preserves capped reserves, correction expenditure and overflow. `funded_total_accounting` combines this identity with distributed private profits, renewal costs, collectible fines and political expenditure. Neither fines nor overflow are silently credited as physical renewal. These are monetary identities under external service receipts, not a derivation of productive value or physical conversion.

## Correspondence limits and corrections

For exact rational inputs, the displayed operating formulas match Python's ordinary authorized policy: the profit gap, practice update, influence memory, clipped accountability, pre-receipt reserve payment and separate support updates agree. Lean fixes authorization; Python additionally supports denied authorization and a disclosed frozen-rule comparator. Those alternative policies are outside the invariant theorem.

Lean discards a failed state's quantities into `none`; Python retains its final quantities and ledger, then freezes further activity. Their safe operating histories agree by inspection, but no cross-language refinement theorem is present. Real-valued convergence, the full destructive-region argument and finite-time failure proof remain paper proofs. Rational invariance plus finite-precision trajectories do not machine-check those limit claims.

Two documentation points were reported to the integrating agent: the recovery collar extends outside the main rectangle but is not its superset, because it raises the lower share bound; and the mathematical study's experiment-README link was unresolved at review time because that README had not yet been created. The previously flagged formal README grounding link was already repaired when checked. These observations do not change the checked theorem scope.

Integration follow-up: the experiment README is now present and the paper and formal guide use external recovery-region wording. The original grounding link resolves at its existing relative depth; no scientific change or new verification is implied by this documentation reconciliation.

The accepted local result is a conditional invariant/recovery certificate for a supplied market institution. The origin, truthfulness, authority and inclusive scope of that institution remain derivation and identification obligations.
