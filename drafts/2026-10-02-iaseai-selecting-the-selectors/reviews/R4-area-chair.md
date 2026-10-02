# Review R4: area chair meta-assessment

*AI review. Ren asked for peer reviewers on 2026-10-02. The reviewer was a Claude Opus 5.5 subagent, briefed as a senior IASEAI area chair. It read only the anonymous PDF and `submission/main.tex`. It listed the submission folder but did not open NOTES.md or build/. It re-implemented the numerics in the session scratchpad. Its report is reproduced verbatim below.*

*Notes added by the session (2026-10-02):*
- *The reviewer's logistics item 0 repeats the stale "2 October" snippet. The live IASEAI'27 page gives 5 October 2026 (AOE).*
- *IASEAI'27's own guide links the AAAI kit (AuthorKit27), so the template is correct.*
- *Sources the reviewer marked as press reports (AEF-1, the CNBC letter) have not been verified by the session.*

---

# Area chair meta-assessment: "Selecting the Selectors" (IASEAI'27 draft)

**What I read.** Only the PDF (`/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/Selecting_the_Selectors_IASEAI27_draft.pdf`) and `/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/submission/main.tex`. The main text runs from p. 1 to the top of p. 9, about 8.2 of the 10 allowed pages, so roughly 1.8 pages are free.

**What I checked.** I checked every proof. I also re-implemented the numerics from Appendix B independently; the scripts are in the session scratchpad under `ac_meta_7f3/`. Nothing under `/Users/ren/theories` was modified.

## 1. Summary

**Positioning.** This is a structural-risk paper with a governance payload, built on a minimal formal model. It is not an alignment paper in the technical sense. Its alignment content is two claims:
- Obedient, per-system alignment does not limit capture at the level of the whole field.
- AI-assisted evaluation is only as good as the evaluator's independence from what it evaluates.

**The model.** There are n domains. In each, a replicator equation governs the share x_i of a practice that is costly under neutral rules. That share is coupled to a stock of rule support r_i, fed through a nonnegative conversion matrix. Because the system is cooperative, whether a capture configuration is stable becomes a condition on sets of domains: the set must be internally sustaining and externally closed. On top of that sit a cascade closure, a dual pruning "core", keystones, re-absorption, and a masking term through which a captured evaluator silences an alarm.

**Bottom line.**
- The prose is well above the IASEAI median, the hedging is unusually honest, and the proofs are correct.
- The formal core is elementary and partly known. Propositions 1–3 are weighted, continuous-time analogues of Morris (2000) on cohesion and contagion and of the Easley–Kleinberg cluster theorem. The paper cites neither.
- The most AI-relevant result (closure) holds by construction of Eq. (5).
- Nothing is measured.
- Two headline claims are false or unsupported under natural readings.
- As it stands the paper is borderline. Most of the damage is in claims and framing, not mathematics, so it can be repaired in three days.

**Title and key terms.**
- *"Selecting the Selectors"* helps. It is memorable and names the right phenomenon. But the text uses it in two senses:
  - §3.2 uses it for shaping the rules that select you.
  - §3.3, §4.4 and the title use it for capturing the harm-detection and correction channel.
  - §3.2 and §4.4 even share the same heading.
- *"Meta-attractor"* hurts.
  - In the model it is just an ordinary stable equilibrium of the joint (x, r) system.
  - Theory reviewers will read "meta" as inflation, and it adds jargon for governance readers.
  - Remove it from the abstract; at most keep it as an informal label in §3.
- *"Answerability"* currently hurts a little. It is in the title, but appears only as prose principles in §7 and is never formalized. It could become the paper's unifying concept (plan item 3b).

**Oversell.** The abstract claims to:
- "characterize every stable capture configuration" — the characterization holds only in the generic case;
- show that "no domain-by-domain audit can certify a field" — false for audits that measure inbound conversion (objection 3);
- show that "only reforms at keystone domains unravel a configuration" — keystone reforms unravel only down to the residual core;
- "derive discriminating tests" — the tests are proposed and qualitative, not derived.

