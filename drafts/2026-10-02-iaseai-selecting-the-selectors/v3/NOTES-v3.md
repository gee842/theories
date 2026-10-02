# v3 notes: "No Viable Winner" (2026-10-02, late evening)

*Written by Claude Opus 5.5, which drafted v3. Every sentence of the paper is AI-drafted from Ren's direction; none is Ren's verbatim. Ren's direction is preserved in `sources/16-claude-code-directions/2026-10-02-paper-v3-spine-direction.md`.*

## What Ren asked for

1. The paper is the theory of *why*: certain dynamics will undo us unless we pivot. It is more than a result about control and correction.
2. It must show why the current trajectory will not work, and what has to change.
3. "Demonstrate" means an argument that careful intellectuals cannot simply refute: the invariant constraints a system must respect as part of a larger system, and, by game theory and the present dynamics, that the trajectory of winning digs its own grave. It must be defensible in academic logic.
4. The most important conclusion: we have to work together, as a shared future of humankind.

## How v3 answers it

**The defensibility strategy.**
- Every claim is a conditional theorem proved with standard tools.
- A critic who rejects the conclusion must therefore reject a condition.
- Each condition (C0–C4) is stated as an observable, with present evidence and a falsifier (Table 2).
- The invariants (I1–I4) are shown to be jointly sufficient and individually indispensable within the model.
- Cooperation is derived (Corollary 1), not appealed to.

**The spine.**

| Section | Content | Ren's point |
|---|---|---|
| 3 | A field inside a host; viability as a constraint (Definition 2) | "a system within a bigger system" |
| 4 | Lemma 1 (selection is blind to common terms); Prop. 1 (selection drives the field to the floor, whatever anyone values); Prop. 2 (the weight on winning λ; every player, the winner included, loses in absolute terms) | "by game theory … the current trajectory of winning is just digging our own graves" |
| 5 | Prop. 3 (control over correctors is selected in the largest carriers, size threshold); Prop. 4 (correction is not supplied from inside); Prop. 5 (required independent correction d*, and the rate condition α ≥ g/2) | the guardian test: "the corruption of the constraining mechanism itself" |
| 6 | Prop. 6 (silent crossing; permanent silence of moderate harm); Fig. 2 | the evidence comes too late |
| 7 | Theorem 1 (no viable winner); Table 1 (seven current remedies and the condition each leaves in place) | "why the current trajectory will not work" |
| 8 | Theorem 2 (invariants I1–I4); Corollary 1 (cooperation is necessary); instruments; what cooperation does and does not require; joint development as the strongest form | "what has to be changed"; "we have to work together" |
| 9 | Table 2 (conditions, indicators, evidence, falsifiers); identification | "cannot be simply refuted" |
| 10 | Objections; limitations; conclusion ("a common future") | |

## What came from where

- **From v2 (kept, corrected):**
  - the field model (Eqs. 3–4) and its certificates, cascades and reforms, now in Appendix B;
  - the carrier capacity model;
  - the detection model.
