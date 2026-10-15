#!/usr/bin/env python3
"""P114 landing kit, the apart modules read on the shared base: python3 -B apply_p114.py [--dry] [--section N]

Run from the repository root.

`--dry` writes nothing. It runs THEOREM-CONNECTIVITY.py twice, on the records as they are and on a temporary copy of
them with this kit's aliases added, and prints both summaries. The compiled modules must be in the checker's shared
cache (scratch_build.py or the checker puts them there).

Without `--dry`, once the core receipt holding Becoming.Courses and Becoming.CoursesBridge exists, it
* checks that the retained copy of the landed core receipt passed for the current bytes of Courses.lean and
  CoursesBridge.lean, and that every alias and declaration named here is a declaration of those modules in it;
* edits the 26 records whose spine aliases all stood apart from the base (THEOREM-CONNECTIVITY.py on c143e7d9): each
  gains the module source as a proof reference with its declarations, the retained core receipt as a receipt reference,
  a binding of the source to the receipt, its aliases and one bilingual history entry. Claims, statements, Ren's words,
  dependencies, validation scope and the references already held are left as they are;
* measures again and prints the summary.
Then regenerate DECIDABILITY-INVENTORY.md on the checked bytes and run `make research-render` and `make research-check`.
The study section (provisionally 138) is already in the branch; `--section N` names the number it lands as, for the
history entries.
"""
import hashlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path.cwd()
KIT = Path(__file__).resolve().parent
STUDY_DIR = KIT.parents[1]
RECORDS = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
CORE_RECEIPT = LEAN + 'becoming/becoming-verification.json'
C = 'Becoming.Courses.'
BR = 'Becoming.'

