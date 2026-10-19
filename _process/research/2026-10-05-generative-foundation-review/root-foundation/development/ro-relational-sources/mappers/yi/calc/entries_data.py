# Mapping entries for slice `yi` (data for build_entries.py). Every reading is the AI's.
A = 'yidao-v1.3'
T = 'evidence/texts/'
XS = 'sources/zhouyi-yizhuan/yizhuan/xici-shang.json'
XX = 'sources/zhouyi-yizhuan/yizhuan/xici-xia.json'
SG = 'sources/zhouyi-yizhuan/yizhuan/shuogua.json'
XG = 'sources/zhouyi-yizhuan/yizhuan/xugua.json'
WY = 'sources/zhouyi-yizhuan/yizhuan/wenyan.json'
B = 'Becoming.'


def H(n):
    return f'sources/zhouyi-yizhuan/hexagrams/{n:02d}.json'


def R(path, *texts):
    return [{'path': path, 'text': t} for t in texts]


def D(*names):
    return [B + n for n in names]


G_ORDER = {
    'statement': (
        'Let `Hexagram.order` be the received order and `RunsOrder next := ∀ i, i + 1 < 64 → '
        'next (order.getD i allBroken) = order.getD (i + 1) allBroken`. (a) For every local rule '
        '`ρ : Bool → Bool → Bool → Bool`, neither the law giving each line ρ of the line below, itself and '
        'the line above with the six places closed in a ring, nor the same law with the wrap read negated '
        '(as `waxWane` reads it), satisfies `RunsOrder`; none agrees with the order on more than 9 of its 63 '
        'steps. (b) For every permutation σ of the six places and every mask m, the law '
        '`s ↦ xor (permute σ s) m` does not satisfy `RunsOrder`; the most any agrees on is 28 steps '
        '(σ the reversal, m = 0), exactly the turned-over steps inside the pairs (`order_paired`). (c) The 31 '
        'steps between pairs change between 1 and 6 lines. All three by `decide`. With `exists_law_iff` and '
        '`Run.keepHistory_shown`: the order is a run only of the law it shows, which admits only it.'),
    'nearest': D('Hexagram.order_paired', 'Hexagram.order_paired_by_law', 'exists_law_iff',
                 'Run.keepHistory_shown', 'shown_le_iff'),
    'why_it_matters': (
        'It closes the open item of the Yi chapter (§8, why the order is as it is) with a checked negative: '
        'the 序卦 reasons are lawful inside the pairs and asserted between them. It is the strongest '
        'counterexample in this slice to reading the received text as relational law throughout, and it keeps '
        'the integrator from building a law of succession on the order.'),
}

G_HOUTIAN = {
    'statement': (
        'On the eight three-line configurations `Bool × Bool × Bool` (lines from the bottom), with '
        '震 = (t,f,f), 巽 = (f,t,t), 離 = (t,f,t), 坤 = (f,f,f), 兌 = (t,t,f), 乾 = (t,t,t), 坎 = (f,t,f), 艮 = (f,f,t): '
        '(a) the cycle 震→巽→離→坤→兌→乾→坎→艮→震 is a run of no map `s ↦ xor (permute σ s) m` (at most 4 of '
        'its 8 steps agree) and of no three-cell local rule, cyclic or with the wrap negated (at most 5 of 8); '
        '(b) of its four diametric pairs only (離, 坎) is a complement pair, while each pair of 說卦 ch. 3 '
        '(乾坤, 艮兌, 震巽, 坎離) is. By `decide`.'),
    'nearest': D('Hexagram.complement', 'Hexagram.order_paired', 'exists_law_iff'),
    'why_it_matters': (
        'Within one 傳, chapter 3 arranges the trigrams by the complement relation and chapter 5 by an '
        'assigned cycle of stations; the statement makes that difference checked rather than asserted, as '
        'for the received order.'),
}

G_ZAGUA = {
    'statement': (
        'Let `zagua : List Hexagram` be the 64 hexagrams in the order of 雜卦. (a) `zagua.length = 64` and '
        '`∀ s, s ∈ zagua`; (b) for i < 28, members 2i and 2i + 1 are related by `reverse` or `complement`, and '
        'these 28 unordered pairs with {大過, 頤}, {姤, 夬}, {漸, 歸妹}, {既濟, 未濟} are exactly the 32 '
        'unordered pairs of `pairs order`; (c) among the last eight members (大過 姤 漸 頤 既濟 歸妹 未濟 夬) '
        'no two adjacent members are related by `reverse` or `complement`, and the pair of each lies among '
        'the eight. By `decide`.'),
    'nearest': D('Hexagram.order_paired', 'Hexagram.Paired', 'Hexagram.both_fixed_iff', 'Hexagram.mem_order'),
    'why_it_matters': (
        'It shows that the second arrangement in the 傳 keeps the pairs and drops the order between them, '
        'which separates what the 傳 layer carries (the pairing, lawful) from what it arranges (the sequence, '
        'asserted), and locates the one place the pairing is broken up (the close).'),
}

G_PARITY = {
    'statement': (
        '(a) `∀ s, (yang (waxWane s) + yang s) % 2 = 1` and `∀ k s, (yang (flip k s) + yang s) % 2 = 1`; '
        '(b) `GoAlike (Law.process waxWane) (fun s => yang s % 2)` (by `Learning.goAlike_iff_lumped`), '
        'beside `yang_not_goAlike`; (c) `∀ s, phaseCount s % 2 = (yang s + 1) % 2`, so (a) for `waxWane` is '
        '`phaseCount_parity` read in the count of unbroken lines; (d) for the three lines of one half: the '
        'count of unbroken lines is odd exactly when the half is all unbroken or one line changed from all '
        'broken, and even exactly when it is all broken or one line changed from all unbroken. By `decide`.'),
    'nearest': D('Hexagram.yang_not_goAlike', 'Hexagram.phaseCount_parity', 'Learning.goAlike_iff_lumped',
                 'Hexagram.flip', 'Hexagram.pairs_goAlike'),
    'why_it_matters': (
        '繫辭下 ch. 3 classes the trigrams by parity (陽卦奇，陰卦偶), and 說卦 ch. 10 generates them by '
        'one-line changes (一索、再索、三索); the statement joins the two passages, shows that the parity '
        'carries law where the count (多陰、多陽) does not, and gives the hexagram law a second lumping beside '
        'the complement pairs.'),
}

G_GUABIAN = {
    'statement': (
        'Let `swap i j : Hexagram → Hexagram` exchange the lines at places i and j. (a) `yang (swap i j s) = '
        'yang s`; (b) with 泰 = `number 11`, 否 = `number 12`, 損 = `number 41`, 益 = `number 42`: '
        '`swap .p3 .p6 泰 = 損` (the unbroken line moves from the lower half to the upper: 損下益上), '
        '`swap .p1 .p4 否 = 益` (損上益下), `swap .p1 .p4 泰 = heng` (剛上而柔下), `swap .p3 .p6 否 = xian` '
        '(柔上而剛下); (c) the twenty configurations with three unbroken lines are 泰, 否 and the eighteen '
        'reached from them by one swap of a lower place with an upper place whose lines differ; (d) reading the '
        'unbroken lines of the lower and upper halves as the standings of two relata, each such swap is one '
        'balanced step of the exchange law (`World.exchange_step_iff`) moving one between them with the total '
        'kept. (a)–(c) by `decide`, (d) by instancing the exchange on a two-relatum world.'),
    'nearest': D('Hexagram.flip', 'World.exchange_step_iff', 'Flow.Balances.rise_given', 'Flow.Balances.fall_taken',
                 'Hexagram.yang'),
    'why_it_matters': (
        '卦變 is the other open item of the Yi chapter (§8). The 彖 states movements of lines between the '
        'halves (損下益上, 損上益下, and in 恒, 咸, 隨, 蠱, 賁, 渙 剛上/柔下/柔來); the swap is the one '
        'structure under which these statements are exact, and it makes 損 and 益 one exchange read from two '
        'ends, joining the hexagram line to the Flow base. The conservation is of the line count under the '
        'swap, a fact of the configurations, not a claim of the text (atlas HX-R013).'),
}

G_JIAO = {
    'statement': (
        'Define `meets s h := s.line (place .lower h) && !s.line (place .upper h)` (交 at height h: the '
        'unbroken value below, the broken above). Then `∀ h, meets (number 11) h = true` (泰) and '
        '`∀ h, meets (number 12) h = false` (否), while `∀ h, opposed (number 11) h = true ∧ opposed (number 12) h '
        '= true`. By `decide`.'),
    'nearest': D('Hexagram.opposed', 'Hexagram.oppositions_glue_iff', 'Hexagram.halves_glues_iff'),
    'why_it_matters': (
        '泰 and 否 are alike under every relation the spine states between the halves; the 彖’s 交/不交 '
        'separates them only by reading a direction into the two values. Stating it makes the added premise '
        'explicit. It belongs with the owners of the line relations (Y2–Y4).'),
}

G_NOREST = {
    'statement': (
        '`∀ s, waxWane s ≠ s`, and `∀ s, ¬ ∃ T, ∀ n, T ≤ n → (Law.run waxWane s).state (n + 1) = '
        '(Law.run waxWane s).state n`: no configuration is a rest of the law of waxing and waning, the '
        'completed one (既濟) included. From `six_steps` and `complement_moves` with `Law.rests_iff`.'),
    'nearest': D('Hexagram.six_steps', 'Hexagram.complement_moves', 'Law.rests_iff', 'Hexagram.waxWane_returns'),
    'why_it_matters': (
        'It states in one lemma what 既濟 "終止則亂" and Cheng Yi’s 无常止 claim of the hexagram world; the '
        'spine has it only through six_steps. Small.'),
}

