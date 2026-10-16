# Actual predictor cycles as a paid macro learner

6 October 2026. AI-authored mathematical companion to [Prediction protocol](../../../../theories/becoming/history/PREDICTION-PROTOCOL.md). This instantiates the earlier [protocol interface](PROTOCOL-COMPOSITION-MATH.md) using the existing [predictor law](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/formal/PredictionAction.lean); it does not introduce a replacement learner.

## 1. State, boundary and permitted events

The inherited state contains usable fuel \(F\), source-packet count \(H\), circuit lease \(\ell\), updater lease \(J\), last executed action \(b\), hidden regime \(z\), installed updater \(u\), score \(q\), transient receipt and phase. Other physical fields are retained unchanged by a trial. The score invariant is \(q\le4\). A boundary is exactly

\[
B(s)\iff \operatorname{phase}(s)=\mathrm{ready}\ \land\ q(s)\le4.
\]

The original command is

\[
A(q,b)=
\begin{cases}
0,&q<2,\\
b,&q=2,\\
1,&q>2.
\end{cases}
\]

`trialProtocol` permits rent and work only when the committed action equals the current command. It permits write and finish only when that action equals the physically stored executed selector. Updater formation and regime reversal are not permitted trial events. This uses the existing `Protocol` and `BlockPath` definitions: every permitted edge must also be a legal edge of the original predictor process, and a completed block is a nonempty first return to the declared boundary.

The phase law forces

\[
\mathrm{ready}\xrightarrow{\mathrm{rent}}\mathrm{rented}
\xrightarrow{\mathrm{work}}\mathrm{observed}
\xrightarrow{\mathrm{write}}\mathrm{written}
\xrightarrow{\mathrm{finish}}\mathrm{ready}.
\]

`blockPath_iff_cycle` establishes that every completed block from a boundary has exactly this event word, the initial circuit command, all four original guards at their actual intermediate states, and the original four-event endpoint. Conversely those guards and command produce such a block. The bounded-score invariant ensures that finish returns to a boundary even after an update. It does not require that the leases remain positive after finish.

## 2. Independent arithmetic specification

Let \(r\) be rent, \(c\) the work charge, \(w\) writing cost, \(v\) a source packet's energy, and \(m\) the sum of both renewal charges. Let \(L\) and \(K\) be the circuit and updater renewal lifetimes. The trial's physical receipt is

\[
y=\operatorname{receiptOf}(a,z,\mathrm{true})=[a=z].
\]

This equation specifies the noiseless *plant response*. It is not an input by which the controller reads the hidden regime. The write's target is decoded from the executed action and receipt:

\[
d=\operatorname{decode}(a,y)=\begin{cases}a,&y=1,\\\neg a,&y=0.\end{cases}
\]

Use natural-number truncated subtraction exactly as the implementation does, and retain its evaluation order. Define post-work fuel

\[
F_*=
\begin{cases}
((F\mathbin{-}r)\mathbin{-}c)+v\mathbin{-}m,&y=1,\\
(F\mathbin{-}r)\mathbin{-}c,&y=0.
\end{cases}
\]

The independent `macroGuard` is

\[
\mathrm{phase}=\mathrm{ready},\qquad
\ell>0,\quad J>0,\quad H>0,\quad r+c\le F,\quad w\le F_*.
\]

At a boundary, the score bound is already supplied by its type. The `macroEnd` equations are

\[
F'=F_*-w,\quad H'=H-1,\quad b'=a,\quad
q'=U(u,q,d),
\]

\[
\ell'=\begin{cases}L,&y=1,\\\ell-1,&y=0,\end{cases}
\qquad
J'=\begin{cases}K,&y=1,\\J-1,&y=0.\end{cases}
\]

Phase returns to ready and receipt becomes false; the updater and remaining physical fields are unchanged. Here

\[
U(\mathrm{Fast},q,d)=\begin{cases}4,&d=1,\\0,&d=0,\end{cases}
\qquad
U(\mathrm{Slow},q,d)=\begin{cases}\min(4,q+1),&d=1,\\q-1,&d=0.\end{cases}
\]

The macro step requires \(a=A(q,b)\), `macroGuard`, and exactly this endpoint. Neither its guard nor endpoint is defined using the existence of a physical block. `cycle_enabled_iff_macroGuard` and `cycle_end_eq_macroEnd` prove equivalence to the original sequential implementation. `macro_step_iff_completed` then establishes exact correspondence with completed protocol blocks.

Its state type remains the full physical boundary subtype. This is an exact contraction of events, not a smaller-state quotient or a derivation of the memory encoding. The concrete command and update equations already define the controlled operation. The proof instantiates the generic block/report realization theorems; it does not instantiate `closedLoop` with a separately declared `Controller` or claim that another concern learner has been implemented.

The guards preserve sequential liquidity. A return can pay writing after work, but cannot pay rent or work before it arrives. A single net-energy inequality would be too weak; requiring rent, work and writing all before a successful return would be too strong.

Because \(F_*\) depends on the realized plant response, `macroGuard` characterizes completed-trial feasibility. It is not a pretrial decision procedure given to the controller. A real rent/work prefix can begin when the full macro guard is false and then fail to finish. The macro law does not give the circuit foreknowledge to avoid those branches.

## 3. Recovering the actual consumed observation

