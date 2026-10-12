#!/usr/bin/env python3
"""Apply the documentation of P73–P75 to a checkout: two study sections and their English summary
entries, the unification plan's rows and bullets, the chapter edits, the cognition chapter's edits, the
totals in the chapter's section 9 and the study's English summary, and the reading-catalogue entry.

Usage: python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER

S is the first of two consecutive study sections: S for P73 with P74 (learning), S+1 for P75 (the root
of wisdom). PLAN_ZH_AFTER and PLAN_EN_AFTER are the prefixes of the plan's table row and bullet these go
after. Counts come from ROOT's receipts: the consolidated receipt must cover Becoming.Learning, and the
CorrectionInquiry and LearningCorrespondence receipts must have passed against it. Every anchor must
occur exactly once; rerunning on an applied checkout fails.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
S = int(sys.argv[2])
PLAN_ZH_AFTER, PLAN_EN_AFTER = sys.argv[3:5]
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'

receipt = json.loads((ROOT / D / 'becoming/becoming-verification.json').read_text())
periphery = json.loads((ROOT / D / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
bridge = json.loads((ROOT / D / 'universal-ethics/evolution-connectionism/learning-correspondence-verification.json').read_text())
assert receipt['status'] == periphery['status'] == bridge['status'] == 'passed'
# Both periphery bridges were checked against this core: the root's bytes in their receipts are the core receipt's.
for other in (periphery, bridge):
    for name, digest in other['source_sha256'].items():
        if name in receipt['source_sha256']:
            assert receipt['source_sha256'][name] == digest, ('periphery checked against another core', name)
assert 'Becoming' in periphery['source_sha256'] and 'Becoming.Learning' in bridge['source_sha256']
spine = [m for m in receipt['modules'] if m['spine']]
theorems = {m['module']: m['theorems'] for m in receipt['modules']}
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_CORE = len(receipt['core_closure'])
N_PKG = len(spine)
print('totals', N_THM, N_DECL, N_CORE, N_PKG)


def anchor(heading):
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces as hyphens."""
    text = heading.lstrip('#').strip().lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


VALUES = {
    '{RECEIPT}': receipt['utc'],
    '{PERIPHERY}': periphery['utc'],
    '{BRIDGE}': bridge['utc'],
    '{N_BRIDGE}': str(bridge['modules'][0]['theorems']),
    '{N_THM}': str(N_THM),
    '{N_DECL}': str(N_DECL),
    '{N_CORE}': str(N_CORE),
    '{N_LEARNING}': str(theorems['Becoming.Learning']),
    '{LEAN}': '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming',
    '{PERI}': '../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism',
}
# (key, study fragment prefix, theorems of the section's module), in the order of the study sections.
SECTIONS = [('LEARNING', 'p73', VALUES['{N_LEARNING}']), ('WISDOM', 'p75', '')]
STUDY = {}
for i, (key, prefix, n) in enumerate(SECTIONS):
    sec = str(S + i)
    zh = (HERE / f'docs/study/{prefix}_zh.md').read_text()
    heading = zh.split('\n', 1)[0].replace('{S}', sec)
    assert heading.startswith(f'## {sec}. '), heading
    VALUES[f'{{S_{key}}}'] = sec
    VALUES[f'{{ANCHOR_{key}}}'] = anchor(heading)
    VALUES[f'{{STUDY_{key}}}'] = f'{STUDY_LINK}#{anchor(heading)}'
    STUDY[key] = (sec, n, zh, (HERE / f'docs/study/{prefix}_en.md').read_text())


def fill(text, sec=None, n_module=None):
    if sec is not None:
        text = text.replace('{S}', sec)
        if n_module:
            text = text.replace('{N_MODULE}', n_module)
    for k, v in VALUES.items():
        text = text.replace(k, v)
    left = re.findall(r'\{[A-Z_]+\}', text)
    assert not left, left
    return text


def line_start(s, prefix, last=False):
    starts = [i for i in range(len(s)) if (i == 0 or s[i - 1] == '\n') and s.startswith(prefix, i)]
    assert len(starts) == 1 or (last and starts), (prefix[:80], len(starts))
    return starts[-1]


def insert_before_line(s, prefix, text, blank, last=False):
    i = line_start(s, prefix, last)
    return s[:i] + text + ('\n\n' if blank else '\n') + s[i:]


def insert_after_line(s, prefix, text):
    i = line_start(s, prefix)
    j = s.index('\n', i) + 1
    return s[:j] + text + '\n' + s[j:]


def edit(path, fn):
    p = ROOT / path
    s = p.read_text()
    s2 = fn(s)
    assert s2 != s, path
    p.write_text(s2)
    print('edited', path)


def sub1(s, pattern, repl):
    s2, n = re.subn(pattern, repl, s)
    assert n == 1, (pattern, n)
    return s2


def study_edits(s):
    for key, _, _ in SECTIONS:
        sec, n, zh, en = STUDY[key]
        s = insert_before_line(s, '## English summary', fill(zh, sec, n).rstrip('\n') + '\n', True)
        s = insert_before_line(s, 'The package now has ', fill(en, sec, n).rstrip('\n'), True, last=True)
    matches = list(re.finditer(r'The package now has \d+ theorems and \d+ declaration audits, over a core closure of '
                               r'\d+ modules and a package of \d+', s))
    last = matches[-1]
    return (s[:last.start()] + f'The package now has {N_THM} theorems and {N_DECL} declaration audits, over a core '
            f'closure of {N_CORE} modules and a package of {N_PKG}' + s[last.end():])


