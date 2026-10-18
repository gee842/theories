# Review of the applied Soi Si Lom 5 2 integration (Opus, 2026-10-04)

Scope: the uncommitted edits to the nine theory READMEs, `GLOSSARY.md`, `MAP.md`, `OPEN-QUESTIONS.md`, `TIMELINE.md`, `sources/SOURCES.md`, the source README's added sections, the request record, and `MERGE.md`. Read against `translation-zh.md`, `translation-notes.md`, both recognition passes (`chunk-*.json`, `checks/NN.json`), the 10-02 transcript, the 10-03 direction file, v6.1 `THEORY.md`/`DISCUSSION.md`/fidelity review, and the community document v0.3 and its NOTES. Written without reading `REVIEW-fable.md`.

Every replacement quotation proposed below was checked as an exact substring of its timestamped paragraph in `translation-zh.md`.

## Findings, ranked

### 1. must-fix: "宇宙癌症" was not spoken; Ren said "cosmic cancer" in English
Both recognition passes, at both places, have the English: `chunk-07`/`checks/07` 「创造一个cosmic cancer或者之类的东西」 [38:15]; `chunk-08`/`checks/08`/`passage-cancer_care` 「我们造了一个cosmic cancer」 [43:30]. 宇宙癌症 is the translator's rendering. Three places record it as a spoken Chinese term:
- `GLOSSARY.md`, cosmic cancer header: "天癌 (文言 rendering) / 宇宙癌症 (spoken, 2026-10-04)". Replace the parenthesis with: "宇宙癌症 (the 2026-10-04 translation's rendering; the English "cosmic cancer" was spoken, in both recognition passes)".
- `theories/meta-attractor/README.md`, *Cosmic cancer, and the root, in his voice*: "This is the image, with the Chinese 宇宙癌症 and the English term, in a recording with one voice that Ren supplied as his own." Replace with: "This is the image, spoken in English as "cosmic cancer" at [38:15] and again at [43:30] (both recognition passes; 宇宙癌症 is the translation's rendering), in a recording with one voice that Ren supplied as his own."
- Same file, open question 44 extension: "The image, the Chinese 宇宙癌症 and its conditional are now in a recording…". Replace with: "The image, spoken in English as "cosmic cancer" ([38:15]; [43:30]; 宇宙癌症 is the translation's rendering), and its conditional ([43:54]) are now in a recording…".
- Optional, claim 306: "risks a "宇宙癌症"" → "risks a "cosmic cancer" (宇宙癌症 in the translation)".

