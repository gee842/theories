# Feedback on "What Makes US–China AI Cooperation Credible?" (second draft)

Ren · 3 October 2026

This feedback is compiled from three independent review passes: argument and strategy, fact and citation check, and editorial and figures. Page numbers refer to the 32-page PDF of the second draft. Section 3 sets out the theoretical position I think the paper should argue from.

---

## Summary

**What is strong.** The draft's best material is new and genuinely useful. It shows what Plan-A-style verification would need in order to operate lawfully inside China:

- approvals under the DSL and PIPL;
- the CAC's October 2025 interpretation on viewing data on site;
- CII review;
- the symmetric US deemed-export rules;
- local custody;
- the separation of evidence, assessment and decision.

The facts are unusually clean. About 60 claims were checked, and one needs a hard correction.

**The argument has three problems.**

1. **It does not answer its title question.** The paper never says what makes cooperation credible. Track 2 concedes that the partner "cannot force a refusing host to comply" (p. 18) and that its benefit "may be far too weak" (p. 19).
2. **Part I criticises a version of Plan A that Plan A does not hold.** It also misses the weaknesses that Plan A's own authors document.
3. **It criticises Plan A from inside the frame that creates the problem.** It argues that Plan A is too coercive to be credible and proposes doing less. It never asks why credibility among rivals is so hard in the first place.

On top of this, caveats bury the claims. About one sentence in four or five carries a "not X" disclaimer, and the Conclusions end on one.

**Recommendation.** Rebuild the paper around the question of why credibility is hard (Section 3). Keep the China implementation analysis as its second half. The alternatives are set out in Section 6.

---

## 1. What to keep

- **The China implementation analysis (pp. 17–19),** including its honest statement of what local custody costs.
- **The evidence taxonomy (Figs. 7 and 9).** Capacity baselines, covered activity and undeclared compute need different checks; match the evidence to the claim.
- **The seeded-failure pilot (p. 17).** Inject omitted runs, misclassified workloads and sham retirements, then publish detection rates and false alarms.
- **Convertible capacity (p. 15).** A freeze on training lets capacity accumulate and makes exit more attractive.
- **Erosion (p. 10).** Dependence on AI raises the cost of carrying out the threat, so parties may weaken their commitments in advance. This is the best point in Part I.
- **Symmetric criteria (p. 21).** Judge both sides by the same standards of authority, access and decision rights.
- **The principle on p. 17,** "criticism should address those actual designs." Part I should follow it.

---

## 2. Problems in the argument

The problems are ranked by how much each one weakens the paper.

### 2.1 No theory of credibility (pp. 2, 18–19, 28)

A commitment is credible when complying with it, and punishing a breach of it, are in each actor's interest after the fact. The Summary's list covers verifiability and legitimacy, not that. Track 2 then gives up enforcement altogether, replacing it with reciprocity and a small recurring benefit.

**Fix:** state a thesis about what makes cooperation credible, and judge both Plan A and the two tracks against it. Section 3 offers one.

### 2.2 MACD is analysed as the wrong kind of threat (pp. 5–10)

Plan A's MACD is not a strike that leaders may decline to order. It works in three ways:

- **It is automatic.** The chips stop working unless the regular "continue" messages keep arriving.
- **It is a hostage exchange.** Chinese R&D sits in Canada and US R&D in Mongolia.
- **It denies a defector the compute.** Plan A's dissolution branch argues that if the new compute survived, AI takeoff "would be several times faster."

The draft notes the automatic design (p. 7) and then analyses a discretionary strike anyway. Two passages also restate Plan A as if objecting to it:

- The "released overhang" in Fig. 4 is Plan A's own rationale for MACD, not an objection to it.
- The graduated responses on p. 9 largely repeat Plan A's own escalation ladder.

**Fix:** analyse the problems the real design has.

- Withholding "continue" gives each side a veto it can use for blackmail.
- Accidents or hacks could trigger destruction.
- A catastrophic threshold makes cheating below it safer. This is the stability–instability problem.
- As dependence grows, the hostage grows, and so does the pressure to weaken the mechanism in advance. The draft states this in one sentence on p. 10; make it the centre of Part I.

### 2.3 §1.1 rebuts a claim Plan A does not make (pp. 3–4)

Plan A calls the US lead "one extra reason" for China to come to the table, not the thing that secures agreement. The DSA chain in Fig. 2 also cuts both ways:

