# Independent review of direction and turnover

5 October 2026. AI-assisted mathematical review of [DIRECTION-AND-TURNOVER.md](DIRECTION-AND-TURNOVER.md). **The final propositions pass review.** Read the note and its final assumption clarifications; independently checked the threshold balance, irreducibility argument, ring calculation, survival-conditioning example and accessible-record bound. No simulation was needed. This review checks the stated mathematics; it does not constitute an independent literature audit of the cited Seifert source or new physical evidence.

The threshold balance is exactly p_t Q f_U: internal transitions cancel, leaving entry minus exit. K, assay profiles, information access and comparison horizons must remain fixed. Otherwise a changing assessment can add a time-dependent term unrelated to physical progress. The final text explicitly retains this restriction and distinguishes monotonicity over an interval from an endpoint comparison.

The finite irreducible-chain proof is correct. Strictly positive stationary weights turn pointwise Qf≥0 into Qf=0; the maximum principle and reachability then force constancy. Applying this to every upward-set indicator proves the capability claim. Its quantifier is **every initial state and every positive time**, not improvement from a selected poor preparation or comparison between two stationary laws. The text also correctly distinguishes finitely many explicit assay profiles from finitely many output coordinates; a finite sufficient operational state independently makes the image of K finite. An expanding physical record is not silently covered by the finite-state theorem.

For the three-state ring, summing the three edge currents times their log rate ratios gives (a−b)log(a/b), with the stated positive sign. The stationary capability distribution is constant regardless of that current. Physical entropy interpretation still requires the declared driven realization and rate-ratio framework; the abstract calculation does not identify a particular chemical implementation. The survivor example is also correct with the final strict assumption 0<delta_A<delta_B: unconditional mass in A decreases while its fraction among survivors increases.

## Accessible information and absorption

The final statement explicitly supplies the two premises needed for its uniform protocol bound:

1. The loss set is invariant under every admissible continuation.
2. Changing the continuation preserves the law, including the posterior, of the already realized past.

Let S_t={T_loss>t} and r_t=Pr(S_t | G_t). For each admissible continuation pi and productive future assay E_pi, success implies S_t. Hence

\[
\Pr^{\pi}(E_\pi\mid\mathcal G_t)
\le\Pr^{\pi}(S_t\mid\mathcal G_t)=r_t.
\]

Because this holds uniformly, taking an existentially successful protocol does not evade the bound. A nonempty region of these productive assays at reliability alpha requires r_t≥alpha. Thus, for any upward set excluding the empty region,

\[
\Pr(\mathbf C_t\in U)
\le\Pr(r_t\ge\alpha)
\le\frac{\mathbb E r_t}{\alpha}
=\frac{\Pr(T_{\rm loss}>t)}{\alpha}.
\]

This uses accessible posterior capability, not free knowledge of hidden state. When absorption status is measurable in the accessible record, r_t is the actual survival indicator and the sharper survival-probability bound follows. Full microscopic observation is unnecessary. Conversely, when loss is hidden, the assessed region need not disappear on each already-absorbed history immediately; the ensemble bound handles that uncertainty correctly.

The convergence conclusion needs almost-sure absorption under the actual past dynamics and fixed positive reliability. It concerns future productive assays that cannot succeed from the loss set. Archived achievements, informational tasks or other capabilities of inert material are outside that class. Restart-capable continuations would invalidate the key premise and require a new model. These limits are stated in the note.

The note therefore supplies valid constraints on a proposed directional theorem, without confusing repeated delivery, intervention gains, stationary comparison, survivor enrichment and unconditional temporal improvement. It does not itself supply the favorable formation-and-retention balance or complete the positive universal objective.

Reviewed source SHA-256: `7c819e13ff39c2c42e602946a498cc159e943bccd985444839e8724b3d97fe20`. Review follows repository commit `348d82644a92315a0ea415a9edc44708e27ad516`; the new note was uncommitted. Only this review file is authored here.