### 2. must-fix: [38:55] "the direction is right" rests on a word the translator added
Both passes have 「我不能说它有多么好，但是它至少不疯狂，并且它是正确的」 (`chunk-07`, `checks/07`): "and it is right". The translation's 「而且这个方向是正确的」 adds 这个方向, and `translation-notes.md` does not flag it. The integration builds its reading of the slogans as a *direction* on that added word, and so presents Ren's endorsement of one state's documents as weaker than he said it.
- `theories/zhishan-intelligence-must-be-good/README.md`, claim 292: "are "at least not mad", and their direction is right; no claim is made about how good they are." → "are "at least not mad" and are right (both recognition passes: 它是正确的; the translation's 这个方向 is an addition); no claim is made about how good they are."
- Same file, argument, after "Then the hedge: 「…」 [38:55] (… and the direction is right).", add: "Both recognition passes have 「并且它是正确的」 (and it is right); "direction" is the translator's word, so reading the slogans as a direction is the theory's standard, not his wording."
- Add the same one-clause flag at own words 93 (zhishan), at the [38:55] quotation in `relational-self-and-datong` (*The state's narratives…*, "By that standard the talk's own hedge is the right register"), and in `GLOSSARY.md` 人类命运共同体.
- Add a row to `translation-notes.md` (38:55, 这个方向 not in either pass) and a line to the source README's *What still needs listening*.

### 3. must-fix: named states inside theory argument bodies, against the 2026-10-03 rule
Ren: "不要点名中美，无论是什么国家和什么国家…只要这种dynamics在，都一样". `MERGE.md` says "The argument bodies state the mechanism generically", and `meta-attractor` does (attributions only in own words). Five other argument bodies quote the attributions directly. Replacements (all exact substrings):
- `keep-the-possibility-space-open`, *The participant's dilemma*: 「当下我们处在一个西方的秩序里面，而这个秩序本身就在斗争，落后就要挨打」 [21:32] (we are now inside a Western order, …) → "an order that is itself at struggle, 「这个秩序本身就在斗争，落后就要挨打」 [21:32] (where falling behind means being beaten)". Own words 77 already keeps the full sentence.
- Same file, *A second ground*: the [24:19] quotation → 「当关系发生变化的时候，变的并不只是某一件事情，而是围绕这些关系的整套现实因果，都在发生变化」 [24:19] (…), so that in the tradition's thought 「加速主义其实也讲不通，它是不合理的」 [24:19] (accelerationism does not make sense; it is unreasonable).
- `zhishan-intelligence-must-be-good`, *The slogans read as direction*: 「至少看看中国立场上的文件，说的是什么？“AI 向善”“AI 普惠”。…」 → "The talk points to one state's position documents: 「“AI 向善”“AI 普惠”。就是：发展 AI，不能断了子孙后代的路，要追求人类命运共同体」 [38:55] (…)". *The oneness argument, addressed*: drop 「西方的朋友们」 (Western friends) from the body; see finding 12.
- `selfishness-spiral-and-narrative-value-frames`, *The lock, by population*: 「尤其是，我觉得西方的朋友们其实都很关心这件事…」 → "of those on the other side who care: 「其实都很关心这件事，都想找一个出路，却没有办法跳出那种框架」 [46:38]". *Frames are read across the boundary*: replace the [48:33] quotation with "the other side reads it as colonial, hegemonic logic and concludes 「那怎么合作？显然就得跟你对抗」 [48:33]". *The strain*: cut the [39:22] quotation to 「当这些东西被塑造出来时，它们内在的价值观，其实是在把大家、把这个民族作为一个整体，带往这样的方向。这类东西才最具有正当性（legitimacy）和历史高度」, introduced as "of the shaping of a society's expectations, language and political expression".
- `alignment-selection-on-cognition`, *Alignment at three scales*: replace the [45:06] quotation with 「即使它们是与你完美对齐的结果，完全遵循你的意志」 … 「结果就会好吗？这件事太说不通了」 [45:06] (even if they were perfectly aligned to you … would the result be good, in the present state of struggle? That makes no sense at all), and delete "The talk's "西方" names the present carrier of the state of struggle; the claim is about any principal formed by it." (own words 61 keeps it).
- `relational-self-and-datong`, *The label, and the logic under it*: replace the [19:49] quotation with "the relational way of thinking is labelled from outside 「“集体主义”（collectivism）」, 「但这并不代表他们理解它的内在逻辑」, and 「这样的标签化，也是一种过度简化」 [19:49]".

### 4. must-fix: the flagged referent at [36:02] is decided as "the caring logic"
`translation-notes.md` says the referent of 这套逻辑 is not to be decided. Two places decide it, then say it is unsettled:
- `selfishness-spiral…`, *The lock, by population*: "Most people would probably endorse the caring logic:" → "Most people would probably endorse 「这套逻辑」 ("this logic"), whose referent the translation leaves open:".
- `OPEN-QUESTIONS.md` §1.2, 2026-10-04: "Most people would probably endorse the caring logic," → same replacement.

### 5. must-fix: the assistant's readings stated as what the talk or Ren says
Each must be marked as the assistant's.
- `relational-self-and-datong`, *The state's narratives*: "The talk names the mechanism itself at [18:05]: the vocabulary in which power has to justify itself lets its conduct be held to account in those terms." [18:05] says only that justification of government returns to the older logic. → "The talk observes at [18:05] that power still justifies itself in the older vocabulary. Read as a mechanism (the assistant's reading), that vocabulary lets its conduct be held to account in its own terms."
- `selfishness-spiral…` claims, where the file's legend says **[R]** marks Ren's own words. Claim 165: move "; "makes sense" is where the frame's output passes for the world's" into a trailing "(the reading of "makes sense" is the assistant's)". Claim 167: same for "a frame that has become common sense no longer has to answer…". Claim 168: same for "The legitimating vocabulary is a ledger that can constrain conduct or be emptied into cover."
- Formation then selection, "weighted by tempo" (an Opus-only composition per `MERGE.md`; the talk sets [34:03] and [36:08] near each other with [35:15]–[36:02] between them and states no order):
  - `drives…` argument: "The talk puts them in order. Construction comes first: … Selection comes after: … A composition rule follows from the order." → "The talk speaks of both within two minutes. Construction: … Selection: … Read as a sequence, which is the assistant's composition and not the talk's statement, they give a rule."
  - `drives…` claim 89: drop "Formation comes first and selection after:"; tag "(reading the two as a sequence is the assistant's)". Claim 90: add "; "tempo sets the weight" is the assistant's composition".
  - `drives…` Relations: "On 2026-10-04 Ren put construction and selection in sequence: formation by education, then selection by power, weighted by tempo" → "On 2026-10-04 Ren spoke of formation by education [34:03] and selection by power [36:08] in adjacent passages; the sequence weighted by tempo is the assistant's composition".
  - `drives…` open question 19: "The talk gives the order (formation [34:03], then selection [36:08]) and a weight (tempo [36:08])." → "The talk gives the two (formation [34:03], selection [36:08]) and a rate claim [36:08]; the order and the weighting are the assistant's."
  - `alignment…` argument: "The talk says where that cognition comes from, in two stages." → "Read with the talk's passages on education and on reward (the two-stage reading is the assistant's), that cognition comes from two places." Open question *Construction against selection*: "The sequence in claim 221 and its companion in drives (…) is Ren's order, not yet a model." → "Claim 221 here (selection only) and claims 89–90 in `drives…` compose Ren's two observations into an order; the composition is the assistant's and is not yet a model."
  - `OPEN-QUESTIONS.md` §1.7: "The recording puts formation and selection in order" → "The recording speaks of formation and of selection in adjacent passages, and the assistant reads them as an order".
