# COHERENCE-A: the integration editor's read of the V6.2 core

4 October 2026. One reading of the whole core, abstract to conclusion, from a THEORY.md assembled out of `src/` in a scratch copy at the time of reading (assembler: "no problems"; 56,099 words without references). I judged it as one paper: one voice; one home per point; conditions owned by statements; claim boxes a thirty-minute reader can trust; hand-offs; the plan's vocabulary (§8.3); no repetition or contradiction between sections; Ren's voice; the standing rules. I read it against V6.2-PLAN, CLAIMS §8–§9, the open issues in elegance-build-notes, EVIDENCE and TESTS, and, wherever a quotation was in question, against the corpus. No file was edited.

**Verdict.** The core reads as one paper. The chain agrees with the statements it summarizes in each of its homes: the abstract, the guide, §1.2 and §12.4. The tiers agree across the abstract, the guide, §12's box and §12.1. Every number that appears twice appears the same both times, and every section hands off to the next. What is wrong is local, but much of it sits on the thirty-minute path: the definition of tier 1(b), the scope of admission, a handful of attributions and three citations. Ten edits fix every error and contradiction I found. Twenty-two more improve the page.

**Form of each entry.** Each entry gives the file and line in `src/core/` (current line numbers), the current text, the replacement, the reason, and whether the edit is necessary or improving. Texts are exact, markup included, and each "current" string occurs exactly once in its file. I applied all 47 replacements together to a scratch copy (`scratchpad/cohB`). There the assembler reports "no problems" and `xref_v62.py` reports "ALL CHECKS PASS". Run against the present THEORY, `sentcheck.py` flags only two things: the paragraph that edit 15 deletes, whose points live in Remark 2.5 and §10.4, and the sentence that edit 26 rewords. I did not rerun `checks_v62.py`, since no number changes. Edits that touch a decision CLAIMS §9 leaves to Ren say so.


## A. The top ten (all necessary: an error, a contradiction, or a misattribution on the page)

### 1. Tier 1(b)'s definition does not fit its item 8 (necessary)

`src/core/c0_s12.md` line 18, §12.1, Tier 1(b) opening.

Current:
```text
What these items guard against arrives before the evidence that would show it: an alarm averaged over captured evaluators fires late or not at all ({{masking}}); where capture precedes evidence, the host crosses its floor before any alarm ({{slowroute}}); and a masked divergence is detected only as often as it shows under evaluation ({{masked}}) [thm∣prem]. A protection that waits for that evidence waits too long, so under the protection standard the burden of proof lies on withdrawal: each item stands until its crux is measured favourable, and then loses only the part that crux bears [val].
```

Replace with:
```text
What items 6 and 7 guard against arrives before the evidence that would show it: an alarm averaged over captured evaluators fires late or not at all ({{masking}}); where capture precedes evidence, the host crosses its floor before any alarm ({{slowroute}}); and a masked divergence is detected only as often as it shows under evaluation ({{masked}}) [thm∣prem]. A protection that waits for that evidence waits too long, so under the protection standard the burden of proof lies on withdrawal: each item stands until its crux is measured favourable, and then loses only the part that crux bears [val]. Item 8 stands on every reading; the part its cruxes bear is only the reliance on it to change conduct, which moves to custody and pace where C6 or C8 is measured against it.
```

