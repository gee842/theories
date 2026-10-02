# Review R4 (round 2): area chair meta-assessment

*AI review of v2. On 2026-10-02 Ren asked for "another round of independent review like before, how ready is this for the reviewers?". The reviewer was a Claude Opus 5.5 subagent, briefed as a senior IASEAI'27 area chair. It read only the anonymous v2 PDF, `submission/` (main.tex, references.bib, figure and table sources) and, for spot checks, `build/figures.py`, `field.py`, `carrier.py` and `checks.log`. It did not read NOTES.md, the round-1 reviews or the corpus. It re-implemented the numerics independently. Its report is reproduced verbatim below.*

---

# Area Chair Meta-Assessment: "Selecting the Selectors: Recursive Selection and the Evolution of Control over AI Evaluation" (IASEAI'27, anonymous draft of 2 Oct 2026)

## 1. Summary and bottom line (how ready is it?)

**What the paper does.** It models AI-relevant "selection domains": development, evaluation, standards, procurement, formation and information. In each domain, a practice's share x_i grows when rule support r_i offsets its baseline cost, and success in domain j converts into rule support in domain i through a matrix B (Eqs. 1–2, p. 3). There are four layers of results:

- **Capacity (Section 4).** Carriers that differ heritably in conversion capacity q are selected for q when the appropriable, persistence-weighted return χ·yᵀMy exceeds marginal cost (Prop. 2, Eqs. 3–4). The return is a quadratic form in the carrier's cross-domain success. A ratchet links capacity to capture thresholds (Prop. 3).
- **Field results (Section 5).** Local tests cannot certify against capture. A row sum below one certifies its own domain, and the core is an exact joint test (Prop. 4). Cascades, re-absorbed reforms and keystone sets follow (Prop. 5).
- **Detection (Section 6).** A detection-delay law: evaluators from the evaluated lineage mask harm, and the delay diverges at βx̄ = V_alarm/K (Prop. 6).
- **Application (Sections 7–9).** A mapping to AI oversight, tests, and governance principles.

**Bottom line.**
- **Substance: close to ready.** The mathematics is correct as far as I checked, and every reported number I re-ran reproduces with independent code.
- **Presentation: not yet ready for a mixed IASEAI reviewer pool.** The paper is very dense (about 8,000 words in about 8.5 pages, with roughly 20 coined terms). The central theorem is phrased in a way ("exactly when") that invites a tautology objection. Some main-text claims rest only on appendices.
- **One substantive modeling issue.** The Figure 2 capacity illustration uses a "representative carrier" assumption (Appendix B, p. 13) that departs from Eq. (3). Under the literal Eq. (3) reading, one of the three headline runs reverses and a new qualitative fact appears: capacity cannot invade from rarity. This is fixable in half a day, and it strengthens the paper if stated as a result.
- **No fatal problems.**
- **Readiness: about 6/10.** With two focused days it becomes a competitive borderline-accept for a venue that took about 19% of submissions as archival papers.

### 1a. What I checked (proofs and numerics)

All my scripts and outputs are in `/private/tmp/claude-501/-Users-ren-theories/f263a065-8a67-4878-a3b3-e65dcc1d8b2a/scratchpad/review2/R4/`:
- `mymodel.py`: my field model, written from Eqs. 1, 2, 5, 6 and the Appendix B parameters, not from the authors' code.
- `check1_field.py` to `check6_tip.py`, each with a matching `*.out` file.

**Proof spot-check (Appendix A)**
- **Lemma 1:** correct.
- **n = 1 case:** correct. I re-derived Φ̇ = κx(1−x)(ar−c)² + (εa/b)(bx−dr)² ≥ 0.
- **Prop. 1:** correct. The Jacobian is block-triangular. The zero diagonal of the Metzler block rules out Hurwitz stability. The Perron–Frobenius continuity argument for a positive eigenvalue when B_MM has a cycle holds.
- **Prop. 2:** correct. I checked the closed form against direct integration of Eq. (3) and they agree to 6 digits. ℓ′(u) = m(u)/u³ with m′ < 0 holds.
- **Props. 4–6:** correct. The construction in 4(a) checks. The 4(c) pruning induction works. The comparison argument in 5(ii) holds. The algebra and delay formulas in 6 hold.
- **Remarks 1, 3, 4:** correct.
- **Gaps (all minor):**
  - c_i > 0 is needed for R_ij but never stated, and Def. 1 even contemplates c_i ≤ 0.
  - Cor. 3's "rises by the factor 1+α" holds only for the quadratic cost of Prop. 2(iv).
  - Prop. 3 assumes capacity does not enter c_i. The simulation charges 0.05q per decision, so monotonicity needs b̂_ij·c_i > γ·b⁰_ij. This holds for the paper's parameters.
  - The ν-slack in Prop. 5(i) is loose but harmless.
  - The L_i weighting in Eq. (4) relies on keyed support resetting to zero each horizon (ζ_i(0) = 0). This is unstated, and the simulation does not reset.