- The lock by population (Opus-only per `MERGE.md`): `selfishness…` "The talk sorts three populations." → "Read by population, which is the assistant's sorting, the talk's statements fall into three groups." `OPEN-QUESTIONS.md` §1.2 "The recording sorts the lock by population" → "Read by population (the assistant's sorting), the recording's statements sort the lock"; and "Their frame keeps struggle as the ground, so their remedies are stronger parties." → prefix "On the assistant's reading,".
- `meta-attractor` *Why the copies fight*: "The talk answers in Ren's voice." → "The talk bears on it (the mapping is the assistant's)." Open question 49: "Ren's answer to item 46 is a rank objective (claim 302)" → "Read as an answer to item 46 (the assistant's reading), the talk's kernel is a rank objective (claim 302)".
- `zhishan…` *The oneness argument*: "Both are Hobbes, the war of all against all and the sovereign that ends it, and the talk's point is that they are one frame" → "Both are Hobbes, the war of all against all and the sovereign that ends it. The talk calls either name a frame of struggle; that problem and cure form one frame is the assistant's reading".
- `GLOSSARY.md` Moloch: "That is why his own term names a selection that can be changed, **molochlization**, and not a god…" (he coined it on 10-02, before the talk) → "On the assistant's reading, this is also why his own term, **molochlization**, names a selection that can be changed and not a god…".
- `alignment…` *A conditional that its own terms close*: "The talk's own sentences close the door." → "Read with the talk's other sentences, the door closes (the reading is the assistant's)." Claim 218 tag: add "the reduction is the assistant's". Open question *The third road, again*: "The talk's own [37:35], [44:44] and [45:06] say so;" → "On the assistant's reading, the talk's own [37:35], [44:44] and [45:06] imply it;".
- `OPEN-QUESTIONS.md` §1.1: "the talk's claim is that the prior each side sets by reading the other is now the binding variable." → "the assistant reads the talk as making the prior each side sets by reading the other the binding variable."

### 6. must-fix: the end-of-talk refusal to drop out is attached to 逍遥
[51:08] is about the structural problems, 46 minutes after [05:26]; the talk never says 逍遥 is not withdrawal.
- `shengsheng-buxi…` argument: "The talk agrees with 第十九章 that 逍遥 is not withdrawal: 「不能直接退出、不管了」 [51:08] (…)." → "The talk's last minute refuses dropping out of the structural problems, 「不能直接退出、不管了」 [51:08]; it does not speak of 逍遥 there, but the refusal is consistent with 第十九章's reading that 逍遥 is not withdrawal (the link is the assistant's)."
- `GLOSSARY.md` 逍遥 *Drift*: "Both agree that 逍遥 is not exit from the world: 「不能直接退出、不管了」 [51:08] (…)." → "第十九章 says 逍遥 is not withdrawal. The recording's refusal to drop out [51:08] is said of the structural problems, not of 逍遥, and is consistent with it (the link is the assistant's)."