# record id → (module, aliases, further declarations, zh, en). Aliases are Lean names of theorems whose statements use
# the base (`Generative.Process`/`Trace`, `Becoming.Frame`/`Run`, `Becoming.World`/`Flow`/`Web`); the further
# declarations are the definitions and steps the aliases use.
CHANGES = {
    'acquired-binding-compositional-use': (
        'Courses', [C + 'course_reads_iff'], [C + 'encode_course'],
        '每个词都是过程从 s 回到 s 的历程、分组恢复诸词时，每个由词组成的历程都被读作其词的意义，恰当每个词被读作其意义'
        '（course_reads_iff；词组成历程，encode_course）。',
        'where every word is a course of a process from s back to s and grouping recovers the words, every course of words '
        'is read as the meanings of its words exactly when each word is read as its meaning (course_reads_iff; words '
        'compose courses, encode_course).'),
    'transition-grouping-word-partition': (
        'Courses', [C + 'course_words_iff', C + 'course_chunks_iff', C + 'no_run_record_groups'], [C + 'encode_course'],
        '每个词都是过程从 s 回到 s 的历程时，按 r 分组恢复每个由词组成之历程的词，恰当每个词内部相连、且没有词的末一步与任何词的首一步相连'
        '（course_words_iff）；一个历程诸步的分组唯一（course_chunks_iff）；两个词在内部以不同的方式延续同一步时，任何过程的任何运行前 '
        'n 步的记录按其多数联结分组都漏掉某个由词组成的历程（no_run_record_groups）。',
        'where every word is a course of a process from s back to s, grouping by r recovers the words of every course of '
        'words exactly when each word is linked inside and no word\'s last move is linked to any word\'s first '
        '(course_words_iff); the grouping of a course\'s moves is unique (course_chunks_iff); where two words continue one '
        'move differently inside, grouping by the majority bonds of the record of the first n moves of any run of any '
        'process misses some course of words (no_run_record_groups).'),
    'enacted-scene-binding': (
        'Courses', [C + 'run_resolves_iff', C + 'course_resolves_every_iff'], [],
        '对无重复的意义库，一个运行的前 n 步之后形式解析为 e，恰当 e 在库中、每个承载的步都提供它、且其余每个意义都在某个承载的步中缺席'
        '（run_resolves_iff）；每个词都是从 s 回到 s 的历程且分组恢复诸词时，按解析读每组给出每个由词组成之历程的意义，恰当每个词的'
        '记录分开其意义（course_resolves_every_iff）。',
        'for a repertoire without repeats, the form resolves to e after the first n moves of a run exactly when e is in '
        'the repertoire, every bearing move offers it and every other meaning is missing from some bearing move '
        '(run_resolves_iff); where every word is a course from s back to s and grouping recovers the words, reading each '
        'group by resolution gives the meanings of every course of words exactly when each word\'s records separate its '
        'meaning (course_resolves_every_iff).'),
    'encounter-selection-and-revision': (
        'Courses', [C + 'run_candidates_append', C + 'run_narrows', C + 'run_stays_iff'], [C + 'window_append'],
        '运行的诸步读作记录：前 n + k 步留下的候选恰是前 n 步的候选中在其后 k 步上成立者（run_candidates_append）；'
        '在某步被排除的意义此后一直被排除（run_narrows）；候选沿运行保持，恰当其后每个承载的步都提供它（run_stays_iff）。',
        'the moves of a run read as records: the candidates the first n + k moves leave are exactly those of the first n '
        'that stand on the next k (run_candidates_append); a meaning ruled out at a step stays ruled out (run_narrows); a '
        'candidate stays one along a run exactly while every later bearing move offers it (run_stays_iff).'),
    'retrospective-source-binding': (
        'Courses', [C + 'run_resolves_explained_iff'], [],
        '运行的诸步经一族解释而读：一步提供一个意义恰当族中某个以该意义为目标的世界解释它，且前 n 步中每个承载的步都由某个以 t 为'
        '目标的族世界解释时，n 步之后形式的候选恰为 [t]，恰当库中其余每个意义都被某个承载的步排除，族中没有以该意义为目标的世界解释'
        '那一步（run_resolves_explained_iff）。',
        'the moves of a run read through a family of explanations: where a move offers a meaning exactly when some family '
        'world with that meaning as target explains it, and each bearing move of the first n is explained by a family '
        'world with target t, the candidates after n moves are exactly [t] when every other meaning of the repertoire is '
        'ruled out by a bearing move that no family world with that meaning explains (run_resolves_explained_iff).'),
    'formed-copying-correction': (
        'Courses', [C + 'inspection_le_iff', C + 'inspection_course_le'], [C + 'inspection'],
        '检验读作一个过程，其步是被检验的位置（inspection）：检验位置 i 的每一步对每个产物、池与支持都不使相对模板的缺陷上升，恰当参照'
        '在 i 与模板一致（inspection_le_iff）；在忠实位置上的每条检验历程都不使缺陷上升（inspection_course_le）。',
        'inspection read as a process whose moves are the sites inspected (inspection): every inspection of site i keeps '
        'the defects against a template from rising, for every product, pool and support, exactly when the reference '
        'agrees with the template at i (inspection_le_iff); no course of inspections at faithful sites raises the defects '
        '(inspection_course_le).'),
    'formed-copying-registration': (
        'Courses', [C + 'reading_completes_iff', C + 'copy_grows'],
        [C + 'completes_units_iff', C + 'readSteps_orbit', C + 'tick_extends'],
        '确定之律 k 步的计划完成，恰当目标在其轨道第 k 处成立（completes_units_iff），经接触而读的复制诸步沿其律的轨道'
        '（readSteps_orbit）。待处理的记号与词一样多时，经接触而读的复制的 word.length 步计划以词加入产物而完成，恰当每个位置读到词的'
        '记号、池供给该词且支持覆盖其汲取（reading_completes_iff）；复制的产物沿其过程的每条历程只增（copy_grows）。',
        'a plan of k moves of a determined law completes exactly when the goal holds on its orbit at k '
        '(completes_units_iff), and the moves of a copy reading through contacts go along its law\'s orbit '
        '(readSteps_orbit). Where as many tokens are pending as the word has, the reading copy\'s plan of word.length '
        'moves completes with the word added to the product exactly when every site reads the word\'s token, the pool '
        'supplies the word and the support covers its draws (reading_completes_iff); the copy\'s product only grows along '
        'every course of its process (copy_grows).'),
    'inherited-structural-copying': (
        'Courses', [C + 'copy_built_iff', C + 'release_course_iff', C + 'lineage_course_iff', C + 'every_released_iff_course'],
        [C + 'steps_orbit', C + 'release'],
        '复制的诸步沿其确定之律的轨道（steps_orbit）；作为其过程的计划，复制的产物是该词，恰当池供给该词且支持覆盖其汲取'
        '（copy_built_iff）。共享一个池的复制读作释放之律（release）的历程：一批中每个复制都被释放，恰当诸词是释放之律从所持的池与'
        '支持出发的历程（every_released_iff_course），恰当池合起来供给全部的词、支持覆盖它们全部的汲取与释放（release_course_iff）；'
        '一个词依次复制 n 次是释放之律的历程，恰当池中每个记号至少有该词所用的 n 倍、支持覆盖 n 倍的汲取与释放（lineage_course_iff）。',
        'a copy\'s moves go along its determined law\'s orbit (steps_orbit); as a plan of its process, the copy\'s product '
        'is the word exactly when the pool supplies the word and the support covers its draws (copy_built_iff). Copies '
        'from one shared pool read as courses of the release law (release): every copy of a batch is released exactly '
        'when its words are a course of the release law from the pool and support held (every_released_iff_course), so '
        'exactly when the pool supplies all the words together and the support covers all their draws and releases '
        '(release_course_iff); one word copied n times in turn is a course of the release law exactly when the pool holds '
        'each token at least n times as often as the word uses it and the support covers n times its draws and release '
        '(lineage_course_iff).'),
    'material-preparation-output': (
        'Courses', [C + 'copy_empties_iff', C + 'copy_completes_iff'], [C + 'steps_orbit', C + 'completes_units_iff'],
        '作为其确定过程的计划，复制完成而无待处理者，恰当池供给该词且支持覆盖其汲取（copy_completes_iff）；复制的过程使池中无剩余，'
        '恰当池中每个记号恰如词所用的次数、且支持覆盖汲取（copy_empties_iff）。',
        'as a plan of its determined process, the copy completes with nothing pending exactly when the pool supplies the '
        'word and the support covers its draws (copy_completes_iff); the copy\'s process leaves nothing in the pool exactly '
        'when the pool holds each token exactly as often as the word uses it and the support covers the draws '
        '(copy_empties_iff).'),
    'market-finite-support-obstruction': (
        'Courses', [C + 'Drains.leaves_run', C + 'exhausts_run'], [C + 'run_history', C + 'run_admissible', C + 'historyRun'],
        '受扰过程的运行就是其诸步的可容许历史（run_history、run_admissible；反之 historyRun）。于是在被耗竭的家族第 n 级之下的起点，'
        '在受扰过程的每个运行上于 n 步之内离开护栏（Drains.leaves_run）；有界增长下的耗竭律对受扰过程的每个运行成立（exhausts_run）。',
        'a run of the disturbed process is the admissible history of its moves (run_history, run_admissible; conversely '
        'historyRun). So a start below level n of a drained family leaves the guard within n steps on every run of the '
        'disturbed process (Drains.leaves_run), and exhaustion by bounded growth holds on every run (exhausts_run).'),
    'market-partial-correction-boundary': (
        'Courses', [C + 'avoids_iff_closed_reach', C + 'some_avoids_iff_reach', C + 'fixed_avoids_reach', C + 'Funnel.runs',
                    C + 'basin_runs', C + 'course_reaches_iff_funnel', C + 'course_reaches_iff_variant'],
        [C + 'reach_iff_orbit', C + 'trace_orbit', C + 'orbit_trace', C + 'Reaches.runs', C + 'course_reaches_iff_orbit'],
        '确定之律的过程所到达者就是其轨道（reach_iff_orbit）。所以其过程从 s 所到达的构型都不在目标中，恰当某个含 s、避开目标且在律下'
        '封闭的集合存在（avoids_iff_closed_reach）；某个种子永不到达，恰当一个避开目标的封闭集含有某个种子（some_avoids_iff_reach）；'
        '目标之外的不动构型不到达目标（fixed_avoids_reach）。漏斗或每个盆在第 n 级所含的起点，在受扰过程的每个运行上 n 步之内到达目标'
        '（Funnel.runs、basin_runs）；对确定之律，至多 n 步的历程到达目标恰当一个漏斗含起点，目标判定时恰当一个数值变式在起点至多为 n'
        '（course_reaches_iff_funnel、course_reaches_iff_variant）。',
        'what a determined law\'s process reaches is its orbit (reach_iff_orbit). So no configuration its process reaches '
        'from s is in the target exactly when some set holding s, avoiding the target and closed under the law exists '
        '(avoids_iff_closed_reach); some seed never reaches it exactly when a closed set avoiding the target holds a seed '
        '(some_avoids_iff_reach); a fixed configuration outside the target never reaches it (fixed_avoids_reach). A start '
        'that a funnel, or every basin, holds at level n meets the target within n steps on every run of the disturbed '
        'process (Funnel.runs, basin_runs); for a determined law, a course of at most n moves reaches the target exactly '
        'when a funnel holds the start, and, with the target decided, exactly when a numeric variant is at most n there '
        '(course_reaches_iff_funnel, course_reaches_iff_variant).'),
    'market-supported-finite-transition': (
        'Courses', [C + 'lasts_iff_courses', C + 'courses_iff_ladder', C + 'courses_iff_necessary'], [C + 'lasts_of_courses'],
        '起点持续 n 步，恰当受扰过程从它出发、至多 n 个可容许扰动的每条历程都留在护栏之内（lasts_iff_courses）；所以这样的历程都留在'
        '护栏之内，恰当某个梯级族在第 n 级含起点（courses_iff_ladder），恰当每个必要族在第 n 级含起点（courses_iff_necessary）。',
        'a start lasts n steps exactly when every course of the disturbed process from it with at most n admissible '
        'disturbances stays within the guard (lasts_iff_courses); so every such course stays within the guard exactly when '
        'some ladder holds the start at level n (courses_iff_ladder), and exactly when every necessary family does '
        '(courses_iff_necessary).'),
    'reserved-shutdown-during-recovery': (
        'Courses', [C + 'runs_valid_completes', C + 'exits_completes'], [],
        '部分之律的运行是其过程（Assurance.ofPartial）的轨迹。从有效构型出发，带保留出口之律的每个被容许计划，作为该过程的计划完成于'
        '有效构型（runs_valid_completes）；长于余量的计划完成于出口处的有效构型（exits_completes）。',
        'a partial law\'s run is a trace of its process (Assurance.ofPartial). From a valid configuration, every admitted '
        'plan of a law with a reserved exit completes, as a plan of that process, into a valid configuration '
        '(runs_valid_completes), and every plan longer than the margin into a valid configuration at the exit '
        '(exits_completes).'),
    'versioned-request-completion': (
        'Courses', [C + 'Advances.completes_plan', C + 'pending_before_course'], [],
        '无燃料的工作作为计时之律过程的计划，在 work + 1 步内完成（Advances.completes_plan）；该过程至多 work 步的每条历程都使任务'
        '仍待处理，工作减去所走的步数（pending_before_course）。',
        'unfuelled work completes in work + 1 moves as a plan of the tick\'s process (Advances.completes_plan); every '
        'course of at most work moves of that process leaves the task pending, with the work lowered by the moves taken '
        '(pending_before_course).'),
    'historical-source-binding': (
        'Courses', [C + 'runs_reading_right_iff', C + 'runs_settle_iff'],
        [C + 'runs_look_right_iff', C + 'anyChange', C + 'anyRun', C + 'run_settles'],
        '以过程的运行为历史、以某日期的构型为当时所立的关系：由实际运行与隐藏来源产生的日期 d 的包，一族中符合带日期记录的运行与被容许'
        '来源所作的每个解释都给出实际内容，恰当该族中以某被容许来源给出同一包而内容不同的每个运行，都被某个带日期的控制与实际运行分开'
        '（runs_reading_right_iff；读一个日期的构型，runs_look_right_iff）。每种变化都被容许、两个构型不同时，两端的控制使每个运行上'
        '其间的日期都已定，恰当至多容许一次变化或其间没有日期（runs_settle_iff；对每个过程的充分方向，run_settles）。',
        'with the runs of a process as the histories and the configuration at a date as the relation then holding: every '
        'explanation of the packet at date d, produced by the actual run and the hidden source, by a family run fitting '
        'the dated records and an admitted source gives the actual content exactly when every family run giving the same '
        'packet with another content under some admitted source is told apart from the actual run by a dated control '
        '(runs_reading_right_iff; reading the configuration at a date, runs_look_right_iff). Where every change is '
        'admitted and two configurations differ, controls at both ends settle the dates between on every run exactly when '
        'at most one change is admitted or no date lies strictly between (runs_settle_iff; the sufficient direction for '
        'every process, run_settles).'),
    'control-coherence-loss': (
        'Courses', [C + 'runs_no_restore', C + 'runs_decoder_pair_iff'], [C + 'reducedRun'],
        '约化所保留的运行是经约化而读之律的运行（reducedRun）。约化运行在两个运行不同的日期相同时，约化运行的任何映射都不能在每个日期'
        '还原两者（runs_no_restore）；在约化运行相同的日期，对一个观察量在两者上都对的解码存在，恰当观察量在那里相同'
        '（runs_decoder_pair_iff）。',
        'what a reduction keeps of a run is a run of the law read through it (reducedRun). Where the reduced runs agree '
        'at a date at which the runs differ, no map of the reduced runs restores both runs at every date '
        '(runs_no_restore); at a date where the reduced runs agree, a decoder right for an observable at both runs exists '
        'exactly when the observable agrees on them there (runs_decoder_pair_iff).'),
    'binding-preserving-substitution': (
        'Courses', [C + 'steps_agree_iff_levels', C + 'supplied_agree_iff_levels'], [],
        '网的两步在每个只经条件水平而读、且每个条件水平都被某个读法直接读出的读法下相同，恰当每个条件水平相同'
        '（steps_agree_iff_levels）；替代者在每个读法下与步 t 相同，恰当它所供给的步在每个条件上与 t 水平相同'
        '（supplied_agree_iff_levels）。',
        'two steps of a web agree under every reading that reads a step only through its conditions\' levels, each level '
        'read directly by some reading, exactly where every condition stands at the same level (steps_agree_iff_levels); '
        'a replacement agrees with step t under every reading exactly where the step it supplies stands at t\'s level at '
        'every condition (supplied_agree_iff_levels).'),
    'risk-certificate-outcome-distinction': (
        'Courses', [C + 'run_judges_iff', C + 'no_run_judge_of_merged'], [C + 'reducedRun', C + 'visited', C + 'mem_visited'],
        '只读约化运行的判断者在前 n 个日期给出一个观察量，恰当观察量在约化所合并的每两个日期上相同，不用选择（run_judges_iff）；'
        '约化合并了观察量所分开的两个日期时，没有判断者经它读出运行（no_run_judge_of_merged）。',
        'a judge reading only the reduced run gives an observable at each of the first n dates exactly when the '
        'observable goes alike at every two of those dates the reduction merges, with no choice (run_judges_iff); where '
        'the reduction merges two dates the observable tells apart, no judge reads the run through it '
        '(no_run_judge_of_merged).'),
    'draws-on-a-shared-stock': (
        'Courses', [C + 'selections_within_iff', C + 'supported_not_together'], [C + 'twoDrawers'],
        '在网的一步，对一个列出的形成家族，每种选取在一个条件上的需要都在该条件水平之内，恰当整个家族的需要在内'
        '（selections_within_iff）；网 twoDrawers 中每个形成在步 0 都被支持，两者的需要合起来却超出条件的水平'
        '（supported_not_together）。',
        'at a step of a web, for a listed family of formations, the needs on one condition of every selection are within '
        'the condition\'s level exactly when the needs of the whole family are (selections_within_iff); in the web '
        'twoDrawers each formation is supported at step 0 while their needs together exceed the level '
        '(supported_not_together).'),
    'fulfillment-chance-floor': (
        'Courses', [C + 'claims_floor', C + 'claims_every_weighting_iff'], [],
        '框架的主张在其列出的构型上由布尔事件读出：每个列出的、实现需求与旧支持的构型都实现新支持时，在每个权重下，被旧支持满足的'
        '需求质量在新支持的质量之内，后者在整体之内（claims_floor）；每个权重都使一个主张的质量在另一个之内，恰当凡实现前者的列出'
        '构型都实现后者（claims_every_weighting_iff）。',
        'the claims of a frame read at its listed configurations by Boolean events: where every listed configuration '
        'realizing the demand and the old support realizes the new support, under every weighting the mass of demand met '
        'by old support is within the mass of the new support, and that within the whole (claims_floor); every weighting '
        'keeps one claim\'s mass within another\'s exactly where every listed configuration realizing the first realizes '
        'the second (claims_every_weighting_iff).'),
    'fallible-witness-diagnosability': (
        'Courses', [C + 'dates_no_common_report_envelopes_iff', C + 'dates_no_common_report_iff', C + 'run_reports_apart'],
        [C + 'anyChange', C + 'anyRun'],
        '运行在列出日期上的二值识是可错的证人：两个故障集留下共同的忠实日期时，任何过程的任何运行都不同时由一个故障集下的 x 与另一个'
        '下的 y 解释（run_reports_apart）；在每种变化都被容许的二值构型的历程上，没有历程被两个回答在所容许的故障集下解释，恰当每两个'
        '被容许的故障集都留下共同的忠实日期（dates_no_common_report_iff、dates_no_common_report_envelopes_iff）。',
        'a run\'s two-valued registrations at listed dates are fallible witnesses: where two fault sets leave a common '
        'faithful date, no run of any process is explained both by x with the one at fault and by y with the other '
        '(run_reports_apart); over the courses of two-valued configurations in which every change is admitted, no course '
        'is explained by both answers under admitted fault sets exactly where every two admitted fault sets leave a '
        'common faithful date (dates_no_common_report_iff, dates_no_common_report_envelopes_iff).'),
    'losses-of-the-sum-over-histories': (
        'Courses', [C + 'loop_courses_double'], [C + 'loop', C + 'loop_trace'],
        '一个构型与回到它的两步组成的环（loop）上，历程之和所经过的 n 步历程都是环的历程，共 2 ^ n 条（loop_courses_double）。',
        'around the loop of one configuration and two moves back to it (loop), the courses of n moves the sum over '
        'histories goes through are courses of the loop, and there are 2 ^ n of them (loop_courses_double).'),
    'separation-loses-the-relation': (
        'Courses', [C + 'relation_persists_courses', C + 'courses_keep_unrelated', C + 'copy_relates_course',
                    C + 'forgetting_unrelates_courses', C + 'coupling_course'], [C + 'reachedFrom'],
        '沿确定之律过程的历程，从整体出发 n 步所到达者（reachedFrom）：各部分各自移动时保持无关（矩形，courses_keep_unrelated）；'
        '两个移动都不合并时，关系沿每条历程持续（relation_persists_courses）；把第一部分复制入第二部分的一步使两部分相同，不是矩形'
        '（copy_relates_course）；遗忘一个部分使之无关（forgetting_unrelates_courses）；耦合一步关联，再作用一步解除'
        '（coupling_course）。',
        'along the courses of a determined law\'s process, what n moves reach from a whole (reachedFrom): parts moved each '
        'by itself stay unrelated (rectangular, courses_keep_unrelated); where neither move merges, a relation persists '
        'along every course (relation_persists_courses); one move copying the first part into the second makes them go '
        'alike, which is not rectangular (copy_relates_course); forgetting a part unrelates it '
        '(forgetting_unrelates_courses); a coupling relates in one move and, acting again, unrelates (coupling_course).'),
    'growth-constrained-fragmentation': (
        'Courses', [C + 'system_iff_certified', C + 'not_within_system_of_closed'], [],
        '一个区域是形成 f 的系统（在共同条件中共同参与的闭包，Flow.WithinSystem），恰当它含 f、在共享条件下封闭且在 f 的系统之内'
        '（system_iff_certified）；在共享下封闭、含 f 而不含 g 的区域表明 g 不在 f 的系统中（not_within_system_of_closed）。',
        'a region is the system of formation f (the closure under taking part in a common condition, Flow.WithinSystem) '
        'exactly when it holds f, is closed under sharing a condition and lies within f\'s system (system_iff_certified); '
        'a region closed under sharing that holds f but not g shows g is not in f\'s system '
        '(not_within_system_of_closed).'),
    'organizational-formation-from-generative-comparison': (
        'Courses', [C + 'extension_frontier_exists', C + 'extension_frontier_has_iff'], [],
        '在框架构型的非空列出选项表上，生成扩展弱判定时，某个构型不被任何成员扩展（extension_frontier_exists）；扩展与任务都判定时，'
        '没有成员扩展的每个构型都完成任务，恰当每个缺任务的成员都被某个成员扩展（extension_frontier_has_iff）。',
        'on a nonempty listed menu of a frame\'s configurations where generative extension is weakly decided, some '
        'configuration is extended by no member (extension_frontier_exists); with extension and the task decided, every '
        'configuration no member extends performs the task exactly when every member lacking it is extended by some member '
        '(extension_frontier_has_iff).'),
    'classification-robust-generative-comparison': (
        'CoursesBridge', [BR + 'extension_classification_robust_iff', BR + 'frame_classification_robust_iff_of_em'],
        [BR + 'extension_classification_robust'],
        '（桥接 Becoming.CoursesBridge）在框架的构型上，基本内容即框架在那里实现者：每种新内容分类下的严格偏好，恰是保留新内容且以之为'
        '增益时更好，排中律为具名假设（frame_classification_robust_iff_of_em）；沿生成扩展（a 实现 b 所实现的一切及一个 b 所缺的活'
        '内容），不需排中律，a 在每种分类下都被严格偏好，恰当它保留 b 的每个新内容（extension_classification_robust、'
        'extension_classification_robust_iff）：排中律只在两边基本内容相同、比较转到增益时才需要。',
        '(bridge Becoming.CoursesBridge) on a frame\'s configurations, the basic contents being what the frame realizes '
        'there: strict preference under every classification of fresh contents is retaining them and being better with '
        'them as gains, with excluded middle named (frame_classification_robust_iff_of_em); along a generative extension '
        '(a realizes everything b realizes and a living content b lacks) no excluded middle is needed, and a is strictly '
        'preferred under every classification exactly when it keeps every fresh content of b '
        '(extension_classification_robust, extension_classification_robust_iff): excluded middle is needed only where the '
        'basic contents are the same on both sides and the comparison passes to gains.'),
}
assert len(CHANGES) == 26
RUN = {}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def receipt():
    """The retained copy of the landed core receipt, passed for the current bytes of both modules, with their
    declarations."""
    core = json.loads((ROOT / CORE_RECEIPT).read_text())
    RUN['core'] = LEAN + 'becoming/becoming-checks/' + core['utc'] + '/verification.json'
    r = json.loads((ROOT / RUN['core']).read_text())
    assert r['status'] == 'passed', RUN['core']
    assert sha(RUN['core']) == sha(CORE_RECEIPT), 'the retained copy differs from the receipt'
    names = {}
    for module in ('Courses', 'CoursesBridge'):
        assert r['source_sha256']['Becoming.' + module] == sha(B + module + '.lean'), ('receipt predates the source', module)
        entry = next(m for m in r['modules'] if m['module'] == 'Becoming.' + module)
        names[module] = {d['name'] for d in entry['declarations']}
    for rid, (module, aliases, further, _, _) in CHANGES.items():
        missing = [n for n in aliases + further if n not in names[module]]
        assert not missing, ('not a declaration of the landed module', rid, missing)
    return core['utc']


