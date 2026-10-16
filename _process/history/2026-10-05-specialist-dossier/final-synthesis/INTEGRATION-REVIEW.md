# Critical integration review

5 October 2026. Reviewed the then-current INTEGRATED-THEORY.md and COMPOSITION-AND-SCOPE.md, checked their identification claims against IDENTIFICATION-AND-VALUE.md and the saved reproduction-test reports, and inspected the operational companion's finite-horizon and confidence assumptions. This is internal AI review, not independent human peer review.

## Required repairs before claiming the package is complete

### 1. The bounded-recurrence counter is one step too permissive

**Location:** [COMPOSITION-AND-SCOPE.md:48](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/COMPOSITION-AND-SCOPE.md:48).

The current text says that service must occur at least once every \(D\) steps, resets the counter on delivery, increments it otherwise, and prohibits values **above** \(D\). With a reset to zero, this permits \(D\) consecutive missed steps and a delivery interval of \(D+1\). For \(D=1\), one missed service step is still permitted, contradicting service every step.

**Exact repair:** define \(q=0\) immediately after delivery, update \(q^+=0\) on a service transition and \(q^+=q+1\) otherwise, and require \(q<D\), equivalently forbid \(q\ge D\). Specify the initial counter or deadline phase. Then no length-\(D\) block of nonservice transitions is allowed. Alternatively retain the original inequality and explicitly change the requirement to at most \(D\) consecutive missed steps, but that is a different contract.

This is a genuine functional guarantee error, not merely a terminology preference. It matters because the composition note is used to explain how preservation of an institution becomes preservation of an independently specified function.

### 2. State the synthetic intervention's starting point precisely

**Location:** [INTEGRATED-THEORY.md:200](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:200).

“After restoring execution” can imply a switch after a calibration period with inherited archives. The saved 9.99-point comparison instead enables execution from the same original complete initial state and follows the process for 25 rounds. The calibration equivalence concerns a restricted projection; it does not assert equality of hidden archives or every observable history.

**Suggested replacement:**

> The feedback and rival models share the specified calibration history law. Enabling execution from the same original complete initial state changes 25-round retention by approximately 9.99 percentage points in the feedback model and zero in its rival. This is a constructed intervention contrast, not an observed institutional effect. The new exact design examples likewise verify logic and computation, not a real-world causal hypothesis.

Support: [reproduction-test README:25](/Users/ren/theories/experiments/integrated-correction/general-framework/reproduction-test/README.md:25), [README:35](/Users/ren/theories/experiments/integrated-correction/general-framework/reproduction-test/README.md:35), and [README:39](/Users/ren/theories/experiments/integrated-correction/general-framework/reproduction-test/README.md:39).

### 3. The mechanism companion must exist before delivery

At the time of this review, the links to MECHANISM-MATH.md at [INTEGRATED-THEORY.md:73](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:73) and in the specialist-material list had no target file. The partner may still be writing it. Final delivery must include it, especially because the main text delegates regularity assumptions and a global collapse proof to that document.

All other local targets in these two reviewed documents existed. This was a file-existence check; it did not prove that every heading anchor remains valid after editing.

## Substantive checks that passed

**Report/access/content intervention.** The four-arm counterexample is correct: \(M=A,Y=BM\) and \(M=A,Y=AB\) agree on every ordinary \((A,B)\) assignment. A delivered-content intervention setting \(M=0\) with \(A=B=1\) separates them. The main text correctly requires either a feasible, consistently implemented content intervention or an independently justified route exclusion. It does not infer mediation solely from positive first-stage and access effects, or from a positive factorial interaction. See [INTEGRATED-THEORY.md:172](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:172).

**Experimental optimum.** Section 6 accurately describes a finite candidate and experiment family, retained experiment identities, and a minimum pairwise total-variation objective. It does not mislabel this as globally optimal multiclass inference or sequential experiment design. The companion's exact example has design weights \(3/4,1/4\), expected resource cost \(5/4\), minimum pairwise separation \(1/4\), and a matching dual certificate. The resulting \(3/8\) error is a worst-pair best equal-prior binary error, not a simultaneous three-class error guarantee.

**Composition.** C1 and C2 are valid one-step induction certificates under their supplied transition laws. C1 correctly requires joint feasibility and shared-resource compatibility, preserves participant-specific observations, states initial membership, and is only sufficient. C2 correctly requires safe establishment transitions rather than assuming that individually sustainable modes can be switched arbitrarily. These do not prove that a policy is selected or implemented; the documents appropriately keep that issue inside the mechanism model.