### 7. must-fix: a remedy that adapts to the logic of winning, offered as the assistant's proposal
`OPEN-QUESTIONS.md` §2 *Winning, or opposing*: "If he means that a party inside the game may win by some means until a joint exit exists, he should say which means are excluded; the assistant's proposal is not with AI, and not by closing others' futures." A list of permitted ways to win is an adaptation, which the 10-03 ruling rules out, and it contradicts the same paragraph's (and keep-open claim 223's) distinction between 护闭 and winning. Replace with: "If he means more than the description, the corpus's answer is not a list of permitted ways to win but 护闭: the capacity not to be beaten, bounded, reopening, under the custody rules, never aimed at decisive advantage, with AI kept out of the struggle (the 2026-10-03 order). Whether he accepts that line is his to say." Make the same change to `MERGE.md` decision 2 before it goes to Ren.
Two related edits:
- Same paragraph: "Side A also gets something right that Side B's texts understate: because the advantage is real while slack lasts," → "…understate: if the advantage is real while slack lasts (`meta-attractor` claim 299, a conjecture),". As written it grants the race's premise as fact.
- `keep-the-possibility-space-open`, open question *Win, or oppose the logic*: "the abundance floor, so that falling behind does not mean destitution;" → "the abundance floor as provision beneath the game (not as insurance against losing, which the 10-03 ruling rejected);".

### 8. must-fix: the author's testimony counted as strong evidence for his theory
`OPEN-QUESTIONS.md` §2 *Winning, or opposing*: "…an actor with a wider objective who still races because it reads the order as struggle, and among the best evidence the theory has, because it comes from the theory's author." Testimony from the theory's author is the least independent evidence there is. Fable's plan makes the same point: a monologue's value as evidence of his position is high and its value as a test is low. Replace with: "…because it reads the order as struggle. Coming from the theory's author, it shows his position; it is not independent evidence for the mechanism."

### 9. should-fix: 小康 → 大同 is folded into "official formulas", and its lineage is missing
The integration's own critique says 小康 → 大同 is not the official sequence, yet three places list it as an official formula:
- `relational…` argument: "The talk places present official formulas in the 大同 line: 人类命运共同体, AI 向善, and the sequence 「先走到“小康”…」 [19:03]" → "The talk places present official formulas, 人类命运共同体 and AI 向善, in the 大同 line [17:27], and reads policy as running 「先走到“小康”，而小康的下一步其实就是“大同”」 [19:03]".
- Claim 58: "(人类命运共同体, AI 向善, 小康 and then 大同)" → "(人类命运共同体, AI 向善) continue the 大同 kernel, and policy runs from 小康 to 大同,".
- `MAP.md`: "(人类命运共同体, AI 向善, and the sequence from 小康 to 大同)" → "(人类命运共同体, AI 向善), and reads policy as running from 小康 to 大同".
Factual addition to the relational critique ("…not the official sequence.") and to `GLOSSARY.md` 大同 ("…not as 大同."): "The forward order is 康有为's (三世说: 升平 as 小康, 太平 as 大同), and the talk names 康有为 at [17:27]; in 《礼运》 itself 小康 is the lesser order after 大道既隐. Both recognition passes have 「(他/它)说 OK 先走到小康」 at [19:03], so the talk presents the sequence as what the policy says; the translation drops that attribution."

### 10. should-fix: inferential clauses without a mark in claims
- `meta-attractor` claim 301: add "(that its own rules are not violence inside the frame, and that correction loses its standing, are the assistant's)". Claim 303: delete "Neither has a winner." (see 14). Claim 304: "cannot yield a way out" overstates 「很难想出出路」 (passes: 想不太出路) → "makes a way out hard to find".
- `zhishan…` claim 291: "Symmetry is therefore a condition of being believed." → add "(the conclusion is the assistant's)".
- `keep-the-possibility-space-open` claim 225 is word for word alignment claim 222 but lacks its tag: add "the reading as a condition is the assistant's". Claim 224: "a reading of 40:22 with 35:15" → "the assistant's reading of 40:22 with 35:15".
- `drives…` claim 85: "This names the regulator of "channel, do not deny"." → "(the link to "channel, do not deny" is the assistant's)". Claim 91: "a reading of" → "the assistant's reading of".
- `selfishness…` claim 172: "read as attempts to win by other means" mistranslates 「仍然是想用这种方式去赢」 → "read as still aiming to win this way".