def edit(d, rid, utc, section):
    module, aliases, further, zh, en = CHANGES[rid]
    source = B + module + '.lean'
    have = {r['path'] for r in d['references']}
    assert source not in have, (rid, 'already references', source)
    d['references'].append({'path': source, 'role': 'proof', 'sha256': sha(source), 'declarations': aliases + further})
    if RUN['core'] not in have:
        d['references'].append({'path': RUN['core'], 'role': 'receipt', 'sha256': sha(RUN['core']), 'declarations': []})
    binding = {'source': source, 'receipt': RUN['core'], 'sha256_pointer': '/source_sha256/Becoming.' + module,
               'success_pointer': '/status', 'success_value': 'passed'}
    assert binding not in d['proof_bindings']
    d['proof_bindings'].append(binding)
    for alias in aliases:
        assert alias not in d['aliases'], (rid, alias)
        d['aliases'].append(alias)
    d['history'].append({
        'zh': f'2026-10-16，P114 散立的模块在共同基底上陈述（研究 §{section}；Ren 2026-10-15：“so for our theories, they are '
              f'proved in a dag order and can be all connected right?”）：主律在共同基底上陈述，不加前提：{zh}'
              f'Becoming.{module} 由核心运行编译与审计（回执 {utc}），公理报告为空。论断、假设、Ren 的话、依赖与既有证明不变；'
              '只加引用、绑定、别名与本条。',
        'en': f'16 October 2026, P114, the apart modules read on the shared base (study section {section}; Ren, 15 October: '
              '“so for our theories, they are proved in a dag order and can be all connected right?”): the main law '
              f'stated on the shared base, no premise added: {en} Becoming.{module} is compiled and audited by the core run '
              f'(receipt {utc}), with empty axiom reports. Claims, hypotheses, Ren\'s words, dependencies and the earlier '
              'proofs are unchanged; only references, bindings, aliases and this entry are added.'})


