#!/usr/bin/env python3
"""Write E1's three records and update premises-read-off-the-exchange and theory-of-becoming-foundation:
python3 -B make_records.py CORE_RECEIPT   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of the module (a short name must match
exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'ExchangePremises'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
_h = re.search(r'^## (\d+)\. Which remaining premises a reading of the exchange settles \(E1\)$',
               (ROOT / STUDY).read_text(), re.M)
assert _h
SEC = _h.group(1)
ANCHOR = f'#{SEC}-which-remaining-premises-a-reading-of-the-exchange-settles-e1'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


def decls(mod):
    m = next(m for m in core['modules'] if m['module'] == f'Becoming.{mod}')
    assert core['source_sha256'][f'Becoming.{mod}'] == sha(src(mod)), ('receipt does not bind', mod)
    return m


def resolve(names, mod=MOD):
    full = [d['name'] for d in decls(mod)['declarations']]
    out = []
    for n in names:
        hits = [f for f in full if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (mod, n, hits)
        out.append(hits[0])
    return out


m = decls(MOD)
assert not any(m['axiom_dependencies'].values())
N_DECL, N_THM = len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')
BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']
CORR = {'en': 'The first open target of chapter §8.1, the deductive necessity of the whole, had no progress entry since the '
              'early spine; §125 left four World premises as states of parts. This result settles {what}. The '
              'classification of the eight premises into readings of one exchange and states of the law is the AI\'s; '
              'the session reviewing the repository on 19 October 2026 set the task.',
        'zh': '第 8.1 节的首要开放目标，整体的演绎必然性，自早期脊柱以来没有进展条目；§125 把 World 的四个前提留作部分的状态。'
              '本结果判定{what_zh}。把八个前提分为一次交换的读法与律的状态是 AI 的；任务由 2026年10月19日审阅仓库的会话提出。'}
FOUNDATION = {'id': 'theory-of-becoming-foundation', 'detail': {
    'en': 'Progress on the first target: what a reading of the exchange makes necessary, and where becoming is contingent '
          'in the law.',
    'zh': '首要目标的进展：交换的读法使什么成为必然，生成在律中何处偶然。'}}


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


READING_DEP = dep(
    'premises-read-off-the-exchange', 'formal-reuse',
    'Reuses Flow.Exchanging, Flow.readOff, World.withRest, World.restFlow, Flow.present_distinct, '
    'World.withRest_exchanging_iff, World.withRest_closed_iff, ExchangeLaw.readWorld and ExchangeLaw.readWorld_glue.',
    '复用 Flow.Exchanging、Flow.readOff、World.withRest、World.restFlow、Flow.present_distinct、World.withRest_exchanging_iff、'
    'World.withRest_closed_iff、ExchangeLaw.readWorld 与 ExchangeLaw.readWorld_glue。',
    'Worlds read off an exchange with the rest counted, the four tying premises holding.',
    '算入其余、从交换读出的世界，四个联结前提成立。',
    'The worlds on which each remaining premise is settled.', '判定每个其余前提所在的世界。', 'None.', '无。',
    src('Reading'))
COUNTERFACTUAL_DEP = dep(
    'counterfactual-is-the-course', 'formal-reuse',
    'Reuses ExchangeLaw, levels, levels_succ, course, Feasible, Nonanticipating and readWorld_closed_iff.',
    '复用 ExchangeLaw、levels、levels_succ、course、Feasible、Nonanticipating 与 readWorld_closed_iff。',
    'The course a law generates; the rest idle exactly where a law of what has stood is feasible.',
    '律生成的历程；读已立者的律可行之处其余恰闲置。',
    'Witness worlds with the rest idle.', '其余闲置的见证世界。', 'The law reads what has stood.', '律只读已立者。',
    src('Counterfactual'))
PREMISES_DEP = dep(
    'map-of-premises', 'formal-reuse',
    'Reuses the eight premises World.Dissipative, World.Embodied, World.Counted and World.Transmitting, keep, mem_keep, '
    'keep_distinct, beyond and lt_beyond.',
    '复用八个前提中的 World.Dissipative、World.Embodied、World.Counted、World.Transmitting，以及 keep、mem_keep、keep_distinct、'
    'beyond 与 lt_beyond。',
    'The premises and the list operations.', '前提与列表运算。', 'What is settled for each premise.', '每个前提被判定之处。',
    'None.', '无。', src('Premises'))


def record(rid, title, statement, laws, hypotheses, dns, counterexamples, nxt, corr, aliases, deps, related, extra_refs,
           bounds=BOUNDS):
    aliases = [resolve([a[len('Becoming.'):]])[0] if a.startswith('Becoming.') else a for a in aliases]
    cited = {src(MOD)} | {p for p, _ in extra_refs}
    extra_refs = list(extra_refs) + [(d['interface']['evidence'], None) for d in deps
                                     if d['interface']['evidence'] not in cited]
    assert len(statement['en']) <= 300, (rid, len(statement['en']))
    r = {
        'schema_version': 2, 'id': rid, 'title': title, 'kind': 'theorem', 'status': 'recorded-checked',
        'family': 'F01', 'reviewed_at_utc': NOW, 'statement': statement,
        'laws': [{'en': en, 'zh': zh, 'declarations': resolve(names)} for en, zh, names in laws],
        'hypotheses': hypotheses, 'does_not_show': dns, 'counterexamples': counterexamples,
        'standard_boundaries': bounds,
        'validation_scope': {
            'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {N_DECL} declarations '
                  f'of Becoming.{MOD}, {N_THM} of them theorems, have empty axiom reports; the checker verifies core purity. '
                  f'Author review in study section {SEC}; not independently reviewed.',
            'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {N_DECL} 项声明（{N_THM} 项定理）公理报告为空；'
                  f'检查器并核对核心纯净。作者审查见研究第 {SEC} 节；未经独立审查。'},
        'next_delta': nxt, 'correspondence': corr, 'canonical_source': src(MOD), 'aliases': aliases,
        'dependencies': deps, 'related': related + [FOUNDATION],
        'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                        'sha256': sha(src(MOD))}]
        + [dict({'path': p, 'role': 'proof'}, **({'declarations': ds} if ds else {}), sha256=sha(p)) for p, ds in extra_refs]
        + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
           {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
           {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
        'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                            'success_pointer': '/status', 'success_value': 'passed'}],
        'history': [{
            'en': '19 October 2026: added (E1), on the first target of chapter §8.1, the deductive necessity of the whole; '
                  f'study section {SEC}.',
            'zh': f'2026年10月19日：新增（E1），针对第 8.1 节的首要目标，整体的演绎必然性；研究第 {SEC} 节。'}],
    }
    path = RECORDS / f'{rid}.json'
    assert not path.exists(), ('record exists', rid)
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('written', rid)


# E1a: the census.
record(
    'census-read-off-the-exchange',
    {'en': 'The census read off the exchange', 'zh': '从交换读出的普查'},
    {'en': 'Read off the exchange, the relata that exchange are listed with no decision procedure wherever a named family '
           'closes each step; every finite world has a census with its rest counted. No census fails at any step, and '
           'asking one at every step of every flow over Nat is LPO.',
     'zh': '从交换读出，凡有一个具名的家族围住每一步，交换者就被列出，不需判定程序；每个有限世界算入其余都有普查。没有普查在任何一步失败，'
           '而对 Nat 上每个流的每一步要求普查是有限全知原则。'},
    [('Whether a formation exchanges with some member of a list is decided by going through the list; where a family '
      'closes a step, a formation exchanges exactly where it takes part and exchanges within the family, so the formations '
      'taking part, listed once, are kept to those that exchange: a census read off the exchange, with no decision '
      'procedure supplied.',
      '一个形成是否与某个列表成员交换，逐一查看列表即可判定；家族围住一步时，形成恰在它参与且在家族内交换时交换，所以把各列一次的参与形成'
      '留下交换者即得从交换读出的普查，不提供判定程序。',
      ['Flow.ExchangesWithin', 'Flow.exchangesWithin_decided', 'of_not_not', 'Flow.exchanging_iff_within',
       'Flow.listed_at_of_closed', 'Flow.listed_at_of_enclosed', 'Flow.readOff_census_of_closed']),
     ('With the rest counted, every world whose formations taking part are listed once and whose steps a named family '
      'closes has a census; every finite world does, where World.Finite.counted needed activity decided.',
      '算入其余，参与形成各列一次、每一步由一个具名家族围住的每个世界都有普查；每个有限世界都有，而 World.Finite.counted 需要活跃可判定。',
      ['World.withRest_counted', 'World.Finite.withRest_counted']),
     ('Without enclosure, that a world read off an exchange fails a census at a step is refuted: of a list without '
      'repetition, the members meeting any property cannot fail to be listable.',
      '不被围住时，从交换读出的世界在某一步缺普查被否证：对无重复的列表，满足任何性质的成员不可能不可列出。',
      ['listed_of_em', 'not_not_listed', 'Flow.not_not_listed_at']),
     ('A census at every step of every flow over Nat with its formations listed once is exactly LPO: under marking s a '
      'formation exchanges exactly where s marks something.',
      '对 Nat 上参与形成各列一次的每个流的每一步要求普查，恰是有限全知原则：在 marking s 下形成恰在 s 标出某处时交换。',
      ['Flow.marking', 'Flow.cond_pos', 'Flow.marking_exchanging', 'Flow.memDecided', 'Flow.listed_iff_lpo']),
     ('Enclosure is not read off: read off the spreading law, which gives every relatum a unit, the rest is idle and no '
      'step is enclosed, and the world has a census all the same.',
      '被围住不是读出的：从给每个关系项一个单位的 spreading 律读出，其余闲置，没有一步被围住，世界仍有普查。',
      ['ExchangeLaw.spreading', 'ExchangeLaw.spreadingWorld', 'ExchangeLaw.spreading_closed', 'ExchangeLaw.origin',
       'ExchangeLaw.optionIndex', 'ExchangeLaw.spreading_not_enclosed', 'ExchangeLaw.spreading_counted'])],
    [{'en': 'No axiom. The formations taking part at each step are listed once (a condition of the representation, as in '
            'Flow.readOff_census); for the census as a function of the step, a family closing each step is named (data, '
            'not only its existence at each step); listed_iff_lpo concerns flows over Nat.',
      'zh': '不加公理。每一步的参与形成各列一次（表示的条件，同 Flow.readOff_census）；普查作为步的函数时，围住每一步的家族是具名的'
            '（数据，不只是每一步的存在）；listed_iff_lpo 关于 Nat 上的流。'}],
    [{'en': 'That an actual unfolding\'s exchange at a step lies within finitely many relata: enclosure is a state of the '
            'law.', 'zh': '实际展开在一步上的交换落在有限多个关系项之内：被围住是律的状态。', 'kind': 'scope'},
     {'en': 'A census over every step where each step is enclosed but no family is named: that would also need countable '
            'choice.', 'zh': '每一步都被围住而没有具名家族时，所有步上的普查：那还需要可数选择。', 'kind': 'scope'},
     {'en': 'That a census counts a population in any further sense: it lists the relata that exchange.',
      'zh': '普查在更进一步的意义上计数一个群体：它列出交换的关系项。', 'kind': 'correspondence'}],
    [{'path': src(MOD), 'detail': {
        'en': 'spreadingWorld: no step is enclosed (spreading_not_enclosed) and a census exists (spreading_counted): '
              'enclosure suffices for a census and is not needed.',
        'zh': 'spreadingWorld：没有一步被围住（spreading_not_enclosed），普查存在（spreading_counted）：被围住对普查是充分的，不是必要的。'}}],
    {'en': 'A census over every step without a named family; an independent review.',
     'zh': '无具名家族时所有步上的普查；独立审查。'},
    {'en': CORR['en'].format(what='the census: a reading under enclosure, never refuted, and LPO where asked of every flow'),
     'zh': CORR['zh'].format(what_zh='普查：在被围住处是读法，从不被否证，对每个流要求它是有限全知原则')},
    ['census read off the exchange', '从交换读出的普查', 'Becoming.Flow.readOff_census_of_closed',
     'Becoming.World.Finite.withRest_counted', 'Becoming.Flow.listed_iff_lpo'],
    [READING_DEP, PREMISES_DEP],
    [{'id': 'premises-read-off-the-exchange', 'detail': {
        'en': 'There a census needed exchanging decided (Flow.readOff_census); here a family closing the step decides it.',
        'zh': '那里普查需要交换可判定（Flow.readOff_census）；这里围住该步的家族判定它。'}},
     {'id': 'counting-where-the-counts-exist', 'detail': {
        'en': 'Counting over counted censuses takes no decision; here the census itself is read off the exchange.',
        'zh': '在已计数的普查上计数不需判定；这里普查本身从交换读出。'}}],
    [(src('Premises'), ['Becoming.World.Counted', 'Becoming.World.Finite.counted', 'Becoming.keep', 'Becoming.mem_keep']),
     (src('Change'), ['Becoming.LPO'])],
    bounds=BOUNDS + ['decidability'])

# E1b: the three states of the law.
record(
    'premises-that-are-states-of-the-law',
    {'en': 'Dissipation, embodiment and transmission are states of the law', 'zh': '耗散、体现与传递是律的状态'},
    {'en': 'Read off laws of exchange, with the rest counted and idle and the four tying premises holding, dissipation, '
           'embodiment and bounded transmission are each met by one world and failed by another. With the rest counted, '
           'embodiment is balance and each relatum exchanging exactly while it stands.',
     'zh': '从交换之律读出、算入其余且其余闲置、四个联结前提成立时，耗散、体现与有界传递各有一个满足的世界与一个不满足的世界。'
           '算入其余时，体现恰是平衡加上每个关系项恰在它立着时交换。'},
    [('Dissipation is loss: with the rest counted and idle, a world whose formations give nothing dissipates; read off '
      'the responsive law the relatum takes its condition\'s unit and gives it back, and the world does not dissipate.',
      '耗散是损失：算入其余且其余闲置，形成什么都不给的世界耗散；从 responsive 律读出，关系项取走其条件的单位又给回，世界不耗散。',
      ['World.restFlow_give_zero', 'World.withRest_dissipative_of_gives_nothing', 'ExchangeLaw.still',
       'ExchangeLaw.still_levels', 'ExchangeLaw.stillWorld', 'ExchangeLaw.responsiveWorld', 'ExchangeLaw.still_balanced',
       'ExchangeLaw.responsive_balanced', 'ExchangeLaw.still_closed', 'ExchangeLaw.responsive_closed',
       'ExchangeLaw.still_dissipative', 'ExchangeLaw.responsive_not_dissipative']),
     ('Embodiment is closure and no dormancy: with the rest counted, every relatum stands exactly while it is active '
      'exactly where the world balances and each relatum exchanges exactly while it stands; read off still from a standing '
      'of one the relatum stands and does not exchange, read off responsive it exchanges exactly while it stands.',
      '体现是封闭加上没有休眠：算入其余，每个关系项恰在活跃时立着，恰当世界平衡且每个关系项恰在立着时交换；从 still 以水平一读出，关系项立着而'
      '不交换，从 responsive 读出，它恰在立着时交换。',
      ['World.withRest_embodied_iff', 'World.withRest_embodied_balanced', 'ExchangeLaw.still_not_embodied',
       'ExchangeLaw.responsive_embodied']),
     ('Bounded transmission is heredity of response: where nothing comes to stand it holds with any bound; read off the '
      'sprouting law, the sprout comes to stand from the source, its exchange then responds to the ground and the source\'s '
      'giving does not, so no bound transmits the dependence, with the rest idle.',
      '有界传递是回应的遗传：没有什么开始立着之处它以任何界成立；从 sprouting 律读出，萌芽由源而立，其交换随后回应地，而源的给予不回应，'
      '所以没有界传递这一依存，其余闲置。',
      ['World.transmitting_of_nothing_comes', 'ExchangeLaw.nothing_comes', 'ExchangeLaw.still_transmitting',
       'ExchangeLaw.responsive_transmitting', 'ExchangeLaw.Sprouting', 'ExchangeLaw.sprouting', 'ExchangeLaw.sprouts',
       'ExchangeLaw.groundOne', 'ExchangeLaw.needOneOf', 'ExchangeLaw.sproutingWorld',
       'ExchangeLaw.sprouting_nonanticipating', 'ExchangeLaw.sprouting_feasible', 'ExchangeLaw.sprouting_closed',
       'ExchangeLaw.sprout_descends', 'ExchangeLaw.sprout_requires', 'ExchangeLaw.source_unrequired',
       'ExchangeLaw.sprouting_not_transmitting']),
     ('The three are contingent: three worlds read off laws, each with the rest counted and idle and the four tying '
      'premises holding; still meets dissipation and transmission and not embodiment, responsive embodiment and '
      'transmission and not dissipation, sprouting not transmission.',
      '三者都是偶然的：三个从律读出的世界，各自算入其余且其余闲置、四个联结前提成立；still 满足耗散与传递而不满足体现，responsive 满足体现与'
      '传递而不满足耗散，sprouting 不满足传递。',
      ['ExchangeLaw.contingent'])],
    [{'en': 'No axiom and no premise: each witness is a world read off a law of exchange with the rest counted, the rest '
            'shown idle; the general laws (withRest_dissipative_of_gives_nothing, withRest_embodied_iff, '
            'transmitting_of_nothing_comes) state their hypotheses.',
      'zh': '不加公理，不加前提：每个见证都是算入其余、从交换之律读出的世界，其余已示闲置；一般规律（withRest_dissipative_of_gives_nothing、'
            'withRest_embodied_iff、transmitting_of_nothing_comes）写明各自的假设。'}],
    [{'en': 'Which law of exchange holds in an actual unfolding: whether it loses, has dormant relata or passes on what '
            'its descendants respond to is empirical.',
      'zh': '实际展开中哪条交换之律成立：它是否有损失、是否有休眠的关系项、是否传下后代所回应者，是经验问题。', 'kind': 'scope'},
     {'en': 'That loss, embodiment or heredity is good, or that a law meeting them supports 生生.',
      'zh': '损失、体现或遗传是好的，或满足它们的律支持生生。', 'kind': 'non-implication'},
     {'en': 'A reading under which standing is not the level that balance glues to the exchange; under such a reading '
            'embodiment would need restating.',
      'zh': '一种立着不是平衡粘合到交换上的水平的读法；在那种读法下体现需要重述。', 'kind': 'scope'}],
    [{'path': src(MOD), 'detail': {
        'en': 'responsiveWorld fails dissipation; stillWorld fails embodiment; sproutingWorld fails bounded transmission; '
              'each with the rest counted and idle and the four tying premises holding.',
        'zh': 'responsiveWorld 不满足耗散；stillWorld 不满足体现；sproutingWorld 不满足有界传递；各自算入其余且其余闲置、四个联结前提成立。'}}],
    {'en': 'The spine\'s laws that use these premises stated over the laws of exchange that meet them; local conditions on '
           'a law that give each; an independent review.',
     'zh': '用到这些前提的脊柱规律，陈述在满足它们的交换之律上；给出每个前提的律的局部条件；独立审查。'},
    {'en': CORR['en'].format(what='dissipation, embodiment and bounded transmission: states of the law of exchange, not '
                                  'readings'),
     'zh': CORR['zh'].format(what_zh='耗散、体现与有界传递：交换之律的状态，不是读法')},
    ['states of the law of exchange', '交换之律的状态', 'Becoming.ExchangeLaw.contingent',
     'Becoming.World.withRest_embodied_iff', 'Becoming.ExchangeLaw.sprouting_not_transmitting'],
    [READING_DEP, COUNTERFACTUAL_DEP, PREMISES_DEP],
    [{'id': 'map-of-premises', 'detail': {
        'en': 'There the eight premises are independent relative to one another; here three of them are contingent on the '
              'law with the rest of the readings fixed by it.',
        'zh': '那里八个前提相对于彼此独立；这里其中三个在其余读法由律固定时取决于律。'}}],
    [(src('Space'), ['Becoming.World.Dissipative', 'Becoming.World.Embodied']),
     (src('Premises'), ['Becoming.World.Transmitting']),
     (src('Reading'), ['Becoming.ExchangeLaw.responsive', 'Becoming.ExchangeLaw.responsive_levels',
                       'Becoming.ExchangeLaw.readWorld_glue'])])

# E1c: requirement over open exchanges.
record(
    'requirement-over-open-exchanges',
    {'en': 'Requirement as response where several exchanges are open', 'zh': '多个交换开放时把要求读作回应'},
    {'en': 'Where a relation of exchange leaves several exchanges open, requirement read as necessary response gives '
           'activity needing support on every run, and with the rest counted the four tying premises hold; read as '
           'possible response it does not. A law is the relation leaving one exchange open.',
     'zh': '交换关系留下多个交换开放时，把要求读作必然的回应，每个运行上活动都需要支持，算入其余时四个联结前提成立；读作可能的回应则不然。'
           '律是只留下一个交换开放的关系。'},
    [('A relation of exchange leaves open, under each level history, any number of exchanges across a step; a run takes '
      'an open exchange at every step. A formation\'s exchange necessarily responds to a condition falling below a need '
      'where, under every history differing at most in that level at that step with the level below the need, no open '
      'exchange has it exchange; read as requirement, activity needs support on every run, for every history and need, '
      'and with the rest counted the four tying premises hold.',
      '交换关系在每个水平历史下留下一步上任意多个交换开放；运行在每一步取一个开放的交换。一个形成的交换必然回应条件低于所需，当在至多在该步该'
      '水平上不同且水平低于所需的每个历史下，没有开放的交换让它交换；读作要求，每个运行上对每个历史与所需活动都需要支持，算入其余时四个联结前提'
      '成立。',
      ['ExchangeRelation', 'ExchangeRelation.Exchanges', 'ExchangeRelation.RespondsBelow', 'ExchangeRelation.Runs',
       'ExchangeRelation.readWeb', 'ExchangeRelation.readWeb_dependent', 'ExchangeRelation.world',
       'ExchangeRelation.reading_glue']),
     ('Read as possible response (some open exchange leaves it idle), activity need not be supported: under the free '
      'relation a formation takes a unit at a level of nothing and possibly responds.',
      '读作可能的回应（某个开放的交换让它闲置），活动不必被支持：在 free 关系下形成在水平为零时取一个单位，且可能回应。',
      ['ExchangeRelation.MayRespondBelow', 'ExchangeRelation.free', 'ExchangeRelation.takingOne',
       'ExchangeRelation.free_unsupported']),
     ('A law of exchange is the relation leaving one exchange open; its course is a run of it, and there necessary and '
      'possible response are the law\'s response: read off the course as a run, the web\'s requirement is the law\'s.',
      '交换之律是只留下一个交换开放的关系；它的历程是这个关系的运行，在那里必然回应与可能回应都是律的回应：把历程读作运行，网的要求就是律的。',
      ['ExchangeLaw.relation', 'ExchangeLaw.course_runs', 'ExchangeLaw.relation_exchanges', 'ExchangeLaw.relation_admits',
       'ExchangeLaw.relation_responds_iff', 'ExchangeLaw.relation_may_iff', 'ExchangeLaw.relation_readWeb_requires',
       'ExchangeLaw.relation_readWeb_may'])],
    [{'en': 'No axiom and no premise: the relation, the run along a history and the need are given; levels need not follow '
            'balance on a run, the rest counting the difference.',
      'zh': '不加公理，不加前提：关系、沿历史的运行与所需是给定的；运行上的水平不必遵从平衡，差额由其余计入。'}],
    [{'en': 'Which exchanges are open in an actual unfolding, or that any exchange responds to anything.',
      'zh': '实际展开中哪些交换开放，或任何交换回应任何东西。', 'kind': 'scope'},
     {'en': 'A join to the branching processes of Becoming.Branching: the relation is not stated as a Generative.Process.',
      'zh': '与 Becoming.Branching 的分支过程相连：关系没有陈述为 Generative.Process。', 'kind': 'scope'}],
    [{'path': src(MOD), 'detail': {
        'en': 'free_unsupported: under the free relation a formation exchanges at a level of nothing while its exchange '
              'possibly responds to the condition falling below one.',
        'zh': 'free_unsupported：在 free 关系下，形成在水平为零时交换，而其交换可能回应条件低于一。'}}],
    {'en': 'The relation of exchange read as a process on level histories and joined to Becoming.Branching; levels '
           'following balance on runs; an independent review.',
     'zh': '把交换关系读作水平历史上的过程并与 Becoming.Branching 相连；运行上水平遵从平衡；独立审查。'},
    {'en': CORR['en'].format(what='the next delta of premises-read-off-the-exchange: requirement read as response where '
                                  'several exchanges are open'),
     'zh': CORR['zh'].format(what_zh='premises-read-off-the-exchange 的下一步：多个交换开放时把要求读作回应')},
    ['requirement over open exchanges', '开放交换上的要求', 'Becoming.ExchangeRelation.readWeb_dependent',
     'Becoming.ExchangeRelation.free_unsupported', 'Becoming.ExchangeLaw.relation_responds_iff'],
    [READING_DEP, COUNTERFACTUAL_DEP],
    [{'id': 'returning-where-the-course-branches', 'detail': {
        'en': 'Branching processes where the configuration fixes only which steps are admissible; here which exchanges are '
              'open under a level history.',
        'zh': '配置只固定哪些步可容许的分支过程；这里是在水平历史下哪些交换开放。'}}],
    [(src('Reading'), ['Becoming.ExchangeLaw.RespondsBelow', 'Becoming.ExchangeLaw.readWeb',
                       'Becoming.ExchangeLaw.supported_of_responds', 'Becoming.World.withRest_dependent_iff'])])

# premises-read-off-the-exchange: the census scope line and the next delta.
p = RECORDS / 'premises-read-off-the-exchange.json'
d = json.loads(p.read_text())
old = 'Closure, dissipation, embodiment, bounded transmission and the decision to list what is active are not read off the exchange; they remain states of parts.'
hit = [x for x in d['does_not_show'] if x['en'] == old]
assert len(hit) == 1
hit[0]['en'] = ('Closure, dissipation, embodiment and bounded transmission are not read off the exchange: they are states of '
                'the law (premises-that-are-states-of-the-law). The decision to list what is active is not needed where a '
                'named family closes each step (census-read-off-the-exchange).')
hit[0]['zh'] = ('封闭、耗散、体现与有界传递不从交换读出：它们是律的状态（premises-that-are-states-of-the-law）。'
                '凡有具名的家族围住每一步，列出活跃者不需判定（census-read-off-the-exchange）。')
d['next_delta'] = {'en': 'An independent review.', 'zh': '独立审查。'}
d['related'] += [
    {'id': 'census-read-off-the-exchange', 'detail': {
        'en': 'The census, left here needing exchanging decided, is read off the exchange where a named family closes each '
              'step.', 'zh': '这里留下需要交换可判定的普查，在具名家族围住每一步之处从交换读出。'}},
    {'id': 'premises-that-are-states-of-the-law', 'detail': {
        'en': 'Of the states of parts left here, dissipation, embodiment and bounded transmission are states of the law.',
        'zh': '这里留下的部分的状态中，耗散、体现与有界传递是律的状态。'}},
    {'id': 'requirement-over-open-exchanges', 'detail': {
        'en': 'This record\'s next delta: requirement as response where several exchanges are open.',
        'zh': '本记录的下一步：多个交换开放时把要求读作回应。'}}]
d['history'].append({
    'en': '19 October 2026, E1: the scope line on closure, dissipation, embodiment, bounded transmission and the decision to '
          'list what is active corrected (census-read-off-the-exchange, premises-that-are-states-of-the-law); the next '
          'delta, requirement read as response over branching, done (requirement-over-open-exchanges), leaving an '
          f'independent review; three related records added. The claim is unchanged; study section {SEC}.',
    'zh': '2026年10月19日，E1：关于封闭、耗散、体现、有界传递与列出活跃者之判定的范围条目更正（census-read-off-the-exchange、'
          'premises-that-are-states-of-the-law）；下一步“分支过程上把要求读作回应”已完成（requirement-over-open-exchanges），'
          f'余下独立审查；新增三个相关记录。论断不变；研究第 {SEC} 节。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated premises-read-off-the-exchange')

# theory-of-becoming-foundation: a progress entry.
p = RECORDS / 'theory-of-becoming-foundation.json'
d = json.loads(p.read_text())
d['progress'].append({
    'en': 'Premises read off one exchange (E1): of the eight World premises, five are readings (the four tying premises, '
          'and the census under enclosure, never refuted without it) and three, dissipation, embodiment and bounded '
          'transmission, are states of the law of exchange, as closure and enclosure are; the necessary content of the '
          'whole cannot include those three.',
    'zh': '从一次交换读出的前提（E1）：World 的八个前提中五个是读法（四个联结前提，以及被围住时的普查，不被围住时从不被否证），耗散、'
          '体现与有界传递三个是交换之律的状态，与封闭和被围住一样；整体的必然内容不能包括这三个。',
    'source': STUDY + ANCHOR})
d['related'] += [
    {'id': 'premises-that-are-states-of-the-law', 'detail': {
        'en': 'Where becoming is contingent in the law: dissipation, embodiment and bounded transmission are met by some '
              'laws of exchange and failed by others, with the readings fixed.',
        'zh': '生成在律中偶然之处：读法固定时，耗散、体现与有界传递有满足与不满足它们的交换之律。'}},
    {'id': 'census-read-off-the-exchange', 'detail': {
        'en': 'The census is a reading of the exchange under enclosure.', 'zh': '普查在被围住时是交换的读法。'}}]
d['history'].append({
    'en': '19 October 2026, E1: a progress entry and two related records (premises read off one exchange: which premises '
          f'are readings and which are states of the law); study section {SEC}. The target\'s wording is unchanged.',
    'zh': f'2026年10月19日，E1：新增一条进展与两个相关记录（从一次交换读出的前提：哪些前提是读法、哪些是律的状态）；研究第 {SEC} 节。目标措辞不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated theory-of-becoming-foundation')
