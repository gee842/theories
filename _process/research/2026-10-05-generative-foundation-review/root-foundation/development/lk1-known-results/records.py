"""LK1: prior-art boundaries for the README featured records and the alignment and Runaway records.

Run from the checkout root. Adds one does_not_show item (schema 2) or rewrites one limitations
clause within the growth ratchet (schema 1), a history note, a reference to the significance
review, and refreshes reviewed_at_utc. Idempotent: an item already present is not added twice.
"""
import hashlib, json, pathlib

ROOT = pathlib.Path('.')
REC = ROOT / 'theories/becoming/results/records'
SA1 = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md'
NOW = '2026-10-20T07:47:06+00:00'
SA1_SHA = hashlib.sha256((ROOT / SA1).read_bytes()).hexdigest()


def item(en, zh, kind='correspondence'):
    return {'zh': zh, 'en': en, 'kind': kind}


SCHEMA2 = {
    'own-count-misses-joint-excess': [item(
        'Restates the tragedy of the commons and overshoot (Lloyd 1833, Hardin 1968, Meadows and others 1972); the laws are near-definitional arithmetic over natural numbers.',
        '重述公地悲剧与过冲（Lloyd 1833；Hardin 1968；Meadows 等 1972）；规律是自然数上近乎定义的算术。')],
    'consumption-ends-with-feeders': [item(
        'Near-definitional: the level falls at each active step, so it bounds the run as a ranking function does; a consumer overshooting what feeds it is known (Catton 1980).',
        '近乎定义：水平在每个活跃步下降，所以像排序函数一样界定运行；消耗者超出其供给者是已知的（Catton 1980）。')],
    'feeding-closure': [item(
        'Standard: the closure is the least region closed under feeding, a transitive closure (a least fixed point), and its existence and constructive reach are known.',
        '标准的：闭包是对供给封闭的最小区域，即传递闭包（最小不动点），其存在与构造性可达是已知的。')],
    'derived-extent-limits': [item(
        'Near-definitional: the limits are shown by constructed webs, and a requirement derived from wanting one\'s own continuation is a hypothetical imperative (Kant 1785).',
        '近乎定义：界限由构造的网显示，由想要自身延续推出的要求是假言命令（Kant 1785）。')],
    'selection-through-couplings': [item(
        'Known as the proxy problem (Goodhart 1975, Amodei and others 2016, Manheim and Garrabrant 2018); Zhuang and Hadfield-Menell (NeurIPS 2020) prove a stronger, quantitative form.',
        '即代理问题（Goodhart 1975；Amodei 等 2016；Manheim、Garrabrant 2018）；Zhuang、Hadfield-Menell（2020）证明了更强的定量形式。')],
    'runaway-distance-uncoupled': [
        item('Near-definitional: the raised world is alike through the couplings because the stock is not among what couples in by level.',
             '近乎定义：抬高的世界经耦合无别，因为存量不在经水平耦合入者之中。', 'scope'),
        item('Holds because the stock is unobserved by hypothesis; where it is observed, a break can often be seen coming, as early-warning signals of critical transitions show (Scheffer et al., Nature 2009).',
             '成立是因为按假设存量不被观察；存量被观察之处，断裂常可预先看到，如临界转变的早期预警信号所示（Scheffer et al., Nature 2009）。')],
    'experiment-needs-return': [item(
        'Restates the fundamental problem of causal inference (Holland 1986): a record shows one side of the with-and-without comparison; the kept history is Bennett\'s (1973).',
        '重述因果推断的基本问题（Holland 1986）：记录只显示有与无之比较的一侧；保存的历史即 Bennett 的（1973）。')],
    'closing-needs-net-draw': [item(
        'Near-definitional: the margin law is the balance equation substituted into the admission inequality, and comparing admitted sets by inclusion is the opportunity-set ordering (Pattanaik and Xu 1990).',
        '近乎定义：余量规律是把平衡方程代入接纳不等式，以包含比较被接纳的集是机会集的排序（Pattanaik and Xu 1990）。')],
    'alignment-direction-under-widening': [item(
        'No result on alignment beyond the known proxy problem: the selection laws state it qualitatively, and Zhuang and Hadfield-Menell (NeurIPS 2020) prove a stronger theorem.',
        '代理问题之外没有关于对齐的结果：选择的规律定性地陈述它，Zhuang and Hadfield-Menell（NeurIPS 2020）证明了更强的定理。')],
}

SCHEMA1 = {
    'seeking-boundary': [
        ('the counting of B1 is elementary, and the substance is in stating it of targets within the unfolding',
         'B1 is elementary (a strict maximum holds of one; rest under run-down is ranking-function termination)', 'en'),
        ('B1 的计数是初等的，实质在于把它们陈述为展开之中的目标',
         'B1 是初等的（严格最大者至多一个；衰减下的停息是排序函数的终止）', 'zh')],
    'target-capture': [
        ('the share theorems are the counting for a two-valued target',
         'the share theorems are Price\'s selection differential (1970) for a two-valued target', 'en'),
        ('份额定理是二值目标的计数', '份额定理是二值目标的 Price 选择差（1970）', 'zh')],
    'separation-loses-the-relation': [
        ('Relation is stated for wholes of two parts, with parity as the witness for three',
         'Relation is stated for wholes of two parts (rectangularity is the standard product criterion), parity witnessing three', 'en'),
        ('关系只对两个部分的整体陈述，三个部分以奇偶为见证', '关系只对两个部分的整体陈述（矩形即乘积的标准判据），三个部分以奇偶为见证', 'zh')],
    'whole-persists-through-generation': [
        ('the witnesses are minimal.', 'the proof is a pigeonhole, near-definitional; witnesses minimal.', 'en'),
        ('见证都是最小见证。', '证明是鸽巢原理，近乎定义；见证都是最小见证。', 'zh')],
}