The paper's candor ("possibility results", "estimate nothing") appears only in §§8–9. The abstract needs one scope sentence.

**Undersell.** The paper underplays four things:
- **Timeliness.** Evaluator independence is a live September 2026 debate. There is a reported public letter calling for independent evaluators, and the AI Evaluator Forum's AEF-1 baseline covers access, conflicts of interest, funding, recusal and transparency. Judge-lineage bias has been measured (sources below).
- **Computable audit logic.** Given an estimated R, the stable sets, keystones and re-absorption risk can all be computed.
- **The closing-window result.** Reform the origin domain while it is still a keystone.
- **The constructive flip side.** The same mechanism is how durable safety regimes are built, so what separates healthy from pathological self-maintenance is answerability, not persistence.

## 2. Predicted scores and decision

| Criterion | Predicted score (range) | Main drivers |
|---|---|---|
| Relevance | 8 (7–9) | Evaluator independence and structural risk are core IASEAI themes |
| Quality | 5–6 (4–7) | Correct but elementary math; masking assumed; no empirics; overclaims |
| Clarity | 6–7 (5–7) | Excellent sentences; dense; overloaded terms; Table 1 uses notation before it is defined |
| Originality | 5–6 (4–7) | The synthesis is new for AI; the math is known; the concepts are familiar |
| Significance | 5–6 (4–7) | Useful vocabulary and principles, but unmeasured |

**Likely reviewer pool.**
- **Governance/policy reviewer**, about 7 overall. Likes the design principles; asks for evidence.
- **Multi-agent, game-theory or cooperative-AI reviewer**, about 5. "Standard threshold dynamics, closure by construction, overclaims."
- **Ethics/auditing reviewer**, about 6. "Practice and answerability are under-theorized; the cancer analogy and the anecdote read as unprofessional; engage the accountability literature."
- **Possibly an alignment reviewer**, about 5–6. "So what for alignment?"

**Predicted decision as it stands: borderline, mean about 6.** IASEAI'26 accepted about 19% of submissions as archival papers (57 of 300). At that rate, a borderline paper is more likely rejected than accepted unless an area chair champions it.
- My judgment: about 30–40% chance of archival acceptance as is.
- About 50–60% after the plan below.

One point in its favour: no IASEAI'26 archival title addressed structural capture or evaluator independence.

## 3. What a champion would argue

- **A precise, under-studied mechanism made tractable.** The mechanism is success converting into control over future selection. Stability becomes a combinatorial property of sets of domains, which is interpretable and computable.
- **Crisp, policy-relevant results:**
  - capture of a domain whose own incentives are subcritical;
  - re-absorption of reforms confined to one domain unless inbound conversion is cut;
  - keystones, and the window that closes once the captured domains sustain one another (Fig. 3b);
  - hysteresis, so reforms must overshoot;
  - correction as a race between the cascade into evaluation and the decline in harm;
  - speed matters only through mismatch between adoption and rule revision.
- **Careful conceptual work.**
  - It separates concentration, capture, damage, collapse and closure.
  - It lists falsifiers and the conditions under which the account loses force.
  - It refuses to accuse particular actors and applies the analysis to the governance regime itself.
- **Timely and well-suited to IASEAI.** It gives a principled basis for firewalls and mixed-lineage evaluator panels, and it bridges political economy, evolutionary theory, science of science and ML evaluation.
- **Technically clean.** The proofs are correct and short. My re-implementation reproduced the cascade times, closure timing and re-absorption, though see objection 7.

## 4. What a skeptic would raise

