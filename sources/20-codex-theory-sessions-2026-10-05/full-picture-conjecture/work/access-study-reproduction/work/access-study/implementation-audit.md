# Independent implementation audit: account access and correction

5 October 2026. Source reference read only. The independent oracle is `audit_oracle.py`; it neither imports the source workspace nor calls the new model's diagnostic or production functions. The implementation audit is complete for the checks specified below; no discrepancy was found.

## Inherited chronology verified from source

Inspected `/Users/ren/theories/experiments/recoverable-inquiry/model.py` as text. No imports or writes occurred there. The original stochastic chronology is:

1. At observed state `(remaining,stock,cash,ready,fault belief)`, choose drop, keep if already ready, or rebuild if unready. Pay readiness first.
2. A current diagnostic is permitted only after **keep** on already ready equipment. Rebuild buys next-period readiness; it does not restore current diagnosis.
3. Pay for the test before income. Select a repair prescription contingent on its observed result. Every resulting repair bill must be prefunded. Direct repair without testing remains available.
4. Score a repair's absent-target burden using the fault **before** repair; then repair resets the fault to absent and adds one in `x'=clip(x+1+repair−2D,0,3)`.
5. Draw damage from the effective post-repair fault state. Group latent paths with the same observed stock, because clipping can merge damage outcomes. Output is exactly `2x'` and is not a second independent signal.
6. Receive output only after bills; keep cash up to eight and record overflow. Filter the current effective fault from the public observation, then apply onset `.1` and clearance `.05` to obtain the next fault probability.
7. Stock zero is absorbing; it stops future decisions and output. At finite horizon end the original code resets irrelevant belief/readiness but keeps account balances.

The original single-account objective included negative output, terminal stock salvage, and a collapse penalty. The new four-dimensional outcome probes deliberately change that evaluation. Agreement of kernels does not imply agreement of the original optimum; the report must not treat the new optimum as a rerun of S06.

## Frozen extension choices checked

Read `PROTOCOL.md` after it appeared. The new treasury is unbounded over the finite horizon and all overflow is retained. Permission is observable and deterministic: barred, immediate, or unlock after one round. At living nonterminal states with immediate access, a free **round-start maximal transfer** fills cash to eight. There is no new diagnostic-contingent transfer stage. No terminal transfer occurs. The largest possible operating bill is six, below the cash cap.

These choices isolate account access. They do not model credit, strategic permission changes, legal legitimacy, or dynamic recognition. The maintained belief is free. The observation interface must include account/permission information but must not count deterministic cash/output duplicates as independent evidence.

The protocol lists **seven**, not six, support directions. Finite probes can demonstrate differing attainable sets, but equal probe values are not a complete Pareto-set equality test. The formal normalization result supplies the stronger equivalence claim where its assumptions hold. The all-liquid control is correctly marked as potentially different later if overflow becomes barred.

## Independent oracle and exact two-period witness

The oracle explicitly enumerates the latent starting fault, diagnostic outcome, repair, damage, and next-period fault; it then groups all latent paths by the complete public observation before forming the posterior. It independently enumerates legal prescriptions and solves the resulting finite policy tree with exact rational arithmetic. This implementation does not reuse either diagnostic/production helper.

At horizon two, stock two, unready equipment, certain current fault, and total cash five, compare:

- Low liquidity: accessible zero, barred treasury five.
- Higher liquidity: accessible one, barred treasury four.

Both have exactly the same sole first action: drop readiness, do not test, do not repair. The first transition gives stock one with probability `4/5` and stock three with probability `1/5`; observed output is respectively two or six. The next fault probability is `19/20` in both branches, since the initial fault was already known. Thus the stock-one branch has next-period damage probability `.1+.7(.95)=153/200`.

The low-liquidity state has cash two on that branch and cannot pay repair three. Its minimum collapse probability is `(4/5)(153/200)=153/250=.612`. The high-liquidity state has cash three, repairs on that branch, and attains zero collapse. This policy has expected expense `(4/5)3=12/5=2.4` and absent-target burden `(4/5)(1/20)=1/25=.04`. Terminal stock below two has probability `2/25=.08`, because the healthy damage chance can leave repaired stock at one. The distinction between failure and the separately supplied recovery criterion therefore remains visible.

With immediate maximal transfer both initial states normalize to identical cash five/treasury zero and have the same solution. The result is not merely a difference in programmed first-action availability: the initial action set and actual first action coincide, while an endogenous output receipt exposes a subsequent liquidity threshold. Removing output also removes this particular route to second-round affordable repair; that is a test of the mechanism, not a universal statement that production eliminates access problems.

Exact certificate: `audit_oracle_results.json`. The checked witness uses no sampling, floating optimum, or statistical significance claim. It was derived before the new model's main run and should be described as a preread analytical certificate, not held-out evidence.

## Independent implementation comparisons

The task-owned `model.py` was inspected directly. Its diagnostic and production helpers preserve the inherited chronology, while `normalize` and the extra treasury ledger implement the frozen extension. Every support action is prefunded; no next-period readiness is used early; repair burden refers to the pre-repair fault; posterior aging occurs after joint production filtering; output arrives after bills; terminal/failed states do not perform another transfer. The recurrence optimizes the declared linear probe with the specified tie order. Its selected-policy evaluation and account identities are exact fractions, not float values relabeled exact.