**Numerical re-implementation (independent RK4, step 0.02–0.1)**

| Claim (page) | Paper | My result |
|---|---|---|
| Cascade at θ=1.2: P, E/I, S, F captured (p. 5) | ≈43, 56, 67, 106 | 42.5, 55.3, 66.7, 105.4 ✓ |
| Firewalled rows 0.94; standards reset re-absorbed (p. 5) | E, F independent; t≈38 | E, F ≈ 0.0005; t = 37.2; firewall holds ✓ |
| Table 2 β rows: t_det, delay (formula), min V (p. 14) | 74.7 … 462.1; 13.0 … 387.4 | 74.7 … 462.0; 13.1 … 387.4; min V 0.536 … 0.104 ✓ |
| ψ rows; μ rows (p. 14) | as tabulated | identical to ±0.5 ✓ |
| θ=0.6: 23 stable configurations, 13 survive entry, 3 capture both selectors (p. 13) | from a margin ≥ 0.05 heuristic | Census ✓. **Direct simulation at μ=10⁻⁴ confirms that exactly those 13 persist** and all ten with margin 0.01 collapse to D |
| Hysteresis at μ=10⁻⁶ (Fig. 4) | appears above θ=1; lost below 0.26 | appears at 1.025; persists to 0.275 ✓; φ=0.22 survives decoupling ✓ |
| μ=10⁻⁴: tips at θ=0.975, lost at 0.275 (p. 13) | — | Lost at 0.275 ✓. Tipping at 0.975 ✓ **only after t ≈ 1,900** (a slow saddle-node passage); a 1,500-unit sweep misses it |
| Fig. 2 under the paper's specification (pp. 5, 13) | χ=0.8: q̄>0.9 at ≈28, full capture ≈184; χ=0.3 slower; χ=0.1 displaced | 27.4 / 182.4; 247 / 386.5; displaced ✓ |
| Fig. 2 with keyed support driven by the type's **own** success (Eq. 3 read literally) | not reported | χ=0.8 still captures (55.7 / 220). **χ=0.3: high-capacity type displaced, capture stays in D.** Threshold ≈ 0.55–0.6 instead of 0.25. **A 1% high-capacity type cannot invade even at χ=1** (under the paper's spec it invades and captures by t≈181–210) |
| Frozen capacity at 0.5 leaves capture in D | ✓ | ✓ |
| Appendix D Γ_T values | 0.82, 1.88, 0.59, 0.38 | 0.8192, 1.8822, 0.5859, 0.3764 ✓ |
| "For β ≥ 0.6 the alarm never fires" (p. 6) | never | Within 600 units ✓. At β=0.6 with μ=10⁻⁴, x_E ≈ 0.99979, so **the alarm does fire at t ≈ 2,359**, with V ≈ 3×10⁻⁴. Say "β > 0.6" or "not before collapse" |

## 2. Predicted scores and decision

Scale: each criterion 1–5 (5 = excellent). Overall 1–10 (4 = weak reject, 5 = borderline, 6 = weak accept, 7 = accept).

**Aggregate prediction**

| Criterion | As is: mean (range) | After the plan | Main driver |
|---|---|---|---|
| Relevance | 4.5 (4–5) | 4.6 | Squarely on evaluations, oversight, frontier governance, standards, multi-agent and RSI themes |
| Quality | 3.3 (2–4) | 3.6 | For: correct proofs, reproducible numerics. Against: thin central theorem, representative-carrier assumption, no data |
| Clarity | 2.8 (2–4) | 3.4 | Polished sentences but compressed; jargon; forward references; claims resting on appendices |
| Originality | 3.1 (2–4) | 3.4 | New coupling of capacity selection with cascade thresholds; components known; key prior art missing |
| Significance | 3.2 (2–4) | 3.4 | Actionable levers (appropriability, row certificates, delay vs. silence) but uncalibrated |
| **Overall** | **5.5 (4–7)** | **6.0–6.3** | |