edit(f'{RF}/BECOMING-RENEWAL-READING.md', study_edits)

rows = (HERE / 'docs/plan_rows.md').read_text()
zh_rows = fill(rows.split('=== ZH_ROW ===\n')[1].split('=== EN_BULLET ===')[0]).strip('\n')
en_bullets = fill(rows.split('=== EN_BULLET ===\n')[1]).strip('\n')
edit(f'{RF}/BECOMING-UNIFICATION-PLAN.md',
     lambda s: insert_after_line(insert_after_line(s, PLAN_ZH_AFTER, zh_rows), PLAN_EN_AFTER, en_bullets))

spec = importlib.util.spec_from_file_location('chapter', HERE / 'docs/chapter.py')
chapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chapter)


def chapter_edits(s):
    for kind, anchor_text, text in chapter.EDITS:
        text = fill(text)
        if kind == 'before':
            s = insert_before_line(s, anchor_text, text, not text.startswith(('- ', '| ')))
        elif kind == 'after_line':
            s = insert_after_line(s, anchor_text, text)
        else:
            assert s.count(anchor_text) == 1, (anchor_text[:80], s.count(anchor_text))
            s = s.replace(anchor_text, text)
    s = sub1(s, r'覆盖 \d+ 项定理、\d+ 项声明审计，源声明的公理报告全部为空；核心闭包共 \d+ 个模块（包 \d+ 个模块',
             f'覆盖 {N_THM} 项定理、{N_DECL} 项声明审计，源声明的公理报告全部为空；核心闭包共 {N_CORE} 个模块（包 {N_PKG} 个模块')
    s = sub1(s, r'cover \d+ theorems and \d+ declaration audits, all source declarations with empty axiom reports; the core '
                r'closure has \d+ modules \(the package \d+',
             f'cover {N_THM} theorems and {N_DECL} declaration audits, all source declarations with empty axiom reports; '
             f'the core closure has {N_CORE} modules (the package {N_PKG}')
    return s


edit('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', chapter_edits)

spec = importlib.util.spec_from_file_location('cognition', HERE / 'docs/cognition.py')
cognition = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cognition)


def cognition_edits(s):
    for kind, anchor_text, text in cognition.EDITS:
        text = fill(text)
        if kind == 'before':
            s = insert_before_line(s, anchor_text, text, True)
        else:
            assert s.count(anchor_text) == 1, (anchor_text[:80], s.count(anchor_text))
            s = s.replace(anchor_text, text)
    return s


edit('theories/becoming/chapters/COGNITION-LEARNING-AND-EVOLUTION.md', cognition_edits)

EN = ("Learning needs no axiom: no record fixes the next value, also among worlds held by a list, and every learner "
      "has a course refuting each of its claims, the registration of a law keeping its record, so open; learning by "
      "refutation never passes a hypothesis that holds, and where a list holds the world it is refuted a bounded "
      "number of times, its coming to rest unrefuted and when it rests not registered; a lumping determines exactly "
      "the inputs it lumps with the data and is right exactly where the world goes alike across it, structure and "
      "change being one lumping; the earlier acquisition chain and connectionist models are instances (P73, P74; 理 "
      "is read as Ren reads it, the modeling of the laws of structure and of change; the other readings are the AI's, "
      "pending Ren). These laws complete the formal part of the root of wisdom at the scope Part I reaches, the "
      "correspondence of actual formation remaining open (P75). ")
ZH = ("学习不用公理：无记录固定下一个，被列表所持的世界中亦然；每个学习者都有在每个主张处否证它的序列，那是保留记录之律的识，开放；"
      "按否证学习从不越过成立的假设，被列表所持的世界中否证有界、静止不能被否证、何时静止不被识；归并恰在它与数据归并之处决定、"
      "正确恰在世界经它同去之处，结构与变化是同一个归并；既有的习得链与连接主义模型是其实例（P73、P74；理依 Ren 读作对结构与变化之"
      "规律的建模，其余读法是 AI 的，待 Ren）。这些规律在第一部分所及完成智慧之根的形式部分，实际形成的对应仍开放（P75）。")
cat = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
data = json.loads(cat.read_text())
entry = next(d for d in data if d['id'] == 'the-theory-of-becoming')
before_en = 'A formation can test only a claim that differs in what registers in it (P49'
before_zh = '一个形成只能检验在它所反映者中有所不同的主张（P49'
assert entry['argument_en'].count(before_en) == 1 and entry['argument_zh'].count(before_zh) == 1
assert EN not in entry['argument_en']
entry['argument_en'] = entry['argument_en'].replace(before_en, EN + before_en)
entry['argument_zh'] = entry['argument_zh'].replace(before_zh, ZH + before_zh)
B = f'{D}/becoming/Becoming/'
lean = entry['lean']
for after, new in ((B + 'Selection.lean', B + 'Learning.lean'),
                   (f'{D}/universal-ethics/generative-capacity/CorrectionInquiry.lean',
                    f'{D}/universal-ethics/evolution-connectionism/LearningCorrespondence.lean')):
    assert new not in lean and lean.count(after) == 1, (after, new)
    lean.insert(lean.index(after) + 1, new)
cat.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('reading entry: sentence and', len(lean), 'Lean files')
