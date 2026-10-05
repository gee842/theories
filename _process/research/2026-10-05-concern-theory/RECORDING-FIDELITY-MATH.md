# Formed finite records and the acquired-evidence contract

6 October 2026. AI-authored mathematical bridge from formed material organization to the retained observations required by [the noisy teaching results](TRANSFER-EVIDENCE-MATH.md). The [specified experiment](../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/PROTOCOL.md) and [Lean formalization](../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/formal/README.md) implement a finite record interface. They do not construct a calibrated assay, an updater, confidence arithmetic or a concern-guided actuator.

The earlier confidence theorem assumes that physically acquired records are prefixes of declared observation sources. Paying for an operation does not establish this: a material write can fail selectively after its outcome is known. This note supplies a sufficient physical contract, a precise retention obstruction, and an exact false-certificate comparison. Its contribution is the connection to actual formed parts, write escrow and capacity, rather than a new general theory of selection bias or confidence bounds.

## 1. Conditional retention changes the teaching law

Let h contain the complete acquired history before a trial. Admission is decided before its innovation Y is realized. Conditional on h and admission, suppose Y is Bernoulli with probability β∈(0,1). Let K indicate whether its bit is retained, and put

\[
r_y(h)=\Pr(K=1\mid Y=y,h),\qquad
R(h)=(1-\beta)r_0(h)+\beta r_1(h).
\]

**R1 — Retained-bit law.** Whenever R(h)>0,

\[
\Pr(Y=1\mid K=1,h)
=\frac{\beta r_1(h)}{(1-\beta)r_0(h)+\beta r_1(h)},
\tag{1}
\]

and

\[
\mathbb E[K(Y-\beta)\mid h]
=\beta(1-\beta)[r_1(h)-r_0(h)].
\tag{2}
\]

Consequently the conditional retained-bit mean equals β exactly when r₀(h)=r₁(h). These are direct consequences of the two conditional outcome probabilities; no independence between the retention rule and the outcome is assumed.

For independent repeated trials with a stationary independent retention experiment having fixed r₀,r₁ and R>0, the successive retained marks are iid Bernoulli with the probability in (1). To see this, sum over the number of rejected trials before the next accepted one: the probability its mark is one is Σⱼ≥₀(1−R)ʲβr₁=βr₁/R. Independence of the unused future trials repeats the same argument after each retained mark. This stationary repeated-resumption result is not a claim that arbitrary adaptive retention produces one iid stream with a fixed altered mean. Equation (1) is the local statement in that case.

Nor is r₀=r₁ necessary for every finite anytime guarantee. A process that omits its first zero and then stops permanently retains only ones, but they are the genuine original prefix before that zero. Its stopping count is selected by outcomes. Conditional-on-survival observations are biased, yet every certificate it evaluates is still a certificate on an original prefix. Section 4 treats this distinction explicitly.

## 2. A physically total recorder for admitted outcomes

The underlying formation law has free A/H variants, a resident, a capture site, common fuel F, finite source E and a one-unit local fuel store. Starting from absent variants and a damaged site, its actual preparation trace for K slots is:

1. Form K H variants and one A; associate A and repair the site.
2. Capture and locally copy A, K times.

With material capacity 2K+1, sufficient initial fuel and source, this trace ends with K free A, K free H, one A resident, F=F₀−K−3 and E=E₀−K. Its total energy expenditure is 2K+3, including the K local copies. These are occurrences under the earlier formation law, not an assigned successful endpoint. The concrete K=2 trace is checked in Lean using that unchanged law.

A new, explicitly supplied assembly recipe incorporates one A and one H into each blank slot, spending one common fuel. Thus the recording stage starts with K slots, F*=F₀−2K−3, E*=E₀−K. The bit encoding, balanced recipe and source-to-common-fuel receipt mechanism are supplied. This is a composition through actual parts and stocks; it is not a derivation of the recipe or wiring. The earlier formation event repertoire is suspended after this handoff.

Let B be blank slots, W the committed Boolean word, and P the phase: idle, awaiting an outcome, or latched with that outcome. A non-idle phase occupies one slot. Writer escrow e is one exactly during a non-idle phase. The total assembled slot count S satisfies

\[
S=B+\mathbf1_{P\ne\mathrm{idle}}+|W|,
\qquad e=\mathbf1_{P\ne\mathrm{idle}}.
\tag{3}
\]

An assembly event requires idle phase and available A, H and common fuel; it does not inspect W. The particular experiment assembles every available pair before trials. A broader trace may assemble later, but it must pay and preserve the same ledger.

A trial consists of three events:

