#!/usr/bin/env python3
"""Readings of L1, S1 and S2 decided on Ren's words of 18 October 2026 ("alright, generally agree, please make your
own pareto frontier decisions, and push the frontier - words are important, but i think you are capable"):
DELEGATED-CHOICES D40-D42 (English and Chinese editions), the chapter's labelled reading paragraphs, the work board
and the sources context. Every edit must match exactly once. usage (from the repository root): python3 -B apply_readings.py"""
import sys

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md'
WORDS = '../../../../sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md#rens-message-on-the-readings-of-l1-s1-and-s2'
REC = '../../../../theories/becoming/results/records/'
STUDY = 'BECOMING-RENEWAL-READING.md'
QUOTE = ('“alright, generally agree, please make your own pareto frontier decisions, and push the frontier - words are '
         'important, but i think you are capable”')

EDITS = {}

# ---------------------------------------------------------------- DELEGATED-CHOICES.md (English)
EN = RF + 'DELEGATED-CHOICES.md'
EDITS[EN] = [
    ("Every decision is **decided by the AI on Ren's delegation of 15 October 2026**, not Ren's own decision, and Ren can "
     "reverse any of them.",
     "Every decision is **decided by the AI on Ren's delegation of 15 October 2026**, not Ren's own decision, and Ren can "
     "reverse any of them. D40-D42 are decided on Ren's words of 18 October 2026 (section 12)."),
    ("| D39 | coupling strength and entanglement | adopted with exact scope, 识 itself Ren's; entanglement as the strength "
     "of coupling, not quantum entanglement |\n",
     "| D39 | coupling strength and entanglement | adopted with exact scope, 识 itself Ren's; entanglement as the strength "
     "of coupling, not quantum entanglement |\n"
     "| D40 | what an extrapolation given nothing fixes | adopted with exact scope: worlds a list holds; a reading is a "
     "function, not a model held |\n"
     "| D41 | enough under undetermined laws | adopted with exact scope: possible is what a course allows; the side of "
     "the process is not 无明 |\n"
     "| D42 | when the runs of a process settle | adopted with exact scope: not changing for ever is not settling; the "
     "analogy with D34 of form only |\n"),
    ("**What would change it.** Another reading of these terms by Ren; an actual learner whose learning these readings "
     "cannot represent.\n\n<a id=\"7-从关系开始的重建--the-relation-first-re-founding\"></a>",
     "**What would change it.** Another reading of these terms by Ren; an actual learner whose learning these readings "
     "cannot represent.\n\n"
     "<a id=\"d40-不被给予任何东西的外推所确定者--what-an-extrapolation-given-nothing-fixes\"></a>\n"
     "### What an extrapolation given nothing fixes\n\n"
     "**Decision.** Adopted with exact scope (L1, [record](" + REC + "what-an-extrapolation-given-nothing-fixes.md), "
     "[study section 173](" + STUDY + "#173-what-an-extrapolation-given-nothing-fixes-l1)). In every world a list holds, "
     "a prefix, given nothing, fixes the whole future through the map (`Learnable.ahead_fixes`), and a target is "
     "learnable exactly where it is, from some step on, a reading of that future (`Learnable.learnable_iff_reading`). "
     "So what the learner of `learnable_iff` is given beyond the prefix (`fromLaw`: the world and the target) serves "
     "only as a reading of a future the prefix already fixes, not as further access to the configurations. The witness "
     "that no learner given nothing rests on every learnable target (`Learnable.given_nothing_not_every`) is adopted as "
     "stated and called elementary: two constant targets in a one-configuration world; the content is what the prefix "
     "does fix. This is a formal side of Ren's correction of 16 October 2026 that selection “is about the cognitive "
     "model, not just record” ([words](../../../../sources/15-codex-theory-conversations/2026-10-16-selection-through-a-model.md)): "
     "the remembered past fixes the future through the map, and what it does not supply is the reading. The Lean name "
     "`reading` is kept: a function from futures through the map to values. Declined: (1) reading this beyond worlds a "
     "list holds, where over every course no prefix fixes the next value (`Learning.no_prefix_fixes_next`); (2) reading "
     "“a reading of the future” as a model some formation holds: the theorem says such a function exists, not that "
     "anything represents it.\n"
     "**Reasons.** The theorems state these with no premise; (1) is excluded by the theorem cited; (2) would add a "
     "premise of representation.\n"
     "**What would change it.** A form of the fixing beyond worlds a list holds (for instance with a bound on what is "
     "registered); a better name than `reading`.\n\n"
     "<a id=\"d41-不确定之律下够的边界--the-boundary-of-enough-under-undetermined-laws\"></a>\n"
     "### The boundary of enough under undetermined laws\n\n"
     "**Decision.** Adopted with exact scope (S1, [record](" + REC + "the-boundary-of-enough-under-undetermined-laws.md), "
     "[study section 174](" + STUDY + "#174-the-boundary-of-enough-under-undetermined-laws-s1)). Enough is a relation of "
     "the process with the target, not a property of the target alone. Possible enough: some run from a configuration "
     "comes to rest with its target met exactly where a reachable configuration meets the target and has a step that "
     "stays (`Enough.possibly_rests_iff`). Assured enough: every run does exactly where, besides, every reachable "
     "configuration with a step that stays meets the target and every run settles, a part that does not mention the "
     "target (`Enough.assured_iff`). “Possible” is not read as what a seeker can bring about: it is what some course of "
     "the process allows, whatever settles which course is taken (at a parting, the situation, D34); what a part of the "
     "unfolding can assure while the rest stays undetermined is not stated, since `Becoming.Enough` does not divide a "
     "step between a part and the rest. 无明 is not widened: its D26 reading concerns the target, one that cannot be "
     "met at rest; failing to rest because runs keep changing is a failure on the side of the process, named by its "
     "structure (D42) and not counted as 无明, which is Ren's term (section 10).\n"
     "**Reasons.** The theorems' readings; the readings declined would add a premise (a chooser of the course) or "
     "extend Ren's term.\n"
     "**What would change it.** Ren reading 无明 to include the side of the process; a theorem of enough where the step "
     "is divided between a part and the rest.\n\n"
     "<a id=\"d42-过程的运行何时安定--when-the-runs-of-a-process-settle\"></a>\n"
     "### When the runs of a process settle\n\n"
     "**Decision.** Adopted with exact scope (S2, [record](" + REC + "when-the-runs-of-a-process-settle.md), "
     "[study section 175](" + STUDY + "#175-when-the-runs-of-a-process-settle-s2)). In a world a list holds, whether "
     "some run keeps changing is a property of the process: exactly where a reachable change can be undone "
     "(`Settling.keeps_changing_iff`). That runs do not change for ever does not give a step from which they settle; "
     "that gap is the limited principle of omniscience, already for two configurations "
     "(`Settling.OneWay.never_keeps_changing`, `Settling.OneWay.lpo_of_settles`). Read: in a finite world the process "
     "decides whether its runs keep changing, but knowing that a run will not change for ever is not knowing when it "
     "has stopped. D34's learner with finitely many states and no bound rests at a step it can never certify; the "
     "likeness is adopted as an analogy of form, not an identification. Names: “settle” means unchanged from some step "
     "on, as in `Becoming.Frequency`; “come to rest” adds the target met.\n"
     "**Reasons.** The theorems; the strength is exact (keeping changing on the process, settling at the limited "
     "principle of omniscience), so the reading adds nothing.\n"
     "**What would change it.** A constructive settling theorem under a premise the core accepts; a name Ren prefers "
     "for settling.\n\n"
     "<a id=\"7-从关系开始的重建--the-relation-first-re-founding\"></a>"),
    ("- The proofs pushed under the same delegation: P111 `Becoming.Gain` (where novelty's gain comes from) and P112 "
     "`Becoming.Gluing` (when readings in context glue, for parity constraints), in their records and the study.",
     "- The proofs pushed under the same delegation: P111 `Becoming.Gain` (where novelty's gain comes from) and P112 "
     "`Becoming.Gluing` (when readings in context glue, for parity constraints), in their records and the study.\n"
     "- Ren's words of 18 October 2026 on the readings of L1, S1 and S2, " + QUOTE + " ([words](" + WORDS + ")), read "
     "as general agreement with the readings as the AI explained them and as delegating their wording and scope: "
     "D40-D42."),
]