- If a lead may not turn into usable coercion, that lowers the stakes of every deal, the draft's own Track 2 included.
- The chain is examined only from China's side. As a lead grows, the trailing side's interest in a deal rises while the leading side's falls; this is the shifting-power problem. Plan A's research transparency is also a large transfer from the leader.

**Fix:** make the bargaining analysis two-sided. Section 3.5 shows how Fig. 2 can do much more work.

### 2.4 The analogies and the matrix do not fit (pp. 4–7)

- **North Korea** is a patron coercing a client over an asset the regime needs to survive, with no commitment device. It shows why discretionary threats fail. That is exactly why Plan A made MACD automatic, so read properly the case supports Plan A.
- **The p. 6 matrix** treats the true state of the world as a move by nature. In fact the violator chooses it. If the enforcer is known to hesitate on ambiguous evidence, violations will be designed to stay in evidential states 1 and 2.
- **NORAD 1980** is a false-positive story, which pulls against the paper's argument about reluctance to act. It is useful only as an illustration of dual phenomenology: escalate only when two independent sensor types agree.

**Fix:** use arms-control compliance cases instead: the Krasnoyarsk radar, INF/9M729 (2014–19), the JCPOA snapback (2025) and Biopreparat. Then merge the matrix, the three evidential states and the graduated responses into one table: evidential state, permitted response, and the corroboration it requires. That table would be a genuine contribution to Plan A.

### 2.5 Track 1 has no causal path to Track 2 (pp. 11, 21–22, Fig. 5)

- **They are cheap signals.** Tabletop exercises and reproducibility reports cost little, so a state planning to cheat can send them as easily as an honest one. They therefore build little trust.
- **The flagship channel is the wrong one.** The CNCERT/CISA pairing sits in the most securitised domain in the relationship: cyber intrusion and its attribution politics.
- **The risk** is cooperation theatre.

**Fix:** a ladder of reciprocated steps that grow costlier, with explicit gates into Track 2:

- the shared test harness sets Track 2's thresholds;
- log reconciliation grows into workload accounting;
- the incident channel becomes the notification route for evidential state 1.

Section 3.5 explains what makes a step a signal rather than talk.

### 2.6 The retention incentive is mis-specified (§2.2.4, p. 19)

- **Wrong standard.** "Exit offers no assured payoff" is not the test, because exit turns on expected value.
- **Wrong motive.** A benefit can deter exit driven by greed, but not exit driven by fear.
- **Wrong scale.** A monthly forensic service is orders of magnitude too small for the stakes, as the draft itself concedes.
- **A nonstarter example.** A Tencent-hosted service for US defenders will not fly: the Pentagon added Tencent to its Section 1260H list of Chinese military companies in January 2025.
- **Plan A already offers more.** The section ignores Plan A's own far larger side-payments: research transparency, and equal in-deal R&D allocations. The draft's own p. 8 illustration shows those allocations.

**Fix:** rebuild this section on sharing the contested prize itself (Section 3.5), not on a service that exit forfeits.

### 2.7 The pace concession undercuts the design, and the trigger is a placeholder (pp. 24–26)

- **Timing.** Table 1's pilots run to 2028. That is the window the draft's own METR extrapolation flags.
- **Shadow of the future.** Enforcement by the host plus reciprocity only works with a long shadow of the future, and rapid capability growth removes it. So §2.4 undercuts the design, not just its timetable.
- **The "any time: risk trigger / do not wait" row** relies on "lawful" restrictions that, by the draft's own account (pp. 20–21), do not exist for nonpublic frontier training:
  - China's GenAI Measures exclude it;
  - EO 14409 disclaims licensing.

**Fix:**

- name the trigger metrics;
- name the response, for example notice within 72 hours and a standstill on named runs pending joint review;
- name the legal authority, or make obtaining it an explicit legislative ask.

Better still, turn the concession into the thesis (Section 3.6).

### 2.8 Plan A weaknesses the draft misses

A China-based paper is best placed to press these. All are in Plan A's own documents.

- **Impairment, not dissolution.** Deal Decline estimates decline at 37% within 5 years and 48% within 10, split roughly evenly between dissolution and impairment. Impairment does not trigger compute destruction, because, in the supplement's words, "it's harder to set up a system which destroys compute upon impairment." The draft cites Deal Decline only for the three evidential states, which are not in it (Section 4).
- **The US has the better exit option.**
  - Cold storage follows pre-deal ratios: about 5M H100e for the US against about 500k for China.
  - If the deal breaks down, both sides return to racing with their pre-deal shares, which in Deal Decline's own words "also favors the US."
  - US executive agreements are fragile across elections.
