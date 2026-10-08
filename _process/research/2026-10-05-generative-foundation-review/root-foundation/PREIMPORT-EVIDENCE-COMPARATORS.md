# Pre-import evidence and control-system safety comparators

AI-authored primary-source audit, 6 October 2026. Named connection: **paid access to independently retained evidence, before a proposed reason overwrites controller memory → justified action selection → actual recipient consequence**. It extends [semantic calibration](../../../../theories/becoming/chapters/SEMANTIC-CALIBRATION.md), within [generative grounding](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md). It does not repeat the earlier [measurement-tampering and explanation comparisons](SEMANTIC-CALIBRATION-SOURCES.md).

**Finding:** runtime assurance and predictive safety filtering already implement a strong comparator: evaluate proposed commands against a separate model and current state before allowing or replacing actuation. The closest contribution of our present bridge is therefore its explicitly acquired, paid and correctly bound evidence history, together with preserving that history across import. Screening commands before action is not novel by itself. The cited implementations do not establish that our particular physical mechanism works.

## Primary implemented comparisons

### Predictive safety filtering on a physical racing vehicle

Tearle, Wabersich, Carron and Zeilinger (2021), [*A predictive safety filter for learning-based racing control*](https://arxiv.org/html/2102.11907v1), provides the strongest physical comparator inspected. An MPC filter evaluates a requested input against a current state estimate and a backup trajectory ending in an invariant terminal set; it modifies the input before actuation. The implementation uses a 1:28 RC car, VICON position/orientation, an extended Kalman state estimator, an 80 Hz loop and radio commands. Both human commands and a neural imitation policy are evaluated.

Crucial scope restrictions are explicit: the implementation softens track and terminal constraints; terminal invariance is established for constant-curvature segments and does not strictly extend to instantaneous segment changes. Its nonlinear verification is attempted from 1,000 random initializations. Successful physical demonstrations therefore do not convert every stated nominal condition into an exhaustive deployment guarantee. The inspected account does not establish bounded sensor age or arbitrary estimator-fault tolerance. Relevant sections: II–III, V-B and VI. These observations concern the reported implementation; no experiment or code was rerun here.

### Neural Simplex: reject an unrecoverable proposal before executing it

Phan, Grosu, Jansen, Paoletti, Smolka and Stoller (2020), [*Neural Simplex Architecture*](https://www3.cs.stonybrook.edu/~stoller/papers/nfm2020.pdf), separates neural proposals, a certified baseline controller and a decision module. A proposal that would leave the baseline controller's recoverable region triggers takeover. The neural controller can train in shadow mode while the baseline controls the plant, and later regain control under a reverse-switching condition.

In the rover case, the checker predicts a proposed action one time step ahead and checks braking recoverability using distance readings. Its contract supplies bounds on obstacle intrusion between sensor directions, maximum acceleration and geometry; the reported control step is 0.1 seconds. These assumptions are materially stronger than “two controllers agree.” The case studies are computational demonstrations, not a new physical validation of our mechanism. Relevant sections: 2–3 and 5.2. A proposal's hypothetical predicted successor is also kept distinct from the actual successor produced by the executed baseline command; this distinction is useful for avoiding fabricated action receipts.

### ULGEN: implementing the check/use order matters

Yalcinkaya, Torfah, Desai and Seshia (2023), [*ULGEN: A Runtime Assurance Framework for Programming Safe Cyber–Physical Systems*](https://beyazit-y.github.io/files/tcad23.pdf), DOI `10.1109/TCAD.2023.3246386`, is a particularly close implementation comparator for ordering. Its paper is CC BY 4.0. The framework supports event-driven and time-driven controllers, decision modules and priority-based communication. A decision module's execution schedule is tied to controller executions, with developer-selected decision frequencies and operating regions.

Section IV makes event dequeue, event handling and controller execution one atomic operation with respect to other machines, replacing separate operations that could interleave. In the authors' simple braking comparison (§V-A), their two-thread SOTER implementation violates the requirement in 82 of 100 simulator runs, while their two-thread ULGEN implementation has no violations in those 100 runs. That is a reported, bounded comparison of those implementations and schedules, not a universal failure rate for Simplex or every SOTER system. It supplies concrete evidence that a correct-looking architectural diagram can lose its guarantee through execution ordering.

The same paper states that OS timers in its backend are not reliable for hard real-time systems. Its compiler does not establish all required well-formedness properties: the programmer must supply important controller-region and switching obligations. The formal safety result starts inside a declared operating region. Its compositional account requires disjoint machine variables; the interpretation of those variables as physical state still needs a valid interface to the plant. The Kobuki physical demonstration (§VII-A) evaluates a specified trajectory bound under an obstacle-free-environment assumption; the later exploration case changes that setup explicitly.

The authors' [public repository](https://github.com/BerkeleyLearnVerify/ULGEN) lists the modified compiler, runtime-related material, case-study code, reproduction instructions and videos. The repository landing documentation was inspected; the framework was not built or executed here. Relevant paper sections inspected: II–IV, V-A and VII-A/B. This is stronger than citing a conceptual proposal, but remains external reported evidence.

## Explicit sensing, timing and model boundaries

Desai, Ghosh, Seshia, Shankar and Tiwari, [*SOTER: A Runtime Assurance Framework for Programming Safe Robotics Systems*](https://arxiv.org/html/1808.07921), explicitly assumes that trusted state estimators report state accurately within bounds. Its decision module uses a `2Δ` reachability lookahead so the safe controller can run before the safety boundary is crossed; the theorem also supplies well-formedness and an initially valid invariant. Its formal presentation abstracts communication buffers into topic values. Relevant sections: II-A and III–IV. This makes “current state” and available reaction time visible assumptions, rather than evidence of immunity to stale or corrupted sensors. The later ULGEN comparison above is relevant to the implementation gap and should accompany claims about timing guarantees.

Wabersich and Zeilinger, [*Predictive control barrier functions: Enhanced safety mechanisms for learning-based control*](https://arxiv.org/html/2105.10241v3), explicitly examines model deviations and unexpected disturbances that can make predictive safety filters infeasible. It develops an auxiliary softened problem and a recovery mechanism, evaluated numerically. Its contract still depends on model/control-barrier assumptions; recovering a feasible region after a violation is a different claim from never violating a constraint. Relevant sections: I–III and V. The paper helps prevent treating a fallback label or a feasible softened optimization as proof that the original hard requirement was preserved.

The non-licensed-paper summaries above are each below 200 words. The sections that follow are our proposed interface requirements and counterexamples, not empirical findings attributed to those papers.

## What independence and freshness must mean in our bridge

Three different properties should not be collapsed:

1. **Separate computation:** the monitor uses a different algorithm from the proposed controller. This alone leaves both dependent on the same false observation.
2. **Protected evidence provenance:** the incoming reason cannot rewrite the evidence against which it is being checked. This is the property the pre-import interface needs for its declared archive-corruption intervention. It does not require statistical independence between memories of the same event.
3. **Current applicability:** the acquired evidence still constrains the recipient relation at the moment the command takes effect. Neither a recent check of old memory nor a matching context label establishes this property by itself.

The control-system analogue of the self-import error would be accepting a proposed command's claimed state as the monitor's state, then showing that the command is safe in that claimed state. Different code paths would not rescue that circular evidence flow. The runtime monitor should consume a protected evidence snapshot or an independently maintained estimator whose updates have their own warranted acquisition route.

A minimal interface can be stated without equating a stored bit with truth. Let `K(e,t)` be the set of physical situations consistent with acquired evidence `e`, its scope, uncertainty and permitted evolution through action time `t`. Let `P(w,u)` be the declared action requirement in situation `w`. A checker might authorize `u` only if `P(w,u)` holds for every `w` in `K(e,t)`. Conditional correctness then additionally requires that the actual situation belongs to `K(e,t)`, and that the checked command is the one executed on the intended target.

This is an analyst's contract proposal, not an implemented result. In the repository's binary construction, a faithful qualified command plus a stable recipient law can make the relevant candidate set a singleton. With an undetected relation change, the old singleton can be wrong. Honest uncertainty may instead require both relations to remain possible; if no command satisfies both, a sound checker cannot manufacture a uniquely warranted command from agreement alone.

Clock age and content stability also differ. Recent evidence can be wrong through a common sensor fault; older evidence can remain sound under a genuinely unchanged relation. A freshness contract therefore needs both a warranted acquisition time/history and a bound or mechanism for relevant change. A controller read paid just before action is fresh access to a record, not necessarily a new observation of the recipient.

## Concrete test requirements for the next paid construction

| Intervention or boundary | What the new implementation must expose |
|---|---|
| Incoming archive tag alone is corrupted | Read the actual acquired controller before any import; compare correctly bound fields; preserve the source of disagreement. |
| Reason command and acquired controller share corruption | Preserve the possibility of matching but false evidence. A monitor that passes it has not independently identified the world. |
| Correct new reason conflicts with stale memory | Do not turn prior qualification into unconditional veto. Investigating or acquiring current evidence needs a specified permitted action and cost. |
| The relation changes between checking and execution | Show the permitted transition, revalidation or conservative validity window. An atomic software step does not freeze the external recipient. |
| Read succeeds but import or actuation cannot be paid | Record partial paid progress and retained evidence; neither create free fuel nor infer an executed action from an admitted command. |
| Command is checked for one target but routed to another | Bind the evidence, decision and actual recipient throughout; correct inference does not repair a wrong actuator route. |
| Checker misses its deadline or cannot establish a result | Supply a physically meaningful fallback with its own applicability and budget. “No action” is not universally safe if support is time-critical. |

The strongest ordinary comparator is a direct read of the same qualified pre-import register followed by a conventional scoped safety check and the same paid execution path. A second comparator can use current reacquisition and a predictive uncertainty set when the declared law makes that information accessible. Comparisons must equalize observation access and account for acquisition, computation, storage and actuation; these control papers do not supply the repository's material account for us.

Track actual harmful commands, beneficial-command coverage, unanswered disagreements, missed beneficial opportunities, delayed execution and total resource use. Refusing every command can prevent a narrow class of executed errors while defeating the required recipient-support objective. Conversely, matching useful delivery in the nominal case cannot establish resistance to shared corruption or change.

## Contribution and remaining premises

These comparisons strengthen the connected account by specifying which parts must be real: acquired evidence, an ordering that preserves it during assessment, a valid interval through actuation, and an effective intervention path. They also block a novelty claim for screening commands or a sufficiency claim for internal agreement.

The invariant or safe set, its grounding in affected conditions, the choice of protected recipients, authority to intervene and treatment of conflicting futures remain supplied or unresolved. Keeping a car inside a track is a declared engineering property; it does not derive a universal ethics. In our construction, a correct command for the supplied objective `G` likewise does not explain why that objective deserves authority. The cited work provides implemented comparators and failure boundaries, not empirical validation of our complete mechanism or a completed alignment/governance solution.
