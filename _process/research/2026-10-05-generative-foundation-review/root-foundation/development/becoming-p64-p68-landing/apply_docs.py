#!/usr/bin/env python3
"""Apply the documentation of P64–P68 to a checkout: four study sections and their English summary
entries, the unification plan's rows and bullets, and the chapter edits.

Usage: python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER

S is the first of four consecutive study sections: S for P64 (Selection), S+1 for P65 (Response), S+2
for P66 with P68 (Mechanism), S+3 for P67 (Attraction). PLAN_ZH_AFTER and PLAN_EN_AFTER are the
prefixes of the plan's table row and bullet these go after. Counts come from ROOT's receipts, which
must cover the four modules. Every anchor must occur exactly once; rerunning on an applied checkout
fails.
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
assert receipt['status'] == periphery['status'] == 'passed'
spine = [m for m in receipt['modules'] if m['spine']]
theorems = {m['module']: m['theorems'] for m in receipt['modules']}

# (key, module, study fragment prefix), in the order of the study sections.
MODULES = [('SELECTION', 'Selection', 'p64'), ('RESPONSE', 'Response', 'p65'), ('MECHANISM', 'Mechanism', 'p66'),
           ('ATTRACTION', 'Attraction', 'p67')]


def anchor(heading):
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces as hyphens."""
    text = heading.lstrip('#').strip().lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


VALUES = {
    '{RECEIPT}': receipt['utc'],
    '{PERIPHERY}': periphery['utc'],
    '{N_THM}': str(sum(m['theorems'] for m in spine)),
    '{N_DECL}': str(sum(len(m['declarations']) for m in spine)),
    '{N_CORE}': str(len(receipt['core_closure'])),
    '{LEAN}': '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming',
}
STUDY = {}
for i, (key, module, prefix) in enumerate(MODULES):
    sec = str(S + i)
    zh = (HERE / f'docs/study/{prefix}_zh.md').read_text()
    heading = zh.split('\n', 1)[0].replace('{S}', sec)
    assert heading.startswith(f'## {sec}. '), heading
    VALUES[f'{{S_{key}}}'] = sec
    VALUES[f'{{N_{key}}}'] = str(theorems[f'Becoming.{module}'])
    VALUES[f'{{ANCHOR_{key}}}'] = anchor(heading)
    VALUES[f'{{STUDY_{key}}}'] = f'{STUDY_LINK}#{anchor(heading)}'
    STUDY[key] = (sec, VALUES[f'{{N_{key}}}'], zh, (HERE / f'docs/study/{prefix}_en.md').read_text())


def fill(text, sec=None, n_module=None):
    if sec is not None:
        text = text.replace('{S}', sec).replace('{N_MODULE}', n_module)
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


def study_edits(s):
    for key, _, _ in MODULES:
        sec, n, zh, en = STUDY[key]
        s = insert_before_line(s, '## English summary', fill(zh, sec, n).rstrip('\n') + '\n', True)
        s = insert_before_line(s, 'The package now has ', fill(en, sec, n).rstrip('\n'), True, last=True)
    return s


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
    return s


edit('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', chapter_edits)
