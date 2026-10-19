#!/usr/bin/env python3
"""Y5 (19 October 2026): carry Becoming.HexagramSequences into RO's passage map. RO's map is built from its mappers'
entries by build_passages.py, which changes an entry only where its FIXES says; this script
  1. lets a fix also add declarations and records and mark the entry's gap closed (`declarations_add`, `records_add`,
     `gap_closed`), beside the corrections it already applies;
  2. adds the fixes of the nine 易传 passages Y5 proves or sharpens (序卦 within and between pairs, 雜卦, the 彖 of
     損益, 泰否 and 既濟未濟, 繫辭下's 陽卦奇, 說卦 ch. 3 and ch. 5), each with its reason: the Lean declarations, the
     record hexagram-arrangements-and-laws, the sentences of the readings that said "computed" or "see gap" where the
     Lean now states the fact, and, for the seven with a gap, the gap marked closed by Y5;
  3. reruns build_passages.py, so passages.json is rebuilt from the entries with the fixes.
usage: python3 -B ro_fixes.py [CHECKOUT_ROOT]   (run once, on a checkout whose build_passages.py has none of these)
The readings stay the AI's (D54 and this item's decision); the mappers' entries are not changed."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
KIT = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources'
BUILD = KIT / 'build_passages.py'
H = 'Becoming.Hexagram.'
REC = ['hexagram-arrangements-and-laws']


def hx(*names):
    return [H + n for n in names]


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


FIXES = {
    'xugua-within-pairs': {
        'declarations_add': hx('bo', 'fu', 'bo_fu', 'ringRule', 'waxWane_twisted'),
        'records_add': REC,
        'reading_sub': [('翻转把律倒过来走（reverse_waxWane）。',
                         '它也是读直之环上的移位：各爻上升一位、上爻不变而入初位，一步由剥至复；消息之律上爻入初时变其刚柔，'
                         '由剥一步至坤，再一步至复（bo_fu，Y5）。翻转把律倒过来走（reverse_waxWane）。')],
        'why': 'Y5: 剝窮上反下 is also one step of the straight ring shift, where waxing and waning passes through 坤 '
               '(bo_fu)'},
    'xugua-between-pairs': {
        'declarations_add': hx('RunsOrder', 'orderNext', 'orderNext_runsOrder', 'runsOrder_agrees',
                               'runsOrder_lossless_iff', 'orderNext_one_orbit', 'runsOrder_reads',
                               'runsOrder_blind_not_lumped', 'ringRule_not_runsOrder', 'twistedRule_not_runsOrder',
                               'waxWane_not_runsOrder', 'runsOrder_not_commutes', 'rearrange_not_runsOrder',
                               'runsOrder_not_lumped'),
        'records_add': REC,
        'reading_sub': [
            ('计算核对：受传卦序不是任何三格局部规则（256 条，循环或扭转边界）的运行，最多合 9/63 步；'
             '也不是任何"置换六位并加掩码"之律（720×64 条）的运行，最好的是翻转，只合 28/63 步，恰是对内翻转的那些；'
             '对与对之间的过渡改变一到六爻不等。',
             'Y5 在 Lean 中证明：运行受传卦序之律，除未济一处外都与取每卦至其后一卦之律相同，其中恰取未济至乾者不合并，'
             '六十四卦成一轨（runsOrder_agrees、runsOrder_lossless_iff、orderNext_one_orbit）；但这样的律每一爻皆读每一爻'
             '（runsOrder_reads），所以没有三格局部规则（循环或扭转边界，消息之律在内）运行它（ringRule_not_runsOrder、'
             'twistedRule_not_runsOrder、waxWane_not_runsOrder）；它不与翻转、全变或二者交换（runsOrder_not_commutes），'
             '而一切"置换六位并加掩码"之律都与全变交换，所以也没有这样的律运行它（rearrange_not_runsOrder）。'
             '脚本另算部分相合：三格局部规则最多合 9/63 步；置换加掩码之律最好的是翻转，合 28/63 步，恰是对内翻转的那些；'
             '对与对之间的过渡改变一到六爻不等。'),
            ('这回答 Yi 章 §8 的开放问题：卦序在对间是断言而非导出，只有对内是律。',
             '这回答 Yi 章 §8 的开放问题，并改正那里“卦序本身不是任何律的轨道”之说：卦序是一张表之律的运行，'
             '不是只读部分构形或保持对称之律的运行；在对间是断言而非导出，只有对内是律。')],
        'gap_closed': ('Y5 (Becoming.HexagramSequences), in a stronger form: (a) and (b) as runsOrder_reads, '
                       'ringRule_not_runsOrder, twistedRule_not_runsOrder, runsOrder_not_commutes and '
                       'rearrange_not_runsOrder, with the laws running the order characterized (runsOrder_agrees, '
                       'runsOrder_lossless_iff, orderNext_one_orbit); the best partial agreements (9 and 28 of 63) '
                       'and (c) stay script computations.'),
        'why': 'Y5 proved in Lean what the reading computed, in a stronger form, and corrected the 易传 chapter\'s '
               'claim that the order is the orbit of no law'},
    'zagua-pairs': {
        'declarations_add': hx('zagua', 'zagua_every', 'partner', 'paired_iff_partner', 'partner_partner',
                               'partner_run', 'order_partners', 'zagua_partners', 'zagua_last_eight',
                               'zagua_not_commutes'),
        'records_add': REC,
        'reading_sub': [
            ('AI读法：计算核对：杂卦六十四名恰是受传卦序的同样三十二对；',
             'AI读法：Y5 在 Lean 中写成（zagua_every、order_partners、zagua_partners、zagua_last_eight，'
             '其序由易传章的检查脚本与所存杂卦核对）：杂卦六十四名恰是受传卦序的同样三十二对；'),
            ('它保留对，丢掉对与对之间的次序，与 xugua-between-pairs（对间次序是断言）相合。',
             '它保留对，丢掉对与对之间的次序，与 xugua-between-pairs（对间次序是断言）相合；'
             '运行杂卦之序的律也不与翻转、全变或二者交换（zagua_not_commutes）。'),
            ('Y1 未存杂卦原文。', 'Y1 未存杂卦原文，Y5 以本图谱所存之文核对。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): zagua_every, zagua_partners and zagua_last_eight.',
        'why': 'Y5 proved in Lean what the reading computed'},
    'tuan-sun-yi': {
        'declarations_add': hx('swap', 'yang_swap', 'across', 'passing', 'across_exchange', 'named_exchanges',
                               'exchangesRun', 'exchangeWorld_balances', 'exchangeWorld_rise_fall', 'three_iff',
                               'exchanges_from_tai_pi'),
        'records_add': REC,
        'reading_sub': [
            ('AI读法：计算核对：损即泰交换第三、六爻', 'AI读法：Y5 在 Lean 中写成（named_exchanges、yang_swap）：损即泰交换第三、六爻'),
            ('卦变（交换两爻）脊柱无，见 gap。',
             '卦变（交换两爻）已由 Y5 写成：下卦与上卦之间的相易是两卦之间交换之律的一步（across_exchange），'
             '一切相易之历程读为世界皆平衡（exchangeWorld_balances）；三阳三阴之卦二十，恰是泰、否与由之一易所得之十八卦，'
             '自泰否起的相易不出其外（three_iff、exchanges_from_tai_pi）。')],
        'gap_closed': ('Y5 (Becoming.HexagramSequences): yang_swap, across_exchange, named_exchanges, '
                       'exchangeWorld_balances, three_iff.'),
        'why': 'Y5 proved in Lean what the reading computed and what its gap named'},
    'xici-yanggua-qi': {
        'declarations_add': hx('yangOdd', 'yangOdd_lumped', 'yangOdd_goAlike', 'yangOdd_goAlike_changes',
                               'phaseCount_yangOdd', 'count3', 'strokes3', 'odd3_iff', 'trigramOdd_flip',
                               'changes_run_trigram'),
        'records_add': REC,
        'reading_sub': [
            ('AI读法：计算核对：震坎艮各一阳二阴', 'AI读法：Y5 在 Lean 中写成（odd3_iff）：震坎艮各一阳二阴'),
            ('所以奇偶两类是律通行的归并（理）。',
             '所以奇偶两类是律通行的归并（理）；Y5 以阳爻数直接写出（yangOdd_goAlike、yangOdd_goAlike_changes、'
             'phaseCount_yangOdd）。'),
            ('三爻层面的陈述与阳爻数的陈述脊柱尚无，见 gap。',
             '三爻层面的陈述由 Y5 写成：一爻之变使其所在之卦由阳卦为阴卦或反之，另一卦不变（changes_run_trigram）。')],
        'gap_closed': ('Y5 (Becoming.HexagramSequences): odd3_iff, yangOdd_goAlike, yangOdd_goAlike_changes, '
                       'changes_run_trigram.'),
        'why': 'Y5 proved in Lean what the reading computed and what its gap named'},
    'shuogua-tiandi-dingwei': {
        'declarations_add': hx('Trigram.complement3', 'Trigram.opposite_stations'),
        'records_add': REC,
        'reading_sub': [('AI读法：计算核对：四对恰是三爻层面的四对互补',
                         'AI读法：Y5 在 Lean 中写成（Trigram.opposite_stations）：四对恰是三爻层面的四对互补')],
        'why': 'Y5 proved in Lean what the reading computed'},
    'shuogua-di-chu-zhen': {
        'declarations_add': hx('Trigram.stations', 'Trigram.stations_not_commutes', 'Trigram.ringRule3_rotate',
                               'Trigram.stations_not_rules', 'Trigram.rearrange3_complement',
                               'Trigram.rearrange3_not_stations', 'Trigram.opposite_stations'),
        'records_add': REC,
        'reading_sub': [
            ('计算核对，震→巽→离→坤→兑→乾→坎→艮→震不是任何"置换各爻并加掩码"之律的运行（最多合 4/8 步），'
             '也不是任何三格局部规则（循环或扭转）的运行（最多 5/8）；圆上四对对位中只有离坎互补，而第三章的四对全是互补。',
             'Y5 在 Lean 中证明：运行震→巽→离→坤→兑→乾→坎→艮之律不与互补、翻转、二者或三爻之轮转交换'
             '（Trigram.stations_not_commutes），所以没有三格局部规则（循环或扭转）、也没有"置换各爻并加掩码"之律运行它'
             '（Trigram.stations_not_rules、Trigram.rearrange3_not_stations）；圆上四对对位中只有离坎互补，'
             '而第三章的四对全是互补（Trigram.opposite_stations）。脚本另算部分相合：置换加掩码之律最多合 4/8 步，'
             '三格局部规则最多 5/8。')],
        'gap_closed': ('Y5 (Becoming.HexagramSequences): Trigram.stations_not_commutes, Trigram.stations_not_rules, '
                       'Trigram.rearrange3_not_stations, Trigram.opposite_stations; the best partial agreements stay '
                       'script computations.'),
        'why': 'Y5 proved in Lean what the reading computed'},
    'tuan-tai-pi-jiao': {
        'declarations_add': hx('meets', 'meets_tai_pi', 'pi_of_tai', 'kept_alike', 'tai_pi_runs'),
        'records_add': REC,
        'reading_sub': [
            ('但"交/不交"不能从脊柱现有的位之关系读出：泰与否在每个高度都"对"（oppositions_glue_iff），'
             '二者在"对"之下完全相同。区别它们要把一个方向读入两值（天升地降，故天在下则交），这是额外前提，见 gap，交给 Y2–Y4。',
             '但"交/不交"不能从为全变所保持的位之关系读出：泰与否在每个高度都"对"（oppositions_glue_iff），'
             '否是泰之全变，凡全变所保持之读法沿二者的消息历程每一步都相同（kept_alike、tai_pi_runs）。'
             '区别它们要把一个方向读入两值（天升地降，故天在下则交）：Y5 写作交（meets），泰三个高度皆交、否皆不交'
             '（meets_tai_pi）；这是一个读法，全变不保持它。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): meets, meets_tai_pi, kept_alike, tai_pi_runs.',
        'why': 'Y5 stated the direction the reading named as a gap'},
    'tuan-jiji-weiji': {
        'declarations_add': hx('waxWane_moves', 'run_never_rests', 'never_comes_to_rest', 'changes_run_never_rests'),
        'records_add': REC,
        'reading_sub': [('消息之律无不动点，脊柱没有单独命名的引理，见 gap。',
                         '消息之律无不动点，由 Y5 写成：没有构形为其不动点（waxWane_moves），其运行在任何一步都不止，'
                         '也不自某步起止（run_never_rests、never_comes_to_rest），一爻之变的历程亦然（changes_run_never_rests）。')],
        'gap_closed': ('Y5 (Becoming.HexagramSequences): waxWane_moves, run_never_rests, never_comes_to_rest, '
                       'changes_run_never_rests.'),
        'why': 'Y5 stated the lemma the reading named as a gap'},
}

text = BUILD.read_text()
assert 'declarations_add' not in text
text = once(text, 'or a sentence of a reading replaced after review).',
            'or a sentence of a reading replaced after review, or, where a later item\n'
            'proved what an entry computed or its gap named, declarations and records added and the gap marked closed).')
text = once(text, "                'declarations': e.get('declarations', []),\n                'records': e.get('records', []),\n",
            "                'declarations': e.get('declarations', []) + fix.get('declarations_add', []),\n"
            "                'records': e.get('records', []) + fix.get('records_add', []),\n")
text = once(text, "            for old, new in fix.get('reading_sub', []):\n",
            "            if fix.get('gap_closed') and 'gap' in p:\n"
            "                p['gap'] = dict(p['gap'], closed=fix['gap_closed'])\n"
            "            for old, new in fix.get('reading_sub', []):\n")


def literal(value, indent):
    """A Python literal of a fix's value, wrapped at 120 columns."""
    pad = ' ' * indent
    if isinstance(value, str):
        def word(c):
            return c.isascii() and (c.isalnum() or c == '_')
        out, line = [], ''
        for ch in value:
            if len(repr(line + ch)) > 120 - indent:
                cut = len(line)
                if word(ch):
                    while cut > 0 and word(line[cut - 1]):
                        cut -= 1
                    cut = cut or len(line)
                out.append(repr(line[:cut]))
                line = line[cut:]
            line += ch
        out.append(repr(line))
        return ('\n' + pad).join(out) if len(out) > 1 else out[0]
    if isinstance(value, list) and all(isinstance(x, str) for x in value):
        return '[' + (',\n' + pad + ' ').join(repr(x) for x in value) + ']'
    if isinstance(value, list):
        return '[' + (',\n' + pad + ' ').join(
            '(' + literal(a, indent + 2) + ',\n' + pad + '  ' + literal(b, indent + 2) + ')' for a, b in value) + ']'
    raise TypeError(value)


blocks = []
for key, fix in FIXES.items():
    lines = [f"    {key!r}: {{"]
    for k, v in fix.items():
        lines.append(f"        {k!r}: {literal(v, 8 + len(repr(k)) + 2)},")
    lines[-1] = lines[-1][:-1] + '},'
    blocks.append('\n'.join(lines))
END = "        'why': 'review: \"the theory supports chapter 39\" stated as which laws agree with which chapter'},\n}\n"
text = once(text, END, END[:-2] + '\n'.join(blocks) + '\n}\n')
compile(text, str(BUILD), 'exec')
BUILD.write_text(text)
run = subprocess.run([sys.executable, '-B', str(BUILD)], capture_output=True, text=True)
print(run.stdout, run.stderr)
assert run.returncode == 0 and 'PROBLEM' not in run.stdout
