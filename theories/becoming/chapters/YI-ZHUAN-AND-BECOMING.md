# 易传与生成／变化之论：周易的构形在脊柱上

2026年10月19日。回应 Ren 的提问与要求（[原话](../../../sources/15-codex-theory-conversations/2026-10-19-the-changes-on-the-spine.md)）：我们的工作与周易、尤其易传的关系能否看见、能否建立；建立起来，成为库的一部分，在脊柱上有明确的对应。本章由 AI 撰写；Ren 的原话另存，是来源，不是任何主张的根据。表中与正文的每一条读法都是 AI 读法，依 [D47](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md#d47-易传在脊柱上的读法--the-readings-of-the-yi-zhuan-on-the-spine) 在理论的一个说明之中成立或修改。

**建成了什么。** 一是周易所描述的构形本身：六爻、每爻刚柔二值、一爻之变、消息之律、所传卦序，作为脊柱上的一个世界写入纯核心模块 [`Becoming.Hexagrams`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Hexagrams.lean)（71 条定理，无公理），脊柱对一切世界证明的律在这些构形上被检查，而不只是被断言。二是逐句对应：易传、经文与两种注疏的 44 段文字，逐字取自保存下来的维基文库版本，每段标明它与理论的关系（相合 24、定域 14、相分 6）和它对应的脊柱声明。三是检查：[`verify_mapping.py`](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/verify_mapping.py) 核对每段文字在所存版本中逐字出现、每个声明在核心检查的审计清单之中、卦序与所存六十四页逐卦一致、本章的对应表与对应文件一致。结果记录是 [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md)。

**没有建成什么。** 这不是对周易整体的解释，也不说易传作者意谓这些律。吉凶悔吝的判断、说卦的取象、三材的指认、卦序（序卦）本身的次第之理、占筮与数术，都不在模块之中；相分之处保留为相分。

## 1. 文本与版本

文本取自中文维基文库，2026年10月19日经 MediaWiki 接口取得，原样保存在 [`sources/zhouyi-yizhuan/`](../../../sources/zhouyi-yizhuan/PROVENANCE.json)，每页记有版本号、版本时间与 SHA-256。这是带标点、分章的电子版，不是影印本，未与任何刻本对校；章次依此版。版本中的繁简异体标记（`-{无}-`）在读时去掉。

| 篇 | 维基文库页面 | 版本号 | 版本时间（UTC） |
|---|---|---:|---|
| 繫辭上 | 易傳/繫辭上 | 2611140 | 2025-11-02 |
| 繫辭下 | 易傳/繫辭下 | 2611136 | 2025-11-02 |
| 序卦 | 易傳/序卦 | 2611127 | 2025-11-02 |
| 說卦 | 易傳/說卦 | 2614055 | 2025-11-09 |
| 文言 | 周易/文言 | 2615215 | 2025-11-11 |
| 六十四卦（卦辭、爻辭、彖、象，乾坤含文言） | 周易/乾 至 周易/未濟，循每页的“下一卦”链接 | 各页见清单 | 2022-02-16 至 2026-09-27 |
| 孔穎達《周易正義》 | 周易正義/10 | 2384519 | 2024-04-01 |
| 王夫之《周易外傳》卷五 | 船山遺書/周易外傳卷五 | 2633077 | 2025-12-14 |

## 2. 卦的世界

模块所写的，都是经文本身描述的结构；它对每一种结构证明的，是脊柱对一切世界证明之律在此的实例，或是有限的计算。

- **六十四种构形。** 一卦是自下而上的六爻，每爻为阳（刚，`true`）或阴（柔，`false`）（`Hexagram`、`Hexagram.line`）。相等与属于逐爻判定，不用任何公理（`eqb`、`mem_of_memb`）。所传卦序由各卦的下卦、上卦逐一写出（`order`），长六十四，含全部构形（`order_length`、`mem_order`）；两两成对，每对之后一卦是前一卦倒转，倒转不变者则六爻皆变（`order_paired`），即孔穎達所说“非覆即變”。检查脚本另行核对：卦序第 n 项的六爻，正是所存第 n 页“X下Y上”所给的六爻。
- **一爻之变。** 一步把一个位置上的爻变为其反（`flip`、`changes`）。任一构形可由任一构形得到（`reach_every`），每一构形皆复返（`changes_returns`），不失任何可能，而过程有合并（`changes_merges`、`changes_keeps`）：在历程分叉之处，复返不等于不合并（`Branching.keeps_of_returns`）。
- **消息之律。** 每爻升一位，上爻出而以其反入初位（`waxWane`）；逆行则每爻降一位（`unwaxWane`）。此律不合并（`waxWane_lossless`），所以依 `Law.lossless_iff_returns`，每一构形皆复返（`waxWane_returns`）。六步之后六爻皆变，即至错卦（`six_steps`、`run_six_steps`）；十二步之后复得原卦（`twelve_steps`）。自坤起，阳爻自下逐步而上：坤、復、臨、泰、大壯、夬、乾（`waxing`）；自乾起，阴爻同样自下而上：乾、姤、遯、否、觀、剝、坤（`waning`）。这就是十二消息卦之环：坤首次复至坤在第十二步（`first_return`），自乾第七步一阳复生为復（`seventh_step`）。它只是此律的一轨：隨四步即返而两步不返（`fourth_step`），其轨为隨、中孚、蠱、小過。
- **有合并之律。** 若上爻出后入初位的只是阴爻（`wane`），律便合并：剝与坤都走到坤（`wane_merges`）。六步之后一切皆坤（`wane_six`），律不再离开坤（`allBroken_absorbing`），其他构形都被吸入、永不回来、不复返（`wane_drawn`、`wane_never_back`、`wane_not_returns`），可能有所永失（`wane_loses`）。对六十四卦上的一切律，每一构形皆复返，恰当此律不合并（`every_returns_iff`）。
- **对称与读法。** 律与错（六爻皆变）交换（`waxWane_complement`），倒转一卦则律逆行（`reverse_wax`、`reverse_waxWane`）。把一卦与其错卦合为一对，是律在其上同行的归并（`pairs_lumped`、`pairs_goAlike`，经 `Learning.goAlike_iff_lumped`）；按阳爻之数归并则不是（`yang_not_lumped`、`yang_not_goAlike`）。
- **爻作为主张、框架与世界。** 沿律读之，某位之主张实现，恰当该位之爻为阳（`lines`）。沿律的每一运行，某爻在任意晚的步上转为阳（`arising_recurs`），依 `Frame.claims_recur_iff` 也在任意晚的步上止于阳（`ceasing_recurs`）；读作此框架的世界，诸位在任意晚的步上生起与止息（`world_arising_recurs`、`world_ceasing_recurs`）。
- **在六十四之内往下走。** 任一过程下，任一运行的前六十五个状态中必有重访（`revisits_within_order`），一爻之变的每一运行从每一步往后都有重访（`changes_run_revisits`）；而带着历史的律不被任何清单所含（`kept_history_unlisted`）。

## 3. 三种关系

- **相合**：经文所说的结构，脊柱上有已检查之律与之对应。
- **定域**：脊柱给出此句成立的确切范围，并修正其全称形式。
- **相分**：经文所断言者理论不断言，或与理论的结构名称冲突。

相合不是印证：律的成立不靠经文，经文的意义也不由律穷尽。定域不是否定：它说出在哪里成立。相分各保其说。

## 4. 逐句对应

表由[对应文件](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/passages.json)生成，检查脚本核对两者一致；改动应改对应文件，再以 `--table` 重印此表。声明名省去前缀 `Becoming.`。

<!-- passage-map:begin -->
| 经文 | 出处 | 关系 | 脊柱上的声明 | 读法（AI） |
|---|---|---|---|---|
| <a id="p-chonggua"></a>「八卦成列，象在其中矣；因而重之，爻在其中矣」 | 《繫辭下》第一章 | 相合 | `Hexagram`<br>`Hexagram.line`<br>`Hexagram.order`<br>`Hexagram.order_length`<br>`Hexagram.mem_order` | 卦由下卦、上卦相重而成，六爻各取刚柔二值；所传卦序长六十四，含全部构形。 |
| <a id="p-sancai"></a>「兼三材而兩之，故六」 | 《繫辭下》第八章 | 相合 | `Hexagram.Place`<br>`Hexagram.places`<br>`Hexagram.line` | 六位，每位二值；把六位两两分作天、地、人三材，不在模块之内。 |
| <a id="p-taiji"></a>「是故易有太極，是生兩儀，兩儀生四象，四象生八卦」 | 《繫辭上》第十一章 | 定域 | `Hexagram.order_length`<br>`World.unity` | 每加一个二值之分，构形加倍，至六分而六十四；脊柱把它读作一个展开之上逐层的区分，不是时间中的先后产生。 |
| <a id="p-feifu"></a>「今驗六十四卦，二二相耦，非覆即變」 | 孔穎達《周易正義》（序卦疏） | 相合 | `Hexagram.reverse`<br>`Hexagram.complement`<br>`Hexagram.Paired`<br>`Hexagram.pairs`<br>`Hexagram.order_paired` | 对所传卦序逐对检验：每对之后一卦是前一卦倒转（覆），倒转不变者则六爻皆变（變）。 |
| <a id="p-qiankun-chenglie"></a>「乾坤成列，而易立乎其中矣」 | 《繫辭上》第十二章 | 相合 | `Hexagram.waxing`<br>`Hexagram.waning`<br>`Hexagram.six_steps` | 消息之律下，坤六步至乾，乾六步至坤；任一构形六步即至其错卦。 |
| <a id="p-gangrou"></a>「剛柔相推而生變化」 | 《繫辭上》第二章 | 相合 | `Hexagram.flip`<br>`Hexagram.changes`<br>`Hexagram.reach_every`<br>`Hexagram.changes_returns`<br>`Hexagram.changes_keeps`<br>`Hexagram.changes_merges`<br>`Branching.keeps_of_returns` | 一爻之变：任一构形可由任一构形得到，每一构形皆复返，不失任何可能；而此过程有合并，可见复返不等于无合并。 |
| <a id="p-wuwang-bufu"></a>「无平不陂，无往不復」……「无往不復，天地際也」 | 泰·九三、象 | 定域 | `Law.lossless_iff_returns`<br>`Hexagram.every_returns_iff`<br>`Hexagram.waxWane_returns`<br>`Hexagram.wane_not_returns`<br>`Law.drawn_iff_not_returns` | 有限构形之内，一律之下每一构形皆复返，恰当此律不合并；律有合并处，被吸入者不复返。 |
| <a id="p-qiri-laifu"></a>「反復其道，七日來復」 | 復·卦辭、彖 | 相合 | `Hexagram.rising`<br>`Hexagram.falling`<br>`Hexagram.waning`<br>`Hexagram.seventh_step` | 依消息卦的读法：自乾起，一阴生为姤，第六步至坤，第七步一阳复生为復。 |
| <a id="p-tiandi-zhixin"></a>「復其見天地之心乎」 | 復·彖 | 相分 | `Hexagram.waxWane_returns`<br>`Web.significance_undetermined` | 复返是不合并之律的定理；把复返读作天地之心（意向或关切），律不支持，动力学不决定意义。 |
| <a id="p-xiaoxi"></a>「日中則昃，月盈則食，天地盈虛，與時消息」 | 豐·彖 | 相合 | `Hexagram.waxWane`<br>`Hexagram.waxing`<br>`Hexagram.waning`<br>`Hexagram.twelve_steps`<br>`Hexagram.first_return` | 消息之律：每爻升一位，上爻出而以其反入初位；盈（乾）之后即消，虚（坤）之后即息，自坤十二步首次复至坤。 |
| <a id="p-shang-xiaoxi"></a>「君子尚消息盈虛，天行也」 | 剝·彖 | 相合 | `Hexagram.waxWane_lossless`<br>`Hexagram.twelve_steps`<br>`Hexagram.fourth_step` | 消息盈虚是一个不合并之律的运行；十二消息卦之环只是其中一轨，隨、中孚、蠱、小過四步即返。 |
| <a id="p-wanglai-butong"></a>「闔戶謂之坤，闢戶謂之乾，一闔一闢謂之變；往來不窮謂之通」 | 《繫辭上》第十一章 | 定域 | `Hexagram.waxWane_returns`<br>`Hexagram.every_returns_iff`<br>`Hexagram.allBroken_absorbing` | 往来不穷，恰在律不合并之处；只入阴爻之律下坤为吸收态，往而不来。 |
| <a id="p-riyue"></a>「日往則月來，月往則日來，日月相推而明生焉」……「往者，屈也；來者，信也。屈信相感而利生焉」 | 《繫辭下》第四章 | 相合 | `Hexagram.arising_recurs`<br>`Hexagram.ceasing_recurs`<br>`Frame.claims_recur_iff` | 沿律之每一运行，一爻在任意晚的步上转为阳，也在任意晚的步上止于阳；“利生焉”是评价，不在律中。 |
| <a id="p-yiyin-yiyang"></a>「一陰一陽之謂道」 | 《繫辭上》第五章 | 定域 | `Web.change_readings`<br>`World.arising_iff_ceasing`<br>`World.law_iff_em`<br>`Hexagram.world_arising_recurs`<br>`Hexagram.world_ceasing_recurs` | 生起与止息是一个变化的两种读法；有限且活动可判定的世界中二者同时反复；不经判定而对一切有限世界断言之，等价于排中律。 |
| <a id="p-jizhi-shan"></a>「繼之者善也，成之者性也」 | 《繫辭上》第五章 | 相分 | `Web.significance_undetermined`<br>`Unrestricted`<br>`g0_of_unrestricted` | 易传断言继之者善；理论中动力学不决定意义，生命意义只在延续条件之下是定理，此条件明示而不断言。 |
| <a id="p-gu-wanwu"></a>「鼓萬物而不與聖人同憂」 | 《繫辭上》第五章 | 相合 | `Web.significance_undetermined` | 律鼓动万物，自身不带关切：无物有意义与万物有意义，动力学两者都不排除。 |
| <a id="p-jianzhi"></a>「仁者見之謂之仁，知者見之謂之知」 | 《繫辭上》第五章 | 相合 | `Web.change_readings`<br>`Learning.goAlike_iff_lumped`<br>`Hexagram.pairs_goAlike`<br>`Hexagram.yang_not_goAlike` | 同一展开有多种读法；一种读法承载律，恰当律在其归并上同行：错卦之对承载，阳爻之数不承载。 |
| <a id="p-rixin"></a>「富有之謂大業，日新之謂盛德」 | 《繫辭上》第五章 | 相合 | `Hexagram.waxWane_returns`<br>`Law.withHistory_never_returns`<br>`Hexagram.kept_history_unlisted` | 构形皆复返，而带着历史的展开永不复返，不被任何清单所含：无往不复与日新是同一律的两层读法；大业、盛德之评价不在律中。 |
| <a id="p-shengsheng"></a>「生生之謂易」 | 《繫辭上》第五章 | 定域 | `Hexagram.wane_drawn`<br>`Hexagram.wane_loses`<br>`World.living_crosses`<br>`World.arising_opens`<br>`Web.generation_fed_from_beyond` | 脊柱上的变化比生生宽：它也含合并与可能之失；生生作为生成之持续，需要开放，并由外部供给。 |
| <a id="p-jishu-zhilai"></a>「極數知來之謂占」 | 《繫辭上》第五章 | 定域 | `Learning.no_prefix_fixes_next`<br>`Learning.diagonal_misses`<br>`Identification.bounded_agree`<br>`Learning.goAlike_iff_lumped` | 一般而言没有有限前缀定得下一步；知来只在历程有界、读法为律所同行之处成立；以数占筮不被支持。 |
| <a id="p-buce"></a>「陰陽不測之謂神」 | 《繫辭上》第五章 | 相合 | `Learning.diagonal_misses`<br>`Web.tail_unexcluded` | 对任一外推，皆有其失误的历程；没有模型时，有限前缀不排除其后的任何走向。 |
| <a id="p-gantong"></a>「易，无思也，无為也，寂然不動，感而遂通天下之故」 | 《繫辭上》第十章 | 定域 | `Web.observed_level_couples`<br>`Flow.uncoupled_beyond_coupling` | 感即耦合：经耦合而入的差别得以传达；耦合闭包之外者不被区分，“通天下”恰止于耦合所及。 |
| <a id="p-xian-gan"></a>「咸，感也」……「觀其所感，而天地萬物之情可見矣」 | 咸·彖 | 相合 | `Web.observed_level_couples`<br>`Flow.uncoupled_beyond_coupling`<br>`Flow.unselected_beyond_coupling` | 所见即所感：一个形成所显示的，是其耦合所携带的；闭包之外的部分，选择也不能及。 |
| <a id="p-yanji"></a>「夫易，聖人之所以極深而研幾也」 | 《繫辭上》第十章 | 定域 | `Web.observed_level_couples`<br>`Web.break_not_bounded` | 研几只能经由耦合而入者：依水平耦合的条件，其差别传入；断裂所系的条件若不耦合，断裂之前无物界定其远近。 |
| <a id="p-zhiji"></a>「知幾其神乎」……「幾者，動之微，吉之先見者也」 | 《繫辭下》第四章 | 定域 | `Web.break_not_bounded`<br>`Web.observed_level_couples`<br>`Flow.policy_uses_after_failure` | 几之先见恰在相关条件耦合入读法之处；否则断裂前无可登记，经耦合的策略只在失败之后才动用更大的储备。 |
| <a id="p-qiong-bian"></a>「易窮則變，變則通，通則久」 | 《繫辭下》第二章 | 定域 | `Hexagram.waxing`<br>`Hexagram.waning`<br>`Hexagram.allBroken_absorbing`<br>`Web.consumed_ends_when_fixed`<br>`Web.consumed_continues_transformed` | 消息之律下极则转；只入阴爻之律下坤为吸收态，穷而不变。失而不复之后，依存不变者不能延续，延续者已改变其依存：穷则变不是普遍律。 |
| <a id="p-kanglong"></a>「上九：亢龍，有悔」……「亢龍有悔，盈不可久也」……「「亢龍有悔」，窮之災也」……「「亢龍有悔」，與時偕極」 | 乾·上九、象、文言 | 相合 | `Law.more_never_rests`<br>`Flow.takesAll_of_more`<br>`Flow.more_exhausted` | 以多于现在为目标者永不止息；供给有界时，递增之取终取尽所予；封闭之下，多于现在必竭。 |
| <a id="p-kang-zhiwei-yan"></a>「亢之為言也。知進而不知退。知存而不知亡。知得而不知喪」 | 《文言》（乾） | 相合 | `Flow.policy_uses_after_failure`<br>`Web.break_not_bounded` | 只知进者，所失只在断裂时登记：经耦合的策略只在失败之后动用更大储备；断裂之前，耦合所入者不界定其远近。 |
| <a id="p-gen-zhi"></a>「艮，止也。時止則止，時行則行，動靜不失其時」 | 艮·彖 | 相合 | `Law.rests_iff`<br>`World.rests_unrefuted_enclosed` | 止是相对于律而言：轨道止于其目标，恰当它到达律所不变之态；静不是世界停止。 |
| <a id="p-lishuang"></a>「履霜，堅冰至」……「履霜堅冰，陰始凝也。馴致其道，至堅冰也」 | 坤·初六、象 | 相合 | `Hexagram.wane`<br>`Hexagram.wane_six`<br>`Hexagram.wane_drawn`<br>`Hexagram.wane_never_back`<br>`Law.DrawnInto.never_back` | 只入阴爻之律：每步多一阴爻，六步皆阴而不复离，被吸入者永不回来；在消息之律下坤并非吸收态，坚冰是否长存在律不在卦。 |
| <a id="p-weiji"></a>「物不可窮也，故受之以未濟；終焉」 | 《序卦》 | 相合 | `Law.withHistory_unlisted`<br>`Hexagram.kept_history_unlisted`<br>`World.arising_opens`<br>`Onward.run_iff_continues` | 卦序终于未济：带着历史的展开不被任何清单所含；生起无尽须开放；有限构形之内，运行恰是长如清单之历程。 |
| <a id="p-ziqiang"></a>「天行健，君子以自強不息」 | 乾·象 | 定域 | `Flow.fed_from_beyond`<br>`Web.generation_fed_from_beyond` | 平衡而耗散的交换中，持续者由外部供给，封闭的部分不能只凭自身不息；自强读作耦合之中自身之分则相合，读作自足则相分。 |
| <a id="p-yuanshi"></a>「原始反終，故知死生之說」 | 《繫辭上》第四章 | 相合 | `Frame.arises_iff`<br>`Frame.novel_iff_arises`<br>`World.living_crosses` | 生起是一主张被新实现；活着跨越生起与止息，不由二者之反复决定。 |
| <a id="p-xiang"></a>「是故易者，象也。象也者，像也」 | 《繫辭下》第三章 | 定域 | `Learning.goAlike_iff_lumped`<br>`Hexagram.pairs_goAlike`<br>`Hexagram.yang_not_goAlike` | 象是一种归并的读法；它承载律，恰当律在其上同行。 |
| <a id="p-yijian"></a>「易簡，而天下之理得矣」 | 《繫辭上》第一章 | 定域 | `Learning.goAlike_iff_lumped`<br>`Hexagram.pairs_lumped`<br>`Hexagram.yang_not_lumped` | 更简的读法保留律，恰当它是律所同行的归并：六十四归为三十二对仍成律，按阳爻之数归并则不成；并非任何简化皆得理。 |
| <a id="p-daoqi"></a>「是故形而上者謂之道，形而下者謂之器」 | 《繫辭上》第十二章 | 定域 | `exists_law_iff`<br>`shown_le_iff`<br>`Run.keepHistory_shown` | 律由展开读出：一历史所显之律是它所属的最小律；某一决定之律容纳此历史，恰当此历史自洽。把形而上读作器外另一实在，则相分。 |
| <a id="p-wang-qi"></a>「天下惟器而已矣。道者器之道，器者不可謂之道之器也」……「無其器則無其道」 | 王夫之《周易外傳》卷五 | 相合 | `exists_law_iff`<br>`shown_le_iff`<br>`Run.keepHistory_shown` | 道是器之道：一历史所显之律只容纳此历史，律不先于其所行之展开。 |
| <a id="p-biandong"></a>「變動不居，周流六虛，上下无常，剛柔相易，不可為典要，唯變所適」 | 《繫辭下》第七章 | 相合 | `Hexagram.run_six_steps`<br>`Hexagram.twelve_steps`<br>`Learning.no_prefix_fixes_next`<br>`Contextual.fitsFree_iff` | 消息之律下每爻周流六位；没有有限前缀定得下一步；去语境的读法，恰在各语境相接处一致时才合。 |
| <a id="p-liuyao-xiangza"></a>「六爻相雜，唯其時物也」 | 《繫辭下》第七章 | 相合 | `Contextual.indexed_fits`<br>`Contextual.glues_iff_agree` | 一爻之义随其位与时：带语境索引的框架合于所示的一切；各语境所示能粘合，恰当它们在相接处一致。 |
| <a id="p-zhen-fu-yi"></a>「天下之動，貞夫一者也」 | 《繫辭下》第一章 | 相合 | `World.unity` | 每一世界是交换律的一次运行，其平衡即其诸读法之粘合。 |
| <a id="p-tianzun"></a>「天尊地卑，乾坤定矣。卑高以陳，貴賤位矣」 | 《繫辭上》第一章 | 相分 | `Hexagram.complement_complement`<br>`Hexagram.waxWane_complement`<br>`Hexagram.reverse_waxWane` | 构形中乾坤互为错卦，律与错交换、倒转则律逆行：结构不含尊卑；贵贱之位是理论不采的等级。 |
| <a id="p-guijian"></a>「三與五同功而異位，其遇不同：三多凶，五多功，貴賤之等也」 | 《繫辭下》第八章 | 相分 | `Hexagram.Place`<br>`Contextual.indexed_fits` | 位有别，是语境之索引；位无等级。 |
| <a id="p-dade"></a>「天地之大德曰生，聖人之大寶曰位」 | 《繫辭下》第一章 | 相分 | `World.living_crosses`<br>`Web.significance_undetermined`<br>`g0_of_unrestricted` | 大德曰生是断言；理论中生起不定活着，生命意义只在延续条件之下成立；大宝曰位是等级。 |
| <a id="p-dayan"></a>「大衍之數五十，其用四十有九」……「以卜筮者尚其占」 | 《繫辭上》第九章、第十章 | 相分 | `Learning.no_prefix_fixes_next`<br>`Learning.diagonal_misses` | 数术不在脊柱之中：任一由有限记录给出预言的程序，都有其失误的历程。 |
<!-- passage-map:end -->

## 5. 几处要点

**无往不复与日新，是同一律的两层。** 泰九三“无往不復”，在有限构形之内，恰是律不合并时的定理（`Law.lossless_iff_returns`）：消息之律下每卦皆返。同一律带着历史读，则永不复返，也不被任何清单所含（`Law.withHistory_never_returns`、`Hexagram.kept_history_unlisted`）：构形复返，历史日新。两句不冲突，因为说的是同一展开的两种读法。律一旦合并，“无往不復”即失效：只入阴爻之律下，被吸入坤者不再回来（`wane_not_returns`）；“无往不復”的成立范围，就是不合并。

**穷则变不是普遍律。** 消息之律下，极则必转：乾之后即姤，坤之后即復。只入阴爻之律下，坤是吸收态，穷而不变。在依存之网上，失而不复之后，依存不变的形成不能延续（`Web.consumed_ends_when_fixed`），延续的形成必已改变其依存（`Web.consumed_continues_transformed`）。所以“變則通，通則久”的一半有律：能久者已变；“窮則變”的另一半没有：穷不保证变，也可以是终。

**一阴一阳的强度。** 生起与止息是一个变化的两种读法（`Web.change_readings`，依定义）。有限且活动可判定的世界中，生起反复恰当止息反复（`World.arising_iff_ceasing`）；把这一律不经判定地断言于一切有限世界，等价于排中律（`World.law_iff_em`）。若把“一陰一陽之謂道”读作对一切世界的全称之律，它恰与排中律一样强；在六十四卦这样逐爻可判定的世界上，它是定理（`Hexagram.world_arising_recurs`、`Hexagram.world_ceasing_recurs`）。

**象与易简：哪些读法承载律。** 象是一种归并。一种读法承载律，恰当律在其归并上同行（`Learning.goAlike_iff_lumped`）。六十四卦归为三十二对错卦，律仍是律（`pairs_goAlike`）；按阳爻多少归并，律就不再是律（`yang_not_goAlike`）：阳爻同为三的泰与否，下一步分属阳爻四与阳爻二。“易簡而天下之理得”在这里有确切的范围：简化得理，恰当简化是律所同行的归并。

**感与几：止于耦合所及。** 咸彖“咸，感也”与繫辭“感而遂通”，读作耦合：经水平耦合的条件，差别传入（`Web.observed_level_couples`）；耦合闭包之外，什么也不被区分（`Flow.uncoupled_beyond_coupling`），选择也不能及（`Flow.unselected_beyond_coupling`）。“通天下之故”于是恰止于耦合所及。几也是一样：断裂所系的条件若不以水平耦合入读法，则断裂之前，没有经耦合而入的东西界定断裂有多远（`Web.break_not_bounded`），经耦合的策略只在失败之后动用更大储备（`Flow.policy_uses_after_failure`）。“知幾其神乎”说的难处，在这里是一条律：几的先见，只在相关条件已耦合入读法时可能。这也是文言“亢之為言也，知進而不知退”的结构：只知进者，所失只在断裂时登记。

**生生之谓易：变化比生生宽。** 理论中的变化包括生成与退化，两者不重叠；生生是生成之持续（D1），不是任何新的组织。只入阴爻之律是一种变化，它合并、失去可能（`wane_drawn`、`wane_loses`）。活着跨越生起与止息，不由二者的反复决定（`World.living_crosses`）。生成之持续需要开放（`World.arising_opens`），并由外部供给（`Web.generation_fed_from_beyond`）。所以“生生之謂易”在理论中是定域：易（变化）不尽是生生；生生是变化中的一种历程，有它的条件。

**自强不息与外部供给。** “天行健，君子以自強不息”是劝勉，不是本体论断。若把“自强”读作只凭自身而不息，平衡而耗散的交换中没有这样的部分：持续者由外部供给（`Flow.fed_from_beyond`）。若读作在耦合之中尽其自身之分，则与理论相合。

**道器：律由展开读出。** 一历史所显之律，是它所属的最小律（`shown_le_iff`）；带着历史的运行所显之律，只容纳此历史（`Run.keepHistory_shown`）；某一决定之律容纳一历史，恰当此历史自洽（`exists_law_iff`）。律不先于其所行之展开，也不在展开之外另成一实在。这与王夫之“道者器之道”相合；“形而上者謂之道”读作器外另一实在，则与理论相分。

## 6. 相分之处

- **继之者善，天地之大德曰生，復见天地之心。** 易传把善、大德与心归于天地之行。理论中动力学不决定意义：无物有意义与万物有意义，动力学两者都不排除（`Web.significance_undetermined`）。生命意义只在延续条件（`Unrestricted`）之下是定理（`g0_of_unrestricted`），此条件在理论中明示而不断言，其根据开放。
- **天尊地卑，贵贱位矣；三多凶，五多功，贵贱之等；圣人之大宝曰位。** 构形之中乾坤互为错卦，律与错交换，倒转则律逆行：结构里没有尊卑。位有别，是语境的索引（`Contextual.indexed_fits`），不是等级。贵贱之位是社会等级，理论不采。
- **大衍之数，卜筮尚占。** 数术与占筮不在脊柱之中。任一由有限记录给出下一步的程序，都有它失误的历程（`Learning.no_prefix_fixes_next`、`Learning.diagonal_misses`）；知来只在历程有界、读法为律所同行之处成立。

## 7. 读法的标注与依据

本章的读法都是 AI 读法。它们依 D45 在理论的一个说明中成立：经文是这些词句意义的证据，读法是否站得住，由它在理论中的位置论证。Ren 的话是来源。“七日來復”依消息卦的读法，这只是诸读法之一；“周流六虛”读作消息之律下爻的升降，“兼三材而兩之”只取六位二值的结构。凡读法超出 Lean 所证者，表中写明不在律中。

## 8. 未做之事

- 卦序（序卦）的次第之理：只检查了配对，卦序本身不是任何律的轨道。
- 吉凶悔吝与卦爻辞的判断、说卦的取象与方位、卦气与纳甲。
- 爻位的应、比、中、正：它们是语境中的关系，可以作为带索引的读法写入，尚未写。
- 与刻本的对校；历代注疏的系统比较（王弼、程颐、朱熹的读法未逐一对照）。
- 一个独立的审读。

## 9. 怎样检查

```bash
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/verify_mapping.py
```

模块的证明由核心检查器检查（`check_becoming.py`），其收据列出每个声明与空的公理依赖。