### 11. should-fix: cross-references that point to the wrong thing
- `meta-attractor`, *Slack is what the advantage runs on*: "at full appropriability the prize is fully dissipated (Proposition 3.6(3))". In v6.1, 3.6(3) is "at $r=1$", and $r$ is decisiveness. Appropriability is $\chi$ in §4. → "at decisiveness $r=1$ the prize is fully dissipated".
- `meta-attractor`, *The frame calls correction violence*: "It differs from conceptual capture (claims F)". Claims F are *Minds, organisations, and the closing of the loop*; conceptual capture is claim 129 (G) and the section *Conceptual capture, and why a new handle was needed*. → "(claim 129; *Conceptual capture, and why a new handle was needed*)".
- `keep-the-possibility-space-open`, *Trust before verification*: "This section names … "assurance without surveillance" as an unsolved frontier problem." That phrase is in the open questions (*Assurance without surveillance*, raised inside the corpus), not the argument. → "This section names assurance as the mechanism, and the open questions list "assurance without surveillance" as an unsolved frontier problem."

### 12. should-fix: [46:38] "turns to" Western friends, but it speaks of them in the third person
The source README says so correctly ("speaks of "西方的朋友们" in the third person"). Second-person 你们 begins at [49:09].
- `zhishan…` provenance: "though at [46:38] the talk turns to "西方的朋友们"" → "though at [46:38] it speaks of "西方的朋友们" and from [48:33] addresses a "你们"".
- `zhishan…` *The oneness argument, addressed*: the argument at [42:20] comes before [46:38] and is said of "大家", so "It gives them the argument …" reverses the order. Restructure: "At [42:20] the talk makes the argument the community document's §十一 makes in writing: … Later it says of those on the other side who care that they 「其实都很关心这件事，都想找一个出路，却没有办法跳出那种框架」 [46:38]." And "It is the first time the document's address to Western friends is in Ren's voice." → "It is the first time §十一's oneness argument is in Ren's voice."
- `TIMELINE.md`: "though at one point the talk turns to "西方的朋友们"" → "though at one point it speaks of "西方的朋友们", and later addresses a "你们"".
- `OPEN-QUESTIONS.md` §4.6: "it addresses Western friends as fellow parts of one system [42:20]" → "it argues that everyone is part of one system [42:20]".

### 13. should-fix: contradictions between files
- Believer rule. `zhishan…`: "The hedge applies Ren's 2026-10-02 rule, "don't read them as a believer", to these documents." `OPEN-QUESTIONS.md` §4.6: "What it does not do is run the believer rule on the narrative it praises." → zhishan: "The hedge keeps a distance from the documents, but it does not ask the 2026-10-02 question, "on the meta level, what are they trying to do?"".
- 止戈 as a bound. `keep-the-possibility-space-open`: "and the talk names the bound of that knowledge in the next breath, 武 read as 止戈 [22:14]". `relational…` critique: the talk "does not state them as bounds". → keep-open: "In the next breath the talk turns to 武 read as 止戈 [22:14], which the theory can take as that knowledge's bound; the talk does not state it as one."
- Freeze endgames. `selfishness…` *The endgames* (existing) says "the two freeze states are stable but dead"; `meta-attractor` now says "Universal defensive closure is not a stable freeze". In `selfishness…` *Loop 4, and the endgames*, after "give two of this theory's five their way of ending:", add: "This revises the reading in *The endgames* that the freeze states are stable: on [35:15] the freeze slows evolution until collapse, which joins Ren's 2025 hedge that collapse follows when change outpaces coordination."

### 14. should-fix: "neither has a winner" attributed to [35:15]
The talk gives collapse in one branch and endless growth and escalation in the other. It does not say there is no winner; that is the assistant's inference, or the film's. Remove it from the attribution:
- `GLOSSARY.md` cosmic cancer: "…turns inward or outward, neither with a winner [35:15]" → "…turns inward or outward [35:15] (that neither has a winner is the assistant's inference)".
- `MAP.md`: "and with two endgames, neither of which has a winner [35:15]" → "and with two endgames [35:15]".
- `TIMELINE.md`: "and the two endgames of the cancer logic, neither with a winner;" → "and the two endgames of the cancer logic;".
- `meta-attractor` claim 303: see 10. The argument's "Neither path has a winner." is acceptable as the assistant's sentence.