# ---------------------------------------------------------------- DELEGATED-CHOICES.zh.md (Chinese edition)
ZH = RF + 'DELEGATED-CHOICES.zh.md'
EDITS[ZH] = [
    ("每项决定是 **AI 依 Ren 2026-10-15 的交托决定**，不是 Ren 自己的决定；Ren 可以改其中任何一项。",
     "每项决定是 **AI 依 Ren 2026-10-15 的交托决定**，不是 Ren 自己的决定；Ren 可以改其中任何一项。D40-D42 依 Ren "
     "2026-10-18 的话决定（§12）。"),
    ("| D39 | 耦合强度与纠缠 | 以确切范围采用，识本身属 Ren；纠缠读作耦合的强度，不等同于量子的纠缠 |\n",
     "| D39 | 耦合强度与纠缠 | 以确切范围采用，识本身属 Ren；纠缠读作耦合的强度，不等同于量子的纠缠 |\n"
     "| D40 | 不被给予任何东西的外推所确定者 | 以确切范围采用：由一个列表容纳的世界；读法是函数，不是被持有的模型 |\n"
     "| D41 | 不确定之律下的够 | 以确切范围采用：可能是某一进程所允许者；过程一侧不是无明 |\n"
     "| D42 | 过程的运行何时安定 | 以确切范围采用：不永远变化不是安定；与 D34 的相似只在形式上 |\n"),
    ("**会改变它的。** Ren 对这些用语的另一读法；一个实际的学习者，其学习不能由这些读法表示。\n\n"
     "<a id=\"7-从关系开始的重建--the-relation-first-re-founding\"></a>",
     "**会改变它的。** Ren 对这些用语的另一读法；一个实际的学习者，其学习不能由这些读法表示。\n\n"
     "<a id=\"d40-不被给予任何东西的外推所确定者--what-an-extrapolation-given-nothing-fixes\"></a>\n"
     "### D40. 不被给予任何东西的外推所确定者\n\n"
     "所在：理论“学习者经其识所能学者”的 L1 各条与第 8.2 节“学习”一行；[what-an-extrapolation-given-nothing-fixes]("
     + REC + "what-an-extrapolation-given-nothing-fixes.md) 的读法；研究第 173 节。\n\n"
     "**决定。** 以确切范围采用。在每个由一个列表容纳的世界中，不被给予任何东西，一个前缀确定经映射的整个未来"
     "（`Learnable.ahead_fixes`）；一个目标可学，恰当它从某步起是对那个未来的一个读法（`Learnable.learnable_iff_reading`）。"
     "所以 `learnable_iff` 的学习者在前缀之外被给予的（`fromLaw`：世界与目标），只作为对前缀已确定的未来的一个读法，"
     "不是对构形的更多通达。没有不被给予任何东西的学习者静止于每个可学目标，其见证（`Learnable.given_nothing_not_every`）"
     "按原样采用，并称为初等的：单构形世界中的两个常值目标；内容在于前缀确实确定的东西。这是 Ren 2026-10-16 之更正"
     "的一个形式侧面：选择“is about the cognitive model, not just record”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-16-selection-through-a-model.md)）："
     "记住的过去确定经映射的未来，它不提供的是读法。Lean 名称 `reading` 保留：从经映射的未来到值的函数。不采用："
     "（1）把它读到列表容纳的世界之外，那里在每个进程上没有前缀确定下一个值（`Learning.no_prefix_fixes_next`）；"
     "（2）把“对未来的一个读法”读作某个构成所持有的模型：定理说的是这样的函数存在，不是有什么表示它。\n"
     "**理由。** 定理不加前提地陈述这些；（1）为所引定理排除；（2）会加一个表示的前提。\n"
     "**会改变它的。** 在列表容纳的世界之外的确定形式（例如对所识者给一个界）；比 `reading` 更好的名称。\n\n"
     "<a id=\"d41-不确定之律下够的边界--the-boundary-of-enough-under-undetermined-laws\"></a>\n"
     "### D41. 不确定之律下够的边界\n\n"
     "所在：理论“无明的边界条件”中“不确定之律下的够”一条；[the-boundary-of-enough-under-undetermined-laws]("
     + REC + "the-boundary-of-enough-under-undetermined-laws.md) 的读法；研究第 174 节。\n\n"
     "**决定。** 以确切范围采用。够是过程与目标的关系，不只是目标的性质。可能之够：从一个构形的某次运行静止且目标被满足，"
     "恰当某个可达构形满足目标且有一步停留（`Enough.possibly_rests_iff`）。确保之够：每次运行都如此，恰当此外每个有停留"
     "之步的可达构形都满足目标，且每次运行都安定；后一部分不提目标（`Enough.assured_iff`）。“可能”不读作寻求者所能促成者："
     "它是过程的某一进程所允许者，无论什么决定走哪一进程（在分开之处，是情境，D34）；在其余仍不确定时展开的一部分能确保"
     "什么，没有陈述，因为 `Becoming.Enough` 不把一步分为一部分与其余。无明不被扩大：D26 对它的读法关乎目标，即静止时不能"
     "达到的目标；因运行不断变化而不能静止，是过程一侧的失败，以其结构命名（D42），不算作无明；无明是 Ren 的用语（§10）。\n"
     "**理由。** 定理的读法；不采用的读法会加一个前提（选择进程者）或扩大 Ren 的用语。\n"
     "**会改变它的。** Ren 把无明读作包括过程一侧；一步在一部分与其余之间划分时的够的定理。\n\n"
     "<a id=\"d42-过程的运行何时安定--when-the-runs-of-a-process-settle\"></a>\n"
     "### D42. 过程的运行何时安定\n\n"
     "所在：理论“无明的边界条件”中“运行何时安定”一条；[when-the-runs-of-a-process-settle]("
     + REC + "when-the-runs-of-a-process-settle.md) 的读法；研究第 175 节。\n\n"
     "**决定。** 以确切范围采用。在由一个列表容纳的世界中，某次运行是否不断变化是过程的性质：恰当某个可达的变化可被撤回"
     "（`Settling.keeps_changing_iff`）。运行不永远变化，并不给出它们自此安定的一步；这一差距是有限全知原理，两个构形时已然"
     "（`Settling.OneWay.never_keeps_changing`、`Settling.OneWay.lpo_of_settles`）。读作：在有限的世界中，过程决定其运行是否"
     "不断变化，但知道一次运行不会永远变化，不是知道它何时已停。D34 中有有限多个状态而没有界的学习者，静止于它永远不能确证"
     "的一步；这一相似作为形式上的类比采用，不是等同。名称：“安定”指自某步起不变，如 `Becoming.Frequency`；“静止”另加目标被满足。\n"
     "**理由。** 定理；强度是精确的（不断变化在过程上，安定在有限全知原理），所以读法不加任何东西。\n"
     "**会改变它的。** 在核心接受的前提下的构造性安定定理；Ren 对安定更喜欢的名称。\n\n"
     "<a id=\"7-从关系开始的重建--the-relation-first-re-founding\"></a>"),
    ("- 同一交托之下推进的证明：P111 `Becoming.Gain`（新的增益从哪里来）与 P112 `Becoming.Gluing`（奇偶约束下语境中的读法何时粘合），"
     "见其记录与研究。",
     "- 同一交托之下推进的证明：P111 `Becoming.Gain`（新的增益从哪里来）与 P112 `Becoming.Gluing`（奇偶约束下语境中的读法何时粘合），"
     "见其记录与研究。\n"
     "- Ren 2026-10-18 对 L1、S1、S2 读法的话，" + QUOTE + "（[原话](" + WORDS + ")），读作对 AI 所解释的读法的总体同意，"
     "并交托其措辞与范围：D40-D42。"),
]

