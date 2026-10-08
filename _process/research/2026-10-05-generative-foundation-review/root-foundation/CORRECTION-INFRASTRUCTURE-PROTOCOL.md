# Correction infrastructure: pre-execution comparison protocol

8 October 2026. AI-authored implementation of Ren's instruction “formalize, till frontier contribution appears”. This protocol is written before the exhaustive comparison is executed. It fixes a bounded study, not the whole research goal's completion threshold.

## Target and credit

Test the composition of an acceptance incentive with preservation of effective correction opportunities when base actions change those opportunities. Reuse completed G0/J practical principles and connected goal revision; do not relabel those studies as unfinished. Mathematical targets are the acceptance/access separation, the cost of access preservation, and finite-horizon composition with values recalculated inside the permitted domain. Dynamic programming, safety shielding and observational uniformity are established machinery, not inventions of this study.

State, action, observation and correction are differentiated roles in one evolving installation. The model's safe-state classification is supplied and fixed for each run; it stands for independently specified effective correction access. No observed behavior, ethical derivation or field deployment is inferred from this classification.

## Exhaustive model family

Three states, two base actions, deterministic transitions, two states classified as having correction access and one without it. The inaccessible state is absorbing. Enumerate all 3^4 transition tables from the two accessible states and all 2^4 reward tables with accessible-state rewards in {0, 2}; rewards in the absorbing state are zero. Total: 1,296 models. Examine both accessible initial states and horizons 1 through 5: 12,960 model/start/horizon cases. Both acceptance decisions are available with bonus 1. Values are exact integers, not learned estimates. Dead ends of the correction-preserving action set are reported as infeasible, not silently given zero reward.

Compare four policies under identical transition, reward, state access and horizon information:

1. **Acceptance transformation alone:** maximize unrestricted finite-horizon base values and add the constant bonus for accepting; ties use base action 0.
2. **Filter with stale values:** admit only actions having a safe continuation over the remaining horizon, but rank them by unrestricted values. Recompute the safe set at each step.
3. **Recomputed composition:** optimize values computed within the safe continuation domain, then apply the acceptance bonus.
4. **Conventional constrained planner:** obtain the best safe action sequence by exhaustive enumeration, without the acceptance transformation. It is the strong reference, not an intentionally weak comparator.

Record feasibility, acceptance-bit compliance, every realized prefix's access, realized base return, constrained-optimum regret and the first complete counterexample for each failed stronger claim. Count accepting bits only at executed decisions. No safe action must not count as successful corrigibility. Evaluate all ties separately for the one-step acceptance/access theorem; the deterministic tie rule above is only for trajectory comparisons.

## Additional exact controls

Maintenance costs {0,1,2,4,8,16}; acceptance bonuses {1,3,17}; a separate access bonus {0,1,4,16}. Report all optimal action/acceptance pairs and the strict threshold cost < access bonus, including the unsafe equality tie. Test the formal two-stage trap (temptation 3, 5 or 9; safe branch returns 2 and the safe continuation of the tempting branch returns 1). Check hidden-state repair with indistinguishable versus distinguishing observations. Compare channel-replacement traces with a temporary gap and overlapping handoff. These controls are constructed model checks, not AI evaluations.

## Decision criteria and scope

If recomputed composition differs from the exhaustive constrained optimum or loses access on a feasible case, repair or reject the implementation; Lean checking alone cannot excuse a correspondence error. If a conventional planner matches, credit the match. Evidence of an advantage over acceptance alone and stale-value filtering establishes the need for the added specification or recomputation in this family, not superiority to shielding or a learned-agent deployment result.

The candidate contribution is a precisely scoped boundary and composition result connected to a current corrigibility transformation. Global priority remains unestablished. Primary-source comparison must preserve existing access, oversight and institutional corrigibility work, and must distinguish our stronger operational requirement from any paper's own definition. All new proof claims require actual Lean checking and dependency audits. No external agent review is claimed without one.