### 15. should-fix: two Chinese-studies statements are imprecise
- 程朱 / 陆王. `drives…` open question 16: "心 and 理 are also the two poles of the 程朱 / 陆王 dispute: for 程朱, 性即理, pattern is given and the heart must conform to it; for 陆王, 心即理, the heart is pattern." The poles are not 心 and 理. The dispute is over where 理 is: in 性, which the 心 holds and comes to know through 格物, or in 心 itself. → "The 程朱 / 陆王 dispute turns on how 心 relates to 理: for 程朱, 性即理, pattern is the nature endowed in us, which the heart holds and must come to know through 格物, so heart and pattern are not identical; for 陆王, 心即理, the heart is pattern." In `GLOSSARY.md` 心理 *Caution*: "心 and 理 are also the two poles of the 程朱 / 陆王 dispute, 性即理 against 心即理;" → "How 心 relates to 理 is the 程朱 / 陆王 dispute, 性即理 against 心即理;".
- 仁 = 人 + 二 appears nowhere in the corpus before this edit, and the talk does not use it. Yet `jian…` open question 64 says "The talk applies the method of 止戈为武 and 仁 = 人 + 二". Delete "and 仁 = 人 + 二" there, in `drives…` open question 16, in the `GLOSSARY.md` 心理 caution, and in the `GLOSSARY.md` note on constructive glosses. Alternatively, mark it "(《说文》's 从人从二; not a corpus gloss)".

### 16. should-fix: `jian…` overstates [13:16] as "the grammar claim"
[13:16] is about what *some* (一些) pre-Qin theories describe. It becomes the grammar claim only if the flagged word at 13:40 is 时态.
- Argument: "the grammar claim returns unprompted:" → "a claim next to the grammar claim returns:", and add after the quotation: "It is about what some pre-Qin theories describe; it joins the grammar claim only if the flagged word at 13:40 is 时态."
- Claim 309: "**The grammar claim, spoken again (2026-10-04).** Pre-Qin theories describe…" → "**No I–other opposition, spoken (2026-10-04).** Some pre-Qin theories describe…", with the tag "[observation; it joins claim 307 only if the flagged word at 13:40 is 时态]".
- The talk's one sentence about *language* structure, [12:53], is unused. Add it to own words: 「我觉得，这与西方那种二元式的、我与他相对立的语言和思维结构，并不一样。」 [12:53].
- Optional: the recognisers' 实态 is a homophone of 时态 (shítài), while 实体 (shítǐ) is not. That supports the 时态 reading independently of the 10-02 sentence.

### 17. should-fix: `MAP.md` calls [41:03] "a third reason"
"He adds a third reason, mutual understanding: 「如果可以从这个视角尝试理解中国，尝试相互对齐」 [41:03]". The two reasons above it are reasons for grounding the work in pre-Qin thought. [41:03] asks the other side to understand. → "He also asks the other side to try to understand from this angle: 「…」 [41:03] (…). That is a request across the divide, not a third reason for the Chinese grounding."

### 18. should-fix: small fidelity slips in `relational-self-and-datong`
- "The five constants then arrive as the answers…". [20:18] gives four. → "Four of the five constants, 仁义礼智, then arrive as the answers… (信 follows at [30:17])".
- Status: "gave the theory's interior and its way of deciding in his voice for the first time". Ren's 2026-05-04 note already has 「心与理也可建立环，反馈」 (`drives…` own words 60; the `GLOSSARY.md` 心理 *First* says so). → add "at length", and the parenthesis "(the 心/理 loop first appears in his note of 2026-05-04, `drives-narrative-attractors-and-mind` own words 60)".
- Claim 63: "Seeking peace and love privately while the structural problems stay unsolved is not open to us; one cannot simply drop out." The talk allows peace and love "at the same time" and adds no "privately" (passes: 「你就想OK我就peace…但同时你要把这种结构性问题先解决掉，你不能直接就drop out」). → "One may say "I seek peace, I seek love", but at the same time the structural problems must be solved first; one cannot simply drop out and stop caring." Argument: "The last minute refuses the private exit:" → "The last minute refuses dropping out:".
- "It names the leaders who carried the line [17:27]" → "It names figures who carried the line [17:27]". 康有为 was not a ruler.