**Likely reviewer pool**

| Reviewer | Rel | Qual | Clar | Orig | Sig | Overall | Predicted headline |
|---|---|---|---|---|---|---|---|
| Governance/policy | 5 | 3–4 | 2–3 | 3–4 | 3–4 | 6 (5–7) | "Timely and well grounded in the capture literature; but how would a regulator measure R_ij or row sums? Several principles (independence, conflict-of-interest rules, structural separation, sunsets) are familiar." |
| Multi-agent / game theory | 4 | 2–4 | 3–4 | 2–3 | 3 | 5 (4–6), drops to 4 if they notice the carrier spec | "Prop. 2 is a first-order condition plus the Price equation. Eq. (1) is explicitly 'not a game'. Missing Olson, rent-seeking and niche-construction monopolies. Section 5 is known threshold/k-core material. The capacity simulation has no frequency dependence." |
| Ethics / auditing | 5 | 3–4 | 3 | 3–4 | 3–4 | 6 (5–7) | "Valuable on evaluator independence, AI judges and control units; the value-neutral pathology criteria are welcome. The normative 'closure test' is ad hoc. Auditor-independence analogs (issuer-pays ratings, audit rotation) are missing." |
| Technical alignment | 3–5 | 3 | 3 | 3 | 2–4 | 5 (4–6) | "Thoughtful mapping to debate, AI control, W2S, RRM and CAI. But masking is non-strategic (no sandbagging or evaluation awareness), the carriers are organizations rather than models, and there are no experiments." |

**Predicted decision.** As submitted today: a borderline split (two weak accepts, two borderline or weak rejects), decided by the AC.
- **Probability of archival acceptance as is: about 30% (range 20–40%).** This is above the 19% base rate because rigor and polish are above the venue median.
- **After the plan: about 45% (range 35–55%).** The residual uncertainty is mostly reviewer assignment: a math-averse governance reviewer, or a game theorist who reads Prop. 2 as tautological.

## 3. What a champion would argue

1. **The right question, sharply posed.** The paper does not ask whether success entrenches. It asks when selection favors investing in control over the selection process, and it answers with conditions: appropriability χ, persistence L_i versus correction d_i, cost, and cross-domain presence (Prop. 2, Cor. 1). Corollary 1 is a disciplined "when it does not happen" result, rare in this literature.
2. **A lever that fixed-conversion analyses cannot see.** Lowering the appropriability of rule-making (interface-neutral standards, rotating held-out benchmarks, outcome-based procurement; Section 9) lowers the selected capacity without touching incidental coupling. Faster correction lowers both capture and the incentive to cultivate it (Prop. 2(iii)).
3. **Decentralized, operational independence criteria.** Isolated tests cannot certify (Prop. 4a, a fallacy of composition), but each authority can certify its own domain from its inbound row (Prop. 4b, d). "Inbound conversion below one, counted in control units" (Remark 2) is a concrete standard for evaluator independence that goes beyond the EU AI Act's notified-body independence (p. 9).
4. **A crisp result on AI judges.** Single-lineage bias of a few percentage points means delay, not silence. Silence needs something shared by all lineages, such as formation or training data (Prop. 6, Remark 3, p. 6). "A hundred models trained on the same data count as one unit" is quotable and correct within the model.
5. **Reform dynamics with policy bite.** Margin reforms are re-absorbed unless they push inbound conversion below one. Keystones can re-absorb their own reform under feedback. A way of succeeding can outlive its origin (Prop. 5; p. 5).
6. **Rigor and reproducibility far above the venue median.** Short, correct proofs. Every number reproduces independently. Robustness to entry rate, explicit falsifiers ("When the account loses force", p. 8), and self-application ("Apply the analysis to the regime", p. 9).
7. **On theme.** It covers evaluations, control and oversight, standards and certification, multi-agent dynamics, frontier governance and (via the "Speed" paragraph) automated evaluation-writing in recursive improvement.

## 4. What a skeptic would raise (ranked by expected effect on the decision)

**No issue is fatal.**

