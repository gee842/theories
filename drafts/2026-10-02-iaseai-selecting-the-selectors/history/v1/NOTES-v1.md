# Selecting the Selectors — IASEAI'27 draft (2026-10-02)

*These notes were written by Claude Opus 5.5, which drafted the paper. Ren has not yet reviewed it.*

**Title.** *Selecting the Selectors: Recursive Selection, Cross-Domain Capture, and the Answerability of AI Development.*

**Venue.** IASEAI'27, at Ren's direction (`sources/16-claude-code-directions/2026-10-02-meta-attractor-of-power-request.md`). Full submissions close **5 October 2026, AOE**.

**Format.** AAAI Press format (AuthorKit27), anonymous. The main text is about 8 pages of the 10 allowed and ends at the top of page 9. References and two appendices follow, 11 pages in all.

## Files

- `Selecting_the_Selectors_IASEAI27_draft.pdf` — the compiled draft. It was built with Tectonic (XeTeX) for checking, not for submission. See "Before submitting".
- `submission/` — everything needed to build the PDF you submit, ready to upload to Overleaf:
  - `main.tex`, `references.bib` and three figure files (`fig-schematic.tex`, `fig-field.tex`, `fig-hysteresis.tex`, all pgfplots/TikZ);
  - the unmodified `aaai2027.sty` and `aaai2027.bst`, from `AuthorKit27.zip`. The zip was downloaded from the link in the IASEAI guide, `https://iaseai.org/downloads/AuthorKit27.zip`, with Ren's permission (5,214,512 bytes, SHA-256 `64bd4452…736a1`).
- `build/`:
  - `figures.py` (pure Python) regenerates the two data figures and prints every number quoted in the paper.
  - `checks.log` is that printout. `hyst-cache.json` caches the hysteresis sweep, which takes about seven minutes to recompute; delete it to rerun.
  - `build.sh` builds a draft. `aaai2027x.sty` is the AAAI style with only its pdfTeX engine check commented out, so that Tectonic can compile it.

## How the paper was built from the corpus

The paper merges the 2026-10-02 essay with four bodies of existing work.

**From *The Meta-Attractor of Power* (2026-10-02)** (`sources/03-meta-attractor/2026-10-02-the-meta-attractor-of-power.md`):
- the central proposition, "selecting the selectors" and the research-community thought experiment;
- success without contribution, and the way of succeeding as what persists;
- cancer as a level conflict, kept with its boundary sentence;
- practical and epistemic closure;
- power's two roles and contraction;
- the convertibility test, the loss-of-force conditions and the reflexive clause;
- obedience versus system-level alignment, rate mismatch, and answerability.

**From *When Capability Outruns Correction* v2 (2026-09-29)** (`drafts/2026-09-28-capability-outruns-correction/`):
- the single-domain capture model (ẋ = κx(1−x)(ar−c), ṙ = ε(bx−dr)) with its threshold R = ab/(cd);
- the substrate V, with selection blind to it;
- masking of observation by captured measurement;
- lever latency (margin levers fast; memory and flow levers slow);
- the "which clock decides" remark.

The paper does not take over its epistemic-lag speed limit, the pause and restraint results, or the regime design. Those stay with that paper.

**From the meta-attractor canon** (`theories/meta-attractor/README.md`):
- the four coupled layers treated as one loop. Here they are domains coupled by a conversion matrix, with formation standing for the cognitive layer.
- partial reform is re-absorbed (the 2025-08 formal layer). Here it is Corollary 2.
- the direction-neutral definition, with destructiveness as an added condition (the 2026-07 causal chain, the whitepaper, the 10-02 essay). Here it is Definition 1.
- the pattern carried by humans, machines or composites. Here the state variables are practices, not identities (Remark 1).
- "the metric survives its own refutation". Here it is Proposition 4.

**From alignment as selection on cognition** (`theories/alignment-selection-on-cognition/README.md`):
- the principal is formed by the game, so the ends an aligned system serves are an output of the dynamics;
- the two capture channels into the machine: the corpus, and the loss function through revenue. Here they appear as the formation paragraph (model-generated data, preference optimization, the 2025 sycophancy rollback).

**From the Chinese line** (whitepaper §11.4):
- the three custody rules, restated as "answerable closures" (§7). This is the first time they appear in English and in a paper.

The structure:
- §§1–3 state the mechanism.
- §4 is a new model: n domains, each with a practice share and rule support, coupled by conversion.
- §5 reads it for general-purpose AI.
- §§6–7 give tests and design principles.
- §8 answers objections.

## What the merge produced

Each of these is new relative to both the essay and the corpus. All are AI-drafted results, proved in the paper's Appendix A and checked numerically in `build/checks.log`.

