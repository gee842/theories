# Reliable updating through bounded change / 有界变化中的可靠更新

8 October 2026. AI-authored theoretical continuation of Ren’s “继续”, under the [prospective scope](EVOLUTION-DRIFT-MARGINS-PROTOCOL.md). **42 new Lean theorems / 56 new declaration audits pass; the 251 unchanged predecessor audits are separately rebuilt (307 total).**

**中文结果：**参考取得后，传递关系不必完全不变。逐步变化界与读数噪声界可以推出当前误差范围；整个范围处于成功侧才确认成功，处于失败侧才确认失败，横跨边界则保留不确定。再从原有网络本身推出反应余量，便能证明：在明确的参考年龄范围内，第一次失败仍触发实际修复，随后任意有限的两类任务保持已修复网络。可靠性因而是参考、变化速度、辨别余量和后续行动之间的有条件关系，不是一次校准之后永久获得的属性。

## The precise connection

The [reference-renewal predecessor](EVOLUTION-CALIBRATION-RENEWAL.md) permitted arbitrary changes between finite blocks but used the same channel for reference acquisition and every task within a block. This study removes that identical-channel requirement during use. It does not remove coherent initial acquisition, an affine response class or the need for warranted bounds.

Records, transmission, network response and subsequent updating are differentiated relations within the same activity. The mathematical distinction between actual response and acquired reading preserves how one affects the other and how the resulting record affects the retained matrix. It introduces no fundamentally separate knower/world pair. A rate supplied to this local model is not thereby external to generative reality; this particular construction has not derived that rate or its warranted adoption.

The governing derivation advanced here is **acquired discrimination → reliable control of learning despite continuing relational change**. This is an implementation connection relevant to selection-rule revision. It does not supply an ethical warrant for the selected tasks or replace the completed G0/J route.

## From actual changes to an error enclosure

For one coordinate, let the channel at reference age \(n\) be

\[
r_n(p)=g_np+b_n,
\qquad y_n=r_n(p)+\eta_n.
\]

Age counts successive changes in this execution; it is not automatically physical time. At age zero, coherently acquire exact reference values \(z=r_0(0)\) and \(o=r_0(1)\), with \(g_0\ne0\). The decoder uses those retained values and the current reading:

\[
\widehat p_n=\frac{y_n-z}{o-z}.
\]

The reader need not be given current gain, bias, true response or true noise separately. These appear in the correspondence proof. The supplied envelope parameters used by the guard must still be applicable to the actual history.

Assume, at each successive step,

\[
|g_{k+1}-g_k|\le a,\qquad
|b_{k+1}-b_k|\le b,\qquad
|\eta_n|\le\varepsilon,
\qquad |p|\le1.
\]

`successive_change_bound` derives accumulated deviations; `decoded_error` and `aged_decoding_bound` then establish

\[
\widehat p_n-p
=\frac{(g_n-g_0)p+(b_n-b_0)+\eta_n}{g_0},
\qquad
|\widehat p_n-p|\le R_n
:=\frac{n(a+b)+\varepsilon}{|g_0|}.
\]

Rates are nonnegative in the history theorem. No stochastic independence, averaging or favorable cancellation is required. For a target coordinate \(s\in\{-1,1\}\), the actual signed response is \(m=sp\), its estimate is \(\widehat m=s\widehat p\), and the same error bound holds. The tanh network supplies \(|p|<1\); it is not an unverified amplitude bound on a different organism or device.

Initial reference readings here are exact and correctly bound. Noise bounds concern subsequent readings. Mixed-time or noisy initial references would require another denominator/error derivation; this result does not quietly absorb them into \(\varepsilon\). Gains after acquisition may change or even vanish, but an informative decision still needs the stated separation. A collapsed live channel cannot obtain a useful guarantee merely by being included in the syntax.

## Three decisions, with exact interval meaning

The scalar gate operates on an estimate and its nonnegative enclosure radius:

| Available interval | Report | Justified conclusion |
|---|---|---|
| \(\widehat m-R>0\) | Success | Every compatible response is strictly positive. |
| \(\widehat m+R\le0\) | Failure | Every compatible response is nonpositive. |
| Otherwise | Unresolved | The interval contains both a positive and a nonpositive response. |

