# What in the corpus could strengthen the paper: subagent survey (2026-10-02)

*AI survey. Ren asked for "a sub agent to research which of our current theories could serve as good supplements and improvements". The surveyor was a Claude Opus 5.5 subagent. It read NOTES.md, main.tex, the corpus maps, the meta-attractor, alignment, zhishan and keep-the-possibility-space-open READMEs, the 09-28 v2 paper and its reviews, research-line v0.6 and v0.8, whitepaper v1.1 §11.3–11.4, the diagnostic worksheet, reading notes out-cb-02/03, and CRITIQUE-FINDINGS. It changed no files.*

*The report is kept in the session log rather than reproduced here; this file summarizes it faithfully, section by section, with its file pointers. Every suggested insertion text in it is AI-drafted from mostly AI-drafted corpus material. Only two items are in Ren's own words: the 2026-08-14 Bonfire work order, and the 2024-07-28 game-design line ("a winner of the game should be rewarded with anything other than more advantages of the game").*

## A. Before 5 October (ranked; about 1.0 page in all)

1. **Why the alarm cannot be recalibrated.** Add a remark after Prop. 4 restoring the 09-28 v2 indistinguishability lemma (§6.1) and "capture lowers the effective alarm" (§6.2). Inverting Eq. (5) needs βx_E, which only an independent channel reveals. y identifies V only up to [max{0,(y−βK)/(1−β)}, y]. With noise, any rule on y alone errs with probability at least ½(1−TV) (Le Cam; Tsybakov). A second channel's gap βx_E(K−V) measures masking directly. Present it as a standard two-point argument, not a theorem.
2. **Formation lowers the neutral benchmark.** Set c_i(x_F) = c⁰_i − g_i x_F. Formation then enters through what counts as a cost: the conceptual capture of the meta-attractor README (claim 129), and Lukes's third dimension of power. The system stays cooperative. Captured formation rescales every row it reaches by c⁰/(c⁰−g), and if g ≥ c⁰ the practice holds the domain with no rule support. In §8, the convertibility test needs an independently formed baseline.
3. **Social-science prior art the paper does not cite.**
   - Espeland & Sauder 2007 (AJS 113(1)), on the reactivity of rankings: "the metric survives its own refutation" is their empirical finding.
   - Ostrom 2005 (operational versus constitutional-choice rules: r_i sits at the second level).
   - Krippner 2011 (financialization).
   - Conrad 2005 (JHSB 46(1), medicalization).
   - Claim only the coupling across domains and into the selectors.