1. **A formal object for the corpus's residue claim.** `OPEN-QUESTIONS.md` §4.7 argues that what survives the prior art is the four layers treated as one loop. Definition 1 makes it testable: a *field-level* meta-attractor is a stable configuration in which some captured domain could not sustain capture alone (R_ii < 1). It exists only through cross-domain conversion.
2. **Which configurations can be stable (Proposition 1).** A captured set S is stable exactly when it is internally sustaining (every member receives inbound conversion above one from S) and externally closed (no outsider does). No mixed equilibrium is stable. Stability belongs to the set, not to any one domain.
3. **No local certificate (Corollary 1).** Every domain can be safe in isolation while the field is capturable, so audits domain by domain cannot certify a field. This is the essay's cross-domain reinforcement, and the corpus's point that capture need not be total to be decisive, in theorem form.
4. **Re-absorption and keystones (Corollary 2, Proposition 3, Corollary 4).** A reform confined to one domain is re-absorbed while its inbound conversion from the captured set exceeds one. A sustained reform at a *keystone* unravels every member outside the core of what remains. The window for unwinding a field by acting at its origin closes once the captured domains sustain one another (Figure 3b). This is the field-level counterpart of the 09-28 restraint window, which narrows as rule support accumulates. Here the window narrows as conversion among the captured domains grows.
5. **Persistence beyond the origin (Corollary 3).** "An organization can fail while its operating logic spreads to its successors" holds as a theorem when the captured domains are mutually sustaining.
6. **Closure as a race (Proposition 4, Remark 2).** Once the cascade reaches evaluation, the alarm can be silenced for good. Whether correction happens is a race between the cascade into evaluation and the decline of the shared condition, with decision and reversal delays added. This turns the essay's last line, and the corpus's "the metric survives its own refutation", into a condition that can be checked.
7. **Dependence and contraction (Remark 3).** If degraded shared conditions raise dependence and so conversion, a degradation shock can make capture possible with no change in the practice, and harm and capture reinforce each other. This is the essay's §6 and the corpus's "crisis as a new field for accumulation".
8. **The five distinctions as separate conditions (Table 1).** The essay's four, plus closure: concentration, capture, field-level capture, damage, collapse, closure.
9. **A partial answer to the corpus's largest internal debt.** The alignment README sets two claims against each other. One is "we cannot safely train an AI not captured by this attractor". The other is the reallocation principle: move AI onto the referee's bench. The paper's condition is weaker than "uncaptured" and can be checked: AI on the oversight side helps only if its provenance (lineage, data, funding, access) is independent of the success of what it oversees. In the model, that is small inbound conversion into evaluation and masking β ≈ 0. Lineage overlap and correlated errors are measurable (Panickssery et al. 2024; Kim et al. 2025).
10. **Game-level by construction.** The model's unit is the field, not the act, so it agrees with Ren's 2026-09-26 ruling that the unit is the game. It does not argue that ruling's scope, that AI should stay out of every competitive, concentrating game. That remains outside this paper, as it was outside the 09-28 one.

## What the paper leaves out, and why

- **The rest of *When Capability Outruns Correction*.** That includes the speed limit, the correction window in its general form, restraint, pauses, accumulation, the regime and the three domains. They belong to that paper. The two papers now share only the single-domain model and the masking result. Neither is published, so there is no novelty conflict. If both go to archival venues, keep IASEAI's rule on parallel archival review in mind (see below).
- **The covariance argument (ẇ = λCw, CAOC, PDI).** It answers a different question, which ends get promoted, and has the open defects recorded in the meta-attractor README (open items 31–32).
- **The historical layer, the 开/闭 vocabulary, 行星技术 and "do not fight for us".** Out of register for this venue. Answerability and the answerable-closures test carry their content in field terms.
- **Forsgren's "Hegemonic logic".** The essay opens from it, and the paper does not cite it. Read on 2026-10-02, it advances a specific contested allegation: that US strategy is to "Ukrainify Europe". Citing it in an anonymous AI-safety paper invites the reading that the paper endorses that claim. Power's two roles is grounded instead in Strange (structural power), Lukes and Bachrach–Baratz (faces of power), and Farrell and Newman (weaponized interdependence). The paper keeps the essay's refusal to validate claims about any particular actor and its symmetric application. Ren may overrule this.

## Decisions taken that Ren may overrule

- **Title.** "Selecting the Selectors" was chosen over "The Meta-Attractor of Power" because it names the AI-relevant step in field language. "Meta-attractor" appears once, in the introduction, as the name of the pattern.
- **The agent-fleet observation (§5, "Agents").** Three sentences, anonymized: "one software project … that we observed". It is the same Bonfire case that `When Capability Outruns Correction` v2 §3.2 uses, and the v2 notes ask whether to keep it. Cut it if Ren prefers.
- **Statement of Contributions.** It says "conceptual antecedents of Section 3 appeared in informal, non-peer-reviewed essays". Keep this if any meta-attractor essay is publicly posted, and delete it otherwise. Either way the paper cites none of them, as anonymity requires.
- **Cancer.** Kept as three sentences, with the boundary ("does not license treating people or institutions as cells").
- **The six domains and every number** are illustrative. No parameter is calibrated, and the paper says so.

