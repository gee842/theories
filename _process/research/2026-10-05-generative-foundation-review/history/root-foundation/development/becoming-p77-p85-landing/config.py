"""Serialized landing of P77–P79, P82, P84 and P85 through the shared landing kit.

Existing proof packages are inputs, preserved byte for byte. This run adds no theorem.
Section numbers and verification counts are filled only from the landing checkout's receipts.
Run after P76 + P81 and P80, before the P58c rest-strength rename.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'content.json').read_text())
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'
REC = '../results/records/'
PACKAGES = []
for i, p in enumerate(DATA['packages']):
    module, after = p['module'], DATA['packages'][i - 1]['module'] if i else 'Branching'
    imports_en = '`' + '`, `'.join(p['imports'][:-1]) + ('` and `' if len(p['imports']) > 1 else '') + p['imports'][-1] + '`' if len(p['imports']) > 1 else '`' + p['imports'][0] + '`'
    imports_zh = '、'.join('`' + x + '`' for x in p['imports'])
    anchor_zh = '`Branching` 导入 `Unfolding`、`Attraction` 与 `Capture`；' if not i else PACKAGES[-1]['imports_zh'][1]
    anchor_en = '`Branching` imports `Unfolding`, `Attraction` and `Capture`;' if not i else PACKAGES[-1]['imports_en'][1]
    record_links = '、'.join('[' + x + '](../../../../theories/becoming/results/records/' + x + '.md)' for x in p['records'])
    reuse_links = '、'.join('[' + x + '](../../../../theories/becoming/results/records/' + x + '.md)' for x in p['reuses'])
    evidence = '../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
    PACKAGES.append(dict(
        module=module, package=f'becoming-p{p["number"]}-landing', key=module.upper(), prefix=f'p{p["number"]}',
        after=after, layer='L3', scope_before='Attraction: for every determined law,',
        study_heading=p['title_zh'] + '（P' + str(p['number']) + '）',
        study_suffix_zh='\n\n**复用、产出与检查。** 复用 ' + reuse_links + '；本节的确切增量与消费者接口由 ' + record_links + ' 记录。当前 [Becoming.' + module + '](' + evidence + '/Becoming/' + module + '.lean) 的 {N_MODULE} 项定理由[合并回执](' + evidence + '/becoming-verification.json) {RECEIPT} 覆盖；外围回执 {PERIPHERY} 通过。以上边界与给定条件保持，整合没有增加独立审查。',
        study_suffix_en='\n\n**Reuse, output and verification.** Reuses ' + reuse_links.replace('、', ', ') + '; the exact delta and consumer interfaces are recorded in ' + record_links.replace('、', ', ') + '. The current [Becoming.' + module + '](' + evidence + '/Becoming/' + module + '.lean) has {N_MODULE} theorems covered by [consolidated receipt](' + evidence + '/becoming-verification.json) {RECEIPT}; periphery receipt {PERIPHERY} passed. The stated conditions and limits remain, and integration adds no independent review.',
        bullet=f'* `Becoming.{module}` (L3): {p["title_en"]} (P{p["number"]}). {p["en"]}',
        scope=f'{module}: {p["en"]}', readme_zh=p['zh'], readme_en=p['en'],
        imports_zh=(anchor_zh, anchor_zh + f'`{module}` 导入 {imports_zh}；'),
        imports_en=(anchor_en, anchor_en + f' `{module}` imports {imports_en};'),
    ))

PLAN_ZH = '\n'.join(
    '| P' + str(p['number']) + ' ' + p['title_zh'] + ' ✓ | 新模块 `Becoming.' + p['module'] + '`（{N_' + p['module'].upper() + '} 项定理）。' + p['zh'] + ' ' + p['boundary_zh'] + ' ' + ('推进已有记录 ' if p['number'] == 85 else '记录 ') + '、'.join(p['records']) + '；研究 §{S_' + p['module'].upper() + '}。 |'
    for p in DATA['packages'])
PLAN_EN = '\n'.join(
    '- **P' + str(p['number']) + ':** ' + p['title_en'] + '. `Becoming.' + p['module'] + '` ({N_' + p['module'].upper() + '} theorems). ' + p['en'] + ' ' + p['boundary_en'] + ' ' + ('Advances existing record ' if p['number'] == 85 else 'Records ') + ', '.join(p['records']) + '; study §{S_' + p['module'].upper() + '}.'
    for p in DATA['packages'])

paragraphs, whole_zh, whole_en, statuses, spine = [], [], [], [], []
for p in DATA['packages']:
    k, n = p['module'].upper(), str(p['number'])
    links = '、'.join('[' + r + '](' + REC + r + '.md)' for r in p['records'])
    paragraphs.append('**' + p['title_zh'] + '（第一部分，P' + n + '）。** ' + p['zh'] + ' ' + p['boundary_zh'] + ' 见 [Becoming.' + p['module'] + ']({LEAN}/' + p['module'] + '.lean)、[研究 §{S_' + k + '}]({STUDY_' + k + '})与 ' + links + '。\n\n**' + p['title_en'] + ' (Part I, P' + n + ').** ' + p['en'] + ' ' + p['boundary_en'])
    whole_zh.append('- ' + p['zh'] + '（P' + n + '）。')
    whole_en.append('- ' + p['en'] + ' (P' + n + ').')
    statuses.append('| ' + p['title_zh'] + '（P' + n + '） | 已陈述并检查：' + p['zh'] + ' ' + p['boundary_zh'] + ' ' + links + ' |')
    spine.append('| L3 | [Becoming.' + p['module'] + ']({LEAN}/' + p['module'] + '.lean) | ' + p['zh'] + '（P' + n + '） | {N_' + k + '} |')

CHAPTER_EDITS = [
    ('before', '**整体与 manifold。**', '\n\n'.join(paragraphs)),
    ('after_line', '- 过程与框架是同一展开的读法', '\n'.join(whole_zh)),
    ('after_line', '- The process and the frame are readings of one unfolding', '\n'.join(whole_en)),
    ('after_line', '| 一个关系的起点（P69） |', '\n'.join(statuses)),
    ('after_line', '| L3 | [Becoming.Branching]', '\n'.join(spine)),
    ('after_line', '- 一个关系的起点（P69）：', '- P77–P79、P82、P84、P85：列出一次读作同一已定；步序读作有交集交换的偏序；给定权重的历史之和及其实际对应；取用即依存是否作为形成规律；延续所需的供给与任一特定供给者的区别。读法由 AI 提出，待 Ren。'),
    ('after_line', '- One relational starting point (P69):', '- P77–P79, P82, P84, P85: listing once read as decided identity; the step index read through the partial order of joined exchanges; the sum of weighted histories and its actual correspondence; whether drawing being depending is a law of forming; the difference between being fed and needing any particular feeder. These readings are the AI\'s, pending Ren.'),
    ('replace', '由依存的形成推出传递（`TransmitsWithin` 现为前提）；', 'P84 已把传递刻画为承继与所需之界，证明它在起约束处独立于其余前提，并从取用的读法加上取用即依存推出；仍需同时必要的形成规律与无界水平的形式；'),
    ('replace', 'deriving transmission from how dependence forms (`TransmitsWithin` is now a premise);', 'P84 characterizes transmission as inheritance with a need bound, proves it independent wherever it binds, and derives it from a reading of drawing with drawing being depending; a necessary as well as sufficient forming law and unbounded levels remain;'),
    ('replace', '没有哪个特定来源形成复现的见证（两个可移去的来源）；', 'P85 已给出没有哪个特定来源形成复现的见证（`Successive.relay`）；同一世界去掉一个来源形成后仍每步得到供给的可移去形式仍开放；'),
    ('replace', 'a witness in which no particular source formation recurs (two removable sources);', 'P85 gives a witness in which no source formation recurs (`Successive.relay`); the removable form, still fed at every step with a source formation removed from the same world, remains open;'),
    ('replace', '从关系推出共同的步序；', 'P78 给出足迹所定的有交集交换偏序，恰刻画可通过交换无交集相邻步达到的次序；最小足迹、正规形与重排中的普查仍开放；'),
    ('replace', 'deriving the shared index of steps from relations;', 'P78 characterizes reachable reorderings by the partial order of joined exchanges for a given footprint; the least footprint, a normal form and censuses along reorderings remain open;'),
    ('replace', '分支路径上的度量（P82）。', '分支路径上的赋权由 P82 在给定权重规律、有限列表与有限步数下完成；实际权重的由来、带相位振幅与无限和仍开放。'),
    ('replace', 'a measure on branching courses (P82).', 'P82 supplies weighted branching courses under the stated weight laws, finite listings and a finite horizon; actual weights, phased amplitudes and infinite sums remain open.'),
    ('replace', '| 传递 | transmission | 后代承接亲代的依存，所需至多多 δ；是由应用给出的前提，脊柱不推出；`price` 中是每个后代相对其亲代的变化 | `Flow.TransmitsWithin`、`raised`、`lowered` |', '| 传递 | transmission | 后代承接亲代的依存，所需至多多 δ；在起约束处独立于其余前提；给定取用的读法与取用即依存时推出（P84）；`price` 中是每个后代相对其亲代的变化 | `Flow.TransmitsWithin`、`Flow.transmitsWithin_iff`、`World.transmitting_of_drawn`、`raised`、`lowered` |'),
]

READING = dict(
    after_en="(P69; Ren agreed that law and history are one unfolding read two ways, “there are no two realities”; the other readings are the AI's, pending Ren). ",
    after_zh='（P69；Ren 同意律与历史是同一展开的两种读法，“there are no two realities”；其余读法是 AI 的，待 Ren）。',
    en=' '.join(p['en'] + ' (P' + str(p['number']) + ').' for p in DATA['packages']) + ' The weights, footprints and local conditions are supplied as named; no actual correspondence or ethical judgment follows. ',
    zh=''.join(p['zh'] + '（P' + str(p['number']) + '）。' for p in DATA['packages']) + '权重、足迹与局部条件按定理所名给出；不由此推出实际对应或伦理判断。',
    lean_after='Branching.lean',
)
HISTORY = {p['module'].upper(): (
    '2026-10-13：接续并整合 P' + str(p['number']) + ' 的现存证明包；见整合文档 §{S}。',
    '2026-10-13: resumed and integrated the existing P' + str(p['number']) + ' proof package; see §{S} of the integration note.'
) for p in DATA['packages']}
RECORDS = DATA['records']
LABEL = 'P77–P79/P82/P84/P85'
DELTAS = ['zero_notes.py', 'record_delta.py']