def measure(records=None):
    path = STUDY_DIR / 'THEOREM-CONNECTIVITY.py'
    spec = importlib.util.spec_from_file_location('theorem_connectivity', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if records is not None:
        mod.RECORDS = records
    argv, sys.argv = sys.argv, [str(path)]
    out = io.StringIO()
    try:
        with redirect_stdout(out):
            mod.main()
    finally:
        sys.argv = argv
    return json.loads(out.getvalue())


def summary(m):
    keys = ('spine_theorems', 'classes', 'apart_used_by_nothing', 'records_by_best_alias_class',
            'records_resting_only_on_apart_theorems')
    return {k: m[k] for k in keys}


def dry():
    before = measure()
    with tempfile.TemporaryDirectory(prefix='p114-records-') as scratch:
        copy = Path(scratch)
        for p in RECORDS.glob('*.json'):
            shutil.copyfile(p, copy / p.name)
        for rid, (_, aliases, _, _, _) in CHANGES.items():
            d = json.loads((copy / (rid + '.json')).read_text())
            assert not set(aliases) & set(d['aliases']), rid
            d['aliases'] += aliases
            (copy / (rid + '.json')).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        after = measure(copy)
    print(json.dumps({'records as they are': summary(before), 'with the aliases added': summary(after)},
                     ensure_ascii=False, indent=1))


def main():
    args = sys.argv[1:]
    section = int(args[args.index('--section') + 1]) if '--section' in args else 138
    if '--dry' in args:
        dry()
        return
    utc = receipt()
    for rid in CHANGES:
        path = RECORDS / (rid + '.json')
        d = json.loads(path.read_text())
        edit(d, rid, utc, section)
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print(rid, len(CHANGES[rid][1]), 'aliases')
    print(json.dumps(summary(measure()), ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