## Verification done

- **Numbers.** Every number in the text comes from `build/figures.py`; see `checks.log`. The hysteresis sweep was recomputed from scratch on 2026-10-02 with a settle time of 1,500 units. An earlier run with a 600-unit settle had shown a transient (4 domains still captured at θ = 0.25); the recomputed sweep shows full unravelling there, as the theory predicts below θ = 0.3.
- **Proofs.** Appendix A was written and checked in this session: configurations, the Metzler-block argument for mixed equilibria, cascade, unravelling, keystones, selectors and the n = 1 case. Ren or a mathematician should reread them before submission.
- **References verified on the web on 2026-10-02:**
  - Kim, Garg, Peng and Garg (ICML 2025);
  - Singh et al., *The Leaderboard Illusion* (arXiv 2504.20879);
  - Panickssery, Bowman and Feng (NeurIPS 2024);
  - Wei, Ezell, Gabrieli and Deshpande (AIES 2024, 7(1):1539–1555);
  - Longpre et al. (ICML 2024, PMLR 235:32691–32710);
  - Ahmed, Wahed and Thompson (*Science* 379:884–886);
  - Farrell and Newman (*International Security* 44(1):42–79);
  - Narechania and Sitaraman (43 Yale L. & Pol'y Rev.);
  - Hammond et al. (arXiv 2502.14143);
  - the OpenAI sycophancy posts (April–May 2025);
  - Kleinberg and Raghavan (PNAS 2021); Bommasani et al. (NeurIPS 2022);
  - Smaldino and McElreath (*R. Soc. Open Sci.* 3:160384); Aktipis et al. (*Phil. Trans. B* 370:20140219);
  - Acemoglu and Robinson (AER 98(1):267–293); Abdalla and Abdalla (AIES 2021:287–297).

  References shared with the 09-28 paper carry that session's checks only in part. Its ten v1 references (among them Armstrong et al., Han et al. and Zwetsloot–Dafoe) and its arXiv IDs (among them Critch–Russell, Kasirzadeh and Kulveit et al.) were checked on the web. Stigler, Pierson, Weitz et al. and the other classics were cited from knowledge there too. The following are also cited from knowledge: Strange, Lukes, Bachrach–Baratz, Granovetter, Watts, Hanahan–Weinberg, Raji et al., Costanza-Chock et al., Birhane et al., Sharma et al., Shumailov et al., Taori–Hashimoto, Zheng et al., Whittaker and Khan. Spot-check them. Page numbers that could not be confirmed were removed (Kasirzadeh, Birhane, Taori, Narechania).
- **Anonymity.** The source, PDF text and bibliography were searched for names, project names, URLs and first-person self-citation; none were found.
- **Build.** No undefined references, no overfull lines. Page layout under the draft style is identical to the template: the template sample compiles to the same 10 pages under both engines.

## Before submitting (deadline 5 October 2026, AOE)

1. **OpenReview account.** IASEAI warns that approval "can take up to two weeks". If Ren has no account yet, this is the binding constraint. Then connect it through the IASEAI members portal.
2. **Build the submitted PDF with pdfLaTeX** from `submission/`, unchanged, for example on Overleaf. Confirm that the main text still ends within 10 pages; it should, since the layout is the same. Overleaf's TeX Live must include pgfplots 1.18.
3. **Supplementary material.** Appendix B says the script "is available as supplementary material". Upload `build/figures.py` (with `checks.log`) as supplementary material if the OpenReview form allows it. If not, delete that sentence.
4. **Track.** Archival means AAAI Press proceedings, at least 50% new technical content relative to the authors' prior publications (met, since nothing is published), and no parallel review at another archival venue. Non-archival means presentation only. Both require the submitting author to attend in person.
5. **Title, abstract and author list** are fixed at the deadline.
6. **Competing-interests disclosure** per the IASEAI policy. It is not shown to reviewers.
7. **AI-assistance disclosure.** The IASEAI guide is silent on it, and acknowledgments must be removed for review. AAAI policy makes authors responsible for all content. Decide what the camera-ready says. This paper is AI-drafted from Ren's ideas, the 10-02 essay and the corpus, and none of its sentences are Ren's verbatim.

## Open for Ren

- Read the proofs and the model section first. They carry the paper's novelty claim.
- Decide the title, the agent-fleet paragraph, the essays sentence, and the Forsgren omission.
- Decide whether *When Capability Outruns Correction* v2 still goes elsewhere (arXiv or a journal), now that its capture model is shared with this paper.
