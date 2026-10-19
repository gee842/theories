# Slice `yi`: the 易傳 and 周易 beyond Y1–Y3 (AI notes)

All readings here are the AI's. Ren's thesis (that a relational ontology runs through Chinese thought) was tested, not assumed. Fragments are copied from the 易道体系图 v1.3 texts and checked by exact match; repository forms from `sources/zhouyi-yizhuan/` are given as `repo_fragments` wherever Y1 preserved the passage. Two fragments (程頤's preface and the 朱子語類) are in neither atlas: their entries carry `needs_source` with the zh.wikisource page they were read from.

**Output.** `entries.json` holds 49 entries: 17 agreement, 17 scope, 15 divergence, and 7 gaps. None of the 69 passages in `passages.json` is remapped. The line relations (應 as opposition, 比, 承, 乘, 當位, 中) and 王弼's 《略例》 are left to their owners. `calc/` holds the four computations cited below (`order.py`, `zagua.py`, `houtian.py`, `parity.py`, each run as `python3 -I <script> <path to Hexagrams.lean>`, except `houtian.py`, which needs no argument). It also holds the builder that checked every fragment, repository fragment, declaration (against an index of the Lean sources), record id and atlas id.

## 1. The slice's relational structure

The material has three layers, and they behave differently.

**經.** The judgements and line texts are mostly outside this slice. Only one point matters here: 元亨利貞 in the 經 is a formula of divination. Reading it as four virtues is a 傳 reading (wenyan-side).

**傳, describing the configurations.** Where the 傳 describes relations among the configurations themselves, it is relational, and the claim can almost always be stated exactly and checked against the spine:

- the four complement pairs of 說卦 ch. 3;
- the one-line generation of 說卦 ch. 10;
- the parity classes of 繫辭下 ch. 3;
- the turned-over pairs that 序卦 names inside each pair;
- the pairs that 雜卦 contrasts;
- 乾坤毀 (contrast and change depend on each other);
- 恒 (lasting through change);
- 革 (change of rule);
- 損益 (one exchange read from two ends);
- 節 (bounded on both sides);
- 既濟 (completion is no rest).

**傳, arranging or valuing.** Where the 傳 arranges or values, it stops being relational in the checked sense:

- It **assigns**: the order between pairs in 序卦, the stations of 說卦 ch. 5, the image lists of ch. 11, and the analogies of the 大象.
- It **ranks**: 君子/小人 fixed on the two values, 一君二民, the 然後 chain up to 君臣上下, yin as wife and minister.
- It **reads value into the start of the course**: 四德, and 餘慶/餘殃.

**注 and 疏.** The commentaries hold a real contest between two readings.

- **Ground readings** read the relations from a prior ground:
  - 韓康伯: 有必始於無, and yin and yang "wait on" a 一 that is 無;
  - 孔穎達: 太極 as 元氣 before 天地 divided;
  - 朱熹's 語類: 未有天地之先，畢竟是先有此理.
- **Relational readings answer them from inside the tradition:**
  - 王夫之: 乾坤并建, 时无先后, 权无主辅; 无有道而无天地; 未济之世亦乾坤之世;
  - 程頤: 无一定之理 and 體用一源.

The relational reading is therefore a position within the commentary tradition, not its consensus.

**Verdict for this slice.** The thesis holds for the structural core of the 傳: where its statements can be checked, they are relational and mostly lawful. It fails for the arranging and ranking layers. It is contested in the commentaries. Most of the counterexamples are of the "fixed rank on a value" and "assigned, not derived" kinds. The four kinds the brief names all occur:

- prior substance or ground: 孔's 元氣, 韓's 無, 朱's prior 理;
- fixed nature: 君子/小人 on the values;
- personal will: 大人 先天而天弗違;
- contest to win: 夬 剛決柔 closing 雜卦; 陰疑於陽必戰.

## 2. Strongest correspondences

1. **恒彖, 久 as continuation through change** (tuan-heng-jiu). The brief asked whether 久 is continuation through change. In the 恒 彖 it is. What lasts is an invariant of the law along every run: the changes of line going once round are kept (`changesAround_invariant`, `changesAround_run`), and what the law reaches stays on one orbit (`reach_keeps_orbit`). Every configuration returns after twelve steps (`twelve_steps`), which is 終則有始. A pattern lasts only by being passed on (`ByPassing.passes_within`).
2. **說卦 ch. 3** (shuogua-tiandi-dingwei). The four pairs are exactly the four trigram complements. Stacked, they give the eight hexagrams opposed at every height, which is where the oppositions glue (`oppositions_glue_iff`). 相錯 is the complement relation, which the law commutes with. It is not repulsion.
3. **說卦 ch. 10** (shuogua-yi-suo). 索 is a one-line change of 坤 or 乾 at place 1, 2 or 3. The two generated at one place are complements, which is `flip_complement`.
4. **序卦 within pairs** (xugua-within-pairs). Seven of the eleven 物不可以終X steps fall inside a pair, where the second hexagram is the first turned over or changed in every line (`order_paired`). 剝窮上反下 names the turn literally.
5. **革彖** (tuan-ge). 革 is a change of rule, not of state. A perturbed state is reabsorbed and a perturbed rule changes the outcome (`Captured.*`, `perturbation_reabsorbed`). A changing rule regains what each fixed rule loses (`Switching.*`), as 天地革而四時成 needs.
6. **乾坤毀 … 易不可見，則乾坤或幾乎息矣** (xici-qiankun-hui). A distinction that no future shows is no distinction (`Law.alike_iff_sameFuture`, `Alike.tests`).
7. **睽彖** (tuan-kui). Complements differ in every line and never meet under the law, yet the law commutes with the complement and the pairs are a lumping it goes alike across. They are apart as configurations and alike in what the law does with them.
8. **井, 節, 既濟, 損益.** These match the Flow base:
   - 井: drawing and replenishment recur together (`Run.draws_iff_replenishes`, `Stock.repeat_covered_iff`).
   - 節: bounded on both sides (`beyond_given_bounded`; `waitsAll_more_waiting`, `withholding_absorbs`).
   - 既濟: no rest (`rests_iff`, `six_steps`), and stopping replenishment runs the stock down.
   - 損益: one balanced exchange read from its two ends (`rise_given`, `fall_taken`, `exchange_step_iff`).
9. **Commentary.** 王夫之's 并建 (no first, no ruler) is the complement symmetry, and 无有道而无天地 is the law read from its world (`shown_le_iff`, `exists_law_iff`). 程頤's 下厚則上安 is the feeding dependence (`beyond_gives_nothing`, `consumption_ends_with_feeders`).

## 3. Divergences and non-relational strands

- **序卦 between pairs** (xugua-between-pairs). This is the main result of the slice. The received order is a run of no three-cell local rule; with ring or negated-wrap boundaries, none agrees on more than 9 of its 63 steps. Nor is it a run of any law that permutes the places and applies a mask; the best of these, turning over, agrees on 28 steps, exactly the turned-over steps inside the pairs. Between pairs the order changes from 1 to 6 lines. So the reasons the 序卦 gives between pairs (物不可以終否，故受之以同人; 飲食必有訟) are readings laid over a list. They are not a law of succession that the configurations carry. This settles the open item in §8 of the Yi chapter: the order is asserted between pairs and lawful only inside them. Formally, the order is a run only of the law it shows, which admits only it (`Run.keepHistory_shown`).
- **說卦 ch. 5** (shuogua-di-chu-zhen). The 傳 itself glosses 帝 as 萬物出 and 戰 as 陰陽相薄, so no personal will is asserted. But its cycle of trigrams through stations is a run of no permutation-with-mask law (best 4 of 8 steps) and no three-cell rule (best 5 of 8). Only one of its four diametric pairs (離坎) is a complement. One 傳 thus holds both a structural arrangement (ch. 3) and an assigned one (ch. 5).
- **Ranking on values.** Four passages fix rank or moral nature on a value or a count, a relation the law treats symmetrically (`waxWane_complement`, `changes_symmetric`, `Commutes.rest_paired`):
  - 泰彖 內君子而外小人 (tuan-tai-junzi-xiaoren);
  - 繫辭下 陽一君而二民，君子之道也 (xici-yijun-ermin);
  - 序卦 有父子然後有君臣…有上下 (xugua-fuzi-junchen);
  - 坤文言 陰雖有美…妻道也，臣道也 (wenyan-yin-cong).

  One nuance is kept: the 否 彖 inverts the 泰 sentence, so the verdict there follows placement, which is relational. Only the names fixed on the values are not.
- **Contest.** 雜卦 closes on 夬 決也，剛決柔也。君子道長，小人道消也 (zagua-guai-end), and 坤文言 has 陰疑於陽必戰. Under the law, 夬 is followed by 乾 and then 姤; no law compatible with the complement draws everything to one side.
- **Value read into the course.** 元者善之長也 (wenyan-side) and 積善之家，必有餘慶 (wenyan-yuqing). The spine's dynamics fix no significance (`significance_undetermined`). Ethics comes only as theorems under the continuation condition, which itself orders nothing. 程頤 restricts the four virtues to 乾坤 (cy-side-qiankun), a scope correction from inside the commentaries.
- **A person coinciding with the course.** 大人 … 先天而天弗違 (wenyan-heqide) conflicts with `no_prefix_fixes_next`, `diagonal_misses` and `Frame.self_incomplete`. 後天而奉天時 remains.
- **Prior ground or stuff.**
  - 韓康伯's 夫有必始於無 (han-you-shi-yu-wu) and 陰陽雖殊，無一以待之 (han-dao-wu-zhi-cheng, which is scope: 道 being no formation does fit);
  - 孔穎達's 太極謂天地未分之前，元氣混而為一 (kong-taiji-yuanqi);
  - 朱熹's 未有天地之先，畢竟是先有此理 (zx-yulei-li-xian), which he qualifies himself with 理與氣本無先後之可言, making the priority logical, not temporal.

  The 本義 lines are different (zx-qi-li, scope). There 理 is 其理, the law of the alternation, and 大極者其理也 reads 太極 as that law rather than as 元氣.
- **Analogy.** The 大象's 君子以… (daxiang-junzi-yi) take an image as a model for conduct. The structure carries only for 既濟 (no rest, so 思患而豫防) and 革 (change of rule, so 治歷明時).
- **Two relations under one name.** 文言's 同聲相應 is response between likes, a lumping. The 彖's 應 is opposition, values differing at one height. They must not be identified (wenyan-tongsheng).

## 4. How the earlier repository studies stand

- **YI-ZHUAN-AND-BECOMING.md and passages.json (Y1–Y3).** Kept and extended. This slice adds:
  - 久 in 恒;
  - 革, 損益, 節, 井, 睽;
  - 既濟/未濟's 終止則亂 and 不續終;
  - 說卦 ch. 3, 5, 10 and 11;
  - 雜卦, which Y1 did not preserve;
  - the 文言 sentences not yet mapped;
  - the 注/疏 layer of 韓, 孔, 程, 朱 and 王.

  Two items the chapter's §8 left open now have checked answers or statements. The order's reason is answered negatively (gap 1). 卦變 is stated as a line exchange (gap 2). Its note that 卦序 is "not any law's orbit" becomes exact: no local rule and no permutation-with-mask law.
- **DAO-AND-GENERATIVITY.md (6 October).** Its caution is kept: textual affinity is not identity, and 傳 statements are not derivations. So is its row on 系辭上 ch. 5, now covered passage by passage by Y1. Its vocabulary (生成理论, "共同生成") is superseded by the current terms (生生, the continuation condition, 識, 明, 理).
- **DAO-CLASSICAL-SOURCES.md §4.** Kept as provenance. It is narrowed by Y1's jizhi-shan (divergence) and by this slice's 四德 and 餘慶 divergences. Its hope that the 易傳 gives "a more direct generation–value link" now stands as follows: the 傳 asserts that link; the spine does not derive it.
- **HANZI-AND-THEORY-TREE.md and PRE-QIN-AND-WENYAN.md.** Their method is kept: a sense is scoped to its context, and counterexamples enter the core. They are extended by the 應 case (one name, two structures) and by the ranking counterexamples, which are the 易 counterpart of their 韓非/商君 examples. Their candidate vocabulary table predates the adopted naming study and is superseded where it conflicts.
- **The study of 理 (COGNITION-LI-AND-RECIPROCITY, in history).** It is refined here. 理 differs by commentator:
  - in 程頤's 乾 注 it has no form and is shown through images, with no priority asserted;
  - in his 既濟 注 there is 无一定之理;
  - in the 本義 it is the 理 of the alternation;
  - in the 語類 it comes first.

  The current gloss of 理 (a lumping the law goes alike across) fits the first three and not the last.
- **WANG-YANGMING.md and LIANGZHI-EVOLUTION.md.** Untouched by this slice. The 理/心 question belongs to the ru slice. zx-yulei-li-xian may overlap with the ru mapper and should be coordinated.

## 5. Candidate gaps, ranked

Each gap was checked absent by grepping the four hexagram modules and the digests.

1. **The received order is a run of no simple law** (xugua-between-pairs). It is a run of no three-cell local rule (ring or negated wrap; at most 9 of 63 steps) and of no place-permutation-with-mask law (at most 28, exactly the in-pair turns). Steps between pairs change 1 to 6 lines. All by `decide`. With it goes the smaller 說卦 ch. 5 statement (shuogua-di-chu-zhen, on `Bool × Bool × Bool`). This is a checked negative that closes §8's open item and keeps anyone from building a law of succession on the order.
2. **卦變 as exchange** (tuan-sun-yi). Define `swap i j`.
   - It keeps the count of unbroken lines.
   - 損 is 泰 with lines 3 and 6 swapped; 益 is 否 with lines 1 and 4 swapped; 恒 is 泰 with 1 and 4 swapped (剛上而柔下); 咸 is 否 with 3 and 6 swapped (柔上而剛下).
   - The twenty configurations with three unbroken lines are 泰, 否 and the eighteen one cross-half swap from them.
   - Each swap is one balanced step of the exchange law between two relata: the unbroken lines of the lower half and of the upper half.

   This joins the hexagram line to the Flow base and makes the 彖's 剛來/柔上 statements exact.
3. **The parity of the unbroken-line count is a lumping** (xici-yanggua-qi).
   - Every step of the law and every one-line change flips it.
   - `GoAlike (Law.process waxWane) (yang · % 2)` holds, beside `yang_not_goAlike`.
   - The parity is linked to `phaseCount_parity` by `phaseCount ≡ yang + 1 (mod 2)`.
   - Within a half, the count is odd exactly when the half is 乾 or one line changed from 坤.

   This joins 繫辭下 ch. 3 to 說卦 ch. 10, and it shows that 奇/偶 carries law where 多/少 does not.
4. **雜卦 census** (zagua-pairs). The 雜卦 sequence is a permutation of the order. It holds the same 32 pairs, 28 adjacent and 4 interleaved in its last eight, with no adjacent pair there.
5. **Direction-indexed 交** (tuan-tai-pi-jiao). Define `meets`, true at every height of 泰 and none of 否, while both are opposed at every height. It shows that 交 adds a premise beyond 應. It should be handed to Y2–Y4.
6. **No rest under waxing and waning** (tuan-jiji-weiji). `waxWane s ≠ s`, and no run comes to rest. It is a one-line corollary of `six_steps`, small.

Gaps 1, 3, 4 and 6 are pure `decide` on the hexagram world and need no premise. Gap 2(d) needs only an instance of the existing exchange law.

## 6. Counter-review

- **Pattern-matching risk on the Flow laws.** 井, 節, 損益, 下厚則上安 and 終止則亂 are matched to Flow laws by structure: draw/replenish, bounded take, balanced exchange, feeding closure, run-down. The texts do not quantify anything. The match is between the shape of the claim and the shape of the law, not a derivation of the text. The atlas's own limits (HX-R013: no conservation in the 彖; CY-R014: a commentator’s analogy, not a causal law) are kept, and conservation is attributed only to the configurations under a swap.
- **Lumping risk.** 睽, 同聲相應 and 說卦 ch. 11 all lean on `goAlike_iff_lumped`. The agreement in 睽 rests on the complement being both "most apart" and "alike under the law". That is exact for the hexagram law, but 天地/男女/萬物 are images, so the agreement is with the configuration reading of the 彖, not with a claim about 男女.
- **The 乾坤毀 agreement** reads 或幾乎息 as "the distinction is not registered". That is a reading of a hedged clause.
- **Ground readings and the commentator's intent.** 韓's 無 can be read apophatically (無 as "no thing", not as a thing prior), which would move han-you-shi-yu-wu toward scope. I kept it as a divergence because 有必始於無 states a direction of beginning that the spine lacks. 孔's own 疏 (道雖無於陰陽，然亦不離於陰陽) partly retracts it, and the entry says so.
- **Scope of 朱熹.** The 語類 entry is outside the 易 commentary proper and is taken from a page not in either atlas. Its fragments must be checked against the preserved page.
- **What the computations do and do not show.** "No simple law" covers two explicit families (three-cell local rules, and permutation with mask). It does not show that no short description of the order exists. The claim is stated only for those families.
- **Readings that could be wrong.** 各正性命 (tuan-qian-gezheng) favours natures formed within change by sentence order; a reader could defend the prior-nature reading. 程頤's 序 (cy-xu-tiyong) is scope because 從道 can be read as a prior norm; I did not decide it.
