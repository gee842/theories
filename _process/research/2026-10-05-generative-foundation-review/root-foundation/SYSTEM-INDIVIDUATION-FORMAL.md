# Relational individuation: checked scope of explanatory supports

8 October 2026. AI-authored formal study responding to Ren's question, “What makes something a system, and how do its constitutive relationships generate its possibilities and changes?” This supplements the current system-individuation argument; it does not define systemhood by the conclusion that needs explanation.

**结果 / Result.** 同一关系域可以有两个不可比较的最小解释支持，却没有最小的共同支持。把所有坐标默认为可独立重新组合，会抹去产生这种情形的真实约束。形成活动可以改变哪些读数足以识别后续可能性；读数的充分性仍不独自证明因果参与、维持能力或唯一实体边界。 / One admitted relational domain can have incomparable minimal explanatory supports without a least support. Assuming freely recombinable coordinates can erase the constraint responsible for this result. Formation can change which readings suffice for later possibilities. Such sufficiency does not alone establish operative causation, self-maintenance, or a unique entity boundary.

## 1. What this adds

[SystemsOrganization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/SystemsOrganization.lean) already proves exact projected dynamics from fibre consistency and gives a formation mechanism. [FormedEffectiveLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/FormedEffectiveLaw.lean) already derives one concrete sufficient summary and its exact finite-history law. Those results are reused rather than counted again.

The present advance concerns an earlier question: **how does the admitted joint domain constrain attempts to reduce or intersect explanatory supports?** A selected region is a collection of readings of one state. There is no primitive independent environment or externally assigned owner. Interdependence of the readings may be exactly what makes several different small supports sufficient. The proof shows why a universally unique smallest support, or a boundary read off from isolated-coordinate variation, cannot be taken for granted.

This is a limit on particular mathematical individuation methods. It does not show that all actual systems lack boundaries or that correspondence is arbitrary.

## 2. Exact general parameters and inference

The new [SystemIndividuation module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/SystemIndividuation.lean) uses:

- A state type `S` and a predicate `admitted : S → Prop` specifying the states under comparison.
- An index type `I`, reading type `R`, and `read : S → I → R`.
- A selected response `response : S → V` and a region `B : I → Prop`.

`Supports admitted read response B` means: any two admitted states agreeing on every selected reading in `B` have the same response. This openly defines **explanatory sufficiency for that response**, not systemhood, material constitution or causal contribution.

`Recombines admitted read B C` says that, when two admitted states agree on the overlap of `B` and `C`, a third admitted state realizes the first state's `B` readings together with the second state's `C` readings. The intermediate state belongs to the same admitted domain; it is not an unrestricted intervention stipulated outside that domain.

`intersection_support_of_recombination` proves that two supports can be intersected when this recombination holds. Recombination is **sufficient**, not claimed necessary for a particular response. For example, a constant response can have empty support even in a nonrecombinable domain.

`full_product_recombines` constructs the intermediate state point by point for the full product `I → R`, with a decision procedure for membership in `B`. This supplies recombination rather than assuming it for that model. `full_product_support_intersection` then derives intersection closure. There is no finiteness restriction on `I` and no choice axiom. The full product remains a substantive mathematical domain choice; it is not asserted to represent every actual organization.

Other general results preserve sufficiency under enlarging the selected region or restricting the admitted domain, and show that a genuine response contrast cannot agree on a sufficient region. None concludes that a particular sufficient reading was operatively used.

## 3. A constrained domain with no least support

The finite example has one joint pair of Boolean readings and admits just diagonal states `(false,false)` and `(true,true)`. Its response is the left reading. These are supplied mathematical values and domain, not an empirical identification.

Both the left-only and right-only regions determine the response. Their intersection is empty and cannot distinguish the two admitted responses. Therefore:

- The intersection is not a support.
- The domain does not have the required left/right recombination.
- There is **no least support** included in every sufficient support.
- The left-only and right-only supports are each **minimal among decidable regions**.

The last qualification is part of `MinimalSupport` itself: each competing region comes with `DecidablePred C`. The no-least-support theorem does **not** have this restriction and quantifies over arbitrary proposition-valued candidate regions. The two claims must not be conflated. No classical axiom is needed to get the positive membership required by the minimality results because the compared regions have explicit decision procedures.

No admitted pair differs in just one coordinate while changing the response. Nevertheless the two diagonal states have different responses. `no_isolated_contrast_on_diagonal` and `joint_contrast_on_diagonal` verify this together. Thus lack of an admissible isolated-coordinate contrast does not establish absence of consequential joint difference. Extending the domain to permit independent interventions would change this question and needs its own warrant.