Finish clears the receipt. The endpoint receipt therefore cannot serve as a report of the earlier action outcome. Instead use the theorem

\[
q\le4\Longrightarrow U(u,q,0)\ne U(u,q,1)
\]

for both installed rules. On a completed trial, define

\[
\widehat d=[q'=U(u,q,1)],\qquad
\widehat y=[\widehat d=a].
\]

The observation companion proves, in order:

1. The final score equals the update applied to the actual intermediate `label`.
2. \(\widehat d\) equals that consumed label under the score bound.
3. \(\widehat y\) equals the actual intermediate receipt, using the executed action.
4. The reconstruction function is unchanged by modifying the hidden regime in either endpoint.

The general algebraic identity for `cycleEnd` does not assert executability by itself. The reported-process theorem uses it only on a separately proved completed block. The arithmetic reported macro law retains the action, explicit guards and endpoint, with an observation equal to the actual receipt. It has exactly the same finite labeled histories as the generic `reportedProcess` instantiated by this boundary-pair reconstruction.

This reporting convention is semantic: the before/after pair is available to the trace description. It does not mean both scores coexist in a final physical register or that a downstream runtime observer receives the receipt for free. A physical recipient needs its own evidence path. It is also distinct from target correctness: \(d=z\) uses the original noiseless complementary plant, while outages can invalidate that inference even when receipt recovery is exact.

The counterexample at \(q=5\), Slow, has \(U(u,5,0)=U(u,5,1)=4\). It refutes extending this decoder beyond the stated invariant. It is not a reachable counterexample from the parent model's retrofit with \(q=2\).

## 4. Finite histories and accounts

`macro_trace_iff_realization` gives, for any actual initial and final boundary and finite action word, an exact equivalence between a macro trace and a concatenated physical realization. `realization_event_count` proves that \(n\) completed trials contain exactly \(4n\) micro-events. This is an event count, not a time or scheduling bound.

`realization_source_consumption` gives the independent source equation \(H(t)+n=H(s)\), including failed returns in completed trials. Thus even a trial whose fuel balance rises consumes one of the actual finite packets. The law supplies no source replenishment between these trials.

The corresponding reported theorem gives an actual realization for each action/receipt word. The score, last action, updater, fuel, source and leases are fields of those actual boundaries; an induction does not choose a new initial reserve or update architecture for each trial.

Under the inherited `UpdaterFormation.Admissible` premise, `realized_energy_material` transports the original exact energy ledger:

\[
E(t)+\operatorname{spentAlong}(s,\sigma)=E(s),
\]

with the original unchanged material count. `spentAlong` includes unsuccessful packet waste as well as declared expenditure. `realized_prefix_ledger` gives both ledger equalities at every actual cut \(\sigma=\alpha\beta\), including cuts inside a trial. Its intermediate state is the actual endpoint of \(\alpha\), not a separately funded restart.

The parent law also represents failed prefixes that never finish. Those are preserved explicitly in the observation companion. The macro equivalence quantifies over completed histories and cannot by itself establish their probability, prevalence, completion or representativeness. No repeated completed trial hides a paid abort before it.

## 5. Checked obstructions and useful edge cases

The primary law has \(r=1,c=3,w=1,v=10,m=2\). The examples check a three-unit state that can pay rent but cannot start correct work, and a four-unit state that performs wrong work but cannot write its acquired failure evidence. Each resulting intermediate state has no enabled event in this declared deterministic payable-write law. That statement is scoped to this law, rather than a claim that physical rescue is impossible in every extension.

A four-unit correct trial checks that real capture can fund the later write. A completed failed trial can consume the last updater lease unit and block the next trial despite retained memory and remaining resources. A corrected score can change the next command while the stored executed action still permits finish. These are checks of the actual parent's state transitions, not a second favorable example process.

## 6. Derivation boundary and reproducibility

The new sources are [PredictionProtocolBridge.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolBridge.lean) and [PredictionProtocolObservation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolObservation.lean). The [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/check_prediction_protocol.py) freezes their canonical dependency sources, compiles in a fresh temporary directory with Lean 4.29.1, audits every new theorem's axiom dependencies and checks that sources did not change during the build.

The [saved audit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/prediction-protocol-audit.txt) passes all twelve modules and **38 new theorem audits**: fifteen bridge and twenty-three observation/failure results. Nineteen new declarations have empty axiom dependencies; the rest use only `propext` and/or `Quot.sound`. Predecessor audits separately disclose `Classical.choice` where used. The record includes checker, compiler, toolchain and source hashes. The [separate internal review](PREDICTION-PROTOCOL-REVIEW.md) covers the actual law and the claims above; no empirical realization is asserted.

The [delivery checks](PREDICTION-PROTOCOL-CHECKS.json) separately record local link-target checks and matching source/tool hashes. They are document and preservation checks, not additional scientific evidence.

The new result supplies the concrete finite trial contract previously left as a premise. The source predictor's recipe, complementary observation law, finite updater repertoire, memory encoding and normal action route remain supplied. Typed-part construction is a distinct implementation, not identified with these material slots. Ready-state reversal/reformation and the numerical model's outages, skipped writes and rebuilding are excluded from this cycle-only mapping. Formation and revision of these remaining interfaces, reliable evidence use and the later derivation of concern remain open under the governing goal.