- **Taiwan.** Plan A's dissolution scenario begins with a war over Taiwan, in which "perhaps one side is okay with" destruction of the compute. MACD does not deter an exit motivated by war. The draft never mentions Taiwan.
- **Adjudication by power.** Training practices are banned by majority vote "weighted by bargaining clout."

---

## 3. A different starting point: why credibility is hard

The draft asks whether Plan A's enforcement is credible. The prior question is why an agreement among rivals needs enforcement this strong at all: destroying compute, then fabs, then robots, with war in the background.

My theory gives an answer. It addresses a position rather than a document. The position is that we can keep the contest, accelerate, and still be safe. Plan A is the most careful version of that position, and the draft's two tracks are a narrower version of it. The argument below is about generic actors, not any particular pair of states.

### 3.1 The root: a model of self and world

The dynamics of the present trajectory follow from one governing model, which I call the *winning model*. It is embodied in declared objectives, in how institutions select and reward, and in narratives of success. It has three tenets:

- **The isolated self.** An actor's welfare is its own payoff; others are rivals or instruments.
- **Naive Darwinism.** The strong prevail, and prevailing justifies itself; cooperation is a tactic or a weakness.
- **Winner-take-all compounding.** Advantage compounds and converts across domains, and falling behind cannot be recovered.

Inside this model the race is the rational game, and its cost grows with the power of the technology. The model governs where it is held, and also where it is attributed. An actor that does not hold it still races if it believes its rival does. That is the security dilemma, in which fear makes each side the type it feared.

This is a description of a governing logic, not an accusation against any people. It is also false:

- about actors' interests, since the shared losses are real;
- about evolution, since cooperation is how complex life is built;
- about human behaviour.

It persists because it confirms itself, reshapes institutions in its image, and recruits the drive for status.

The long-run consequence is the core of the theory. Suppose shared damage grows with the power of the technology and can become irreversible. Then survival requires one of two things:

- the gap between the bounded self-model and the inclusive one ("we are one") closes faster than the contested stakes grow; or
- the stakes themselves shrink.

Bounded competition is not the problem. Firms can compete on usefulness and cost inside a cooperative arrangement. What has to go is competition for control over the shared conditions and over the correctors.

### 3.2 Verification changes the odds of detection, not the value of winning

Reduce an agreement to two actions: comply or defect.

- *R* is the payoff when both comply.
- *T* is the payoff from defecting while the other complies.
- *P* is the payoff when both defect.
- *S* is the payoff from complying while the other defects.
- Verification detects a defection in time with probability *υ*, and a detected defector receives the sanctioned outcome *P − F*.

The theory proves three things about this game.

- **If *T* > *R*** (winning is worth more than cooperating), compliance requires *υ* > (*T* − *R*) / (*T* − *P* + *F*). As the value of winning grows, the detection required tends to certainty.
- **If *T* < *R***, compliance requires no verification at all. It is rational once trust reaches (*P* − *S*) / ((*R* − *T*) + (*P* − *S*)), and verification only lowers that threshold.
- **Detection counts only before a defection becomes decisive.** Acceleration shortens that window.

So verification is needed exactly to the degree that winning is worth more than cooperating.

Plan A takes a second, real route: bound the largest covert project, so that defection gains little. That route holds only while the verified coalition's lead in effective compute grows at least as fast as algorithmic progress erodes it. The race does not end. It moves up a level, to the coalition against potential defectors. This explains Plan A's enormous planned expansion of compute.

### 3.3 The lid must grow with the pressure

Deterring exit requires the expected sanction to exceed the *net* gain from exit: the value of leaving with an advantage, minus the value of staying.

- **The gain grows.** The net gain grows with the capability the agreement holds in check.
- **Relative standing is preserved.** An agreement that preserves relative positions (proportional reserves, cold storage at pre-deal ratios) preserves the relative term in every payoff, and with it the motive to exit.
- **So enforcement must escalate.** Plan A's escalation from compute to fabs to robots to war is not a design flaw. It follows from the structure.