`positive_interval_exact` and `negative_interval_exact` prove the first two equivalences for the scalar interval. `unresolved_contains_opposites` supplies actual endpoint witnesses in the third case. Zero belongs to failure because the inherited recall criterion is strict positivity. These are claims about all values in the declared interval, not proof that every endpoint is realized by this particular network or jointly attainable across coordinates.

For three coordinates, all must certify success to report complete recall; any certified failure suffices to report failure; the remaining cases stay unresolved. `report_positive` and `report_negative` connect these reports to actual responses whenever the enclosure contains them.

The functional extension `guardedUpdate` learns only after certified failure. Success and unresolved reports retain the current matrix. This differs from the earlier apparatus’s default handling of missing evidence. The new division, interval comparison and three-way gate are specified operations, not an already constructed material extension with a checked assembly/support tariff.

The condition

\[
2R<|m|
\]

is sufficient to guarantee that **every estimate obeying the error bound** produces the correct definite scalar verdict. The factor two covers both displacement of the estimate and the gate’s requirement that its entire interval lie on one side. It is not needed for the soundness of a certificate already obtained, nor claimed necessary for a particular reading. When separation fails, a reading can still be conclusive; it is the uniform guarantee that may be unavailable.

## The margin comes from the retained network

Keep the preceding two profiles \(A=(1,1,1)\), \(C=(1,1,-1)\) and matrix family \(B(u,v)=uAA^T+vCC^T\). The inherited native response is one tanh step. No new success table replaces it.

At the overwritten matrix \(B(1,4)\), the input fields for \(A\) are \((7,7,-1)\); the third coordinate really fails. After the inherited learning update, the matrix is \(B(2,4)\). Its input fields are \((10,10,2)\) for \(A\) and \((14,14,-10)\) for \(C\). The signs agree with each respective target. `field_gives_margin`, `overwritten_margin` and `repaired_margin` derive a common positive absolute margin

\[
\mu=\tanh(1)>0
\]

from these fields and tanh monotonicity. It is a sufficient common lower bound; no optimal capacity or margin claim is made.

`actual_aged_errors` composes the acquired decoder with the actual native responses. `native_step_exact` proves correspondence between the guarded update and the earlier responsive updater when each coordinate satisfies the error and separation conditions. Thus `bounded_drift_repairs` establishes an actual first update from \(B(1,4)\) to \(B(2,4)\), without resetting the matrix or retrospectively calling the first failed task successful. `bounded_drift_preserves` establishes that later \(A\) or \(C\) responses retain the repaired matrix under the same bound.

`repair_then_retained_history` proves the connected history: choose a finite horizon \(H\) with \(2R_{H,i}<\mu\) for every coordinate. Start at age \(n\) with the overwritten matrix, perform \(A\), and follow any finite list of \(A/C\) tasks, with \(n+\text{list length}\le H\), counting the first \(A\) in that length. Nonnegative rates make earlier radii no larger than the horizon radius. The first step repairs; every subsequent step retains \(B(2,4)\). All task ages are strictly before the stated endpoint, so using \(R_H\) is conservative.

The theorem tracks the matrix and the actual observation/update function over this finite history. It does not add resource counters to that function. Earlier inspection and operational support accounts remain valid in their own models; a new physical finite-energy execution or new cost advantage requires a compatible implementation of this gate. Arbitrarily long finite lists are not an infinite-lifetime claim with fixed nonzero rates and a fixed horizon.

## A sufficient assurance window and a residual floor

When \(a+b>0\), `assurance_window` proves the exact algebraic equivalence

\[
2R_n<\mu
\quad\Longleftrightarrow\quad
n<\frac{|g_0|\mu/2-\varepsilon}{a+b}.
\]

This solves the sufficient separation condition, not the device’s maximum actual lifetime or an optimal reinspection schedule. A negative or zero right-hand side gives no nonnegative admissible age under this strict condition. When both rates vanish, the general radius formula still applies and only the noise term remains; the divided-rate expression is deliberately not used.

`residual_noise_floor` gives \(R_n\ge\varepsilon/|g_0|\). Refreshing coherent references may reset accumulated age but does not by itself remove subsequent reading noise. Consequently repeated calibration alone need not restore the uniform guarantee. Better reading precision, larger response margins or a revised operation can matter; their availability and costs are not inferred from this inequality.

## Substantive counterreview and retained failures