# ---------------------------------------------------------------- the chapter
LEARNABLE_READINGS = ("*Readings* [AI reading, D26]. Registration bounds what is learned. This is the not-seeing below "
                      "threshold of `Becoming.Testing`, stated for learners; what lies beyond registration is reached only "
                      "by widening it. Record: [learnable-through-registration](../results/records/learnable-through-registration.md). "
                      "Study: [section 119](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/"
                      "BECOMING-RENEWAL-READING.md#119-经其识所能学者).")
WUMING_READINGS_END = ("Records: [seeking-boundary](../results/records/seeking-boundary.md), "
                       "[target-capture](../results/records/target-capture.md). Study: [section 83](../../../_process/research/"
                       "2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#83-无明的边界条件寻求何处能静止于够p62).")
SR = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
EDITS[CHAPTER] = [
    (" On the sufficiency side the learner given only the reading learns the target (`Learnable.reading_rests_from`). "
     "So what `fromLaw` is given beyond the prefix is exactly a reading of the future through the map.",
     " On the sufficiency side the learner given only the reading learns the target (`Learnable.reading_rests_from`)."),
    (" with the same prefixes (`Learnable.given_nothing_not_every`). The witness is elementary; the content is what the "
     "prefix does fix. The same three hold",
     " with the same prefixes (`Learnable.given_nothing_not_every`). The same three hold"),
    (LEARNABLE_READINGS,
     LEARNABLE_READINGS + "\n\n*Reading* [AI reading, D40]. The prefix alone fixes the future through the map; what a "
     "learnable target adds to it is a reading of that future, which a learner given nothing does not have. So what "
     "`fromLaw` is given beyond the prefix serves only as a reading of a future the prefix already fixes. The witness "
     "that no learner given nothing rests on every learnable target is elementary; the content is what the prefix does "
     "fix. This holds in worlds a list holds: over every course, no prefix fixes the next value. Record: "
     "[what-an-extrapolation-given-nothing-fixes](../results/records/what-an-extrapolation-given-nothing-fixes.md). "
     "Study: [section 173](" + SR + "BECOMING-RENEWAL-READING.md#173-what-an-extrapolation-given-nothing-fixes-l1)."),
    (WUMING_READINGS_END,
     WUMING_READINGS_END + "\n\n*Readings* [AI reading, D41, D42]. Enough is a relation of the process with the target. "
     "Possible enough is what some course allows, whatever settles which course is taken, not what a seeker can bring "
     "about; assured enough adds a part of the process alone, that every run settles. Failing to rest therefore has two "
     "sources: the target, one that cannot be met at rest, which is 无明 as read above; and the process, runs that keep "
     "changing, which is not 无明 and is named by its structure, a reachable change that can be undone. In a world a "
     "list holds the process decides whether its runs keep changing, but knowing that a run will not change for ever "
     "is not knowing when it has stopped. Records: [the-boundary-of-enough-under-undetermined-laws](../results/records/"
     "the-boundary-of-enough-under-undetermined-laws.md), [when-the-runs-of-a-process-settle](../results/records/"
     "when-the-runs-of-a-process-settle.md). Study: [section 174](" + SR + "BECOMING-RENEWAL-READING.md#174-the-boundary-"
     "of-enough-under-undetermined-laws-s1), [section 175](" + SR + "BECOMING-RENEWAL-READING.md#175-when-the-runs-of-a-"
     "process-settle-s2)."),
]