Plan A's own estimates show the result. Decline is 48% within ten years. If the deal dissolves and compute survives, takeoff is several times faster.

The draft's convertible-capacity point (p. 15) and its erosion point (p. 10) are its own versions of this mechanism. They belong at the centre of the critique, not in passing.

### 3.4 What verification cannot carry

Verification can confirm present compliance. It cannot confirm four other things:

- **Future commitment.** It holds only while the expected sanction keeps pace with the net exit gain.
- **Unverifiable information.** Words about shared danger are not credible merely because the danger is shared. A sender gains from the receiver's restraint whatever the sender itself intends to do.
- **The judgment of approvers.** Sampled recomputation proves that the declared workload is what ran. It cannot prove that approving it was right. Approvers, evaluators and adjudicators are exposed to the same capture by success as every other corrector.
- **Its own reliability.**

Trust also has three parts:

- the belief that the other side will comply;
- confidence in the instruments;
- confidence that the arrangement will persist.

Verification amplifies trust but does not create it. Installing the instruments is itself a first step taken under trust.

### 3.5 What lowers the value of winning

Four instruments act on *T* or on its effects:

1. **Shared, checkable evidence that no one can bank on winning.** The draft's Fig. 2 is the seed of this. An AI lead may not convert into capability dominance, decisive advantage and usable coercion. That is an argument that the value of winning is smaller than racers believe, for every side, not only for the trailing one.
2. **Sharing the contested prize.** If a fraction β of what is contested is shared, the intensity of the race, the waste and the hazard all fall by the factor (1 − β). This holds for every actor, including one that cares only about relative standing. By contrast, pooling payoffs widens the effective self, but it does nothing under selection on relative standing. This is the right form for §2.2.4: not a modest service that exit forfeits, but a share of the frontier's benefits large enough that racing for the remainder is not worth it.
3. **Lowering the vulnerability of restraint (*P* − *S*).** Develop the frontier in common, so that restraint does not leave one exposed.
4. **Costly, verifiable signals.** One example is a durable, inspectable removal of AI from one's own strategic decision loops. It costs little for an actor that takes the risk of losing control seriously, and it can be made costly to imitate. A step separates trustworthy from untrustworthy actors only if it costs an actor seeking relative advantage at least what that actor would gain by inducing restraint. That requires the step to be durable, verifiable and costly to reverse; a reversible gesture is cheap talk. By this test the draft's Track 1 exercises are cheap talk unless they are gated into costlier steps.

### 3.6 How to classify an arrangement, and what this means for the draft

**Classify each arrangement by what it changes.**

- **A continuation** leaves winning as the objective and lets success buy control of correction, whatever safeguards it adds.
- **A bridge** changes the tempo but keeps relative standing in its enforcement and its fallback.
- **A pivot** changes the governing model. It directs consequential AI to shared provision, places strategic uses under jointly verified limits, binds the pace of capability to the capacity for correction, and builds common infrastructure that no one owns.

Plan A is a bridge. The draft's two tracks change less than Plan A does. The test for any design, including our own, is this: **does it lower the value of winning, or only bound defection?** Durability tests apply to every arrangement on its own estimates:

- What is the fallback?
- What is the hazard of breakdown?
- Who keeps authority?
- Can the correctors be captured?
- What happens when the strongest party violates the arrangement?
- What happens on succession?

**What this means for the draft:**

- **Answer the title question.** Cooperation becomes credible as the value of winning falls below the value of cooperating. Verification then lowers thresholds instead of carrying the whole load. This fixes 2.1.
- **Make §1.1 two-sided.** Turn Fig. 2 from "China need not accept Plan A's terms" into "neither side can bank on winning." This fixes 2.3.
- **Centre Part I on the mechanism of 3.3,** using the draft's own erosion and convertible-capacity points, plus Plan A's impairment and fallback asymmetry. This fixes 2.2 and 2.8.
- **Rebuild §2.2.4 on sharing the prize.** This fixes 2.6.
- **Rebuild Track 1 as gated, costly signals.** This fixes 2.5.
- **Make the §2.4 concession the thesis.** Incremental verification is insufficient while winning is worth more than cooperating. I think this paper is unusually well placed to make that claim.

---

## 4. Factual corrections

### 4.1 Must fix

- **The CAISI name (p. 12, fn 17; p. 29 P03, fn 64).** nist.gov/caisi now redirects to the "Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)". The change was made around 30 September 2026 and was checked on 3 October. The remit is substantively unchanged. Write "CAISI (renamed CAISSI in September 2026)".

