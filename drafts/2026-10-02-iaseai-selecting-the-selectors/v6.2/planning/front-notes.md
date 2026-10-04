# V6.2 front matter: review and installation notes

4 October 2026. This note covers the review of the front-matter drafts in `planning/front/single/` (whose drafter stopped before checking them), the revisions, and their installation into `src/`.

**Files installed:**
- `src/core/00_head.md`: title, status line, abstract, 中文导读;
- `src/core/10_s01.md`: §0 and §1;
- `src/core/d0_symbols.md`;
- `src/supp/00_S0.md`.

No other file in `src/` was touched.

**Source of truth.** The final §2–§12 in an assembled scratch copy, read in full, with every claim of the abstract, §1.2 and the guide checked against the claim box and statement of its section. Also used: `planning/elegance-build-notes.md` §6, plan §1, §2, §4, §6 and §8, and D1-opus §1.2–§1.4, §3.2, §5 and §7.

## 1. Checks

The checks ran in a scratch copy of v6.2 with the four files installed (`assemble_v62.py`, `cd src && refs_v62.py`, `assemble_v62.py`, `xref_v62.py`).

- **Assembly:** "no problems", 93 core and 35 supplement declarations; no forward use, no doubled kind names, no banned phrases.
- **References:** the core and supplement reference lists come out byte-identical to those in `src/`, so the front matter needs no reference change. The discussion list differs only because X1 and X2 changed after the last refs run; that comes from another agent's edits, not from these files.
- **xref:** ALL CHECKS PASS.
  - Citation coverage is complete both ways.
  - All 32 must-stay phrases are present.
  - No state or firm is named.
  - The guide and §1.2 each have nine items. Their term match per item is 82, 86, 82, 100, 93, 92, 91, 100 and 67%; the threshold is 60%.
- **Banned phrases:** none in the four files. This covers plan §8.3 and the task list: "every forward-looking actor", "manufactur-", "on any reading", "win this race", "shared flourishing", "systemically false", "decides whether leads compound", "regime" and "one pressure".
- **Banned in the guide:** none of 宿主, 签名, 闭合于自身, 这个过程是好的, 弱化身 or 强化身 appears. 母体 is used throughout.