The right reading predicts the response by correlation; the response definition still reads the left. This is deliberately an example where **predictive substitution does not establish operative use or shared causal constitution**. It constrains an overstrong route to boundaries, rather than pretending to have already derived physical boundaries.

## 4. Formation and subsequent possibilities in one process

The same pair type carries one fixed `Generative.Process`, with three events:

| Event | Explicit local law |
|---|---|
| `correlate` | Replace `(left,right)` by `(left,left)`. |
| `flip` | Negate both readings. |
| `pulse` | Permitted exactly when `left = true`; preserve the state. |

`correlate_establishes_diagonal` proves that the formation event reaches the correlated domain from every pair. `diagonal_preserved_by_step` and `diagonal_preserved_by_trace` prove that every subsequent event and every finite admitted history stays in that domain.

On this established domain either reading identifies the full state and therefore preserves **every finite event-word possibility** (`left_supports_all_possibilities_on_diagonal`, `right_supports_all_possibilities_on_diagonal`). Here possibility means existential feasibility of a finite event word. The theorem does not quantify probabilities, arbitrary endpoint questions, guarantees over every nondeterministic branch, or sustainable recurrence. The proof identifies the complete pair from either coordinate on the diagonal; it does not establish that an actual observer can acquire that reading. The right reading does not do so on the unrestricted domain: `(false,true)` and `(true,true)` agree on it but differ on whether `[pulse]` is possible.

The checked history

```text
(false,true) --correlate--> (false,false) --flip--> (true,true) --pulse--> (true,true)
```

joins formation, subsequent change and realized activity. **Correlation establishes the sufficiency of a reading; it does not create pulse availability in this history.** It preserves the left value and hence immediate pulse enablement. `flip` changes that enablement. Correlation is not necessary for pulse: an initially true left value already permits it. There is no claim that this copying step creates autonomous maintenance or that predictive compression causes the later event.

The source therefore provides a bounded exact example of a formed domain changing the validity of a description, alongside later changes in possibilities under the same law. The existing formation mechanisms retain their separate, stronger constructive scope.

## 5. Checked proof and dependencies

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_system_individuation.py) compiled byte-exact snapshots in a fresh temporary build with Lean **4.29.1**, using only this module and unchanged `GenerativeCore`. It audited every new explicit named declaration, preserved theorem signatures, and compared the exact inherited Core audit inventory to its pinned receipt.

[Immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/system-individuation-checks/20261007T233431.104249Z/receipt.json):

- **27 new theorems / 41 new explicit named declarations**, all with empty axiom-dependency lists.
- **18 inherited Core theorem audits**, all empty and identical to the pinned baseline map; these are not new results or a retrospective audit of every Core declaration.
- 15 retained artifacts including byte-exact sources, checker/helper snapshots, compile logs, signature logs and audit programs/logs.
- Sources and checker unchanged during checking; no `sorry`, `admit`, custom `axiom`, `unsafe`, `native_decide`, implementation replacement or skipped kernel checking in the scanned source.

Generated constructors, projections and deriving declarations are checked by Lean but not counted as separately inventoried named declarations.

| File | SHA-256 |
|---|---|
| `SystemIndividuation.lean` | `aa2da76bae0b742b0966d856334ed0cd7e29ccf05ce33b0b674a00e5e0689578` |
| `check_system_individuation.py` | `abf0dfb0e39de26fd053ecabb84b621cb047c7e3cbd5c7c17235ab84c268e9ef` |
| Immutable `receipt.json` | `3379682d8dcb4f97f2f772f6a460c8baa7a95169790bcb0a9ce95dc7d8eab5a6` |

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_system_individuation.py
```

A rerun creates a new retained run and updates only this study's verification pointer. Empty axiom audits establish the dependency property of the Lean terms; they do not eliminate logical inference, supplied definitions, admitted-domain choices or the need for actual correspondence.

## 6. Contribution and remaining task

The results establish a constructive boundary on a proposed route to system individuation: exact description does not necessarily select one smallest region, and correlated support is not itself constitutive participation. They also establish that an actually formed invariant domain can change which readings suffice to preserve possibilities. The law, state representation and selected question remain explicit in this local model.

This advances the transition from joint relationships to accountable system descriptions. It supplies neither an assumption-free universal world law nor the philosophical warrant that every actual system's constitutive relations have been correctly identified. No normative direction follows from predictive sufficiency. The completed explicit G0/J ethical route and previously completed conditional generative mechanisms remain separate results to reuse.
