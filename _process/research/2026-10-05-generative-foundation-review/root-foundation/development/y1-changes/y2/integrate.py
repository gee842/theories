#!/usr/bin/env python3
"""Join Y2's module to the core package: copy Becoming/HexagramPlaces.lean in, import it after Becoming.Hexagrams, add
its root doc bullet after Hexagrams', its CORE entry after Hexagrams', its scope text after Hexagrams' in
check_becoming.py, and its README row after Hexagrams'. usage: python3 -B integrate.py [PACKAGE_CHECKOUT_ROOT]
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
    "* `Becoming.HexagramPlaces` (L4): the relations of the places of a hexagram, read in context,\n"
    "  with no premise. A line is in phase where its value is its place's parity (正), the two lines\n"
    "  at one height of the two trigrams are opposed where they differ (應), adjacent lines\n"
    "  alternate, rise or fall across their seam (比, 承, 乘), and the middle height is lines 2 and 5\n"
    "  (中). Each relation is a reading indexed by its sites (`Contextual`): it glues to a reading of\n"
    "  the whole configuration exactly where every site shows the same, so the phases glue only at\n"
    "  既濟 and 未濟, and the two trigrams read as contexts glue exactly where no height is opposed,\n"
    "  no frame of context-free claims fitting the heights. Opposition is told by phase: the lines\n"
    "  at a height are opposed exactly where both or neither are in phase. The complement turns every\n"
    "  phase and keeps every opposition; the change of a line turns its phase and its height's\n"
    "  opposition and nothing else. Under the law of waxing and waning a line's phase turns at every\n"
    "  rise, so the count in phase changes parity at every step (3, 2, 3, ... from 乾), while the\n"
    "  oppositions run under the same law on three cells, a lumping the law goes alike across.\n"
    "  Four censuses of the 彖 and the 小象 are checked on their configurations; the chapter on the\n"
    "  易传 reads each passage.\n")

SCOPE = (
    "    \"HexagramPlaces: a line is in phase where its value is its place's parity, the lines at one \"\n"
    "    \"height of the two trigrams are opposed where they differ, adjacent lines alternate, rise or \"\n"
    "    \"fall across their seam, and the middle places are lines 2 and 5; a relation read at its \"\n"
    "    \"sites glues to a reading of the whole configuration exactly where every site shows the same, \"\n"
    "    \"the phases exactly at the two configurations with every line in phase or none, the seams at \"\n"
    "    \"four, the oppositions where every height or none is opposed; the two trigrams read as \"\n"
    "    \"contexts glue exactly where no height is opposed, so no frame of context-free claims fits \"\n"
    "    \"the heights while the indexed frame does; the lines at a height are opposed exactly where \"\n"
    "    \"both or neither are in phase; the complement turns every phase, keeps every opposition and \"\n"
    "    \"alternation and exchanges rises and falls, and turning over does the same at the mirrored \"\n"
    "    \"site; changing a line turns its phase and its height's opposition and nothing else, moving \"\n"
    "    \"the count in phase by one; under the law of waxing and waning each line rises with its value \"\n"
    "    \"and its phase turns, so the counts in phase before and after a step add to five or seven and \"\n"
    "    \"the count changes parity at every step, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 3, 4 along the twelve \"\n"
    "    \"steps from all unbroken, and is not a lumping the law goes alike across; alternations travel \"\n"
    "    \"with their lines; the oppositions run under the law of waxing and waning on three cells, a \"\n"
    "    \"lumping the law goes alike across, three steps turning every one, six keeping it, two \"\n"
    "    \"keeping it exactly for two patterns; rises and the bottom line count as many as falls and \"\n"
    "    \"the top line; the listed statements of four censuses of the text hold of their \"\n"
    "    \"configurations. No ethical premise is used. \"\n")

ROW = (
    "| L4 | [`Becoming.HexagramPlaces`](Becoming/HexagramPlaces.lean) | the relations of the places of a hexagram, "
    "read in context (no premise): in phase (正), opposed at a height of the two trigrams (應), alternating, rising "
    "or falling across a seam (比, 承, 乘), the middle (中); a relation read at its sites glues to a reading of the "
    "whole exactly where every site shows the same (`atSites_glues_iff`), the phases at 既濟 and 未濟 "
    "(`phases_glue_iff`), the trigrams where no height is opposed (`halves_glues_iff`, `halves_no_free_frame`); "
    "opposition is told by phase (`opposed_iff_phase`); the complement turns every phase and keeps every "
    "opposition (`inPhase_complement`, `opposed_complement`); the change of a line turns its phase and its "
    "height's opposition only (`inPhase_flip_self`, `opposed_flip_other`); under the law of waxing and waning the "
    "count in phase changes parity at every step (`phaseCount_waxWane`, `phase_qian_orbit`) and the oppositions "
    "run under the same law on three cells (`opposition_waxWane`, `opposition_goAlike`); four censuses of the 彖 "
    "and the 小象 hold of their configurations (`placeStatements_agree`, `centreStatements_agree`, "
    "`fallStatements_agree`, `middleOppositionStatements_agree`) |\n")

target = PKG / 'Becoming/HexagramPlaces.lean'
assert not target.exists(), target
shutil.copyfile(HERE / 'Becoming/HexagramPlaces.lean', target)

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Hexagrams\n', 'import Becoming.Hexagrams\nimport Becoming.HexagramPlaces\n')
root = once(root, "  list. What the passages of the text say beyond these laws is read in the chapter on the 易传.\n",
            "  list. What the passages of the text say beyond these laws is read in the chapter on the 易传.\n" + BULLET)
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Hexagrams", ', '"Becoming.Hexagrams", "Becoming.HexagramPlaces", ')
chk = once(chk, '    "revisits within sixty-five steps, and the law with its history kept is held by no list. No "\n'
                '    "ethical premise is used. "\n',
           '    "revisits within sixty-five steps, and the law with its history kept is held by no list. No "\n'
           '    "ethical premise is used. "\n' + SCOPE)
(PKG / 'check_becoming.py').write_text(chk)

readme = (PKG / 'README.md').read_text()
lines = readme.splitlines(keepends=True)
hits = [i for i, line in enumerate(lines) if line.startswith('| L4 | [`Becoming.Hexagrams`](Becoming/Hexagrams.lean) |')]
assert len(hits) == 1, hits
lines.insert(hits[0] + 1, ROW)
(PKG / 'README.md').write_text(''.join(lines))
print('integrated into', PKG)
