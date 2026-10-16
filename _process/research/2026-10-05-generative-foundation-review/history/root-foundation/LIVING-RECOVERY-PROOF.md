# Gross transport and the conditions of an actual return

8 October 2026, Asia/Bangkok. AI-authored formal continuation of [the living-dependency study](LIVING-DEPENDENCY-INTEGRATION.md), addressing the next bridge identified in [the preceding realization proof](LIVING-REALIZATION-PROOF.md): passive transport can change direction, and a temporary departure from a selected operative condition need not exclude a later return. The source is [LivingRecovery.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean).

**Result:** exact transport and work accounts now compose over unrestricted actual finite histories, retaining gross inward transfer, passive outward transfer and active export separately. A bound only at the endpoint yields a subtraction-free necessary budget for that actual return. There is no condition that earlier states stay inside the bound. The result removes the earlier model's nonnegative-net-transfer and every-state-bound restrictions; it does not derive the existence or physiological adequacy of a recovery. **Fifteen new named theorems and twenty explicit declarations pass Lean 4.29.1.**

The universal inference advanced remains concrete: the continued or renewed realization of a living relation constrains what must actually occur through its changing conditions. This module supplies a more faithful class of transport histories for that inference. It does not claim that all living continuation reduces to this class, or introduce an ethical verdict into the process law.

## 1. Actual gross transfers in one history

An arbitrary core process supplies actual state/action transitions. An arbitrary index type identifies selected transport relations within its states. For each index, the supplied `TransportLaw` retains inside amount \(x\), available work support \(e\), and four transition quantities:

- \(i\): passive inward transfer;
- \(o\): passive outward transfer;
- \(q\): active export subject to the work-coupling law;
- \(r\): support supplied or transformed into the work coordinate.

All are nonnegative natural-number quantities in declared units. A constant indexed cost \(k\) supplies a lower work cost per active export unit. There is no positive work charge on passive outward relief. The exact transition laws are

\[
x' + q + o = x + i,
\qquad
e' + kq \le e+r.
\]

The first law preserves both directions rather than truncating a signed net quantity to zero. The second does not claim that passive transport generates usable work. Amount, compartment and transfer refer to differentiated relations within the same unfolding; they are not an independent agent acting on a separately constituted environment. Their physical realization and appropriate boundary remain correspondence questions.

`Window P states actions start length` requires every actual transition and retains its reached intermediate states. It imposes no inside-amount bound. `fluxSum` uses the existing actual-window sum to total a selected transition quantity along exactly that history. It does not combine individually possible events from incompatible histories.

## 2. General window accounts

`window_transport` derives the exact cumulative equality

\[
x_{\mathrm{end}}+\sum q+\sum o
 = x_{\mathrm{start}}+\sum i.
\]

`window_work` independently derives

\[
e_{\mathrm{end}}+k\sum q
 \le e_{\mathrm{start}}+\sum r.
\]

Both are proved by composition of the actual transition laws, without an operative-state invariant. Gross fluxes can alternate in direction; the initial state may already be outside a desired range, and intermediate states can move farther away.

`positive_flux_has_event` establishes that a positive finite total has an actual positive contributing transition inside the window. This constructive witness connects the aggregate requirement to something that happens in the same history; it is not a claim that a response is merely enabled.

## 3. A necessary budget for an actual bounded endpoint

Take a supplied endpoint bound \(B\), with the sole endpoint premise \(x_{\mathrm{end}}\le B\). Combining the two cumulative laws gives `recovery_account`:

\[
kx_{\mathrm{start}}+k\sum i+e_{\mathrm{end}}
\le
kB+e_{\mathrm{start}}+\sum r+k\sum o.
\]

This inequality uses no truncated headroom subtraction. It remains applicable when \(x_{\mathrm{start}}>B\) or an intermediate state exceeds \(B\). The term \(k\sum o\) credits passive relief in the scaled accounting comparison; it is **not stored biochemical energy, work produced by passive transport, or a claim of fungibility**.

Two general necessity results follow with actual-event witnesses:

| Theorem | Explicit excess condition | Actual conclusion |
|---|---|---|
| `compensation_required` | \(x_{\mathrm{start}}+\sum i>B+\sum o\). | At least one transition in this history has positive active export. |
| `support_input_required` | \(kx_{\mathrm{start}}+k\sum i>kB+e_{\mathrm{start}}+k\sum o\). | At least one transition has positive support input. |

The second credits both passive relief and retained work before requiring input. Gross inward transfer alone does not justify the conclusion. Actual input to the work coordinate can originate in previously formed support elsewhere; it is not automatically new whole-level formation. Neither result identifies a unique implementation or proves an adequate one can be selected.

These are necessary accounts **for an actual history whose measured amount reaches the stated bound**. They are not sufficient conditions for restored living, regained membrane function, resumed division or intact repair machinery. A correct material balance can coexist with damage to relations omitted by the selected amount/work coordinates. If a concrete physiological recovery target entails an appropriate amount bound, the account can constrain that recovery. Establishing that target correspondence is separate work.

## 4. Finite provision and conditional repeated returns

