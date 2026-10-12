"""The chapter edits for P80 (THE-THEORY-OF-BECOMING.md): section 2 after P65's block, Part I stated whole, the
boundary on others' responses, section 8 (status, open item, further proofs), the spine table and the glossary.
Placeholders: {LEAN}, {S}, {STUDY}, {N_MODULE}. Each edit is (kind, anchor, text): 'after_line' inserts after the
line starting with the anchor, 'after_block' after the paragraph starting with it, 'replace' replaces the anchor."""

CF_ZH = ('**回应由动力学给出（第一部分，P80）。** P65 的比较给出两样：第二个流，与其余经识回应的前提。本模块把其余的交换给作'
         '一个规律，两样都推出（[Becoming.Counterfactual]({LEAN}/Counterfactual.lean)）。交换律从水平历史读出每个形成每步从每个条件'
         '取用与给予多少（`ExchangeLaw`）；它读已立者，是指跨过第 t 步只读到第 t 步为止的历史（`ExchangeLaw.Nonanticipating`）。'
         '两个平衡的流在场形成相同、起始相同，部分的动作相同，其余遵从同一个读已立者的律，则两者每步水平相同、交换相同'
         '（`counterfactual_fixed`）：给出律之后，一个动作的进程不是另给的。律从起始水平逐步生成进程，即阶段与至今历史上一个确定律'
         '的轨道（`ExchangeLaw.history_orbit`）；生成的流平衡，恰当律从不从一个条件取用多于其上所立与所给的'
         '（`ExchangeLaw.course_balances_iff`）。所以一个动作的反事实就是它生成的进程（`counterfactual_is_course`）；每个形成都遵从'
         '一个读已立者的律时，平衡的流就是律生成的进程（`ExchangeLaw.course_unique`）。律对部分之外的每个形成只读其所识时'
         '（`ExchangeLaw.Through`），其余在律的任意两个进程中经识回应（`ExchangeLaw.Through.responds`）：P65 的前提成为定理。每个读'
         '已立者的律都经识一切而读；条件有限时，它经其交换所敏感的条件而读（`ExchangeLaw.Nonanticipating.through_sensitive`），而它'
         '所经的每个识，连同形成所依存的，都不漏掉其敏感的任何条件（`ExchangeLaw.Through.registers_of_sensitive`）：敏感是最小的识。于是'
         '比较在律的两个进程之间、在经律之识画出的回应所及之内决定，条件有限时这个识就是律的敏感；一个动作与另一个动作所生成的进程'
         '之间亦然，不另给第二个流与回应（`comparison_of_courses`、`comparison_through_sensitivity`、`comparison_with_act`）。动作是'
         '标准因果模型的输入：进程是 P68 中以部分的动作为输入的模型的轨道，未取的动作是干预，记录不固定其结果，模型固定它'
         '（`ExchangeLaw.course_trajectory`、`ExchangeLaw.act_not_taken`）。P65 的 `Loop` 中，第二个形成的回应是只读其所观察者的律，'
         '`Loop.responds` 由它推出，两个流各是该律在其动作下唯一平衡的进程（`Loop.responds_by_law`、`Loop.courses_fixed`）。读法'
         '（AI 的，待 Ren）：反事实不是实际之外的第二个世界，而是同一规律在部分另作时的进程，可行时存在、由动作固定；对遵从读已立者之律的其余，P65 的前提'
         '不是另加的关于形成怎样行为的假设，读作识，形成识其交换所敏感者。律本身、它读已立者、进程可行，以及条件无穷多时敏感是否仍是最小的识，'
         '都不推出。见[研究 §{S}]({STUDY})与 [counterfactual-is-the-course](../results/records/counterfactual-is-the-course.md)、'
         '[comparison-where-the-rest-responds](../results/records/comparison-where-the-rest-responds.md)。')

