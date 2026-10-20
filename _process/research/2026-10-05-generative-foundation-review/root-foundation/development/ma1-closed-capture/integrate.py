#!/usr/bin/env python3
"""Join MA1's module Becoming.ClosedCapture to the core package: copy it in, import it after Becoming.RuleCapture,
add its root doc bullet after RuleCapture's, its CORE entry and scope text in check_becoming.py, and its README rows.
usage: python3 -B integrate.py   (MA1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['MA1_ROOT']).resolve() if os.environ.get('MA1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'ClosedCapture.lean', PKG / 'Becoming' / 'ClosedCapture.lean')

DOC = (
    "* `Becoming.ClosedCapture` (L1): a loop whose every level reads only the share. On `RuleCapture`'s\n"
    "  two-level course with the fast configuration a pair, the share and what lies beyond it: where\n"
    "  neither the next share nor the rule read reads what lies beyond, courses alike in share and rule\n"
    "  stay alike in both, and the share's law joined with a step beyond runs exactly as the share's law\n"
    "  alone; so a locked loop stays locked while a loss rising by at least one a step passes every bound, and a\n"
    "  reading favouring at no loss above a bound turns at the step after the first reading step past it\n"
    "  (`Beyond`: the same selection locked read from the share, falling read from the loss). Where how\n"
    "  the rule is read is itself formed from the share, rule and reading are one rule read from the\n"
    "  share: a change of the reading alone is absorbed at the next reading step, and where the rule read\n"
    "  favours at every reading every course locks from its second reading step (`Proportional`).\n"
)
SCOPE = (
    '    "ClosedCapture: where neither the next share nor the rule read reads what lies beyond the share, "\n'
    '    "courses alike in share and rule stay alike in both whatever lies beyond, the share\'s law joined "\n'
    '    "with a step beyond runs exactly as the share\'s law alone, a locked loop stays locked while a loss "\n'
    '    "rising by at least one a step passes every bound, and a reading favouring at no loss above a bound turns "\n'
    '    "at the step after the first reading step past it; where how the rule is read is formed from the "\n'
    '    "share, rule and reading are one rule read from the share, a change of the reading alone is "\n'
    '    "absorbed at the next reading step, and a rule read favouring at every reading locks every course "\n'
    '    "from its second reading step. "\n')
README_ROW = (
    '| L1 | [`Becoming.ClosedCapture`](Becoming/ClosedCapture.lean) | a loop whose every level reads only the share (no '
    'premise beyond the hypotheses named): where neither the next share nor the rule read reads what lies beyond the '
    'share (`ClosedCapture.Unread`), courses alike in share and rule stay alike in both (`ClosedCapture.unread_course`, '
    '`ClosedCapture.reads_beyond_of_apart`), and the share\'s law joined with a step beyond runs as the share\'s law alone '
    '(`ClosedCapture.join_course`); a locked loop outlives a loss passing every bound (`ClosedCapture.lock_outlives_loss`), '
    'and a reading of the loss turns past its bound (`ClosedCapture.turned_by_loss`; witness `ClosedCapture.Beyond`, '
    '`Beyond.closed_locked`, `Beyond.open_falls`); where how the rule is read is formed from the share, rule and reading '
    'are one rule read from the share (`ClosedCapture.both_reads`), a change of the reading is absorbed '
    '(`ClosedCapture.reading_absorbed`, `ClosedCapture.readers_not_below`, `ClosedCapture.readers_uniform_locks`; '
    'witness `ClosedCapture.Proportional.reform_absorbed`) |')
README_ZH_ROW = (
    '| L1 | [`Becoming.ClosedCapture`](Becoming/ClosedCapture.lean) | 每一层都只读份额的回路（除所列假设外不加前提）：'
    '下一份额与读出的规则都不读份额之外者时（`ClosedCapture.Unread`），份额与规则相同的进程在两者上始终相同'
    '（`ClosedCapture.unread_course`、`ClosedCapture.reads_beyond_of_apart`），带份额之外一步的合并之律与份额自身之律同样运行'
    '（`ClosedCapture.join_course`）；锁定的回路比越过每一界限的损失更持久（`ClosedCapture.lock_outlives_loss`），'
    '读损失的读法在越过其界限后转向（`ClosedCapture.turned_by_loss`；见证 `ClosedCapture.Beyond`）；规则怎样被读本身由份额形成之处，'
    '规则与读法合为一个从份额读出的规则（`ClosedCapture.both_reads`），只改读法被吸收（`ClosedCapture.reading_absorbed`、'
    '`ClosedCapture.readers_uniform_locks`；见证 `ClosedCapture.Proportional.reform_absorbed`） |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.ClosedCapture' not in root, 'already integrated'
root = once(root, 'import Becoming.RuleCapture\n', 'import Becoming.RuleCapture\nimport Becoming.ClosedCapture\n')
root = once(root, '* `Becoming.PatternPassing` (L1): a pattern that outlasts each of its carriers',
            DOC + '* `Becoming.PatternPassing` (L1): a pattern that outlasts each of its carriers')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.RuleCapture",', '"Becoming.RuleCapture", "Becoming.ClosedCapture",')
chk = once(chk, '    "PatternPassing: on a web whose activity is carrying,',
           SCOPE + '    "PatternPassing: on a web whose activity is carrying,')
(PKG / 'check_becoming.py').write_text(chk)

for name, row, after in (('README.md', README_ROW, '| L1 | [`Becoming.RuleCapture`](Becoming/RuleCapture.lean) |'),
                         ('README.zh.md', README_ZH_ROW, '| L1 | [`Becoming.Capture`](Becoming/Capture.lean) |')):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(after)]
    assert len(idx) == 1, (name, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
