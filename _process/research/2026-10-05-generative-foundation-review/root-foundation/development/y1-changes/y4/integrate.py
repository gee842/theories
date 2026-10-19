#!/usr/bin/env python3
"""Join Y4's module to the core package: copy Becoming/HexagramSites.lean in, import it after Becoming.HexagramPlaces,
add its root doc bullet after HexagramPlaces', its CORE entry after HexagramPlaces', its scope text after
HexagramPlaces' in check_becoming.py, and its README row after HexagramPlaces'.
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
    "* `Becoming.HexagramSites` (L4): two relations of the places read at other sites, after 王弼's\n"
    "  《周易略例》, with no premise. In the second relation of phase the bottom and top places have no\n"
    "  fixed place (初上无位): a line between them holds its place where it is in phase, and the ends\n"
    "  say nothing. No parity of the top place makes 需's and 乾's top lines both out of phase, as the\n"
    "  text says they are; under the second relation every listed statement of place in the 彖 and\n"
    "  the 小象 holds, while the parity of six places fails four. Configurations alike between the\n"
    "  ends have the same inner seams and middle opposition; changing an end line keeps every phase\n"
    "  between them. Under waxing and waning the line entering place 2 takes its phase from the\n"
    "  bottom, so the phases between the ends are not a lumping the law goes alike across. Two lines\n"
    "  answer where they differ, at any two places; a line answering every other is unique, in\n"
    "  twelve configurations, independent of place and phase, and never lasts a step of waxing and\n"
    "  waning: at the top it passes out, and two steps on a sole line stands at the bottom. Censuses\n"
    "  of the 彖, the 小象 and the line texts are checked on their configurations; every law is read\n"
    "  along runs.\n")

SCOPE = (
    "    \"HexagramSites: in the second relation of phase a line between the bottom and top places has \"\n"
    "    \"the phase of its place's parity and a line at either end has none, a line holding its place \"\n"
    "    \"where it is in phase between the ends; of two lines differing at a place every parity of the \"\n"
    "    \"place puts one in phase, so no parity of the top place leaves both listed top lines out of \"\n"
    "    \"phase; the listed statements of place hold under the second relation, and those of the whole \"\n"
    "    \"configuration hold between the ends while two of five hold at six places; the phases \"\n"
    "    \"between the ends glue exactly where all four or none are in phase; configurations alike \"\n"
    "    \"between the ends have the same inner seams and middle opposition, and changing an end line \"\n"
    "    \"keeps every phase between them and turns the opposition and alternation beside it; the \"\n"
    "    \"complement turns every phase between the ends and turning over mirrors them; under the law of \"\n"
    "    \"waxing and waning the line entering the second place takes the phase opposite its phase at \"\n"
    "    \"the bottom, so the phases between the ends are not a lumping the law goes alike across; two \"\n"
    "    \"lines answer where their values differ, at any two places; a line answering every other is \"\n"
    "    \"alone of its value, unique, in the twelve configurations one change from uniform, four \"\n"
    "    \"holding their place, four out of phase between the ends and four at the ends; no \"\n"
    "    \"configuration with such a line has one a step of waxing and waning later, it is back six \"\n"
    "    \"steps on, and at the top it passes out and stands at the bottom two steps on; every law is \"\n"
    "    \"read along the runs of the named process or of any process. No ethical premise is used. \"\n")

ROW = (
    "| L4 | [`Becoming.HexagramSites`](Becoming/HexagramSites.lean) | two relations of the places at other sites, "
    "after 王弼's 《周易略例》 (no premise): the second relation of phase, with no fixed place at the bottom and top "
    "(`fixedPhase`, `holdsPlace`); 王弼's dilemma as a law of the text's statements (`top_no_parity`); every listed "
    "statement of place of the 彖 and the 小象 holds under it, four failing at six places (`placeStatements_hold`, "
    "`tuanWhole_between`, `tuanWhole_six`); what the phases between the ends tell and the ends do not "
    "(`inner_seams_told`, `ends_not_told`); the line entering place 2 takes its phase from the bottom, so they are "
    "not a lumping (`fixedPhase_waxWane_enters`, `betweenPhases_not_goAlike`); two lines answer where they differ "
    "(`answers`); a line answered by all others is unique, in twelve configurations, independent of place and phase "
    "(`sole_unique`, `sole_iff_flip`, `sole_places`), and never lasts a step of waxing and waning, passing from the "
    "top to the bottom (`soleAny_waxWane`, `sole_top_passes`); censuses of the 彖 and the line texts "
    "(`answeredStatements_sole`, `lineTextMiddle_places`); every law read along runs (`run_sole`, "
    "`changes_run_between`, `sole_shown_along_run`) |\n")

target = PKG / 'Becoming/HexagramSites.lean'
assert not target.exists(), target

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.HexagramPlaces\n', 'import Becoming.HexagramPlaces\nimport Becoming.HexagramSites\n')
Y2_END = ("  of the law backward, and of any process. Four censuses of the 彖 and the 小象 are checked on\n"
          "  their configurations; the chapter on the 易传 reads each passage.\n")
root = once(root, Y2_END, Y2_END + BULLET)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.HexagramPlaces", ', '"Becoming.HexagramPlaces", "Becoming.HexagramSites", ')
Y2_SCOPE_END = ('    "listed statements of four censuses of the text hold of their configurations. No ethical "\n'
                '    "premise is used. "\n')
chk = once(chk, Y2_SCOPE_END, Y2_SCOPE_END + SCOPE)

readme = (PKG / 'README.md').read_text()
lines = readme.splitlines(keepends=True)
hits = [i for i, line in enumerate(lines)
        if line.startswith('| L4 | [`Becoming.HexagramPlaces`](Becoming/HexagramPlaces.lean) |')]
assert len(hits) == 1, hits
lines.insert(hits[0] + 1, ROW)
shutil.copyfile(HERE / 'Becoming/HexagramSites.lean', target)
(PKG / 'Becoming.lean').write_text(root)
(PKG / 'check_becoming.py').write_text(chk)
(PKG / 'README.md').write_text(''.join(lines))
print('integrated into', PKG)
