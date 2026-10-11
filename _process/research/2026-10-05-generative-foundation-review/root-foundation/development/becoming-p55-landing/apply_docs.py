#!/usr/bin/env python3
"""Apply P55's documentation to a checkout: the study section and its English paragraph, the
unification plan's row and bullet, and the chapter edits.

Usage: python3 -B apply_docs.py ROOT SECTION P49_SECTION PLAN_ZH_AFTER PLAN_EN_AFTER

SECTION is P55's study section number and P49_SECTION P49's; PLAN_ZH_AFTER and PLAN_EN_AFTER are
the prefixes of the plan's table row and bullet that P55 goes after. Counts come from ROOT's
receipts. Every anchor must occur exactly once; rerunning on an applied checkout fails.
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
SEC, P49SEC, PLAN_ZH_AFTER, PLAN_EN_AFTER = sys.argv[2:6]
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'

receipt = json.loads((ROOT / D / 'becoming/becoming-verification.json').read_text())
periphery = json.loads((ROOT / D / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
assert receipt['status'] == periphery['status'] == 'passed'
spine = [m for m in receipt['modules'] if m['spine']]
VALUES = {
    '{S}': SEC,
    '{P49}': P49SEC,
    '{ANCHOR}': f'{SEC}-失控经自身反映的回路所不能反映的p55',
    '{RECEIPT}': receipt['utc'],
    '{PERIPHERY}': periphery['utc'],
    '{N_MODULE}': str(next(m for m in receipt['modules'] if m['module'] == 'Becoming.Runaway')['theorems']),
    '{N_THM}': str(sum(m['theorems'] for m in spine)),
    '{N_DECL}': str(sum(len(m['declarations']) for m in spine)),
    '{N_CORE}': str(len(receipt['core_closure'])),
}


def fill(text):
    for k, v in VALUES.items():
        text = text.replace(k, v)
    assert all(k not in text for k in VALUES), text[:200]
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


study_zh = fill((HERE / 'docs/study_zh.md').read_text()).rstrip('\n') + '\n'
study_en = fill((HERE / 'docs/study_en.md').read_text()).rstrip('\n')
edit(f'{RF}/BECOMING-RENEWAL-READING.md',
     lambda s: insert_before_line(insert_before_line(s, '## English summary', study_zh, True),
                                  'The package now has ', study_en, True, last=True))

rows = (HERE / 'docs/plan_rows.md').read_text()
zh_row = fill(rows.split('=== ZH_ROW ===\n')[1].split('=== EN_BULLET ===')[0]).strip('\n')
en_bullet = fill(rows.split('=== EN_BULLET ===\n')[1]).strip('\n')
edit(f'{RF}/BECOMING-UNIFICATION-PLAN.md',
     lambda s: insert_after_line(insert_after_line(s, PLAN_ZH_AFTER, zh_row), PLAN_EN_AFTER, en_bullet))

spec = importlib.util.spec_from_file_location('chapter', HERE / 'docs/chapter.py')
chapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chapter)


def chapter_edits(s):
    for kind, anchor, text in chapter.EDITS:
        text = fill(text)
        if kind == 'before':
            s = insert_before_line(s, anchor, text, not text.startswith('- '))
        elif kind == 'after_line':
            s = insert_after_line(s, anchor, text)
        else:
            assert s.count(anchor) == 1, (anchor[:80], s.count(anchor))
            s = s.replace(anchor, text)
    return s


edit('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', chapter_edits)
