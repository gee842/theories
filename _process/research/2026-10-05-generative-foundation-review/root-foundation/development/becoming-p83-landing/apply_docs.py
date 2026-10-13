#!/usr/bin/env python3
"""Apply the documentation of P83 to a checkout: the study section and its English summary entry, the
unification plan's row and bullet, and the chapter edits.

Usage: python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER

S is P83's study section. PLAN_ZH_AFTER and PLAN_EN_AFTER are the prefixes of the plan's table row and
bullet it goes after (after P70–P72: '| P72、P72q 语境中的识与量子实现' and '- **P72 and P72q:**'). Counts
come from ROOT's receipts, which must cover Becoming.Identification. The sections of P70 and P73 are
found by their headings. The layer is Description's, read from the receipt. The review sentences come
from docs/review.json. One sentence each is added to P73's counterreview point 3 and English summary,
which left the step of rest to P83. Every anchor must occur exactly once; the chapter anchors are lines the P70–P72
package adds, so apply this after it. Rerunning on an applied checkout fails.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
S = str(int(sys.argv[2]))
PLAN_ZH_AFTER, PLAN_EN_AFTER = sys.argv[3:5]
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY_PATH = f'{RF}/BECOMING-RENEWAL-READING.md'
STUDY_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'

receipt = json.loads((ROOT / D / 'becoming/becoming-verification.json').read_text())
periphery = json.loads((ROOT / D / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
assert receipt['status'] == periphery['status'] == 'passed'
modules = {m['module']: m for m in receipt['modules']}
assert 'Becoming.Identification' in modules and 'Becoming.Identification' in receipt['core_closure']
LAYER = modules['Becoming.Description']['layer']
review = json.loads((HERE / 'docs/review.json').read_text())


def anchor(heading):
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces as hyphens."""
    text = heading.lstrip('#').strip().lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


study = (ROOT / STUDY_PATH).read_text()


def section_of(tag):
    found = re.findall(r'^## (\d+)\. .*（[^）]*' + tag + r'[^）]*）$', study, flags=re.M)
    assert len(found) == 1, (tag, found)
    return found[0]


zh = (HERE / 'docs/study/p83_zh.md').read_text()
heading = zh.split('\n', 1)[0].replace('{S}', S)
assert heading.startswith(f'## {S}. '), heading
assert f'\n## {S}. ' not in study, f'section {S} is taken'

VALUES = {
    '{S}': S,
    '{S_DESCRIPTION}': section_of('P70'),
    '{S_LEARNING}': section_of('P73'),
    '{N_MODULE}': str(modules['Becoming.Identification']['theorems']),
    '{LAYER}': LAYER,
    '{RECEIPT}': receipt['utc'],
    '{PERIPHERY}': periphery['utc'],
    '{REVIEW_ZH}': review['zh'],
    '{REVIEW_EN}': review['en'],
    '{STUDY}': f'{STUDY_LINK}#{anchor(heading)}',
    '{LEAN}': '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming',
    '{SPINE_AFTER}': f'| {LAYER} | [Becoming.Description]',
}
print('P70 §', VALUES['{S_DESCRIPTION}'], 'P73 §', VALUES['{S_LEARNING}'], 'layer', LAYER)


def fill(text):
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


# P73's section left the step of rest to P83; at its owner's request one sentence each, in its counterreview
# point 3 and its English summary, says that P83 states it.
P73_ZH = ('（只是草图，此处未检查），留给 P83。',
          '（只是草图，此处未检查），留给 P83。P83 已给出这一步：轨道被长 N 的列表所持时，学习者从第 N + (2N − 1)·tri N 步起'
          '每步主张且正确（`Identification.held_learner_rests`，§{S}）。')
P73_EN = ('(a sketch, not checked here); that is left to P83.',
          '(a sketch, not checked here); that is left to P83. P83 states it: where the orbit is held by a list of length N, '
          'the learner claims and is right at every step from N + (2N − 1)·tri N on (`Identification.held_learner_rests`, '
          'section {S}).')


def study_edits(s):
    for read, revised in (P73_ZH, P73_EN):
        assert s.count(read) == 1, (read, s.count(read))
        s = s.replace(read, fill(revised))
    s = insert_before_line(s, '## English summary', fill(zh).rstrip('\n') + '\n', True)
    en = (HERE / 'docs/study/p83_en.md').read_text()
    return insert_before_line(s, 'The package now has ', fill(en).rstrip('\n'), True, last=True)


edit(STUDY_PATH, study_edits)

rows = (HERE / 'docs/plan_rows.md').read_text()
zh_row = fill(rows.split('=== ZH_ROW ===\n')[1].split('=== EN_BULLET ===')[0]).strip('\n')
en_bullet = fill(rows.split('=== EN_BULLET ===\n')[1]).strip('\n')
edit(f'{RF}/BECOMING-UNIFICATION-PLAN.md',
     lambda s: insert_after_line(insert_after_line(s, PLAN_ZH_AFTER, zh_row), PLAN_EN_AFTER, en_bullet))

spec = importlib.util.spec_from_file_location('chapter', HERE / 'docs/chapter.py')
chapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chapter)


def chapter_edits(s):
    for kind, anchor_text, text in chapter.EDITS:
        anchor_text, text = fill(anchor_text), fill(text)
        if kind == 'before':
            s = insert_before_line(s, anchor_text, text, not text.startswith(('- ', '| ')))
        elif kind == 'after_line':
            s = insert_after_line(s, anchor_text, text)
        else:
            assert s.count(anchor_text) == 1, (anchor_text[:80], s.count(anchor_text))
            s = s.replace(anchor_text, text)
    return s


edit(CHAPTER, chapter_edits)