- **From V3-PLAN (the other session's plan):**
  - the control/correction pair and d* (Results 1–3 there);
  - the size threshold;
  - the masking decomposition m = x_E β_in + (1−x_E) β_out (GPT R4);
  - the permanent silence of moderate harm (GPT R1).
- **From the 09-28 paper (*When Capability Outruns Correction* v2):**
  - relative selection is blind to the substrate;
  - the pause result (Appendix Prop. 9);
  - the latency of memory levers (used in Theorem 2(b), I4).

  If both papers are ever submitted to archival venues, the overlap needs disclosure.
- **New in v3:**
  - Lemma 1 for the whole class of relative and payoff-monotone rules;
  - Prop. 2, the weight on winning;
  - the rate condition α ≥ g/2 with its converse (Prop. 5 iii–iv);
  - the silent-crossing threshold m_fl (Prop. 6 ii);
  - Theorem 1 and Theorem 2 with indispensability;
  - Corollary 1;
  - the remedies table;
  - the evidence table.

## Round-2 must-fix items from v2, and their status

- **Fig. 2 own-share inconsistency:** the figure is dropped. The own-share model is now the size threshold (Prop. 3 ii).
- **Ratchet cost omission:** the ratchet is dropped. Its role is taken by d*, which includes cultivated conversion explicitly.
- **Keystone "NP-hard":** the keystone material is dropped from v3.
- **Scope at fixed total size:** corrected (Prop. 3 iv).
- **Assistance factor 1+α:** dropped. The AI-assistance effect now runs through γ in d*.
- **"β ≥ 0.6 never fires":** the v2 numerics are gone. Prop. 6 states the necessary condition only for V → 0 (GPT R1).
- **Formation remark:** replaced by β_out.
- **Diverse panels:** GPT R4's sentence adopted.
- **Oversight paragraph errors:** the paragraph is dropped. Oversight appears only as AI judges and evaluator access.
- **Novelty sentence:** "new in this setting … standard tools".
- **β vs percentage points:** no inference from measured lifts to β.
- **Bibliography corrections (Laurito, Goel, Greenblatt, Narechania, Kwak/Carpenter, EU AI Act, Abdalla):** being verified by the reference agent. See `REFS-VERIFIED.md`.

## Decisions for Ren

1. **Title.**
   - Draft: *No Viable Winner: Competitive Selection, Captured Correction, and the Necessity of Cooperation in AI Development*.
   - Alternative: *Selecting the Selectors: Why Competitive AI Development Cannot Correct Itself, and Why Cooperation Is Necessary*.
   - Alternative: *A Common Future or None: …*.
2. **"Common future".** The conclusion cites *Our Common Future* (WCED 1987) and avoids the phrase 人类命运共同体 ("community of shared future for mankind"). Double-blind reviewers from several countries would read that phrase as a national slogan. The substance is the same.
3. **Symmetry.** Both the US (AI Action Plan, "Winning the Race") and China (2017 State Council plan) are cited as framing development as a race. Cooperation precedents and the Bletchley Declaration are cited for both sides.
4. **The 09-28 paper.** Material is reused, so decide whether that paper stays a separate working paper.
5. **The other session's `experiment/` folder.** v3 does not use it.
6. **v2.** It stays in `submission/` untouched. The v3 sources are in `v3/` and are not yet copied into `submission/`.

## v3.1 (2026-10-03, early morning): after three independent reviews

Three reviewers (governance and philosophy of science; economics and game theory; mathematics) read v3.0 (`v3.0.pdf`, `main-v3.0.tex`); their reports are in `reviews/`.

| Review | Verdict on v3.0 | Estimate after their fixes |
|---|---|---|
| Governance and philosophy of science | borderline, leaning weak reject; about 20% | 35–40% |
| Economics and game theory | weak reject; about 30% | 55–65% |
| Mathematics | core derivations correct, numerics byte-identical; one headline result rested on an unstated assumption; two theorem clauses false as stated; the corollary contradicted Prop. 4 | — |

**What all three agreed.**
- The second-order core is new and survives attack: control over correctors selected in the largest carriers, correction not supplied from inside, the required rate, the pause, and capture before evidence.
- The headline went beyond the theorems in four places: "no viable winner", "every remedy fails", "the conditions of any viable trajectory", and "cooperation is a necessity".

**What v3.1 changes.**
1. **Title: *No Viable Race*.** In the model a single winner whose stake in the host is shared would restrain itself (Remark 2). What fails is the race. The new title makes the thesis exact without weakening it.
2. **Two tiers.**
   - Tier 1 holds without C0: selection of control, starvation of correction, the required rate, and the silence of moderate harm.
   - Tier 2 needs C0: Theorem 1 and the necessity results.
   - The cooperative conclusion has a C0-free route through the contestability premise ("Cooperation without a floor").
3. **Masking is now the central mechanism (Section 6).** Every decentralized escape needs accurate observation:
   - coordination at a threshold;
   - reversion in repeated play (Remark 1, with the cutoff on the discount factor);
   - reputation;
   - countervailing pressure (Remark 4);
   - insurers' pricing.

   Captured evaluation removes all of them. This came from the economics review, and it is also the corpus's own thesis about epistemic closure.
4. **The AI result is now a comparison of two rates (Prop. 5 iv).**
   - The required growth is g/(1+η) with long horizons and g/η with short ones. "Half" is the quadratic, long-horizon case.
   - Capture requires g > (1+η)(b + g_c). If independent correctors adopt AI as fast as the field does, they keep pace.
   - The policy lever is to equip and fund independent correction with AI.
5. **Necessity made exact.**
   - Theorem 2(c): a time-averaged effective liability of at least ν is necessary for every viable trajectory.
   - Theorem 2(b) is renamed non-redundancy.
   - Corollary 1, "No unilateral solution": no carrier's unilateral contribution is favoured by selection. Where no single rule-maker reaches the whole field (C5) and states weigh winning above λ_s > (θ_s − n_s)/(n_s − 1), agreement among rule-makers is necessary. For two states the condition is λ_s > θ_s − 2.
   - (I2)–(I4) are not self-enforcing.
6. **Conditions completed.**
   - C1 is restated as τ_eff < ν, with the covariance condition.
   - C5 (reach and payoff) and C6 (order of events, with the T_A bound) are added.
   - The maintained assumptions A1–A6 are listed, each with what changes if it is dropped.
   - Measurements that would refute the account are named in advance, to avoid immunization.
7. **Cooperation given content.**
   - Definition 3: coverage, content, verification. It constrains properties, not institutional form.
   - Table 2: what must be agreed, by whom, verified how, and existing seeds in the US, EU and China.
8. **Table 1 rebuilt.** Each remedy is given in its strongest form, with what it supplies, what it leaves, and what agreement adds. New rows cover technical safety, binding regulation, liability with insurance, public institutes, and measures that change standing between states (worded symmetrically).
9. **Mathematics corrected.**
   - Theorem 2(a) now claims eventual recovery, plus a transient condition (with a counterexample in Appendix C).
   - Theorem 1 states its full hypotheses, and C6 is quantitative.
   - The payoff clause moved out of Theorem 1 and now carries its conditions.
   - Prop. 8(iii) is restated so the remaining domains must stay captured.
   - The certificate uses the full row.
   - The fixed cost f caps the requirement (Prop. 5 v).
   - Splitting a carrier divides cultivated conversion by k², not k.
   - L_i/d_i decreases (not L_i).
   - n > θ (not n ≥ θ).
   - The brute-force check of Prop. 2 now covers both branches (180 cases).
10. **Political reading.**
    - Host examples now lead with conditions all blocs agree on.
    - "Capture is structural; we claim no present institution is captured."
    - "Independence means independence from the field, not any political form."
    - "Replacing executives or firms" replaces "replacing leaders".
    - "States in strategic competition".
    - The precedents paragraph names the conditions that made past agreements work.
    - The antitrust caveat is added.
    - "Common future" (WCED 1987) is kept.
11. **Related work.** Han et al. (AI races), Cave & ÓhÉigeartaigh, international institutions, verification and compute governance, frontier regulation, if-then commitments, sandbagging and evaluation awareness, Barrett on self-enforcing agreements and thresholds, Becker and Peltzman, gatekeepers, Alger & Weibull, and Schaffer 1989 (references verified in `REFS-VERIFIED-2.md` and `-3.md`).

**Checks.** `checks_v31.py` appends to `checks.log`:
- both branches of Prop. 2;
- the repeated-game cutoff;
- the rate law for η ∈ {0.5, 1, 2, 3}, long and short horizons;
- the fixed-cost saturation;
- the T_A bound;
- the k² factor;
- the sufficiency transient.