1. **Thin, partly known formal contribution. Major; fatal with theory reviewers only if left oversold.**
   - Propositions 1–3 are cohesion and contagion results in monotone-dynamics dress.
   - "Complete characterization" holds only in the generic case. Proposition 1(ii) rules out only *linear* asymptotic stability, and for n>1 there is no appeal to Hirsch's generic convergence result.
   - Proposition 4 holds by construction: the masking in Eq. (5) is assumed linear in x_E.
   - The Statement of Contributions concedes "standard tools", which is good, but the abstract contradicts that tone.
2. **No empirical grounding. Major; not fatal at IASEAI, but caps significance.**
   - "General-purpose AI plausibly raises the parameters" carries the whole AI argument.
   - Table 2 is explicitly illustrative.
   - The "Agents" paragraph is an unverifiable anecdote ("sessions that we observed").
3. **The no-local-certificate headline is false under row-level audits. Major, and the objection most likely to sink the paper because it can be checked in a minute.**
   - Lemma 1 gives limsup r_i ≤ Σ_j b_ij/d_i. So if a domain's row sum Σ_j R_ij < 1, then x_i → 0 from any state, whatever the other domains do.
   - The row is the domain's own inbound conversion, which §7 says each authority sees ("each see one row, so assessment must be joint"). One row therefore *does* certify a domain, conservatively, and all row sums below 1 certify the field. §7's inference is a non sequitur.
   - What actually fails is certification from domain-internal incentives (R_ii) alone, and sharp, non-conservative assessment when row sums exceed 1.
   - Restate Corollary 1, the contribution list, Table 1, §7 and §8 accordingly. This is better turned into a positive result: an inbound-conversion audit standard.
   - Similar but smaller issues:
     - "Only keystone reforms unravel": they unravel only down to the residual core.
     - "Partial reforms are re-absorbed" is stated in the abstract without its condition (inbound conversion > 1).
4. **Internal inconsistencies. Major in total; easy to fix.**
   - Fig. 1 marks evaluation (E) and formation (F) as "selector domains", and §7 calls them "keystones of epistemic closure (Proposition 4)". But Proposition 4 involves only E, F has no formal selector role, and in the numerics F is not a keystone (development is). "Keystone" is a defined term (Corollary 4) being used loosely.
   - §5 says "Formation is the slowest domain, and Corollary 2 explains why reforms elsewhere are re-absorbed". But speed does not enter Corollary 2, and F's outbound conversion is only φ = 0.1.
   - "Selecting the selectors" has two meanings (§3.2 versus §3.3).
   - "Closure" has four meanings: the set operator cl(S), "externally closed", epistemic closure, and "answerable closures".
   - Fig. 1 draws ring coupling among the outer domains, but the numerics use all-pairs φ (hence the "4φ" threshold).
   - Table 1's caption says "Five distinctions" for six rows.
5. **"Neutral rules" are undefined, and the model is normatively symmetric. Major for ethics and governance reviewers.**
   - A safety practice sustained by the standards and procurement support it generates also satisfies Definition 1.
   - Pathology comes from depletion of V plus closure, not from self-maintenance. The paper never says this, and never formalizes answerability despite the title.
6. **Missing literatures. Moderate.**
   - Morris (2000, RES); Easley & Kleinberg (2010, ch. 19);
   - performative prediction and performative power (Perdomo et al. 2020; Hardt, Jagadeesan & Mendler-Dünner 2022), the ML-native version of "success shapes the environment that evaluates you";
   - Campbell's nested hierarchy of vicarious selectors, a near-literal antecedent of "selecting the selectors";
   - co-evolution of behaviours and institutions (Bowles, Choi & Hopfensitz 2003);
   - dynamic regulatory capture (Martimort 1999); strategic complementarities (Milgrom & Roberts 1990);
   - judge-lineage bias: Goel et al. 2025, "Great Models Think Alike and this Undermines AI Oversight" (ICML 2025); "Preference Leakage" (Li et al., ICLR 2026); "Who Judges Matters" (arXiv 2609.17857, Sept 2026, same-family lift of 3.4–8.4 percentage points);
   - AI control and trusted monitoring;
   - AEF-1. Verify primary sources; my information comes from press reports.
