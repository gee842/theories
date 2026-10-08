# 可接纳变化怎样由实际形成路径获得根据
# Deriving the comparison domain from formation and continuation

8 October 2026. AI-authored formal continuation of the [systems study](SYSTEM-INDIVIDUATION-FORMAL.md), addressing Ren's question about why identified relationships and admitted variations characterize the target. This study closes an independent domain input in the existing mathematical example. It does not certify that the example describes any particular physical system or establish the stronger assumption-free foundation.

**结果 / Result.** 原来的两坐标过程保持不变。从任意初始状态，凡首先完成 `correlate`、再进行任意有限后续活动的结果，恰好是两个对角状态。排除额外状态由每一步的保持性证明；覆盖全部对角状态由具体的零次／一次翻转路径证明。可接纳域因此成为原有过程的推论，而不再是这项应用独立提供的筛选谓词。 / Under the unchanged process, endpoints following correlation and any finite continuation are exactly the two diagonal states. Step preservation excludes surplus states; explicit zero/one-flip paths reach every included state. The comparison domain is therefore derived from this process and declared phase, rather than independently stipulated for this application.

## 1. The dependence being discharged

[SystemIndividuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/SystemIndividuation.lean) has a generic `admitted` predicate and an example restricting two Boolean readings to equal values. It already proves that `correlate` establishes this restriction and that every subsequent event preserves it. That is the **upper-bound** half of a domain explanation: nothing outside the diagonal can occur following formation. It alone does not prove that every diagonal state can actually be reached from a given seed.

The new [VariationWarrant module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/VariationWarrant.lean) supplies the missing coverage half and carries the derived domain into complete finite continuations and response-support questions. This distinguishes an invariant containing all realized endpoints from the exact set of those endpoints.

The operational law is unchanged:

| Event | Inherited operation |
|---|---|
| `correlate` | `(left,right)` becomes `(left,left)` |
| `flip` | Both readings are negated |
| `pulse` | Admitted when the left reading is true; state retained |

These are roles within one joint state and event relation. The proof does not posit a separate observer or a freely acting intervention source. The word “actual” here concerns executions of this specified mathematical process, not a new laboratory observation.

## 2. Two constructive directions establish exact coverage

`Prepared seed t` abbreviates the existence of a finite suffix with

```text
Trace process seed (correlate :: suffix) t.
```

This selects an explicit phase of the unchanged process. It does not define the endpoint restriction as diagonal. `preparation seed bit` supplies the empty suffix if the seed's left value equals `bit`, and one `flip` otherwise.

`preparation_trace` checks the four Boolean cases and constructs

```text
seed --correlate; preparation seed bit--> (bit,bit).
```

Then:

- `every_prepared_endpoint_is_diagonal` proves the upper inclusion using the actual first correlation event and inherited preservation along every later trace.
- `every_diagonal_endpoint_has_preparation` proves the lower inclusion by constructing a preparation for the target's first coordinate.
- `prepared_iff_diagonal` combines these into exact equality in membership, for **every seed**.
- `prepared_iff_short_preparation` proves that every attained endpoint has a preparation with zero or one flips.
- `off_diagonal_endpoint_not_prepared` excludes either unequal reading pair from this phase.

There is no `Exact` field, coverage hypothesis, surjectivity premise or supplied diagonal-domain equivalence in these theorems. Their conclusion is derived from the event definitions and Boolean cases. The event definitions, state carrier and choice of phase remain explicit mathematical inputs.

The exact domain is independent of the seed, but the preparing word depends on the seed. No claim of preparation without cost or of physical reset availability follows from the mathematical event alphabet.

## 3. Full continuations use the boundary that was prepared

`prepared_closed_under_continuation` appends a later trace to the history that reached its starting state. It reuses the Core's existing shared-boundary concatenation theorem; it does not concatenate independent trajectories without checking their actual join.

`formed_continuation_iff` derives, for every finite later word and selected final endpoint:

```text
some formation-plus-preparation followed by word reaches t
    iff
word reaches t from (false,false) or from (true,true).
```

The forward direction recovers the actual prepared intermediate state. The reverse direction constructs the preparation of that very state. This is exact endpoint correspondence for all finite later words, derived without an independent correspondence input.

`formed_outcome_iff` preserves any selected proposition about the final endpoint as well. Consequently it preserves more than the bare existence of an event word. These are existential finite-history results: they do not assert probabilities, guarantees over all branches, physical controllability, sustainability or infinite histories.

The preparation is existentially quantified. Different experiments or histories may use different preparations. The theorem does not claim a single preparation simultaneously realizes both diagonal values or every later possibility.

## 4. Supports are tested on genuinely attained comparison states

`support_iff_prepared_tests` derives the response-support criterion using the two attained preparation endpoints. The selected response can have any result type in the theorem's declared universe; the region remains any proposition-valued subset of the two reading positions. No arbitrary isolated-coordinate change is admitted.