1. **"The central theorem is a tautology."** *Major; 1–2 h to reframe.*
   - Prop. 2(i) is the derivative of a payoff that is linear in q by construction. Part (ii) is the Price equation (the paper says it "only keeps the books"). Part (iii) follows from nonnegative coefficients.
   - The abstract's "selection favors greater capacity *exactly when*…" invites this objection.
   - **Fix:** claim what is actually derived. The return's structure follows from rule-support dynamics: it is quadratic in the carrier's own cross-domain success, weighted by persistence, decreasing in correction, and its kernel is the cultivated part of the matrix that sets capture thresholds. Then stress the ratchet (Prop. 3) and the implications in item 2. Drop "exactly when".

2. **The capacity illustration rests on an unstated "representative carrier" assumption that departs from Eq. (3).** *Major; 3–4 h.*
   - Eq. (3) drives a carrier's keyed support with its *own* success y. Appendix B (p. 13) instead drives each type's keyed stock with the *whole practice's* share x_j ("representative carriers").
   - Consequences:
     - A minority type is over-credited by a factor 1/p.
     - Frequency dependence disappears.
     - Keyed plus shared support exceeds what is produced, because the shared stock uses each type's actual share Σ_k q_k x_jk.
   - Under the literal Eq. (3) reading (my runs):
     - The χ threshold at equal frequencies rises from 0.25 to about 0.55–0.6.
     - The χ = 0.3 run reverses (capacity displaced; capture stays in D). This undercuts "the runs differ in nothing but appropriability" as a demonstration of the 0.25 threshold.
     - A 1% high-capacity type cannot invade even at χ = 1.
   - The qualitative claim survives at χ = 0.8 (full capture by t ≈ 220).
   - **Fix, and turn it into a result:** because W is quadratic in the carrier's own success, the return scales with the square of carrier size. Capacity is selected among large, broadly present carriers and cannot invade from rarity. Concentration is therefore a precondition, and fragmentation (interoperability, antitrust) lowers the return quadratically. This fits frontier AI (few large developers) and strengthens Section 7.
   - Either state the representative assumption explicitly as the "few large carriers" regime, or adopt own-share keying and report both.

3. **Originality relative to uncited prior art.** *Major for the originality score; 1.5–2 h.*
   - Cor. 1(a) is Olson's (1965) logic of collective action applied to rule support. Endogenous lobbying and rent-seeking (Tullock 1967; Grossman–Helpman 1994) are absent.
   - Krakauer, Page & Erwin (2009, *Am. Nat.*) show that shared niche construction suffers a tragedy of the commons and that the ability to monopolize the niche stabilizes it. This is a closer and more general precedent for χ than Gerlee & Anderson (2015), which p. 2 calls "the closest precedent".
   - "Practices" are Nelson–Winter (1982) routines.
   - Shared formation raising β for every lineage is algorithmic monoculture (Kleinberg & Raghavan 2021). It is already in references.bib but uncited.
   - Evaluator funding by the evaluated has classic analogs that auditing and governance reviewers will expect: issuer-pays credit ratings (e.g., Bolton, Freixas & Shapiro 2012) and auditor independence/rotation rules.
   - Optional: Harre (2025) on multi-level selection and AI governance institutions.
   - Add one sentence per item saying what is new here: the coupling of capacity selection to cross-domain thresholds, and the detection law.

4. **Clarity for a mixed audience.** *Major for the clarity score; 3–4 h, partly overlapping items 1–2.*
   - Coined vocabulary: practice, carrier, selector, rule support, conversion, capacity, appropriability, meta-attractor, configuration, internally sustaining, uninvadable, hull, core, keystone, firewall, control unit, error-access graph, formation, masking, closure (two kinds), answerability, generative/pathological.
   - Compressed sentences; propositions without proof ideas.
   - Section 4's illustration (p. 5) uses "the six-domain field of Section 5" before Section 5 defines it.

5. **No empirical grounding.** *Major for the significance score; not fixable in 3 days.*
   - Parameters are uncalibrated ("estimate nothing", p. 9) and Table 1 is illustrative.
   - The identification route (distributed-lag regression, p. 8) is correct within the model but requires measuring decision shares x_i over time.
   - **Mitigate (≤ 1 h):** one calibrated back-of-envelope in the main text. For example, a same-family lift of about 0.067 (Awuni et al. 2026), if read heuristically as β, gives a delay of ln[(1−β)·0.6/(0.6−β)] ≈ 0.049 harm e-folding times. With a two-year e-folding time that is about five weeks: delay, not silence. Label the β mapping as heuristic.