**An underestimated bound can confidently report the wrong answer.** `understated_bound_false_success` uses identity reference records, an actual live bias of \(1/2\), and an actual response \(-1/4\). The acquired value becomes \(+1/4\). Declaring radius \(1/8\) yields certified success even though the response fails; the true error is \(1/2\), outside that radius. This preserves an actual changed response relation, not a freely toggled correctness predicate. Calibration alone has not warranted the supplied envelope.

**Uncertainty can retain real damage.** `wide_bound_withholds` proves that a radius of one, even with an exact estimate of this tanh response, leaves every coordinate unresolved. `uncertainty_can_retain_failure` applies that rule to \(B(1,4)\): no update occurs and the first memory still fails. The enclosure is valid but too broad. Withholding a weight change is therefore distinct from harmless delay, actual maintenance or successful correction.

**A certified failure is not a universal license for a learning rule.** The gate establishes the present task’s failure. It does not prove that the selected Hebbian update improves every other capacity. The old interference counterexamples remain. Preservation of both stated memories follows here from their particular post-repair matrix and margins, not from failure certification alone.

**The rate and noise limits are not learned by this theorem.** They constrain actual successive channels and readings. A mistaken limit breaks inclusion; a valid but loose limit can block action. Forming, maintaining or justifying such a limit is a specific unresolved premise of this interface, not evidence that the whole relational theory lacks observation or learning.

**The result is local theoretical progress.** It relaxes exact constancy to quantified departure and derives its native consequence. It does not establish biological population convergence, superiority to every evolutionary theory, normative necessity or the inevitable evolution of careful self-revision. No new empirical gate is imposed on this completed theoretical connection.

## Credit, primary comparison and what follows

[Timed feedback](TIMED-FEEDBACK-INTEGRATION.md) already composes calibration with supplied drift and a derived age upper bound. [Fallible inspection](FALLIBLE-INSPECTION-INTEGRATION.md) already retains compatible alternatives and certifies consequences only when the relevant admitted cases agree. Their results, including source-order and actual-inclusion qualifications, are completed resources. The present addition is the explicit affine decoder error, native tanh margin, three-way updater and retained-memory history at their intersection. Their clocks, physical meanings and support tariffs are not silently transferred to this network.

Guard bands are also established measurement practice. JCGM 106:2012, §§8.3.1–8.3.3, discusses shifting acceptance limits to manage mistaken decisions and distinguishes guarded acceptance and rejection. Its probabilistic coverage treatment is not a deterministic enclosure containing every possible actual value. Our proof uses a hard bound as a premise and does not turn a stated coverage probability into certainty. [Official primary text](https://www.bipm.org/documents/20126/2071204/JCGM_106_2012_E.pdf). The [reading record](../../../../sources/evolutionary-selection/comparative-direction/README.md#bounded-drift-and-margin-continuation) preserves the inspected scope; no new invention of guard bands is claimed.

The selected within-block departure connection is complete at the stated conditional scope. The next precise connection is **how an applicable change/noise envelope is formed or maintained, and how its loss of decisiveness initiates supported renewed inquiry**. The present formula supplies a criterion; it does not yet construct that inquiry policy, show its cost is worthwhile, or ensure that delaying a task is bearable. Reuse existing protected execution, acquired monitoring and inquiry-selection results through the explicit correspondence needed here. This is a candidate next study, not a retroactive condition for crediting the present theorem.

## Proof and integration record

[DriftMargins.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/DriftMargins.lean) · [fresh checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/check_drift_margins.py) · [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/drift-margins-verification.json). All 42 new theorems and 14 other explicit declarations pass (56 new audits; 307 total with predecessors).

The five predecessor modules and their 251 explicit-declaration audits remain separately credited. The fresh checker rebuilds the six-module repository closure with Lean 4.30.0-rc2 and pinned Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`; Mathlib itself uses the existing pinned cache. It rejects warnings, proof holes, custom axioms and unsafe shortcuts, audits explicit declarations and records source/compiler/import/log hashes. Generated declarations are kernel-checked; standard logical dependencies are disclosed. [Documentary checks](EVOLUTION-DRIFT-MARGINS-CHECKS.json) separately verify links, preservation, proof bindings and the owned paired C14 integration. The counterreview above is by the author, with no claim of independent-agent acceptance or a repository-wide freshness audit.
