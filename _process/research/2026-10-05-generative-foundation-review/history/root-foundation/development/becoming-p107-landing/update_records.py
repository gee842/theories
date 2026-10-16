#!/usr/bin/env python3
"""P107: substantive updates to four existing records (run with the checkout root as argument).

usage: update_records.py ROOT
Each change asserts the text it replaces, so a concurrent edit stops the script instead of being
overwritten. One paired history note per record; the landing's reconciliation of hashed documents
extends that note rather than adding a second one (bind_p107.py).
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
NOTE = {'zh': '2026-10-14 P107（从关系开始的重建，研究 §124）：', 'en': '14 October 2026, P107 (the relation-first re-founding, study section 124): '}


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def save(r):
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def note(r, zh, en):
    r['history'].append({'zh': NOTE['zh'] + zh, 'en': NOTE['en'] + en})


def imbalance():
    r = load('imbalance-as-relatum')
    # Schema 1: limitations and correspondence may grow by at most 40 en / 20 zh characters, so the
    # sentences the adoption made untrue are replaced in place; the adoption's form is stated in
    # premises-read-off-the-exchange and linked from related.
    replace(r['correspondence'],
            {'zh': '（零前提计划 §1.4 的重新奠定）。AI 的读法：算入不平衡后，平衡是表示的性质，它对世界所说的改由一个关系项的不活跃来说；'
                   '哪种读法更好由 Ren 定。',
             'en': "(the re-founding of the zero-premise plan, section 1.4). The AI's reading: with the imbalance counted, balance "
                   "is a property of the representation, and what it said of a world is said instead by the inactivity of one "
                   "relatum; which reading is better is Ren's."},
            {'zh': '（零前提计划 §1.4 的重新奠定）；Ren 2026-10-14 采用。AI 的读法：算入不平衡后，平衡是表示的性质，它对世界所说的改由'
                   '一个关系项的不活跃来说。',
             'en': "(the re-founding of the zero-premise plan, section 1.4); Ren adopted it on 14 October 2026. The AI's reading: "
                   "with the imbalance counted, balance is a property of the representation, and what it said of a world is said "
                   "instead by the inactivity of one relatum."})
    replace(r['limitations'],
            {'zh': '这是表示之间的等价，不是采用：', 'en': 'This is an equivalence of representations, not an adoption:'},
            {'zh': '这是表示之间的等价，使采用无损：', 'en': 'This is an equivalence of representations, which makes the adoption lossless:'})
    replace(r['counterexamples'][0]['detail'],
            {'zh': '等价不是采用；核心仍以平衡为局部条件。',
             'en': 'The equivalence is not an adoption; the core keeps balance as a local condition.'},
            {'zh': '采用之后，这一条件仍是部分的状态：其余是否闲置（World.withRest_closed_iff）。',
             'en': 'Adopted, the condition stays a state of a part: whether the rest is idle (World.withRest_closed_iff).'})
    old = {'zh': 'Ren 决定是否采用；采用时核心的规律以新增关系项的闲置陈述平衡。',
           'en': "Ren's decision whether to adopt it; adopted, the core's laws would state balance as the added relatum idle."}
    assert r['next_delta'] == old, r['next_delta']
    r['next_delta'] = {
        'zh': '核心现有的规律在 Flow.BalancesOn 上的陈述是否改写为其余在该家族上闲置（每条经 Flow.balancesOn_iff_idle 等价）；'
              '实际生成中其余是什么（它的交换作为差读出，不是观察）；独立审查。',
        'en': 'Whether the existing laws stated on Flow.BalancesOn are rewritten as the rest idle on the family (each is '
              'equivalent through Flow.balancesOn_iff_idle); what the rest is in an actual becoming (its exchange is read off '
              'as a difference, not observed); an independent review.'}
    r['related'] += [
        {'id': 'premises-read-off-the-exchange',
         'detail': {'zh': '采用之后：每个世界算入其余都平衡，平衡恰是其余从不活跃（World.withRest_balanced、World.withRest_closed_iff）；'
                          '核心现有的规律保留 Flow.BalancesOn 的陈述，经 Flow.balancesOn_iff_idle 读作其余闲置。',
                    'en': 'After the adoption: every world with its rest counted balances, and balance is exactly the rest never '
                          'active (World.withRest_balanced, World.withRest_closed_iff); the existing laws keep their statements on '
                          'Flow.BalancesOn, read through Flow.balancesOn_iff_idle as the rest idle.'}},
        {'id': 'unity-of-readings',
         'detail': {'zh': '其余的交换是所立与交换两种变化读法之差；算入它，两种读法处处粘合（Flow.changeReadings_glue_counting_rest）。',
                    'en': 'The rest\'s exchange is the difference between the standing\'s and the exchange\'s readings of change; '
                          'counted, the two glue at every step (Flow.changeReadings_glue_counting_rest).'}}]
    note(r, '记录 Ren 2026-10-14 的采用（“please, finish all”，批准从关系开始的重建）：对应中“哪种读法更好由 Ren 定”改为采用；限制中'
            '“这是表示之间的等价，不是采用”改为“使采用无损”；反例说明末句“等价不是采用；核心仍以平衡为局部条件”改为采用后的读法；下一步原为'
            '“Ren 决定是否采用；采用时核心的规律以新增关系项的闲置陈述平衡”，改为陈述的改写、其余是什么与独立审查；采用的形式（Becoming.Reading '
            '的 World.withRest，Becoming.Novelty 的 Flow.bounded_counting_rest）在 premises-read-off-the-exchange 中陈述，related 加它与 '
            'unity-of-readings。陈述与证明不变。',
            'records Ren\'s adoption of 14 October 2026 (“please, finish all”, approving the relation-first re-founding): in the '
            'correspondence “which reading is better is Ren\'s” becomes the adoption; in the limitations “This is an equivalence of '
            'representations, not an adoption” becomes “which makes the adoption lossless”; the counterexample\'s last sentence '
            '“The equivalence is not an adoption; the core keeps balance as a local condition” becomes the reading after adoption; '
            'the next step, formerly “Ren\'s decision whether to adopt it; adopted, the core\'s laws would state balance as the '
            'added relatum idle”, becomes the rewriting of statements, what the rest is and an independent review; the adoption\'s '
            'form (World.withRest in Becoming.Reading, Flow.bounded_counting_rest in Becoming.Novelty) is stated in '
            'premises-read-off-the-exchange, which related adds with unity-of-readings. Statement and proofs unchanged.')
    save(r)


def premises_map():
    r = load('map-of-premises')
    r['does_not_show'].append({
        'zh': '独立性在 World 分别选取的八个字段之间，是表示的自由，不是生成的偶然；从交换读出、算入其余时，其中四个由读法成立'
              '（premises-read-off-the-exchange）。',
        'en': 'The independence is among World\'s eight separately chosen fields, the freedom of the representation, not '
              'contingency in becoming; read off the exchange with the rest counted, four of them hold by reading '
              '(premises-read-off-the-exchange).',
        'kind': 'scope'})
    r['related'].append({
        'id': 'premises-read-off-the-exchange',
        'detail': {'zh': '读出时四个前提（平衡、只有活跃者给予、只有活跃者取用其所汲取的、对交换之律的活动需要支持）由读法成立；它们在这里的'
                         '独立性见证（World.unbalanced_but、strained_but、scatter_but、morsel_but）都把一个读法选得与它所读的交换不符。',
                   'en': 'Read off, four premises (balance, only active relata giving, only active relata taking what they draw on, '
                         'and activity needing support under a law of exchange) hold by reading; their independence witnesses here '
                         '(World.unbalanced_but, strained_but, scatter_but, morsel_but) each choose a reading apart from the '
                         'exchange it reads.'}})
    note(r, '不显示的一项补上：独立性度量 World 分别选取的字段的自由，不度量生成的偶然；读出时四个前提由读法成立。起因是 Ren 问'
            '“why do we need "World"?”与那天对前一个回答（以独立性为规律不必然的证据）的更正。related 加 premises-read-off-the-exchange。'
            '陈述、规律与证明不变。',
            'a does-not-show item added: the independence measures the freedom of World\'s separately chosen fields, not '
            'contingency in becoming, and read off the exchange four premises hold by reading. Prompted by Ren\'s question “why do '
            'we need "World"?” and that day\'s correction of an earlier answer that had used the independence as evidence that the '
            'laws are not necessary. related adds premises-read-off-the-exchange. Statement, laws and proofs unchanged.')
    save(r)


def process_frame():
    r = load('process-and-frame-as-readings')
    replace(r['next_delta'],
            {'zh': '；Ren 的判断：起点是否读作 World，过程与框架是否读作它的读法。',
             'en': "; Ren's judgment whether the starting point reads as World, with the process and the frame as its readings."},
            {'zh': '。', 'en': '.'})
    replace(r['limitations'],
            {'zh': 'Ren 只确认了律与历史的读法；', 'en': 'Ren having confirmed only the reading of law and history;'},
            {'zh': 'Ren 确认了律与历史的读法并批准了语境中的读法；',
             'en': 'Ren having confirmed the reading of law and history and approved readings in context;'})
    r['related'].append({
        'id': 'unity-of-readings',
        'detail': {'zh': '读一个展开的都是语境中的读法，诸读法总是一个世界（Contextual.world，如 Frame.world）；World 是粘合的读法，算入其余时'
                         '每个世界都是交换之律的一次运行（World.unity），World.exchangeRun 的平衡前提由此去掉。Ren 批准语境中的读法为一般情形、'
                         'World 为粘合的情形，过程与框架同是一个展开的读法。',
                   'en': 'Whatever reads an unfolding is a reading in context, and the readings are always one world '
                         '(Contextual.world, as Frame.world); World is the glued reading, and with the rest counted every world is '
                         'one run of the law of exchange (World.unity), which drops the balance premise of World.exchangeRun. Ren '
                         'approved the readings in context as the general case and World as the glued case, the process and the '
                         'frame being readings of one unfolding.'}})
    note(r, '下一步中“Ren 的判断：起点是否读作 World，过程与框架是否读作它的读法”由 Ren 2026-10-14 的批准（“please, finish all”）回答，删去；'
            '限制中“Ren 只确认了律与历史的读法”改为“Ren 确认了律与历史的读法并批准了语境中的读法”；related 加 unity-of-readings，'
            '说明所批准的读法。陈述与证明不变。',
            'in the next step, “Ren\'s judgment whether the starting point reads as World, with the process and the frame as its '
            'readings” is answered by Ren\'s approval of 14 October 2026 (“please, finish all”) and removed; in the limitations, '
            '“Ren having confirmed only the reading of law and history” becomes “Ren having confirmed the reading of law and history '
            'and approved readings in context”; related adds unity-of-readings, stating the approved reading. Statement and proofs '
            'unchanged.')
    save(r)


def contextual():
    r = load('contextual-registration')
    old = {'zh': '零前提计划把不依语境的主张列为表示的承诺（整合者决定）；奇偶障碍的一般定理；概率的语境性；Ren 的判断：值读作语境中的识。',
           'en': "The zero-premise plan listing context-free claims as a commitment of the representation (the integrator decides); "
                 "the general parity obstruction; probabilistic contextuality; Ren's judgment on reading a value as a registration "
                 "in context."}
    assert r['next_delta'] == old, r['next_delta']
    r['next_delta'] = {
        'zh': '零前提计划把不依语境的主张列为粘合的情形（World）的承诺，而不是语境中的读法的承诺（整合者决定）；奇偶障碍的一般定理；概率的语境性。',
        'en': 'The zero-premise plan listing context-free claims as a commitment of the glued case (World), not of the readings '
              'in context (the integrator decides); the general parity obstruction; probabilistic contextuality.'}
    r['related'].append({
        'id': 'unity-of-readings',
        'detail': {'zh': '语境中的诸识总是一个世界的关系项，不用粘合；World 的平衡是所立与交换两种变化读法的粘合。Ren 批准语境中的读法为一般情形。',
                   'en': 'Registrations in context are always the relata of one world, with no gluing; World\'s balance is the '
                         'gluing of the standing\'s and the exchange\'s readings of change. Ren approved the readings in context as '
                         'the general case.'}})
    note(r, '下一步原为“零前提计划把不依语境的主张列为表示的承诺（整合者决定）；奇偶障碍的一般定理；概率的语境性；Ren 的判断：值读作语境中的识”：'
            '不依语境的主张改为粘合的情形（World）的承诺（仍由整合者决定计划是否这样列出）；“Ren 的判断”由 Ren 2026-10-14 批准语境中的读法为'
            '一般情形（“please, finish all”）回答，删去；related 加 unity-of-readings。陈述与证明不变。',
            'the next step, formerly “The zero-premise plan listing context-free claims as a commitment of the representation (the '
            'integrator decides); the general parity obstruction; probabilistic contextuality; Ren\'s judgment on reading a value as '
            'a registration in context”: context-free claims become a commitment of the glued case (World), the integrator still '
            'deciding whether the plan lists them so; “Ren\'s judgment” is answered by Ren\'s approval of the readings in context as '
            'the general case on 14 October 2026 (“please, finish all”) and removed; related adds unity-of-readings. Statement and '
            'proofs unchanged.')
    save(r)


if __name__ == '__main__':
    imbalance()
    premises_map()
    process_frame()
    contextual()
    print('updated four records')
