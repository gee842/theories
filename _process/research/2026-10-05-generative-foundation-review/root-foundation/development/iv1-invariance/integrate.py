#!/usr/bin/env python3
"""Join IV1's module Becoming.Weightings to the core package: copy it in, import it after Becoming.Boundaries,
add its root doc bullet before Relevance's, its CORE entry after Boundaries and its scope text before Boundaries'
in check_becoming.py, and its README rows (EN and ZH, before Relevance's). A leaf in L2 (its source names
`Unrestricted`): an application of Boundaries' decomposition and of Admission's comparison; nothing below
depends on it.
usage: python3 -B integrate.py   (IV1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['IV1_ROOT']).resolve() if os.environ.get('IV1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'Weightings.lean', PKG / 'Becoming' / 'Weightings.lean')

DOC = (
    '* `Becoming.Weightings` (L2): what every standpoint\'s weighting ranks, and what the step across\n'
    '  standpoints reaches. Over a finite listing, one course widens another exactly when every weighting\n'
    '  positive on every item ranks it higher; a mixed comparison is decided both ways by positive\n'
    '  weightings; a weight of zero ties a widening that adds only that item; one weight for every item\n'
    '  ranks by number; on a web with decided admission and listed admissions this is `Web.Widens`. From\n'
    '  each standpoint\'s presupposition about its own continuation and standpoint-invariance, exactly the\n'
    '  centers\' continuation is forced to have significance, the condition only where every formation is a\n'
    '  center; a standpoint\'s own presupposition forces exactly its closure; drawn along being related at\n'
    '  all the self can exceed every single relation\'s closure (`Chain`); in `Clearing` the narrower scope\n'
    '  retains where the condition loses the dweller. The readings are the AI\'s (D59).\n'
)
SCOPE = (
    '    "Weightings: over a finite listing, a course widens another exactly when every weighting positive on "\n'
    '    "every item weighs it higher; inclusion never lowers a weighted count; a course admitting an item the "\n'
    '    "other does not is weighed higher by some positive weighting, so a mixed comparison is decided both "\n'
    '    "ways; a weight of zero on what a course adds ties it with what it includes; one weight for every item "\n'
    '    "ranks by number; on a web, where admission is decided and what either level path admits is listed, "\n'
    '    "widening is what every positive weighting ranks higher, and a path not admitting what another admits "\n'
    '    "neither widens nor keeps it; from each standpoint\'s presupposition about its own continuation and "\n'
    '    "standpoint-invariance, what is forced is exactly the centers\' continuation, unrestricted exactly "\n'
    '    "where every formation is a center; a standpoint\'s own presupposition forces exactly its closure; the "\n'
    '    "presupposition along every relation of a family is significance over the union of closures, implied "\n'
    '    "by it along being related at all, which in Chain says more; in Clearing, with the clearer the only "\n'
    '    "center, the clearer\'s part retains at the centers and loses the dweller under the condition. "\n')
README_ROW = (
    '| L2 | [`Becoming.Weightings`](Becoming/Weightings.lean) | what every standpoint\'s weighting ranks, and what '
    'the step across standpoints reaches (finite listings, decided admission and natural weights supplied): on the '
    'listed items one course widens another exactly when every positive weighting ranks it higher '
    '(`Weighting.widens_iff_every_positive`; on webs `Web.widens_iff_every_weighting`); a mixed comparison is decided '
    'both ways by positive weightings (`Weighting.mixed_either_way`, `Weighting.outweighs`); a weight of zero ties a '
    'widening (`Weighting.weighed_eq_of_unweighted`); one weight for every item ranks by number '
    '(`Weighting.neutral_ranks_by_number`); closing is never required (`Web.not_widens_of_closes`); from each '
    'standpoint\'s own presupposition and standpoint-invariance exactly the centers count (`forced_iff_center`, '
    '`atCenters_least`, `unrestricted_atCenters_iff`); a standpoint\'s own presupposition forces exactly its closure '
    '(`forced_iff_within`); every relation one at a time against being related at all (`subTrue_every_iff`, '
    '`subTrue_every_of_related`, `Chain.every_not_related`); the narrower scope retains where the condition loses '
    '(`Web.retains_atCenters_iff`, `Clearing.centers_retain_yet_loses`); the readings are the AI\'s (D59) |')
README_ZH_ROW = (
    '| L2 | [`Becoming.Weightings`](Becoming/Weightings.lean) | 每个立场的加权排什么，以及跨立场的一步达到哪里'
    '（有限列举、可判定的接纳与自然数权重为所设）：在所列项上，一条进程扩大另一条，恰当每个正的加权都把它排得更高'
    '（`Weighting.widens_iff_every_positive`；在依存网上 `Web.widens_iff_every_weighting`）；混合的比较由正的加权两个方向都能决定'
    '（`Weighting.mixed_either_way`、`Weighting.outweighs`）；零权使扩大持平（`Weighting.weighed_eq_of_unweighted`）；'
    '每项同一权重即按数目排（`Weighting.neutral_ranks_by_number`）；关闭从不被要求（`Web.not_widens_of_closes`）；'
    '由各立场关于自身延续的预设与立场不变，恰是诸中心被迫有意义（`forced_iff_center`、`atCenters_least`、`unrestricted_atCenters_iff`）；'
    '一个立场自身的预设恰迫使其闭包（`forced_iff_within`）；逐一沿每个关系与沿“有所关联”之比（`subTrue_every_iff`、'
    '`subTrue_every_of_related`、`Chain.every_not_related`）；较窄的范围在条件失去处保留（`Web.retains_atCenters_iff`、'
    '`Clearing.centers_retain_yet_loses`）；读法是 AI 的（D59） |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.Weightings' not in root, 'already integrated'
root = once(root, 'import Becoming.Boundaries\n', 'import Becoming.Boundaries\nimport Becoming.Weightings\n')
root = once(root, '* `Becoming.Relevance` (L2): the uses of living significance under the continuation condition.',
            DOC + '* `Becoming.Relevance` (L2): the uses of living significance under the continuation condition.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Boundaries", "Becoming.Novelty"', '"Becoming.Boundaries", "Becoming.Weightings", "Becoming.Novelty"')
chk = once(chk, '    "Boundaries: with the formations as standpoints and each one\'s own region its closure under a "',
           SCOPE + '    "Boundaries: with the formations as standpoints and each one\'s own region its closure under a "')
(PKG / 'check_becoming.py').write_text(chk)

for name, row in (('README.md', README_ROW), ('README.zh.md', README_ZH_ROW)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('| L2 | [`Becoming.Relevance`](Becoming/Relevance.lean) |')]
    assert len(idx) == 1, (name, idx)
    lines[idx[0]:idx[0]] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
