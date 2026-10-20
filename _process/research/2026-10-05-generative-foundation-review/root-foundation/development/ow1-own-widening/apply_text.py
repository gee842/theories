#!/usr/bin/env python3
"""OW1's chapter text: a paragraph after section 7.2's readings (EN), a sentence in its summary (ZH), and the
correspondence in the relation-to-known-results paragraph on results outside the ten (EN, ZH).
usage: python3 -B apply_text.py   (from the checkout root; each edit must match exactly once)"""
from pathlib import Path

EN = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
ZH = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


en = EN.read_text()
assert 'widens_iff_others_within' not in en, 'already applied'
ANCHOR = ('Read capability as reach: capability that widens what a formation reaches without widening what it couples '
          'into widens the gap, and optimizing harder through the same couplings does not close it.\n')
PARA = (
    '\n**Gaining reach, and where it closes.** `Flow.Balances.widens_iff_others_within` reads §6.1\'s margin law for a '
    'part\'s own region. Where a part\'s activity widens what can form within a decided region of its own (its options) '
    'against the levels without its exchange, the whole widens exactly when its net draw stays within the margin for '
    'every formation outside that region the levels without it admit, and the two are mixed exactly when it goes beyond '
    'for one (`Flow.Balances.mixed_iff_other_beyond`); with a need met exactly, any net draw on that condition makes '
    'own widening mixed (`Flow.Balances.mixed_of_tight`), and drawing on nothing another admitted formation requires '
    'widens the whole (`Flow.Balances.widens_of_untaken_beyond`). The formal results on power-seeking show that '
    'optimal policies tend to keep options open (Turner, Smith, Shah, Critch and Tadepalli, "Optimal Policies Tend To '
    'Seek Power", NeurIPS 2021) and leave open when doing so disempowers others; the power-scarcity result for '
    'constant-sum games (Turner and Stavrianos 2021) is the case with no slack. The law answers that question for '
    'outcomes reached by thresholds on conserved amounts (any reachable set is an admitted set, `Web.admits_reachWeb_iff`, '
    'but balance has content only in that class). The levels without the part are the inaction baseline of relative '
    'reachability (Krakovna et al. 2019) and attainable utility preservation (Turner, Hadfield-Menell and Tadepalli '
    '2020); a measure that reads only the agent\'s own attainable set, in both directions, registers own widening even '
    'where it widens the whole (`Flow.Balances.widens_yet_own_changed`), and the boundary lies in the margins of the '
    'others\' needs, which that measure does not read. Mixed is not ordered: these laws say where gaining reach closes '
    'what another can form, not that it is worse. The mathematics is the margin law split over a region, and welfare '
    'economics (a Pareto improvement exists only with slack) and the Lockean proviso have the same structure '
    '([own widening](../results/records/own-widening-within-the-margin.md)).\n')
en = once(en, ANCHOR, ANCHOR + PARA)
OUT10 = ('regulation restates deadbeat control and disturbance rejection with delay (Dahleh and Pearson 1987) and '
         'requisite variety (Ashby 1956); the selection term is Price\'s (1970);')
en = once(en, OUT10, OUT10 + ' own widening within the margin (§7.2) is the margin law split over a region, answering '
          'for conserved amounts when keeping options open, in the sense of the power-seeking theorems (Turner et al. '
          '2021), closes another\'s, with constant-sum power-scarcity (Turner and Stavrianos 2021) the case with no '
          'slack and Pareto improvement from slack its analogue in welfare economics;')
EN.write_text(en)

zh = ZH.read_text()
assert 'widens_iff_others_within' not in zh, 'already applied'
Z72 = ('每条规律在它所指名的条件下成立，都不用 §6.4 的条件。\n\n**陈述。** 完整陈述见[英文版 §7.2]'
       '(THE-THEORY-OF-BECOMING.md#72-what-a-selection-cannot-reach-无明-in-alignment)。')
zh = once(zh, Z72, Z72.replace('都不用 §6.4 的条件。\n', '都不用 §6.4 的条件。另有一段把 §6.1 的余量之律读到部分自身的区域：部分的活动在其自身区域内扩大所能形成者时，'
          '整体恰在其净汲取不超出区域之外他者余量时扩大，超出时恰为混合（`Flow.Balances.widens_iff_others_within`），'
          '这回答了关于寻求权力的形式结果（Turner 等 2021）留下的问题：保留选项何时关闭他者的选项；混合不被定序。\n'))
Z10 = '调节重述无差拍控制、有延迟的扰动抑制（Dahleh and Pearson 1987）与必要多样性（Ashby 1956）；选择项是 Price（1970）的；'
zh = once(zh, Z10, Z10 + '余量之内的自身扩大（§7.2）是在区域上分开的余量之律，对守恒的量回答了寻求权力定理（Turner 等 2021）意义上的保留选项何时关闭他者的选项，'
          '常和博弈中的权力稀缺（Turner and Stavrianos 2021）是没有余量的情形，福利经济学中有余量才有帕累托改进是其类比；')
ZH.write_text(zh)
print('applied')
