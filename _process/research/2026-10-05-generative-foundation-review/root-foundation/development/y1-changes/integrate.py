#!/usr/bin/env python3
"""Join Y1's module to the core package: copy Becoming/Hexagrams.lean in, import it after Becoming.Learning, add its
root doc bullet after Learning's, its CORE entry after Learning's, its scope text before Description's in
check_becoming.py, and its README row after Learning's. usage: python3 -B integrate.py [PACKAGE_ROOT]
(PACKAGE_ROOT defaults to the checkout holding this file; each edit must match exactly once)."""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


BULLET = (
    "* `Becoming.Hexagrams` (L4): the configurations of the 周易 as a world of the spine, with no\n"
    "  premise. Six lines, each unbroken or broken, give sixty-four configurations, told apart and\n"
    "  listed with no axiom; the received order holds every one, and each of its pairs is turned over\n"
    "  or, where turning over gives the same hexagram, changed in every line. The change of one line\n"
    "  is a process under which every configuration returns and every configuration can be had from\n"
    "  every other, and it merges. The law of waxing and waning, every line rising one place and the\n"
    "  top line entering at the bottom as its opposite, merges nothing, so every configuration\n"
    "  returns (`Law.lossless_iff_returns`); six steps change every line, the first unbroken line\n"
    "  comes back at the seventh step from all unbroken, and all broken returns first at the\n"
    "  twelfth. Where only a broken line enters, the law merges and every other configuration is\n"
    "  drawn into all broken and never comes back. For every law of hexagrams every configuration\n"
    "  returns exactly where the law merges nothing. The pairs of complements are a lumping the law\n"
    "  goes alike across, the count of unbroken lines is not; turning over runs the law backward.\n"
    "  Read as claims, a frame and a world, the lines arise and cease at arbitrarily late steps\n"
    "  (`Frame.claims_recur_iff`); any sixty-five steps revisit, and the kept history is held by no\n"
    "  list. What the passages of the text say beyond these laws is read in the chapter on the 易传.\n")

SCOPE = (
    "    \"Hexagrams: six two-valued lines give sixty-four configurations, equality and membership told \"\n"
    "    \"line by line, and the received order holds every one, each of its pairs turned over or, \"\n"
    "    \"where turning over gives the same hexagram, changed in every line; the change of one line \"\n"
    "    \"returns every configuration, reaches every configuration from every other, keeps every \"\n"
    "    \"possibility and merges; the law of waxing and waning merges nothing, so by \"\n"
    "    \"lossless_iff_returns every configuration returns, six steps on every line is changed, twelve \"\n"
    "    \"steps on the configuration is had again, all broken first returns at the twelfth step and \"\n"
    "    \"the first unbroken line at the seventh step from all unbroken; where only a broken line \"\n"
    "    \"enters the law merges, all broken is absorbing, every other configuration is drawn in, never \"\n"
    "    \"comes back, never returns and a possibility is lost; for every law of hexagrams every \"\n"
    "    \"configuration returns exactly where the law merges nothing; the law commutes with the \"\n"
    "    \"complement, turning over runs it backward, it goes alike across the pairs of complements \"\n"
    "    \"and not across the count of unbroken lines; read along the law as a frame and a world the \"\n"
    "    \"lines arise and cease at arbitrarily late steps; every run of hexagrams under every process \"\n"
    "    \"revisits within sixty-five steps, and the law with its history kept is held by no list. No \"\n"
    "    \"ethical premise is used. \"\n")

ROW = (
    "| L4 | [`Becoming.Hexagrams`](Becoming/Hexagrams.lean) | the configurations of the 周易 as a world of the "
    "spine (no premise): six two-valued lines, told apart and listed with no axiom, the received order holding "
    "every one and paired by turning over or changing every line (`mem_order`, `order_paired`); the change of one "
    "line returns every configuration, reaches every other and merges (`changes_returns`, `reach_every`, "
    "`changes_merges`); the law of waxing and waning merges nothing, so every configuration returns by "
    "`Law.lossless_iff_returns` (`waxWane_lossless`, `waxWane_returns`), six steps change every line, the first "
    "unbroken line comes back at the seventh step and all broken first returns at the twelfth (`six_steps`, "
    "`seventh_step`, `first_return`); where only a broken line enters, every other configuration is drawn into "
    "all broken and never returns (`wane_drawn`, `wane_not_returns`); for every law of hexagrams every "
    "configuration returns exactly where the law merges nothing (`every_returns_iff`); the pairs of complements "
    "are a lumping the law goes alike across and the count of unbroken lines is not (`pairs_goAlike`, "
    "`yang_not_goAlike`); the lines as claims arise and cease at arbitrarily late steps (`arising_recurs`, "
    "`ceasing_recurs`); every run revisits within sixty-five steps (`revisits_within_order`) |\n")

target = PKG / 'Becoming/Hexagrams.lean'
assert not target.exists(), target
shutil.copyfile(HERE / 'Becoming/Hexagrams.lean', target)

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Learning\n', 'import Becoming.Learning\nimport Becoming.Hexagrams\n')
root = once(root, "  Ren on 16 October 2026.\n* `Becoming.Contacts` (L4)",
            "  Ren on 16 October 2026.\n" + BULLET + "* `Becoming.Contacts` (L4)")
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Learning", "Becoming.Revision",', '"Becoming.Learning", "Becoming.Hexagrams", "Becoming.Revision",')
chk = once(chk, '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n',
           SCOPE + '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n')
(PKG / 'check_becoming.py').write_text(chk)

readme = (PKG / 'README.md').read_text()
lines = readme.splitlines(keepends=True)
hits = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Learning`](Becoming/Learning.lean) |')]
assert len(hits) == 1, hits
lines.insert(hits[0] + 1, ROW)
(PKG / 'README.md').write_text(''.join(lines))
print('integrated into', PKG)