| Event | Guard and actual update |
|---|---|
| Reserve | Idle, B≥1, F≥2, E≥2. Set B←B−1, F←F−2; burn operation fuel 1, retain write escrow e=1; await outcome. |
| Observe Y | Latch the actual bit. If Y=0, convert two source units into two common units; if Y=1, no receipt. |
| Commit | Spend the escrow unit, append the latched bit to W, return to idle. |

Admission does not inspect the future bit. Both possible outcomes have a reserved slot and the same already allocated write cost. The source guard licenses the full two-branch physical kernel: a realized failure branch might need no source, but that does not make the successful branch available after admitting the trial. No second admission occurs while busy.

**R2 — Finite total-record contract.** Under this supplied event law, with a schedule that completes the observe and commit events of every admitted trial and with no record erasure, the committed word after each completed trial is exactly the chronologically acquired outcome word. Every admitted outcome is retained: r₀=r₁=1. For any finite trace, including incomplete trials,

\[
W_{\rm final}\mathbin{+\!+}\mathrm{pendingWord}(P_{\rm final})
=
[W_{\rm initial}\mathbin{+\!+}\mathrm{pendingWord}(P_{\rm initial})]
\mathbin{+\!+}\mathrm{observations}(\mathrm{trace}).
\tag{4}
\]

**Proof.** Assembly and reserve preserve the left-hand observation word. Observe appends exactly its realized bit as a pending word. Commit transfers that same bit from the pending word into W. Induction proves (4). At idle endpoints the pending words are empty. Reservation provides a slot and write unit before either outcome; neither observation branch consumes that escrow, and commit is enabled for either bit. Completion therefore gives full retention. An enabled commit does not itself prove that a scheduler eventually performs it. ∎

The generalized finite-trace account also retains exact material and energy. With U the free-plus-resident variant population and L the local fuel bit,

\[
U+2S\le M,\qquad
F+E+L+e+\mathrm{spent}=\mathrm{initial\ stored\ energy}.
\tag{5}
\]

Assembly transfers two free parts into a slot and burns one fuel; reserve burns one and escrows one; observe only transfers source energy; commit burns escrow. All four events preserve material exactly, and each decreases stored energy by its declared spending. Induction proves (5). The old formation ledger composes with this ledger at handoff, including every setup cost. Slots remain occupied after writing; fuel abundance cannot replace them.

This is a sufficient recorder architecture, not a necessary architecture for faithful evidence. Outcome-independent thinning can also preserve calibration under its own acquisition law. A different encoding can use different parts. A permanent halt after a failed write can preserve a genuine prefix. Those alternatives need their own physical and statistical contracts.

## 3. Exact completed macro, with capacity retained

For each y∈{0,1}, define the full-state successor C_y(s) by consuming one blank slot, returning to idle with empty escrow, appending y and setting

\[
F'=F-2+2(1-y),\qquad E'=E-2(1-y).
\tag{6}
\]

Other inherited plant fields and the assembled slot count remain unchanged.

**R3 — Three-event exactness.** A trace consisting of reserve, observe y, commit y from s to t exists exactly when s satisfies the material/phase invariants, its admission guard holds, and t=C_y(s).

**Proof.** Forward: the first event requires invariants and admission; determinism of the three updates gives C_y(s). Backward: the guard supplies the reserve, both observation branches and prepaid commitment; eventwise invariant preservation enables their composition. ∎

The projection to the earlier paid teacher has the same completed-trial fuel/source changes, count increment n←n+1 and loss-count increment s←s+y. Its EWMA, if externally decoded from the complete word, has the same recurrence. This is equality on recorder-admitted completed calls. It is not equivalence of complete processes: the old teacher omits blank capacity, and some of its realized failure transitions allow E<2. The capacity-backed macro retains the world, slots, word, pending phase and escrow, rather than identifying physical states solely by F,E,n,s.

For K=2,F₀=12,E₀=18, the actual old-law preparation yields free A2/H2, active resident, F7,E16. Two assemblies leave F5,E16 and two blanks. After outcomes [0,1], there are no blanks, F3,E14, and both bits are retained. The old teacher can still pay for another trial; this recorder cannot admit it. Initial energy is 30 and final energy 17: setup and recording spent 13. Five material units remain present, four within the two records and one resident. Lean checks this complete witness, not just the arithmetic abstraction.

## 4. Prefix fidelity transfers the existing confidence event

Let X₁,X₂,… be a declared iid Bernoulli(β) innovation source. Pretrial adaptive admission may stop on acquired history and actual affordability, but every admitted innovation must be the next fresh source bit. A funded completion schedule and R2 then make W=X₁…X_N at any inspection. This does not claim that W conditional on a selected N is an iid length-N sample, or that reaching count n preserves its unconditional binomial law.