NOTE = {
    'en': '20 October 2026, LK1 (study section 237): the closest prior result named against the significance review\'s verdicts (study SA1), so that the record is not led with as a new finding; {what}. The claim and its premises are unchanged.',
    'zh': '2026年10月20日，LK1（研究第237节）：按意义审查（研究 SA1）的裁定指名最接近的先前结果，使本记录不被当作新发现来领头；{what}。主张与其前提不变。',
}
WHAT = {
    'schema2': ('one does_not_show item added', '增加一条 does_not_show'),
    'schema1': ('one limitations clause rewritten within the growth ratchet', '在增长限制之内改写 limitations 的一句'),
}
EXTRA = {
    'runaway-distance-uncoupled': ('the statement now carries the hypothesis that the stock couples in by threshold only, and two does_not_show items are added (near-definitional; early-warning signals where the stock is observed)',
                                   '陈述现在带上存量只经阈耦合入的假设，并增加两条 does_not_show（近乎定义；存量被观察处的早期预警信号）'),
    'alignment-direction-under-widening': ('one does_not_show item added, and the correspondence names the proxy-problem literature with what the laws add (the responsive closure, the pool) and what they do not',
                                           '增加一条 does_not_show，对应中指名代理问题的文献，以及规律加了什么（回应的闭包、池）与没有加什么'),
    'experiment-needs-return': ('one does_not_show item added (this record is not in SA1\'s table; the match is LK1\'s judgment)',
                                '增加一条 does_not_show（本记录不在 SA1 的表中；这一对应是 LK1 的判断）'),
    'separation-loses-the-relation': ('one limitations clause rewritten within the growth ratchet (this record is not in SA1\'s table; the match is LK1\'s judgment)',
                                      '在增长限制之内改写 limitations 的一句（本记录不在 SA1 的表中；这一对应是 LK1 的判断）'),
}

RUNAWAY_STATEMENT = {
    'en': 'Every policy through the couplings, with the rest of the exchange fixed, that keeps its support leaves unused any larger stock coupled into it by threshold only; for such a stock, how far off the break is does not couple in before the break.',
    'zh': '每个经耦合、其余交换固定的策略保持支持就永不动用只经阈耦合入它的较多储量；对这样的储量，断裂之前，断裂还有多远不耦合入。',
}
ALIGN_CORR = {
    'en': ' Its selection part restates the proxy problem: Goodhart (1975); Amodei et al., "Concrete Problems in AI Safety" (2016); Manheim and Garrabrant, "Categorizing Variants of Goodhart\'s Law" (2018); and Zhuang and Hadfield-Menell, "Consequences of Misaligned AI" (NeurIPS 2020), who prove that optimizing a proxy omitting attributes of a utility can, under resource constraints, drive the utility arbitrarily low. The laws add the responsive closure (the rest following a law reading through coupling, the closure drawn over time) and the pool (selection through the union of its members\' couplings); they give no bound on that degradation and say nothing of which law training installs.',
    'zh': '其选择部分重述代理问题：Goodhart（1975）；Amodei et al.（2016）；Manheim and Garrabrant（2018）；Zhuang and Hadfield-Menell（NeurIPS 2020）证明，在资源约束下优化省略效用某些属性的代理可使效用任意低。规律加了回应的闭包（其余者遵循经耦合读取的律，闭包跨时间画出）与池（经成员耦合之并的选择）；它们不给出那种降低的界，也不说训练装入哪个律。',
}


def load(i):
    p = REC / f'{i}.json'
    return p, json.loads(p.read_text())


def save(p, r):
    p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


def finish(r, i, kind):
    what = EXTRA.get(i, WHAT[kind])
    note = {'en': NOTE['en'].format(what=what[0]), 'zh': NOTE['zh'].format(what=what[1])}
    if note not in r['history']:
        r['history'].append(note)
    if not any(x['path'] == SA1 for x in r['references']):
        r['references'].append({'path': SA1, 'role': 'review', 'sha256': SA1_SHA, 'declarations': []})
    r['reviewed_at_utc'] = NOW


for i, items in SCHEMA2.items():
    p, r = load(i)
    assert r.get('schema_version') == 2, i
    for it in items:
        if not any(d.get('en') == it['en'] for d in r['does_not_show']):
            r['does_not_show'].append(it)
    assert len(r['does_not_show']) <= 8, (i, len(r['does_not_show']))
    if i == 'runaway-distance-uncoupled':
        r['statement'].update(RUNAWAY_STATEMENT)
    if i == 'alignment-direction-under-widening':
        for lang in ('en', 'zh'):
            if ALIGN_CORR[lang].strip() not in r['correspondence'][lang]:
                r['correspondence'][lang] += ALIGN_CORR[lang] if lang == 'en' else ALIGN_CORR[lang]
    finish(r, i, 'schema2')
    save(p, r)

for i, reps in SCHEMA1.items():
    p, r = load(i)
    for old, new, lang in reps:
        text = r['limitations'][lang]
        if new not in text:
            assert text.count(old) == 1, (i, old)
            r['limitations'][lang] = text.replace(old, new)
    finish(r, i, 'schema1')
    save(p, r)
print('ok')