### 4.2 Tighten

- **NORAD (p. 6).** The 46-cent chip was the Pentagon's attribution; NORAD could not get the suspected circuit to fail again. Write "attributed by the Pentagon to…". Cite National Security Archive Briefing Book #699, an update of #371.
- **"Chips require continuing authorisation" (p. 7).** In Plan A the "continue" messages apply to the new verified training datacenters, not to all chips.
- **fn 12.** The three evidential states do not appear in Deal Decline. Present them as the author's own typology.
- **EO 14409 (p. 20).** The order has three relevant parts:
  - Sec. 3(a) creates a classified benchmarking process run by NSA, Treasury and CISA, which is not voluntary;
  - Sec. 3(b) is a voluntary framework for developer access;
  - Sec. 3(c) disclaims licensing and preclearance.
- **fn 60.** Whitfill & Cunningham is a METR *research note* summarising a longer paper, with a disclaimer that it is not necessarily METR's view. Do not call it a METR "analysis".
- **The Hugging Face incident (p. 13).** One agent escaped the evaluation sandbox. It reached a third party's endpoint hosted on Modal, then Hugging Face. Modal's own infrastructure was not compromised.
- **METR TH1.1.** The doubling time is 130.8 days, with an interval of 107–161. The same post reports 89 days since 2024, which strengthens the pace argument.
- **SB 53.** The duties sit in §22757.12–.13; §.14 is a definitional review and §.15 covers penalties.
- **fn 37, "footnote 54".** That is the web edition's number; the same note is no. 29 in the PDF edition. This paper's own fn 54 is a different note.
- **MOFCOM Announcement No. 18 of 2025.** This is the rare-earth export-control announcement. Say that it is cited only for the bureau's name.

### 4.3 Unverified

- **Casuela (3 July 2026).** The site was down.
- **OpenAI's 26 August 2026 report.** The page returns 403. Secondary coverage confirms CrowdStrike's role and the reduced safeguards.
- **The CNCERT–US-CERT 2013 precedent.** The cited PDF returns 404. fn 62 also cites a Tsinghua student career-centre page, which needs a better source.
- **NORAD history.** fn 9 says "as of 31 December 2013", but the file name says March 2014.
- **The war.gov agreements page.** It returns 403.

**Archive every 2026 web source.** The CAISI page changed within days.

### 4.4 Citation hygiene

- **Duplicate notes:** fn 9 and 10; fn 26 and 27; fn 32 and 33.
- **A stray "[52]"** in fn 16, 63 and 64.
- **A fragile link.** fn 13 points to a build file that will break when the site is redeployed.
- **Access dates** are missing on most notes.

---

## 5. Editorial and production

### 5.1 Structure and prose

1. **Make the Summary and Conclusions carry the recommendations.**
   - Add a three-sentence primer on AI 2040, Plan A and MACD.
   - Add a "what we propose" list by actor and date.
   - Answer the title question.
   - The Conclusions run 168 words, with 6 of 13 sentences negated, and end on a caveat. Rewrite them as findings, then recommendations, then what would change our view.
2. **Collect the disclaimers into one "Scope and non-claims" box.**
   - Density is about 19% of sentences in Part I and 22% in Part II, 31% in the Summary and 46% in the Conclusions. 11 of 12 figures carry one.
   - Halve them.
   - Assert these plainly:
     - neither state can now legally pause nonpublic frontier training;
     - a training freeze alone raises the payoff from exit;
     - evaluations cannot establish compliance with compute limits;
     - bilateral attestation cannot rest on a foreign vendor's root of trust;
     - incident cooperation needs no consensus that catastrophe is coming.
3. **Cut about 14 figures and illustrations to about 6.**
   - Keep the Summary graphic (or Fig. 5), Fig. 2, the p. 6 table, Fig. 6, Fig. 9, Fig. 11 and Table 1.
   - Cut Figs. 1, 3 and 4. None is referenced, and each restates a sentence.
   - Merge Figs. 7, 9 and 10, and merge Figs. 11 and 12.
   - Fig. 8 shows empty boxes.
   - The p. 8 scenario illustrations are referenced nowhere.