# ---------------------------------------------------------------- the work board
EDITS[BOARD] = [
    ("| L1 Unrolling: given nothing, the prefix fixes the whole future through the map; what a learnable feature adds is "
     "exactly a reading of that future, not more access to the configurations; so no learner given nothing learns every "
     "learnable feature | [record](../theories/becoming/results/records/what-an-extrapolation-given-nothing-fixes.md); "
     "chapter section \"What a learner can learn through its registration\" |\n", ""),
    ("| S1 Enough: under undetermined laws what can come to rest and what must part; what must has a part about the "
     "target (every reachable stay meets it) and a part of the process alone (every run settles), so seeking can fail "
     "to rest where every configuration would be enough | [record](../theories/becoming/results/records/"
     "the-boundary-of-enough-under-undetermined-laws.md); chapter \"The boundary condition for 无明\", \"Enough under "
     "undetermined laws\" |\n", ""),
    ("| S2 Settling: whether runs keep changing is, in a world a list holds, a property of the process (a reachable "
     "change that can be undone); never changing for ever is not settling, which is the limited principle of omniscience "
     "already for two configurations | [record](../theories/becoming/results/records/when-the-runs-of-a-process-settle.md); "
     "chapter \"The boundary condition for 无明\", \"When the runs settle\" |\n", ""),
]