4. **A precise closure test.** Restore the custody-rule qualifiers that §7's third question drops: "legitimately" and "merely because custody changed"; and "the key includes data, tooling, skills and successors". Tie the test to relative reachability and attainable utility (Krakovna et al. 2019; Turner et al. 2020), applied to institutions. Apply it to the paper's own remedies.
5. **Keep exit cheap.** Portability, interoperability and substitutable suppliers bound the dependence channel b¹ of Remark 3. A degradation shock cannot make domain i capturable when s¹ < 1 − s⁰. Do not import the Fork theory's strong exit claims; CRITIQUE-FINDINGS (Hirschman, Tiebout) rules them out.
6. **Recursion.** When models write evaluations, generate data and red-team their successors, conversion into evaluation and formation is automated. The selectors then gain machine speed while τ_d does not. Add a test to §6: divergence between in-loop and independent evaluation as the share produced by the same lineage rises (research-line v0.8 §九, row 5).
7. **A documented case: 737 MAX recertification.** The regulator kept compliance findings rather than delegating them (FAA 2020; DOT OIG 2023, verified 2026-09-28/29). That is a cut in inbound conversion into E. Use the field reading (training costs, materials, delegated certification) only if verified against the House T&I report (2020) and JATR (2019).
8. **Precision fixes:**
   - (a) name the independence axes: failure mode, funding, test data, compute and access, and power to trigger correction;
   - (b) add a test for persistence across carriers;
   - (c) say when a reform is absorbed, and that conversion estimates can themselves be captured;
   - (d) AI's effect is conditional on adoption, permissions and scale;
   - (e) sunsets with a legitimacy test: name the harm prevented and who acts when the rule fails (the Bonfire work order, Ren's words);
   - (f) the thresholds are row sums over captured sets, not R₀ (no capture is always stable).
   - Optional: (g) Ren's 2024-07-28 line; (h) one sentence on the non-destructive meta-attractor; (i) the worksheet's example of falling risk reports as masking; Appendix C as the experiment protocol.

## B. Journal version or follow-up papers

1. **Estimate conversion and masking.** Use the Table 2 indicators, the semantic-similarity component of the capture index, and the data sources the corpus names but never pulled. Pre-register.
2. **Mathematical extensions:**
   - Hirsch's generic convergence;
   - stochastic stability;
   - the race of Remark 2 as a proposition;
   - strategic masking and multiple practices;
   - a panel lemma: median aggregation is robust only if errors are decorrelated.
3. **One chain across the two papers.** Capture of E acts as delay in the 09-28 correction window. Decide which paper owns which results.
4. **Case studies with a method:**
   - the 737 MAX as a case spanning several domains;
   - the rankings withdrawals of 2022–23 as a natural experiment;
   - medicalization;
   - 科举 → 八股 as the hardest self-objection;
   - at least one negative case.
5. **Answerability as a design theory.** A crosswalk among the custody rules, reachability and attainable utility, Hirschman, and the independence axes. A two-practice model with a correction-reinforcing practice P*, and a better settlement of the impossibility-versus-reallocation debt.
6. **Apply the model to safety and evaluation institutions themselves.**

## C. Do not add

- **The covariance argument and its indices** (ẇ = λCw, CAOC, PDI, eigenvalue budgeting, PWC/SC/CI/DE/ES). Its defects are open and it is known prior art.
- **Unsourced magnitudes** ("60–70% captured").
- **The historical layer** in this version.
- **The corpus's own vocabulary and stances** (开/闭, 生生, planetary technology, "do not fight for us", 大同): out of register and identifying.
- **Prescriptions addressed to models.**
- **Strong claims about models** ("cannot safely train an uncaptured AI", "LLMs instantiate will to power").
- **The rest of 09-28 v2**, apart from the lemma and the public 737 MAX facts.
- **Exit in its strong form.**
- **Terminal imagery and dated timelines.**
- **Internal AI reviews used as warrants.**
- **Private agent-fleet details.**
- **Also:** the Lean layer, Ren's sense of inner/outer alignment, and the community-mission documents.
- **Agrees with omitting Forsgren.**

## D. Three opportunities for technical alignment researchers

1. **Convertibility in a field of LLM agents.**
   - Setup: about 16 agents from at least three families, over four domains (D tasks, E judge and rubric, S standard, F few-shot curriculum), 40 rounds and 10 seeds per arm.
   - Arms: conversion off versus on; diagonal-only versus coupled; a reform arm with and without a firewall; a ramp arm for hysteresis.
   - Measures: the share of P, rubric drift, the gap between in-loop and held-out judges (masking), and the time to relapse.
   - Falsifiers and boundary conditions are drawn from v0.8 §十.
2. **Reward models and LLM judges as the selector channel.**
   - β ≈ lineage overlap × self-preference.
   - Predictions:
     - optimizing against a same-lineage judge preserves the blind spots the two share;
     - no recalibration recovers true quality without an independent channel;
     - divergence grows with the share of model-generated items;
     - panels help only if their errors are decorrelated.
   - Position against Gao et al. 2023 (verify).
3. **Formation: corpus contrast and evaluation-mediated subjectivation.**
   - The test: at matched capability, models reinforced on competitive corpora should reach for dominating strategies more readily (v0.6 §九, prediction 2).
   - Also measure them as judges, as a direct estimate of conversion from F into E and of β.
   - Only behavioral differences count.
   - Prior art outside the corpus (verify): Betley et al. 2025; Lynch et al. 2025; self-fulfilling misalignment.