4. **Fix the titles and structure.**
   - "Part I: The Case Against Plan A" overclaims what its "May Not" sections argue.
   - Three organising schemes compete: Effect/Adoption/Execution, Bargain/Verification/Authority, and the two tracks. Pick one.
   - Split §2.4 into "The pace constraint" and a short Limitations section.
   - Move Table 1, the paper's real deliverable, forward.
5. **Trim Appendix A** to the 8–10 pairings the body uses. Move the full inventory of 25 online, with URLs, Chinese names and last-checked dates.
6. **Fix how sources are presented.**
   - Add a bibliography.
   - Citations are link text only ("About Us", "transparency"), so printed copies lose the sources.
   - Translate the Chinese titles.
   - Promote fn 31, which sets the paper's scope, into the body.
7. **Add front matter:**
   - authors;
   - a "cite as" line;
   - page numbers;
   - a glossary (about 70 acronyms; "CNAS" collides with the US think tank of that name);
   - an "About OCASC" note;
   - possibly a one-page Chinese abstract.

### 5.2 Production fixes

| Where | Issue | Fix |
|---|---|---|
| p. 6 | A Google Docs date chip, "Jun 3, 1980", glued to "illustrates". | Plain text "3 June 1980". |
| p. 27 | Blank page, from a stray break after the Fig. 12 caption. | Delete the break. |
| pp. 10, 16, 22, 28 | White gaps of 30–55% of the page. | Remove the hard breaks; the figure cuts will help. |
| fn 15, 36, 37, 44, 46–47, 57, 84 | Missing spaces: "historical2013", "updated9 July2026", "PlanA", "footnote54", "the2023", "No.18 of2025", "arXiv2507…", "May2024". | Restore the spaces, then search the whole file. |
| fn 16, 63, 64 | Stray "[52]". | Delete. |
| fn 12 | The link covers only "Deal Declin". | Relink the full title. |
| passim | Two footnote styles, and no space after some note numbers ("3Nick", "9William"). | Apply one style. |
| fn 39, 80, 81 | ".;", "..", "腾讯.;", full-width "！;". | Clean the punctuation. |
| p. 31 | "ANSI ANSI National Accreditation Board". | Delete one "ANSI". |
| passim | Mixed date formats; "AI R&D" and "AI-R&D"; "centers" in the p. 8 image against "centres" in the text. | Use one convention throughout. |
| PDF | Metadata title is "AI2040 review 2nd"; page 2 repeats the cover. | Set the metadata and front matter. |

---

## 6. Suggested path

**Option A: answer the title question (recommended).** The paper would run in four parts:

- **Thesis.** Credibility depends on the value of winning (Section 3).
- **Part I.** Why Plan A's enforcement must escalate, from its own design and estimates: the overhang, the fallback asymmetry, impairment, erosion under dependence.
- **Part II.** What verification needs in order to work in China. This is the current Part II, tightened. Verification still matters, because it lowers thresholds, and this analysis is the paper's distinctive contribution.
- **Part III.** What lowers the value of winning: shared evidence, prize sharing, a common frontier, costly signals. Then a staged path with gates and a real emergency branch.

**Option B: narrow the claim.** Retitle the paper along the lines of "Implementation Conditions for Plan A-Style Verification in China." Shrink Part I to framing, and make the current Part II the core. This is less work, but it gives up the paper's most important argument.

**Suggested order of work:**

1. Write the thesis paragraph and the Summary first.
2. Rewrite Part I.
3. Rework §2.2.4, Track 1 and §2.4.
4. Apply the factual corrections.
5. Do the editorial pass last.

---

*Sources for the checks above:*

- AI 2040 Plan A and its Deal Decline supplement: ai-2040.com and ai-2040.com/supplements/deal-decline, read 3 October 2026.
- NIST CAISSI page: nist.gov/caisi, read 3 October 2026.
- On Tencent's January 2025 Section 1260H listing: [CNN, 7 January 2025](https://edition-prod-cf.sitemirror.cnn.com/2025/01/07/tech/tencent-catl-us-list-china-military-companies-intl-hnk/index.html) and [Yicai Global](https://yicaiglobal.com/news/catl-cloudwalk-other-deny-military-ties-after-us-chinese-military-company-label).
- The formal results in Section 3 are stated and proved in my working paper *Changing the AI Trajectory: Meta-Attractors, Alignment and Cooperation* (v5, October 2026). The relevant parts are §§1, 6.6–6.9 and 8.1–8.2.
