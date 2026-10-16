<a id="p47-独立审查登记与检验--independent-review-of-p47-registration-and-testing"></a>
# P47 独立审查：登记与检验

> **中文版（2026-10-17）。** 正典文本是[英文版](BECOMING-P49-REVIEW.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-11，Asia/Bangkok。**AI 独立审查（第十六次；另一 agent，未参与撰写）。**

审查对象
- `scratchpad/p47/build/Becoming/Testing.lean`（P47，`Becoming.Testing`），sha256 `6ba242ddc8a927a97eca3ea38c071ae5a68b40da68e188b8e0ca3abe50f9646a`，696 行。
- 与工作树 `.claude/worktrees/p47-testing/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Testing.lean` 逐字节相同。构建目录中的其余模块（含 P42 `Becoming.Feedback`，c9c219e3）也与工作树逐字节相同。
- 背景 / Context：计划 `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/REGISTRATION-AND-TESTING-PLAN.md`（工作树中未跟踪 / untracked in the worktree），Ren 的原话 / Ren's words `sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md`，`AGENTS.md`，`theories/becoming/chapters/NONDUAL-METHOD.md`。

分类（同此前审查）
- (甲) 表示省略了某一关系
- (乙) 未解决的推论或说过了头
- (丙) 满足所述条件的真实反例

---

## 摘要

**形式状态。**
- Lean 4.29.1（`f72c35b3`）。模块副本重新编译，没有错误也没有警告。
- 遍历模块的全部常量做公理审计：127 个，公理报告都是空的（`Audit.lean`）。
- 每个定理都证明了它自己的陈述。问题都在散文、读法、名字和一个假设的范围上，不在证明上。
- 探针共 192 个常量，都没有公理（`ProbeAudit.lean`）。另有 `ProbeNames.lean`，故意示范 `nomatch` 证明会带入 `propext`。

**最重要的发现。**
1. **（乙，重大）视界读法说过了头。** “关于整个运行的主张不被任何有限记录检验”，“每个有限的更新检验都在一侧出错”，这两句只在延续开放时成立（`Renewable` 的见证过程）。
   - 对一切历史定义的 `Refutes` 而言，它们平凡成立（C2）。
   - 相对于一个模型，它们是假的：模型固定了交换，观测储量的形成在第一步就否证关于整个运行的假主张（C3）。
   - 相对于模型的否证，就是对“模型且主张”这个合取的否证（C6，迪昂–奎因）。这样的否证可错：模型错了，就否证真的主张（C4）。而登记本身可以否证模型（C4b）。
2. **（甲／丙，重大）阈下不见依赖 `RespondsThrough`。** 这一假设要求：凡 `g` 所登记的条件，所有形成在其上的总交换都只随 `g` 的登记而变。它排除了直接回应储量的他者，也排除了随水平而变的更新。
   - 在 `Attracting` 中，较丰的储量招来取用者，较丰的网反而先断（A7）。
   - 读法“失控是收益被登记、损失要到断裂才被登记”，以及 README 那一行“较丰储量的盈余只在较贫者不再支持之后才被动用”，都没有写出这一假设。
3. **（乙，重大）自身水平的决定。** 参数化的 `obs` 是对的。但把“在一类读法中自身水平算作已登记”当作默认，是较弱的选择。
   - 脊柱已经有结构性的关系：`Web.SelfBearing`（`Becoming.Roles`），即依存于自身的水平。经由它，自身水平像其他条件一样经阈值登记（F3）。
   - `Prey` 中“捕食者在影响闭包之外”只是因为猎物不依存于自身。猎物的水平与它的活动无关，捕食者以零水平活跃（F2）。这是省略了一个关系。
   - 在 `ownStanding` 之下，对自身耗竭的阈下不见无法表达（F1）。而这恰是失控的核心情形。
4. **（乙，中等）所及闭包的传递性在“其余交换不变”的比较中不起作用。** 在其中，起作用的只是直接交换。已检查一个回应性的版本（B1）：闭包内每个成员只经自己的登记回应时，闭包之外的差别永不在闭包之内被登记。它把 `unregistered_beyond_registration` 与 `Clearing.alike_for_clearer` 都作为实例包含进来（B3、B4）。
5. **（乙，中等）阈值定理可以更精确。**
   - 关于第二个网的 `requires` 与 `need` 的假设是空转的（A0）。
   - 可以不用 `DecidableEq`，并允许多个储量的差别（A1、A2）。
   - 起作用的断裂是两网支持的**分岔**（较丰者支持、较贫者不支持），不是较贫者的失败。两者同时失败时，储量差别保持不动（A4、A6）。
   - 一步上的精确刻画：未观测的条件只登记它是否满足需要，被观测的条件登记它的水平（A8）。
6. **（出处，中等）** “Ren 于 10 月 11 日接受了这些读法”，以及“Ren 请 AI 决定自身水平”，都没有保存在任何来源文件中。计划仍写“待 Ren”。

**保留什么。** 全部 Lean 都保留。`Web.Refutes` 是对的“只凭记录”的否证概念，需要并列一个相对于模型的版本。阈值三定理在其假设下正确，`Gated` 是一个非平凡的见证。所及部分正确，作为 P42 的推广，增量不大。`tested_by_dweller` 正确且非空。`finite_reading_withholds_renewal` 正确，但它是一个推论（E），不是新的结果。

<a id="english-summary"></a>

---

<a id="0-范围与方法--scope-and-method"></a>
## 0. 范围与方法

<a id="1-形式复核--formal-recheck"></a>
## 1. 形式复核

- **`ProbeNames.lean`.**

---

<a id="2-发现--findings"></a>
## 2. 发现

<a id="f1乙重大视界读法关于整个运行的主张只在延续开放时不被有限记录判定--the-horizon-reading-whole-run-claims-are-undecided-by-a-finite-record-only-where-the-continuation-is-open"></a>
### F1（乙，重大）视界读法：关于整个运行的主张，只在延续开放时不被有限记录判定

**中文。** 模块说“每个有限的更新检验都在一侧出错”，读法说“关于整个运行的主张不被任何有限记录检验”。所引的定理是 `Renewable.prefix_does_not_decide`：在一个特定过程中，行动不被前缀固定。`Becoming.Horizon` 自己说：“在 `Renewable` 中，动力学由行动固定，所以没有前缀判定的是尚待采取的行动。”在 `Refutes` 的意义下（量化一切水平历史），尾部主张平凡地不被否证（C2）。相对于固定交换的模型，观测储量的形成在第 0 步就否证“储量会降到零”这一假主张（C3）。这时否证是对“模型且主张”的否证（C6），模型错误时会否证真主张（C4），而登记可以否证模型本身（C4b）。所以这条读法应改为：延续开放时，有限记录不判定整个运行；模型使之可检验，代价是检验只相对于模型，而模型自己必须可被登记否证。

<a id="f2甲丙重大阈下不见取决于-respondsthrough读法和-readme-没有写出它--threshold-blindness-rests-on-respondsthrough-which-the-readings-and-readme-omit"></a>
### F2（甲／丙，重大）阈下不见取决于 `RespondsThrough`，读法和 README 没有写出它

**中文。** `RespondsThrough` 不是 `g` 的回应方式，而是一个关于整个环境的假设：凡 `g` 登记的条件，所有在场形成在其上的总取用与总给予，在 `g` 登记相同时都相同。它排除了两类常见情形：其他形成直接回应储量的水平（开放渔场中丰富的鱼群招来更多船只），以及随水平而变的更新（逻辑斯谛再生）。`Attracting` 中，较丰的网（三单位）招来一个取用两单位的形成，`g` 在第 1 步就不被支持，而较贫的网仍支持它：较丰者先断（A7）。这里假设不成立，模块的定理不适用，所以不是对定理的反例；但它是对未加限定的读法的反例：“失控是收益被登记、损失直到断裂才被登记”，以及 README 那行“较丰储量的盈余只在较贫者不再支持之后才被动用”。

<a id="f3乙重大自身水平应经依存于自身登记而非默认为完全的量度prey-依赖一个省略--own-standing-should-register-through-self-bearing-not-as-a-default-gauge-prey-rests-on-an-omission"></a>
### F3（乙，重大）自身水平应经“依存于自身”登记，而非默认为完全的量度；`Prey` 依赖一个省略

**中文。** 见 §6。要点：
- 脊柱已有 `Web.SelfBearing`（依存于自身水平，需要为正）。在其下，自身水平与其他条件一样，只经支持阈值登记（`SelfPrey`，F3 探针）：一口一单位（二到一）在阈值之上，不被登记；一口两单位经支持登记；捕食者在影响闭包之内。
- `Prey` 的“捕食者在猎物的影响闭包之外”只因猎物不依存于自身。猎物在有无被咬时每一步都被支持、活跃（F2 探针），所以被登记的差别对猎物自己没有任何作用；捕食者以零水平活跃（不 `Embodied`）。
- 在 `ownStanding` 下，一个其储量就是自身水平的形成（如 `Gauged`，F1 探针）永不阈下不见；对自身的耗竭无法表达阈下不见，而同一储量若表示为所持条件（`Reserve` 的 `hold f`）则有阈下不见：登记取决于切分方式。

<a id="f4乙中等所及闭包的传递性在其余交换不变的比较中不起作用已检查回应性版本--the-closures-transitivity-is-idle-in-the-fixed-rest-comparison-a-responsive-version-is-checked"></a>
### F4（乙，中等）所及闭包的传递性在“其余交换不变”的比较中不起作用；已检查回应性版本

**中文。** `unregistered_beyond_registration` 用扣留水平比较，其余交换不变。在这一比较中，一个形成登记什么只取决于直接与它所登记者交换的成员（`admits_unreached`、`agrees_of_quiet`）；闭包只是让陈述对一个区域一致成立。P42 审查对影响闭包指出了同一点（P42 F2）。B1 给出闭包真正起作用的比较：两个平衡的流，同样的在场形成；一个区域在两个流中都对“经所登记者受影响”封闭；起点在成员所登记的一切上相同；每个成员在成员所登记的条件上的取用与给予只随它自己的登记而变。那么每个成员在每一步都同样登记，不论闭包之外的形成做什么、成员在无人登记的条件上做什么。P47 的定理（B3）与 `alike_for_clearer`（B4）都是它的实例：清除者的清除，是在其闭包中无人登记的条件上的行动。

<a id="f5乙中等阈值定理可以更精确断裂是分岔--the-threshold-theorem-sharpens-the-break-is-a-divergence"></a>
### F5（乙，中等）阈值定理可以更精确：断裂是分岔

**English.** (中文要点：第二个网的需要假设空转；无需 `DecidableEq`、可多储量；储量差别只在两网支持分岔之后改变；一步上的精确刻画。)

<a id="f6乙中等refutes-检验的是关于一条历史的主张我的行动造成什么是反事实的--refutes-tests-claims-about-one-history-what-an-act-does-is-counterfactual"></a>
### F6（乙，中等）`Refutes` 检验的是关于一条历史的主张；“我的行动造成什么”是反事实的

<a id="f7出处中等ren-接受没有来源记录--rens-acceptance-is-not-in-a-preserved-source"></a>
### F7（出处，中等）“Ren 接受”没有来源记录

<a id="f8乙次要引错的定理--mis-citations"></a>
### F8（乙，次要）引错的定理

<a id="f9乙次要视界对偶是推论--the-horizon-dual-is-a-corollary"></a>
### F9（乙，次要）视界对偶是推论

<a id="f10次要对-p42-的复用--reuse-of-p42"></a>
### F10（次要）对 P42 的复用

<a id="f11次要tested_by_dweller-近乎定义--tested_by_dweller-is-near-definitional"></a>
### F11（次要）`tested_by_dweller` 近乎定义

<a id="f12次要缺少到-becominginquiry-的桥--no-bridge-to-becominginquiry"></a>
### F12（次要）缺少到 `Becoming.Inquiry` 的桥

<a id="f13次要名字--names"></a>
### F13（次要）名字

---

<a id="3-建议的更强定理--proposed-stronger-theorems-all-checked"></a>
## 3. 建议的更强定理

---

<a id="4-读法评估--the-readings-question-7"></a>
## 4. 读法评估

---

<a id="5-名字--names-question-8"></a>
## 5. 名字

| Name | Assessment | Proposal |
|---|---|---|
| `RegistersAlike` | Acceptable. "Register" is measurement vocabulary (an instrument registers). It means "makes the same difference to `g` at `t`". | Keep. In Chinese, avoid 计入 and 登记; use 对 g 不可辨 or 在 g 中显现相同. |
| `AlikeUpTo` | Too generic in the `Web` namespace (alike in what?). | `RegistersAlikeUpTo`, or the observability term `IndistinguishableUpTo`. |
| `Refutes` | Acceptable as Popper's term. For formations without inquiry (the dweller), read it as "the registration excludes the claim". | Keep, and say so in the docstring. Optionally `Excludes` in the core, with "refutes" in prose. |
| `Registers` | Imprecise. For a dependence, `g` registers only the joint support bit, not `c`'s level (A8). | Keep and fix the docstring ("enters what registers in `g`: through support's threshold if depended on, its level if observed"), or `EntersRegistration`. |
| `RegisteredFrom` | Parallel to `AffectedBy`; fine. | Keep. |
| `WithinRegistration` | Parallel to `WithinInfluence`; fine. | Keep. |
| `RespondsThrough` | **Misleading.** It is a hypothesis on the totals of all formations' exchange on `g`'s registered conditions, not on `g`'s responses (F2). | `ExchangeFollows` or `FollowsRegistration`, with the docstring "the exchange on what `g` registers follows `g`'s registration". |
| `supportOnly` | Fine. It names the resulting registration. | Keep. |
| `ownStanding` | Fine as a name. It should be presented as one observation, a gauge of oneself (F3). | Keep, or `selfGauge`. |
| `threshold_blind` | "Blind" is a sensory metaphor; "subthreshold" is the scientific term (as in subthreshold stimuli). | `subthreshold_alike`. Chinese 阈下. |
| `surplus_untouched`, `surplus_after_break` | "Surplus" is economic vocabulary. "Reserve" is taken (`Becoming.Reserve`, a technical sense), and so are "margin" (`Margin`) and "excess" (joint excess). | `difference_kept` and `difference_changes_after_divergence` (A1, A4). |
| `Gauged` | Good. | Keep. |
| `Gated` | Reuses "gated" from gated renewal (`Continuation`, `section Gated`) and the support-gated law (`Horizon`, `Feedback.law`) for a different relation: drawing while supported. | `Thresholded` or `SupportDrawn`. |
| `Prey` | Ecological; fine. Revise the witness (F3). | Keep, plus `SelfPrey`. |
| `Ended` | Specific to the dweller and to step 2. | `DwellerEnded`. |
| `one_ne_two`, `two_ne_three` | Generic arithmetic exported at the root of `Becoming`. | Make them `private`, or use `by decide` in place (axiom-free, `ProbeNames`); avoid `nomatch` (it brings in `propext`). |
| `Web.admits_iff_supported` | Mirrors `Web.supported_iff_admits` (`Becoming.Admission`, one web) with a different statement (two agreeing webs). | `Web.admits_iff_supported_of_agree`. |

---

<a id="6-自身水平的决定--the-decision-on-own-standing-question-6"></a>
## 6. 自身水平的决定

---

<a id="7-修正清单按严重程度-corrections-in-order-of-severity"></a>
## 7. 修正清单（按严重程度）

2. **`RespondsThrough` (F2).**

---

<a id="8-探针文件--probe-files"></a>
## 8. 探针文件