6. **Thin multi-agent content.** *Minor to major; 30 min.*
   - Eq. (1) is a switch, not a game. Masking is non-strategic. There is no competition among practices within a domain.
   - All of this is acknowledged (p. 9). Add a sentence on why strategic masking, sandbagging or evaluation awareness would raise β and so strengthen the conclusions, and name it as the main open problem.

7. **Field prediction (a) does not follow from the model as worded.** *Minor to major (it is a stated testable prediction); 15 min.*
   - Section 8, p. 8: "Holding size fixed, investment … rises superlinearly with … cross-domain presence."
   - Corollary 2 assumes weight one in every domain, so size grows with scope. With total success s fixed and spread over |S| domains, yᵀMy = cL·s²·[φ̂ + (η̂−φ̂)/|S|]. That increases with spread only if φ̂ > η̂, and it is bounded, not superlinear.
   - Reword as "holding within-domain share fixed", or state the condition.
   - The superlinearity also depends on C(q) not scaling with presence; the simulation charges per-decision costs.

8. **Main-text claims supported only in appendices.** *Minor; 1–2 h.*
   - "Because capture is hysteretic (Appendix B)" and "keystone status shifts … (Appendix B)" (p. 8) support governance principles. Cite the n = 1 bistability and Prop. 1 instead, or move a compact Fig. 4 into the main text.
   - The figure parameters (κ, ε, initial state, V) appear only in Appendix B.
   - Appendix D is never referenced: reference it or cut it.

9. **Wording and technical provisos.** *Minor; about 1 h total.*
   - **p. 5:** "general-purpose coupling changes which configuration a development seed reaches, not which can exist" is false as stated. At θ = 1.2 only 2 of the 23 configurations stable at θ = 0.6 remain. Intended meaning: selector capture does not *require* strong coupling.
   - **p. 6:** "β ≥ 0.6 never fires": see the table in 1a.
   - **Cor. 3:** add the quadratic-cost proviso.
   - **State c_i > 0.**
   - **Prop. 3:** add the capacity-cost proviso.
   - **Prop. 4(c):** "no capture attracts every state…" should read "every share tends to zero from every state with all shares below one".
   - **Abstract:** "decentralized and exact certificates" should become "decentralized sufficient certificates (rows) and an exact joint test (the core)".
   - **p. 13:** the 0.85 inbound conversion ignores capacity cost (0.83 normalized), while the 0.89 threshold includes it.
   - **Mixing assumption:** state that x_E (practice share in evaluation) is identified with the in-lineage fraction of the panel.
   - **Reset assumption:** state the horizon-reset behind L_i.

10. **"Meta-attractor" and "a definition" as a contribution.** *Minor; 20 min.* The paper admits "not new mathematics" (p. 3). Demote contribution (1), or merge it into (3)/(4), so the term reads as vocabulary rather than a claim.

11. **Figures.** *Minor; 1 h.*
    - Fig. 3(d), p. 7: the "never" label is clipped to "nev". The node sits at x = 0.605 with xmax = 0.7. Move it or set `clip=false`.
    - Fig. 1, p. 3: the "development" label overlaps the D–S arrow, the D–F arrow crosses "harm h", and the φ edges are not drawn.
    - Fig. 3(a–b): six series decoded only from the caption; poor in grayscale. Use direct labels or markers.

12. **Citations.** *Minor; 10 min.*
    - Laurito et al. (2025, PNAS) omits co-author Ada Böhm.
    - All 2026 items verified: Awuni et al. arXiv:2609.17857 (same-family lift 3.4–8.4 pp); Żatuchin arXiv:2610.00369 (posted 30 Sep 2026); Li et al., ICLR 2026.

## 5. Could it be an important paper that advances alignment?

**Directly: not as a technical alignment advance in its current form; yes, potentially, as a contribution to keeping AI oversight correctable ("field alignment").**

Its alignment-relevant core consists of three checkable handles:
- an overseer-independence criterion: inbound conversion below one, counted in control units (Prop. 4d, Remark 2);
- the delay-versus-silence distinction for lineage-shared judges (Prop. 6, Remark 3);
- the appropriability lever predicting when organizations will invest in shaping evaluation (Prop. 2).

