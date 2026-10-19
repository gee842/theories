#!/usr/bin/env python3
"""Join E1's module to the core package: copy it in, import it after Becoming.Reading, add its root doc bullet
after Reading's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (E1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['E1_ROOT']).resolve() if os.environ.get('E1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MOD = 'ExchangePremises'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'lean' / 'Becoming' / f'{MOD}.lean', PKG / 'Becoming' / f'{MOD}.lean')

DOC = (
    '* `Becoming.ExchangePremises` (L4): which of the remaining premises a reading of the exchange\n'
    '  settles, with no premise beyond the hypotheses named. The census is a reading wherever a step\'s\n'
    '  exchange lies within finitely many relata: the relata that exchange are listed with no decision\n'
    '  procedure, every finite world has a census with its rest counted, no world read off an exchange\n'
    '  fails a census at any step, and asking it of every flow is the limited principle of omniscience;\n'
    '  enclosure is not itself read off, and a world read off a law that is never enclosed still has one.\n'
    '  Dissipation, embodiment and bounded transmission are states of the law of exchange: read off laws,\n'
    '  with the rest counted and idle and the four tying premises holding, each is met by one world and\n'
    '  failed by another; with the rest counted, embodiment is closure and no dormancy. Requirement read\n'
    '  as necessary response over a relation leaving several exchanges open gives activity needing\n'
    '  support on every run; read as possible response it does not.\n')
SCOPE = (
    '    "ExchangePremises: read off the exchange with the rest counted, the relata that exchange are "\n'
    '    "listed with no decision where a named family closes each step, every finite world has a "\n'
    '    "census, no census fails at any step, and a census of every flow over Nat at every step is LPO; "\n'
    '    "read off the spreading law no step is enclosed and a census exists; "\n'
    '    "dissipation, embodiment and bounded transmission are each met and failed by worlds read off "\n'
    '    "laws with the rest idle and the four tying premises holding; embodiment with the rest counted "\n'
    '    "is balance and each relatum exchanging exactly while it stands; over a relation of exchange, "\n'
    '    "requirement read as necessary response gives activity needing support on every run, as "\n'
    '    "possible response it does not, and for a law the two are the law\'s response. "\n')
README_ROW = (
    '| L4 | [`Becoming.ExchangePremises`](Becoming/ExchangePremises.lean) | which remaining premises a reading of the '
    'exchange settles (no premise beyond the hypotheses named): the census read off the exchange with no decision where '
    'a named family closes each step (`Flow.readOff_census_of_closed`, `World.withRest_counted`, '
    '`World.Finite.withRest_counted`), never failing at a step (`Flow.not_not_listed_at`), and at every step of every '
    'flow over `Nat` exactly LPO (`Flow.listed_iff_lpo`); enclosure not read off, a census without it '
    '(`ExchangeLaw.spreading_not_enclosed`, `ExchangeLaw.spreading_counted`); dissipation, embodiment and bounded transmission contingent '
    'on the law with the rest idle and the tying premises holding (`ExchangeLaw.contingent`); embodiment with the rest '
    'counted is closure and no dormancy (`World.withRest_embodied_iff`); requirement as necessary response over a '
    'relation of exchange gives activity needing support on every run (`ExchangeRelation.readWeb_dependent`, '
    '`ExchangeRelation.reading_glue`), possible response does not (`ExchangeRelation.free_unsupported`), and a law is '
    'the relation leaving one exchange open, its web\'s requirement read off the course the law\'s (`ExchangeLaw.relation_responds_iff`, `ExchangeLaw.relation_readWeb_requires`) |')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Reading\n', 'import Becoming.Reading\nimport Becoming.ExchangePremises\n')
root = once(root, '* `Becoming.Readings` (L4): one unfolding, read in context,',
            DOC + '* `Becoming.Readings` (L4): one unfolding, read in context,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Reading", ', '"Becoming.Reading", "Becoming.ExchangePremises", ')
chk = once(chk, '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n',
           SCOPE + '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Reading`](Becoming/Reading.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
