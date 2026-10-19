#!/usr/bin/env python3
"""Join Y3's module to the core package: copy Becoming/HexagramLaws.lean in, import it after Becoming.HexagramPlaces,
add its root doc bullet after HexagramPlaces', its CORE entry after HexagramPlaces', its scope text after
HexagramPlaces' in check_becoming.py, and its README row after HexagramPlaces'. usage: python3 -B integrate.py
[PACKAGE_CHECKOUT_ROOT] (the root defaults to the checkout holding this file; each edit must match exactly once)."""
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
    "* `Becoming.HexagramLaws` (L4): four more laws on the sixty-four configurations and the census\n"
    "  of the law of waxing and waning, with no premise, stated along the runs of the spine. The\n"
    "  nuclear law (互) merges: what it makes of a hexagram is fixed by the four inner lines, and\n"
    "  within two steps every run is in 乾, 坤 or the turns of 既濟 and 未濟, exactly the four that\n"
    "  return, the first two and the last two of the received order, lines 3 and 4 telling which.\n"
    "  The cast of turning and staying lines (之卦) merges and settles in one step; the hexagram\n"
    "  shown is not a lumping the law goes alike across, the hexagram the lines go to is. Keeping,\n"
    "  changing every line (錯), turning over (綜) and both form a four-group with twenty classes,\n"
    "  eight of two and twelve of four, which the nuclear law goes alike across and the law of\n"
    "  waxing and waning does not; the configurations turning over keeps are those the received\n"
    "  order pairs by changing every line. Adding one merges nothing and has one orbit of\n"
    "  sixty-four, line k turning every 2 ^ (k - 1) steps. The law of waxing and waning keeps the\n"
    "  changes of line once round (承 and 乘 with the ends), one, three or five, and has six orbits,\n"
    "  five of twelve steps and one of four.\n")

SCOPE = (
    "    \"HexagramLaws: the nuclear law, lines 2 to 4 below and 3 to 5 above, is fixed by the four \"\n"
    "    \"inner lines, merges and loses a possibility, leaves only lines 3 and 4 three times over after \"\n"
    "    \"two steps, rests exactly at all unbroken and all broken, takes the two alternating \"\n"
    "    \"configurations each to the other, draws every run into these four within two steps, so that \"\n"
    "    \"exactly these four return, the first two and the last two of the received order, four at \"\n"
    "    \"once, twelve at the first step and forty-eight at the second, sixteen to each fixed one and \"\n"
    "    \"thirty-two to the turns as lines 3 and 4 tell; lines 3 and 4 are a lumping it goes alike \"\n"
    "    \"across and the count of unbroken lines is not; it commutes with the complement and with \"\n"
    "    \"turning over, so the runs from a configuration and its complement never meet; the four \"\n"
    "    \"symmetries form a group of four, each its own inverse, any two commuting, with twenty \"\n"
    "    \"classes, eight of two and twelve of four, a lumping the nuclear law goes alike across and \"\n"
    "    \"the law of waxing and waning does not; the configurations turning over keeps are exactly \"\n"
    "    \"those the received order pairs by the complement, and those turning over and the complement \"\n"
    "    \"take alike are the pairs in which the two agree; turning lines change into their opposites \"\n"
    "    \"and stay, a merging law settled in one step, returning exactly where no line turns, the \"\n"
    "    \"hexagram shown not a lumping it goes alike across and the hexagram the lines go to one; \"\n"
    "    \"adding one, line 1 lowest, merges nothing and has one orbit of sixty-four, line k turning \"\n"
    "    \"every 2 ^ (k - 1) steps with the lines below as they were; the law of waxing and waning keeps \"\n"
    "    \"the rises and falls with one more where the bottom and top lines agree, one, three or five \"\n"
    "    \"on twelve, forty and twelve configurations, so it does not reach every configuration from \"\n"
    "    \"every other, and has six orbits, of twelve, twelve, twelve, twelve, four and twelve \"\n"
    "    \"configurations, the orbit a lumping it goes alike across. No ethical premise is used. \"\n")

ROW = (
    "| L4 | [`Becoming.HexagramLaws`](Becoming/HexagramLaws.lean) | four more laws on the hexagram world and the "
    "census of waxing and waning (no premise), along the runs of the spine: the nuclear law 互 is fixed by the inner "
    "lines and merges (`nuclear_inner`, `run_inner`, `nuclear_merges`), two steps leave lines 3 and 4 "
    "(`nuclear_two`, `run_two_middle`), and exactly 乾, 坤, 既濟 and 未濟 return, the ends of the received order "
    "(`returns_iff_attractor`, `process_returns_iff_ends`, `nuclear_two_fixed_one_cycle`), entered within two steps "
    "(`run_in_attractor`, `entry_counts`, `basin_counts`); it commutes with the four symmetries (`nuclear_act`, "
    "`nuclear_run_act`, `run_complement_apart`), which form a group of four with twenty classes (`Symmetry.act_comp`, "
    "`class_census`, `classes_goAlike`, `classes_not_goAlike_waxWane`, `turn_fixed_iff`); the cast of turning lines "
    "settles in one step and returns exactly where no line turns (`MarkedLines.run_settled`, "
    "`MarkedLines.returns_iff`), the hexagram shown not a lumping and the hexagram gone to one "
    "(`MarkedLines.shown_not_goAlike`, `MarkedLines.onward_goAlike`); adding one has one orbit of sixty-four "
    "(`addOne_one_orbit`) with line k turning every 2 ^ (k - 1) steps (`line_turns`); waxing and waning keeps the "
    "changes around (`changesAround_run`, `changesAround_values`) and has six orbits (`starts_return`, "
    "`reach_keeps_orbit`, `orbit_census`) |\n")

target = PKG / 'Becoming/HexagramLaws.lean'
assert not target.exists(), target
shutil.copyfile(HERE / 'Becoming/HexagramLaws.lean', target)

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.HexagramPlaces\n', 'import Becoming.HexagramPlaces\nimport Becoming.HexagramLaws\n')
# The bullet goes after HexagramPlaces' bullet, before the next one.
start = root.index("* `Becoming.HexagramPlaces` (L4)")
end = root.index("\n* `", start) + 1
assert root.count("* `Becoming.HexagramPlaces` (L4)") == 1
root = root[:end] + BULLET + root[end:]
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.HexagramPlaces", ', '"Becoming.HexagramPlaces", "Becoming.HexagramLaws", ')
# The scope text goes after HexagramPlaces' text, which ends at its first "premise is used. ".
assert chk.count('    "HexagramPlaces: ') == 1
start = chk.index('    "HexagramPlaces: ')
end = chk.index('premise is used. "\n', start) + len('premise is used. "\n')
chk = chk[:end] + SCOPE + chk[end:]
(PKG / 'check_becoming.py').write_text(chk)

readme = (PKG / 'README.md').read_text()
lines = readme.splitlines(keepends=True)
hits = [i for i, line in enumerate(lines)
        if line.startswith('| L4 | [`Becoming.HexagramPlaces`](Becoming/HexagramPlaces.lean) |')]
assert len(hits) == 1, hits
lines.insert(hits[0] + 1, ROW)
(PKG / 'README.md').write_text(''.join(lines))
print('integrated into', PKG)
