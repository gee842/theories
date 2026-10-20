#!/usr/bin/env python3
"""Join LC1's extension of Becoming.LeastLoss to the package: copy the module in, and restate its README row, its
root doc bullet in Becoming.lean and its scope text in check_becoming.py.
usage (from the checkout root to edit): python3 -B integrate.py   (each edit must match exactly once)"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def edit(path, old, new):
    text = path.read_text(encoding='utf-8')
    assert text.count(old) == 1, ('edit does not match once', path.name, old[:90], text.count(old))
    path.write_text(text.replace(old, new), encoding='utf-8')
    print('edited', path.name)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'LeastLoss.lean', PKG / 'Becoming' / 'LeastLoss.lean')
print('copied LeastLoss.lean')

edit(PKG / 'README.md',
     'a loss above nothing needs a merge (Law.Lossless.regains, Law.Lossless.loses_nothing, Law.loss_needs_merge; along a '
     'run of every process Branching.Lossless.loses_nothing, Branching.loss_needs_merge) |',
     'a loss above nothing needs a merge (Law.Lossless.regains, Law.Lossless.loses_nothing, Law.loss_needs_merge; along a '
     'run of every process Branching.Lossless.loses_nothing, Branching.loss_needs_merge); rest from a finite reading, with '
     'no least loss: an amount read off configurations a list holds that does not rise falls strictly at most as often as '
     'the list is long, over any amounts (Amounts.falls_within_reading, Amounts.rests_of_finite_reading, along a run '
     'Branching.rests_along_run), so falls that recur need a reading no list holds (Halving.stock_unlisted); a part\'s '
     'merge paid by the rest: under a law merging nothing, possibilities no two alike, read by a part and a rest that '
     'tell them apart, number at most the part\'s count times the rest\'s (Law.distinct_within, Law.Lossless.keeps_apart, '
     'Law.Lossless.narrowing_paid), and a part reset at every step needs a whole no list holds '
     '(Law.Lossless.reset_unlisted; witness Reset.paid_by_rest) |')

edit(PKG / 'Becoming.lean',
     '  descriptions that lump and dissipate, and a finite law that merges nothing returns\n'
     '  (`Becoming.Recurrence`).\n',
     '  descriptions that lump and dissipate, and a finite law that merges nothing returns\n'
     '  (`Becoming.Recurrence`). Read off configurations a list holds, an amount that does not rise\n'
     '  falls strictly at most as often as the list is long, over any amounts, so rest needs no least\n'
     '  loss there; and under a law that merges nothing a part\'s narrowing is paid by the rest, the\n'
     '  possibilities being kept apart, so a part reset at every step needs a whole no list holds.\n')

edit(PKG / 'check_becoming.py',
     '"law along an orbit, so a loss above nothing needs a merge. "\n',
     '"law along an orbit, so a loss above nothing needs a merge; an amount read off configurations a "\n'
     '    "list holds that does not rise falls strictly at most as often as the list is long, over any "\n'
     '    "amounts, so its falls do not recur with no least loss, along a run of every process too, and the "\n'
     '    "halving stock\'s values are no list\'s; under a law merging nothing, possibilities no two alike "\n'
     '    "stay so, and read by a part and a rest that tell them apart number at most the part\'s count "\n'
     '    "times the rest\'s, so a part reset at every step needs a whole no list holds, as in Reset, whose "\n'
     '    "part merges at every step while the whole merges nothing. "\n')