# ---------------------------------------------------------------- the sources context
EDITS[SOURCE] = [
    ("- Ren's own terms stay Ren's (DELEGATED-CHOICES section 10): the decisions do not extend 无明.",
     "- Ren's own terms stay Ren's (DELEGATED-CHOICES section 10): the decisions do not extend 无明.\n"
     "- The decisions are DELEGATED-CHOICES D40 (L1), D41 (S1) and D42 (S2), with the chapter's reading paragraphs "
     "labelled \"AI reading, D40\" and \"AI reading, D41, D42\"; the three rows leave the work board's \"Decisions "
     "pending Ren\"."),
]

BOARD_ROWS = [('what-an-extrapolation-given-nothing-fixes', 'D40'),
              ('the-boundary-of-enough-under-undetermined-laws', 'D41'),
              ('when-the-runs-of-a-process-settle', 'D42')]


def board_row_endings(text):
    """The L1, S1 and S2 claim rows end with "reading pending Ren"; each becomes "reading decided (Dnn)"."""
    lines = text.split('\n')
    done = 0
    for i, line in enumerate(lines):
        if not line.startswith('| **'):
            continue
        for slug, d in BOARD_ROWS:
            if f'records/{slug}.md' in line and line.count('reading pending Ren |') == 1:
                lines[i] = line.replace('reading pending Ren |', (
                    f"reading decided ({d}, DELEGATED-CHOICES; Ren 18 October: \"alright, generally agree, please make "
                    f"your own pareto frontier decisions\") |"))
                done += 1
    if done != 3:
        sys.exit(f'board rows: expected 3, found {done}')
    return '\n'.join(lines)


MARK = {EN: '| D40 |', ZH: '| D40 |', CHAPTER: '[AI reading, D40]', BOARD: '(D40, DELEGATED-CHOICES;',
        SOURCE: 'DELEGATED-CHOICES D40 (L1)'}
for path, edits in EDITS.items():
    text = open(path, encoding='utf-8').read()
    if MARK[path] in text:
        print('already edited', path)
        continue
    for old, new in edits:
        n = text.count(old)
        if n != 1:
            sys.exit(f'{path}: expected one match, found {n}: {old[:90]!r}')
        text = text.replace(old, new)
    if path == BOARD:
        text = board_row_endings(text)
    open(path, 'w', encoding='utf-8').write(text)
    print('edited', path, len(edits))