**Mechanism numbers.** Direct substitution confirms \(H=4\), \(u_{\mathrm{crit}}=1/4\), \(E^*=2\), and \(C^*=3\pm\sqrt7\) for the stated rational-production example. The strict floor interval \(7/12<u<2/3\) and the chosen equilibrium at \(u=5/8\) are also correct. This calculation checks the numerical illustration, not the unprovided general-production or global-collapse proofs.

**Central and final scope.** The synthesis distinguishes a conditional necessity, a causal architecture requiring validation, and normative acceptance. The opening, task-status table, and final review statement explicitly leave real-system loop identification and practical superiority unfinished. They do not equate endogenous persistence with alignment. These boundaries should remain in the final user-facing response. See [INTEGRATED-THEORY.md:7](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:7), [line 13](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:13), and [line 204](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:204).

**Evidence record.** The institutional finding remains bounded persistence evidence; the authority-investment estimate remains inconclusive; the microbial primary joint criterion and earlier selector prediction remain failed. The new synthetic results do not overwrite these findings. The claim register is consistent with the existing reproduction-test record.

## Clarifications recommended without treating them as new discoveries

1. C1 should state that the admitted disturbance set is nonempty and the transition is total on its operating region, or model deadlock as an explicit failing transition. Otherwise “continuation” can become vacuous when no admitted next transition exists. The invariance statement itself is valid, but a nonblocking premise is needed for continued operation.
2. [INTEGRATED-THEORY.md:198](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md:198) says fitting and testing “must use different evidence.” Qualify this as the contract for the claimed held-out predictive comparison. It is not a universal theorem prohibiting valid likelihood inference, prequential assessment, or adjusted reuse of observations.
3. The main finite-policy optimum should continue to be read with ADAPTIVE-OPTIMUM.md's single-controller interface and finite library. The composition theorem supplies a certificate for already specified local policies; it does not convert the single-controller synthesis theorem into arbitrary decentralized controller synthesis.
4. The first four rows in the optimality table solve distinct declared problems. No theorem in the package selects the jointly best scientific architecture, causal model, acceptable-risk criterion, and ethical procedure. This is presently acknowledged rather than concealed.

## Citation verification and its limits

The primary references checked for the current integration support the stated lineage:

- [Chen and colleagues](https://arxiv.org/abs/1810.10636) address compositional invariant sets through assume-guarantee contracts.
- [Ghasemi, Sadraddini and Belta](https://arxiv.org/abs/1909.06425) explicitly address decentralized robust invariance with local information.
- [Moldovan and Abbeel](https://arxiv.org/abs/1205.4810) address safe exploration with substantive dynamics assumptions.
- [Heim and colleagues](https://proceedings.mlr.press/v100/heim20a.html) distinguish a learnable safety measure from safety guarantees before that measure has been learned.
- [Itao and Kaneko](https://doi.org/10.1073/pnas.2500960122) and [Weitz and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/) support the caution that endogenous institutions and game-environment feedback are established antecedents.

The simple discrete-time composition proofs are self-contained and do not claim to import every theorem of the cited continuous-state studies. The citations support the restrained statements actually made; this is not an exhaustive novelty audit.

## Review boundary

After the two textual repairs and the mechanism companion's completion, no further blocker was found in the **central claim, identification logic, stated experiment-design optimum, composition proof, numerical illustration, empirical status, or checked citations**. That is the reviewed scope. It is not certification of every theorem in the corpus, full external validity, a mechanized proof audit, or a declaration that the four requested scientific achievements have all been empirically completed.

## Repair verification addendum

Verified the requested targeted repairs in the saved documents on 5 October 2026:

1. **Recurrence counter — resolved.** COMPOSITION-AND-SCOPE.md now prohibits counter values greater than or equal to \(D\), explicitly describes rolling \(D\)-step windows, and specifies initialization from elapsed time or an explicitly credited time-zero delivery.
2. **Synthetic intervention timing — resolved.** INTEGRATED-THEORY.md now states that execution is enabled from the same original complete initial state and distinguishes the feedback model's approximately 9.99-point 25-round change from the rival's zero change.
3. **Nonblocking continuation premise — resolved.** The composition note now requires a nonempty admitted disturbance set and a defined transition for every admitted state, joint action, and disturbance, with explicit continuation conventions for terminal outcomes.
4. **Held-out evidence wording — resolved.** The fitting/testing separation is now explicitly the rule for this prospective comparison, rather than an unrestricted assertion about all statistical inference.
5. **Missing mechanism companion — file-integrity issue resolved.** MECHANISM-MATH.md now exists at the referenced path. Its remaining proof review is separately assigned to the mathematical reviewer; this existence check does not certify those proofs.

No new broad review or experiment rerun was performed for this addendum. The original review's scope limitations remain. The identified integration repairs are complete, and no unresolved blocker remains within that reviewed scope.