7. **The numerics specification is incomplete. Minor to moderate, and substantive.** Pure replicator dynamics lets capture deepen without bound (logit x grows linearly while a domain stays captured), so the results depend on how shares near 1 are handled. Under my reading of Appendix B:
   - **Floor on both x and 1−x (1e-4):** Fig. 3 reproduces, but the post-reform minimum of V is 0.53, not 0.46.
   - **Floor on x only:** the 0.46 reproduces, but Fig. 3a's drop at θ = 0.3 does not; capture persists well below 0.3. In float64 x-coordinates, procurement also freezes at x≈1 after the reform, which contradicts "unwinds capture in every domain".
   - **Both reported results reproduce only with an effective floor of about 1e-12 on 1−x.**
   - Downstream domains release 40–125 time units after the keystone reform. The paper does not report this, and it bears directly on Remark 2's reversal time.
   - Fix: specify an entry floor or mutation rate for alternatives, rerun, update the numbers, and report unwinding times.
8. **Under-specified unit of analysis. Moderate.**
   - It is unclear what a "practice" is and how x_i and r_i would be measured.
   - The tests lack identification; conversion estimates face common shocks and reverse causality.
   - The model has one practice, linear conversion, and no strategic incumbents. Incumbents investing in conversion is the obvious extension.
9. **Scope sprawl and tone. Minor.**
   - The cancer analogy, "Power's two roles" with its cryptic contraction sentence, the states paragraph, the "answerable closures" questions and the anecdote dilute the paper and invite political readings.
   - The opening line casts alignment research as "component" research, which alignment reviewers may read as a strawman.
10. **Small technical items. Minor.**
    - Corollary 1's proof should state that the other off-diagonal entries are zero.
    - Proposition 4 ends with an informal "Hence…" inside the statement.
    - Contribution 3 has no section pointer.

## 5. Could it be an important paper that advances alignment?

**Not yet.** In its current version it is a competent structural-risk and governance paper. Alignment researchers would not cite it as advancing alignment. Its alignment claim ("obedience is not field alignment") is already established by Critch & Krueger, gradual-disempowerment work and multi-principal analyses.

What separates it from importance, in order of how binding each gap is:
1. **Missing empirical work.** It needs at least one measurement:
   - the convertibility signature, i.e. persistence and hysteresis only when winners shape the next round's evaluation; or
   - an estimate of β, meaning lineage-driven under-reporting of harm by AI judges.
2. **Formal depth in the right place.** Derive masking rather than assume it. Add a recursive-oversight version, in which each generation's judge or reward model descends from earlier winners (RLAIF, self-rewarding models, model-written evals), giving thresholds on how much lineage diversity oversight needs. Add endogenous conversion growth, which turns "reform keystones while they are keystones" into a timing result.
3. **Framing.** Tie the model to scalable oversight, AI control, automated alignment research and evaluation awareness, rather than positioning it against component research.
4. **Scope.** Cut the general theory of power and centre on evaluator capture.

Framing alone can get it accepted. It cannot make it important.

## 6. Three-day plan (deadline 5 Oct AOE), in priority order

**0. Today (30 minutes): logistics.**
- IASEAI'27 appears to use OpenReview. Reports say the portal closes for "paper proposals" on 2 October, with later submissions considered on a rolling basis.
- IASEAI'26 froze the registered title, abstract and authors after registration, and required an IASEAI template "or risk rejection without review". This PDF uses `aaai2027.sty`.
- Confirm both points. If title and abstract must be registered today, register the revised versions now.

