# Review of the applied integration (Fable, 2026-10-04)

Scope: the uncommitted diff in `theories/`, `GLOSSARY.md`, `MAP.md`, `OPEN-QUESTIONS.md`, `TIMELINE.md`, `sources/SOURCES.md`, plus the new source README sections, the request record, the drafts README and `MERGE.md`. Read against `translation-zh.md`, `translation-notes.md`, both recognition passes, and the cited targets. Quotation substrings and the existence of claim/proposition numbers were not redone.

## Findings, ranked

### Must-fix

**1. A phrase attributed to claim 12 is not in claim 12, and is AI-composed 古文.**
`theories/relational-self-and-datong/README.md`, argument *2026-10-04 … A way of deciding*, last sentence: "That is claim 12's 今日所行，向之乎？背之乎？ asked as a question about leverage."
Claim 12 reads "whether today's act moves toward or away" and marks its source "the 古文 essay AI-composed to his one-line prompt". The 古文 phrase exists only in that essay (`sources/12-claude-ai-chats/2026-05-01_大同作为方向的古文解读_2a814005.md`) and nowhere else in the corpus. As written it presents AI-composed 古文 as the claim's words.
Replace with: "That is claim 12's question, whether today's act moves toward or away (the 古文 essay's 今日所行，向之乎？背之乎？, AI-composed to his prompt), asked as a question about leverage."

**2. The alignment section says the headline claim had no form in Ren's words; claim 81 is his, verbatim, 2026-06-03.**
`theories/alignment-selection-on-cognition/README.md`, *Alignment at three scales*: "Until now its field-vocabulary form rested on AI drafting and on what the 2026-10-02 conversation implied; future texts can cite this, with the translation caveat."
Claim 81 is Ren verbatim: "Even if we have perfect inner alignment, if the outer alignment is not solved, as the competition we have been living in now, the further we go, the worse it gets." The new sentence contradicts the file it is in.
Replace with: "Ren stated it in writing on 2026-06-03 (claim 81, in his own sense of 'inner alignment'). This is its second statement in his voice, the first spoken and the first with 对齐; future texts can cite both, this one with the translation caveat." Also claim 216's tag: "[mechanism; the headline claim in Ren's voice, beside claim 81]".

**3. The 39:22 sentence is summarised without its condition, which overstates the tension with the believer rule.**
Both recognition passes: "当这些东西它被塑造出来的时候它内在的那种价值观就其实在把大家在把这个民族作为一个整体它再往这样的方向上带然后这样的东西才是最后／最有 legitimacy 和历史高度的东西". 这样的东西 is shaping *of this kind*: expression whose inner values carry the people as a whole in this direction (the 大同 / 向善 direction just named). Legitimacy is claimed for whole-directed shaping, not for narrative-shaping as such. Claim 59 keeps the condition ("carries values that lead a people as a whole, and has the most legitimacy"). Every summary drops it:
- `selfishness-spiral…/README.md`, *The strain*: "grants direction-setting itself the most legitimacy"; open question *Loop 3, approved when the direction is approved*: "grants direction-setting narrative the most legitimacy".
- `OPEN-QUESTIONS.md` §2 *Reading state narrative*, Side B: "the shaping of a society's expectations and language, which the West calls propaganda, 「这类东西才最具有正当性…」"; §4.6: "calls the shaping of expectations 'which the West calls propaganda' the most legitimate kind of direction-setting".
- `MAP.md` 2026-10-04 paragraph: "says that the shaping of a society's expectations and language, which the West calls propaganda, has 「最具有正当性…」".
- `TIMELINE.md`: "the reading of a society's narrative-shaping as what has the most legitimacy".
- `relational-self…/README.md` own words 74 note: "Said of the shaping of a society's expectations, language and political expression".
- `MERGE.md` *Where they agreed*: "the reading of state narrative-shaping as the most legitimate kind".
Replace each with the conditioned form, e.g.: "the shaping of a society's expectations, language and political expression (which the West calls propaganda), when its inner values carry the people as a whole in this direction, has 「最具有正当性（legitimacy）和历史高度」 [39:22]". Then add one sentence where the tension is argued (`OPEN-QUESTIONS.md` §2 *Where the evidence lands*; `relational-self` *The state's narratives*): "On this reading Ren locates the legitimacy in the direction of the values, so the first test (direction judged by the corpus's own definitions) is the one that engages, and the believer rule still applies to the further claim that the direction is what its sponsor intends." `MERGE.md` *Decisions for Ren* 3 should offer him the two readings of 这样的东西 instead of one.