These bear on RLAIF, LLM-as-judge, AI control (a trusted monitor of different provenance is literally a firewall) and, most of all, on automated AI R&D, where model lineages write their successors' evaluations, data and red-team attacks. There, "selecting the selectors" becomes literal and runs at machine speed while τ_d stays institutional.

Whether it becomes important hinges on two things it lacks:
1. an estimate of β and inbound conversion for a real oversight pipeline;
2. a version in which the heritable carriers are model lineages (training dispositions that shape evaluators) rather than organizations.

With those, it could become a standard reference model for "evaluation capture". Without them it will be read as a careful, well-argued theory paper: a good IASEAI paper, not a field-changing one. The frequency-dependence point (item 2 in Section 4) is the most promising route to a sharper, more surprising claim: concentration is a precondition for selection on control capacity.

## 6. Three-day plan (priority order) and what not to spend time on

**Day 1 (Fri 3 Oct)**
1. **Fix the carrier specification and turn it into a result (3–4 h).**
   - In their `carrier.py`, change the keyed-stock source from Σ_j b̂_ij X_j to Σ_j b̂_ij x_jk (an own-share variant) and rerun.
   - Report the threshold shift and the invasion barrier in two or three sentences in Section 4, plus a robustness line in Appendix B. Optionally add a dashed curve to Fig. 2.
   - State the representative assumption explicitly if you keep it.
   - Add the "return ∝ size², concentration precondition, fragmentation lever" sentence to Sections 4, 7 and 9.
   - Fix Field prediction (a).
2. **Rewrite the abstract and intro paragraphs 2–3 for a mixed audience (2–3 h).**
   - Target about 160–180 words for the abstract (currently 203).
   - Drop "exactly when" and the "kernel" jargon.
   - State the three conditions and the cross-domain amplification in plain words.
   - Add the delay-versus-silence takeaway.
   - Add one sentence on automated AI R&D (the RSI theme).
   - If the submission system holds a registered abstract, update it too.
3. **Related work (1.5–2 h).** Add Olson, Tullock/Grossman–Helpman, Krakauer–Page–Erwin (revise the "closest precedent" sentence), Nelson–Winter, Kleinberg–Raghavan, issuer-pays ratings and auditor rotation; optionally Harre 2025. Consider replacing or supplementing the Hamilton analogy: χ is closer to the excludable share in Olson's logic, or to "monopolizability" in niche construction, than to relatedness.

**Day 2 (Sat 4 Oct)**

4. **Clarity and self-containedness (3–4 h).** Use the roughly 1.4 spare pages to *decompress*, not to add material:
   - a half-column notation/glossary box;
   - one-line proof ideas after Props. 1, 4, 5 and 6;
   - fix the forward reference (introduce the six-domain field before the Section 4 illustration, or move that illustration after Section 5);
   - re-anchor the hysteresis claim in the main text (n = 1 bistability or a compact Fig. 4);
   - merge the four-item contribution list with the Statement of Contributions;
   - trim "Layers of closure", "Test closures" and "Existing instruments" if space is needed;
   - optionally add a short worked example: an RLAIF judge pipeline with E = judges, x_E = in-lineage share, β = in-lineage lift, and a firewall of judges with different data, funding and lineage.
5. **Wording and technical provisos from Section 4, item 9 (1 h).**
6. **Figure fixes (1 h):** Fig. 3(d) label, Fig. 1 overlaps, grayscale-safe legends.

**Day 3 (Sun 5 Oct; submit well before AOE)**

7. **Build with pdfLaTeX and the official style (1–2 h).**
   - Confirm the main text still ends by page 10 (it ends on p. 9 now; Times metrics should keep it there).
   - No Type 3 fonts; no overfull boxes; metadata free of author fields.
8. **Supplementary code (1 h).**
   - Regenerate all numbers with the updated specification.
   - Anonymize the package: I could not inspect `build.sh`, the caches or zip metadata, so check them for paths and usernames.
   - Include a README.
9. **Final anonymity and citation sweep and proofread (1 h).** Fix the Laurito author list. Keep about 2 h of buffer.
10. **After submission:** prepare rebuttal notes for items 1, 3, 5 and 6 of Section 4. IASEAI has an author-response phase.

