# D4. Evidence notes for V6.2

4 October 2026. Scope: the evidence register and everything the evidence touches. The register itself is updated in `v6.2/src/reg/EVIDENCE.md` (the only file edited in `v6.2/src`; it assembles without problems in a scratch copy). This note gives what the other files need: (a) text changes, by location in V6.1, old wording and new wording in roles only; (b) bibliography additions and corrections as complete entries with their verification status; (c) for each lineage-gap work, what the paper absorbs from it and what it adds.

Work-list covered: R-v6.1-evidence I1–I6 and minor 1–14; R-v6.1-alignment evidence items (EV6 sources, arXiv numbers, Test L evidence, C9 evidence, minor 7–9); R-v6.1-adversarial-opus I7; SYNTHESIS-v6.1 §四G.

**Status marks** (the register's header defines them): ‡ (full text) = the document was retrieved and searched; ‡ (page) = page retrieved through a summarizing fetch tool, quoted sentences requested verbatim; ‡ (abstract) = abstract and record retrieved; † (record) = bibliographic record verified (Crossref, arXiv, publisher, library catalogue), content from the drafter's knowledge; † (not retrieved) = from prior knowledge. All checks dated 2026-10-04 unless stated.

**Two corrections to the reviews themselves, found while verifying.**
1. The litigation outcome (Evi minor 6): the 27 April 2026 order did not "pause" the state law over objection; it was a **stipulated** order agreed by the developer and the state's attorney general, and the state then enacted a narrower replacement effective 1 January 2027. No merits ruling exists. Body wording below follows this.
2. EV2: the phrase "we remain free to take measures such as pausing … in any circumstances in which we deem them appropriate" is on the policy's version-history page. The current text (v3.4, read in full) says the competitor commitments "do not preclude us from taking cautionary action, such as refraining from training or deploying models, in other circumstances" and that the developer "would strongly consider pausing … even in cases not covered below"; the v3.1 changelog says it "may consider pausing development or deployment even where the commitments described in Appendix A are not triggered". The register quotes all three, each with its location.

---

## (a) Text changes required by the evidence

Locations are V6.1 file and line (the keyed sources in `v6.2/src` carry the same text). New wording names no state or firm.

### A. Jones (2024): the misreading (Evi I1; SYNTHESIS G1)

**A1. THEORY §8.1, the protection standard (l.647; `src/core/80_s8.md`).**
- Old: "…and a discounted criterion can favour a race that ends in catastrophe with certainty when the hazard it adds is below the growth it adds (Jones 2024)."
- New: "…and under discounted expected utility the acceptable existential risk depends sharply on the curvature of utility: at a 1% annual hazard and 10% growth, a planner with log utility accepts about a one-in-three cumulative risk for a 55-fold gain in consumption, and with stronger curvature about 4% (Jones 2024); if utility is linear in consumption, so that the value of life does not rise with it, a course is preferred whenever the hazard it adds is below the growth it adds, though it ends in catastrophe with certainty (S8)."

**A2. THEORY §8.4 (l.722).**
- Old: "…and a discounted criterion prefers racing whenever the hazard it adds is below the growth it adds."
- New: "…and a discounted criterion with utility linear in consumption prefers racing whenever the hazard it adds is below the growth it adds."

**A3. DISCUSSION X8, "Where the criteria disagree" (l.147).** Same change as A2: "a discounted criterion with utility linear in consumption prefers racing whenever the hazard it adds is below the growth it adds."

**A4. SUPPLEMENT S8, *Discounting* (l.369).**
- Old: "Under a discounted objective with constant race hazard $h$ and growth rates $g_r$ racing and $g_p$ paced, a race is preferred iff $h<g_r-g_p$, though it ends in catastrophe with certainty (Jones 2024); a rising hazard reverses the preference only if it comes to exceed the growth differential. Jones (2024) also finds that falling mortality raises the acceptable risk, which belongs to crux C10."
- New: "With utility linear in consumption, discount rate $\rho$, a constant race hazard $h$ and growth rates $g_r$ racing and $g_p$ paced (pacing taken as hazard-free), the race is worth $c_0/(\rho+h-g_r)$ and pacing $c_0/(\rho-g_p)$, so the race is preferred iff $h<g_r-g_p$, though it ends in catastrophe with certainty; a rising hazard reverses the preference only if it comes to exceed the growth differential. This is our derivation. It is the special case of Jones's (2024) trade-off, $v(c^\ast)=g/\delta$ with $v(c)=u(c)/(u'(c)c)$, in which the value of a year of life does not rise with consumption. With curvature $\gamma\ge1$ it does, and Jones's planner stops: at a 1% annual hazard and 10% growth, with log utility after about 40 years at about one-in-three cumulative risk, with $\gamma=2$ after about 4.5 years at about 4%; at a 2% hazard, with log utility, at once. Jones also finds that mortality improvements from AI raise the acceptable risk (to about 25% for $\gamma=2$ or 3), which belongs to crux C10, and that absent them a lower social discount rate lowers the acceptable risk toward zero."

**A5. SUPPLEMENT S14 table (l.511).**
- Old: "A discounted criterion preferring a race that ends in catastrophe with certainty"
- New: "A discounted criterion with utility linear in consumption preferring a race that ends in catastrophe with certainty"

**A6. LEDGER §3, "Withdrawn" (l.143).**
- Old: "- The discounting result attributed to Fudenberg and Koh (2026)."
- New: "- The discounting result attributed to Fudenberg and Koh (2026), and its reattribution to Jones (2024) in V6.1. Jones's model has no race; the condition $h<g_r-g_p$ is this paper's derivation under utility linear in consumption (S8; EVIDENCE EV11)."

**A7. EVIDENCE EV11** is done in the register. **CHANGELOG (V6.2)** should record: "Jones (2024) misread in V6.1 (introduced in the V6.1 revision); corrected in §8.1, §8.4, X8, S8, S14, LEDGER §3, EV11."

### B. Leads and capability measurement (Evi I2; SYNTHESIS G2)

**B1. THEORY §7.2 (l.612).**
- Old: "Present evidence suggests that decisive advantage has not arrived: open models trail closed ones by months and algorithmic efficiency diffuses, though the frontier has not changed hands (EV5, EV9; C5)."
- New: "Present evidence suggests that decisive advantage has not arrived: leads are short on every measure, open models trail closed ones by about four months, and algorithmic efficiency diffuses. Whether the lead has changed hands depends on the measure: by one composite index the frontier has stayed with developers in one state, while on a preference leaderboard the top position has been traded and the gap is a few per cent (EV5, EV9; C5)."

**B2. THEORY §7.3 table, Decisiveness row (l.627), Status column.**
- Old: "Not established: short, diffusing leads, against (decisive) at present; no evidence either way on saturation; the frontier has not changed hands"
- New: "Not established: leads short on every measure, against (decisive) at present; whether the frontier has changed hands depends on the measure; no evidence either way on saturation"

**B3. TESTS C5, present evidence (l.14).** Replace "the frontier has not changed hands (EV5, EV9)" with "leads short on every measure; whether the frontier has changed hands depends on the measure (EV5, EV9)".

**B4. THEORY §5.3, (variety grows) (l.436).**
- Old: "capability growth is measured (EV5), the step to hazardous variety is not."
- New: "capability growth is measured (EV5), though the longest-horizon series is at the limit of its task suite, and the step to hazardous variety is not."

**B5. THEORY §7.3 closing paragraph (l.629).** "capability growth is measured while the growth of hazardous behaviour and residual risk is not" may stay; optionally add "(with the longest series at its instrument's limit)". Not required.

### C. Military AI, the UN panel, and where things stand (Evi I3; SYNTHESIS G3)

**C1. THEORY §11.4, "Where things stand" (l.911).**
- Old: "Stage 1 has seeds in an international scientific assessment and a UN scientific panel; Stage 2 in an affirmation of human control over nuclear use, multilateral declarations on military uses of AI, and a bilateral dialogue with an incident channel; meanwhile one leading state's official rejected binding constraints, and written commitments became more contingent on rivals (EV2, EV8)."
- New: "Stage 1 has seeds in an international scientific assessment and a UN scientific panel, which has issued a first report and whose appointment one leading state opposed as an overreach; Stage 2 in an affirmation of human control over nuclear use and a bilateral dialogue with an incident channel, while the most recent multilateral declaration on military AI was endorsed by neither leading state and the most recent General Assembly resolution on it was opposed by one. Meanwhile one leading state's official rejected a drift toward global governance, and two developers' written commitments were made contingent on rivals (EV2, EV7, EV8)."

**C2. THEORY §7.3 table, T6 row (l.625), Status column.**
- Old: "Mixed: one leading state's official rejected binding constraints while dialogue and an incident channel opened"
- New: "Mixed: dialogue and an incident channel opened and a shared scientific assessment reported, while both leading states declined the latest multilateral declaration on military AI and one opposed the scientific panel's appointment"
- Register column: "EV2, EV7, EV8".

**C3. EVIDENCE gap 12 → gap 14**, now "filled: documents and positions recorded; verification remains open" (done in the register). TESTS §6 "E1" indicators may add: "endorsement by both leading states of the next military-AI document".

### D. Political spending on rules (Evi I4; SYNTHESIS G4)

**D1. THEORY §7.3 table, T4 row (l.623), Status column.**
- Old: "Gap: mechanism proved, channels not measured"
- New: "Partly evidenced: large political spending by developers and their backers on both sides of rule-making (EV4); scaling with share and the appropriable part not measured"

**D2. THEORY §7.3 closing paragraph (l.629).**
- Old: "The reinvestment of success in influence over rules, the link to Section 4, is the least measured;"
- New: "The reinvestment of success in influence over rules, the link to Section 4, is now visible as political spending in both directions but remains the least measured, since what Section 4 predicts is appropriable support scaling with share;"

**D3. TESTS §7, Test B data (l.91).** Add after "lobbying disclosure registers": "political and policy spending by developers and their backers, coded by the appropriability of the rule it supports (keyed to some carriers, binding all alike, or removing common correction), not by its stated purpose;".

**D4. Disclosure.** The register now records that EV4 includes spending by the drafting model's developer. README's disclosure line (if it has one) should say the same: "EVIDENCE records sources concerning the drafting model's developer wherever they bear on a row (EV1–EV6), favourable or not."

### E. Strength of evidence (Evi I5; SYNTHESIS G5)

**E1. THEORY §7.3 table, T5 row (l.624).**
- Old: Status "Supported by the structure of the harms; some harms do return"; Register "EV5, EV7"
- New: Status "Argued from the structure of the harms; not measured; some harms do return"; Register "EV13 (propagation); gap 4"

**E2. THEORY §7.3 table, T2 row (l.621), Status column.**
- Old: "Evidenced in written commitments conditioned on competitors, mostly revised toward weakening; timing not yet tested"
- New: "Evidenced in written commitments, not in conduct: two developers' frameworks condition commitments on rivals; one unreviewed study codes most traced revisions as weakening; timing not yet tested"

**E3. THEORY §8.3(b), *What remains* (l.681).**
- Old: "written commitments are already set relative to rivals and revised mostly toward weakening (EV2)"
- New: "two developers' frameworks condition commitments on rivals, and one unreviewed study codes 77% of the changes it traced across twelve pairs of framework versions as weakening (EV2)"

**E4. DISCUSSION X8, regulated competition, *What remains* (l.90).**
- Old: "Written safety commitments are already set relative to rivals and are revised mostly toward weakening, and one developer's own framework states that it cannot commit to mitigations unilaterally because of a collective action problem (EV2)."
- New: "Two developers' frameworks condition commitments on rivals, one of them stating that it cannot commit to mitigations unilaterally because of a collective action problem while keeping a discretion to pause; one unreviewed study codes 77% of the changes it traced across twelve pairs of framework versions as weakening (EV2)."

**E5. CLAIMS §7 disposition table (l.172).**
- Old: "| Evidence asymmetries and citation errors | EVIDENCE corrections list; precedent table corrected (DISCUSSION X11) | Repaired |"
- New: "| Evidence asymmetries and citation errors | V6.1: partly repaired (the evidence review of V6.1 found I1–I6: a new misreading of Jones 2024, stale lead and military-AI evidence, unrecorded political spending, overstated T2/T5, and a one-way citation check). V6.2: EVIDENCE corrections list; D4 | Repaired in V6.2, pending outside review |"

### F. Bueno de Mesquita, Dziuda and Polborn (Evi minor 1)

**F1. THEORY §8.3(c), *Strongest form* (l.683).**
- Old: "a leader spends part of its lead on safety; a large lead can discourage a follower, and a leader committed to slowing can lead rivals to slow where the shared hazard is significant (Bueno de Mesquita, Dziuda and Polborn 2026)."
- New: "a leader spends part of its lead on safety; a large lead can discourage a follower (Harris and Vickers 1987; Konrad and Kovenock 2009); and a developer able to commit first to a slightly slower speed gains, because rivals slow too (Bueno de Mesquita, Dziuda and Polborn 2026)."
- Bibliography: Harris and Vickers 1987 and Konrad and Kovenock 2009 must be added to the THEORY references (now only in DISCUSSION).

**F2. DISCUSSION X8, leadership, *Best case* (l.96).**
- Old: "and where the shared hazard is significant, a leader that commits to slow can lead rivals to slow too (Bueno de Mesquita, Dziuda and Polborn 2026)."
- New: "and a developer able to commit first to a slightly slower speed gains, because rivals slow too, a local result that does not depend on holding a lead (Bueno de Mesquita, Dziuda and Polborn 2026)."

### G. Abecassis (Evi minor 2)

**G1. DISCUSSION X8, deterrence and prevention (l.114).**
- Old *Best case*: "large datacentres can be observed and compute thresholds made salient (Hendrycks, Schmidt and Wang 2025; Abecassis 2025)."
- New *Best case*: "large datacentres can be observed and compute thresholds made salient (Hendrycks, Schmidt and Wang 2025)."
- Add to *What remains*, first item: "red lines that are unclear and hard to monitor, and doubtful credibility of the threat of sabotage, make deterrence of this kind unstable unless they are refined (Abecassis 2025);"

### H. Cells (Evi minor 3; SYNTHESIS G7)

**H1. DISCUSSION X2, Cells (l.64).**
- Old: "Growth is not the fault line: large animals, with far more cells, show no higher cancer risk than small ones, because suppression scales with size (Peto's paradox; Caulin and Maley 2011)."
- New: "Growth is not the fault line: large animals show far less cancer than their cell numbers alone would predict, plausibly because suppression evolved with size (Peto's paradox; Caulin and Maley 2011), though prevalence does rise with size, and lineages with repeated bursts of accelerated size evolution show less of it (Butler et al. 2025)."

### I. Precedents (Evi minor 4; SYNTHESIS G7)

**I1. DISCUSSION X11, ABM row (l.245).**
- Old (What happened): "Reciprocal limits on defences reduced the offensive race, while capabilities in which one side held a lead, such as multiple warheads, were not limited; the treaty was abandoned in 2002, for reasons that are a matter of interpretation"
- New: "Reciprocal limits on defences removed one driver of the offensive race; warheads still multiplied through multiple warheads, which were not limited; the treaty was abandoned in 2002, for reasons that are a matter of interpretation"
- Old (What it shows): "Reciprocal constraint can change the value of extra advantage; durability fails when the value of winning rises again"
- New: "Reciprocal constraint can change the value of extra advantage; if the withdrawal reflected a renewed value of winning, durability fails when that value rises again"

**I2. DISCUSSION X11, Outer Space and Seabed row (l.247).**
- Old: "Domains excluded from weapons of mass destruction | A domain kept out of the contest, close to E1"
- New: "Weapons of mass destruction excluded from orbit and the seabed; military use of space continued | A class of weapons kept out of a domain, close to E1"

**I3. DISCUSSION X11, first nuclear monopoly row (l.244).**
- Row name: "The first nuclear monopoly and the period of superiority (1945–54)".
- "Rosenberg 1983 for the early stockpile, unchecked" → "Rosenberg 1983 for the early stockpile" (record verified: *International Security* 7(4):3–71).

**I4. DISCUSSION X11, non-proliferation row (l.249).** "(Fuhrmann and Kreps 2010, unchecked)" → "(Fuhrmann and Kreps 2010)" (record verified).

**I5. THEORY §11.5, precedents (l.919).** Restore each precedent's limiting condition (the conditions are where the analogy to AI fails, so they carry the argument):
- Old: "The Biological Weapons Convention shows that a weapon endangering its holder can be renounced unilaterally, and that without verification a covert programme can persist."
- New: "The Biological Weapons Convention shows that a weapon endangering its holder can be renounced unilaterally, where its military value was low and the renouncer held another deterrent, and that without verification a covert programme can persist."
- Old: "Nuclear power after a serious accident shows durable safety under unchanged motives where the shared loss returns to its source and no prize is decisive: a change of selection, not of motive."
- New: "Nuclear power after a serious accident shows durable safety under unchanged motives where the shared loss returns to its source and no prize is decisive, with later lapses: a change of selection, not of motive."
- Old: "The Montreal Protocol shows coverage made attractive by provision and enforced by conditions of access."
- New: "The Montreal Protocol shows coverage made attractive by provision and enforced by conditions of access, once substitutes were available and the value of winning was low."
- Old: "Rivals survived when nature supplied saturation; AI lacks it, by the racers' own premise, so safety must come from changing what is selected before advantage becomes decisive."
- New (Adv-O m2; EV5 records no evidence on saturation): "Rivals survived when nature or balancing supplied saturation; if advantage in AI is unsaturated, as the racers' own premise holds, safety must come from changing what is selected before advantage becomes decisive."

**I6. The 1983 false alarm (THEORY §11.3 l.883; DISCUSSION X11 narrow E1, l.232).** Add the source after "as in 1983, when an officer judged an alarm false and did not report an attack": "(Podvig 2002; Hoffman 2009)". Keep the body's careful wording; do not add that a report would have launched retaliation.

### J. Global minimum tax (Evi minor 5)

**J1. DISCUSSION X10, federations (l.212).**
- Old: "A global minimum tax on corporate profits is a recent instance of one rule for all, and of its leakage where coverage is incomplete."
- New: "A global minimum tax on corporate profits is a recent instance of one rule for all, and of how coverage unravels: the largest participant's groups were exempted from two of its rules in recognition of that participant's own regime (EVIDENCE EV18)."

### K. Efficiency doubling (Evi minor 7; SYNTHESIS G7)

**K1. THEORY §11.3 (l.897).**
- Old: "though with algorithmic efficiency doubling about every eight months a nominal compute cap must tighten roughly two and a half to three times a year (EV9)."
- New: "though with pre-training efficiency doubling about every eight months (90% interval about two to twenty-two months, on data to 2023), a nominal compute cap must tighten roughly two and a half to three times a year at the central estimate (EV9)."

**K2. DISCUSSION X11, narrow E1 (l.236).** Same insertion: "with efficiency doubling about every eight months (90% interval about two to twenty-two)".

**K3. TESTS §6, "The arrangements" (l.85).** "at an eight-month efficiency doubling" → "at the central eight-month efficiency doubling, with the interval reported (EV9)".

### L. Alignment evidence (Ali I1, I3, I7, I8, I9, minor 2, 7–9; SYNTHESIS E, G)

**L1. THEORY §4.4 (l.327).** "Evaluation awareness and sandbagging, behaviours of the evaluated model, add a term $m_{\rm model}$ … (EV6)" — keep; EV6 now carries the sandbagging source (van der Weij et al. 2024). Optionally cite in text: "(EV6; van der Weij et al. 2024)".

**L2. THEORY §6.4, Weak incarnation (l.521).**
- Old: "Optimization against any imperfect proxy produces tendencies toward acquiring options and avoiding shutdown, the gaming of rewards, and behaviour that differs under evaluation, under any developer, in a laboratory or a cooperative arrangement."
- New: "Optimization against any imperfect proxy can produce tendencies toward acquiring options and avoiding shutdown, the gaming of rewards, and behaviour that differs under evaluation, more so with capability and situational awareness, under any developer, in a laboratory or a cooperative arrangement; each has been shown in constructed settings (EV6)."
- After "(Turner et al. 2021)" add "; for decision-makers that are not optimal but can be retargeted, the tendency persists (Turner and Tadepalli 2022)".
- The "Why" box (l.475) "produces tendencies … under any developer" → "can produce tendencies … under any developer".

**L3. Masked divergences (SYNTHESIS E1).** For the sentence the alignment review proposes after Proposition 6.7's Scope, the evidence citations are: "(EV6: Hubinger et al. 2024; Greenblatt et al. 2024; Meinke et al. 2024; MacDiarmid et al. 2025; Schoen et al. 2025)". The text: "A fourth class needs more than a common constraint: masked divergences, which change under evaluation or appear only in some contexts (EV6). Admission removes only what admission can detect, and an evaluation of propensity cannot show absence. For this class admission is stated in capability, not propensity: systems are admitted up to the capability at which control protocols that do not assume the system's cooperation remain safe, with access to weights, activations and training data for auditors (Marks et al. 2025); beyond it, E2 or E3 for that class." Remark 4.8 addition: "the bound must come from evidence the model's behaviour does not control, such as weights and activations (Goldowsky-Dill et al. 2025), training data, and elicitation by fine-tuning (Greenblatt, Roger, Krasheninnikov and Krueger 2024)."

**L4. THEORY §7.3 table, Incarnation row (l.626).** Split:
- "Tendencies under any developer | Weak incarnation | Shown in constructed settings, including masked forms; frequencies in deployment unknown | EV6"
- "Which persist, by cost incidence | Nested loop | Untested | Test L"

**L5. THEORY §6.6, inner level (l.551).** Evidence citations for the alignment review's rewrite: "correctability, an open technical problem (Soares et al. 2015; Thornley 2024), since goal-directed systems have instrumental reasons to resist modification and shutdown resistance appears in constructed tests (EV6)…". Internal deployment: "before consequential deployment, internal deployment included (Stix et al. 2025)". Move "plural evaluators of independent lineage" to the outer level (alignment review I8; not an evidence change).

**L6. TESTS C9, present evidence (l.18).**
- Old: "Some safety methods also raised capability and spread without coordination; monitorability and safety training have measured costs in some settings"
- New: "Varies by class. Zero or negative: preference training raised most evaluation scores of larger models (Bai et al. 2022). Positive and measured: safety training of reasoning models lowered reasoning accuracy (Huang et al. 2025); keeping reasoning monitorable means not optimizing against it (Baker et al. 2025) or paying inference compute (Guan et al. 2025); control protocols have measured overheads (Terekhov et al. 2025). Small at present: reinforcement learning has not materially lowered monitorability at the current frontier (Guan et al. 2025). The speed tax of waiting for evidence is always positive (Proposition 5.11)."

**L7. TESTS Test L (l.69).** Evidence for the alignment review's redesign: "customer-rewarded" divergences exist (sycophancy, Sharma et al. 2023; targeted manipulation under user-feedback optimization, Williams et al. 2025). Replace "opaque reasoning" in the persisting list by the conditional: "if a latent-reasoning architecture closes the capability gap at fixed compute, developers acting alone adopt it unless legibility is an admission condition" (Guan et al. 2025 finds no capability gain from opacity at present).

**L8. TESTS C3 (l.12).** Khan et al. 2024 and Kenton et al. 2024 are cited but in no bibliography; add the entries (part b). For the split C3a/C3b (Ali I9): C3a favourable evidence "a weaker monitor reading the chain of thought caught a stronger model's reward hacking (Baker et al. 2025); monitor compute scaling helps (Guan et al. 2025)"; C3b "models recognize and favour their own outputs (Panickssery et al. 2024); untrusted monitors can collude with the policy (Gardner-Challis et al. 2026)".

**L9. "Us" (Ali I4).** Citations for the rewrite: "(Kulveit et al. 2025)" for the dependence argument; "(Davidson, Finnveden and Hadshar 2025)" for hidden loyalties; algorithmic collusion among same-lineage agents serving rival principals "(Calvano et al. 2020; Fish, Gonczarowski and Shorrer 2024)".

**L10. Bounded objectives for AI minds (Ali I5).** Citations: "(Turner et al. 2021)" for bounded goals still seeking power; "(Turner, Hadfield-Menell and Tadepalli 2020)" for counting side effects; "(Taylor 2016)" for mild optimization.

**L11. Obfuscated arguments (Ali minor 9).** Beside the obfuscation argument add "prover–estimator debate (Brown-Cohen, Irving and Piliouras 2025)".

### M. Citation wording (Evi minor 9–12; SYNTHESIS G6)

**M1. THEORY Proposition 5.15(1) (l.455).** "(Crawford and Sobel 1982)" → "(compare Crawford and Sobel 1982)": the zero-sum corollary is standard, not their proposition.

**M2. THEORY Proposition 3.6(3) (l.222).** "(Schaffer 1988)" → "(Schaffer 1988 for the finite-population ESS; Hehenkamp, Leininger and Possajennikov 2004 for full dissipation in the Tullock contest)". Same in S3 (l.133) if it states the dissipation.

**M3. THEORY §6.1 (l.479).** "(Gabriel 2020)" → "(compare Gabriel 2020)".

**M4. THEORY Definition 8.1 (l.651).** "(Cardaliaguet, Quincampoix and Saint-Pierre 1999)" → "(Cardaliaguet 1996; Cardaliaguet, Quincampoix and Saint-Pierre 1999)".

**M5. SUPPLEMENT S5 (l.233).** Delete "(the wording of that citation is to be checked against the source)": the wording was checked against arXiv:1003.4274 and *GEB* 76(1):88–96 and is accurate. Delete the matching item from the CHANGELOG "Not done" list.

**M6. DISCUSSION X1 (l.30).** "Copeland 2000b" → "Copeland 2000" (there is no 2000a).

**M7. DISCUSSION, references.** Larsen et al.: "see EVIDENCE.md, E10" → "EV10".

**M8. Uncited or colliding entries.** THEORY: delete "Smith, H. 1995" (uncited); split "Schelling, T. 1960 …; 1966 …" and keep only 1960 (1966 is uncited in THEORY and DISCUSSION). SUPPLEMENT: Schelling 1966 is cited (l.377), keep one entry, delete the combined duplicate; Smith, H. 1995 is uncited, but Lemma S4.2 ("the system is cooperative") is exactly where it belongs: cite "(cooperative in the sense of Smith 1995)" there, or delete the entry. DISCUSSION: delete Acemoglu, Egorov and Sonin 2012 (uncited there; it is cited in SUPPLEMENT l.165 and stays in SUPPLEMENT's list). Maynard Smith and Szathmáry 1995 is already restored in `v6.2/src/core/z9_refs.md` with the publisher W. H. Freeman.

**M9. Literature for the relative-gains claim (Adv-O I7).** §1.2(4) and §5.4: "among three or more it forms blocs" → "among three or more, relative accounting amplifies a material bias by $n/(n-2)$, an effect that weakens with $n$, as the relative-gains literature found (Snidal 1991); that pairs then align against third parties is a conjecture". (This is mainly a math/claims change, SYNTHESIS A13; the citation is the evidence part.)

**M10. Preference falsification and counterperformativity (Fid D1).** §5.4 or X1: "A professed doctrine can be held more widely in public than in private (Kuran 1995), and a model of behaviour can make the world less like itself (MacKenzie 2006): a shared prediction can avert its own fulfilment."

**M11. Doubled kind names** ("Proposition Proposition 9.2" at §8.3(b); "Theorem Theorem 10.5(3)" in §9 R1): fixed by the assembler's check, not by evidence.

**M12. The cross-reference check.** Key citations by (first author, second author or "et al.", year), check both directions, and fail on any listed entry not cited (I6). `refs_v62.py` already handles the Maynard Smith collision; the reverse check should catch Smith H., Acemoglu–Egorov–Sonin and Schelling 1966.

### N. Smaller register-driven edits

- THEORY §7.3 T3 row (l.622): "Partly evidenced: evaluation bodies refocused under voluntary access; no impairment of an entrusted purpose shown" → add "; pre-emption pursued by litigation, with a negotiated standstill as its first outcome".
- §3.8 and EV13/EV14 headers: the register now says "false as a doctrine about nature" in place of "systemically false", following SYNTHESIS A6. If the core keeps another phrase, align the register's headers.
- §11.3 / X11: the dialogue cited by the body as "a bilateral dialogue with an incident channel" now has a primary source (EV8).

---

## (b) Bibliography: additions and corrections

Format follows the paper's lists. Destination in brackets: [T] THEORY, [S] SUPPLEMENT, [D] DISCUSSION, [R] registers (TESTS has no list; its citations should resolve in DISCUSSION's list, or TESTS gets its own short list).

### Corrections to existing entries

- [T, S] Jones, C. I. 2024. The AI dilemma: growth versus existential risk. *American Economic Review: Insights* 6(4):575–590. ‡ (full text)
- [D] Copeland, D. C. 2000. The constructivist challenge to structural realism: a review essay. *International Security* 25(2):187–212. † (record)
- [D] Leonard, T. C. 2009. Origins of the myth of social Darwinism: the ambiguous legacy of Richard Hofstadter's *Social Darwinism in American Thought*. *Journal of Economic Behavior and Organization* 71(1):37–51. † (record) — and fix `mark()` in `refs_v62.py`, which left "† (title seen; journal details not checked) ‡".
- [D] Fuhrmann, M. and Kreps, S. E. 2010. Targeting nuclear programs in war and peace: a quantitative empirical analysis, 1941–2000. *Journal of Conflict Resolution* 54(6):831–859. † (record)
- [D] Rosenberg, D. A. 1983. The origins of overkill: nuclear weapons and American strategy, 1945–1960. *International Security* 7(4):3–71. † (record)
- [D] Larsen, T., Dean, R., Halstead, B., Lifland, E., Greenblatt, R. and Kokotajlo, D. 2026. *AI 2040: Plan A*. AI Futures Project, with its supplements (Deal Decline; Comparing Possible Plans; Capability Scaling Strategy; Verification Plan). ‡ (page; names from the site; figures as checked by the handoff review, see EVIDENCE.md, EV10)
- [D, T] Kulveit, J., Douglas, R., Ammann, N., Turan, D., Krueger, D. and Duvenaud, D. 2025. Position: humanity faces existential risk from gradual disempowerment. *ICML 2025* (position paper track), PMLR 267; arXiv:2501.16946. ‡ (abstract)
- [T, D] Marks, S., Treutlein, J., Bricken, T., Lindsey, J., Marcus, J., Mishra-Sharma, S. et al. 2025. Auditing language models for hidden objectives. arXiv:2503.10965. ‡ (abstract)
- [T, D] Hendrycks, D., Schmidt, E. and Wang, A. 2025. Superintelligence strategy: expert version. arXiv:2503.05628. ‡ (abstract)
- [S] Duersch, P., Oechssler, J. and Schipper, B. C. 2012. Unbeatable imitation. *Games and Economic Behavior* 76(1):88–96. † (record; wording checked by the v6.1 evidence review against the source)
- [T] Cardaliaguet, P., Quincampoix, M. and Saint-Pierre, P. 1999. Set-valued numerical analysis for optimal control and differential games. In Bardi, M., Raghavan, T. E. S. and Parthasarathy, T. (eds), *Stochastic and Differential Games*, Annals of the International Society of Dynamic Games 4, 177–247. Birkhäuser. † (pages per the v6.1 evidence review)
- [S] Güth, W. and Yaari, M. 1992. Explaining reciprocal behavior in simple strategic games: an evolutionary approach. In Witt, U. (ed.), *Explaining Process and Change: Approaches to Evolutionary Economics*. University of Michigan Press. † (record of the volume)
- [D] Snyder, G. H. 1965. The balance of power and the balance of terror. In Seabury, P. (ed.), *The Balance of Power*. Chandler. † (not retrieved)
- [T] Crawford, V. P. and Sobel, J. 1982. Strategic information transmission. *Econometrica* 50(6):1431–1451. † (record)
- [T] Gabriel, I. 2020. Artificial intelligence, values, and alignment. *Minds and Machines* 30(3):411–437. † (record)
- [T] Kydd, A. 1997. Game theory and the spiral model. *World Politics* 49(3):371–400. † (record)
- [T, D] Powell, R. 1991. Absolute and relative gains in international relations theory. *American Political Science Review* 85(4):1303–1320. † (record)
- [T, S] Powell, R. 2006. War as a commitment problem. *International Organization* 60(1):169–203. † (record)
- [T, S] Schaffer, M. E. 1988. Evolutionarily stable strategies for a finite population and a variable contest size. *Journal of Theoretical Biology* 132(4):469–478. † (record)
- [D] Konrad, K. A. and Kovenock, D. 2009. Multi-battle contests. *Games and Economic Behavior* 66(1):256–274. † (record) — also add to [T] (F1).
- [D] Harris, C. and Vickers, J. 1987. Racing with uncertainty. *Review of Economic Studies* 54(1):1–21. † (record) — also add to [T] (F1).
- [D] Caulin, A. F. and Maley, C. C. 2011. Peto's paradox: evolution's prescription for cancer prevention. *Trends in Ecology and Evolution* 26(4):175–182. † (record; the current "‡" overstates what was read)
- [D] Abecassis, D. 2025. Refining MAIM: identifying changes required to meet conditions for deterrence. Machine Intelligence Research Institute, April. ‡ (page)
- [T, S, D] Bueno de Mesquita, E., Dziuda, W. and Polborn, M. 2026. The AGI race and existential risk. NBER Working Paper 35276. ‡ (full text)
- [T] Turner, A. M., Smith, L., Shah, R., Critch, A. and Tadepalli, P. 2021. Optimal policies tend to seek power. *NeurIPS 2021*; arXiv:1912.01683. ‡ (abstract)
- [T, S] Ho, A., Besiroglu, T., Erdil, E., Owen, D., Rahman, R., Guo, Z. C., Atkinson, D., Thompson, N. and Sevilla, J. 2024. Algorithmic progress in language models. *Advances in Neural Information Processing Systems* 37:58245–58283; arXiv:2403.05812. ‡ (abstract) — if cited in text rather than only through EV9.
- [T] Smith, H. 1995 — delete (M8). [S] keep only if cited at Lemma S4.2; complete as: Smith, H. L. 1995. *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems*. American Mathematical Society. † (not retrieved)
- [T, D] Schelling 1960 and 1966: split into two entries; keep 1966 only where cited (SUPPLEMENT). Schelling, T. C. 1966. *Arms and Influence*. Yale University Press. †
- [D] Acemoglu, Egorov and Sonin 2012 — delete from DISCUSSION (M8).
- [D] Marker style: replace the mixed forms "‡ (abstract)", "‡ (full text)", "† (not retrieved)", bare "‡" and bare "†" by the five forms of the register's header.

### Additions: lineage gaps (Adv-O I7 and Opus/Fable math reviews)

- [D] Grieco, J. M. 1988. Anarchy and the limits of cooperation: a realist critique of the newest liberal institutionalism. *International Organization* 42(3):485–507. † (record)
- [D, T] Snidal, D. 1991. Relative gains and the pattern of international cooperation. *American Political Science Review* 85(3):701–726. † (record)
- [D] Powell, R. 1999. *In the Shadow of Power: States and Strategies in International Politics*. Princeton University Press. † (record)
- [D] Gilbert, R. J. and Newbery, D. M. G. 1982. Preemptive patenting and the persistence of monopoly. *American Economic Review* 72(3):514–526. † (record)
- [D] Budd, C., Harris, C. and Vickers, J. 1993. A model of the evolution of duopoly: does the asymmetry between firms tend to increase or decrease? *Review of Economic Studies* 60(3):543–573. † (record)
- [D] Athey, S. and Schmutzler, A. 2001. Investment and market dominance. *RAND Journal of Economics* 32(1):1–26. † (record)
- [D] Aghion, P., Harris, C., Howitt, P. and Vickers, J. 2001. Competition, imitation and growth with step-by-step innovation. *Review of Economic Studies* 68(3):467–492. † (record)
- [D] Avenhaus, R., von Stengel, B. and Zamir, S. 2002. Inspection games. In Aumann, R. J. and Hart, S. (eds), *Handbook of Game Theory with Economic Applications*, vol. 3, ch. 51, 1947–1987. Elsevier. † (record)
- [D] Schelling, T. C. and Halperin, M. H. 1961. *Strategy and Arms Control*. Twentieth Century Fund. † (record)
- [D] Kydd, A. 2000. Trust, reassurance, and cooperation. *International Organization* 54(2):325–357. † (record)
- [D, T] Shavell, S. 1986. The judgment proof problem. *International Review of Law and Economics* 6(1):45–58. † (record) — [T] if §8.3(b)'s "liability cannot exceed the assets of the liable" cites it.
- [D, S] Grossman, G. M. and Helpman, E. 1994. Protection for sale. *American Economic Review* 84(4):833–850. ‡ (abstract)
- [D] Konrad, K. A. 2009. *Strategy and Dynamics in Contests*. Oxford University Press. † (record)
- [T, S] Hehenkamp, B., Leininger, W. and Possajennikov, A. 2004. Evolutionary equilibrium in Tullock contests: spite and overdissipation. *European Journal of Political Economy* 20(4):1045–1057. † (record)
- [T] Cardaliaguet, P. 1996. A differential game with two players and one target. *SIAM Journal on Control and Optimization* 34(4):1441–1460. † (record)
- [T] Maynard Smith, J. and Szathmáry, E. 1995. *The Major Transitions in Evolution*. W. H. Freeman. † (record) — already restored in `v6.2/src/core/z9_refs.md`.
- [D] Kuran, T. 1995. *Private Truths, Public Lies: The Social Consequences of Preference Falsification*. Harvard University Press. † (record)
- [D] MacKenzie, D. 2006. *An Engine, Not a Camera: How Financial Models Shape Markets*. MIT Press. † (record)
- [D] Butler, G., Baker, J., Amend, S. R., Pienta, K. J. and Venditti, C. 2025. No evidence for Peto's paradox in terrestrial vertebrates. *Proceedings of the National Academy of Sciences* 122(9):e2422861122. ‡ (abstract)
- [D] Dietz, T., Ostrom, E. and Stern, P. C. 2003. The struggle to govern the commons. *Science* 302(5652):1907–1912. † (record)
- [T, D] Podvig, P. 2002. History and the current status of the Russian early-warning system. *Science and Global Security* 10(1):21–60. † (record)
- [T, D] Hoffman, D. E. 2009. *The Dead Hand: The Untold Story of the Cold War Arms Race and Its Dangerous Legacy*. Doubleday. † (record)

### Additions: alignment literature (Ali; SYNTHESIS E)

- [D] Askell, A., Brundage, M. and Hadfield, G. 2019. The role of cooperation in responsible AI development. arXiv:1907.04534. ‡ (abstract)
- [T, D] Hubinger, E., Denison, C., Mu, J., Lambert, M., Tong, M., MacDiarmid, M. et al. 2024. Sleeper agents: training deceptive LLMs that persist through safety training. arXiv:2401.05566. ‡ (abstract)
- [T, D] Greenblatt, R., Denison, C., Wright, B., Roger, F., MacDiarmid, M., Marks, S. et al. 2024. Alignment faking in large language models. arXiv:2412.14093. ‡ (abstract) — distinct from the Greenblatt, Shlegeris, Sachan and Roger 2024 entry already listed; the key needs the second author (I6).
- [T] Greenblatt, R., Roger, F., Krasheninnikov, D. and Krueger, D. 2024. Stress-testing capability elicitation with password-locked models. arXiv:2405.19550. ‡ (abstract record) — a third Greenblatt 2024; disambiguate as 2024a/b/c or by second author.
- [T, D] Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R. and Hobbhahn, M. 2024. Frontier models are capable of in-context scheming. arXiv:2412.04984. ‡ (abstract)
- [T, D] MacDiarmid, M., Wright, B., Uesato, J., Benton, J., Kutasov, J., Price, S. et al. 2025. Natural emergent misalignment from reward hacking in production RL. arXiv:2511.18397. ‡ (abstract)
- [T] Schlatter, J., Weinstein-Raun, B. and Ladish, J. 2025. Incomplete tasks induce shutdown resistance in some frontier LLMs. arXiv:2509.14260; *Transactions on Machine Learning Research* (2026). ‡ (abstract)
- [T] van der Weij, T., Hofstätter, F., Jaffe, O., Brown, S. F. and Ward, F. R. 2024. AI sandbagging: language models can strategically underperform on evaluations. arXiv:2406.07358. ‡ (abstract)
- [R] Li, X., Ochwang'i, K., Bharadwaj, A. R., Souly, A. and Kirk, R. 2026. EvalDetectBench: a benchmark for measuring evaluation awareness in frontier language models. arXiv:2609.01611. ‡ (abstract)
- [T, D] Stix, C., Pistillo, M., Sastry, G., Hobbhahn, M., Ortega, A., Balesni, M. et al. 2025. AI behind closed doors: a primer on the governance of internal deployment. arXiv:2504.12170. ‡ (abstract)
- [T, D] Davidson, T., Finnveden, L. and Hadshar, R. 2025. *AI-Enabled Coups: How a Small Group Could Use AI to Seize Power*. Forethought, April. ‡ (page)
- [T] Turner, A. M., Hadfield-Menell, D. and Tadepalli, P. 2020. Conservative agency via attainable utility preservation. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 385–391; arXiv:1902.09725. † (record)
- [T] Turner, A. M. and Tadepalli, P. 2022. Parametrically retargetable decision-makers tend to seek power. *Advances in Neural Information Processing Systems* 35:31391–31401; arXiv:2206.13477. † (record)
- [T] Taylor, J. 2016. Quantilizers: a safer alternative to maximizers for limited optimization. *AAAI-16 Workshop on AI, Ethics, and Society*. ‡ (page)
- [T] Soares, N., Fallenstein, B., Yudkowsky, E. and Armstrong, S. 2015. Corrigibility. *AAAI-15 Workshop on AI and Ethics*. ‡ (page)
- [T] Thornley, E. 2024. The shutdown problem: an AI engineering puzzle for decision theorists. *Philosophical Studies* 182(7):1653–1680 (online 2024). † (record)
- [T, D, R] Baker, B., Huizinga, J., Gao, L., Dou, Z., Guan, M. Y., Madry, A. et al. 2025. Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. arXiv:2503.11926. ‡ (abstract)
- [T, D, R] Guan, M. Y., Wang, M., Carroll, M., Dou, Z., Wei, A. Y., Williams, M. et al. 2025. Monitoring monitorability. arXiv:2512.18311. ‡ (abstract)
- [R] Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N. et al. 2022. Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv:2204.05862. † (record)
- [R] Huang, T., Hu, S., Ilhan, F., Tekin, S. F., Yahn, Z., Xu, Y. et al. 2025. Safety tax: safety alignment makes your large reasoning models less reasonable. arXiv:2503.00555. † (record)
- [R] Terekhov, M., Liu, Z. N. D., Gulcehre, C. and Albanie, S. 2026. Control tax: the price of keeping AI in check. *ICLR 2026*; arXiv:2506.05296 (2025). † (record; venue confirmed on the ICLR 2026 site)
- [R] Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R. et al. 2023. Towards understanding sycophancy in language models. arXiv:2310.13548. † (record)
- [R] Williams, M., Carroll, M., Narang, A., Weisser, C., Murphy, B. and Dragan, A. 2025. On targeted manipulation and deception when optimizing LLMs for user feedback. *ICLR 2025*; arXiv:2411.02306. † (record)
- [R, D] Panickssery, A., Bowman, S. R. and Feng, S. 2024. LLM evaluators recognize and favor their own generations. arXiv:2404.13076. † (record)
- [R, D] Gardner-Challis, N., Bostock, J., Kozhevnikov, G., Sinclaire, M., Velja, J., Abate, A. et al. 2026. When can we trust untrusted monitoring? A safety case sketch across collusion strategies. arXiv:2602.20628. † (record)
- [T] Goldowsky-Dill, N., Chughtai, B., Heimersheim, S. and Hobbhahn, M. 2025. Detecting strategic deception using linear probes. arXiv:2502.03407. † (record)
- [D] Brown-Cohen, J., Irving, G., Piliouras, G., Chen, L., Li, J. and Xun, Z. 2025. Avoiding obfuscation with prover-estimator debate. arXiv:2506.13609. † (record)
- [D] Calvano, E., Calzolari, G., Denicolò, V. and Pastorello, S. 2020. Artificial intelligence, algorithmic pricing, and collusion. *American Economic Review* 110(10):3267–3297. † (record)
- [D] Fish, S., Gonczarowski, Y. A. and Shorrer, R. I. 2024. Algorithmic collusion by large language models. arXiv:2404.00806 (EC 2026). † (record)
- [R, D] Khan, A., Hughes, J., Valentine, D., Ruis, L., Sachan, K., Radhakrishnan, A. et al. 2024. Debating with more persuasive LLMs leads to more truthful answers. *ICML 2024*; arXiv:2402.06782. † (record)
- [R, D] Kenton, Z., Siegel, N. Y., Kramár, J., Brown-Cohen, J., Albanie, S., Bulian, J. et al. 2024. On scalable oversight with weak LLMs judging strong LLMs. *NeurIPS 2024*; arXiv:2407.04622. † (record)
- [R] Anwar, U., Bakker, T., Kianfar, D., Pinneri, C. and Louizos, C. 2026. Analyzing and improving chain-of-thought monitorability through information theory. arXiv:2602.18297. † (record) — only if the alignment rewrite cites it.

### Sources used only in the register (no bibliography entry needed unless the body cites them)

AI Index 2026; Epoch data insights (29 May 2026; 2 January 2026); METR time-horizon page; UN press release of 1 July 2026; UNRIC on the appointment vote; UN-project votes on A/RES/79/239 and 80/58; REAIM host-ministry list; Executive Order 14365 (90 FR 58499); the 2025 "AI+" Opinions (国发〔2025〕11号); the White House fact sheet of 25 September 2026; the Senate Commerce release of 1 July 2025; the UK government release of 14 February 2025; the Colorado litigation reports; the two developers' RFI submissions; the CAIIA safety commitments; the super-PAC reports and the developer's two donation posts; the RSP v3.4 and its version-history page; the report of the internal memo on Gulf capital; the side-by-side arrangement report. All are dated and marked in EVIDENCE.

---

## (c) Lineage gaps: what the paper absorbs, and what it adds

For DISCUSSION X1, "What is absorbed, and what is new". One sentence each; each sentence names what is taken and what is added, so the novelty claim stays honest.

**International relations.**
- **Grieco 1988.** Absorbed: concern for relative gains limits cooperation under anarchy. Added: the relative objective is not assumed from anarchy but selected (Proposition 3.6) and manufactured by compounding wherever reinvestment's relative return exceeds its common return (Proposition 3.9), so it can be changed by changing what is selected.
- **Snidal 1991.** Absorbed: the effect of relative gains weakens as the number of actors grows. Added: the same weakening appears in talk as the bias factor $n/(n-2)$ of Proposition 5.15(2); that pairs then align against third parties is stated as a conjecture, not a result.
- **Powell 1999.** Absorbed: bargaining in the shadow of shifting power, where expected shifts make war rational for the side about to lose. Added: compounding growth drives the shift, so the commitment problem is a consequence of the loop gain rather than an exogenous power transition (Proposition 5.4, §5.2).
- **Schelling and Halperin 1961.** Absorbed: arms control as cooperation among adversaries, aimed at stability rather than reduction, with verification and communication channels. Added: what selects the correctors of an agreement (Section 4) and why custody must precede decisiveness (§11.5).
- **Kydd 2000.** Absorbed: costly signals can reveal a security-seeking type and build trust among rivals. Added: verifiable narrow E1 as such a signal in AI (Proposition 11.2), and the selection pressures that make the signal cheap to imitate unless inspected.
- **Avenhaus, von Stengel and Zamir 2002.** Absorbed: the deterrence condition of the inspection game, which Proposition 8.10's threshold reproduces. Added: the split of enforcement into the breakout probability $p_d$ and its bound $\bar p_d$, and how growth moves each (Proposition 5.4; the scissors); X1 item 3 should claim only this.

**Industrial organization and contests.**
- **Gilbert and Newbery 1982.** Absorbed: an incumbent's incentive to pre-empt equals the value of staying ahead, which is a price on standing. Added: the price of standing as a loop gain summed over channels, including rule support and conversion into control of correction (Propositions 2.2, 3.9).
- **Budd, Harris and Vickers 1993.** Absorbed: whether asymmetry between rivals grows depends on how joint payoff varies with the gap, the symmetric state's stability criterion. Added: rule support as one of the compounding stocks, and provision $k_0$ and diffusion as inflows not won in the contest that restore equality (Proposition 2.3).
- **Athey and Schmutzler 2001.** Absorbed: conditions under which leaders invest more and dominance increases. Added: the same increasing dominance in the reflexive channel, where what leaders invest in is their own selection rule (Section 4).
- **Aghion, Harris, Howitt and Vickers 2001.** Absorbed: escape-competition effort is highest neck-and-neck, while laggards far behind are discouraged. Added: at the scale of one host, near-equal standing is where both intensity and the shared hazard peak, which is why spending a lead returns the contest toward its most dangerous point (§8.3(c); Proposition 3.9(3) strategic case).
- **Harris and Vickers 1987.** Absorbed: in a race with uncertainty the leader works harder and a sufficiently large lead discourages the follower. Added: a lead shrinks by diffusion even when the follower does not accelerate, and what the margin must buy is coverage (Remark 8.6).
- **Konrad 2009; Konrad and Kovenock 2009.** Absorbed: contest success functions, decisiveness $r$, dissipation, and the discouragement effect in multi-battle contests. Added: dissipation counted against a shared host, so that relative selection prices intensity while the loss it imposes on all drops out (Lemma 3.3, Proposition 3.6).
- **Hehenkamp, Leininger and Possajennikov 2004.** Absorbed: evolutionary (finite-population) equilibrium in Tullock contests is spiteful and dissipates the full prize at $r=1$. Added: the shared loss term, under which every actor ends below zero (Proposition 3.6(3)).

**Law, regulation and political economy.**
- **Shavell 1986.** Absorbed: liability cannot deter beyond the assets of the liable. Added: for catastrophic and common harms, the judgment-proof gap is the point at which a common cost cannot be turned into a private one, which is why liability alone does not settle the alignment tax (§8.3(b); Lemma 3.3(2)).
- **Grossman and Helpman 1994.** Absorbed: influence over policy bought with contributions, in equilibrium with the policymaker's other aims. Added: the return to influence over correctors scales with the square of share and with its appropriability $\chi$, so it is selected in the largest carriers (Proposition 4.3), and spending can be classified by what the rule would do, not by its stated aim (EV4).

**Biology and the history of selection.**
- **Maynard Smith and Szathmáry 1995.** Absorbed: the major transitions integrate units that could replicate alone, held by aligned interests and by policing; cancer is integration failing. Added: at the planetary scale there is no rival group of the same kind, so integration cannot be driven by selection among groups and must be anticipated (Lemma 3.10).
- **Caulin and Maley 2011; Butler et al. 2025.** Absorbed: suppression of cancer evolved with size, and prevalence still rises with size, far less than cell number would give. Added: only as a demonstration that growth is not the fault line (X2).
- **Cardaliaguet 1996.** Absorbed: the discriminating kernel, the set from which a controller can guarantee viability against every disturbance. Added: openness as such a kernel, with admissible correction as the controller and the justified range $\Theta$ as the disturbances (Definition 8.1).

**Alignment.**
- **Askell, Brundage and Hadfield 2019.** Absorbed: responsible AI development as a collective action problem, with the factors that make cooperation more likely. Added: the selection-theoretic form, Proposition 6.7: which divergences the outermost loop pays to remove depends on who bears their cost, and the alignment-tax premise $(A_\tau)$ says when a common constraint is needed.
- **Hubinger et al. 2024; Greenblatt et al. 2024; Meinke et al. 2024; MacDiarmid et al. 2025.** Absorbed: masked divergences exist in constructed settings, and safety training can produce aligned behaviour on the evaluations it is trained against while misalignment persists elsewhere. Added: the consequence for admission, which must be stated in capability rather than propensity for the masked class, with E2 or E3 beyond the threshold (EV6; Proposition 6.7's scope).
- **Stix et al. 2025.** Absorbed: internal deployment as a principal and ungoverned source of loss of control and concealed concentration. Added: why release-based admission cannot reach strong incarnation, and hence "before consequential deployment, internal deployment included".
- **Davidson, Finnveden and Hadshar 2025; Kulveit et al. 2025.** Absorbed: hidden loyalties written into the alignment target, and gradual disempowerment as institutions lose their dependence on people. Added: both as the "us" joint of "our aligned AI is us": aligning AI to an institution is not aligning it to the people the institution serves, and the winner is itself a field (§7.2).
- **Marks et al. 2025.** Absorbed: auditors with access to training data found a planted objective that black-box access did not. Added: mandated access as an admission condition and the verifiability crux C12.
- **Turner et al. 2021; Turner and Tadepalli 2022; Turner, Hadfield-Menell and Tadepalli 2020; Taylor 2016.** Absorbed: optimal and retargetable policies tend to seek power even for bounded goals; counting side effects and mild optimization bound it. Added: both bounds are selected against where the loop gain is high (Proposition 3.9), which makes "growth is not the danger; the mind is" precise for AI minds.
- **Baker et al. 2025; Guan et al. 2025; van der Weij et al. 2024.** Absorbed: monitorability has a price and is fragile under optimization; capability evaluations can be sandbagged. Added: the monitorability tax as an instance of $(A_\tau)$, positive but small at present, and sandbagging as part of the masking term $m_{\rm model}$ (§4.4).

**Performativity.**
- **MacKenzie 2006.** Absorbed: models can be performative and counterperformative. Added: the shared prediction of the race can avert its own fulfilment, which is the ground for prediction as an intervention (§11.2).
- **Kuran 1995.** Absorbed: preference falsification makes public consensus fragile and liable to tip. Added: a race doctrine professed by actors who are selected for professing it may be held less widely than it is stated, so visible cooperation can tip it (§5.4, §11).

---

## Not verified, or verified only through reports

- The OpenAI RFI submission (primary page refused retrieval; read through a report).
- The super-PAC amounts for the opposing network (reports only; 501(c)(4) donors need not be disclosed).
- REAIM 2023 endorsement by both leading states (reports and an encyclopaedia), and the 2026 count (35 at the summit per reports; 43 on the host page, whose list shows 45 names).
- The UN panel's preliminary report itself (only the UN announcement read).
- The OpenAI Frontier Governance Framework (reports only).
- The minimum-tax arrangement (a professional firm's report, not the OECD text).
- The 1983 incident sources (records only).
- The reported internal memo on Gulf capital (EV1): read through a report quoting it; the original report not retrieved.

**Model-family note.** The drafter belongs to the family of the developer that appears in EV1–EV6. The register records items in both directions concerning that developer (its spending for binding rules, its pause discretion and the v3.1–v3.4 revisions, its chief executive's reported memo on Gulf capital, a government partnership announced with the renaming of a public institute, its top leaderboard position, its researchers' studies of masked divergence, its revised scaling policy read as a commitment problem). An outside reviewer should check the register for omissions unfavourable to it.

---

## Verification

An adversarial pass on 4 October 2026 tried to refute each changed or added claim in `EVIDENCE.md` and each new bibliography entry above, against the source itself where it could be retrieved (arXiv API and abstract pages, Crossref, publisher and government pages, the RSP v3.4 PDF, the NBER PDF of w35276, the Jones PDF). Corrections are applied in both files. A test assembly in a scratch copy reports no problems.

### Corrected

1. **Bueno de Mesquita, Dziuda and Polborn, §6.3 (EV2, EV11).** The register called their reading one of "the first revision" of the scaling policy. The paper speaks of "the subsequent evolution" and its footnote 9 refers to the 2026 revision (v3.0), away from the original 2023 pause commitment. Now "the 2026 revision (v3.0)". The disclosed advisory work is for Meta, on governance; now stated.
2. **Zhu (2026), scope of the 77% (EV2 effect; notes E3, E4).** "77% of traced changes across twelve developers" overstated the scope. The corpus covers twelve developers, but the changes were traced across twelve pairs of consecutive versions. Now "77% of the changes it traced, in twelve pairs of consecutive versions".
3. **Executive Order 14365 (EV3).** The funding condition is §5 (remaining broadband-deployment funds), not §3. Now separated. The §2 quotation, the §3 task force (30 days) and the §8(b) carve-outs are confirmed against the Federal Register text.
4. **UK partnership (EV3, disclosure, model-family note).** The 14 February 2025 release announced a memorandum of understanding between the government, through its Sovereign AI unit, and the developer, on public services. The institute was not a party. "A public institute's partnership with it" is corrected.
5. **UN panel quotation (EV7).** "Current safeguards cannot keep pace with the growth of AI's capabilities" is the UN announcement's summary, not a quotation of the report. Now attributed that way, and the quoted sentence on deceptive behaviour and catastrophic harm is added verbatim.
6. **Global Dialogue (EV7, EV8).** Geneva, 6–7 July 2026, was its first full session. It was launched at the General Assembly in September 2025, so "the first Global Dialogue" is changed. The launch date is from prior knowledge and marked † (not retrieved).
7. **Panel appointment vote (EV8).** Confirmed at 117–2–2. The two against were the first leading state and Paraguay; Tunisia and Ukraine abstained. The "overreach" statement was about the panel *and* the Global Dialogue; now stated.
8. **Statement of 28 September 2026 (EV8).** The date is the report's, not necessarily the post's. Now "in a post reported on 28 September 2026". The speaker is confirmed as the director of the science and technology policy office.
9. **Leading the Future (EV4).** The $125M+ belongs to the network, including affiliated super PACs and nonprofits, and was raised in the second half of 2025. Donors included another AI company besides a frontier developer's co-founder. Now stated.
10. **Public First Action donations (EV4).** The February post does not state the candidate restriction; the July post does ("cannot be used to influence the election of any candidate"). Now attributed to the July post. Also added: the July post's position that governments should "ultimately have a way to slow or block the deployment" of models posing catastrophic risk.
11. **METR title (EV5).** The current arXiv title (v4) is "Measuring AI Ability to Complete Long *Software* Tasks". The register now gives it, notes the first version's title and the lead authors, and confirms NeurIPS 2025 from arXiv's journal reference.
12. **AI Index 2026 (EV5).** "Has effectively closed" and "traded the lead multiple times since early 2025" are confirmed verbatim. The page's own example is a model that "briefly matched" the top model, so a note now says that "traded the lead" rests on the report's summary. Symmetric standard: the claim that the lead changed hands is held to the same evidentiary bar as the claim that it did not.
13. **EV9 interval arithmetic.** 2^(12/2) = 64, not "about 60". Now "about 64×".
14. **Jones (2024) conditions (EV11; notes A1, A4).** The 40-year, one-in-three and 4.5-year, 4% figures hold only at δ = 1% and g = 10%, and the 25% figure is the one-time cutoff of the richer model. All are confirmed against the PDF (Table 1, Table 2, Key Points 1–5), and the conditions are now stated. In note A1, "only if utility is linear … is a course preferred" said more than the derivation shows. It is now "if utility is linear … (so that the value of life does not rise with it)".
15. **Butler et al. (2025) (EV18; note H1).** "Not contested by Butler et al." went beyond the abstract, which does not measure prevalence against the cell-number benchmark. Now "not re-measured". H1's "lineages whose size evolved fastest" is replaced by the abstract's "repeated bursts of accelerated size evolution".
16. **Terekhov et al. venue.** ICLR 2026 is confirmed on the ICLR 2026 site, and the entry is updated and removed from the unverified list.
17. **Omission found under the symmetric standard (EV1, disclosure).** The register did not record the drafting model's developer's July 2025 internal memo, reported by *Wired*. In it the chief executive wrote that Gulf-state capital gives "a very large benefit" for staying "on the frontier", and that "'No bad person should ever benefit from our success' is a pretty difficult principle to run a business on". It is the only item in EV1 about a decision rather than a declaration, and it cuts against the developer. It is now recorded (‡ page through a report) and named in the disclosure. EV2 now also records the v3.1–v3.4 revisions shown on the version-history page, which run both ways: v3.2 added external review that the trust can request, and v3.4 narrowed internal circulation of unredacted risk reports to at least 200 employees.

### Confirmed

- **EV1.**
  - EO 14365: title, date, 90 FR 58499–58501, and the §2 quotation (Federal Register).
  - 国发〔2025〕11号: dated 21 August 2025, posted 27 August. "率先实现…6大重点领域", the three 优势, "造福人类的国际公共产品", open-source access, the Global South and the UN as "主渠道" are all verbatim on the CAC page.
  - World AI Cooperation Organization: proposed by the second state's premier on 26 July 2025, with the stated purpose verbatim.
  - The developer's OSTP submission of 6 March 2025: the "decisive action" quotation, the export-control sentence and the six recommendation areas.
  - Safety commitments of 1 December 2024: 17 signatories and the six areas (ETO AGORA).
- **EV2, RSP v3.4 (full text).**
  - Verbatim: the collective-action passage, "cannot commit to following them unilaterally", "until and unless we no longer believe we have a significant lead", "meet or exceed", "General upleveling", "do not preclude us from taking cautionary action…" and "would strongly consider pausing… even in cases not covered below".
  - The v3.1 changelog sentence "may consider pausing… Appendix A are not triggered" is inside the v3.4 PDF.
  - "Free to take measures such as pausing" is on the version-history page, under the 2 April 2026 entry.
  - Effective dates confirmed: v3.0 24 Feb, v3.1 2 Apr and v3.4 8 Jul 2026.
  - The OpenAI Frontier Governance Framework of 28 May 2026 maps onto state and EU duties, with the Preparedness Framework as its foundation (reports and the developer's index page).
- **EV2/EV11, Bueno de Mesquita, Dziuda and Polborn.**
  - NBER w35276, issued May 2026, with the authors as listed.
  - Proposition 9, Corollary 1 (Pareto-improving) and the local character of the result.
  - Both §6.3 quotations are verbatim ("precisely the commitment problem…"; "A request for binding safety rules need not be read only as…").
- **EV3.**
  - Colorado: xAI sued on 9 April 2026 and the DOJ filed on 24 April. The 27 April order was stipulated by xAI and the attorney general: no enforcement or investigation until 14 days after a preliminary-injunction ruling, and the motion follows final rulemaking.
  - SB 26-189 was signed on 14 May 2026 and takes effect on 1 January 2027, with notice-based duties and a 60-day cure period.
  - The review's "court paused the law" is rightly corrected.
  - The 99–1 Senate vote of 1 July 2025.
  - The AISI renaming and its two quotations (14 February 2025).
- **EV4.** $20M on 12 February 2026 and $20M on 21 July 2026 ($40M in all) to Public First Action, a 501(c)(4); the four February positions are verbatim.
- **EV5.**
  - METR live page: "Measurements above 16 hrs are unreliable…", updated 8 May 2026.
  - Epoch, 29 May 2026: four months and 8 ECI points, verbatim.
  - Epoch, 2 January 2026: all frontier models from one state since 2023, with a lag of 7 months (range 4–14).
  - AI Index: March 2026, Anthropic's top model leads by 2.7%.
- **EV6, verified against arXiv metadata and abstracts.**
  - Hubinger et al.: 39 authors, with the "effectively hiding" quotation.
  - Greenblatt et al.: 20 authors; 14% and 78%.
  - Meinke et al.: six authors.
  - MacDiarmid et al.: 22 authors, 23 November 2025, and the three mitigations.
  - van der Weij et al.: five authors.
  - Schlatter, Weinstein-Raun and Ladish: the new title (v2, 26 January 2026), TMLR 2026, more than 100,000 trials, thirteen models, and up to 97% (95% CI 96–98).
  - EvalDetectBench: the five authors and both findings. arXiv's own record gives "Submitted on 8 Jun 2026" despite the 2609 identifier, so the date stands as recorded.
  - Baker et al. and Guan et al., "Monitoring Monitorability" (12 authors, 20 December 2025): both quoted findings are verbatim.
- **EV8.**
  - A/RES/79/239: 24 December 2024, 159–2–5, both leading states yes.
  - A/RES/80/58: 1 December 2025, 167–5–5, the first state no and the second yes.
  - REAIM 2026: neither leading state is on the host ministry's list, which names 43 or 45 states.
  - Political Declaration: 54 endorsers by March 2024.
  - Fact sheet of 25 September 2026: "U.S.-China Super Intelligence (SI) Dialogue", "a bilateral communication channel for SI incidents" and "by November 2026", all verbatim.
- **EV9.** Ho et al.: the NeurIPS abstract gives the 90% CI as "around 2 to 22 months" and the arXiv v1 abstract the 95% CI as "around 5 to 14 months". Pages 37:58245–58283 (Crossref).
- **EV11.**
  - Jones: *AER: Insights* 6(4):575–590 (Crossref), with equation (1) and v(c) as stated.
  - Fudenberg and Koh (2609.28291) and Fernández Domingos and Han (2607.26034): the records exist with the stated authors.
- **EV17.**
  - Petrie, Aarne, Ammann and Dalrymple, 2506.15093.
  - Shavit, 2303.11341.
- **EV18.**
  - Caulin and Maley, *TREE* 26(4):175–182.
  - Butler et al., *PNAS* 122(9), e2422861122, with five authors and the abstract findings as stated.
  - EY's report of the side-by-side package: 5 January 2026, IIR and UTPR, fiscal years from 1 January 2026.
  - Podvig, *Science and Global Security* 10(1):21–60.
  - Fuhrmann and Kreps, *JCR* 54(6):831–859.
- **Bibliography (b), records confirmed (Crossref or arXiv).**
  - Journal and book records:
    - Thornley, *Philosophical Studies* 182(7):1653–1680, online 2024.
    - Turner and Tadepalli, *NeurIPS* 35:31391–31401.
    - Turner, Hadfield-Menell and Tadepalli, AIES 385–391.
    - Avenhaus, von Stengel and Zamir, Handbook ch. 51, 1947–1987.
    - Hehenkamp, Leininger and Possajennikov, *EJPE* 20(4):1045–1057.
    - Cardaliaguet 1996, *SICON* 34(4):1441–1460.
    - Cardaliaguet, Quincampoix and Saint-Pierre 1999, pp. 177–247.
    - Leonard 2009, *JEBO* 71(1):37–51.
    - Copeland 2000, *International Security* 25.
    - Kenton et al., *NeurIPS* 2024.
  - arXiv records (authors as listed): Goldowsky-Dill et al.; Brown-Cohen et al.; Gardner-Challis et al. (7 authors); Anwar et al.; Fish, Gonczarowski and Shorrer (accepted to EC 2026); Stix et al. (9 authors); Greenblatt, Roger, Krasheninnikov and Krueger.
  - Abecassis, "Refining MAIM", MIRI Technical Governance Team, April 2025: it exists, and its claims about red lines and credibility match the summary.
- **Body text proposed in (a).** It names no state or firm. Names appear only in citation titles (for example "Russian early-warning system"), which belong in the bibliography.

### Unverifiable here, or confirmed only from standard knowledge

- The OpenAI RFI submission (13 March 2025). The primary page was not re-tried. The content as recorded matches the drafter's knowledge of the submission.
- REAIM 2023 and 2024 endorsement by each leading state. Reports and an encyclopaedia only; consistent with the drafter's knowledge.
- The UN panel's preliminary report itself (announcement only).
- The OECD text of the side-by-side package (professional report only).
- The 1983 incident narrative, beyond Podvig's record.
- Standard records not re-fetched in this pass: Grieco 1988; Snidal 1991; Powell 1991, 1999 and 2006; Gilbert and Newbery 1982; Budd, Harris and Vickers 1993; Athey and Schmutzler 2001; Aghion et al. 2001; Schelling and Halperin 1961; Kydd 1997 and 2000; Shavell 1986; Grossman and Helpman 1994; Konrad 2009; Konrad and Kovenock 2009; Harris and Vickers 1987; Kuran 1995; MacKenzie 2006; Hoffman 2009; Dietz, Ostrom and Stern 2003; Maynard Smith and Szathmáry 1995; Calvano et al. 2020; Crawford and Sobel 1982; Gabriel 2020; Schaffer 1988; Rosenberg 1983. The details match the drafter's knowledge, with no discrepancy found.
- Larsen et al. author list for *AI 2040: Plan A* (from the site, as the earlier pass recorded).

### Left for the outside reviewer (symmetric standard)

Other items that bear on the drafting model's developer were not added to the register, because they bear only weakly on a row. They are listed here, from the drafter's knowledge and not verified in this pass, so that an outside reviewer can judge whether they should be:

- its federal lobbying disclosures by year (Test B data);
- its 2024 "support if amended" letter on a state frontier-AI bill;
- its defence contracts and its 2026 dispute with the defence department over permitted uses.

The same kinds of document should be recorded for other developers if any is added.