`audit_compare.py` imports only the task-owned module with bytecode writes disabled. Across **648 H1/H2 initial states** (stock1–3, cash0–5/total5, ready0/1, prior0/half/1, and all three access modes), all of the following passed:

- **4,536 independently optimized support values**, using a separately written exact finite policy-tree recursion and latent event generator.
- **4,536 complete selected-policy metric vectors**, independently evaluated from latent events while following the candidate policy.
- **2,359 exact branch-distribution/posterior comparisons**, **18,872 stage-metric comparisons**, and **5,304 branch ledgers** over **880** distinct reachable nodes.
- **4,536** exact expected terminal-account conservation identities.

The independent optimizer uses a different benign tie ordering; only its scalar minima are used to certify optimality. Full selected metric vectors are certified by independent evaluation of the candidate's stated policy, avoiding a false discrepancy between equally optimal policies. Results are retained in `audit_compare_results.json`.

`audit_controls.py` independently checks the three parameter-changing controls: output zero, onset and healthy damage zero, and completely uninformative diagnostics. Across **5,184 distinct normalized states**, **20,034 action kernels** and **42,300 branch masses** matched the explicit latent enumeration; **18,144** independently optimized H1 values also matched. This checks control transitions at H1/H2 and exact H1 optima. It does not independently solve every H4 control. Results: `audit_control_results.json`.

## Targeted independent H4 validation

After the main run reported its primary H4 cases, `audit_h4.py` independently solved **18** preidentified checks: stock2, certain starting fault, unready, total5; cash splits0/1/5; barred/immediate/delayed access; failure-only and mixed probes. Every exact support value matched. The independent four-coordinate vectors happened to agree in all these cases too; that agreement is not assumed for arbitrary objective ties. Results: `audit_h4_results.json`.

For failure-only optimization, the barred minima are:

| Initial accessible cash | Initial treasury | Minimum four-round collapse probability |
|---:|---:|---:|
| 0 | 5 | `153/250 = .612` |
| 1 | 4 | `17/1250 = .0136` |
| 5 | 0 | `0` |

Immediate and one-round-delayed access give zero for all three splits in this particular stock/prior case. Delayed access is not generally equivalent to immediate access; the main grid includes other situations with earlier binding bills.

The `.0136` obstruction has a concrete financing path. With probability `.8`, first-period damage leaves stock1 and cash3; a second-period repair can be paid. With probability `.1` that repair period still has healthy damage, leaving stock1 and cash2. Next-period fault probability is `.1` and damage probability `.17`; no repair can be paid then. This path contributes `.8·.1·.17=.0136`. An alternative policy could skip the earlier repair, but would create a greater failure probability. The independent optimization verifies that the displayed lower value is attainable and optimal under the declared feasible policies. It is a renewed cash threshold, not an observation gate.

The zero-output result was independently checked without any optimizer or belief-state calculation in `audit_no_output.py`. With barred liquid cash0/1 and unready equipment, no paid action ever becomes affordable. Direct propagation of the joint **true stock/true fault** law gives four-round failure **`1583669/2000000 = .7918345`** for both. This confirms removal of the particular cash0/cash1 distinction when earned output is removed. Results: `audit_no_output_results.json`.

## What these checks do and do not establish

The checks support kernel, posterior, ledger, finite policy, and selected numerical claims for this model. They do not independently recompute all **1,134** main H4 support results or all H4 control optima; those remain the main implementation's exact enumeration. They do independently validate the principal H4 numerical witness, all small-horizon support values, and the control kernels by distinct latent calculations. The formal immediate-normalization result is a separate proof obligation; numerical partition equality alone is not its proof.

`audit_summary.py` separately recomputed the report's aggregation from the saved exact main rows. It checked all **1,134** support-score and ledger identities, **378** access-order triples, and all six-partition groups. The split-sensitive counts are **24/63 barred**, **15/63 delayed**, and **0/63 immediate**, matching the main summary. There are **zero** selected optima with a positive test count. The saved model snapshot exactly matches the audited live model. This is an independent summary/consistency check, not a rerun of every optimum; results are retained in `audit_summary_results.json`.

No paid diagnostic is used by the selected main-grid optima, according to the main result. Consequently this study should claim an account-access/repair-financing result, not demonstrate the value of paid inquiry, recognition, or institution formation. Diagnostic kernel correctness remains verified because the independent audit includes ready states and actions that use it; availability in the model is not evidence that the chosen optimum needed it.

The full four-dimensional outcome comparison is deliberately not a moral optimum. Expected expense, the limited absent-target burden, terminal stock threshold, and collapse probability remain distinct. A zero failure optimum can still have positive probability of ending at stock1, positive burden, and opportunity costs. Equal initial funds do not match realized expense across the barred and accessible models.

Audited candidate model SHA-256: `051976c28e15a06bbed3be9c95328755bcbf676dfe30440c03a3e0684d000135`.

Audited protocol SHA-256: `076420c06d25f634266da8bcf8d60a6b0689f3032e5afc076784ff4ed42154cb`.

Each results file records scope and relevant hashes. No source-reference files were imported or modified. All additional scripts and results live in this task's `work/access-study/` directory. No numerical or logical inconsistency was found in the audited implementation.
