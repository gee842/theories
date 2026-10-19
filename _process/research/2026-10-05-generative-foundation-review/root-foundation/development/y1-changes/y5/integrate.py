#!/usr/bin/env python3
"""Join Y5's module to the core package: copy Becoming/HexagramSequences.lean in, import it after
Becoming.HexagramSites (Y4), add its root doc bullet after HexagramSites', its CORE entry after HexagramSites', its
scope text after HexagramSites' in check_becoming.py, and its README row after HexagramSites', so that the package
lists the five modules in the order of the chapter on the 易传.
usage: python3 -B integrate.py [PACKAGE_CHECKOUT_ROOT]
(the root defaults to the checkout holding this file; each edit must match exactly once)."""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


BULLET = (
    "* `Becoming.HexagramSequences` (L4): what of the arrangements of the 傳 is a law, with no\n"
    "  premise. A law runs the received order (序卦) exactly where it agrees everywhere but at 未濟\n"
    "  with the law taking each to the next; only the one closing 未濟 to 乾 merges nothing, with one\n"
    "  orbit of sixty-four. Every such law reads every line for every line, so no three-cell rule on\n"
    "  a ring of six runs the order, waxing and waning among them, though 剝 to 復 is a step of the\n"
    "  straight shift (剝窮上反下); none commutes with 錯, 綜 or both, so no rearrangement of the places\n"
    "  with a mask runs it. Exchanging two lines (卦變) keeps the count of unbroken lines; an exchange\n"
    "  across the trigrams is a step of the law of exchange between them (損下益上 and 損上益下 at 損\n"
    "  and 益), and from 泰 and 否 the exchanges stay among the twenty with three unbroken lines. The\n"
    "  parity of the count turns at every step of waxing and waning and every change of a line, a\n"
    "  lumping both go alike across; for trigrams it is 陽卦奇，陰卦偶, and a change of a line turns\n"
    "  its trigram's class. The 雜卦 keeps the received order's pairs, the last eight interleaved. No\n"
    "  run of waxing and waning rests or comes to rest. The stations of 說卦 ch. 5 are the run of no\n"
    "  law commuting with 錯, 綜 or the rotation; 交 holds at every height of 泰 and none of 否, which\n"
    "  every reading the complement keeps reads alike along their runs.\n")

SCOPE = (
    '    "HexagramSequences: a law runs a list where its run from the first member holds the list; the "\n'
    '    "laws running the received order agree everywhere but at its last member, the one taking the "\n'
    '    "last to the first is the only one merging nothing and has one orbit of all sixty-four; each "\n'
    '    "reads every line for every line, so no three-cell rule on a ring of six, with the wrap read "\n'
    '    "straight or turned, runs the order, the law of waxing and waning among them, while one step "\n'
    '    "of the order is a step of the straight shift; none commutes with the complement, the turning "\n'
    '    "over or both, so no rearrangement of places with a mask runs it, and none goes alike across "\n'
    '    "the pairs or the parity of the count; exchanging two lines keeps the count, an exchange of a "\n'
    '    "lower with an upper line is a step of the law of exchange between the two halves, every "\n'
    '    "course of exchanges read as a world balances, and the twenty configurations with three "\n'
    '    "unbroken lines are two and those one exchange across from them, among which every course of "\n'
    '    "exchanges from the two stays; the parity of the count turns at every step of waxing and "\n'
    '    "waning and every change of a line and is a lumping both go alike across, the nuclear law "\n'
    '    "not; for three lines an odd count is the uniform unbroken or the uniform broken with one "\n'
    '    "line changed, the strokes having the same parity, and along every course of changes a change "\n'
    '    "turns the parity of its half and keeps the other\'s; the 雜卦 lists each configuration once, "\n'
    '    "sets each beside its partner in its first fifty-six and interleaves the last four pairs, and "\n'
    '    "is the run of no law commuting with the symmetries; no run of waxing and waning or course of "\n'
    '    "changes rests at any step; the eight stations are the run of no law commuting with the "\n'
    '    "complement, the turning over, both or the rotation of three lines; every reading the "\n'
    '    "complement keeps reads a configuration and its complement alike along their runs, and the "\n'
    '    "lower line unbroken under a broken upper one at a height does not. No ethical premise is "\n'
    '    "used. "\n')

ROW = "| L4 | [`Becoming.HexagramSequences`](Becoming/HexagramSequences.lean) | what of the arrangements of the 傳 is a law (no premise): the received order is the run of laws agreeing with `orderNext` but at 未濟, exactly one lossless, one orbit of sixty-four (`runsOrder_agrees`, `runsOrder_lossless_iff`, `orderNext_one_orbit`); every such law reads every line for every line and commutes with no symmetry, so no three-cell rule on a ring, waxing and waning among them, and no rearrangement of places with a mask runs it (`runsOrder_reads`, `ringRule_not_runsOrder`, `waxWane_not_runsOrder`, `runsOrder_not_commutes`, `rearrange_not_runsOrder`), 剝 to 復 a step of the straight shift (`bo_fu`); 卦變 keeps the count and is a step of the law of exchange between the trigrams, 損 and 益 at 泰 and 否 (`yang_swap`, `across_exchange`, `named_exchanges`, `three_iff`, `exchanges_from_tai_pi`, `exchangeWorld_balances`); the parity of the count, a lumping waxing and waning and the change of lines go alike across, 陽卦奇 for trigrams, a change turning its trigram's class (`yangOdd_goAlike`, `yangOdd_goAlike_changes`, `odd3_iff`, `changes_run_trigram`); the 雜卦 keeps the pairs (`zagua_partners`, `zagua_last_eight`); no rest under waxing and waning (`never_comes_to_rest`); the stations of 說卦 ch. 5 keep no symmetry (`Trigram.stations_not_commutes`); 交 tells 泰 from 否 where every reading the complement keeps does not, along their runs (`kept_alike`, `tai_pi_runs`) |\n"

target = PKG / 'Becoming/HexagramSequences.lean'
assert not target.exists(), target

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.HexagramSites\n', 'import Becoming.HexagramSites\nimport Becoming.HexagramSequences\n')
Y4_END = ("  of the 彖, the 小象 and the line texts are checked on their configurations; every law is read\n"
          "  along runs.\n")
root = once(root, Y4_END, Y4_END + BULLET)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.HexagramSites", ', '"Becoming.HexagramSites", "Becoming.HexagramSequences", ')
Y4_SCOPE_END = ('    "read along the runs of the named process or of any process. No ethical premise is used. "\n'
                '    "Withholding: ')
chk = once(chk, Y4_SCOPE_END, Y4_SCOPE_END.replace('    "Withholding: ', SCOPE + '    "Withholding: '))

readme = (PKG / 'README.md').read_text()
lines = readme.splitlines(keepends=True)
hits = [i for i, line in enumerate(lines)
        if line.startswith('| L4 | [`Becoming.HexagramSites`](Becoming/HexagramSites.lean) |')]
assert len(hits) == 1, hits
lines.insert(hits[0] + 1, ROW)
shutil.copyfile(HERE / 'Becoming/HexagramSequences.lean', target)
(PKG / 'Becoming.lean').write_text(root)
(PKG / 'check_becoming.py').write_text(chk)
(PKG / 'README.md').write_text(''.join(lines))
print('integrated into', PKG)