**Lengths** (assembler figures, with the draft's in brackets):

| Part | Now | Draft |
|---|---|---|
| Front (abstract) | 545 words | — |
| §0 | 495 words | 473 |
| §1 | 2,899 words | about 2,660 |
| §1.2 | about 1,470 words | 1,346 |
| Symbols | 789 words | — |
| 导读 | 2,645 字 | 2,695 |

## 2. What changed from the draft, and why

### Abstract
- **Opening.** The draft defined the selection pressure of winning as "success raises the stakes and weakens what could restrain it". The new opening is Definition 2.1: the three conditions, then the closure. The "raises and weakens" sentence is a set of Part I results, each in its own model, whose co-movement is C0, not a definition.
- **Price of standing.** The fixed-prize clause is added: "wherever the discounted loop gain is positive" (Proposition 3.9(1)). The draft had only the proportional-prize case.
- **Correction.** The rate-law sentence now states only the sufficient half, from a certified start (Proposition 4.5(2)). The draft's "loses it to slower growth where …" sits in §1.2.
- **Scissors.** The pivot is named (the won share), "each arm proved in its own model" is kept, and co-movement is "what the diagnosis tests".
- **Masked divergences.** "Escape even a common constraint enforced at admission" became "can escape even a common constraint conditioned on evaluated behaviour" (Remark 6.8). Admission on evidence the system's behaviour does not control is the C12 route, which the draft's wording denied.
- **Added.** "We are one" as the long-term requirement, with "global" failures (§3.6).
- **Tiers.** The tiers follow §12.1: tier 1(a) and 1(b) told apart, "on the present evidence", and coercive restriction inside the compared tier.
- **Not added.** Talk and internal deployment, which the draft abstract also lacked, stay in §1.2 and the guide, to save length.

### Guide
The guide was rewritten to mirror the new §1.2 item by item and §12.1 tier by tier.
- **用途与意义** now states broad E1's aggregate mechanism, as §0 does.
- **"May come false".** "成为共识的预测，有助于让自己落空" became "预测也才可能落空": a hope, as §0 states it, not a claim.
- **Ren's own line.** Ren's book line 癌亦增长，而其长竭母体之生 is quoted instead of a paraphrase.
- **核心** is now the abstract's opening (the three conditions and the closure), plus "改变它的不是更好的玩家" (Remark 3.10).
- **Item 1** carries the channel-by-channel lever conditions exactly, and no longer repeats 核心's definition (about 25 字 saved).
- **Item 4** names the pivot, adds "随赌注超出博弈之下的供给而增大", and keeps C0 as the arms' co-movement. "参与者越多放大越弱" replaces "人越多越弱".
- **Item 5:** internal deployment now applies to "最可能成为载体的…自动化 AI 研究的系统". The draft said strong incarnation itself "最先出现在开发者内部", which §6.4 does not claim.
- **Item 9** points to the 判断 instead of repeating the tiers.
- **判断.** Tier 1(b) gives the reason for its burden rule (危害先于证据). Tier 3 now has "最坏情形都越过容忍线" and both of §12.1's reasons, (i) and (ii); the draft had only a compressed (i).

### §0
- **Dilemmas.** "In the models of Part I, wherever racing is each actor's best response, each ends worse off than under joint restraint" stated as a general result what Part I shows in particular dilemmas (Propositions 3.6(3), 3.7, 6.1 and 6.2), with the dissipation of Proposition 5.2. It now reads "in the dilemmas Part I computes", with the dissipation clause sourced to §5.1.
- **The game, not the act.** This paragraph now states broad E1's aggregate mechanism from §6.6: in a contest decided by relative strength, an instrument adopted by all leaves each where it stood and pushes down whoever lacks it, and where people are the instrument it displaces them. It keeps "a use that helps one person …" and the Section 3.5 sentence.
- **Meaning.** Ren's identity wording is kept verbatim. The draft's cancer sentence ("opposes one logic, not growth, competition, technology or any people: … a part … forgets the body it belongs to") nearly repeated §12.4's "What has to be opposed is not growth, competition or any people, but one logic: a part that forgets it belongs to a body". It was replaced by sentences with a different job:
  - "written from inside that process, for every participant in it rather than for any side";
  - the opposition is to a logic, an objective with no point of enough held by a part that counts only itself (§3.8, §5.3);
  - "a future kept open to every participant, the minds now being made among them" (the 共开 of §3.7).

  Neither "Humanity has a great future …" nor "What has to be opposed …" appears in §0 any more.

### §1.1
"…with cooperative aims declared in the same documents" is added, to match T1's status in §7.3. "Through acceleration" is dropped, since the register does not show it as declared.

### §1.2, item by item
1. "Leads compound below one" became "below a structural gain of one".
2. The opening now has the §3 box's selection sentence: "errs toward what can be divided, and selection favours the narrowest". "However carriers are grouped, selection does not favour what benefits all" is added as the reason for anticipation. The requirement keeps §12.4's form, "if growth and change are to continue" (see open issue 3).
3. The draft said slower correction loses "wherever influence keeps pace". It now loses "to carriers whose influence tracks its selected level" (Proposition 4.5(2)). The floor condition is an antecedent, and the human-capacity clause is kept.
4. "The pivot is the share of capacity that has to be won". The objective arm is stated as in §5's box. "Each arm is proved in its own model; that the arms close together in the world is conjecture C0". The reduced joint model was dropped to save length; it is in §5's box. Talk is $n/(n-2)$, fading with $n$, and "blocs are a reading, not a result".
5. The tax premise is stated as an antecedent: "against an otherwise identical developer that does not counter it". Internal deployment is attached to "the systems most likely to become such carriers, those that automate AI research".
6. The draft's "the trajectory's dynamics are signatures …" and Table 7.1 pointer are kept. "Shifts winners toward those whose objectives give least" was not added, because it needs Proposition 7.3(2)'s premise and would lengthen the item; §7's box carries it.
7. "Where every worst case crosses the tolerance, the ranking is a judgment" is added. The requirements sentence now has §9's exact antecedent: the floor within reach, a race carrier present, and no single rule-maker reaching every carrier whose load can carry the host below it.
8. "No lever makes the selected intensity zero" is kept, with "while a positional prize remains" as its antecedent. Theorem 10.4 was left out, since it needs two antecedents and the item is a summary.
9. The ratchet and dwell sentence is added, "in the field model". Trust is an outcome, through narrow E1 and the costly signal. The tiers follow §12.1. "Under three conditions of its own" is attached to coercive restriction, and broad E1 is the scope.

### §1.4
- **Not claimed.** "That relative actors enforce or talk as blocs" is added. The name sentence uses the plan's wording ("the name is for the mechanism; attraction is shown only in the field model of Section 4; whether the generative order attracts is a conjecture").
- **Tags.** The tags paragraph now says that the English renderings of Ren's Chinese, and model paraphrases of his spoken words, are the drafters' until he confirms them.
- **What is new.**
  - Γ "organizes known instability results".
  - The price of standing is "Powell (1991), generalized by the common channel, which decides where the concern arises".
  - The enforcement split is "with the comparative statics by which the share of capacity that has to be won moves both".
  - The nested loop clause no longer claims to explain incarnation, weak and strong; it now ends "which divergences the selection of developers keeps, and why masked ones can escape even a common constraint".
- **Review status.** The draft said "CLAIMS records what became of its findings", which the V6.2 registers are still being written to show. It now reads "whose review round this version answers".
- **Reading path:** abstract or guide, §0, §1.2, §1.4, the claim boxes, Table 7.1, §12.

### Symbols (`d0_symbols.md`)
- **"One meaning".** The claim is restricted to the table, and it excepts the statements and proofs that define a letter afresh, which S0 lists.
- **Added:**
  - $\Phi_H$, and $\Phi^R$, $\Phi^T$, $\Phi^P$, $\Phi^S$, moved here from S0 because they are core symbols (§8.1, Proposition 8.5);
  - $V_{\rm alarm}$ and $\delta_{f,j}$;
  - $w$ in its own right, as the elasticity behind $w\delta_h$;
  - $u_t$, glossed as the uncovered share of hazard modes.
- **Labels:**
  - "Tests A–G, I–M and Γ", since there is no Test H;
  - "Studies of the research programme";
  - EV1–EV18, (A1)–(A9), and the four conditions of a correction decision.
- **Premises** (clock), (safe fallback), (bounded own risk) and (advantage keeps pace) are added.

### S0 (`00_S0.md`)
- **(A9)** carries its tag [num: MP; held for outside review].
- **Shared table:**
  - added $g_V$, $\mathsf u_t$ and $L_b$, read for both `join` and `commonfrontn`;
  - moved $w$ and the $\Phi$ superscripts to the core table;
  - $V^{\rm exit}$ and $V^{\rm stay}$ glossed as "of leaving, first, … and of staying".
- **Reuses.** A new paragraph, organized by chapter, lists every reuse of a table letter that a scan of the three documents found (see open issue 5). Among them:
  - Remark 5.5's $T$ (both a span of periods and a payoff);
  - Proposition 5.12's $u$ and $w$;
  - the $w(y)$, $u$, $w$, $a$ and $b$ of S2;
  - the $w$, $z$, $b$, $w_i$ and $x_j$ of S3;
  - S4's $u$;
  - the $F$, $x$, $s$, $m$ and $u$ of S5;
  - the $T$, $H$ and $x$ of S6;
  - the $\rho$, $\gamma$, $u$, $v$, $g$ and $h$ of Jones (2024) in S8;
  - the $x$ and $s$ of S9 and S10;
  - the $u$ and $s$ of S11;
  - in the core, the $S$ and $g$ of `compound`, the $g$ and $H$ of `twochan`(5), the $x$ of `blind`(3), the $S(x_p)$ of `pausefield`, and the $b$ of (15).
- **Renames,** organized by chapter, with two additions: Definition 3.2's $F\to\mathcal F$, and S3's constraint costs $\kappa_k\to c_k$ (the V6.1 proof of Lemma 3.3 wrote $\kappa_k$). Every rename the merge and elegance notes record is listed (U02, U03, U04, U05, U06, U08, U10 and U11).
- **Claim tags** gain the same sentence on renderings and paraphrases as §1.4.

## 3. Open issues

1. **Guide length.** The guide is 2,645 字 against a target of about 2,400, about 10% over; the draft was 2,695.
   - What fills it: nine items that each carry their section's antecedents, and a 判断 that keeps all of §12.1's tiers, the three conditions and both reasons.
   - Cuts that would reach 2,400, in order of least loss:
     1. drop 本文不主张什么's last two clauses (about 25 字);
     2. drop tier 3's reason (i) (about 35);
     3. drop item 4's sentence on blocs (about 12);
     4. drop item 3's human-capacity clause (about 18);
     5. drop item 5's instrument sentence (about 50);
     6. drop 核心 (about 75), leaving item 1 to define.

     All but the first lose something §1.2 states.
2. **xref term list.** It still maps 'host' to 宿主 and 'signatures' to 签名, both banned in the guide, so every item that mentions them loses a term. The list should read 母体 and 征候. This is xref's owner's file, not touched here.
3. **"If growth and change are …".** §3.6 says "are favoured", and §12.4 and the front matter say "are to continue". The v6 CLAIMS marks the "favoured" form (R, D), and the V6.1 fidelity review recommended "are to continue" for §1.2. The integration editor should settle one form, and Ren should confirm it.
4. **Remark 5.5** uses $T$ in one remark both for a span of periods, $\upsilon(T)$, and for the payoff of racing against a restrainer. Writing the span as $\upsilon(\cdot)$ evaluated at $T_{\rm dec}$, or as $\upsilon(t)$, would remove the clash. This is the core §5 owner's file. S0 lists the reuse meanwhile.
5. **S0's reuse list.** It comes from a scan of bare table letters in math spans of THEORY, SUPPLEMENT and DISCUSSION, read by context; it is not proved exhaustive. A mechanical check, such as listing every declaration "write/let $X$" of a table letter, would make it so.
6. **S13** (other agents' file):
   - its $F(U,\dots)$ still clashes with the sanction $F$ (merge notes U04);
   - S13 and S15 still contradict S4 and S11 (elegance-build notes §6, item 3).
7. **README** (register, other agents): its reading paths should match §1.4's thirty-minute path.
8. **Abstract length.** The abstract is about 420 words, against D1-opus's draft of about 290. Each sentence carries a result. The candidate cuts are the survival sentence and the masked-divergence clause.
9. **§1.2 length.** §1.2 is about 1,470 words, against D1-opus's target of 750 (the draft had 1,346). Its length comes from conditions written as antecedents. A venue version would cut items 1, 3, 7 and 9 to their headlines.
10. **§0** gives no corpus key for the broad E1 paragraph. §6.6 holds the key ("for any game, that is competitive in dynamics and concentrates, ai accelerate it" [corpus: alignment-selection]), and §0 points there.

## 4. For Ren: renderings and paraphrases, to be marked D in CLAIMS

These are every English rendering of Ren's words, and every model paraphrase of them, in the four files. Each should carry D until Ren confirms it.

**English renderings and paraphrases:**
1. **Identity** (§0, and the guide's 意义): "We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good. Decay and renewal belong to its growth."
   - Model rendering of Ren's spoken "we are not just our life. We are the whole process of the universe doing this and itself and this is great" [shengsheng, 2026-10-02, 01:06], and of his "decay and renewal" ruling (D1-opus §5.1, transcript 00:57).
   - §0 tags it [corpus: shengsheng, 2026-10-02].
2. **Chinese of the same** (guide): 我们不只是各自的一生；我们就是那更大的生生过程本身，它正经由我们继续，这很好。衰败与更新，也属于它的生长。 This is the model's Chinese; "这很好" is used instead of the banned 这个过程是好的.
3. **"Understanding that we are one … is a long-term requirement if growth and change are to continue"** (abstract, §1.2 item 2) and 理解"我们是一体"…是增长与变化得以延续的长期条件 (guide item 2). This renders the (R, D) line of the v6 CLAIMS; see open issue 3.
4. **"Growth is not the danger; the mind is"** (§1.2 item 4) and 危险不在增长，而在心 (guide item 4). The English is keyed [corpus: meta-attractor; Ren, 2026-09-25] in §5.3; the Chinese is the model's.
5. **"The analysis judges games, not acts, and structures, not persons"** (§0) and 本文判断博弈，不判断行为 (guide). This paraphrases Ren's ruling "judge the game, not the act".
6. **The broad E1 mechanism** (§0; guide 用途与意义). It formalizes Ren's "for any game, that is competitive in dynamics and concentrates, ai accelerate it" [alignment-selection, 2026-09-26]:
   - "an instrument that every contestant adopts leaves each adopter where it stood and pushes down whoever lacks it … where people are themselves the instrument, as in labour, it displaces them";
   - in Chinese, 人人都用的工具不改变各自的位置，只把没有它的人压下去.
7. **"Broad E1 … is the scope; narrow E1 is the first step"** (§1.2 item 9) and 广义 E1 是范围，狭义 E1 是第一步 (guide). Ren's ruling of 2026-09-26, as keyed in §11.3.
8. **"AI is a planetary technology: … so it is for all, not a means for one side to grow bigger at the others' expense"** (V1, §1.3). This is D1-opus's rendering of Ren's phrasing.
9. **"The logic of winning"** for 讲赢 (§0 and throughout).
10. **"No better guardian is an answer; a structure in which error cannot grow without limit is"** (§1.2 item 8) and 没有更好的守护者，只有错误不能无限扩大的结构 (guide item 8). These render Ren's book line 真正之秩序，非得永远正确之人，乃立错误不能无限扩大之构 [shengsheng, 2026-07-14 第十四章] into English and into modern Chinese.
11. **"Provision sits beneath the game, like trees"** (§1.2 item 8) and 供给在博弈之下，像树一样 (guide). This paraphrases "Trees are providers" and "the lungs of the ecosystem" [shengsheng].
12. **"Success earns reward, not more advantage in the same game"** (§1.2 item 8; guide item 8). This paraphrases "a winner of the game should be rewarded with anything other than more advantages of the game" [possibility-space].
13. **"Trust is an outcome of a staged transition, not its precondition"** (§1.2 item 9) and 信任是分阶段过渡的结果，不是前提 (guide). This paraphrases "Trust is not a prerequisite—it is an outcome" [selfishness-spiral, 2025-03-14].
14. **"A future kept open to every participant"** (§0). This paraphrases 共开 (共开、共续、不夺共续) [shengsheng].
15. **部分只算自己，忘了自己属于一个身体** (guide 意义). The model's Chinese for §3.8's "no longer knows it belongs to a body".
16. **"Selecting the selectors"** (§1.2 item 3's title) and 选择选择者 (guide). These render 被选择的，开始选择选择者 [meta-attractor].
17. **Model's Chinese terms in the guide:**
    - 生生的选择 (item 8's title) for "the generative alternative";
    - 化身的弱形式/强形式;
    - 征候 for "signatures";
    - 母体 for "host".

**Model formulations in the theory's own voice that compress Ren's rulings** (not attributed to him, listed for completeness):
- "Each actor computes correctly; the game is wrong" (abstract; §1.2 item 2) and 每一方都算得没错，错的是博弈;
- "change what winning confers" and 改变赢了之后能得到什么;
- 改变它的不是更好的玩家 (guide 核心), which renders plan §1's "Better players do not fix this; a different game does".

**Quoted verbatim, no rendering:** 讲赢 and 讲理 (guide); 癌亦增长，而其长竭母体之生 (guide 意义), Ren's book line [shengsheng, 2026-07-14], quoted where the draft paraphrased it.