*Why.* The tier is defined by withdrawal on a favourable measurement and justified by harms that arrive before evidence. Neither fits item 8: sharing and provision guard against no capture or masking, are never withdrawn (they 'realize joint value on every reading'), and what C6/C8 can remove is a reliance, on an unfavourable reading. The elegance pass flagged this (elegance-build-notes §6 item 5, U12 #3) and it is still on the page. The edit keeps the plan's placement and makes the tier's definition true of all three items. (Alternative for Ren: move item 8 to tier 1(a), whose criterion, a justification that no crux changes, it meets.)

### 2. §6.6 scopes admission to "a positive tax"; §12.1 and R8a put the burden on withdrawal (necessary)

`src/core/60_s6.md` line 101, §6.6, outer level.

Current:
```text
for divergences with common costs and a positive tax, with masked classes admitted by capability threshold ({{masked}});
```

Replace with:
```text
for divergences with common costs until their tax is measured zero or negative (Section 12.1), with masked classes admitted by capability threshold ({{masked}});
```

*Why.* §6.6 scopes admission to classes with 'a positive tax'; §12.1 item 7 applies it to every common-cost class and withdraws it only when the tax is measured zero or negative, and Table 9.1 R8a lists 'a tax zero or negative' under 'Not needed when'. Read together, §6.6 puts the burden of proof on imposing the constraint and §12.1 on withdrawing it. The judgment's version is the one the protection standard supports; §6.6 should state it, not its opposite.

### 3. "In the author's words" and quotation marks on lines that are not his (CLAIMS D7, D9, D30, D31, D32) (necessary)

**3a.** `src/core/30_s3.md` line 119, §3.8, Ψ individually rational.

Current:
```text
In the author's words, "the strategy that wins locally takes the name of rationality"
```

Replace with:
```text
The corpus puts it: "the strategy that wins locally takes the name of rationality"
```

*Why.* CLAIMS D9: the drafters' sentence in the causal-chain essay, not his words. 'In the author's words' asserts what the register denies.

**3b.** `src/core/b0_s11.md` line 17, §11.1, trust as outcome.

Current:
```text
In the author's words, "Trust is not a prerequisite
```

Replace with:
```text
The corpus puts it: "Trust is not a prerequisite
```

*Why.* CLAIMS D30: a system-prompt line the corpus lists as AI-drafted from his ideas; authorship uncertain.

**3c.** `src/core/c0_s12.md` line 47, §12.2, Meadows.

Current:
```text
In the author's words, "If we don't solve dominant attractors
```

Replace with:
```text
The corpus puts it: "If we don't solve dominant attractors
```

*Why.* CLAIMS D32: same prompt as D30; authorship uncertain.

**3d.** `src/core/30_s3.md` line 117, §3.8, Definition 3.13 (Ψ2).

Current:
```text
prevailing certifies fitness and right; "the winner takes all, and the winner justifies all" [corpus: selfishness-spiral]
```

Replace with:
```text
prevailing certifies fitness and right: a system that rewards the winner with more edge to win goes "into winner takes all, but also winner justifies all" [corpus: selfishness-spiral]
```

*Why.* CLAIMS D7: the quoted line is the README's paraphrase, in quotation marks; his words (2025-02-03, GLOSSARY l.277, verified in _process/CRITIQUE-FINDINGS) are 'If a system reward winner more edge to win, eventually the system go into winner takes all, but also winner justifies all'. The replacement quotes only his words, raw, and keeps the sentence's job.

**3e.** `src/core/30_s3.md` line 119, §3.8, false as a doctrine.

Current:
```text
and the clause "the winner justifies all" is rejected
```

Replace with:
```text
and the clause "winner justifies all" is rejected
```

*Why.* Same: make the quoted clause his exact words.

**3f.** `src/core/10_s01.md` line 42, §1.3, last paragraph.

Current:
```text
the rejection of "the winner justifies all"
```

Replace with:
```text
the rejection of "winner justifies all"
```

**3g.** `src/core/50_s5.md` line 60, §5.2, after Proposition 5.8.

Current:
```text
This is the formal content of Ψ2, "the winner takes all, and the winner justifies all" ({{psi}}), exact for linear payoffs.
```

Replace with:
```text
This is the formal content of Ψ2, "winner takes all, but also winner justifies all" ({{psi}}), exact for linear payoffs.
```

**3h.** `src/core/b0_s11.md` line 40, §11.3, E1 broad form.

Current:
```text
*The broad form*, AI not an instrument in any contest that tends toward dominance or concentration, judged by the game and not by the act, has its criterion and the three layers of its enforcement in Section 6.6. **Broad E1 is the scope; narrow E1 is the first step** [corpus: alignment-selection, 2026-09-26].
```

Replace with:
```text
*The broad form*, judged by the game and not by the act, has its definition, its criterion and the three layers of its enforcement in Section 6.6; it is the scope, and the narrow form the first step.
```

*Why.* CLAIMS D31: the scope is his ruling of 2026-09-26, but 'narrow E1 is the first step' is the assistant's reading. The bold line with a corpus tag presents it as his. It is also the fourth statement of the same line in the core (§1.2 item 9, §6.6, §10.5, §12.1 'The scope'); §12.1 keeps the plan's closing line, and §11.3 needs only the pointer.

**3i.** `src/core/10_s01.md` line 48, §1.4, Tags.

Current:
```text
[corpus: key] marks the author's own words; the English renderings of his Chinese, and the paraphrases a drafting model made of his spoken words, are the drafters', awaiting his confirmation (CLAIMS).
```

Replace with:
```text
[corpus: key] marks the author's own words; the English renderings of his Chinese, and the paraphrases a drafting model made of his spoken words, are the drafters', awaiting his confirmation (CLAIMS), and lines the corpus records whose authorship it does not settle are introduced as the corpus's, not as his.
```

*Why.* States the convention 3a–3c apply, so a reader can tell 'In the author's words' from 'The corpus puts it'.

### 4. §12.4 alters a tagged corpus line (necessary)

`src/core/c0_s12.md` line 83, §12.4, second paragraph.

Current:
```text
Change the basin first; then add speed [corpus: meta-attractor].
```

Replace with:
```text
Change the basin, then add speed [corpus: meta-attractor].
```

*Why.* The corpus line is 'change the basin, then add speed' (meta-attractor README l.3, l.544; CLAIMS D3), and Remark 2.5 quotes it so. §12.4 carries the corpus tag on an altered form. The plan's 'first; then' was a paraphrase, not the corpus's words.

### 5. One thesis line in two forms: "favoured" and "to continue" (necessary)

`src/core/30_s3.md` line 94, §3.6, the bolded claim.

Current:
```text
is a long-term requirement if growth and change are favoured**
```

Replace with:
```text
is a long-term requirement if growth and change are to continue**
```

*Why.* One thesis line in two forms: 'are favoured' here, 'are to continue' in the abstract, §1.2 item 2, §12.4 and the guide (增长与变化得以延续). The forms differ in kind: 'favoured' makes it conditional on a value, 'to continue' on an outcome, and the formal content §3.6 gives (only anticipation acts in time against a global, irreversible failure) supports the outcome form. CLAIMS D36 and §9 item 5 leave the choice to Ren; whichever he picks, all five places should carry it.

### 6. Strand table: a citation that lost its reason in the elegance pass (necessary)

`src/core/a0_s10.md` line 68, §10.4, strand table, row "Reward separated from advantage".

Current:
```text
evaluated at the present distribution of standing, not at parity ({{corrrate}}(4));
```

Replace with:
```text
evaluated at the present distribution of standing, not at parity, since cultivated conversion into correctors grows with a high moment of shares ({{corrrate}}(4));
```

*Why.* The elegance pass cut the reason (draftA: 'where the reflexive channel's gain scales with a high moment of shares'). Proposition 4.5(4) is about the concentration of cultivated conversion; it does not say that a structural gain must be evaluated off parity, so the cite no longer supports the clause it is attached to. Restoring the reason makes it support it again.

### 7. Remark 10.3 mis-cites Proposition 5.1 (necessary)

`src/core/a0_s10.md` line 40, §10.2, Remark 10.3.

Current:
```text
At the first order more contenders make the race fiercer ({{join}}(4));
```

Replace with:
```text
At the first order more contenders make it likelier that one of them starts the race ({{join}});
```

*Why.* Proposition 5.1(4) (S5) says the race begins with probability tending to one as capable actors multiply; it says nothing about how fierce the race is. The core states 5.1 only in prose, so a reader cannot find a part (4).

### 8. Crux C0, as worded, doubts a theorem (necessary)

`src/core/c0_s12.md` line 57, §12.3, crux C0.

Current:
```text
Whether moving a shared parameter moves several thresholds of {{thresholds}}, the arms of {{scissors}} among them, and the signatures of several groups together
```

Replace with:
```text
Whether, in the world, the thresholds of {{thresholds}} that a shared parameter enters, each in its own model, move together as it moves, the arms of {{scissors}} among them, and with them the signatures of several groups
```

*Why.* §7.1 states as [thm, cell by cell] that a change in one shared parameter moves several thresholds in their models; C0 is whether they move together in the world (§1.4, §5 box, §7.1, §12.4). The crux row, as written, asks whether the theorem holds.

### 9. "Four safeguards" names two different sets in §9 and §10.3 (necessary)

**9a.** `src/core/90_s9.md` line 29, §9, Sufficient safeguards.

Current:
```text
**Sufficient safeguards, and form.** Four safeguards are sufficient and not necessary:
```

Replace with:
```text
**Sufficient routes, and form.** Four routes are sufficient and not necessary:
```

*Why.* §10.3 opens 'Four safeguards make consequences return' and names them (I1)–(I4); §9's 'four safeguards' are a different set of four, one of which is 'the safeguards (I1)–(I4)'. Two adjacent sections use the same counted phrase for different sets.

**9b.** `src/core/90_s9.md` line 29, §9, Sufficient safeguards.

Current:
```text
S9 gives the margins and what each safeguard certifies and does not.
```

Replace with:
```text
S9 gives the margins and what each route certifies and does not.
```

### 10. Broad E1 defined two ways (necessary)

`src/core/10_s01.md` line 29, §1.2 item 9 (last sentence).

Current:
```text
Broad E1, AI not an instrument in any contest that tends toward concentration, is the scope; narrow E1 is the first step.
```

Replace with:
```text
Broad E1, AI not an instrument in any contest that tends toward dominance or concentration, is the scope; narrow E1 is the first step.
```

*Why.* The definition reads 'dominance or concentration' in §6.6, §11.3, §12.1 and the guide (趋向支配或集中); §1.2 drops 'dominance'.

## B. Improving edits, in order of value to the page


### 11. §0 repeats §6.6's mechanism almost word for word (improving)

`src/core/10_s01.md` line 7, §0, The game, not the act.

Current:
```text
The analysis judges games, not acts, and structures, not persons. In a contest decided by relative strength, an instrument that every contestant adopts leaves each adopter where it stood and pushes down whoever lacks it, and where people are themselves the instrument, as in labour, it displaces them. No single use shows this; the aggregate does, in labour, finance and persuasion as much as in force, so a use that helps one person can still be an instrument in a game that concentrates control (Section 6.6).
```

Replace with:
```text
The analysis judges games, not acts, and structures, not persons: in a contest decided by relative strength, an instrument that every contestant adopts leaves each where it stood and pushes down whoever lacks it, which no single use shows and the aggregate does, in labour, finance and persuasion as much as in force (Section 6.6).
```

*Why.* §6.6 states the same mechanism in nearly the same three sentences, with Ren's line, and is its home. §0 keeps the mechanism in one sentence for the thirty-minute reader.

### 12. Name the four conditions of a correction decision: contestable (improving)

**12a.** `src/core/50_s5.md` line 82, §5.3, the growth channel.

Current:
```text
its coverage $U_t$, the number of those modes for which correction is in place that meets four conditions at a stated catch rate;
```

Replace with:
```text
its *contestable coverage* $U_t$, the number of those modes for which contestable correction is in place at a stated catch rate;
```

*Why.* 'Contestable coverage' is the paper's term (abstract, §1.2, §5 box, Theorem 5.13, Table 7.1, §10.4, §12.3) but is never defined under that name; the definition says 'meets four conditions'. A count of 'four conditions' also collides with V6.1's four conditions of the pressure, which Definition 2.1 now gives as three (CHANGELOG). Naming the property removes both problems and matches 'contestability' in §6.5–6.6.

**12b.** `src/core/50_s5.md` line 82, §5.3, the growth channel.

Current:
```text
A correction decision meets the four conditions if it is **legible**
```

Replace with:
```text
A correction decision is *contestable* if it is **legible**
```

**12c.** `src/core/d0_symbols.md` line 29, Symbols and labels.

Current:
```text
the four conditions of a correction decision are legible, overrulable, exercised and resourced;
```

Replace with:
```text
a correction decision is contestable when it is legible, overrulable, exercised and resourced;
```

### 13. Define "decisive class" and "common custody" where they first carry weight (improving)

`src/core/50_s5.md` line 52, §5.2, Corollary 5.7(a).

Current:
```text
(a) changing the premise itself, so that deviations do not become decisive: not building capability of the decisive class, holding it so that no party can use it alone, or detecting and answering faster than breakout;
```

Replace with:
```text
(a) changing the premise itself, so that deviations do not become decisive: not building capability of the decisive class (capability with which a deviation could reach a decisive position), holding it so that no party can use it alone (common custody), or detecting and answering faster than breakout;
```

*Why.* 'The decisive class' and 'common custody' carry E2, tier 2 and G4, and appear in the abstract, §1.2, three boxes and §12.1, but neither is defined in the core. This is their first formal use, and the parentheses define them where the decisive position is defined. (No italics: the statement is already italic.)

### 14. Gloss "host" before §3.1 (improving)

**14a.** `src/core/00_head.md` line 5, Abstract.

Current:
```text
With one host and no outside,
```

Replace with:
```text
With one host, the shared conditions every carrier lives in, and no outside,
```

*Why.* The plan defines 'host' once, with no parasitic sense, but the thirty-minute reader meets it in the abstract, §1.2 and the §3 box before §3.1 defines it, and the parasitic sense is the default reading in English.

**14b.** `src/core/10_s01.md` line 22, §1.2 item 2.

Current:
```text
All carriers share one host and are coupled through it
```

Replace with:
```text
All carriers share one host, the body of shared conditions every carrier lives in (Section 3.1), and are coupled through it
```

### 15. §4.6 restates Remark 2.5 and §10.4 (improving)

`src/core/40_s4.md` line 114, §4.6, penultimate paragraph.

Current:
```text
The same recursion can be generative, but not by the same selection. Correction keyed to no one is not selected among carriers ({{noinside}}), so a generative order cannot rely on its winners to fund correctors they cannot control; it is kept by coverage and financing fixed in formula, through a loop that runs through the whole rather than through its winners ({{pathgen}}; Section 10.4), and whether that loop attracts is a conjecture [conj].
```

Replace with: nothing (delete the paragraph and the blank line after it).

*Why.* Third statement of one point: Remark 2.5 already says the generative order is not selected among carriers (citing Proposition 4.4) and is held by coverage and formula funding, and §10.4 'How the generative order persists' and 'Is the generative order an attractor?' is its home, with the [conj]. Deleting it lets §4.6 end on its refutation conditions and its hand-off.

### 16. "Does not derive that its net effect is positive": three homes for one sentence (improving)

**16a.** `src/core/80_s8.md` line 76, §8.3(f), The hard case.

Current:
```text
The theory does not derive that its net effect is positive and states the case as hard; Section 12.1 states, once, the conditions under which a coercive restriction of frontier inputs enters even the comparison of designs.
```

Replace with:
```text
The case is hard; Section 12.1 states, once, the conditions under which a coercive restriction of frontier inputs enters even the comparison of designs, and what the theory does not derive about it.
```

*Why.* 'The theory does not derive that its net effect is positive' appears three times (§8.3(f), §10.5, §12.1). §8.3 and §10.5 both say §12.1 is the one home; let §12.1 carry the sentence.

**16b.** `src/core/a0_s10.md` line 107, §10.5, A candidate configuration.

Current:
```text
it has one home, the compared-not-settled tier of Section 12.1, under three conditions of its own, and the theory does not derive that its net effect is positive.
```

Replace with:
```text
it has one home, the compared-not-settled tier of Section 12.1, under three conditions of its own.
```

### 17. §12.4 calls the effects the pressure (improving)

`src/core/c0_s12.md` line 81, §12.4, first paragraph.

Current:
```text
and capacity converts decisively into winning, success raises the stakes and the gain from defection and weakens the sanctions, the correctors and the shared language that could restrain it, each in its own model of Part I; that these move together as the stakes outgrow what does not have to be won is the conjecture the diagnosis tests (C0). That is the selection pressure of winning.
```

Replace with:
```text
and capacity converts decisively into winning, the carriers are under the selection pressure of winning: success raises the stakes and the gain from defection and weakens the sanctions, the correctors and the shared language that could restrain it, each in its own model of Part I; that these move together as the stakes outgrow what does not have to be won is the conjecture the diagnosis tests (C0).
```

*Why.* Definition 2.1 makes the three conditions the pressure; 'That is the selection pressure of winning', after a list of effects and a conjecture, names the effects instead. The replacement names the pressure as the abstract's first sentence does.

### 18. The §3 box tags an identification [thm] (improving)

`src/core/30_s3.md` line 3, §3 claim box, last sentence.

Current:
```text
However carriers are grouped, selection does not favour what benefits all; against failure that is global and irreversible, integration must be anticipated, and understanding is how actors come to count what selection cannot see [thm].
```

Replace with:
```text
However carriers are grouped, selection does not favour what benefits all [thm]; against failure that is global and irreversible, integration must be anticipated, since adoption after failure comes too late, and understanding is the transmission by which actors come to count what selection cannot see [def].
```

*Why.* Lemma 3.11 proves that the benefit cannot rise by selection and can rise only by transmission or a rule; that understanding is that transmission is an identification (§3.6: 'Understanding is the lemma's transmission term'), not a theorem. A thirty-minute reader should not see it tagged [thm].

### 19. Make the tests the core cites readable in the core (improving)

`src/core/70_s7.md` line 100, §7.4, after Test G.

Current:
```text
so the test discriminates at intermediate $p_d$ (Section 5.5; S5) [num: JX].
```

Replace with:
```text
so the test discriminates at intermediate $p_d$ (Section 5.5; S5) [num: JX].
- **The others** are cited where their mechanism is, and TESTS states each with its discriminating contrary: Test B, influence and the authorship of standards by share, and carriers' positions on correction keyed to no one (Section 4.6); Test D, share levels against rule support after a reform that insulates rule-making (Section 11.4); Test I, the row sums of a leading coalition's own correctors and its dependence on the governed ({{raceselects}}; C4, C13); Test L, which divergences developers correct, by cost incidence (Section 6.4; C9); Test M, evaluators' row sums and the execution of findings against leaders, under present funding and under item 6 of Section 12.1 (C2).
```

*Why.* Tests B, D, I, L and M are cited fifteen times in the core (Test I six times, as the measure of C4 and C13) and defined only in TESTS. One line makes each citation readable without leaving the core.

### 20. The EV12 sentence understates what held and overstates what failed (improving)

`src/core/40_s4.md` line 112, §4.6, What would refute.

Current:
```text
The author's pilot experiment on this mechanism did not support it, one of four pre-specified predictions failing (EV12);
```

Replace with:
```text
In the author's pilot experiment one of four pre-specified predictions failed, and the experiment gives the mechanism no support yet (EV12);
```

*Why.* As written it reads as if the failure of one prediction in four amounted to non-support of the whole; EV12 says P2–P4 held, P1 failed, and 'no experimental support for the mechanism of THEORY §4 yet'. The replacement states both facts in the register's order.

### 21. Dyad phrasing: "both leading states", "bilateral" (improving)

**21a.** `src/core/70_s7.md` line 88, §7.3, T6 row.

Current:
```text
while both leading states declined the latest multilateral declaration on military AI
```

Replace with:
```text
while leading states declined the latest multilateral declaration on military AI
```

*Why.* 'Both leading states' and 'two leading states' / 'bilateral' make a pair the subject of the world the paper describes, which the standing rule (and Ren's 2026-10-03 ruling: whatever states, whatever firms) excludes even when unnamed. The observations survive in roles.

**21b.** `src/core/b0_s11.md` line 78, §11.4, Where things stand.

Current:
```text
and in two leading states' affirmation of human control over nuclear use and a bilateral dialogue with an incident channel; narrow E1 has no multilateral document that both leading states now endorse, and its only shared basis is that bilateral affirmation (EV7, EV8) [obs].
```

Replace with:
```text
and in an affirmation by two rival states of human control over nuclear use, with a dialogue and an incident channel between them; narrow E1 has no multilateral document that the leading states now endorse, and its only shared basis is that affirmation (EV7, EV8) [obs].
```

### 22. §1.2's title promises one page and runs to three (improving)

`src/core/10_s01.md` line 19, §1.2 heading.

Current:
```text
### 1.2 The argument in one page
```

Replace with:
```text
### 1.2 The argument, step by step
```

*Why.* §1.2 runs to 1,480 words, about three pages. A title the section cannot keep costs trust on the thirty-minute path.

### 23. Race grammar in the theory's voice (improving)

**23a.** `src/core/80_s8.md` line 23, §8.1, Lemma 8.2 Scope.

Current:
```text
that is where regulated competition can win.
```

Replace with:
```text
that is where regulated competition can come out ahead.
```

*Why.* Plan §8.3(7): no race grammar in the theory's own voice.

**23b.** `src/core/c0_s12.md` line 77, §12.3, after the table.

Current:
```text
a conjunction would say that regulated competition wins only by becoming this paper's own design.
```

Replace with:
```text
a conjunction would say that regulated competition comes out ahead only by becoming this paper's own design.
```

### 24. §12.2 restates Remark 3.10 (improving)

`src/core/c0_s12.md` line 43, §12.2, first paragraph.

Current:
```text
The working objective that compounding sets is no error but each actor's correct computation of its interest; where convertibility and decisiveness are high it is narrow even in an actor whose held self-model is accurate, and no argument corrects it [thm∣prem]. Understanding reaches it only as the way actors agree on which parameters to move, and hold them there for their dwell time.
```

Replace with:
```text
The working objective that compounding sets is no error, and no argument corrects it ({{twoerrors}}); understanding reaches it only as the way actors agree on which parameters to move, and hold them there for their dwell time.
```

*Why.* Restates Remark 3.10, which §0, §3.8, §6.1 and §7.1 already apply; §12.2's job is the second place of leverage, which the shortened sentence keeps.

### 25. First pointer to narrow E1 goes to its restatement (improving)

`src/core/40_s4.md` line 61, §4.3, end of Proposition 4.6 discussion.

Current:
```text
and narrow E1 (Section 11.3), act on this term.
```

Replace with:
```text
and narrow E1 (Section 6.3), act on this term.
```

*Why.* Narrow E1 is introduced in §6.3; §11.3 restates it as an arrangement. The first pointer should go to the definition.

### 26. A bare "only slowing helps" (improving)

`src/core/50_s5.md` line 80, §5.3, after Proposition 5.12.

Current:
```text
For classes with an irreducible lag only slowing helps.
```

Replace with:
```text
For hazard classes whose manifestation window alone gives $a\tau_e\ge1$, only slowing, which lowers $a$, restores the margin.
```

*Why.* Statements own their conditions (plan §8.2): the bare sentence leaves the reader to supply which lag and which bound.

### 27. E2 defined with its end in §11.3 and without it in §5.3 (improving)

`src/core/50_s5.md` line 88, §5.3, E2 defined.

Current:
```text
Call **E2** stopping: not building capability of the decisive class, with rollback where hazardous variety already exceeds coverage.
```

Replace with:
```text
Call **E2** stopping: not building capability of the decisive class while the conditions for governing it are absent (Section 11.3), with rollback where hazardous variety already exceeds coverage.
```

*Why.* §11.3 defines E2 with its ending condition ('while the conditions for governing it are absent: an accurate model of the coupling, the shared prediction, and common custody'); §5.3 defines it without, so E2 reads as permanent in one place and conditional in the other, and tier 2's 'custody and E2 activate' together reads oddly without the clause.

### 28. Chinese/English order of the one quotation that differs (improving)

`src/core/50_s5.md` line 94, §5.3, the mind.

Current:
```text
The author's book puts it in one line, 癌亦增长，而其长竭母体之生: cancer grows too, but its growth exhausts the life of its host [corpus: shengsheng, 2026-07-14].
```

Replace with:
```text
The author's book puts it in one line: cancer grows too, but its growth exhausts the life of its host (癌亦增长，而其长竭母体之生) [corpus: shengsheng, 2026-07-14].
```

*Why.* Every other Chinese line in the core gives the English first and the original in parentheses before the tag (§3.8 twice, §4.2, §6.2, §6.6 twice, §7.1, §10.1, §10.4 twice, §10.5 table 共同基础…). Quotation convention; CLAIMS §9 item 4.

### 29. The one corpus tag of a different shape (improving)

`src/core/50_s5.md` line 94, §5.3, the mind.

Current:
```text
[corpus: meta-attractor; Ren, 2026-09-25]
```

Replace with:
```text
[corpus: meta-attractor, 2026-09-25]
```

*Why.* The only tag that names Ren and uses a semicolon; every other dated tag is [corpus: key, date].

### 30. §5.2 duplicates §12.1's Estimator (improving)

`src/core/50_s5.md` line 44, §5.2, after Remark 5.5.

Current:
```text
so an estimate of either that is to trigger a response has to come from correctors whose independence is certified (Section 12.1).
```

Replace with:
```text
which is why Section 12.1 assigns their estimation to certified correctors.
```

*Why.* §12.1's Estimator states the requirement in full; §5.2 needs only the pointer (elegance-build-notes §6 item 5, U05 #4).

### 31. "We represent" in the analytic voice (improving)

`src/core/40_s4.md` line 9, §4.1, opening paragraph.

Current:
```text
We represent the correctors by a field of selection domains
```

Replace with:
```text
The correctors are represented by a field of selection domains
```

*Why.* The only first-person plural in the theory's analytic voice; elsewhere it is 'this paper' or impersonal. (The 'we' of §0 and §12.4 is the affirmative meaning and stays.)

### 32. Pair the design's failures with their reversals in §12.1 (i) (improving)

`src/core/c0_s12.md` line 34, §12.1, reason (i).

Current:
```text
each of the design's failures but two has such a reversal, into separately held functions, recertification, funded standby, rotation or a sunset (X8, row by row);
```

Replace with:
```text
each of the design's failures but two has such a reversal: dissolution, into separately held functions; capture of one function, by recertification; interruption of an essential service, by funded standby; collusion among its checks, by rotation and plural lineage; overreach of a common constraint, by a sunset and appeal (X8, row by row);
```

*Why.* Reason (i) carries the ranking at the standard's third step, and §12 is on the thirty-minute path, but the core lists the reversals without the failures they reverse; the pairing is in X8 only. Naming the five pairs (X8's rows for the design, verbatim in substance) lets a core reader check the claim 'all but two'.

## C. What the core reader needs and cannot find

1. **What "the decisive class" is.** It carries E2, G4 and tier 2, and it appears in the abstract, §1.2, three boxes and §12.1, but nowhere in the core is it defined. Edit 13 defines it.
2. **What common custody is, as an arrangement.** The core says only this much:
   - capability "held so that no party can use it alone";
   - the form row "Common custody, or not built" (§10.5);
   - "separated functions under correctors certified independent of every party", in passing (§8.3(e)).

   Who holds custody, under which correctors, and how activation by mechanism executes are in X10 only. One sentence in §12.1 item 4 would close the gap: name the holders and correctors, and point to the X10 section by name.
3. **"Host" before §3.1.** Edit 14.
4. **Tests B, D, I, L and M.** Edit 19.
5. **The design's failure modes paired with their reversals.** Reason (i) of §12.1 rests on this pairing. Edit 32.
6. **Who registers the tier-2 margin, and how it is revised.** The trigger fires on "a margin registered in advance", and the *Estimator* bullet says who estimates the times, but not who registers the margin. TESTS §6.1 has the answer, and one clause in the *Trigger* bullet would bring it into the core.
7. **The parts of Proposition S8.1.** §11.2, §11.3 and Table 11.3 cite it by part: (2), (3) and (5). §8.1 states it in one sentence about the four signs and does not number its parts. The citing sentences carry enough content to be read, but "(2)" and "(3)" point at nothing in the core. Either drop the part numbers in the core, or give S8.1's parts one clause each in §8.1.

## D. Checked and found coherent

- **Numbers that appear twice, or that come from a source, agree:**
  - $\Gamma^{\rm eq}$ exceeds one at a structural gain of 0.45 (§2.2; S2, where $r^{\rm eq}/r\approx2.5$ there).
  - 0.381 (Remark 3.10; S3).
  - $\theta_g=1$ at $n=4$, $r=1$ (§5.1).
  - 1.6 to 2.6 (Proposition 4.6; S4).
  - 0.61 and 0.0054, 0.035, 0.14 and 0.49 (Proposition 10.1; S10, where the third is 0.141).
  - 10.45 → 3.81 and 10.44 (§11.4; S11).
  - The bound on the lock (§6.3; Remark S6.1).
  - "About four months" (§7.2; EV5).
  - $0.95^7\approx0.70$ (§11.3).
  - $n/(n-2)$ and "three times among three" (§1.2, the §5 box, Proposition 5.16, Table 7.1, the guide).
  - $\Lambda^\ast$ (§2.2 and Proposition 5.17(1)).
- **Tiers.** The abstract, the guide, §1.2 item 9, §12's box and §12.1 place the same steps in the same tiers. The trigger and the three conditions of coercive restriction are worded alike in the guide and in §12.1. Coercive restriction has one home, §12.1, with pointers from §8.3(f), the §8.4 table, §10.5 and §11.3.
- **Counted conditions.** Definition 2.1 has three conditions everywhere it appears. The other "three conditions", those of Proposition 4.13's clock version and of coercive restriction, are distinct and labelled. The only "four conditions" are those of a correction decision (edit 12).
- **When admission applies.** Every statement says "before consequential deployment, internal deployment included": §6.6, R8a, §9's *Where admission does not reach*, §12.1 item 7 and the guide. Admission at release only is named as a limit (§6.4, §9). Only the scope differed (edit 2).
- **E2 and E3** are never interchanged, and "stopping is not slowing" stands in §5.3, §11.3 and §12.1.
- **Vocabulary (plan §8.3).**
  - Absent: "manufactures", "win the race", "every forward-looking actor" and "shared flourishing".
  - In use: "the drive" for §7.1's driver; "keep pace"; "structural loop gain" and "equilibrium gain"; "signature" (征候 in the guide).
  - "Provision not won in the contest" is defined once (§2.2), with "provision beneath the game" as its name in prose.
- **Roles.** `xref_v62.py` finds no named state or firm in the core; only the dyad phrasing of edit 21 remains.
- **Hand-offs.** Each of §2–§11 ends by naming what the next section takes, and each Part's opening states the kind of claim it makes.
- **Provenance.** Plan §5 required two lines to be found in the corpus, and both are there, so their attributions stand:
  - 不要把人类尚未解决的斗争，升级为智能的斗争: the 至善 essay of 2026-07-23 (CLAIMS D18);
  - 真正之秩序，非得永远正确之人，乃立错误不能无限扩大之构: the book of 2026-07-14, and v4.
- **Ren's register.** The affirmative meaning opens the paper (§0) and closes it (§12.4). "Growth is not the danger; the mind is" has its home in §5.3. The opposition is always to a logic, never to a participant.

## E. Decisions for Ren that these edits touch (CLAIMS §9)

- **Item 4, quotation conventions.**
  - Edits 3a–3i apply one rule: "In the author's words" only for his verbatim lines; "The corpus puts it" for lines whose authorship the corpus does not settle; no quotation marks around a paraphrase. §1.4 states the rule (edit 3i).
  - Still open: bracketed repairs or the raw original. These are repaired or glossed inside the quotation marks:
    - §2.1 "optimiz[es]", "discard[s]" (D1);
    - §2.2 "compet[ing]", twice (D2);
    - §7.1 "[narrative-value frames]" (D22);
    - §10.5 "[centralization or decentralization]" (D29).

    These are raw: §6.6 "ai accelerate it"; §7.1 "it out grows" and "will also becoming"; §7.3 "we can not lose but keeps on going". One convention should hold. Raw quotation, with any gloss outside the quotation marks, keeps his voice and matches the majority.
  - Edits 28 and 29 make the order of English and Chinese, and the shape of the tag, uniform.
- **Item 5, "favoured" or "to continue".** Edit 5 recommends "to continue" everywhere. Whichever he chooses, all five places should carry it.
- **Plan placement of item 8 in tier 1(b).** Edit 1 keeps the placement. Moving the item to tier 1(a) is the alternative.
- **D34.** §0 and §12.4 both print the unconfirmed paraphrase "We are not only our separate lives …". §12.4 follows it with his own spoken sentence, which is the stronger close. If he does not confirm the paraphrase, §12.4 can keep only his sentence.

## F. Left as they are, and why

- **Box lengths.** The boxes run 189–304 words against the plan's guide of 90–140. The lever is a uniform pass over all the boxes (elegance-build-notes §6 item 9). After edits 8 and 18, no box claims more than its section shows, or tags it differently.
- **"Growing understanding without executive authority may change nothing"** has its home in §4.3, with pointers in §1.4 and §12.2. That is acceptable.
- **"Each actor computes correctly; the game is wrong"** appears in the chain's homes (the abstract, §1.2, §12.4) and in the statement's home (Remark 3.10). §0, §3.8, §6.1 and §7.1 apply it. Edit 24 removes the one place that restates it.
- **§7.2's activation paragraph and §12.1's *Commitment*.** The first draws the consequence of Corollary 5.7 and points to the second; that is not a repetition.
- **"Masked divergences are the strongest reason from inside alignment for E2 and E3"** appears in §5.3, as a forward pointer, and in §6.4, its home. That is acceptable.
- **The status line and §1.4's *Review status* overlap.** The second adds what to check first, so both can stay.