**Do not spend time on**
- LLM-agent experiments or the Appendix C protocol.
- Calibrating parameters to ecosystem data.
- New theory: strategic masking, within-domain competition, endogenous domains.
- Further polishing of Appendix A beyond the provisos.
- Expanding the meta-attractor or closure philosophy.
- New large figures.
- Converting `\input` figure files to a single source. AAAI camera-ready requires a single file with no `\input`, but that comes later.
- Pruning unused references.bib entries (invisible in the PDF).

## 7. Presentation, format compliance and anonymity

**Title.** Memorable and accurate. "AI Evaluation" undersells the scope (standards, procurement, formation) but is the best hook for this venue. Consider signalling the conditional result: "Selecting the Selectors: When Does Selection Favor Control over AI Evaluation?" This also pre-empts "all optimization seeks control". Low priority.

**Abstract.** 203 words in seven heavily nominalized sentences: "appropriable, persistence-weighted return", "quadratic form … whose kernel…". "Exactly when" invites the tautology critique (Section 4, item 1). "Decentralized and exact certificates" conflates two results. "Derive tests" should be "propose tests". It omits the most accessible finding (delay versus silence).

**Framing.** The intro question is clear and well placed (p. 1). The positioning in structural and multipolar risk (p. 2) is apt. "Aligning each system to its operator does not bound any of this" (p. 1) is defensible via Cor. 3 but reads as combative to alignment reviewers; "is not sufficient" lands better.

**Oversell**
- "Exactly when" (abstract, p. 1).
- "Exact certificates": exact only within the model, and R_ij is unidentified without the counterfactual c_i.
- "With no change in costs" (abstract): capacity carries per-decision cost in the simulation, so say "baseline costs".
- Field prediction (a) as worded.
- Calling the kernel "the cross-domain conversion that also decides whether capture is stable": it is the cultivated component of that matrix.

**Undersell**
- The row-sum certificate as a certifiable independence standard (the venue has a standards-and-certification theme).
- The identification strategy (p. 8).
- "A way of succeeding can outlive its origin" (p. 5).
- Delay versus silence (p. 6).
- The concentration implication of the quadratic return (absent).

**Terminology and notation**
- Overloaded symbols:
  - 𝒞 (configurations), C(q) (capacity cost) and c_i (baseline cost);
  - S (standards domain), 𝒮 (seed sets), 𝒮_k (cascade steps) and s_i (inbound conversion);
  - E (evaluation domain) and E[·] (expectation, App. A);
  - R (normalized conversion) and 𝓡 (reachable set).
- Rename the capacity cost (e.g., Γ(q)) and the reachable set.
- Add a notation box.
- "Practice / carrier / type / lineage" drift between Section 4 and Appendix B.
- c_i > 0 is unstated.

**Figures and tables.**
- Fig. 1 (p. 3): useful; fix overlaps; draw or explain the φ edges.
- Fig. 2 (p. 5): clear; revise per item 2 of Section 4.
- Fig. 3 (p. 7): informative; clipped "nev"; legends only in the caption.
- Table 1 (p. 7): good; a column naming the parameter each indicator informs (b_ij, χ, d_i, β) would tie it to the model.
- Table 2 and Fig. 4 (p. 14) are correctly placed in the appendix. Fig. 4 is the best candidate to promote if space allows.

**Statement of Contributions (p. 2, bold run-in paragraph).**
- Compliant with the IASEAI requirement: clearly indicated, states the novelty, and situates the work against "informal, non-peer-reviewed essays" without naming venues or authors.
- It also satisfies the "≥ 50% new technical content" rule.
- Improvements:
  - say explicitly that no earlier published version exists;
  - say what is new in Sections 5–6 relative to the k-core and threshold literature: stability of the joint share–rule dynamics, re-absorption via inbound conversion, keystone re-absorption under feedback, and the lineage-masking delay law. The current wording ("continuous-time analogues … which we cite") undercuts Section 5;
  - merge with the duplicated four-item list on pp. 1–2.