CF_EN = ("**The response as the dynamics give (Part I, P80).** P65's comparison supplies two things: the second flow, and "
         "the premise that the rest responds through its registration. This module gives the rest's exchange as a law "
         "and derives both ([Becoming.Counterfactual]({LEAN}/Counterfactual.lean)). A law of exchange reads off a level "
         "history what each formation takes from and gives to each condition at each step (`ExchangeLaw`); it reads "
         "what has stood when, across the step from `t`, it reads the history up to `t` only "
         "(`ExchangeLaw.Nonanticipating`). Two balanced flows with the same formations present, starting alike, in "
         "which the part acts alike and the rest follows one law of what has stood, have the same levels and the same "
         "exchange at every step (`counterfactual_fixed`): once the law is given, the course of an act is not "
         "supplied. The law generates a course step by step from starting levels, the orbit of one determined law on "
         "the stage and the history so far (`ExchangeLaw.history_orbit`), and the generated flow balances exactly "
         "where the law never takes more from a condition than stands on it and is given to it "
         "(`ExchangeLaw.course_balances_iff`). So the counterfactual of an act is the course it generates "
         "(`counterfactual_is_course`), and where every formation follows one law of what has stood, a balanced flow "
         "is the course the law generates (`ExchangeLaw.course_unique`). Where the law reads, for each formation "
         "outside the part, only what it registers (`ExchangeLaw.Through`), the rest responds through its "
         "registration in any two courses of the law (`ExchangeLaw.Through.responds`): P65's premise becomes a "
         "theorem. Every law of what has stood reads through registering everything; with finitely many conditions it "
         "reads through the conditions its exchange is sensitive to "
         "(`ExchangeLaw.Nonanticipating.through_sensitive`), and no registration it reads through, with what "
         "the formation depends on, leaves out a condition it is sensitive to "
         "(`ExchangeLaw.Through.registers_of_sensitive`): sensitivity is the least registration. So the comparison of "
         "two courses of the law is decided within the responsive reach drawn through the law's registration, which "
         "with finitely many conditions is its sensitivity; and so is the comparison of an act with the course "
         "another act generates, with neither the second flow nor the response supplied (`comparison_of_courses`, "
         "`comparison_through_sensitivity`, `comparison_with_act`). The act is the input of a standard causal model: "
         "the course is a trajectory of P68's model whose input is the part's move, and an act not taken is an "
         "intervention, whose outcome the record does not fix and the model does (`ExchangeLaw.course_trajectory`, "
         "`ExchangeLaw.act_not_taken`). In P65's `Loop` the second's reply is a law reading only what it observes, "
         "`Loop.responds` follows from it, and each flow is the only balanced course of the law with its act "
         "(`Loop.responds_by_law`, `Loop.courses_fixed`). On the AI's reading, pending Ren, a counterfactual is not a "
         "second world beside the actual one but the course of the same law with the part acting otherwise, existing "
         "where feasible and fixed by the act; for a rest following a law of what has stood, P65's premise is no further assumption about how formations behave, and read as "
         "识, a formation registers what its exchange is sensitive to. The law itself, that it reads what has stood, "
         "feasibility, and whether sensitivity is still the least registration with infinitely many conditions, are "
         "not derived.")

WHOLE_ZH = ('- **回应由动力学给出。** 其余遵从一个读已立者的律时，一个动作的进程由动作固定，可行时存在（`counterfactual_fixed`、'
            '`ExchangeLaw.course_balances_iff`）；律只读各形成所识时，其余经识回应是定理（`ExchangeLaw.Through.responds`），条件有限时'
            '这个识就是律的敏感（`ExchangeLaw.Nonanticipating.through_sensitive`）；未取的动作是标准模型中的干预'
            '（`ExchangeLaw.act_not_taken`）。')
WHOLE_EN = ("- **The response as the dynamics give.** Where the rest follows a law of what has stood, the course of an act is "
            "fixed by the act and exists where feasible (`counterfactual_fixed`, `ExchangeLaw.course_balances_iff`); where "
            "the law reads only what each formation registers, responding through registration is a theorem "
            "(`ExchangeLaw.Through.responds`), and with finitely many conditions that registration is the law's "
            "sensitivity (`ExchangeLaw.Nonanticipating.through_sensitive`); an act not taken is an intervention of the "
            "standard model (`ExchangeLaw.act_not_taken`).")

OTHERS_ZH_OLD = '，而回应本身与这一前提仍是给出的。'
OTHERS_ZH_NEW = ('；其余的交换是读已立者的律时，第二个流是它在另一动作下生成的进程，这一前提由律推出（`comparison_with_act`、'
                 '`ExchangeLaw.Through.responds`），而律本身仍是给出的。')
OTHERS_EN_OLD = ', while the responses and that premise remain supplied.'
OTHERS_EN_NEW = ("; where the rest's exchange is a law of what has stood, the second flow is the course it generates under the "
                 "other act and that premise follows from the law (`comparison_with_act`, `ExchangeLaw.Through.responds`), "
                 "while the law itself remains supplied.")

OPEN_OLD = ('其余交换随之调整、回应由动力学给出而非另给的反事实（其余经识回应时，差别与比较限于部分的回应所及：'
            '[comparison-where-the-rest-responds](../results/records/comparison-where-the-rest-responds.md)）；')
OPEN_NEW = ('到达回应所及之内的差别有多少（其余交换随之调整的反事实已陈述：其余经识回应时，差别与比较限于部分的回应所及，'
            '[comparison-where-the-rest-responds](../results/records/comparison-where-the-rest-responds.md)；回应由动力学给出时，反事实'
            '是同一规律在另一动作下的进程，[counterfactual-is-the-course](../results/records/counterfactual-is-the-course.md)）；')