**1. Claim hygiene (about 4 hours; the biggest acceptance gain per hour).**
- Restate Corollary 1 and every use of it as described in objection 3, adding a row-sum certificate as a positive corollary.
- Fix the keystone and core wording and the abstract conditions.
- Either give formation a formal role, for example β = β̄·x_F or a large b_EF (formation produces future evaluators), or drop the selector and keystone claims about it.
- Use one definition of "selecting the selectors". Rename cl(S) (for example to "cascade hull") and "externally closed" (to "uninvadable").
- Rewrite the abstract to 170–190 words with a scope sentence and without "meta-attractor".
- Fix Table 1 (move it after §4.2, six rows, accurate caption), Fig. 1's edges, contribution 3's pointer, and Proposition 1's "generically".

**2. Position the math honestly (2–3 hours).**
- Add one paragraph after Proposition 2: these are field-level analogues of Morris/Easley–Kleinberg, and what is new is rows as rule-support channels, the coupling to correction, and the keystone/re-absorption policy content.
- Add the literatures in objection 6.
- Cut the Statement of Contributions to about 90 words. Keep the disclosure of the informal essays (compliant: no names or venues) and say plainly that all formal content is new.

**3. Turn the two assumptions into results (5–6 hours).**
- **(a) Derive Eq. (5) as a panel average.** Let a share x_E of evaluators come from the evaluated lineage, each inflating the reported condition by β(K−V). This gives a design quantity: the maximum tolerable captured share of a panel, x_E* = V_alarm/(βK). Tie β to the measured lineage effects.
- **(b) Define answerability.** A configuration is answerable if the alarm can fire (βx_E < V_alarm/K) and some keystone reform completes before the floor (Remark 2's race). This justifies the title and answers objection 5.
- **(c) Optional.** With conversion growing among co-captured domains at rate γ, development stops being a keystone at t* = (1 − R_ii − (n−2)φ₀)/((n−2)γ). This is a one-line, quotable closing-window result.

**4. Anchor the AI section without new experiments (3–4 hours).**
- Add an "existing evidence" column to Table 2: judge-lineage bias for β; evaluator access and funding dependence (Longpre 2024; AEF-1 provisions); industry share of compute, models and benchmarks; model-generated data in corpora.
- Add a short paragraph on implications for alignment practice: RLAIF and automated evals as capture of the selector by lineage; trusted monitoring as a firewall (β≈0); lineage-similarity metrics such as CAPA as an oversight requirement.

**5. Make the numerics consistent (2–3 hours).**
- Specify the floor or entry rate on both shares, rerun, and update 0.46 and the other numbers.
- Report post-reform unwinding times.
- Optionally replace or add a small phase diagram of the race (κ_E against h) to make Remark 2 concrete.
- Make sure the supplementary script is anonymized (no usernames, paths or git metadata) and reproduces every number in the text.

**6. Cut to make room and set the tone (1–2 hours).**
- Remove or reduce to one line the cancer analogy and the states paragraph. Keep the sentence on speed.
- Compress "Power's two roles" to two sentences plus Remark 3.
- Move "answerable closures" and the agent anecdote to an appendix (documented) or cut them.
- Open the introduction with the concrete AI evaluation problem.
- Stay within about 1.5 of the 1.8 free pages.

**Optional, with a go/no-go decision at the end of Day 1.** If evaluation infrastructure already exists, run a small measurement of harm-detection masking: same-family versus cross-family judges on a labelled safety set, at least three model families, with pre-specified metrics and confidence intervals. If it cannot be done cleanly, skip it; a weak experiment hurts more than none.

**Do not spend time on:**
- more threshold-type corollaries, parameter sweeps or figure polish;
- expanding the power, state or contraction theory;
- estimating a real conversion matrix (not feasible in three days, and it risks naming actors);
- re-proving the appendix;
- arguing against "standard tools" — concede it.

**Longer term (for impact):**
- **Measurement:** estimate R_ij and β from funding, personnel, access and lineage data, using natural experiments such as access revocations, cooling-off rules and AEF-1 adoption.
- **Experiments:** pre-registered LLM-agent tests of convertibility and of recursive oversight under lineage overlap.
- **Theory:** multiple competing practices, strategic investment in conversion, stochastic dynamics and early warning, optimal firewall design, entry or mutation terms, networks of jurisdictions, and answerability as reachability of the no-capture state.
- **Venues:** consider splitting into (a) an evaluator-capture and AI-judge-lineage paper for ML or safety venues and (b) a field-audit and keystone-reform paper for governance venues.

## 7. Presentation and clarity

- **Abstract:** about 230 words, dense, and overclaims (section 1). The introduction's first sentence risks reading as a strawman.
- **Overloaded terms:** "closure" and "selecting the selectors", as above.
- **Table 1:**
  - It appears before its notation is defined.
  - The caption says five distinctions for six rows.
  - "None implies the next" is wrong, because the rows are not a chain.
  - The "does not follow from" column mixes notions with procedures ("any domain-level audit").
- **Fig. 1:**
  - The ring coupling contradicts the all-pairs φ in the numerics.
  - The φ label floats unattached.
  - F is coloured as a selector without a formal role.
  - The E→D arrow should be labelled as correction or reform.
- **Fig. 2:**
  - Six lines are crammed into small panels.
  - Evaluation and information overlap (both cross 0.5 at t≈61) and cannot be told apart.
  - The floor line is faint.
  - Time units should be stated as arbitrary.
- **Fig. 3:** the axis label "hub coupling θ" does not match the text's "conversion from development"; the markers are tiny.
- **Table 2:** strong; add the evidence column.
- **Structure:** "core" deserves a Definition environment.
- **Statement of Contributions:** present and clearly labelled, but about 190 words against a requirement of "brief", and it repeats the contribution list.
- **Anonymity:** good.
  - The PDF metadata contains no author (Creator: tectonic).
  - There are no self-citations, and the disclosure of the essays complies with policy.
  - A quick search on the coined terms found no public trace.
  - Check that the supplementary code is scrubbed.

## Sources

- [IASEAI'26 Paper Submission Guide](https://www.iaseai.org/IASEAI%20'26%20Paper%20Submission%20Guide.pdf)
- [IASEAI'26 proceedings](https://ojs.aaai.org/index.php/IASEAI/issue/view/741)
- [IASEAI'27 programme page](https://www.iaseai.org/our-programs/iaseai27)
- [Morris 2000, Contagion](https://academic.oup.com/restud/article/67/1/57/1576255)
- [Easley & Kleinberg, ch. 19](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch19.pdf)
- [Hardt, Jagadeesan & Mendler-Dünner 2022, Performative Power](https://arxiv.org/abs/2203.17232)
- [Goel et al. 2025, Great Models Think Alike](https://model-similarity.github.io/)
- [Li et al., Preference Leakage](https://arxiv.org/abs/2502.01534)
- [Who Judges Matters (arXiv 2609.17857)](https://arxiv.org/abs/2609.17857)
- [AEF-1 coverage (Latent Space)](https://www.latent.space/p/ainews-aef-1-standard-emerges-for)
- [CNBC, Sept 2026: public letter on independent evaluators](https://www.cnbc.com/2026/09/18/ai-safety-evaluators-anthropic-openai-models-security.html)
- [Campbell, Nested hierarchies of vicarious selectors](https://www.researchgate.net/publication/284510853_Nested_hierarchies_of_vicarious_selectors)
- [Martimort 1999, dynamic capture](https://ideas.repec.org/r/oup/restud/v66y1999i4p929-947..html)
- [Bowles, Choi & Hopfensitz 2003](https://www.sciencedirect.com/science/article/abs/pii/S0022519303000602)

## Process notes

- I listed the submission folder, which revealed `NOTES.md` and `build/`, but I opened neither.
- The scratchpad is shared with other agents. During my run another process overwrote a `sim.py` in the scratchpad root. I moved my work to `ac_meta_7f3/` and did not touch their file. My early files in the root (`paper.txt`, `pages/`, `hi/`, `render*.swift`) may collide with other agents' files of the same names.