### 19. should-fix: recording passages dropped without a reason in `MERGE.md`
Fifteen of the 97 paragraphs are never cited. Six of them matter (quotations verified):
- [43:30] 「在这种把“不断变大”奉为信条的邪教式思维中」, in both passes (邪教思维). This is Ren's 2026-06 "cult dynamics" (`selfishness…` claim 143) in his voice. Add to `selfishness…` own words, or to `GLOSSARY.md` political realism / accelerationism, flagging only the verb that follows.
- [34:41] 「我觉得，在范畴的划分上，儒家可能相对最好，比如“仁义礼智”。但这一点，我也不是很确定。」 is one of only two hedges on the praised side. The symmetric-scrutiny argument should cite it (`relational…` own words).
- [34:58] 「首先，我是一个人，我要关心他人，关心周围的关系；我要在这个过程中和谐地存在，让大家一起快乐地存在。」 says what formation forms. It belongs beside [34:03] in `drives…` *Construction and selection* and in claim 89.
- [28:30] "mental constructs" is English in both passes, the same term as `meta-attractor` claim 94. Add 「也许可以叫文化，或者心智结构（mental constructs）；我们并没有很好的词来表达它。」 to `drives…` own words.
- [08:53] 「这种存在本身，也是世界自身的存在。」 is the 10-02 "we are the whole process of the universe" in Chinese. Add it to `relational…` or `shengsheng…` own words.
- [12:53] (see 16) and [23:08] (a developmental East–West claim; at least a `OPEN-QUESTIONS.md` §5 row or own words).

### 20. optional
- `meta-attractor` claim 297, `alignment…` claim 221 and argument, `OPEN-QUESTIONS.md` §1.7 and §5, `TIMELINE.md`: "power changes hands" narrows 权力迭代 ("power iterates"). Use "where power iterates faster", and keep "changes hands" only inside the assistant's *rounds* mechanism.
- `TIMELINE.md`: "Late on 10-03 or just after midnight … Ren recorded" → "On the evening of 10-03, ending no later than 00:09 on 10-04 (Bangkok)". A 51-minute recording cannot have taken place after midnight.
- `alignment…` *The evidence for claim 221*: "associations with leading well are often negative" → "null to weakly negative". Name what to read: the meta-analyses on narcissism (Grijalva et al. 2015) and psychopathy (Landay, Harms and Credé 2019) and leadership; verify before citing.
- [21:32]: both passes have 「我们其实就是要赢」, where 要 is need or want. Add a row to `translation-notes.md`; the theory's descriptive reading is unaffected.
- `keep-the-possibility-space-open`, open question *Win, or oppose the logic*: cite the existing found-by-reading critique "Principle 1 contradicts Frontier 1" (bounded defence as relative advantage). That is exactly where 护闭 meets the AI rule.
- `relational…`: "Narrative reaches the drive system ahead of evaluation (`drives…`)" → cite `drives…` claim 29. "the test the corpus applies to platforms, advertising and security narratives" has no reference; cite 公开可纠 or drop the list.
- `relational…` critique and `OPEN-QUESTIONS.md` §5: "高度的实用主义 among the kernel's degenerations (own words 11)". The word 退化模式 is own words 12, so cite "own words 11–12".
- `GLOSSARY.md` exit: "the safeguard that keeps participation voluntary" against the line above it, "keeps creation voluntary". Use one word.
- `drives…` open question 16 and `jian…` open question 64, on 心理学: optionally add "coined in Japan (西周, 1870s) and adopted in Chinese around 1900; verify".

## Checked and found correct (that the main session might doubt)

