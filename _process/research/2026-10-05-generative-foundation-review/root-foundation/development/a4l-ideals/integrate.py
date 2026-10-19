#!/usr/bin/env python3
"""Join A4-L's modules to the core package: copy Becoming/Ideals.lean and Becoming/HistoryIdeals.lean in, import them
(Ideals after Becoming.Naturals, HistoryIdeals after Becoming.HistoryLanguages), add their root doc bullets after those
modules' bullets, their CORE entries at the same places and their scope text after Horizon's in check_becoming.py, and
their README rows. usage: python3 -B integrate.py   (each edit must match exactly once)"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


for name in ('Ideals', 'HistoryIdeals'):
    assert not (PKG / f'Becoming/{name}.lean').exists(), name
    shutil.copyfile(HERE / f'Becoming/{name}.lean', PKG / f'Becoming/{name}.lean')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Naturals\n', 'import Becoming.Naturals\nimport Becoming.Ideals\n')
root = once(root, 'import Becoming.HistoryLanguages\n', 'import Becoming.HistoryLanguages\nimport Becoming.HistoryIdeals\n')
root = once(root, "* `Becoming.Naturals` (L2): the subtraction and order laws of drawn amounts (no premise):\n"
            "  cancellation, `sub_sub`, `le_sub_of_add_le` and the bounds of a sum, proved by recursion where\n"
            "  the prelude uses `propext`.\n",
            "* `Becoming.Naturals` (L2): the subtraction and order laws of drawn amounts (no premise):\n"
            "  cancellation, `sub_sub`, `le_sub_of_add_le` and the bounds of a sum, proved by recursion where\n"
            "  the prelude uses `propext`.\n"
            "* `Becoming.Ideals` (L2): a history read off its finite stretches, as an ideal of their order\n"
            "  (no premise; it imports nothing). A refutable reading holds, up to double negation, where a\n"
            "  point adheres, and what adheres is closed. A class of ideals is closed exactly where it is the\n"
            "  class within a lower set, its content. A refutable class is closed, and a closed class\n"
            "  refutable, each up to a step that, asked of every order and class, is exactly double-negation\n"
            "  elimination. The least closed hull, avoidance and a lower set's order; the completion:\n"
            "  directed-complete, compact exactly at finite histories, a monotone map extended continuously\n"
            "  and uniquely, and a compact basis that generates fixing its completion.\n")
root = once(root, "* `Becoming.HistoryLanguages` (L3): languages of histories (no premise): a prefix-closed language\n"
            "  of words is realized exactly by the law of its histories (`realizes_feasible`); continuation\n"
            "  profiles, letterwise stability and the obstruction that locates a changed profile; the bounded\n"
            "  language, the latch and the gate.\n",
            "* `Becoming.HistoryLanguages` (L3): languages of histories (no premise): a prefix-closed language\n"
            "  of words is realized exactly by the law of its histories (`realizes_feasible`); continuation\n"
            "  profiles, letterwise stability and the obstruction that locates a changed profile; the bounded\n"
            "  language, the latch and the gate.\n"
            "* `Becoming.HistoryIdeals` (L3): histories as ideals of their finite stretches (no premise). A\n"
            "  run is the ideal of the stretches it passes through. The laws of `Becoming.Ideals` are read on\n"
            "  the histories of every process, and the laws of `Becoming.Horizon` on what a finite history\n"
            "  refutes are their case of runs. Adhering is the least closed class, with no double negation; a\n"
            "  run lies in a closed class where each of its stretches is a stretch of the class; asked of every\n"
            "  process, a refutable class is closed, and a closed class refutable, each exactly under\n"
            "  double-negation elimination. Avoidance, a lower set's own histories, and the completion at\n"
            "  runs: no run is compact, and a continuous reading is fixed at every run by its finite\n"
            "  histories. A history that settles, or goes on with its stretches picked, is a finite history\n"
            "  or a run, and telling which on the histories cut at a sequence's first `true` is the limited\n"
            "  principle of omniscience. Words and histories under prefix; for the process of all sequences,\n"
            "  the runs' histories are the infinite histories of words; prefix-closed languages give closed\n"
            "  classes of histories.\n")
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.ListTests", "Becoming.Naturals", "Becoming.ContingentPlans",',
           '"Becoming.ListTests", "Becoming.Naturals", "Becoming.Ideals", "Becoming.ContingentPlans",')
chk = once(chk, '"Becoming.HistoryLanguages", "Becoming.Coverage",',
           '"Becoming.HistoryLanguages", "Becoming.HistoryIdeals", "Becoming.Coverage",')
chk = once(chk, '    "the support-gated law, whose renewal stops below support. "\n',
           '    "the support-gated law, whose renewal stops below support. "\n'
           '    "Ideals: a history read off its finite stretches is an ideal of their order; a refutable reading "\n'
           '    "of points holds, up to double negation, where a point adheres, and what adheres is closed; a class "\n'
           '    "of ideals is closed exactly where it is the class within a lower set, its content; a refutable "\n'
           '    "class is closed, and a closed class refutable, each up to a step that, asked of every order and "\n'
           '    "class, is exactly double-negation elimination; the least closed hull, avoidance and a lower set\'s "\n'
           '    "order; the ideals are directed-complete, compact exactly at finite histories, a monotone map "\n'
           '    "extends continuously and uniquely, and a compact basis that generates fixes its completion. "\n'
           '    "HistoryIdeals: a run is the ideal of its stretches; the laws of Ideals are read on the histories "\n'
           '    "of every process, and Horizon\'s laws of what a finite history refutes are their case of runs; "\n'
           '    "adhering is the least closed class, with no double negation; a reading of runs holding every "\n'
           '    "adhering run is made of tests on stretches; asked of every process, a refutable class is closed, "\n'
           '    "and a closed class refutable, each exactly under double-negation elimination, and a refutable "\n'
           '    "reading holds at every adhering run exactly under it; avoidance, a lower set\'s own histories and "\n'
           '    "the completion at runs; a history that settles, or goes on with its stretches picked, is a finite "\n'
           '    "history or a run, and telling which on cut histories is the limited principle of omniscience; a "\n'
           '    "history\'s ideal lies below another\'s exactly where it is a prefix of it, and for the process of "\n'
           '    "all sequences the runs\' histories are the infinite histories of words; prefix-closed languages "\n'
           '    "give closed classes of histories. "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
for prefix, row in [
        ('| L2 | [`Becoming.Naturals`](Becoming/Naturals.lean) |',
         '| L2 | [`Becoming.Ideals`](Becoming/Ideals.lean) | a history read off its finite stretches (no premise; imports '
         'nothing): ideals of an order of stretches; a refutable reading holds, up to double negation, where a point '
         'adheres (`RefutableBy.not_not`); a class of ideals is closed exactly where it is the class within a lower '
         'set, its content (`closed_iff_lower`, `lower_iff_content`); a refutable class is closed, and a closed class '
         'refutable, each up to a step that is exactly double-negation elimination asked of every order and class '
         '(`Refutable.closed`, `Closed.refutable_iff`, `refutable_closed_iff`, `closed_refutable_iff`); the least '
         'closed hull (`hull_least`, `hull_unique`), avoidance (`avoids_iff_within`) and a lower set\'s order '
         '(`lift_restrict`, `restrict_lift`); the completion: directed-complete (`idealComplete`), compact exactly at '
         'finite histories (`compact_iff_principal`), continuous extension, unique (`unique_continuous_extension`), '
         'and the completion of a compact basis (`unique_basis_representation`) |'),
        ('| L3 | [`Becoming.HistoryLanguages`](Becoming/HistoryLanguages.lean) |',
         '| L3 | [`Becoming.HistoryIdeals`](Becoming/HistoryIdeals.lean) | histories as ideals of their finite '
         'stretches (no premise): a run is the ideal of its stretches (`Run.stretches`, `Run.stretches_le_iff`); the '
         'laws of `Becoming.Ideals` read on the histories of every process (`Stretches`), with Horizon\'s laws of what '
         'a finite history refutes as their case of runs (`refutable_iff_refutableBy`, `adheres_iff_adheresBy`, '
         '`Stretches.not_not`); adhering is the least closed class, with no double negation '
         '(`Stretches.adheres_iff_closed`); a reading of runs holding every adhering run is made of tests on stretches '
         '(`closed_iff_within_lower`); asked of every process, a refutable class is closed, and a closed class '
         'refutable, each exactly under double-negation elimination (`Stretches.refutable_closed_iff`, '
         '`Stretches.closed_refutable_iff`), and a refutable reading holds at every adhering run exactly under it '
         '(`refutable_holds_iff`); avoidance (`Stretches.avoids_runs`), a lower set\'s own histories '
         '(`Stretches.inherited_histories`) and the completion at runs (`Stretches.run_not_compact`, '
         '`Stretches.run_reading_unique`); a history that settles, or goes on with its stretches picked, is a finite '
         'history or a run (`Stretches.classification`), and telling which on cut histories is LPO '
         '(`Stretches.cut_decided_iff_lpo`); words and histories under prefix (`history_le_iff`, '
         '`HistoryIdeals.classification`), the runs of the process of all sequences as infinite histories of words '
         '(`Stretches.sequences_le_iff`); prefix-closed languages give closed classes (`history_within_iff`), and the '
         'finite histories with the infinite ones of a property are not refutable where a sequence lies outside it '
         '(`finiteOr_not_refutable`) |')]:
    idx = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