### Should-fix

**4. "Ren's answer to item 46" overreaches; he spoke of polities, not of the copies.**
`theories/meta-attractor/README.md` open question 49: "Ren's answer to item 46 is a rank objective (claim 302)"; argument *Why the copies fight*: "The talk answers in Ren's voice."
Replace with: "The talk's mechanism for polities (claim 302), carried to item 46 by the assistant, is a rank objective" and "The talk supplies, for polities, the mechanism item 46 asked for." (The paragraph's later sentence "The talk states the mechanism for polities, not for machines" already says so; the opening should agree with it.)

**5. Assistant inferences sit unmarked inside claims attributed to Ren.**
- `meta-attractor` claim 301: "while its own rules are not" — 37:15 says nothing about the actors' own rules; the asymmetry is the assistant's (it is argued as such in the paragraph). Tag: "[mechanism; the own-rules asymmetry is the assistant's]".
- `meta-attractor` claim 303: "Neither has a winner." — inference; mark it.
- `keep-the-possibility-space-open` claim 225 states the same content as `alignment` claim 222 but without 222's "the reading as a condition is the assistant's". Copy the mark.
- `zhishan` claim 291: "Symmetry is therefore a condition of being believed." — the formulation is the assistant's (the argument says "The talk gives a second, strategic reason" and then builds the three steps). Tag it.
- `selfishness-spiral` claim 165, second clause ("'makes sense' is where the frame's output passes for the world's"); claim 167, second clause; claim 168, second sentence ("The legitimating vocabulary is a ledger…") — all [R]-tagged; mark the clauses "(the assistant's)" or move them to the argument.
- `drives` claim 90: "tempo sets the weight of selection over formation" — the composition rule is the assistant's; the tag says only "the rate is a conjecture".
- `alignment` claim 218: "reduced by claims 215–216 to the first requirement" → "reduced, on the assistant's reading, by claims 215–216".

**6. TIMELINE asserts solitude the source README says is unknown.**
`TIMELINE.md`: "Ren recorded fifty-one minutes alone". The README: "any listener is unknown". Replace "alone" with "in one voice".

**7. A date in the 大同 glossary note is wrong.**
`GLOSSARY.md` 大同, *2026-10-04*: "the official goals set after 2021 are named for 2035 and 2049". The two-stage goals were set at the 19th Party Congress (October 2017) and reaffirmed in 2022; 2021 is when 小康 was declared complete. Replace with: "the official goals that follow 小康 (set in 2017 for 2035 and 2049, reaffirmed in 2022) are stages of modernisation, not 大同". The parallel sentence in `relational-self` *The state's narrative, judged by one standard* ("After 2021 the official goals are named as…") is accurate as written.

**8. Asymmetric scrutiny in §5: the recording's empirical claims about the West get no row.**
`OPEN-QUESTIONS.md` §5 adds rows for [08:33] (Chinese engineering skill), [23:41] (five-year plans), [34:03], [36:08], but none for the recording's claims about the West, which are also observations without sources: [21:00] fear and hostility toward power "非常普遍" in the present West; [31:36] Western companies as cancer-like growth-seeking; [46:38] Western safety-minded friends cannot leave the frame. The text states that the asymmetric-scrutiny rule "cuts both ways" but applies the evidence demand to one side. Add a row: "The present West shows habitual fear and hostility toward power, cancer-like corporate growth-seeking, and a safety community that cannot leave the struggle frame (added 2026-10-04) | recording [21:00; 31:36; 46:38] | His observation, unsourced, tiered as the rows above; attitude surveys and growth-strategy documents compared across polities, and the §1.2 three-group survey for the third".

**9. Dropped from both plans without a reason in MERGE.md.**
- [34:41] Ren's own hedge on the Confucian categories: 「我觉得，在范畴的划分上，儒家可能相对最好…但这一点，我也不是很确定」. PLAN-fable §5(a) names it as one of the talk's two hedges on the Chinese side and says the theory should not inherit the imbalance. Add to `relational-self` claim 54 or 56 and to the argument's *The label, and the logic under it*: "He hedges the ranking himself [34:41]."
- [43:30] 「把“不断变大”奉为信条的邪教式思维」. Ren's 2026-04-11 line that anchors `OPEN-QUESTIONS.md` §1.2 is "大家原教旨式的遵循着他们的邪教". Same word, in his voice, now attached to the growth creed (PLAN-fable row 58). One sentence in §1.2 or in GLOSSARY *political realism / accelerationism*; the uncertain verb at 43:49 need not be quoted.
- PLAN-opus summary, tension 3: the talk's own 护城墙 [35:15] is the 护城河 the corpus records as Chinese business vocabulary (`drives` claim 62; `zhishan` claim 116), evidence that the frame runs on both sides. One clause in `meta-attractor` *The two endgames* or `relational-self` *What is generic, and what is his*.
- [28:30] 「也许可以叫文化，或者心智结构（mental constructs）；我们并没有很好的词来表达它」 — the vocabulary gap the drives section is about; optional.

**10. 51:08 is linked to 逍遥, which the talk does not do.**
`theories/shengsheng-buxi-generative-existence/README.md` 2026-10-04 paragraph: "The talk agrees with 第十九章 that 逍遥 is not withdrawal: 「不能直接退出、不管了」 [51:08]." `GLOSSARY.md` 逍遥 *Drift*: "Both agree that 逍遥 is not exit from the world: 「不能直接退出、不管了」 [51:08]." At 51:08 Ren speaks of peace and love and structural problems; 逍遥 is not mentioned (it occurs only at 05:26). Replace with: "The talk also refuses withdrawal, 「不能直接退出、不管了」 [51:08], without connecting it to 逍遥; in effect it agrees with 第十九章."

**11. Two files disagree on whether 止戈 is stated as a bound.**
`keep-the-possibility-space-open` *The participant's dilemma*: "the talk names the bound of that knowledge in the next breath, 武 read as 止戈 [22:14]". `relational-self` critique *Two tracks of the tradition*: "The talk supplies the bounds of the second track itself … but does not state them as bounds." The second is right (22:14 is offered as 「从另一个方向看」). Replace the keep-open clause with: "and in the next breath the talk offers the other direction, 武 read as 止戈 [22:14], which this theory reads as the bound of that knowledge".

**12. A state is named inside an argument body.**
`theories/zhishan-intelligence-must-be-good/README.md`, *The slogans read as direction*: 「至少看看中国立场上的文件，说的是什么？“AI 向善”“AI 普惠”。…」. Own words 93 already carries "Said of the documents on China's side". Trim the argument's quotation to begin at 「“AI 向善”“AI 普惠”。就是：发展 AI，不能断了子孙后代的路，要追求人类命运共同体」 and introduce it as "the position documents of one state (own words 93)". The keep-open quotation of 「西方的秩序」 [21:32] names a civilisation, not a state, and is framed as the trap from inside; leave it.

**13. The assistant proposes permitted means of winning.**
`OPEN-QUESTIONS.md` §2 *Winning, or opposing the logic of winning*, last sentence: "the assistant's proposal is not with AI, and not by closing others' futures"; `MERGE.md` *Decisions for Ren* 2: "The proposal is: not with AI, and not by closing others' futures." Under Ren's rule that a remedy opposes the logic rather than adapting to it, defining acceptable winning is an adaptation. Replace with: "If he means more than 护闭, he should say what. The corpus's own bounds are the pragmatic minimum (no AI as a party) and the custody rules, and they bound defence; they are not a licence to win."

**14. An inference is given as Ren's reasoning.**
`GLOSSARY.md` *Moloch*, *2026-10-04*: "A diagnosis that keeps struggle as the ground of reality can only prescribe a stronger party. That is why his own term names a selection that can be changed, **molochlization**…". At 46:38 Ren says only that Leviathan-like and Moloch-like are both a struggle frame. Prefix "On the assistant's reading," and change "That is why" to "That is a reason". Same in `meta-attractor` *The guardian test, turned on frames*: "That is the better guardian in theoretical form" → "On the assistant's reading, that is the better guardian in theoretical form."

### Optional

**15.** 权力迭代 [36:08] is glossed "where power iterates faster" in the arguments but "the faster power changes hands" in `meta-attractor` claim 297, `alignment` claim 221 and the §5 row, and "turnover" in meta open question 47. 迭代 is "iterates"; "changes hands" is one operationalisation. Use "iterates (迭代)" in the claims and keep turnover as the assistant's measure in open question 47.

**16.** `alignment` heading "A conditional that its own terms close" → "A conditional closed, on the assistant's reading, by its own terms". The closure is an argument the assistant makes from 37:35, 44:44 and 45:06; the heading says the talk makes it.

**17.** `MAP.md`: "He adds a third reason, mutual understanding: 「如果可以从这个视角尝试理解中国…」 [41:03]". The section's two reasons are reasons for grounding the work in pre-Qin thought; 41:03 is an aim of contact. Write "He adds an aim: that others try to understand China from this angle and align mutually".

**18.** "Automatic diarization found one voice throughout" (nine files) states more than the README does ("one speaker label per chunk; labels local to each chunk; consistent with one voice but does not prove it"). Tighten to "assigned one speaker label in every chunk".

**19.** `selfishness-spiral` *The lock, by population* and `OPEN-QUESTIONS.md` §1.2 settle the 36:02 referent as "the caring logic" and then note it is unsettled. Say "the caring logic (the assistant's reading of the referent, supported by the 但不幸的是 that follows; the translation leaves it open)".

**20.** At 02:57 the word is 理性; the files say 理 regulates 心. Ren set 理 against 心 at 00:39, so the identification is his, but one clause ("理, the 理性 of 02:57") would be exact. `drives` *The regulator, named*; `relational-self` claim 52.

**21.** The MERGE table says shengsheng got "three claims, two own-words entries and one open question" and the-fork no edit; both match. The README's "Where it went" matches every claim, own-words and open-question range; no correction needed there.

## Checked and found correct

- **Section letters and numbering.** No collisions: meta P follows O; alignment L follows K; selfishness P follows O; keep-open N follows M; drives M follows L; zhishan Q follows P; shengsheng Q follows P. Every new claim, own-words and open-question range starts one after the file's last existing number, and the source README's "Where it went" lists them correctly. OPEN-QUESTIONS §1.7 and §4.6 are the items named.
- **Nothing deleted.** All 20 removed diff lines reappear as prefixes of extended lines (the cosmic-cancer header had 宇宙癌症 inserted mid-line). MERGE's "eight existing lines extended" count is right.
- **Recognition passes.** 余量 at 40:22, 赢的逻辑 at 49:24, "aligns with the reality" (05:26), "into that alignment" (06:15), "positive feedback loop that runs away" (02:57), "alignment" (37:35) and "moloch式" (46:38) are in both passes. "training ground" (44:20) and "drop out" (51:08) are in the independent pass only; the first pass has "training round". At 13:40 the first pass has 实态, the second 实体, so the translation's flag stands. 39:22 has "legitimacy" in English in both passes.
- **Flags.** 36:02, 34:29, 13:40 and 24:05 are flagged wherever used; 01:44, 09:38 and 43:49 are not quoted.
- **Cross-references read and confirmed.** meta-attractor claims 141, 283, 288, 292; open questions 31 (η, g′f′, ẇ = λCw), 35 (boundary paragraph), 46; the slack coefficient SC as a gating criterion; claims F (conceptual colonisation, "alternatives lose language") and N (guardian test). relational-self claims 5, 18, 19, 24, 25, 26 (人+二), 30, 34, 35, 41, 47; own words 11 (外儒内法, 高度的实用主义). alignment claims 43 (the "oldest function of reason" line), 55, 81, 210; own words 41–42, 45; sections *How the capture reaches the machine* and *When capability outruns correction*. selfishness-spiral claims 41 (game-design axiom), 78 ("only in theory"), 95 (five endgames), 121, 142, 143, 145, 148, 161; own words 52; the loop 3 ladder (acceptable → right → what we are); the 2026 self-critique at the re-basing. keep-open claim 18, 极皆成闭, "assurance without surveillance" as a listed frontier problem, *What was lost along the way*, custody rules. drives claims 24, 41, 49, 53; own words 60 (心与理也可建立环); open questions 8, 13, 14; "channel, do not deny". zhishan claims 116, 124, 234, 284; found-by-reading 4 and 8; the reviewer's warning about 朱熹 cited alongside 心学 (the fault line). shengsheng claims 257, 277, 296 (with 自在), 329, 333, 343. jian claim 307, own words 81.
- **The v6.1 paper.** Title; Proposition 2.3 (k_0), 3.6 with parts (1)–(3) as described, 8.10 (ϖ and the threshold), 11.2; §3.8 Ψ, §4.3, §11.1; thesis 9 "Trust is an outcome of a staged transition" and "trust is mainly an outcome"; "defensive realism with one more variable" in DISCUSSION X (International relations); the fidelity review's replacement wording; X1's "Legalist programme" among doctrines of national survival.
- **The 2026-10-03 direction file.** "这个理论应当可以推导出，不能" answers the AI-assisted-oversight question; the linear-or-slower and learning/consensus/mechanism lines; trust's two parts (消息可信并可守承诺); the cancer ruling; the pasted sketch's p* threshold, "验证放大信任，但不产生信任", author unstated.
- **Other sources.** Community document v0.3: §二 韩非 and 秦, §三 "武的本义，是止息兵戈", §十一 致西方的朋友; NOTES "没有一句是你的原话" and the 天下为公/己所不欲 rows; Ren's 2026-09-26 request to avoid 善不姓国. 10-02 transcript: five-year-plan systems thinking at 01:24:48, trust at 00:22:31. The 10-02 recording's label "Soi Sathon 11 Yaek 9" is the same kind of label. OCASC review's GRIT ladder.
- **GLOSSARY.** [borrowed] is an existing tag; 化/理, 天理/邪理, 中/极, 良知, 护闭, 伪开 entries exist; 仁义礼智信 has 信 as "the temporal ground".
- **Facts.** 止戈为武 is 《左传·宣公十二年》, 楚庄王; the 止-as-foot paleography is the standard reading. 心理学 as a translation term (Japanese coinage, 1875) is right and is marked "check". 程朱 性即理 against 陆王 心即理 is right in outline. The dark-triad summary (small emergence effects, often negative effectiveness, poorly sourced prevalence) is fair; the 12% figure is in the selfishness-spiral critiques and §4.1, and the alignment text correctly says "the corpus has carried" it.
- **Rules.** Argument bodies state the dynamic generically; named persons appear only in own words 73 and the source note; "西方" quotations are confined to own words or framed as the trap from inside (except finding 12). No remedy adapts to the logic except as noted in finding 13. Mechanism precedes conclusion in every new section; the prose is essay prose.