- Numbering: every claims, own-words and open-questions sequence in the nine files is contiguous with no duplicates. New section letters follow the last one (meta P, alignment L, selfishness P, keep-open N, drives M, zhishan Q, shengsheng Q; jian 309–310 follow 306–308 in Q).
- The source README's *Where it went* matches exactly what was inserted: every claim range, own-words range and open-question number, the three Terms rows, and `OPEN-QUESTIONS.md` §§1.1, 1.2, 1.7, the two §2 items plus the third side, §3, §4.6 (placed under "6. It is a Chinese-state framework…") and §5.
- No existing text was removed. Every removed line reappears as a prefix of its replacement; the cosmic cancer header gained an inserted term only.
- Recognition claims: "aligns with the reality" [05:26] and "positive feedback loop that runs away" [02:57] are in both passes; so are "alignment" [37:35], 赢的逻辑 [49:24] and 余量 [40:22]. "Training ground" is in the independent pass only (the first pass has "training round"), and so is "drop out" (the first has "draw panels"). 天子, 小康, 丛林之神, 李维坦式 and Moloch式 are spoken in both. "Fourteen targeted rechecks" is correct (9 passage + 5 whisper).
- The 10-03 quotations are verbatim: the ruling 「如果胜利者的逻辑是cancer式的…」; 「这个理论应当可以推导出，不能」; trust as 「相信其他方的消息可信并可守承诺」; the pasted sketch's p* and T > R; and the "keep the struggle, accelerate, still be safe" position.
- The 10-02 transcript timestamps are right: [01:46:44] believer rule, [01:37:16] "lacks tenses", [01:34:45] 武, [00:22:31] trust, [01:24:48] five-year plan, [00:18:44] "fight them", [01:29:19–01:30:21] "use the the pre-Qin ontology".
- v6.1: Proposition 3.6 says exactly "narrower than the real coupling raises intensity and lowers its holder's own welfare, and selection favours the narrowest", and 3.6(2) is the best-response result. §3.8 has Ψ1 and the unbounded relative objective, and "never applied to persons, peoples or institutions". Also confirmed: §4.3; Proposition 2.3's $k_0$ and $\delta_f$; Proposition 11.2 (AI out of decision loops as a signal); thesis 9 (信任是…结果，不是前提); §11.1 and ϖ; "defensive realism with one more variable" (THEORY.md l.612); the fidelity review's "departs from by treating self-help…"; and DISCUSSION X1 "the Legalist programme of enriching the state…" among doctrines of national survival.
- Community document v0.3: §二 has 韩非 and 秦 as 文明的自我校正 (l.109). §三 has 「武的本义，是止息兵戈」 (l.119). §十一 has 致西方的朋友. NOTES says 「没有一句是你的原话」 and records 善不姓国 → 天下为公 / 己所不欲 / 反求诸己.
- Facts: 止戈为武 is from 《左传·宣公十二年》, said by 楚庄王, and the foot reading of 止 is the usual paleographic one. The post-2021 goals are 2035 and mid-century modernisation. The reviewer warning on flattening 理一分殊 with 心学 does exist (`zhishan…`, raised inside the corpus).
- Corpus references confirmed by reading:
  - relational claims 5, 12, 18, 19, 24, 25, 30, 34, 35, 41, 47 and own words 11;
  - shengsheng claims 257, 277, 296, 329, 333 and 343 (the quoted Chinese is exact);
  - zhishan claims 116, 124, 234 and 284 ("not evidence of a national character"), found-by-reading 4 (时机是策略决定) and 8, open question 25, and the double bind;
  - meta-attractor claims 141, 283, 288 and 292, open questions 31, 35 and 46, claims N, the SC slack gate, and the one-paragraph "means promoted to an end";
  - drives claims 24, 29, 41, 49 and 53, own words 60, and open questions 8, 13 and 14;
  - alignment claims 43, 55, 81 and 210, own words 41, 42 and 45, claims K, the pragmatic minimum (labour and finance first), the reallocation critique, the agent fleet, and the 12% figure (selfishness found-by-reading);
  - selfishness claims 121, 142, 143, 145, 148 and 161, own words 52, loops 3 and 4, the five endgames, the game-design axiom (claim 41), and the one-root rule;
  - keep-open: 护闭, the custody rules (GLOSSARY), 极皆成闭, 反者道之动 under *What was lost along the way*, anti-inevitability (claim 172), and "leaving the race without being eaten";
  - GLOSSARY entries 修齐治平 (王道者), 化 / 理, 天理 / 邪理 and 信 as the time dimension (relational l.41);
  - OPEN-QUESTIONS §1.1(a), §1.2's behavioural test, *Fighting the unchangeable* and *大道之行's argument from state capacity*;
  - the OCASC review's GRIT ladder, and the v6.1 title.
- `.gitignore` excludes `original.m4a` (`git check-ignore` confirms). The 10-02 recording does carry a Voice Memos location label ("Soi Sathon 11 Yaek 9").