For an included provision coordinate \(d\), `window_store` assumes the actual transfer law \(d'+r\le d\) and derives

\[
d_{\mathrm{end}}+\sum r\le d_{\mathrm{start}}.
\]

`included_store_bounds_recovery` combines it with the return account:

\[
kx_{\mathrm{start}}+k\sum i+e_{\mathrm{end}}+d_{\mathrm{end}}
\le
kB+e_{\mathrm{start}}+d_{\mathrm{start}}+k\sum o.
\]

This follows a support transfer through the same history. Enlarging the represented boundary to include the provision coordinate preserves its depletion. No bound on passive relief is invented, and finite support alone does not exclude indefinitely continuing histories with sufficiently relieving passive transfers. Formation, availability and conversion of the provision remain explicit physical-model questions.

`recurrent_input_at_returns` supplies a conditional indexed recurrence statement. Its premise says that, for each index and start, there is an **actual finite window** with a bounded endpoint and enough excess load, after passive relief and initial work are credited, to invoke `support_input_required`. The conclusion is actual input arbitrarily late along that same history.

The supplied endpoint bound may differ between indices and windows. The theorem does not require an earlier excursion, a fixed recurring operative target or a return to an identical prior state. To interpret it as biological repeated recovery, the target and relevant bounds must be identified independently; selecting a bound afterward does not establish physiological correspondence or load coverage. Actual successful endpoints and excess-load windows are premises, not predictions. No stochastic hazard, positive mean loss or mere passage of time supplies them here.

## 5. Genuine limits preserved by explicit histories

The module includes a simple process whose state is `(inside, work)` and whose action records the four exact transfers. Its laws are precisely the accounts above with unit export cost. The following witnesses test the scope of the general claims:

- `passive_relief_without_work` takes `(4, 0)` to `(2, 0)` by passive outward transfer of two, with no active export or input. Thus crossing a bound of three does not make work input universally necessary for return of this amount.
- `passive_excursion_then_return` composes `(2, 0) → (5, 0) → (2, 0)`, first through inward transfer and then through passive outward transfer. The amount actually exceeds three in the middle; neither sign is deleted from the history.
- `retained_work_restores_after_excursion` composes `(2, 3) → (5, 3) → (2, 0)`. Active export uses retained work after the excursion, with zero new input. The available work is not reset at the intermediate state.

These are kernel-checked structural examples, not parameter fits or biological rescue experiments. They show that the stronger universal claims—every excursion needs fresh support, passive relief is irrelevant, or every represented state must obey the endpoint bound—do not follow from this model. They do not prove that a damaged organism can realize those transfers or that amount restoration alone constitutes its recovery.

## 6. Relationship to the preceding result and primary evidence

`fromRealization` embeds the previous `LivingRealization.TransportLaw` algebraically by carrying its net inward coordinate and recording zero separate passive outward transfer. `embedded_passive_total_zero` checks that the added outward coordinate totals zero, and `old_maintained_window_is_unrestricted` preserves each earlier actual window when the maintained-state restriction is forgotten. The prior source and source-bound receipt are unchanged.

This is an **algebraic embedding of the earlier coordinates**, not a reconstruction of physical gross fluxes hidden by a net measurement. It does not show that passive outward transfer was physically absent in every prior application. Where actual gross fluxes are available, the new model retains both directly. Its greater scope concerns admitted mathematical histories, with empirical correspondence still to be established.

[The primary evidence assessment](LIVING-RECOVERY-EVIDENCE.md) reads the relevant recovery assay more closely. It distinguishes observed nutrient-assisted repolarization and resumed growth from a return to a fixed amount bound, and from this model's passive-relief examples. The proof investigator relies on that source assessment and does not claim a separate primary-paper reading, original-data analysis or direct ATP-flux measurement. The existing stochastic concentration model is not proven to refine these discrete count equations. Fixed amount units, compartment geometry, export coupling and constant cost remain supplied. Endpoint bounds also do not establish continuous safety between represented states.

The new mathematical connection is therefore substantive but bounded: **gross transport plus actual endpoint attainment yields a general support constraint even when interim departures and passive relief are retained**. A separate material change, such as irreversibly lost membrane integrity, can prevent an apparently budget-feasible return. Such a concern must be represented and tested through its physical relations, rather than inferred from an arbitrary good/bad label.

## 7. Verification

A fresh temporary directory received current copies of all five modules in dependency order: `GenerativeCore`, `ContinuationRenewal`, `SituatedRenewal`, `LivingRealization` and `LivingRecovery`. Lean 4.29.1 compiled the complete closure with only that directory on the project `LEAN_PATH`, alongside the toolchain standard library. A generated audit imported the new module and printed the axioms of every explicit new declaration.

**Initial check:** all modules pass; the new module has **15 named theorems / 20 explicit declarations**. Eight have empty axiom dependencies, and twelve use only `propext` and `Quot.sound`. There is no new custom axiom, `sorry`, `admit`, `native_decide` or choice dependency. Mathematical inference is kernel checked; physical correspondence is not certified by that fact.

New source SHA-256: `d835300e75172b58093aa4289df3a499df7bfd81eb0fe17e69223c49ddbd8173`. The unchanged prior `LivingRealization` source retains SHA-256 `539742f929fbc8d3d9efc015ae0b08d80463ed99e65a0ea4af4c4f2eaf80b083`.

**Final source-bound check passes:** the root's [reproducible checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_living_recovery.py) validates **five modules / 107 explicit declaration audits**, including the **20 new declarations / 15 named theorems** above. The [current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-recovery-verification.json) and [immutable run receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-recovery-checks/20261007T184505.678085Z/verification.json) preserve source, checker, compiler and audit bindings. [Independent review](LIVING-RECOVERY-REVIEW.md) reports no blocker at this mathematical and correspondence scope and verifies those bindings.

No generated Lean object, interpreter cache or dependency installation is added to the research tree. Documentation checks do not substitute for the checked inference or establish physiological correspondence.
