#!/usr/bin/env python3
"""Join IV2's extension of Becoming.Weightings to the core package: copy the module in, and extend its root doc
bullet, its scope text in check_becoming.py and its README rows (EN and ZH). No new module: the layer and the
import tree are unchanged.
usage: python3 -B integrate.py   (IV2_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['IV2_ROOT']).resolve() if os.environ.get('IV2_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'Weightings.lean', PKG / 'Becoming' / 'Weightings.lean')

root = (PKG / 'Becoming.lean').read_text()
assert 'selfAscribed' not in root, 'already integrated'
root = once(root, "  retains where the condition loses the dweller. The readings are the AI's (D59).\n",
            "  retains where the condition loses the dweller. A content held de se, a property each standpoint\n"
            "  ascribes to itself, is standpoint-invariant exactly where its readings at the centers agree; held de\n"
            "  se the presupposition gives each center its own closure, held de dicto the step forces the union of\n"
            "  closures, and the two agree exactly where the closures do (`selfAscribed_iff_withinSome`). Invariant\n"
            "  grades give invariant standing, not conversely (`Partial`); a strictly increasing transform of\n"
            "  levels of continuation ranks every widening higher, one strictly concave up to a bound decides\n"
            "  transfers C leaves mixed, and a threshold of sufficiency ties above it. The readings are the AI's\n"
            "  (D59, D60).\n")
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
OLD = '    "center, the clearer\'s part retains at the centers and loses the dweller under the condition. "\n'
chk = once(chk, OLD, OLD +
           '    "Held de se, as a property each standpoint ascribes to itself, the presupposition gives each center "\n'
           '    "its own closure, standpoint-invariant exactly where the closures agree and the condition exactly where "\n'
           '    "each is the whole; standpoint-invariance is holding one shared content, and held de dicto the step "\n'
           '    "forces the union of the closures, which a web admits exactly by admitting it; invariant grades give "\n'
           '    "invariant standing and rank alike, invariant standing does not give invariant grades; a strictly "\n'
           '    "increasing transform of the steps of continuation admitted ranks every widening higher, one strictly "\n'
           '    "concave up to a bound ranks higher a one-step transfer to a lower level, and a transform rising no "\n'
           '    "further from a threshold ties levels at or above it. "\n')
(PKG / 'check_becoming.py').write_text(chk)

EN = ("; held de se the presupposition gives each center its own closure, held de dicto the step forces the union "
      "(`ownClosure_standpointInvariant_iff`, `forced_iff_within_some`, `selfAscribed_iff_withinSome`, "
      "`Web.admitsWithin_forced_iff`); invariant grades give invariant standing, not conversely "
      "(`Weighting.ranks_alike_of_gradeInvariant`, `Partial.ranks_differ`); priority on levels of continuation "
      "agrees with C and decides transfers, sufficiency ties above its threshold (`Weighting.prior_lt_of_widens`, "
      "`Weighting.prior_transfer`, `Weighting.sufficient_ties`); the readings are the AI's (D59, D60) |")
ZH = ("；从己地持有，预设给每个中心其自身的闭包，从言地持有，那一步迫使诸闭包之并（`ownClosure_standpointInvariant_iff`、"
      "`forced_iff_within_some`、`selfAscribed_iff_withinSome`、`Web.admitsWithin_forced_iff`）；等级不变则“是否算数”不变，"
      "反之不然（`Weighting.ranks_alike_of_gradeInvariant`、`Partial.ranks_differ`）；延续层级上的优先与 C 一致并决定转移，"
      "充足在阈值之上持平（`Weighting.prior_lt_of_widens`、`Weighting.prior_transfer`、`Weighting.sufficient_ties`）；"
      "读法是 AI 的（D59、D60） |")
for name, old, new in (('README.md', "; the readings are the AI's (D59) |", EN), ('README.zh.md', '；读法是 AI 的（D59） |', ZH)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('| L2 | [`Becoming.Weightings`]')]
    assert len(idx) == 1 and lines[idx[0]].endswith(old), (name, idx)
    lines[idx[0]] = lines[idx[0]][:-len(old)] + new
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