`possibility_support_iff_prepared_tests` does the same for feasibility of every finite event word. Its comparison-state domain has only two members, but the later-word quantifier remains unrestricted over finite lists. It is **not** a claim that two empirical observations verify all behavior of an unknown physical system.

`right_supports_generated_possibilities` carries the original right-reading sufficiency into the attained domain. `generated_response_support_iff_diagonal` and `generated_domain_has_no_least_support` carry the previous nonexistence of a least sufficient region into this independently generated comparison domain.

This strengthens the scope justification for the earlier example. It does not make the right reading operatively responsible for the pulse. The native pulse law still checks the left coordinate. Predictive or explanatory substitution remains distinct from constitutive participation.

## 5. Exact domains are useful, not a universal gate

A claim need not know the exact set of every possible physical state to be warranted. The type of claim determines which inclusion is needed:

- A concrete permitted execution supplies a witness for an existential possibility within the stated model. Its use for a physical claim needs evidence that this execution is realized or realizable under the physical conditions claimed.
- A property proved throughout a warranted conservative domain applies to its included target states. The existing `SystemIndividuation.support_restrict_domain` already gives the corresponding restriction rule for explanatory sufficiency; it is reused, not recounted as a new theorem.
- Exact coverage needs both directions. A mere invariant is insufficient for claims that every state it describes can be attained; sampled attainable states are insufficient for claims excluding all unsampled alternatives.

The concrete mechanism supplies both directions. The broader lesson is a distinction among proof obligations, not a new law guaranteeing universal scientific correspondence. It avoids replacing actual uncertainty by an arbitrary permission to vary every coordinate independently, and also avoids imposing exhaustive possible-state identification as a prerequisite for every narrower warranted claim.

## 6. Scope counterexamples remain executable

`off_diagonal_execution_before_formation` checks the history

```text
(false,true) --flip--> (true,false) --flip--> (false,true).
```

These are legitimate off-diagonal executions under the same original law. Their exclusion after the correlation prefix is phase-specific, not a claim that unequal readings are universally unrealizable.

`normalization_does_not_preserve_original_word` checks that `[correlate]` and `[correlate,flip,flip]` can have identical endpoints while being different event words. The short-preparation result therefore preserves reachable endpoints, not historical provenance, elapsed steps or every question about the original trajectory. No full-history equivalence is inferred from it.

## 7. Kernel checking and exact dependency scope

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_variation_warrant.py) used a fresh temporary build, byte-exact source snapshots and Lean **4.29.1**. It checked all explicit named declarations in the new module and compared both inherited inventories against the unchanged [systems receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/system-individuation-checks/20261007T233431.104249Z/receipt.json).

[Immutable new receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/variation-warrant-checks/20261007T234515.871133Z/receipt.json):

- **19 new theorems / 21 new explicit named declarations**, all with empty axiom-dependency lists.
- **59 inherited declarations / 45 inherited theorems**, all audited dependencies empty and identical to the pinned inventory: 18 Core theorem audits plus all 41 explicit systems declarations. These are reused results, not new theorems.
- 21 retained artifacts: sources, checker/helper, compiler version, compiler logs, theorem signatures and axiom audit programs/logs.
- Sources and checker unchanged during checking. The scanner disallows `sorry`, `admit`, custom `axiom`, `unsafe`, `native_decide`, implementation replacement and skipped kernel checking.

| Artifact | SHA-256 |
|---|---|
| `VariationWarrant.lean` | `599c90b9643f01b06c5185e4d38b19bb9e502efab2e9d71590fb30d6503042fa` |
| `check_variation_warrant.py` | `30808028af120ff0592d26062d9f2e81dbb9c743ccac57bf52a798b56ca09aa9` |
| Immutable `receipt.json` | `a5136177bc8d18b616f62cbb0fa17a1c5a9403e00ac1c5c94875608bb588ec62` |

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_variation_warrant.py
```

A rerun preserves a new receipt and updates only this study's verification pointer. Generated Lean declarations are kernel checked but are not separately counted by this explicit-declaration inventory. Empty dependency lists do not remove Lean's logical background, the fixed process definitions, selected question or the substantive warrant needed when applying this model to actual systems.

## 8. What is resolved and what is not

**Resolved in the existing formal mechanism:** the admitted comparison domain is no longer an independently supplied diagonal restriction. Its exact extent and its applicability to all finite post-formation continuations follow constructively from the unchanged operation law. The mechanism itself provides the comparison witnesses and preserves the constraint that excludes inappropriate variations.

**Not resolved by this formal result:** that every actual system has this event architecture; that this example describes a particular physical system; that empirically warranted laws or correspondence follow from pure Lean logic; that all constitutive relationships are uniquely identifiable from these response tests; or that the strongest assumption-free foundation is complete. The completed conditional foundation and explicit G0/J ethical route keep their separate scopes.