STATUS_OLD = '开放：回应由动力学给出；偏向伸出的一般形式'
STATUS_NEW = '开放：偏向伸出的一般形式'
STATUS_ROW = ('| 回应由动力学给出（P80） | 已陈述并检查，不用公理：其余遵从一个读已立者的交换律时，动作的反事实是律生成的进程，由动作固定，'
              '可行时存在；律只读各形成所识时，P65 的经识回应是定理，条件有限时这个识就是律的敏感，比较不另给第二个流与回应'
              '（[counterfactual-is-the-course](../results/records/counterfactual-is-the-course.md)、'
              '[comparison-where-the-rest-responds](../results/records/comparison-where-the-rest-responds.md)）。开放：律本身；条件无穷多时'
              '敏感是否仍是最小的识；差别到达多少；读法待 Ren |')

FURTHER_ZH_OLD = '- 反馈与所及：他者有回应的比较，由动力学给出回应而不是另给第二个流（经识回应时的限定已陈述，P65）；'
FURTHER_ZH_NEW = ('- 反馈与所及：条件无穷多时，律的敏感是否仍是它所经的最小的识（回应由动力学给出的比较已陈述，P80；经识回应时的限定，'
                  'P65）；')
FURTHER_EN_OLD = ('- Feedback and reach: a comparison in which others respond as the dynamics give, not through a second flow '
                  'supplied (the confinement where the rest responds through registration is stated, P65);')
FURTHER_EN_NEW = ("- Feedback and reach: whether, with infinitely many conditions, a law's sensitivity is still the least "
                  "registration it reads through (the comparison in which others respond as the dynamics give is stated, "
                  "P80; the confinement where the rest responds through registration, P65);")

SPINE = ('| L4 | [Becoming.Counterfactual]({LEAN}/Counterfactual.lean) | 回应由动力学给出（不用公理；交换律、它读已立者与进程可行'
         '是各定理的假设）：其余遵从一个读已立者的交换律时，部分动作相同、起始相同的两个平衡的流是一个流；律逐步生成进程，即阶段与'
         '历史上确定律的轨道，进程平衡恰当可行；动作的反事实是它生成的进程；律只读各形成所识时其余经识回应（P65 的前提），条件有限时'
         '这个识就是律的敏感，敏感是最小的识；比较在律的两个进程之间、在回应所及之内决定；进程是以部分的动作为输入的标准因果模型的'
         '轨道，未取的动作是干预；Loop 的回应是律 | {N_MODULE} |')

GLOSS = ('| 交换律／读已立者 | law of exchange / reads what has stood | 从水平历史读出每个形成每步与每个条件取用与给予多少；读已立者：'
         '跨过第 t 步只读到第 t 步为止的历史 | `ExchangeLaw`、`ExchangeLaw.Nonanticipating`、`Flow.Follows` |\n'
         '| 敏感 | sensitive | 形成的交换对一个条件敏感：某步只改变该条件的水平就改变它所交换的；条件有限时，读已立者的律经其敏感而'
         '读，它所经的每个识（连同所依存的）都不漏掉其敏感者 | `ExchangeLaw.Sensitive`、`ExchangeLaw.Nonanticipating.through_sensitive`、'
         '`ExchangeLaw.Through.registers_of_sensitive` |\n'
         '| 反事实（进程） | counterfactual (course) | 同一交换律在部分另作时生成的进程；由动作固定，可行（从不取用多于所立与所给）'
         '时存在 | `counterfactual_fixed`、`ExchangeLaw.course_balances_iff`、`counterfactual_is_course` |')

EDITS = [
    # Section 2: after P65's block (its Chinese paragraph, then its English one).
    ('after_block', '**The comparison where the rest responds (Part I, P65).**', '\n' + CF_ZH + '\n\n' + CF_EN),
    # Part I stated whole.
    ('after_line', '- **其余回应时的比较。**', WHOLE_ZH),
    ('after_line', '- **The comparison where the rest responds.**', WHOLE_EN),
    ('replace', OTHERS_ZH_OLD, OTHERS_ZH_NEW),
    ('replace', OTHERS_EN_OLD, OTHERS_EN_NEW),
    # Section 8.
    ('replace', OPEN_OLD, OPEN_NEW),
    ('replace', STATUS_OLD, STATUS_NEW),
    ('after_line', '| 与一般因果系统的比较（P64–P68） |', STATUS_ROW),
    ('replace', FURTHER_ZH_OLD, FURTHER_ZH_NEW),
    ('replace', FURTHER_EN_OLD, FURTHER_EN_NEW),
    # Section 9: the spine table.
    ('after_line', '| L4 | [Becoming.Response]', SPINE),
    # Section 10: the glossary.
    ('after_line', '| 经识回应 | responds through registration |', GLOSS),
]