Let L(n,s) be the single-stream lower bound from [T3](TRANSFER-EVIDENCE-MATH.md#4-an-anytime-finite-certificate-from-actual-counts), with total allowance α. That theorem establishes the simultaneous event

\[
\Pr\{\exists n\ge1:L(n,S_n)>\beta\}\le\alpha,
\qquad S_n=\sum_{j=1}^n X_j.
\tag{7}
\]

**R4 — Prefix transfer, including terminal omission.** If every certificate input is some genuine original prefix (N,S_N), then the probability of ever certifying L(N,S_N)>β is at most α, under any actual inspection or stopping rule. It need not be a stopping time with respect to the retained prefix alone.

**Proof.** Every such false certificate is contained in the event in (7), path by path. No new binomial calculation conditional on funding, survival or N is required. ∎

The full recorder meets this condition. The halt-on-first-zero control omits that final zero and halts permanently: before the omission it had preserved X₁…X_N, and no later bit is appended. It also meets R4, even though its retained bits conditional on survival are all ones and its local keep probabilities are r₀=0,r₁=1. In contrast, omitting a zero and resuming appends later observations across an interior gap, so R4 no longer applies. Loss of this sufficient premise alone would not prove failure; the following exact counterexample does.

## 5. Equal per-attempt expenditure can accompany a false confidence law

Use K=8 slots, at most T=32 attempts, β=1/4 and α=1/10. Start the actual preparation at F₀=84,E₀=72. After formation and eight paid assemblies, F*=65 and E*=64. Fuel and source can fund every potential attempt through 32, regardless of the preceding outcomes; slot availability and commitment policy still determine admission. Thus the comparison is not a hidden fuel or source affordability difference.

All three commitment rules burn the same escrow after every actual attempt. Full commits each bit; drop-zero/resume returns the zero's slot to blank without recording it, then permits another attempt; halt-on-zero does the same omission but stops permanently. Ones consume their slots normally. The controls are explicitly different supplied commitment laws. Raw attempts and their costs remain in the experiment's audit even when its slot decoder omits them.

For the dyadic single-stream bound, the grid denominator at n is the largest power of two ≤n and the per-count allowance is α/[n(n+1)]. Direct exact binomial-tail evaluation gives L(8,8)=3/8. For n≤8, no other possible retained count has L>1/4. Therefore:

\[
\begin{array}{ll}
\text{Full:}&\Pr(\text{false certificate})=(1/4)^8=1/65536,\\[2mm]
\text{Drop zero and resume:}&
\Pr(\text{false certificate})=\Pr\{\mathrm{Bin}(32,1/4)\ge8\}\\
&\displaystyle=\frac{10469065127243216839}{18446744073709551616}\approx0.567529,\\[2mm]
\text{Omit first zero, then halt:}&\Pr(\text{false certificate})=1/65536.
\end{array}
\tag{8}
\]

The full arm stops after eight observations. The resumed-omission arm reaches the eight-one record whenever at least eight of its potential 32 outcomes are ones; the record no longer estimates β. Its false-certificate probability exceeds the declared lifetime allowance. The halt control reaches that same record only when the first eight outcomes are all ones. It preserves the original prefix bound. [The executable study](../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/README.md) checks these exact probabilities, every primary two-bit history, all phase ledgers and the admitted teacher projection.

This obstruction is decoder-specific. At completed endpoints without later assembly or other flows, exact global stock differences also encode the raw attempt count N and one count S:

\[
S=(F^*-F)/2,\qquad N-S=(E^*-E)/2.
\tag{9}
\]

A physically implemented meter with the initial references, sufficient accuracy and paid reading/retention could reconstruct those counts despite slot censorship. The specified certificate reads slots only; the audit's knowledge of stocks is not silently granted to that decoder. Thus (8) refutes this record interface, not every possible way of extracting evidence from the same world.

## 6. Closure and remaining premises

This construction discharges a finite material recording obligation under a declared law: variants are actually formed; parts are incorporated into finite slots; payment and capacity precede the outcome; actual records preserve the admitted source prefix; and an already established confidence event transfers through that faithful interface. It also gives a concrete failure when an outcome-dependent commitment law breaks the interface, despite equal expenditure per attempt.

The source calibration and freshness, recipes, signal routing, escrow protection, completion schedule and record retention are supplied. The formal module verifies these deterministic rules, not the Python implementation or the probability theorems. It does not establish robust recorder survival under inherited wear or damage, and the former formation repertoire is not automatically active in the recorder stage. Confidence arithmetic, learned prediction, causal use by an actuator, correspondence to other centers, shared evaluation and empirical realization remain separate obligations.

Finally, K material slots provide only finite prefix capacity. They support the finite anytime certificate up to actual exhaustion; they do not establish the n→∞ premise of transfer-evidence T2 or T4. Renewable records, growing counters or another resource-supported unbounded sequence need their own formation, upkeep, retention and succession account. No finite successful witness completes durable learning or the unified foundation.
