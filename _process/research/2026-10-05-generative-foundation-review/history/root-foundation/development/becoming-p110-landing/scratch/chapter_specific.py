import sys
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
DC='../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
SRC='../../../sources/15-codex-theory-conversations/2026-10-15-delegated-choices.md'
Z='依 Ren 2026-10-15 的交托'
E="on Ren's delegation of 15 October 2026"
def d(n): return f'[{n}]({DC})'
R=[
# legend
('**读法**（属于 Ren 的选择）', f'**读法**（AI {Z}决定，Ren 可改；仍属 Ren 者见第 8 节，[决定记录]({DC})）'),
("a **reading** (Ren's choice)", f"a **reading** (decided by the AI {E}, which Ren may reverse; what stays Ren's is in section 8, [decision record]({DC}))"),
('the other readings pending Ren)', f'the other readings adopted {E})'),
# generative/degenerative, line 77/110
('Ren 提议中的“生成的”“退化的”指哪个部分由 Ren 选择：', f'Ren 提议中的“生成的”“退化的”指部分对能形成者的扩大与缩小，在形成的层次上是更新的形成与消耗的形成（§6.13；AI {Z}决定，{d("D2")}）：'),
('；若取不重叠，二者在有限世界中重合的活动读法就不是其所指（AI 的推论）；', '；二者在有限世界中重合的活动读法所以不是其所指；'),
("Which parts the proposal's ‘generative’ and ‘degenerative’ name is Ren's to choose: ", f"The proposal's ‘generative’ and ‘degenerative’ name a part's widening and narrowing of what can form, and at the level of formations renewing and consuming formations (section 6.13; decided by the AI {E}, {d('D2')}): "),
("; if non-overlap is taken, the activity reading, on which the two coincide in finite worlds, is not what is meant (the AI's inference); ", "; so the activity reading, on which the two coincide in finite worlds, is not what is meant; ", 2),
# line 273/277
('；提议中的“生成的”“退化的”指哪个部分由 Ren 选择。', f'；提议中的“生成的”“退化的”指部分对能形成者的扩大与缩小，不指活动的读法（AI {Z}决定，{d("D2")}）。'),
('；若取不重叠，在有限世界中重合的活动读法就不是其所指（AI 的推论）；', '；在有限世界中重合的活动读法所以不是其所指；'),
("; which parts the proposal's ‘generative’ and ‘degenerative’ name is Ren's to choose.", f"; the proposal's ‘generative’ and ‘degenerative’ name a part's widening and narrowing of what can form, not the activity reading (decided by the AI {E}, {d('D2')})."),
('但 `selfDrawing` 的不活只在逐步读法对终结之步自我汲取的判定之下成立，这一判定属于 Ren。', f'但 `selfDrawing` 的不活只在逐步读法对终结之步自我汲取的判定之下成立；这一判定是逐步读法的定理，比较不用它（AI {Z}决定，{d("D6")}）。'),
("but `selfDrawing` fails to be living only on the stepwise verdict about self-drawing at an ending, which is Ren's to choose.", f"but `selfDrawing` fails to be living only on the stepwise verdict about self-drawing at an ending; that verdict is a theorem of the stepwise reading, which no comparison uses (decided by the AI {E}, {d('D6')})."),
# line 89/122
('；这样的侵蚀是否计入不活由 Ren 选择）', f'；这样的侵蚀不作为对汲取者的估值，由可能性的比较计入，AI {Z}决定，{d("D6")}）'),
("; whether such undermining counts against living is Ren's to choose)", f"; such undermining is no verdict on the drawer and is counted by the comparison on possibilities, decided by the AI {E}, {d('D6')})"),
('AI 把立场中立读作提议的唯一公理，待 Ren。', f'AI 把立场中立读作提议的唯一公理，{Z}采用（§6.8 中它由不受限的意义推出）。'),
("the AI reads standpoint neutrality as the proposal's one axiom, pending Ren.", f"the AI reads standpoint neutrality as the proposal's one axiom, adopted {E} (in section 6.8 it follows from unrestricted significance)."),
('其余是定理；读法的选择属于 Ren；重述待 Ren 接受〕', f'其余是定理；读法{Z}由 AI 决定；重述是否替代 G0 已由折叠回答〕'),
("the rest are theorems; the choice of readings is Ren's; the restatement awaits Ren's acceptance]", f"the rest are theorems; the readings are decided by the AI {E}; whether the restatement replaces G0 is answered by the fold]"),
# line 93
('“生”与“生生”的读法属于 Ren；', f'“生”与“生生”的读法{Z}由 AI 决定（生生读作生成的空间，{d("D1")}）；'),
# premise table rows
('公开的读法选择，由 Ren 决定（§6.3）；是否即生生，是哲学论证', f'公开的读法选择（§6.3）；比较不用它，生生读作生成的空间（AI {Z}决定，{d("D1")}）；是否即生生，是哲学论证'),
('S0 是否即“想要”的读法依 Ren 2026-10-15 的交托采用（§6.7）', f'S0 即“想要”的读法（AI {Z}决定，§6.7，{d("D11")}）'),
('每个想要之点都是中心（§6.7），待 Ren；', f'每个想要之点都是中心（§6.7），{Z}采用；'),
('S0 加 N_rel 亦可）；待 Ren。§6.8', f'S0 加 N_rel 亦可）；{Z}采用 N_std（{d("D11")}）。§6.8'),
# succession, 生生不息
('接续怎样读、“生生不息”读到哪个层次，属于 Ren。', f'接续经延续的已形成关系读，“生生不息”读在整体的层次，即经更新而复现的生起（AI {Z}决定，{d("D5")}）。'),
("and the reading of succession is Ren's;", f"and succession is read through the formed relations of continuation (decided by the AI {E}, {d('D5')});"),
# stepwise candidate
('四次独立审查之后的工作候选（待 Ren 选择）是“活跃且不侵蚀”', f'四次独立审查之后的工作读法（AI {Z}保留，{d("D10")}）是“活跃且不侵蚀”'),
("the working candidate after four independent reviews, pending Ren's choice, an event lives", f"the working reading after four independent reviews, kept {E} ({d('D10')}), an event lives"),
("the scope of the second 生 is Ren's.", f"the scope of the second 生 is what can form, decided by the AI {E} ({d('D3')})."),
# embodiment
('在把体现的关系项读作“生”这一属于 Ren 的读法下', f'在把体现的关系项读作“生”这一读法下（AI {Z}采用，{d("D4")}）'),
('是否应如此、对哪些汲取者，属于 Ren 对生生的读法。', f'这是逐步读法的判定；它不作为对汲取者的估值，比较以可能性进行（AI {Z}决定，{d("D6")}）。'),
("taking embodied relata as 生, a reading that is Ren's,", f"taking embodied relata as 生, a reading adopted {E} ({d('D4')}),"),
("Whether it should be, and for which drawers, is Ren's reading.", f"This is the stepwise reading's verdict; it is no valuation of the drawer, and comparison is on possibilities (decided by the AI {E}, {d('D6')})."),
# 473
('保持的读法及把守恒读作延续属于 AI 的解释，待 Ren；', f'保持的读法及把守恒读作延续属于 AI 的解释，{Z}采用；'),
# living on and descent
('是否采用它们属于 Ren；`living` 与 C 不变', f'{Z}，它们采用为延续的已形成关系，不作为直接的估值（{d("D9")}）；`living` 与 C 不变'),
("Adopting them is Ren's choice, and neither living nor C changes.", f"{E[0].upper()+E[1:]}, they are adopted as formed relations of continuation, not as direct valuations ({d('D9')}), and neither living nor C changes."),
('**读法由 Ren 选择。** 独立审查判定', f'**读法（AI {Z}决定，{d("D1")}、{d("D10")}）。** 独立审查判定'),
("Which reading, or combination, is the reading of 生生 is Ren's choice; the study's comparison supplies the material.", f"Which reading, or combination, is the reading of 生生 was decided by the AI {E}: 生生 reads as the generative space, and comparison uses no reading of `living` ({d('D1')}); the study's comparison supplied the material."),
# 6.7 heading + anchor
('### 6.7 从想要延续者重述（Ren 的提议，待定）/ Restating from what wants its continuation (Ren\'s proposal, pending)', '<a id="67-从想要延续者重述ren-的提议待定--restating-from-what-wants-its-continuation-rens-proposal-pending"></a>\n\n### 6.7 从想要延续者重述（Ren 的提议）/ Restating from what wants its continuation (Ren\'s proposal)'),
('把 S0 读作“想要”、把 N_std 读作那条公理，是 AI 对提议的读法，待 Ren 判断。', f'把 S0 读作“想要”、把 N_std 读作那条公理，是 AI 对提议的读法，{Z}采用（{d("D11")}）。'),
('；读法与名称属于 Ren；是否替代 G0，已由 G0 的折叠回答（§5）。', f'；读法与名称{Z}由 AI 决定；是否替代 G0，已由 G0 的折叠回答（§5）。'),
("is the AI's reading of the proposal, pending Ren.", f"is the AI's reading of the proposal, adopted {E} ({d('D11')})."),
("; readings and names are Ren's, and whether it replaces G0 is answered by the fold (section 5).", f"; readings and names are decided by the AI {E}, and whether it replaces G0 is answered by the fold (section 5)."),
('是否采用属于 Ren，如以之为生与世系。', f'{Z}，它采用为已形成的关系，如以之为生与世系（{d("D12")}）。'),
("; adopting it is Ren's choice.", f"; {E}, it is adopted as a formed relation, as living on and descent are ({d('D12')})."),
('这一读法尚未形式化，两种读法由 Ren 选择。强式对整体：延续要创造更多的意义，即 G0 的继续生成，读作方向（`Flow.More`、`World.ArisingRecurs`）；', f'这一读法尚未形式化；{Z}，AI 决定两者都不取：不损读作保留，是有与无一个部分的水平之间的关系（§6.8，{d("D13")}）。强式对整体：延续要创造更多的意义，即 G0 的继续生成，读作方向（`Flow.More`、`World.ArisingRecurs`；{Z}，“更多”读作扩大能形成者，{d("D15")}）；'),
("not yet formalized, and the choice is Ren's; the strong form for the whole, continuation is to create more significance, G0's further generation read as a direction (`Flow.More`, `World.ArisingRecurs`),", f"not yet formalized; {E} the AI takes neither: not harm reads as retaining, a relation between the levels with and without a part (section 6.8, {d('D13')}); the strong form for the whole, continuation is to create more significance, G0's further generation read as a direction (`Flow.More`, `World.ArisingRecurs`; {E}, “more” reads as widening what can form, {d('D15')}),"),
('**重述的草案（供 Ren 判断，未被接受）。**', '**重述的草案（照原样保留；§6.8 依 Ren 后来的回答重读了公理，G0 已折叠）。**'),
('- **Draft for Ren to judge, not accepted:**', "- **Draft, kept as written (section 6.8 rereads the axiom after Ren's later answers, and G0 is folded):**"),
('**仍待 Ren。** S0 是否即“想要”的读法（这样读时种子已含“不损”的过滤）；推出的范围沿依存还是沿每个已形成的关系（后者在某些整体中推出中心）；“不损”是对延续的过滤还是对他者的要求；公理的范围是“想要延续者”还是“任何东西”（无人持有的生命：休眠的种子、昏迷、不再想继续的人）；伤害读在哪个层次（个体、谱系、整体）；“更多”的读法；输送是否算已形成的关系；名称。',
 f'**{Z}决定（[决定记录]({DC}) D11–D15、D36）。** S0 是“想要”的读法（这样读时种子已含“不损”的过滤）；推出的范围向后沿依存、向前沿所及，每个已形成的关系只经 N_rel 进入；“不损”读作保留，既不是对延续的过滤，也不是对他者的要求；公理的范围是“任何东西”，如 Ren 的原话（无人持有的生命：休眠的种子、昏迷、不再想继续的人，其意义不决定任何人该做什么）；伤害读在整体的层次，较弱的版本在所在的系统之内，然后是自身（Ren 2026-10-10 的回答），形成以谱系归类，成员的终结仍是损失；“更多”读作方向，即扩大；输送是已形成的关系；名称在陈述有其确切意义处采用。'),
("- **Still Ren's:** whether S0 is the reading of wanting (so read, the seed carries the not-harm filter); whether the derived extent runs along dependence or along every formed relation (the latter derives the center in some wholes); whether “not harm” filters continuations or claims on others; whether the axiom ranges over what wants or over anything (unheld lives: a dormant seed, a coma, someone who no longer wants to go on); the level of harm; the reading of “more”; whether conveyance is a formed relation; names.",
 f"- **Decided {E}** ([decision record]({DC}), D11–D15, D36): S0 is the reading of wanting (so read, the seed carries the not-harm filter); the derived extent runs backward along dependence and forward along reach, every formed relation entering only through N_rel; “not harm” reads as retaining, neither a filter on continuations nor a claim on others; the axiom ranges over anything, as Ren's words say (unheld lives: a dormant seed, a coma, someone who no longer wants to go on, whose significance decides nothing about what anyone should do); harm is read at the whole, a weaker version within the system one is in, then the self (Ren's answer of 10 October 2026), formations being classed as lineages while a member's ending stays a loss; “more” reads as a direction, widening; conveyance is a formed relation; names are adopted where the statement has their exact meaning."),
# not harm retaining
('这两种“不损”的读法不同；G0 的 `living` 指哪一种，属于 Ren。', f'这两种“不损”的读法不同；{Z}，不损读作保留（AI 的决定，{d("D13")}）。'),
("The two readings of not harm differ, and which one G0's `living` names is Ren's choice.", f"The two readings of not harm differ; {E}, not harm reads as retaining (the AI's decision, {d('D13')})."),
# order of levels
('这一方向是否合适，由 Ren 判断。', f'这一方向{Z}采用（{d("D21")}）。'),
("Whether this direction fits is Ren's to judge.", f"This direction is adopted {E} ({d('D21')})."),
# entropy
('哪一个量叫作熵，历史还是守恒量中的记录，由 Ren 决定。', f'叫作熵的是守恒量中的记录，不是历史（AI {Z}决定，{d("D29")}）。'),
("Which quantity is called entropy, the history or the record in the conserved amount, is Ren's decision.", f"The quantity called entropy is the record in the conserved amount, not the history (decided by the AI {E}, {d('D29')})."),
# 1106/1190
('是待 Ren 确认的 AI 读法（§2）。', f'是 AI {Z}采用的读法（§2，{d("D2")}）。'),
("is an AI reading pending Ren (section 2).", f"is an AI reading adopted {E} (section 2, {d('D2')})."),
# section 8 legend
('每个开放项归入四类之一：属于 Ren 的选择、哲学根据、经验对应、进一步的证明。', f'每个开放项归入四类之一：属于 Ren 的、哲学根据、经验对应、进一步的证明。先前列为 Ren 的选择的读法与名称，Ren 2026-10-15 交 AI 以其最好的判断决定（[原话]({SRC})），决定连同理由与会改变它们的东西在[决定记录]({DC})中；仍属 Ren 的在下面列出。'),
("Every open item is then placed in one of four classes: Ren's choice, philosophical warrant, empirical correspondence, or a further proof.", f"Every open item is then placed in one of four classes: Ren's, philosophical warrant, empirical correspondence, or a further proof. The readings and names formerly listed as Ren's choices were left by Ren on 15 October 2026 to the AI's best judgement ([words]({SRC})); the decisions, with their reasons and what would change them, are in the [decision record]({DC}), and what stays Ren's is listed below."),
# table rows
('；把这些读作生成、退化与中性由 Ren 判断 |', f'。扩大、缩小与保持读作生成、退化与中性（AI {Z}决定，{d("D2")}） |'),
('；Ren 提议中的“生成的”“退化的”指什么由 Ren 选择）', f'；Ren 提议中的“生成的”“退化的”不指它，AI {Z}决定，{d("D2")}）'),
('；是否接受属于 Ren；是否替代 G0，已由 G0 的折叠回答（§5） |', f'；读法{Z}采用（{d("D11")}、{d("D12")}）；是否替代 G0，已由 G0 的折叠回答（§5） |'),
('。开放：路线 (b) 是否足够属于 Ren；中心怎样表示其闭包；', f'。路线 (b) 不足以达到 G0 的辖域，两者都保留（AI {Z}决定，{d("D18")}）。开放：中心怎样表示其闭包；'),
('。开放：所及闭包是否读出“the system that one is in”，属于 Ren；他者有回应的比较须给出第二个流；', f'。所及闭包读出“the system that one is in”（AI {Z}决定，{d("D20")}）。开放：他者有回应的比较须给出第二个流；'),
# spine row and glossary
('；“生成的”“退化的”的读法属于 Ren | 65 |', f'；“生成的”“退化的”不指活动的读法（AI {Z}决定，{d("D2")}） | 65 |'),
('它是 related 的一种候选读法（由 Ren 选择）', f'它是 related 的一种读法，{Z}采用为已形成的关系（{d("D12")}）'),
('，怎样读属于 Ren |', f'，经延续的已形成关系读（AI {Z}决定，{d("D5")}） |'),
('；所指的空间部分由 Ren 选择。一种关系读法是更新的形成与消耗的形成，作为关系不重叠。', f'；AI {Z}决定它们指部分对能形成者的扩大与缩小，在形成的层次上是更新的形成与消耗的形成，作为关系不重叠（{d("D2")}）。'),
('；是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（若取不重叠则不是，AI 的推论） |', f'；不是 Ren 提议中的“生成的”“退化的”：二者不重叠，而它们在有限世界中重合（AI {Z}决定，{d("D2")}） |'),
('；指在有限家族之外的交换还是流入由 Ren 选择 |', f'；指在每个有限家族之外的交换，流入是增益，另行陈述（AI {Z}决定，{d("D7")}） |'),
('（AI 把 Ren 2026-10-10 的提议读作“想要延续者”，待 Ren）', f'（AI 把 Ren 2026-10-10 的提议读作“想要延续者”，{Z}采用）'),
('的读法，待 Ren）：从每个立场', f'的读法，{Z}采用）：从每个立场'),
# starting point
('其余读法是 AI 的，依 Ren 2026-10-15 的交托采用：起点是 `World`，带标签的过程与框架是它的读法，两个方向都已证明；', f'其余读法是 AI 的，{Z}采用（{d("D23")}）：带标签的过程与框架是展开的读法，两个方向都已证明（早先的“起点是 `World`”已由 Ren 2026-10-14 的问与 P107 取代，`World` 是诸读法粘合的读法）；'),
("The rest are the AI's readings, adopted on Ren's delegation of 15 October 2026. Not derived:", f"The rest are the AI's readings, adopted {E} ({d('D23')}; the earlier reading that the starting point is `World` is superseded by Ren's question of 14 October 2026 and P107, `World` being the reading where the readings glue). Not derived:"),
]
bad=0
for item in R:
    o,n=item[0],item[1]; want=item[2] if len(item)>2 else 1
    c=s.count(o)
    if c!=want:
        print('COUNT',c,'::',o[:120]); bad+=1
        continue
    s=s.replace(o,n)
if bad: print('BAD',bad); sys.exit(1)
open(p,'w',encoding='utf-8').write(s)
print('applied',len(R))