ENTRIES = [
    # ---------------- 繫辭上傳 ----------------
    dict(
        id='xici-fanwei-buyi', tradition='易傳·繫辭上傳', atlas=A,
        atlas_ids=['JW-XCS-C04-S06', 'WP-XCS-C04-S06-R01'], source_id='DS02', text_path=T + 'DS02.txt',
        locator='繫辭上 第四章', fragments=['范围天地之化而不过，曲成万物而不遗', '故神无方而易无体'],
        repo_fragments=R(XS, '範圍天地之化而不過，曲成萬物而不遺', '故神无方而易无體'),
        kind='scope',
        declarations=D('Hexagram.mem_order', 'Hexagram.waxWane_returns', 'Hexagram.kept_history_unlisted',
                       'Law.withHistory_unlisted', 'Learning.no_prefix_fixes_next', 'Learning.diagonal_misses'),
        records=['hexagrams-on-the-spine', 'recurrence-without-premise', 'learning-by-refutation'],
        relational='易 is said to enclose the transformations of 天地 without exceeding them and to complete the ten thousand things without omission; what relates is the 易 (its configurations and law) and the unfolding it matches. 神无方而易无体 denies that change has one place or one body.',
        reading='AI读法：范围而不过、曲成而不遗，在脊柱上有确切的成立范围。六十四种组态都在受传卦序之中（Hexagram.mem_order），消息之律下每个组态都回来（waxWane_returns），所以"不遗"对组态成立。但保留历史的展开不被任何有限列表容纳（kept_history_unlisted、Law.withHistory_unlisted），任何由前缀作出的外推都在某个过程上落空（no_prefix_fixes_next、diagonal_misses）。所以此句对组态与律成立，对带着历史的展开与对后续之知不成立。"易无体"与此一致：律不是任何一个组态。没有断言：易的组态预先容纳一切实际进程。',
        reading_en='AI reading: the enclosure holds of configurations (all 64 are in the order and each returns under the law) but not of an unfolding that keeps its history, which no list holds, nor of knowing what follows from a prefix; 易无体 matches the law being no single configuration.',
        gap=None),
    dict(
        id='xici-xian-ren-cang-yong', tradition='易傳·繫辭上傳', atlas=A,
        atlas_ids=['JW-XCS-C05-S03', 'WP-XCS-C05-S03-R01'], source_id='DS02', text_path=T + 'DS02.txt',
        locator='繫辭上 第五章', fragments=['百姓日用而不知，故君子之道鲜矣', '显诸仁，藏诸用'],
        repo_fragments=R(XS, '百姓日用而不知，故君子之道鮮矣', '顯諸仁，藏諸用'),
        kind='scope',
        declarations=D('ExchangeLaw.Through.crosses_of_unobserved', 'crossing_passes_iff',
                       'not_not_obs_iff_respondsByLevel', 'Web.observed_level_couples', 'Web.break_not_bounded'),
        records=['where-a-level-couples', 'runaway-distance-unregistered', 'testing-within-registration'],
        relational='What is used and what is registered come apart: the way shows in its effects (显诸仁) and is held in its working (藏诸用); those who act through it daily do not register it. The relation is between a formation and conditions it acts through but does not read.',
        reading='AI读法：脊柱给出"日用而不知"的确切范围。一个形成可以对它不按水平读入的条件作出响应，这种响应只是越过阈值（crosses_of_unobserved、crossing_passes_iff）；按水平读入才把差异传进来（observed_level_couples）；条件不按水平耦合时，断裂之前没有任何读入的东西界定离断裂多远（break_not_bounded）。所以"用而不知"在脊柱上是：通过一个耦合行动而不按水平读入它。明（看见自己所通过的耦合）就是把这条耦合读进来。句子没有断言不知者不受其影响，也没有断言知了就能免于断裂。',
        reading_en='AI reading: "used daily without knowing" is acting through a condition not coupled in by level, so it passes only as a crossing and nothing read bounds the distance to a break; 明 would be reading that coupling in. Knowing it is not claimed to prevent the break.',
        gap=None),
    dict(
        id='xici-qiankun-hui', tradition='易傳·繫辭上傳', atlas=A,
        atlas_ids=['JW-XCS-C12-S03', 'XC-R004', 'WP-XCS-C12-S03-R01'], source_id='DS02', text_path=T + 'DS02.txt',
        locator='繫辭上 第十二章', fragments=['乾坤毁，则无以见易，易不可见，则乾坤或几乎息矣'],
        repo_fragments=R(XS, '乾坤毀，則无以見易，易不可見，則乾坤或幾乎息矣'),
        kind='agreement',
        declarations=D('Law.alike_iff_sameFuture', 'Twins.naming_not_identifiesAlike', 'Alike.tests',
                       'Hexagram.complement_moves', 'Hexagram.waxWane_apart'),
        records=['configurations-alike-by-relation', 'what-a-commuting-law-keeps-apart', 'process-and-frame-as-readings'],
        relational='A two-way dependence: change is seen only through the arrayed contrast of 乾 and 坤, and the contrast nearly ceases where no change shows it. Neither the contrast nor the change is prior.',
        reading='AI读法：后半句与脊柱的已检查之律同构：在确定之律下，两个组态相似当且仅当它们经由读法的未来相同（Law.alike_iff_sameFuture），相似者通过同样的测试（Alike.tests），给两个处处相似的后继起名不成立（Twins.naming_not_identifiesAlike）；一个没有任何变化显示出来的区分，作为区分就"几乎息"了。前半句：互补是使每个组态都移动的对立（complement_moves），消息之律下一个组态与其互补永不合一（waxWane_apart），区分靠变化保持。朱熹本义把"毁"读为卦画不立、"息"读为变化不行，是注层。没有断言乾坤是两种先在的实体（atlas XC-R004 的限制同此）。',
        reading_en='AI reading: the second clause has the structure of Law.alike_iff_sameFuture: a distinction no future shows is no distinction; the first matches that the complement moves every configuration and the law never brings a configuration and its complement together. No two prior substances are asserted.',
        gap=None),
    dict(
        id='han-dao-wu-zhi-cheng', tradition='注·韓康伯（繫辭注，周易正義所載）', atlas=A,
        atlas_ids=['WH-R023', 'YCM130-H4-H-09-R01'], source_id='YWH-H4', text_path=T + 'YWH-H4.txt',
        locator='周易正義 繫辭上 卷七之四，韓注「故神無方，而易無體」「一陰一陽之謂道」',
        fragments=['方、體者，皆繫於形器者也', '道者何？無之稱也，無不通也，無不由也，況之曰道',
                   '陰陽雖殊，無一以待之。在陰為無陰，陰以之生；在陽為無陽，陽以之成'],
        kind='scope',
        declarations=D('World.unity', 'exists_law_iff', 'shown_le_iff', 'Web.change_readings', 'Frame.arises_iff'),
        records=['unity-of-readings', 'process-and-frame-as-readings', 'worlds-are-runs', 'coming-and-ceasing-keep-pace'],
        relational='Han Kangbo separates place and body, which belong to formed things (形器), from 道, which he names 無: no thing, that through which everything passes. The relational point (道 is no formation) is joined to a non-relational one: yin and yang wait on a 一 that is 無 and are generated by it.',
        reading='AI读法：前两句在脊柱上有确切范围：律不是任何组态，而是从历史读出、该历史作为其运行的最小律（shown_le_iff），一个历史有确定之律接纳当且仅当它自洽（exists_law_iff），每个世界是交换律的一个运行（World.unity），生起与止息是同一变化从活动读出（Web.change_readings、Frame.arises_iff）。所以"道非形器，无不通、无不由"可以读成：律不在组态之中，而是一切运行所通过的。超出范围的是第三句：阴阳"待"一个"无之一"，"阴以之生、阳以之成"，给了不是关系项的东西以生成之功；脊柱没有这一项，生起只在运行之内读出。孔疏随即补"道虽无于阴阳，然亦不离于阴阳"，是疏层的收回。注层，不回填为系辞原义（atlas WH-R023）。',
        reading_en='AI reading: "道 is no formation and everything passes through it" fits the spine: the law is no configuration but the least law a history runs by, and every world is one run. The third clause exceeds it: a 無 that yin and yang wait on and are generated by; on the spine arising is read within the run.',
        gap=None),
    dict(
        id='han-you-shi-yu-wu', tradition='注·韓康伯（繫辭注，周易正義所載）', atlas=A,
        atlas_ids=['WH-R025', 'WH-R024', 'WH-N049', 'WH-N050'], source_id='YWH-H11', text_path=T + 'YWH-H11.txt',
        locator='周易正義 繫辭上 卷七之十一，韓注「易有太極，是生兩儀」',
        fragments=['夫有必始於無，故太極生兩儀也', '太極者，無稱之稱，不可得而名'],
        kind='divergence',
        declarations=D('Frame.arises_iff', 'Frame.novel_iff_arises', 'Web.change_readings', 'World.unity',
                       'Run.keepHistory_shown'),
        records=['process-and-frame-as-readings', 'unity-of-readings', 'coming-and-ceasing-keep-pace'],
        relational='A one-way priority: being (有) must begin from non-being (無), and 太極 names that beginning; the two 儀 come after and from it. The relation runs from a ground that is not itself related.',
        reading='AI读法：这是本切片最清楚的非关系线索之一："有必始于无"是一个本体上的先行，在两仪之前，而不是两仪之间的关系。脊柱的结构与之不同：新的东西生起，就是关系项在运行中生起（Frame.arises_iff、Frame.novel_iff_arises）；生起与止息是同一变化的读法（Web.change_readings）；每个世界是一个运行（World.unity）。脊柱里没有一个在运行之外、无关系的起点让"有"从中开始。系辞原句（已有图谱 taiji，scope）不承担此义；分歧在韩注加上的"有始于无"（atlas WH-R025 亦注明非经文明说）。不当作王弼略例（Y4）。',
        reading_en='AI reading: "being must begin from non-being" gives an unrelated ground priority over the relations; on the spine arising is a relatum arising within the run and every world is one run, with no non-relatum to begin from. The divergence is in the commentary layer, not in the 繫辭 line (taiji, scope).',
        gap=None),
    dict(
        id='kong-taiji-yuanqi', tradition='疏·孔穎達（周易正義）', atlas=A,
        atlas_ids=['WH-R029', 'WH-N057', 'WH-N058'], source_id='YWH-H11', text_path=T + 'YWH-H11.txt',
        locator='周易正義 繫辭上 卷七之十一，疏「易有太極」',
        fragments=['太極謂天地未分之前，元氣混而為一，即是太初、太一也'],
        kind='divergence',
        declarations=D('World.unity', 'Web.change_readings', 'Frame.arises_iff', 'Law.alike_iff_sameFuture'),
        records=['unity-of-readings', 'configurations-alike-by-relation', 'process-and-frame-as-readings'],
        relational='Kong Yingda reads 太極 as a state before 天地 divided: 元氣 mixed into one, a stuff prior to the differentiation, from which the two 儀 come when it divides. Relations come after a prior undifferentiated stuff.',
        reading='AI读法：这是"先在之质"的读法：天地未分之前有一团混一的元气，分了才有天地。它与脊柱在两处不同。其一，元气是先于关系的质料，而脊柱的关系项与关系同出于一个运行（World.unity），生起只是活动从无到有的读法（Web.change_readings、Frame.arises_iff）。其二，按 Law.alike_iff_sameFuture，一个状态只能以其未来之别被区分；若它"混而为一"到没有任何未来之别，就不能由自身分出两仪，要分，区分已在关系之中。疏层，与韩注"无称之称"分层保存（atlas WH-R029）；系辞原句不承担这一读法；朱熹本义"大极者其理也"（第四十七条）读法亦不同。',
        reading_en='AI reading: a prior undifferentiated stuff that later divides is a prior substance; on the spine relata and relations come out of one run, and a state with no difference of future cannot by itself yield two. The 疏 layer, not the 傳 line.',
        gap=None),
    # ---------------- 繫辭下傳 ----------------
    dict(
        id='xici-tonggui-shutu', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C04-S01', 'WP-XCX-C04-S01-R01'], source_id='DS03', text_path=T + 'DS03.txt',
        locator='繫辭下（本版第四章）「憧憧往來」節', fragments=['天下同归而殊途，一致而百虑'],
        repo_fragments=R(XX, '天下同歸而殊途，一致而百慮'),
        kind='scope',
        declarations=D('Law.Merges.not_both_return', 'Law.Commutes.not_drawn_to_one', 'Law.Commutes.breaks',
                       'Hexagram.wane_breaks', 'Hexagram.basin_counts', 'Hexagram.qian_not_reach_jiJi'),
        records=['attraction-is-not-returning', 'what-a-commuting-law-keeps-apart', 'hexagram-world-laws'],
        relational='Many routes, one return; one point reached, a hundred deliberations: different starts relate through the place they come to.',
        reading='AI读法：脊柱给"同归而殊途"确切范围。不同的起点到达同一处是合并，合并的两者不能都回来（Law.Merges.not_both_return）：同归必有所失。与互补相容之律不把每个运行引到一处（Commutes.not_drawn_to_one）；要把一个组态与其互补合并，律必须破坏对称（Commutes.breaks、wane_breaks），只消之律把一切引入坤即如此。卦的世界里，互卦之律与互补相容而有损：十六个组态归乾、十六归坤、三十二归既济未济之转（basin_counts），是"殊途同归"的确切实例，但归处有三，不是一；消息之律无损，从乾到不了既济（qian_not_reach_jiJi），那里没有同归。所以此句对有损之律成立，不是普遍的。没有断言同归之处是先在的目标。',
        reading_en='AI reading: converging from different routes is merging, which loses return; a law compatible with the complement draws no run to one place, and merging a configuration with its complement breaks the symmetry. The nuclear law gives an exact instance (16, 16, 32 basins, three places, not one); the lossless law of waxing and waning has none. The passage holds for lossy laws only.',
        gap=None),
    dict(
        id='xici-chihuo-longshe', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C04-S03', 'WP-XCX-C04-S03-R04'], source_id='DS03', text_path=T + 'DS03.txt',
        locator='繫辭下（本版第四章）「憧憧往來」節', fragments=['尺蠖之屈，以求信也。龙蛇之蛰，以存身也'],
        repo_fragments=R(XX, '尺蠖之屈，以求信也。龍蛇之蟄，以存身也'),
        kind='scope',
        declarations=D('Web.waking_not_arising', 'Dormancy.held_both', 'Web.Carries.lasts_within',
                       'Web.Carries.ends_within', 'Web.unsupported_after_loss'),
        records=['identity-across-steps', 'reserve-defers-ending'],
        relational='Contraction for extension, dormancy for keeping the body: a formation relates to its own later activity through a withdrawn stretch.',
        reading='AI读法：已有图谱 riyue 映射了"屈信相感而利生"；这里加的是"蛰以存身"的范围。醒来不是生起：在一步之前持续的形成不在这一步生起（waking_not_arising）；但隔着一个什么都不持续的休眠步，把前后接为同一个只是一种读法，它改变早期形成的类（Dormancy.held_both）。有储备 k 时，失去支持的形成此后至多活跃 k 次（Carries.lasts_within），储备衰减时在储备耗尽前停止（Carries.ends_within）；依赖不变而损失无回，此后不再被支持（unsupported_after_loss）。所以"蛰以存身"在储备的界限内成立，蛰不是无界的保存。句子没有说蛰多久仍能存身。',
        reading_en='AI reading: waking is not arising, but dormancy keeps a formation only within its reserve (at most k active steps once unsupported), and joining the early and late formation across a dormant step is a reading; 蛰以存身 holds within that bound.',
        gap=None),
    dict(
        id='xici-shan-buji', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C04-S08', 'WP-XCX-C04-S08-R01', 'WP-XCX-C04-S08-R02', 'WP-XCX-C04-S08-R03'],
        source_id='DS03', text_path=T + 'DS03.txt', locator='繫辭下（本版第四章）「善不積」節',
        fragments=['善不积不足以成名，恶不积不足以灭身', '以小恶为无伤而弗去也', '故恶积而不可揜，罪大而不可解'],
        repo_fragments=R(XX, '善不積不足以成名，惡不積不足以滅身', '以小惡為无傷而弗去也', '故惡積而不可揜，罪大而不可解'),
        kind='scope',
        declarations=D('break_carried_nowhere', 'Thresholds.Draw.forms_at_break', 'Thresholds.Draw.diverges_at_break',
                       'Law.DrawnInto.never_back', 'Web.unsupported_after_loss', 'Hexagram.waxWane_returns'),
        records=['loops-within-what-a-law-reads', 'necessarily-drawn-is-not-returning', 'reserve-defers-ending'],
        relational='Small steps relate to a later state through accumulation: each small wrong looks harmless because nothing shows it, and the sum crosses into a state that cannot be undone.',
        reading='AI读法：前半与脊柱一致：对一个只在阈值以下读入存量的律，断裂之前两条只在该存量上不同的过程处处相同（break_carried_nowhere），回路在断裂处才形成（forms_at_break），差异只在断裂之后显出（diverges_at_break）；"以小恶为无伤"正是阈值以下读不出差别。后半"不可解"需要范围：被吸入吸收区的不再回来（DrawnInto.never_back），依赖不变而损失无回则此后不再被支持（unsupported_after_loss）；但在无损之律下每个组态都回来（waxWane_returns）。所以"罪大而不可解"只在有吸收区或无回之损时成立，不是普遍之律。善恶的评价不由这些律给出。',
        reading_en='AI reading: the accumulation half matches the threshold laws (below the threshold the difference is carried nowhere and shows only after the break); "cannot be undone" holds only where there is an absorbing region or a loss without return, not under a lossless law.',
        gap=None),
    dict(
        id='xici-an-buwang-wei', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C04-S09', 'WP-XCX-C04-S09-R01', 'WP-XCX-C04-S09-R02'], source_id='DS03',
        text_path=T + 'DS03.txt', locator='繫辭下（本版第四章）「危者安其位」節；（本版第八章）「其辭危」節',
        fragments=['危者，安其位者也', '是故君子安而不忘危，存而不忘亡，治而不忘乱', '危者使平，易者使倾'],
        repo_fragments=R(XX, '危者，安其位者也', '是故君子安而不忘危，存而不忘亡，治而不忘亂', '危者使平，易者使傾'),
        kind='scope',
        declarations=D('Web.break_not_bounded', 'Web.observed_raise_couples', 'Flow.policy_uses_after_failure',
                       'Web.tail_unexcluded', 'Law.rests_iff'),
        records=['runaway-distance-unregistered', 'testing-within-registration', 'seeking-boundary'],
        relational='Security and danger are one relation read at two times: the one who rests in place is the one in danger. Keeping danger in view relates the present secure state to a break it does not show.',
        reading='AI读法：脊柱给出"安而不忘危"何以必要、又何以不充分。条件不按水平耦合时，断裂之前没有读入的东西界定离断裂多远（break_not_bounded）；按水平耦合则任何抬升都立刻被读出（observed_raise_couples）；经由耦合的策略只在失败之后才动用更大的存量（policy_uses_after_failure）。所以"不忘危"在脊柱上是把存量按水平读进来，而不是等待失败。但没有模型时，有限前缀不排除任何后续（tail_unexcluded），读进来也不保证不倾。"危者使平，易者使倾"是读入与稳定之间的关系，脊柱只给出读入的一半。',
        reading_en='AI reading: not forgetting danger is coupling the stock in by level, since otherwise nothing bounds the distance to the break and a policy uses reserves only after a failure; registration is necessary, not sufficient, since without a model a finite prefix excludes no tail.',
        gap=None),
    dict(
        id='xici-debo-weizun', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C04-S10', 'WP-XCX-C04-S10-R01', 'WP-XCX-C04-S10-R02'], source_id='DS03',
        text_path=T + 'DS03.txt', locator='繫辭下（本版第四章）「德薄而位尊」節',
        fragments=['德薄而位尊，知小而谋大，力小而任重，鲜不及矣', '言不胜其任也'],
        repo_fragments=R(XX, '德薄而位尊，知小而謀大，力小而任重，鮮不及矣', '言不勝其任也'),
        kind='agreement',
        declarations=D('Web.supported_iff_admits', 'Web.Admits', 'Flow.beyond_given_bounded', 'Flow.takesAll_of_more',
                       'Flow.Balances.consumption_ends_with_feeders'),
        records=['closing-needs-net-draw', 'where-a-rising-take-ends', 'consumption-ends-with-feeders'],
        relational='A load relates to the capacity that bears it: what is required (位, 謀, 任) against what stands (德, 知, 力). The verdict is a relation between the two, not a property of either.',
        reading='AI读法：结构是"要求超过所立之水平"。脊柱：支持就是被所立之水平接纳，即满足每一项要求（Web.supported_iff_admits、Web.Admits）；在平衡下，取多于所给不能持续（beyond_given_bounded），不断上升的取终将取尽所给（takesAll_of_more），喂养者都失去支持时消耗至多持续该存量那么多步（consumption_ends_with_feeders）。"鲜不及矣"与这些律同构：要求高于能承载者，不能长久。位、尊这些等级词不采纳，只取"要求对水平"。没有断言德厚者必得其位。',
        reading_en='AI reading: a requirement above the standing level: support is admission by the levels that stand, and taking beyond what is given cannot last. The rank vocabulary (位, 尊) is not adopted; only the requirement–level relation is.',
        gap=None),
    dict(
        id='xici-biantong-qushi', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C01-S03', 'XC-R035', 'XC-N037'], source_id='DS03', text_path=T + 'DS03.txt',
        locator='繫辭下 第一章', fragments=['刚柔者，立本者也；变通者，趣时者也'],
        repo_fragments=R(XX, '剛柔者，立本者也；變通者，趣時者也'),
        kind='scope',
        declarations=D('Pace.rule_kept', 'Pace.rule_at_reading', 'Pace.rule_alike_until_reading',
                       'Switching.fixed_loses', 'Switching.changing_regains', 'Contextual.indexed_fits'),
        records=['how-fast-a-rule-may-change', 'contextual-registration'],
        relational='Two levels: the two values (剛柔) stand as the base on which change runs; the change and its passing (變通) follow the time. The rule relates to the moment it reads.',
        reading='AI读法：这是两层之律：快的一层是组态，慢的一层是规则。脊柱：从不读取的规则每步保持（rule_kept）；在读取步，下一条规则由那里的快组态给出（rule_at_reading）；第一次读取之前，快组态的差异到不了规则（rule_alike_until_reading）。固定的规则从第一步起就失去一个组态（Switching.fixed_loses），随时变化的规则把每个固定规则失去的重新取得（changing_regains）。"变通趣时"对应规则读取快层而变，"立本"对应值的基底。范围：变通只在规则读取之处发生，读取之间规则不变；时不是独自造成变化的东西（atlas XC-R035）。',
        reading_en='AI reading: a two-level law, configurations below and a rule above; a rule that changes by reading the fast level regains what each fixed rule loses, and changes only at reading steps. 趣时 holds where the rule reads the moment, not as a fixed timetable.',
        gap=None),
    dict(
        id='xici-yanggua-qi', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['JW-XCX-C03-S02', 'WP-XCX-C03-S02-R01'], source_id='DS03', text_path=T + 'DS03.txt',
        locator='繫辭下 第三章', fragments=['阳卦多阴，阴卦多阳，其故何也？阳卦奇，阴卦偶'],
        repo_fragments=R(XX, '陽卦多陰，陰卦多陽，其故何也？陽卦奇，陰卦偶'),
        kind='scope',
        declarations=D('Hexagram.yang', 'Hexagram.yang_not_goAlike', 'Hexagram.phaseCount_parity', 'Hexagram.flip',
                       'Learning.goAlike_iff_lumped', 'Hexagram.pairs_goAlike'),
        records=['hexagrams-on-the-spine', 'place-relations-in-context', 'generalization-through-lumping'],
        relational='The trigrams are classed by a relation among their lines: 陽卦 (乾 震 坎 艮) have an odd count of unbroken lines, 陰卦 (坤 巽 離 兌) an even one; counting strokes, a broken line as two, gives the same parity. The class is a relation of three lines, not an essence.',
        reading='AI读法：计算核对：震坎艮各一阳二阴、乾三阳，阳爻数奇；巽离兑各二阳、坤零阳，偶；以笔画计（阴爻两画）奇偶相同。脊柱上，阳爻之数本身不是消息之律通行的归并（yang_not_goAlike），但其奇偶是：每一步消息、每一次一爻之变都改变奇偶。这在 phaseCount_parity 中以"当位之数"的坐标已证，二者只差一个恒等式（当位数 ≡ 阳爻数 + 1 mod 2），所以奇偶两类是律通行的归并（理）。于是此句的"多阴/多阳"（数）不承载律，"奇/偶"（奇偶）承载，这是范围的修正。三爻层面的陈述与阳爻数的陈述脊柱尚无，见 gap。',
        reading_en='AI reading: the trigram classes are the parity of the unbroken-line count; the count is not a lumping the law goes alike across, but its parity is, changing at every step and every one-line change (proved as phaseCount_parity in another coordinate). 奇/偶 carries law where 多/少 does not.',
        gap=G_PARITY),
    dict(
        id='xici-yijun-ermin', tradition='易傳·繫辭下傳', atlas=A,
        atlas_ids=['WP-XCX-C03-S02-R02', 'WP-XCX-C03-S02-R03'], source_id='DS03', text_path=T + 'DS03.txt',
        locator='繫辭下 第三章', fragments=['阳一君而二民，君子之道也；阴二君而一民，小人之道也'],
        repo_fragments=R(XX, '陽一君而二民，君子之道也；陰二君而一民，小人之道也'),
        kind='divergence',
        declarations=D('Hexagram.waxWane_complement', 'Law.Commutes.rest_paired', 'Hexagram.changes_symmetric',
                       'Web.significance_undetermined'),
        records=['what-a-commuting-law-keeps-apart', 'one-axiom-yields-g0'],
        relational='The same line count is read as a ruling relation: one 君 and two 民 is the way of the 君子, two 君 and one 民 that of the 小人. A structural parity is turned into a hierarchy and a moral rank.',
        reading='AI读法：奇偶是结构（见上一条），"一君二民为君子之道"则是把计数读成统治关系并赋予道德等级。脊柱：消息之律与互补交换（waxWane_complement），一爻之变在互补下对称（changes_symmetric），静止成对出现（Commutes.rest_paired），没有律使阳或阴、少数或多数处于支配位置；动力学本身也不决定意义（significance_undetermined）。所以此读法是加上去的等级，不是关系所给的。这是"固定等级"的反例，保留为分歧。',
        reading_en='AI reading: the parity is structure; reading one-ruler-two-subjects as the way of the 君子 adds a hierarchy and a moral rank that no law of the configurations gives (the law commutes with the complement; the dynamics fix no significance).',
        gap=None),
    # ---------------- 說卦傳 ----------------
    dict(
        id='shuogua-tiandi-dingwei', tradition='易傳·說卦傳', atlas=A,
        atlas_ids=['JW-SG-C03-S01', 'WP-SG-C03-S01-R01', 'OW-N004'], source_id='YD-OW-SG', text_path=T + 'YD-OW-SG.txt',
        locator='說卦 第三章；第六章',
        fragments=['天地定位，山澤通氣，雷風相薄，水火不相射。八卦相錯', '故水火相逮，雷風不相悖，山澤通氣，然後能變化，既成萬物也'],
        repo_fragments=R(SG, '天地定位，山澤通氣，雷風相薄，水火不相射。八卦相錯', '故水火相逮，雷風不相悖，山澤通氣，然後能變化，既成萬物也'),
        kind='agreement',
        declarations=D('Hexagram.complement', 'Hexagram.opposed', 'Hexagram.oppositions_glue_iff',
                       'Hexagram.halves_no_free_frame', 'Hexagram.xian_opposed', 'Hexagram.heng_opposed',
                       'Hexagram.weiJi_opposed', 'Hexagram.waxWane_complement'),
        records=['place-relations-in-context', 'what-a-commuting-law-keeps-apart'],
        relational='Four pairs of trigrams (天地, 山澤, 雷風, 水火), each a trigram and its line-by-line opposite, are said to stand, pass, press and not repel each other; change and the completion of things come through the pairs relating, not through any one trigram.',
        reading='AI读法：计算核对：四对恰是三爻层面的四对互补（乾坤、艮兑、震巽、坎离）。把一对上下相叠，得到每个高度都"对"的八卦：泰否咸损恒益既济未济。脊柱已证：三个高度上的"对"恰在每个高度都对（上下卦互补）或都不对（重卦）时粘合（oppositions_glue_iff），没有无上下文的断言之框适合这些高度（halves_no_free_frame），咸、恒、未济每个高度皆对（xian_opposed、heng_opposed、weiJi_opposed）。"相错"在这里是互补，不是相斥；消息之律与互补交换（waxWane_complement）。"然后能变化"的因果句脊柱未证，一致的只是配对结构。',
        reading_en='AI reading: the four pairs are exactly the four trigram complements; stacked they give the eight hexagrams opposed at every height, where the oppositions glue; 相錯 is the complement relation, which the law commutes with. The causal "然後能變化" is not proved, only the pairing.',
        gap=None),
    dict(
        id='shuogua-shuwang-zhilai', tradition='易傳·說卦傳', atlas=A,
        atlas_ids=['JW-SG-C03-S02', 'OW-R012'], source_id='YD-OW-SG', text_path=T + 'YD-OW-SG.txt',
        locator='說卦 第三章', fragments=['數往者順，知來者逆。是故易逆數也'],
        repo_fragments=R(SG, '數往者順，知來者逆。是故易逆數也'),
        kind='scope',
        declarations=D('Retrodiction.actual_candidate', 'Retrodiction.reading_right_iff', 'Retrodiction.change_unlocated',
                       'Learning.no_prefix_fixes_next', 'Learning.diagonal_misses', 'Law.alike_iff_sameFuture'),
        records=['historical-source-binding', 'learning-by-refutation', 'wisdom-root-part-one'],
        relational='An asymmetry between two directions of reading: counting what has gone follows the course; knowing what comes goes against it.',
        reading='AI读法：脊柱给出两个方向各自的界限。往：实际历史总是候选（actual_candidate），读对一个早先的内容当且仅当其他给出相同记录的历史都被某个控制分开（reading_right_iff），两端之间的变化不被两端的控制定位（change_unlocated），"数往"顺但不是无条件的。来：没有前缀确定下一个值（no_prefix_fixes_next），每种外推在其对角过程上都落空（diagonal_misses），只有有了律，未来才由组态与律确定（alike_iff_sameFuture）。所以"知来者逆"在脊柱上是：知来要有律，不能从已往的前缀读出。没有断言占筮能知来（atlas OW-R012）。已有图谱 jishu-zhilai（极数知来之谓占）相邻。',
        reading_en='AI reading: reading the past is bounded by controls (the actual history is a candidate; a change between two controls is unlocated); knowing the future needs the law, since no prefix fixes the next value. No claim about divination is made.',
        gap=None),
    dict(
        id='shuogua-di-chu-zhen', tradition='易傳·說卦傳', atlas=A,
        atlas_ids=['JW-SG-C05-S01', 'OW-R045', 'WP-SG-C05-S01-R01'], source_id='YD-OW-SG', text_path=T + 'YD-OW-SG.txt',
        locator='說卦 第五章',
        fragments=['帝出乎震，齊乎巽，相見乎離，致役乎坤，說言乎兌，戰乎乾，勞乎坎，成言乎艮', '萬物出乎震，震，東方也',
                   '戰乎乾，乾，西北之卦也。言陰陽相薄也'],
        repo_fragments=R(SG, '帝出乎震，齊乎巽，相見乎離，致役乎坤，說言乎兌，戰乎乾，勞乎坎，成言乎艮', '萬物出乎震，震，東方也'),
        kind='divergence',
        declarations=D('Hexagram.complement', 'Hexagram.order_paired', 'exists_law_iff', 'Run.keepHistory_shown',
                       'shown_le_iff'),
        records=['place-relations-in-context', 'histories-fix-law-up-to-dead-ends', 'process-and-frame-as-readings'],
        relational='A cycle of the eight trigrams through stations and seasons. The 傳 itself glosses 帝 as the ten thousand things coming forth (萬物出乎震) and 戰 as yin and yang pressing on each other (陰陽相薄), so its glosses are relational; the assignment of trigrams to stations is asserted.',
        reading='AI读法：两点。其一，传文自己把"帝"解为万物之出、把"战"解为阴阳相薄，是关系的，"帝出"不应读成一个意志之主。其二，八卦的这个循环是指派，不是由组态关系导出：计算核对，震→巽→离→坤→兑→乾→坎→艮→震不是任何"置换各爻并加掩码"之律的运行（最多合 4/8 步），也不是任何三格局部规则（循环或扭转）的运行（最多 5/8）；圆上四对对位中只有离坎互补，而第三章的四对全是互补。所以同一传中第三章的排列承载互补之结构，第五章的不承载。按 exists_law_iff，这个循环当然是它自己所显之律的运行，但那条律只接纳这一历史（Run.keepHistory_shown）。方位时令的配属不评价（atlas OW-R045 不把它与后世先后天图等同）。',
        reading_en='AI reading: the 傳 glosses 帝 and 戰 relationally (things coming forth, yin and yang pressing), so no personal will is asserted; but the cycle is assigned, not derived: it is a run of no place-permutation-with-mask law and no three-cell local rule, and only one of its four diametric pairs (離坎) is a complement, whereas every pair of chapter 3 is.',
        gap=G_HOUTIAN),
    dict(
        id='shuogua-yi-suo', tradition='易傳·說卦傳', atlas=A,
        atlas_ids=['JW-SG-C10-S03', 'WP-SG-C10-S03-R01'], source_id='YD-OW-SG', text_path=T + 'YD-OW-SG.txt',
        locator='說卦 第十章',
        fragments=['震一索而得男，故謂之長男；巽一索而得女，故謂之長女', '坎再索而得男，故謂之中男；離再索而得女，故謂之中女',
                   '艮三索而得男，故謂之少男；兌三索而得女，故謂之少女'],
        repo_fragments=R(SG, '震一索而得男，故謂之長男；巽一索而得女，故謂之長女', '坎再索而得男，故謂之中男；離再索而得女，故謂之中女',
                         '艮三索而得男，故謂之少男；兌三索而得女，故謂之少女'),
        kind='agreement',
        declarations=D('Hexagram.flip', 'Hexagram.flip_complement', 'Hexagram.changes_symmetric',
                       'Hexagram.complement_moves', 'Hexagram.changes'),
        records=['what-a-commuting-law-keeps-apart', 'hexagrams-on-the-spine'],
        relational='The six trigrams other than 乾 and 坤 are generated from those two by one change at the first, second or third place: 震 坎 艮 from 坤, 巽 離 兌 from 乾. The two generated at one place are a complement pair.',
        reading='AI读法：一索、再索、三索是在第一、二、三位改变一爻：从坤得震坎艮，从乾得巽离兑；同一索之二恰是互补对（震巽、坎离、艮兑）。脊柱在六爻层面有同一结构：改变一爻与互补交换（flip_complement：在 k 位改变互补者之一爻，等于改变一爻后取互补），一爻之变的过程在互补下对称（changes_symmetric）。所以"索"的生成与互补配对是同一个关系。父母男女的称呼不采纳为结构名；三爻层面的陈述脊柱尚无（与 xici-yanggua-qi 的奇偶 gap 相连：从坤一索者阳爻数奇）。',
        reading_en='AI reading: 索 is a one-line change at place 1, 2 or 3 of 坤 or 乾; the two generated at one place are complements, which is flip_complement (changing a line commutes with the complement). The kinship names are not adopted as structural names.',
        gap=None),
    dict(
        id='shuogua-xiang-lei', tradition='易傳·說卦傳', atlas=A,
        atlas_ids=['JW-SG-C11-S01', 'WP-SG-C11-S01-R01'], source_id='YD-OW-SG', text_path=T + 'YD-OW-SG.txt',
        locator='說卦 第十一章', fragments=['乾為天、為圜、為君、為父', '坤為地、為母、為布、為釜'],
        kind='divergence',
        declarations=D('Learning.goAlike_iff_lumped', 'Learning.Lumped', 'Hexagram.pairs_goAlike',
                       'Hexagram.yang_not_goAlike', 'Law.alike_iff_sameFuture'),
        records=['generalization-through-lumping', 'hexagrams-on-the-spine', 'configurations-alike-by-relation'],
        relational='Open lists of images attached to each trigram (sky, round, ruler, father; earth, mother, cloth, cauldron). What relates them is the asserted association, not a relation stated among the images.',
        reading='AI读法：脊柱上，一种归类承载律，当且仅当律在它所归并的东西之间通行（goAlike_iff_lumped）：互补之对是这样的归并（pairs_goAlike），阳爻之数不是（yang_not_goAlike）。第十一章的象列没有给出任何律在"为君、为父、为玉、为金"之间通行；它们是取象的约定，不是从组态关系读出的理。这里不否认象的用处，只说它们是断言的对应，不是导出的结构；"为君、为父"又把等级与亲属带入卦，不采纳。Y1 的说卦存本无第十一章。',
        reading_en='AI reading: a classing carries law only where the law goes alike across it (as across the complement pairs, not across the line count); the image lists assert associations no law goes alike across. Asserted, not derived.',
        gap=None),
    # ---------------- 序卦傳 ----------------
    dict(
        id='xugua-within-pairs', tradition='易傳·序卦傳', atlas=A,
        atlas_ids=['JW-XG-C01-S23', 'OW-R035', 'JW-XG-C01-S11', 'OW-R034', 'JW-XG-C02-S12', 'OW-R037'],
        source_id='YD-OW-XG', text_path=T + 'YD-OW-XG.txt', locator='序卦 上篇（剝、泰）；下篇（損）',
        fragments=['物不可以終盡，剝窮上反下，故受之以復', '物不可以終通，故受之以否', '損而不已，必益，故受之以益'],
        repo_fragments=R(XG, '物不可以終盡，剝窮上反下，故受之以復', '物不可以終通，故受之以否', '損而不已，必益，故受之以益'),
        kind='agreement',
        declarations=D('Hexagram.reverse', 'Hexagram.Paired', 'Hexagram.order_paired', 'Hexagram.order_paired_by_law',
                       'Hexagram.both_fixed_iff', 'Hexagram.reverse_waxWane'),
        records=['hexagrams-on-the-spine', 'hexagram-world-laws'],
        relational='Within each pair of the order, the second hexagram is the first turned over, or, where turning over changes nothing, changed in every line; the 序卦 reason "a thing cannot end in X" names that turn.',
        reading='AI读法：序卦用"物不可（以）终X / 不可穷"十一次。计算核对：其中七次落在一对之内（终通 泰→否、终尽 剥→复、终遁 遁→大壮、终难 蹇→解、终动 震→艮、终离 涣→节、不可穷 既济→未济），后卦都是前卦翻转或全变（order_paired、order_paired_by_law）。"剥穷上反下"字面就是翻转：剥唯一的阳爻在上，翻过来在下，即复；损翻转即益。翻转把律倒过来走（reverse_waxWane）。所以序卦在对内所说的"不可终"与律有确切对应。泰否、既济未济既是翻转又是全变（both_fixed_iff）。没有断言每个通都必转为否（atlas OW-R034）。',
        reading_en='AI reading: seven of the eleven "cannot end in X" steps fall inside a pair, where the next hexagram is the first turned over or changed in every line (order_paired); 剝窮上反下 names the turn literally (剝 turned over is 復). This part of 序卦 is lawful.',
        gap=None),
    dict(
        id='xugua-between-pairs', tradition='易傳·序卦傳', atlas=A,
        atlas_ids=['JW-XG-C01-S12', 'WP-XG-C01-S12-R01', 'JW-XG-C01-S05', 'WP-XG-C01-S05-R01', 'JW-XG-C02-S23',
                   'WP-XG-C02-S23-R01'],
        source_id='YD-OW-XG', text_path=T + 'YD-OW-XG.txt', locator='序卦 上篇（否→同人、需→訟）；下篇（艮→漸）',
        fragments=['物不可以終否，故受之以同人', '飲食必有訟，故受之以訟', '物不可以終止，故受之以漸'],
        repo_fragments=R(XG, '物不可以終否，故受之以同人', '飲食必有訟，故受之以訟', '物不可以終止，故受之以漸'),
        kind='divergence',
        declarations=D('exists_law_iff', 'Run.keepHistory_shown', 'shown_le_iff', 'Hexagram.order_paired',
                       'Hexagram.mem_order', 'Hexagram.kept_history_unlisted'),
        records=['histories-fix-law-up-to-dead-ends', 'process-and-frame-as-readings', 'hexagrams-on-the-spine'],
        relational='Between pairs the 序卦 gives reasons of the same form (cannot end in 否, so 同人; eating and drinking bring dispute, so 訟), but consecutive pairs stand in no relation the text names or a simple law gives.',
        reading='AI读法：另四次"不可终X"落在两对之间（终否 否→同人、终过 大过→坎、终壮 大壮→晋、终止 艮→渐），在组态上没有已检查的关系。计算核对：受传卦序不是任何三格局部规则（256 条，循环或扭转边界）的运行，最多合 9/63 步；也不是任何"置换六位并加掩码"之律（720×64 条）的运行，最好的是翻转，只合 28/63 步，恰是对内翻转的那些；对与对之间的过渡改变一到六爻不等。所以序卦对对间次序给出的理由（饮食必有讼之类）是加在一个列表上的读法，不是组态所承载的承继之律。这回答 Yi 章 §8 的开放问题：卦序在对间是断言而非导出，只有对内是律。按 exists_law_iff，列表当然是它自己所显之律的运行，但那条律只接纳它自己（Run.keepHistory_shown），这正是"断言"的形式意义。',
        reading_en='AI reading: the received order is a run of no three-cell local rule (best 9 of 63 steps) and of no place-permutation-with-mask law (best 28 of 63, exactly the turned-over steps inside pairs); between pairs the order is asserted, its 序卦 reasons readings laid over a list. It is a run only of the law it shows, which admits only it.',
        gap=G_ORDER),
    dict(
        id='xugua-fuzi-junchen', tradition='易傳·序卦傳', atlas=A,
        atlas_ids=['JW-XG-C02-S01', 'OW-R040'], source_id='YD-OW-XG', text_path=T + 'YD-OW-XG.txt',
        locator='序卦 下篇首', fragments=['有父子然後有君臣，有君臣然後有上下，有上下然後禮儀有所錯'],
        repo_fragments=R(XG, '有父子然後有君臣，有君臣然後有上下，有上下然後禮儀有所錯'),
        kind='divergence',
        declarations=D('Hexagram.waxWane_complement', 'Law.Commutes.rest_paired', 'Hexagram.Symmetry.comp_comm',
                       'Web.significance_undetermined'),
        records=['what-a-commuting-law-keeps-apart', 'hexagram-world-laws', 'one-axiom-yields-g0'],
        relational='A chain of 然後 from 天地 through 男女, 夫婦, 父子 to 君臣 and 上下: rank presented as following from the cosmic order.',
        reading='AI读法：已有图谱 xugua-shouwei 把上篇首"有天地，然后万物生焉"映射为一致；下篇首把这条"然后"链延伸到君臣、上下与礼仪，是把等级读成由天地次第而来。脊柱：律与互补交换，静止成对（waxWane_complement、Commutes.rest_paired），卦的对称彼此可交换（Symmetry.comp_comm），没有一条律给出上下之等；动力学也不决定意义（significance_undetermined）。所以此链是断言的等级次第，不是关系所给的，是"固定等级"的反例。atlas OW-R040 亦注明不把父权等级转为必然规范。',
        reading_en='AI reading: extending the 然後 chain from 天地 to 君臣 and 上下 presents rank as following from the cosmic order; no law of the configurations gives a rank, and the dynamics fix no significance. An asserted hierarchy.',
        gap=None),
    # ---------------- 雜卦傳 ----------------
    dict(
        id='zagua-pairs', tradition='易傳·雜卦傳', atlas=A,
        atlas_ids=['JW-ZG-C01-S12', 'OW-R041', 'JW-ZG-C01-S19', 'OW-R044', 'JW-ZG-C01-S22', 'JW-ZG-C01-S05', 'OW-R043'],
        source_id='YD-OW-ZG', text_path=T + 'YD-OW-ZG.txt', locator='雜卦（一篇）',
        fragments=['剝 爛也，復 反也', '否 、泰 ，反其類也', '革 去故也，鼎 取新也', '損 、益 ，盛衰之始也'],
        kind='agreement',
        declarations=D('Hexagram.Paired', 'Hexagram.order_paired', 'Hexagram.both_fixed_iff', 'Hexagram.reverse',
                       'Hexagram.complement', 'Hexagram.mem_order'),
        records=['hexagrams-on-the-spine', 'hexagram-world-laws'],
        relational='Each named pair is set side by side as a contrast: 剝 rots, 復 returns; 否 and 泰 reverse their kind; 革 removes the old, 鼎 takes the new. The contrast is between the two members of a pair, which the configurations relate by turning over or changing every line.',
        reading='AI读法：计算核对：杂卦六十四名恰是受传卦序的同样三十二对；前五十六名是二十八个相邻对（随蛊、否泰兼翻转与全变；乾坤、小过中孚、离坎为全变；其余为翻转），末八名（大过 姤 渐 颐 既济 归妹 未济 夬）把余下四对交错排列，相邻者无一成对。所以杂卦所对举的，是脊柱已有的配对（order_paired、both_fixed_iff）；它保留对，丢掉对与对之间的次序，与 xugua-between-pairs（对间次序是断言）相合。"反其类"在否泰：二者既是翻转又是全变，"反"在两种意义上都成立。对举不是因果（atlas OW-R041、OW-R044）。Y1 未存杂卦原文。',
        reading_en='AI reading: 雜卦 holds the same 32 pairs as the received order, 28 adjacent and 4 interleaved in its last eight; its contrasts are the spine pairing (turned over or changed in every line). It keeps the pairs and drops the order between them.',
        gap=G_ZAGUA),
    dict(
        id='zagua-guai-end', tradition='易傳·雜卦傳', atlas=A,
        atlas_ids=['JW-ZG-C01-S31', 'WP-ZG-C01-S31-R01', 'JW-ZG-C02-S31'], source_id='YD-OW-ZG',
        text_path=T + 'YD-OW-ZG.txt', locator='雜卦 末句；校詁版末句',
        fragments=['夬 決也，剛決柔也。君子道長，小人道消也', '君子道長。小人道憂也'],
        kind='divergence',
        declarations=D('Hexagram.waxing', 'Hexagram.waning', 'Hexagram.waxWane_returns', 'Hexagram.twelve_steps',
                       'Law.Commutes.not_drawn_to_one', 'Hexagram.waxWane_complement'),
        records=['hexagrams-on-the-spine', 'what-a-commuting-law-keeps-apart'],
        relational='The 傳 closes on one value prevailing: the firm decides against the yielding, the way of the 君子 grows and that of the 小人 wanes. The relation of the two values is read as a contest with a winner.',
        reading='AI读法：这是"争胜"之读的明例，而且在全篇末尾。脊柱：夬之后一步消息即乾，再一步即姤，阴从下复入（waxing、waning、twelve_steps）；每个组态都回来（waxWane_returns）；律与互补交换（waxWane_complement）；没有与互补相容之律把一切引向一处（Commutes.not_drawn_to_one）。所以"刚决柔"不是终局：在律上决之后紧接着遇（杂卦自己在前一句列"姤 遇也，柔遇刚也"）。把一方之长读为君子之道、另一方之消读为小人之道，是给值赋予道德本性。校诂版作"小人道忧也"，异文记下，不影响结构。',
        reading_en='AI reading: closing on the firm prevailing and the 小人 waning reads the two values as a contest with a winner; under the law 夬 is followed by 乾 and then 姤, every configuration returns, and no law compatible with the complement draws everything to one side.',
        gap=None),
    # ---------------- 彖傳 ----------------
    dict(
        id='tuan-tai-pi-jiao', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H11-T', 'HX-R009', 'HX-N013', 'HX-N014', 'JP-H12-T'], source_id='YD-HX01',
        text_path=T + 'YD-HX01.txt', locator='彖 泰（卦十一）；否（卦十二）',
        fragments=['則是天地交而萬物通也，上下交而其志同也', '則是天地不交而萬物不通也，上下不交而天下無邦也'],
        repo_fragments=R(H(11), '則是天地交而萬物通也，上下交而其志同也') + R(H(12), '則是天地不交而萬物不通也，上下不交而天下无邦也'),
        kind='scope',
        declarations=D('Hexagram.opposed', 'Hexagram.oppositions_glue_iff', 'Flow.uncoupled_beyond_coupling',
                       'Flow.system_whole_of_common', 'Flow.unreached_within_system', 'Withholding.withholding_absorbs'),
        records=['place-relations-in-context', 'testing-within-registration', 'levels-of-closure', 'giving-that-waits-on-giving'],
        relational='Passage among all things depends on whether upper and lower meet (交): where they meet, things pass through; where they do not, nothing passes and there is no common realm.',
        reading='AI读法：后果一半有确切范围：在耦合闭包之外的部分，对闭包内每个形成都读不出差别（uncoupled_beyond_coupling）；一个共同条件使系统成为整体（system_whole_of_common）；系统之外的部分到达不了系统之内（unreached_within_system）；一处扣留在其所达之族中终止一切给予（withholding_absorbs）。"不交而万物不通"即：不在同一耦合闭包中，就没有通过。但"交/不交"不能从脊柱现有的位之关系读出：泰与否在每个高度都"对"（oppositions_glue_iff），二者在"对"之下完全相同。区别它们要把一个方向读入两值（天升地降，故天在下则交），这是额外前提，见 gap，交给 Y2–Y4。',
        reading_en='AI reading: "no meeting, no passage" matches the coupling-closure laws (nothing beyond the closure reaches within; one withholding ends giving in its family). But 交 is not the opposition relation: 泰 and 否 are both opposed at every height; telling them apart needs a direction read into the values.',
        gap=G_JIAO),
    dict(
        id='tuan-tai-junzi-xiaoren', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H11-T', 'JP-H12-T'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt', locator='彖 泰（卦十一）',
        fragments=['內陽而外陰，內健而外順，內君子而外小人，君子道長，小人道消也'],
        repo_fragments=R(H(11), '內陽而外陰，內健而外順，內君子而外小人，君子道長，小人道消也'),
        kind='divergence',
        declarations=D('Hexagram.waxWane_complement', 'Hexagram.changes_symmetric', 'Law.Commutes.rest_paired',
                       'Hexagram.complement_moves', 'Web.significance_undetermined'),
        records=['what-a-commuting-law-keeps-apart', 'one-axiom-yields-g0'],
        relational='The two values are given fixed characters: yang is strong and is the 君子, yin is yielding and is the 小人, and the inner/outer placement is read as which of them grows.',
        reading='AI读法：阳健阴顺是象，"内君子而外小人"则把道德本性固定在一个值上。脊柱：律与互补交换（waxWane_complement），一爻之变在互补下对称（changes_symmetric），静止成对（Commutes.rest_paired）；卦的世界里阳与阴之间没有律所给的优劣，排序只能通过额外的比较条件进入，动力学本身不决定意义（significance_undetermined）。所以此句是"固定本性"的读法：把关系中的位置当作本性。但同一彖在否中把句子颠倒（内小人而外君子），说明此处判断随位置而变，这一点是关系的；固定在值上的是君子、小人之名。',
        reading_en='AI reading: attaching 君子 and 小人 to the two values fixes a moral nature on a value the law treats symmetrically; the dynamics fix no ranking. That the 否 彖 inverts the sentence shows the verdict follows placement, which is relational; the names fixed on the values are not.',
        gap=None),
    dict(
        id='tuan-heng-jiu', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H32-T', 'HX-R025'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt', locator='彖 恆（卦三十二）',
        fragments=['天地之道恆久而不已也', '終則有始也', '四時變化而能久成', '觀其所恆，而天地萬物之情可見矣'],
        repo_fragments=R(H(32), '天地之道，恆久而不已也', '終則有始也', '四時變化，而能久成', '觀其所恆，而天地萬物之情可見矣'),
        kind='agreement',
        declarations=D('Hexagram.changesAround_invariant', 'Hexagram.changesAround_run', 'Hexagram.reach_keeps_orbit',
                       'Hexagram.twelve_steps', 'Hexagram.waxWane_returns', 'Web.ByPassing.passes_within',
                       'Web.consumed_continues_transformed'),
        records=['hexagram-world-laws', 'hexagrams-on-the-spine', 'a-pattern-lasts-through-passing', 'becoming-dependence-dynamics'],
        relational='What lasts (恆, 久) is not what stays unchanged: the seasons last by changing, ending turns into beginning, and the constant is seen through the changes.',
        reading='AI读法：已有图谱 heng-jieying 只映射了"刚柔皆应"，"久"这一半未映射。脊柱上，久是变化中的不变量：消息之律每步保持"绕行之变数"（changesAround_invariant），沿每个运行它都是起点的值（changesAround_run），律所到达的都在同一轨道（reach_keeps_orbit）；十二步复得其组态（twelve_steps），每个组态都回来（waxWane_returns），即"终则有始"。一个只经由传递而延续的模式，在每段步中被某个承载者传递（ByPassing.passes_within）；消耗之后仍活跃者是改变了依赖的（consumed_continues_transformed）。所以"恒久而不已"在脊柱上是通过变化而持续：恒是律的不变量，不是静止。这回答任务所问"久"是否为通过变化的延续：在恒彖是。',
        reading_en='AI reading: 久 is continuation through change: what lasts is an invariant of the law along every run (the count of changes around is kept; what the law reaches is on the same orbit), and every configuration returns after twelve steps; a pattern lasts only by being passed on. 恆 is the law’s invariant, not rest.',
        gap=None),
    dict(
        id='tuan-ge', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H49-T', 'HX-R034'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt', locator='彖 革（卦四十九）',
        fragments=['革，水火相息，二女同居，其志不相得曰革', '革而當，其悔乃亡', '天地革而四時成'],
        repo_fragments=R(H(49), '革，水火相息，二女同居，其志不相得，曰革', '革而當，其悔乃亡', '天地革而四時成'),
        kind='agreement',
        declarations=D('Captured.state_perturbation_returns', 'Captured.rule_perturbation_changes',
                       'Law.perturbation_reabsorbed', 'Switching.fixed_loses', 'Switching.changing_regains',
                       'Pace.rule_at_reading'),
        records=['target-capture', 'how-fast-a-rule-may-change'],
        relational='Two that cannot settle together (水火相息: each extinguishes and feeds the other) make a change not of a state but of what governs the states; the seasons are completed by such change.',
        reading='AI读法：革是规则之变，不是状态之变。脊柱：只扰动状态，下一步即被规则收回（state_perturbation_returns、perturbation_reabsorbed）；扰动规则，结果从下一步起随新规则而变（rule_perturbation_changes）。固定规则失去一个组态，变化的规则把它重新取得（Switching.fixed_loses、changing_regains），"天地革而四时成"与此同构：四时之成要求规则本身随时而变。"革而当"对应规则在读取步变（rule_at_reading），时不当则不是这个结构。"汤武革命"的政治引申不采纳。杂卦"革 去故也，鼎 取新也"见 zagua-pairs。',
        reading_en='AI reading: 革 is a change of rule: perturbing the state alone is reabsorbed, perturbing the rule changes the outcome, and a changing rule regains what each fixed rule loses, as the seasons need. The political application is not adopted.',
        gap=None),
    dict(
        id='tuan-sun-yi', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H41-T', 'JP-H42-T', 'HX-R013', 'HX-N026', 'HX-N027'], source_id='YD-HX01',
        text_path=T + 'YD-HX01.txt', locator='彖 損（卦四十一）；益（卦四十二）',
        fragments=['損，損下益上，其道上行', '損剛益柔有時，損益盈虛，與時偕行', '損上益下，民説無疆'],
        repo_fragments=R(H(41), '損，損下益上，其道上行', '損剛益柔有時，損益盈虛，與時偕行') + R(H(42), '損上益下，民說无疆'),
        kind='scope',
        declarations=D('World.exchange_step_iff', 'World.balances_iff_exchange', 'Flow.Balances.rise_given',
                       'Flow.Balances.fall_taken', 'Flow.Balances.accumulates', 'Hexagram.flip'),
        records=['process-and-frame-as-readings', 'rising-and-falling-in-one-exchange', 'becoming-dependence-dynamics'],
        relational='Decrease and increase are one movement read from its two ends: what the lower loses the upper gains (損), and the reverse (益); which is fitting depends on the time.',
        reading='AI读法：计算核对：损即泰交换第三、六爻（一根阳爻由下卦移至上卦：损下益上），益即否交换第一、四爻（损上益下），阳爻总数不变。脊柱：平衡之流中每一升都有所给，每一降都有所取（rise_given、fall_taken），一段步上存量与摄取、补充相抵（accumulates），世界平衡当且仅当其所立按交换之律运行（balances_iff_exchange、exchange_step_iff）。所以损益在脊柱上不是"失"与"得"两种结果，而是一次交换从两端读。范围：这只在交换平衡时成立；"与时偕行"说明哪一端该增减取决于步，律不给出普遍的"益下为善"。atlas HX-R013 提醒不要从彖读出物质守恒：这里守恒的是交换两爻时的爻数，是组态的事实，不是彖的断言。卦变（交换两爻）脊柱无，见 gap。',
        reading_en='AI reading: 損 is 泰 with lines 3 and 6 exchanged (an unbroken line moves from the lower half to the upper), 益 is 否 with lines 1 and 4 exchanged; on the spine this is one balanced exchange read from its two ends, not loss and gain, and which end should rise depends on the step. The line exchange (卦變) is not on the spine.',
        gap=G_GUABIAN),
    dict(
        id='cy-yi-xiahou', tradition='注·程頤《伊川易傳》', atlas=A,
        atlas_ids=['CY-R014', 'CY-N027', 'CY-N028'], source_id='YD-CY3', text_path=T + 'YD-CY3.txt',
        locator='伊川易傳（四庫本）卷三 益卦辭注',
        fragments=['盛衰損益如循環損極必益理之自然', '陽變而為隂者損也隂變而為陽者益也', '下厚則上安故益下為益'],
        kind='agreement',
        declarations=D('Flow.WithinFeeding', 'Flow.beyond_gives_nothing', 'Flow.Balances.consumption_ends_with_feeders',
                       'Clearing.within_closure_yet_loses', 'Hexagram.waxWane_returns'),
        records=['feeding-closure', 'consumption-ends-with-feeders', 'closure-verdict-meets-axiom'],
        relational='Cheng Yi names increase by what it does for the whole: the upper is secure only where the lower is thick, so adding to the lower is what counts as increase. The upper depends on the lower that feeds it.',
        reading='AI读法：程颐把"益"定义为益下，理由是上依赖下：下厚则上安。脊柱：喂养闭包之外的什么都不给闭包内所需的条件（beyond_gives_nothing）；喂养者都失去支持时，消耗至多持续其存量那么多步（consumption_ends_with_feeders）；清除者从自己的闭包看保留了意义，在延续条件下却失去被清除者（within_closure_yet_loses）。所以"下厚则上安"是喂养依赖的确切结构：上之安取决于喂养它的下。"损极必益，理之自然"、"如循环"需要范围：只有在无损之律下才处处回来（waxWane_returns），不是普遍的必然。程颐以阳变阴为损、阴变阳为益（上乾变巽、下坤变震），与彖的"损上益下"在组态上同一（一阳由上移下）。注层，政治比拟不当作财政定律（atlas CY-R014）。',
        reading_en='AI reading: "the upper is secure where the lower is thick" is the feeding dependence: what lies beyond a feeding closure gives nothing to it, and consumption ends with its feeders; "loss at its end must turn to increase, like a cycle" holds only under a lossless law.',
        gap=None),
    dict(
        id='tuan-jie', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H60-T', 'HX-R037'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt', locator='彖 節（卦六十）',
        fragments=['“苦節不可貞”，其道窮也', '天地節而四時成。節以制度，不傷財，不害民'],
        repo_fragments=R(H(60), '苦節不可貞，其道窮也', '天地節而四時成，節以制度，不傷財，不害民'),
        kind='agreement',
        declarations=D('Flow.beyond_given_bounded', 'Flow.takesAll_of_more', 'Flow.Balances.consumption_ends_with_feeders',
                       'Withholding.waitsAll_more_waiting', 'Withholding.withholding_spreads', 'Withholding.withholding_absorbs'),
        records=['where-a-rising-take-ends', 'consumption-ends-with-feeders', 'giving-that-waits-on-giving'],
        relational='A measure relates taking to what is given: the seasons complete by measure; a measure too bitter cannot be kept, since its way is exhausted.',
        reading='AI读法：节在两边都有界，脊柱各有一律。一边：取多于所给不能持续（beyond_given_bounded），上升的取终将取尽所给（takesAll_of_more）。另一边：多一份等待就少一份给予（waitsAll_more_waiting），扣留沿等待之链向下游扩散（withholding_spreads），一处扣留在其所达之族中终止一切给予（withholding_absorbs），即"苦节不可贞，其道穷"。所以节是两条界之间的带：不取过所给，也不扣到给予止息。"制度"、"不伤财，不害民"是传文的社会语汇，不采纳为结构名。atlas HX-R037 读"其道穷"为苦节不可贞之由、不是节制本身致穷，与此一致。',
        reading_en='AI reading: 節 is bounded on both sides: taking beyond what is given cannot last, and added waiting takes giving away until withholding ends all giving (苦節 … 其道窮). The measure is the band between the two laws.',
        gap=None),
    dict(
        id='tuan-jiji-weiji', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H63-T', 'JP-H64-T', 'HX-N048'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt',
        locator='彖 既濟（卦六十三）；未濟（卦六十四）',
        fragments=['“終止則亂”，其道窮也', '“濡其尾，無攸利”，不續終也'],
        repo_fragments=R(H(63), '終止則亂，其道窮也') + R(H(64), '濡其尾，无攸利；不續終也'),
        kind='agreement',
        declarations=D('Law.rests_iff', 'Hexagram.six_steps', 'Hexagram.waxWane_returns', 'Flow.Balances.runs_down',
                       'Flow.uptake_needs_replenishment', 'Web.dissipation_generation_not_recurring'),
        records=['seeking-boundary', 'hexagrams-on-the-spine', 'generation-is-replenishment', 'unceasing-generation-needs-renewal'],
        relational='Completion is not a resting place: stopping at the end brings disorder; the unfinished is what does not carry its course through to the end.',
        reading='AI读法：已有图谱映射了既济"刚柔正而位当"与序卦"受之以未济；终焉"；"终止则乱"与"不续终"未映射。脊柱：确定之律的运行静止，当且仅当它到达一个律不改变的组态（rests_iff）；消息之律下没有这样的组态，六步即全变（six_steps），每个组态都回来（waxWane_returns），所以既济不是静止处。在流上：耗散之下存量每步下降（Balances.runs_down），持续摄取需要持续补充（uptake_needs_replenishment），只耗散而不恢复则生成不能不息（dissipation_generation_not_recurring），"终止则乱"即停止补充的展开衰退。消息之律无不动点，脊柱没有单独命名的引理，见 gap。',
        reading_en='AI reading: under the hexagram law no configuration is a rest (six steps change every line), so 既濟 is no resting place; on flows, stopping replenishment runs the stock down and generation cannot be unceasing. "終止則亂" matches.',
        gap=G_NOREST),
    dict(
        id='cy-jiji-wuchangzhi', tradition='注·程頤《伊川易傳》', atlas=A,
        atlas_ids=['CY-R015', 'CY-N029', 'CY-N030'], source_id='YD-CY4', text_path=T + 'YD-CY4.txt',
        locator='伊川易傳（四庫本）卷四 既濟彖傳注',
        fragments=['天下之事不進則退无一定之理', '濟之終不進而止矣无常止也衰亂至矣', '唯聖人為能通其變於未窮不使至於極也'],
        kind='agreement',
        declarations=D('Law.rests_iff', 'Web.break_not_bounded', 'Flow.policy_uses_after_failure', 'Pace.rule_at_reading',
                       'Switching.changing_regains'),
        records=['seeking-boundary', 'runaway-distance-unregistered', 'how-fast-a-rule-may-change'],
        relational='Cheng Yi: affairs either advance or recede; there is no constant stopping and no single fixed 理; at the end of completion, stopping brings decline. The response is to change before the end is reached.',
        reading='AI读法：两点与脊柱同构。其一，"无常止"：确定之律只在律不改变的组态处静止（rests_iff），程颐说事无此处。其二，"通其变于未穷"：断裂之前，不按水平读入的东西不界定离断裂多远（break_not_bounded），经由耦合的策略只在失败之后动用（policy_uses_after_failure）；在穷之前变，要求规则在读取步就变（rule_at_reading、changing_regains）。值得记下：程颐在这里说"无一定之理"，即事无一成不变之理，他自己的注就不支持把理读成静止先在的定则（对照 zx-yulei-li-xian）。"圣人"不采纳为结构名。atlas CY-R015 注明"并非进越多越好"，保留。',
        reading_en='AI reading: "no constant stopping" is rests_iff (a run rests only at a configuration the law leaves unchanged), and changing before the end needs the rule to change at a reading step, before failure. Cheng Yi’s "无一定之理" itself counts against reading 理 as a fixed prior rule.',
        gap=None),
    # ---------------- 大象傳 ----------------
    dict(
        id='daxiang-junzi-yi', tradition='易傳·大象傳', atlas=A,
        atlas_ids=['JP-H02-DX', 'HX-R006', 'JP-H41-DX', 'HX-R017', 'JP-H49-DX', 'HX-R035', 'JP-H63-DX', 'HX-R052'],
        source_id='YD-HX02', text_path=T + 'YD-HX02.txt', locator='大象 坤、損、革、既濟',
        fragments=['地勢坤，君子以厚德載物', '山下有澤，損；君子以懲忿窒欲', '澤中有火，革；君子以治歷明時', '水在火上，既濟；君子以思患而豫防之'],
        repo_fragments=R(H(2), '地勢坤，君子以厚德載物') + R(H(41), '山下有澤，損；君子以懲忿窒欲') + R(H(49), '澤中有火，革；君子以治歷明時')
        + R(H(63), '水在火上，既濟；君子以思患而豫防之'),
        kind='divergence',
        declarations=D('Learning.goAlike_iff_lumped', 'Learning.Lumped', 'Hexagram.yang_not_goAlike', 'Law.rests_iff',
                       'Captured.rule_perturbation_changes'),
        records=['generalization-through-lumping', 'seeking-boundary', 'target-capture'],
        relational='Each 大象 pairs an image of two trigrams with a conduct (君子以…). The relation is analogy: the image is taken as a model for conduct, with no stated relation carrying from one to the other.',
        reading='AI读法：大象的结构是"取象而法之"，是类比，不是导出。脊柱：一种对应承载律，当且仅当律在其归并之间通行（goAlike_iff_lumped）；象与"君子以"之间没有给出这样的归并，"地势坤"到"厚德载物"、"山下有泽"到"惩忿窒欲"是象征的约定。只在少数大象中结构能带过去：既济"思患而豫防之"与既济不是静止处（rests_iff，见 tuan-jiji-weiji）同构；革"治历明时"与规则之变（rule_perturbation_changes）同构。其余是类比。已有图谱 ziqiang（天行健）为 scope；此条的分歧是：大象作为推理形式整体上是断言的类比。',
        reading_en='AI reading: the 大象 take an image as a model for conduct; that is analogy, carrying law only where a lumping the law goes alike across links image and conduct. It does in 既濟 (no rest, so prepare) and 革 (change of rule, so the calendar); elsewhere it is asserted.',
        gap=None),
    dict(
        id='tuan-kui', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H38-T', 'TP-H38-T-R04', 'TP-H38-T-R05', 'TP-H38-T-R06'], source_id='YD-HX01',
        text_path=T + 'YD-HX01.txt', locator='彖 睽（卦三十八）',
        fragments=['天地睽而其事同也。男女睽而其志通也。萬物睽而其事類也'],
        repo_fragments=R(H(38), '天地睽，而其事同也；男女睽，而其志通也；萬物睽，而其事類也'),
        kind='agreement',
        declarations=D('Hexagram.pairs_goAlike', 'Hexagram.pairOf', 'Learning.goAlike_iff_lumped',
                       'Hexagram.waxWane_complement', 'Hexagram.waxWane_apart'),
        records=['hexagrams-on-the-spine', 'what-a-commuting-law-keeps-apart', 'generalization-through-lumping'],
        relational='Things set apart (睽) still share their work: difference and sameness are read at two levels, apart as configurations, alike in what they do.',
        reading='AI读法：最相异者是互补：每一爻都不同。脊柱：消息之律下互补者永不合一（waxWane_apart），即"睽"；但律与互补交换（waxWane_complement），互补之对是律通行的归并（pairs_goAlike、goAlike_iff_lumped），互补二者在律中做的是同一件事，即"其事同"。所以"睽而其事同"有确切结构：组态之别与律之同在两个层面同时成立。没有断言一切相异者都事同，只在律于其间通行处成立（atlas TP-H38-T-R06 也不把三组合并为万物本质相同）。',
        reading_en='AI reading: complements differ in every line and the law never brings them together, yet the law commutes with the complement and the pairs are a lumping it goes alike across: apart as configurations, alike in what the law does with them.',
        gap=None),
    dict(
        id='tuan-jing', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H48-T', 'TP-H48-T-R02'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt', locator='彖 井（卦四十八）',
        fragments=['井養而不窮也', '改邑不改井'],
        repo_fragments=R(H(48), '井養而不窮也', '改邑不改井'),
        kind='agreement',
        declarations=D('Run.draws_iff_replenishes', 'Stock.repeat_covered_iff', 'Stock.cycles_need',
                       'Flow.replenishment_recurs', 'Flow.uptake_needs_replenishment'),
        records=['recurring-reference-revision', 'unceasing-generation-needs-renewal', 'generation-is-replenishment'],
        relational='The well nourishes without being exhausted because it is drawn from and refilled; the settlement around it may change while the well stays.',
        reading='AI读法："养而不穷"在脊柱上有确切条件：存量有界时，汲取与补充一同复现（draws_iff_replenishes）；一个过程能无限重复，当且仅当首次可行且其回补覆盖其汲取（repeat_covered_iff），无限重复需要回补不少于汲取（cycles_need）；持续摄取需要持续补充（uptake_needs_replenishment）。所以井之不穷不是存量无限，而是汲与补相应。"改邑不改井"：所依之源在周围的形成改变时保持，这一半只作关系读法，未映射到具体之律。',
        reading_en='AI reading: the well is not exhausted because drawing and replenishment recur together and its refill covers its draw; inexhaustibility is a relation of draw and return, not an unlimited stock.',
        gap=None),
    dict(
        id='tuan-qian-gezheng', tradition='易傳·彖傳', atlas=A,
        atlas_ids=['JP-H01-T', 'HX-R003'], source_id='YD-HX01', text_path=T + 'YD-HX01.txt', locator='彖 乾（卦一）',
        fragments=['乾道變化，各正性命'],
        repo_fragments=R(H(1), '乾道變化，各正性命'),
        kind='scope',
        declarations=D('Web.reidentify_step', 'Web.rename_tenure', 'Web.named_throughout', 'Dormancy.held_both', 'World.unity'),
        records=['identity-across-steps', 'unity-of-readings'],
        relational='Each thing’s 性命 is set right within the change of the 乾 way: natures are settled in the change, not before it, on the reading the sentence order favours.',
        reading='AI读法：此句可有两种读法：性命先在、变化使之各归其正（固定本性）；或性命在变化中成形（关系的）。句序是"乾道变化"在前、"各正性命"在后，后一读法更贴近。脊柱给出后一读法的确切范围：同一性是跨步的重新认同，每步的关系在重新认同下不变（reidentify_step），改名保持每项任期、形成与解体（rename_tenure），每步都持续的形成在此认同下始终带着第一步的名（named_throughout）；但跨过休眠步把前后接为同一是一种读法（Dormancy.held_both）。所以"性命"在脊柱上是持续与认同的读法，不是先于变化的本质。已有图谱 jizhi-shan（成之者性也）为分歧；此句不同处在于性命明言在变化之中。',
        reading_en='AI reading: read as natures settled within the change, 性命 corresponds to identity as re-identification across steps (each step’s relations kept under renaming); a prior fixed nature is not supported by the spine, and the sentence order favours the former reading.',
        gap=None),
    # ---------------- 文言傳 ----------------
    dict(
        id='wenyan-yuqing', tradition='易傳·文言傳（坤）', atlas=A,
        atlas_ids=['JP-H02-W'], source_id='YD-OW-WY', text_path=T + 'YD-OW-WY.txt', locator='坤文言',
        fragments=['積善之家，必有餘慶。積不善之家，必有餘殃'],
        repo_fragments=R(WY, '積善之家，必有餘慶。積不善之家，必有餘殃'),
        kind='divergence',
        declarations=D('Web.significance_undetermined', 'Unrestricted', 'g0_of_unrestricted', 'break_carried_nowhere'),
        records=['one-axiom-yields-g0', 'wisdom-root'],
        relational='The accumulated conduct of a household is said to bring it a surplus of blessing or of calamity: a fixed correspondence from conduct to later fortune across generations.',
        reading='AI读法：这是一种报应式的对应：积善必有余庆。脊柱：所表示的动力学不推出生生之意义（significance_undetermined）；意义只在延续条件之下作为定理（g0_of_unrestricted 以 Unrestricted 为前提），而且即便在其下，也没有一条律把"善"的积累映射为"庆"的回报。累积在阈值以下不被读出（break_carried_nowhere）这一结构可以支持"积"的部分，但"必有余庆/余殃"的必然回报不是关系所给，是断言的道德秩序。分歧。',
        reading_en='AI reading: a necessary return of blessing for accumulated good is an asserted moral order; the spine’s dynamics fix no significance, and even under the continuation condition no law maps accumulated good to later fortune. Only the accumulation structure carries.',
        gap=None),
    dict(
        id='wenyan-jian', tradition='易傳·文言傳（坤）', atlas=A,
        atlas_ids=['JP-H02-W'], source_id='YD-OW-WY', text_path=T + 'YD-OW-WY.txt', locator='坤文言',
        fragments=['臣弒其君，子弒其父，非一朝一夕之故，其所由來者漸矣，由辯之不早辯也'],
        repo_fragments=R(WY, '臣弒其君，子弒其父，非一朝一夕之故，其所由來者漸矣，由辯之不早辯也'),
        kind='agreement',
        declarations=D('Web.break_not_bounded', 'Web.observed_raise_couples', 'unread_carried_nowhere',
                       'Thresholds.Draw.forms_at_break', 'Thresholds.Draw.diverges_at_break'),
        records=['runaway-distance-unregistered', 'loops-within-what-a-law-reads'],
        relational='A break is the end of a gradual course; it came because the difference was not told apart early. The relation is between a slow accumulation and the reading that did or did not register it.',
        reading='AI读法：已有图谱 lishuang 映射了坤初六"履霜坚冰"；文言这一句加的是"辨"：断裂的来由是渐，没有及早辨别。脊柱：无人读入之处，差异哪里也不被携带（unread_carried_nowhere）；不按水平读入时，断裂之前没有东西界定离断裂多远（break_not_bounded）；按水平读入则抬升立刻被读出（observed_raise_couples）；回路在断裂处才形成，差异在断裂之后才显（forms_at_break、diverges_at_break）。"由辨之不早辨"即：没有在断裂之前把这一存量按水平读进来。"臣弑君、子弑父"的社会内容不采纳为结构。',
        reading_en='AI reading: the break comes from a gradual course not told apart early: what nothing reads is carried nowhere, and without coupling by level nothing bounds the distance to the break; telling apart early is coupling the stock in by level.',
        gap=None),
    dict(
        id='wenyan-side', tradition='易傳·文言傳（乾）', atlas=A,
        atlas_ids=['JP-H01-W', 'OW-R017', 'OW-R018', 'OW-R019', 'OW-R020'], source_id='YD-OW-WY',
        text_path=T + 'YD-OW-WY.txt', locator='乾文言 首節',
        fragments=['元者，善之長也。亨者，嘉之會也。利者，義之和也。貞者，事之幹也'],
        repo_fragments=R(WY, '元者，善之長也。亨者，嘉之會也。利者，義之和也。貞者，事之幹也'),
        kind='divergence',
        declarations=D('Web.significance_undetermined', 'Unrestricted', 'g0_of_unrestricted', 'Hexagram.waxWane_complement'),
        records=['one-axiom-yields-g0', 'wisdom-root'],
        relational='The four words of the judgement of 乾 (元亨利貞) are read as four virtues of the cosmos and of the 君子: goodness, beauty, rightness and the trunk of affairs. Value is read into the beginning of the course.',
        reading='AI读法：元亨利贞在经文中是占断之辞；文言把它读成四德，把善、嘉、义放进宇宙之始。这是"把价值读入展开"，脊柱明确不这样做：动力学不决定意义（significance_undetermined），意义与伦理只在延续条件下作为定理（Unrestricted、g0_of_unrestricted），而延续条件本身不排序。经与传是不同层，把文言之读回填为卦辞原义是越层。程颐自己把四德限于乾坤（见 cy-side-qiankun）。分歧。',
        reading_en='AI reading: reading 元亨利貞 as four virtues puts value into the beginning of the course; the spine’s dynamics fix no significance, and ethics comes only as theorems under the continuation condition. The 經 formula and the 傳 reading are different layers.',
        gap=None),
    dict(
        id='cy-side-qiankun', tradition='注·程頤《伊川易傳》', atlas=A,
        atlas_ids=['CY-R007', 'CY-R002', 'CY-N003', 'CY-N004'], source_id='YD-CY', text_path=T + 'YD-CY.txt',
        locator='伊川易傳 乾 卦辭注；初九注',
        fragments=['惟《乾》、《坤》有此四德，在他卦則隨事而變焉', '理無形也，故假象以顯義'],
        kind='scope',
        declarations=D('Contextual.indexed_fits', 'Contextual.fitsFree_iff', 'Hexagram.halves_no_free_frame',
                       'Learning.goAlike_iff_lumped', 'exists_law_iff'),
        records=['contextual-registration', 'place-relations-in-context', 'generalization-through-lumping'],
        relational='Cheng Yi restricts the four-virtue reading to 乾 and 坤: in other hexagrams the same words change with the matter, so a word means by its context. 理 has no form and is shown through images.',
        reading='AI读法：程颐对文言的普遍读法作了范围修正：同一字（元、亨、利、贞）在他卦"随事而变"。脊柱同构：带上下文索引的框适合所显的一切（indexed_fits），无上下文的断言之框适合，当且仅当各上下文所显在每个组态处粘合（fitsFree_iff），卦的高度上没有无上下文之框（halves_no_free_frame）。所以"随事而变"即：字义是带上下文的断言，不能跨卦等价（atlas CY-R007）。"理无形，假象以显义"：理是律在其上通行的归并（goAlike_iff_lumped），不是任何一个组态，借组态显出；这一句本身不断言理先于象（atlas CY-R002）。',
        reading_en='AI reading: Cheng Yi’s restriction is a context-indexed reading: the same word is a claim indexed by its hexagram, and a context-free frame fits only where the contexts glue; "理 has no form and is shown through images" fits 理 as a lumping shown in configurations, with no priority asserted here.',
        gap=None),
    dict(
        id='wenyan-heqide', tradition='易傳·文言傳（乾）', atlas=A,
        atlas_ids=['JP-H01-W'], source_id='YD-OW-WY', text_path=T + 'YD-OW-WY.txt', locator='乾文言 九五「大人」節',
        fragments=['夫大人者，與天地合其德', '先天而天弗違，後天而奉天時'],
        repo_fragments=R(WY, '夫大人者，與天地合其德', '先天而天弗違，後天而奉天時'),
        kind='divergence',
        declarations=D('Learning.no_prefix_fixes_next', 'Learning.diagonal_misses', 'Frame.self_incomplete', 'Web.tail_unexcluded'),
        records=['learning-by-refutation', 'registration-within-what-it-registers', 'wisdom-root-part-one'],
        relational='A person (大人) is said to coincide with 天地, 日月, 四時 and 鬼神, so that acting ahead of 天 is never contradicted by it. One formation is placed in full agreement with the whole course.',
        reading='AI读法：这是"个人与天合一、先天而不违"的读法：一个形成在整个进程之前行动而从不落空。脊柱：没有前缀确定下一个值（no_prefix_fixes_next），每种外推在其对角过程上都落空（diagonal_misses），一个以自身组态为断言的框中没有组态实现每一种断言模式（Frame.self_incomplete），有限前缀不排除任何后续（tail_unexcluded）。所以"先天而天弗违"作为普遍之言与脊柱冲突：在整体之中的形成不能先于整体而无误。可以保留的是"后天而奉天时"：随所读之时而行。分歧（人格与天合一）。',
        reading_en='AI reading: a person who acts ahead of 天 and is never contradicted conflicts with the spine: no prefix fixes the next value, every extrapolation misses on its diagonal course, and no configuration realizes every pattern of claims about configurations. "後天而奉天時" remains.',
        gap=None),
    dict(
        id='wenyan-tongsheng', tradition='易傳·文言傳（乾）', atlas=A,
        atlas_ids=['JP-H01-W', 'WH-R016'], source_id='YD-OW-WY', text_path=T + 'YD-OW-WY.txt', locator='乾文言 九五「同聲相應」節',
        fragments=['同聲相應，同氣相求', '則各從其類也'],
        repo_fragments=R(WY, '同聲相應，同氣相求', '則各從其類也'),
        kind='scope',
        declarations=D('Hexagram.opposed', 'Learning.goAlike_iff_lumped', 'Learning.Lumped', 'Law.alike_iff_sameFuture',
                       'Hexagram.pairs_goAlike'),
        records=['place-relations-in-context', 'generalization-through-lumping', 'configurations-alike-by-relation'],
        relational='Like answers like: things of one sound or one breath seek each other, each follows its kind. 應 here is a response between likes.',
        reading='AI读法：文言此处的"应"是同类相应；彖所用的"应"（已有图谱 xian-ganying、heng-jieying 等映射为 opposed）是异类相应：两卦同一高度之爻值不同。两者同名而结构不同，不能等同。脊柱：同类之"从"是归并，在归并内相同者取相同之值（Lumped），律在其间通行即为理（goAlike_iff_lumped），确定之律下相似即未来相同（alike_iff_sameFuture）；"对"（opposed）则是值不同。范围：同类相应只在律于其类之间通行处成立，比如互补之对（pairs_goAlike）；"各从其类"不是普遍之律。王弼"近不必比、远不必乖"（atlas WH-R016）也提醒同声同气不等于机械共振。',
        reading_en='AI reading: 應 here is response between likes, a lumping, while the 彖’s 應 is opposition (different values at one height); the two relations share a name and must not be identified. Like follows like only where the law goes alike across the class.',
        gap=None),
    dict(
        id='wenyan-yin-cong', tradition='易傳·文言傳（坤）', atlas=A,
        atlas_ids=['JP-H02-W'], source_id='YD-OW-WY', text_path=T + 'YD-OW-WY.txt', locator='坤文言（校詁版）；坤文言 末節',
        fragments=['陰雖有美。含之以從王事。弗敢成也。地道也。妻道也。臣道也', '陰，疑於陽必戰，為其嫌於無陽也'],
        repo_fragments=R(WY, '陰雖有美。含之以從王事。弗敢成也。地道也。妻道也。臣道也', '陰，疑於陽必戰，為其嫌於無陽也'),
        kind='divergence',
        declarations=D('Hexagram.waxWane_complement', 'Law.Commutes.rest_paired', 'Hexagram.changes_symmetric',
                       'Hexagram.wane_breaks', 'Law.Commutes.breaks'),
        records=['what-a-commuting-law-keeps-apart'],
        relational='Yin is set under yang: it holds its beauty to serve and dares not complete; it is the way of earth, of the wife, of the minister. Where yin rivals yang there must be war.',
        reading='AI读法：两种非关系线索并见：从属（阴含美以从、弗敢成，妻道臣道）与争战（阴疑于阳必战）。脊柱：律与互补交换（waxWane_complement），一爻之变在互补下对称（changes_symmetric），静止成对（Commutes.rest_paired），阴阳之间没有律所给的主从；要把一切引向一方，律必须破坏对称（Commutes.breaks、wane_breaks），那是另一条律，不是阴阳关系本身。所以从属与必战都是加上去的。"地道无成而代有终"可读为关系的（成于他者），但此句以妻道臣道定之，取从属义。王夫之"权无主辅"（wfz-bingjian）在注层反驳这一读法。从属一句只见于此本校诂版。',
        reading_en='AI reading: subordination (yin serves and dares not complete) and contest (yin rivaling yang must fight) are both added to a relation the law treats symmetrically; drawing everything to one side needs a law that breaks the symmetry.',
        gap=None),
    # ---------------- 王夫之 ----------------
    dict(
        id='wfz-bingjian', tradition='注·王夫之《周易外傳》', atlas=A,
        atlas_ids=['WF-R002', 'WF-N003', 'WF-N004'], source_id='YD-WF1', text_path=T + 'YD-WF1.txt',
        locator='周易外传 繫辭上傳第一章 三',
        fragments=['《乾》《坤》并建于上，时无先后，权无主辅', '无有道而无天地，而曰“一生三，道生天地”，其说诎矣'],
        kind='agreement',
        declarations=D('Hexagram.waxWane_complement', 'Law.Commutes.rest_paired', 'Law.Commutes.not_drawn_to_one',
                       'exists_law_iff', 'shown_le_iff', 'World.unity'),
        records=['what-a-commuting-law-keeps-apart', 'process-and-frame-as-readings', 'unity-of-readings'],
        relational='Wang Fuzhi: 乾 and 坤 are set up together, with no first and no ruling one, like breathing in and out or two eyes seeing one sight; and there is no 道 without 天地, so "道 generates 天地" fails.',
        reading='AI读法：两点都与脊柱同构。其一，"时无先后，权无主辅"：律与互补交换（waxWane_complement），静止成对出现（Commutes.rest_paired），与互补相容之律不把一切引到一处（Commutes.not_drawn_to_one），两值无先后、无主从。其二，"无有道而无天地"：律从历史读出，是该历史作为其运行的最小律（shown_le_iff），有确定之律接纳一个历史当且仅当它自洽（exists_law_iff），每个世界是一个运行（World.unity），没有先于其世界之律。这条注在传统内部反驳韩注"有必始于无"（han-you-shi-yu-wu）与"道生天地"之读，与已有图谱 wang-qi（道者器之道）一致。注层，不回填为传文原义（atlas WF-R002）。',
        reading_en='AI reading: "no first, no ruler" is the complement symmetry the law commutes with (rests come in pairs); "no 道 without 天地" is the law read from its world (the least law a history runs by). It answers, inside the tradition, the commentary readings of a prior 無 or 道.',
        gap=None),
    dict(
        id='wfz-weiji-tongshi', tradition='注·王夫之《周易外傳》', atlas=A,
        atlas_ids=['WF-R006', 'WF-N011', 'WF-N012'], source_id='YD-WF64', text_path=T + 'YD-WF64.txt',
        locator='周易外传 未济',
        fragments=['故《易》成于《既济》而终《未济》，《未济》之世，亦《乾》《坤》之世，而非先后之始终也'],
        kind='agreement',
        declarations=D('Hexagram.process_returns_iff_ends', 'Hexagram.nuclear_two_fixed_one_cycle',
                       'Hexagram.waxWane_returns', 'Hexagram.twelve_steps', 'Law.withHistory_never_returns'),
        records=['hexagram-world-laws', 'hexagrams-on-the-spine', 'recurrence-without-premise'],
        relational='The book ends with 既濟 and 未濟, but the world of 未濟 is also the world of 乾 and 坤: the first and last of the order are not first and last in time.',
        reading='AI读法：卦序之首尾不是时间之始终。脊柱有两处支持：互卦之律下，恰是卦序前二（乾坤）与末二（既济未济）回来（process_returns_iff_ends），乾坤各自不动、既济未济轮转（nuclear_two_fixed_one_cycle），首尾是同一律的吸引处，同时存在，不是先后。消息之律下每个组态都回来（waxWane_returns、twelve_steps），没有第一与最后；只有保留历史的展开不回来（withHistory_never_returns）。再加 xugua-between-pairs：卦序不是任何简单之律的运行，其首尾本无时间意义。注层（atlas WF-R006：注家反对的只是时间先后之读）。',
        reading_en='AI reading: the ends of the order are the attractors of one law held together (under the nuclear law exactly 乾 坤 and 既濟 未濟 return), and under the law of waxing and waning there is no first or last; only a kept history is irreversible.',
        gap=None),
    # ---------------- 朱熹 ----------------
    dict(
        id='zx-qi-li', tradition='注·朱熹《周易本義》', atlas=A,
        atlas_ids=['ZX-R011', 'ZX-R012', 'ZX-R014', 'ZX-N021', 'ZX-N022'], source_id='YD-ZX7', text_path=T + 'YD-ZX7.txt',
        locator='原本周易本義（四庫本）卷七 繫辭上傳 第五章、第十一章、第十二章注',
        fragments=['隂陽迭運者氣也其理則所謂道', '易者隂陽之變大極者其理也', '卦爻隂陽皆形而下者其理則道也'],
        kind='scope',
        declarations=D('exists_law_iff', 'shown_le_iff', 'Run.keepHistory_shown', 'Learning.goAlike_iff_lumped',
                       'Hexagram.waxWane_returns'),
        records=['process-and-frame-as-readings', 'histories-fix-law-up-to-dead-ends', 'generalization-through-lumping'],
        relational='Zhu Xi in the 本義: the alternation of yin and yang is 氣, its 理 is 道; 易 is the change of yin and yang, 太極 is its 理. 理 is named as the 理 of the alternation.',
        reading='AI读法：在本义这几句里，理是"其理"：这一迭运之理、这一变化之理，在脊柱上可读为从历史读出之律（shown_le_iff、exists_law_iff），即律在其上通行的归并（goAlike_iff_lumped）。这几句本身不断言理在气先（atlas ZX-R011）；"大极者其理也"把太极读为律而不是元气，与孔疏（kong-taiji-yuanqi）不同。理的先在之说在语类（zx-yulei-li-xian），不在此。范围：本义此处与脊柱相容，但"形而上/形而下"之分若读成两层存在，即越出脊柱。',
        reading_en='AI reading: in these 本義 lines 理 is the 理 of the alternation, readable as the law a history shows; they assert no priority of 理 over 氣, and they read 太極 as that law rather than as a primal stuff. The priority claim is in the 語類, not here.',
        gap=None),
    dict(
        id='zx-yulei-li-xian', tradition='朱熹《朱子語類》卷一（理氣上）', atlas=None, atlas_ids=[], source_id=None,
        text_path=None, needs_source='https://zh.wikisource.org/wiki/朱子語類/001',
        locator='朱子語類 卷一 理氣上：淳錄（問太極）；祖道錄（或問理在先氣在後）',
        fragments=['未有天地之先，畢竟是先有此理', '理與氣本無先後之可言'],
        kind='divergence',
        declarations=D('shown_le_iff', 'exists_law_iff', 'Run.keepHistory_shown', 'World.unity', 'Frame.arises_iff'),
        records=['process-and-frame-as-readings', 'worlds-are-runs', 'unity-of-readings'],
        relational='Zhu Xi holds both that 理 and 氣 have no before and after, and that before 天地 there is first this 理. 理 is given a priority, logical where not temporal, over what it is the 理 of.',
        reading='AI读法：这是"先在之理"的明文：未有天地之先，毕竟先有此理。朱熹同时说理与气本无先后之可言，同条随后又说推上去时好像理在先，所以先在是逻辑上的而非时间上的。脊柱不支持任何一种先在：律是一个历史作为其运行的最小律（shown_le_iff），保留历史所显之律只接纳该历史（Run.keepHistory_shown），有确定之律当且仅当历史自洽（exists_law_iff），律从运行读出，没有先于其世界的律。王夫之"无其器则无其道"（已有图谱 wang-qi）、"无有道而无天地"（wfz-bingjian）在同一传统中反驳了这一点。文本不在两部图谱中，片段据维基文库页录入，需保存原页核对；语类已在易注之外，可能与 ru 切片重叠。',
        reading_en='AI reading: "before 天地 there is first this 理" gives 理 a priority (logical, since Zhu also says 理 and 氣 have no before and after) over what it is the 理 of; on the spine a law is read from its runs, with no law before its world. Wang Fuzhi answers it within the tradition.',
        gap=None),
    # ---------------- 程頤 易傳序 ----------------
    dict(
        id='cy-xu-tiyong', tradition='注·程頤《伊川易傳》序', atlas=None, atlas_ids=[], source_id=None,
        text_path=None, needs_source='https://zh.wikisource.org/wiki/伊川易傳_(四庫全書本)/伊川易傳序',
        locator='伊川易傳序（元符二年），四庫本，無標點',
        fragments=['易變易也隨時變易以從道也', '至微者理也至著者象也體用一源顯微无間'],
        kind='scope',
        declarations=D('exists_law_iff', 'shown_le_iff', 'World.unity', 'Learning.goAlike_iff_lumped', 'Run.keepHistory_shown'),
        records=['process-and-frame-as-readings', 'unity-of-readings', 'generalization-through-lumping'],
        relational='Cheng Yi: 易 is change, changing with the time so as to follow 道; 理 is the most subtle, 象 the most manifest; 體 and 用 have one source, the subtle and the manifest have no gap.',
        reading='AI读法："体用一源，显微无间"与脊柱相合：律与其运行不是两样，有确定之律接纳一个历史当且仅当该历史自洽（exists_law_iff），律是历史作为其运行的最小律（shown_le_iff），过程与框都是展开的读法（World.unity）。范围在前一句："随时变易以从道"让道作为变化所从之准，"至微者理"可读为先在之理；序文本身不定其先后。程颐既济注"无一定之理"（cy-jiji-wuchangzhi）不支持静止之理，朱熹语类（zx-yulei-li-xian）则推出理在先。所以此条为 scope：一源无间与脊柱一致，"从道"若读成变化服从一个先在之道，即越出。图谱的伊川易传只有指向此序的目录链接，片段据四库本维基文库页录入（无标点，"无"字照原页）。',
        reading_en='AI reading: "體用一源，顯微無間" fits the spine (a law and its runs are not two; the law is read from the history); the scope lies in "changing with the time to follow 道" and "the most subtle is 理", which can be read as a prior norm; the preface does not settle it.',
        gap=None),
]