**Format compliance**
- **The main text ends on page 9, right-hand column, about one-fifth of the way down.** The Conclusion begins at the bottom of the left column and is followed immediately by the References heading.
- Main text is therefore pp. 1–9 (about 8.3–8.6 pages), well under the 10-page limit, with about 1.4 pages of slack.
- References run pp. 9–12. Appendix A begins mid-left-column on p. 12. Appendices A–D run to p. 14.
- All main-text figures and tables are within the limit: Fig. 1 (p. 3), Fig. 2 (p. 5), Fig. 3 and Table 1 (p. 7). Table 2 and Fig. 4 come after `\appendix` (p. 14) and are not counted.
- AAAI two-column layout, US Letter, no page numbers, anonymous author block and submission footnote are present.
- Built with tectonic/xdvipdfmx using TeX Gyre Termes and LM Roman (not penalized). Re-check pagination after the pdfLaTeX build. The `/TemplateVersion` pdfinfo will appear under pdfLaTeX.
- Camera-ready only: AAAI requires a single `.tex` source with no `\input`, and the figures are currently `\input` files.

**Self-containedness.** Adequate for the argument (all results are stated in the main text), with the weaknesses already listed: no proof ideas, simulation parameters and hysteresis support only in Appendix B, an orphaned Appendix D, and a forward reference on p. 5.

**Anonymity: clean.**
- **PDF text:** no names, affiliations, URLs, project names, acknowledgments, funding, or first-person references to prior work.
- **PDF metadata:** Creator "tectonic", Producer "xdvipdfmx (0.1)", CreationDate 2026-10-02T10:09:44Z. No Author, Title, Subject or Keywords; no XMP; no annotations or links.
- **Decompressed PDF streams:** no file paths, usernames or e-mails; the only URLs are font-licence strings (ams.org).
- **LaTeX sources:** only template comments; the bib has no self-identifying entries.
- **Supplementary code I could read** (`figures.py`, `field.py`, `carrier.py`, `checks.log`): no identifying strings.
- **Risk:** distinctive phrases ("meta-attractor", "selecting the selectors") could lead a reviewer to the antecedent essays. A web search for "meta-attractor" with AI safety terms found nothing identifying, so the risk is low. The IASEAI'26 policy allows preprints but forbids linking or mentioning them; the generic Statement of Contributions mention is compliant.

## 8. Sources

**Venue information**
- IASEAI'26 Paper Submission Guide (double-blind rules, preprints, Statement of Contributions wording, 10-page main text, appendices optional for reviewers, review criteria, ≥ 50% new content): https://www.iaseai.org/IASEAI%20'26%20Paper%20Submission%20Guide.pdf
- IASEAI'26 proceedings, AAAI Press (300 submissions, 57 archival; mix of paper types): https://ojs.aaai.org/index.php/IASEAI/issue/view/741
- IASEAI'27 programme page (the deadline used is the 5 Oct 2026 AOE given in the brief; the page is script-rendered): https://www.iaseai.org/our-programs/iaseai27

**Formatting**
- AAAI-27 submission instructions (general format): https://aaai.org/conference/aaai/aaai-27/submission-instructions/
- AAAI LaTeX formatting instructions (single source file, no `\input`, camera-ready): https://courses.cs.umbc.edu/graduate/678/fall20/AuthorKit21/LaTeX/Formatting-Instructions-LaTeX-2021.pdf

**Citation verification**
- Awuni et al. 2026: https://arxiv.org/abs/2609.17857
- Żatuchin 2026: https://arxiv.org/abs/2610.00369
- Laurito et al. 2025 (full author list including A. Böhm): https://www.pnas.org/doi/10.1073/pnas.2415697122
- Itao & Kaneko 2025: https://www.pnas.org/doi/10.1073/pnas.2500960122
- Li et al., ICLR 2026: https://iclr.cc/virtual/2026/poster/10008112 and https://arxiv.org/abs/2502.01534

**Prior art**
- Krakauer, Page & Erwin 2009, "Diversity, Dilemmas, and Monopolies of Niche Construction", *Am. Nat.* 173(1): 26–40: https://www.journals.uchicago.edu/doi/abs/10.1086/593707
- Harre 2025, "From Firms to Computation: AI Governance and the Evolution of Institutions": https://arxiv.org/abs/2507.13616
- Other suggested references are standard works cited from my own knowledge; verify bibliographic details before adding: Olson 1965; Tullock 1967; Grossman & Helpman 1994; Nelson & Winter 1982; Kleinberg & Raghavan 2021 (*PNAS*); Bolton, Freixas & Shapiro 2012 (*J. Finance*).
