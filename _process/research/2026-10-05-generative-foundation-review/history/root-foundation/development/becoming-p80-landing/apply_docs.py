#!/usr/bin/env python3
"""Apply the documentation of P80 to a checkout: the study section and its English summary entry, the
unification plan's row and bullet, and the chapter edits.

Usage: python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER

S is P80's study section, the next after the last landed one. PLAN_ZH_AFTER and PLAN_EN_AFTER are the
prefixes of the plan's table row and bullet these go after. Counts come from ROOT's receipts, which
must cover Becoming.Counterfactual. Every anchor must occur exactly once; rerunning on an applied
checkout fails.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
S = sys.argv[2]
PLAN_ZH_AFTER, PLAN_EN_AFTER = sys.argv[3:5]
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'

receipt = json.loads((ROOT / D / 'becoming/becoming-verification.json').read_text())
periphery = json.loads((ROOT / D / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
assert receipt['status'] == periphery['status'] == 'passed'
spine = [m for m in receipt['modules'] if m['spine']]
theorems = {m['module']: m['theorems'] for m in receipt['modules']}
assert 'Becoming.Counterfactual' in theorems, 'Becoming.Counterfactual is not in the receipt'


def anchor(heading):
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces as hyphens."""
    text = heading.lstrip('#').strip().lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


zh = (HERE / 'docs/study/p80_zh.md').read_text()
en = (HERE / 'docs/study/p80_en.md').read_text()
heading = zh.split('\n', 1)[0].replace('{S}', S)
assert heading.startswith(f'## {S}. '), heading
VALUES = {
    '{S}': S,
    '{N_MODULE}': str(theorems['Becoming.Counterfactual']),
    '{ANCHOR}': anchor(heading),
    '{STUDY}': f'{STUDY_LINK}#{anchor(heading)}',
    '{RECEIPT}': receipt['utc'],
    '{PERIPHERY}': periphery['utc'],
    '{N_THM}': str(sum(m['theorems'] for m in spine)),
    '{N_DECL}': str(sum(len(m['declarations']) for m in spine)),
    '{N_CORE}': str(len(receipt['core_closure'])),
    '{LEAN}': '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming',
}


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


def insert_after_block(s, prefix, text):
    """After the paragraph starting with the prefix, as a paragraph of its own."""
    i = line_start(s, prefix)
    j = s.find('\n\n', i)
    assert j != -1, prefix[:80]
    return s[:j] + '\n\n' + text.strip('\n') + s[j:]


def edit(path, fn):
    p = ROOT / path
    s = p.read_text()
    s2 = fn(s)
    assert s2 != s, path
    p.write_text(s2)
    print('edited', path)


def study_edits(s):
    s = insert_before_line(s, '## English summary', fill(zh).rstrip('\n') + '\n', True)
    return insert_before_line(s, 'The package now has ', fill(en).rstrip('\n'), True, last=True)


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
        if kind == 'after_line':
            s = insert_after_line(s, anchor_text, text)
        elif kind == 'after_block':
            s = insert_after_block(s, anchor_text, text)
        else:
            assert kind == 'replace', kind
            assert s.count(anchor_text) == 1, (anchor_text[:80], s.count(anchor_text))
            s = s.replace(anchor_text, text)
    return s


edit('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', chapter_edits)
