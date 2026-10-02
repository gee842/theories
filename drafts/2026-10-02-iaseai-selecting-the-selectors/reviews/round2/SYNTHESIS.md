# Round 2 review of v2: synthesis (2026-10-02)

*Written by Claude Opus 5.5, which drafted the paper, after Ren asked "do another round of independent review like before, how ready is this for the reviewers?". Four AI reviewers worked independently, set up as in round 1: R1 alignment (Fable 5.1), R2 mathematics (Opus 5.5), R3 governance (Fable 5.1), R4 area chair (Opus 5.5). They saw only the anonymous PDF and its sources, not NOTES.md, the round-1 reviews or the corpus. Their reports are in this folder verbatim.*

## Verdict

| Reviewer | Recommendation | P(archival) as is | After the fixes they list |
|---|---|---|---|
| R1 alignment | weak accept (borderline to weak accept) | ~35% | ~50%; ~60% with a reduced Appendix C simulation |
| R2 mathematics | borderline, leaning weak reject as submitted | ~25% | 35–40% |
| R3 governance | weak accept (upper borderline) | ~30% (25–35%) | not estimated |
| R4 area chair | borderline split, decided by the AC | ~30% (20–40%) | ~45% (35–55%) |

The base rate is about 19% (IASEAI'26: 57 archival papers from 300 submissions). In round 1, v1 drew "borderline / weak reject" from every reviewer, and the area chair put it at 30–40% as is.

The reviewers agree on four points:
- v2 is more rigorous than v1.
- The proofs are correct.
- The numerics reproduce byte for byte. R2 got identical checks.log, cache and figure files from a clean run; R1, R2 and R4 each confirmed the numbers with independent code.
- The central question is the right one, and the certificates and re-absorption results have policy bite.

None of them found a fatal problem. All four found errors a technical reviewer could locate within an hour, and all four found the novelty claim overstated against prior art the paper does not cite. **As it stands: about 30%. With the must-fix list below: about 45%.**

## Must-fix: errors and gaps raised by two or more reviewers, or checkable

1. **The Fig. 2 simulation does not implement Eq. (3)** (R1, R2, R4; confirmed in this session).
   - Eq. (3) drives a carrier's appropriable support from its *own* success. carrier.py uses the whole practice's success ("representative carriers"), and says so only in Appendix B.
   - Under the faithful own-share version:
     - the χ threshold from equal shares rises from 0.25 to about 0.55;
     - χ = 0.3 and 0.5 fail;
     - a 1% high-capacity type cannot invade even at χ = 1.
   - Session check, own-share keying, equal start: χ = 0.3 and 0.5 fail; χ = 0.6 captures everything by t ≈ 290; χ = 0.8 by 220; χ = 1.0 by 206. With a 1% start, every χ from 0.3 to 1.0 fails.
   - All three reviewers suggest turning this into a result. The return scales with the carrier's own size, so capacity is selected only in carriers that are already large and cannot invade from rarity. Concentration is a precondition, and fragmentation lowers the return.
2. **The aggregation behind the ratchet leaves out the capacity cost** (R2). The aggregate is (B⁰ + q̄B̂, c + γq̄).
   - Prop. 3(i) needs c_i b̂_ij ≥ γ b⁰_ij, which holds in the paper's parameters. Without it there are counterexamples.
   - It also needs q̄ uniform across domains, which fails in the paper's own run.
   - The scripted frozen-capacity counterfactual omits the cost that its log line claims.
3. **Checkable false or overstated statements** (R2, R4; R1 on some):
   - "minimum keystone set is NP-hard". Under the paper's definition it is greedy and polynomial; the NP-hard problems are emptying the core and budgeted maximum collapse.
   - Field prediction (a) ("holding size fixed … superlinearly"). At fixed total size the return is Y²cL[φ̂ + (η̂−φ̂)/|S|]: bounded, and increasing only if φ̂ > η̂.
   - Remark 3: β = β⁰ + β¹x_F does not make mixed panels fail, because β multiplies x_E. A formation term is needed, Ṽ = V + min{1, βx_E + β_F x_F}(K − V).
   - Cor. 3's factor 1 + α holds only for quadratic cost.
   - "β ≥ 0.6 never fires" is false at β = 0.6 with μ = 10⁻⁴; the alarm fires at t ≈ 2,360.
   - 0.88 should read 0.96.
   - "Not which can exist" is false as worded.
   - "Keystone status shifts … to sets of selectors" misdescribes Appendix B.
   - The abstract's "kernel … that also decides whether capture is stable" is inexact (the kernel is the cultivated part only).
4. **Oversight paragraph** (R1, R2, R3). AI control's trusted monitor is a weaker model from the same provider (GPT-3.5 monitoring GPT-4), trusted for incapacity, not provenance. In debate the judge is weak, not dependent. "Earlier winners" overstates weak-to-strong.
5. **Novelty and positioning** (all four). Missing works:
   - Niche-construction dilemmas: Krakauer, Page & Erwin 2009; Lehmann 2008; Kylafis & Loreau 2008. These, not Gerlee & Anderson, are the closest precedent for χ.
   - Collective action and rent seeking: Olson 1965; Tullock 1967; Grossman & Helpman 1994; Bombardini & Trebbi 2012.
   - Appropriability: Arrow 1962; Teece 1986.
   - Standard setting: Lerner & Tirole; Simcoe 2012.
   - Certification and ratings: Lizzeri 1999; Strausz 2005; Bolton, Freixas & Shapiro 2012; Lerner & Tirole 2006 (forum shopping).
   - Institutional change: Greif & Laitin 2004; Mahoney & Thelen 2010, whose "conversion" means something else.
   - Field theory: Bourdieu; Fligstein & McAdam; DiMaggio & Powell.
   - Audit and rankings: Power 1997; Espeland & Sauder 2007.
   - Capture theory: Laffont & Tirole 1991; Carpenter 2010; Che 1995.
   - Routines: Nelson & Winter.
   - Already in references.bib but uncited: Kleinberg & Raghavan (monoculture) and Hofbauer & Sigmund (replicator dynamics).
   - Alignment side: Eisenstein et al. 2023 (ensembles share errors); Kenton et al. 2024 and Khan et al. 2024 (LLM-judged debate); Turner et al. 2021 and Carlsmith 2022 (power-seeking).
   
   The novelty sentence should read "new results in this setting, obtained with standard tools".
6. **β and the measured lift** (R1, R3, R4). A pairwise preference lift in percentage points is not the masking fraction β. Mark the inference as heuristic or drop it, give the estimator from Appendix C, and hedge the two September-2026 preprints.
7. **Citation glosses** (R3).
   - Büthe & Mattli argue institutional complementarity, not firm expertise; cite Mattli & Büthe 2003 for power in standard setting.
   - Carpenter, Zucker & Avorn 2008 concerns deadline pressure, not funding dependence, and is contested.
8. **Bibliography** (R3, R4; checked in this session).
   - Laurito et al.: Ada Böhm is missing; the citation should read 122(31).
   - Goel et al.: PMLR 267:19621–19678.
   - Greenblatt et al.: PMLR 235:16295–16336.
   - Narechania & Sitaraman: 43 Yale L. & Pol'y Rev. 95.
   - Kwak and Carpenter & Moss: make the years consistent.
   - EU AI Act: give the Official Journal reference.
   - Abdalla & Abdalla: wrong entry type.
9. **Precision.**
   - State c_i > 0 as a standing assumption.
   - Prop. 2(iii): the proof should say "quadratic, monotone because M ≥ 0", and the statement "nondecreasing".
   - Cor. 1 under convex cost (C′(0) = 0), and its part (e).
   - Prop. 4(c): fix the wording.
   - Prop. 5(ii): say "near the reformed equilibrium".
   - Remark 1: retitle it "from the report alone"; β unknown is the hard case.
   - Remark 3: make the inequality strict.
   - State the per-horizon reset of ζ behind L_i.
   - Table 2 caption: the ψ and μ blocks are at β = 0.
   - Say which μ each number refers to, and give the √μ rule in the main text.
   - Say that x_E is reinterpreted as panel composition.
   - Prediction (d): panel composition, not item provenance.
   - Soften "any heritable trait … obeys the same condition".
   - Reference Appendix D from the main text, and note that its two last figures use T = 20.
   - The fivefold rise in the return to capacity comes from ψ̂ = 0.1; say so.
10. **Figures.**
    - Fig. 3(d): "never" is clipped.
    - Fig. 1: the "development" label overlaps an arrow, and the D–F arrow crosses "harm h".
    - The six series are decoded only from the caption.

## Strongly recommended by one or two reviewers

- **Alignment claim** (R1, R4). Write "not sufficient" instead of "does not bound". Alignment enters the model only through the cost of conversion, and the assistance effect is two-sided.
- **Tautology objection** (R4). Drop "exactly when" and claim the derived structure of the return.
- **Governance actionability** (R3):
  - the expertise–independence trade-off;
  - a table of principles, each marked derived, mapped or normative;
  - a parameter → proxy → status mapping, or an indicator column in Table 1;
  - a stylised worked row;
  - existing instruments: SOX/PCAOB, issuer-pays reform and random assignment, regulatory markets, DRCF, CEN-CENELEC JTC 21, the GPAI Code of Practice, and pre-deployment access agreements of AI safety institutes.
- **Identification as recoverability**, plus a natural-experiment route through margin reforms (R2, R3).
- **Clarity** (R4):
  - notation overloads (𝒞 vs C(q) vs c_i; 𝒮 vs S; E[·]; 𝓡);
  - a notation box;
  - one-line proof ideas;
  - the forward reference to the six-domain field;
  - an abstract of 160–180 words;
  - one list of contributions instead of two.
- **Limitations** (all). Frequency-independent payoffs make capture all-or-nothing; strategic masking is absent.

## Where the reviewers disagree

- **Experiment.** R1 says a reduced Appendix C simulation is the biggest single gain. R4 says not to spend time on experiments before the deadline.
- **Space.** R3 wants more governance content (tables, a worked row). R2 wants to trim constructs no result uses: layers of closure, answerability, error-access graphs. R4 wants to decompress rather than add.

## Recommended plan for v3 (about 1.5 days, leaving buffer before 5 October AOE)

1. **Carriers.**
   - Switch Fig. 2 to own-share keying, as Eq. (3) states.
   - Add the size result: capacity pays only for large carriers, and a rare high-capacity type cannot invade. Describe the representative regime as the single-dominant-lineage case.
   - Fix the aggregation, adding the cost and the ratchet condition.
   - Fix the counterfactual.
2. **Corrections.** Every item in must-fix 3, 4 and 6–10, using the reviewers' replacement text where given.
3. **Positioning.** A paragraph on collective action and niche construction; a paragraph on certification and institutional change; the novelty sentence; the Statement of Contributions merged with the contribution list.
4. **Framing.** Rewrite the abstract and the alignment claim.
5. **Governance.** Mark each principle as derived, mapped or normative; add the expertise–independence trade-off and the instruments; tie Table 1 to model quantities.
6. **Numerics and build.** Rerun figures.py with the new carrier model and the √μ statements; build; check pages; run an anonymity sweep.
7. **Optional, if time remains.** A reduced three-arm simulation of the Appendix C protocol.
