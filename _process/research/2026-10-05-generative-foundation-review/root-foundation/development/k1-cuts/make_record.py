#!/usr/bin/env python3
"""Write K1's record which-links-a-closure-needs and restate the records bound to PreparationCorrespondence:
python3 -B make_record.py CORE_RECEIPT INSTANCE_RECEIPT

Each receipt is checked against the current bytes of the source it binds, and every declaration the records
cite against those Lean elaborated, before anything is written. Run after the study section is in place."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
UE = 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics'
SRC = f'{PKG}/Becoming/Cuts.lean'
FEEDBACK = f'{PKG}/Becoming/Feedback.lean'
INST = f'{UE}/PreparationCorrespondence.lean'
INST_CHECKER = f'{UE}/check_preparation_correspondence.py'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-general-laws-from-examples.md'
core_id, inst_id = sys.argv[1], sys.argv[2]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
inst_receipt = f'{UE}/preparation-correspondence-checks/{inst_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
inst = json.loads((ROOT / inst_receipt).read_text())
assert core['status'] == 'passed' and inst['status'] == 'passed'
assert core['source_sha256']['Becoming.Cuts'] == sha(SRC), 'core receipt does not bind Cuts.lean'
assert core['source_sha256']['Becoming.Feedback'] == sha(FEEDBACK)
assert inst['source_sha256']['PreparationCorrespondence'] == sha(INST), 'instance receipt does not bind the module'
cut_decls = {d['name'] for m in core['modules'] if m['module'] == 'Becoming.Cuts' for d in m['declarations']}
cut_axioms = {n: a for m in core['modules'] if m['module'] == 'Becoming.Cuts' for n, a in m['axiom_dependencies'].items()}
assert not any(cut_axioms.values())
inst_decls = {d['name'] for m in inst['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(r'^## 190\. Which links a closure needs \(K1\)$', STUDY_TEXT, re.M)
ANCHOR = '#190-which-links-a-closure-needs-k1'
GO = '"let\'s make these limited, non general laws, into general ones"'


def c(*names):
    out = ['Becoming.Cuts.' + n if not n.startswith('Flow.') else 'Becoming.' + n for n in names]
    missing = [n for n in out if n not in cut_decls]
    assert not missing, missing
    return out


def i(*names):
    out = ['Becoming.PreparationCorrespondence.' + n for n in names]
    missing = [n for n in out if n not in inst_decls]
    assert not missing, missing
    return out


laws = [
    {'en': 'Removing the links of added from a relation leaves every closure as it was exactly where each removed '
           'link has its second end within its first end\'s closure under what remains; for one link read both ways, '
           'exactly where each end lies within the other\'s closure, and under a symmetric relation where one does.',
     'zh': '从一个关系中去掉 added 的联系，每个闭包保持原样，恰当每条被去掉的联系的后端在余下关系下处于前端的闭包之内；'
           '对双向读的一条联系，恰当两端各在对方的闭包之内；在对称关系下，恰当一端在另一端的闭包之内。',
     'declarations': c('Joined', 'Link', 'link_symm', 'within_congr', 'within_of_steps',
                       'closure_unchanged_iff_bypassed', 'link_cut_unchanged_iff', 'link_cut_unchanged_iff_of_symm')},
    {'en': 'After a link between a and b is joined, g lies within f\'s closure exactly where it did, or f reaches one '
           'of a, b and the other reaches g; no symmetry and no decision is used.',
     'zh': '连上 a 与 b 之间的一条联系之后，g 在 f 的闭包之内，恰当它原来就在，或 f 到达 a、b 之一而另一个到达 g；'
           '不用对称，也不用判定。',
     'declarations': c('within_link_iff')},
    {'en': 'A formation that takes part in no link reaches only itself and nothing else reaches it, so attaching it '
           'by one link changes no closure among the other formations.',
     'zh': '不参与任何联系的形成只到达自身，别的也到达不了它；所以以一条联系接上它，不改变其余形成之间的任何闭包。',
     'declarations': c('Unlinked', 'within_of_unlinked', 'not_within_unlinked', 'within_attached_iff')},
    {'en': 'In a list of links each attaching, to another formation, one that took part in no earlier link, each link '
           'is listed once, and removing any one leaves its ends apart, whatever came before or after it.',
     'zh': '在一列联系中，若每条都把一个此前不参与任何联系的形成接到另一个形成上，则每条联系只列一次，'
           '去掉任何一条都使其两端分开，无论之前或之后有什么。',
     'declarations': c('Links', 'links_symm', 'links_split', 'links_of_mem', 'Attaches', 'Attaches.suffix',
                       'Attaches.listed_once', 'attached_link_separates')},
    {'en': 'With one more link joined between a and b, a grown link p–n is bypassed exactly where p reaches one of a, b '
           'and the other reaches n without it; cutting it then changes no closure exactly there.',
     'zh': '再连上 a 与 b 之间的一条联系后，一条生长出的联系 p–n 被绕过，恰当不经它时 p 到达 a、b 之一而另一个到达 n；'
           '此时切断它不改变任何闭包，也恰在此处。',
     'declarations': c('joined_bypass_iff', 'joined_cut_unchanged_iff')},
    {'en': 'On the base, every system is what it is through the conditions other than c exactly where any two '
           'formations taking part in c lie in one system through the others; a condition one formation takes part '
           'in is needed by no system.',
     'zh': '在基上，每个系统只经 c 以外的条件仍是原样，恰当任何两个参与 c 的形成经其余条件处于同一系统；'
           '只有一个形成参与的条件，任何系统都不需要。',
     'declarations': c('Flow.SharesBeside', 'Flow.BothTakePart', 'Flow.shares_iff_beside',
                       'Flow.system_unchanged_without_iff', 'Flow.system_unchanged_of_single')},
    {'en': 'Where exactly a and b take part in c, g lies within f\'s system exactly where it does through the other '
           'conditions, or f reaches one of them and the other reaches g; a formation taking part only in c is alone '
           'without it, and one taking part in no condition has only itself in its system.',
     'zh': '恰有 a 与 b 参与 c 时，g 在 f 的系统之内，恰当它经其余条件就在，或 f 到达二者之一而另一个到达 g；'
           '只参与 c 的形成，没有 c 就是孤立的；不参与任何条件的形成，其系统只有它自身。',
     'declarations': c('Flow.withinSystem_two_takers_iff', 'Flow.alone_beside_of_only', 'Flow.withinSystem_of_no_part')},
]
listed = {d for law in laws for d in law['declarations']}
assert listed == cut_decls, sorted(cut_decls ^ listed)

record = {
    'schema_version': 2,
    'id': 'which-links-a-closure-needs',
    'title': {'en': 'Which links a closure needs', 'zh': '闭包需要哪些联系'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'levels-of-closure.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'A cut leaves every closure as it was exactly where each removed link is bypassed, and a join adds '
              'exactly what passes through it. Growth by attachment makes every link needed; one added link frees '
              'exactly the links it crosses. A system needs a condition where its takers meet only through it.',
        'zh': '切断使每个闭包保持原样，恰当每条被去掉的联系被绕过；连上一条联系，恰好添上经它通过的。'
              '依附式生长使每条联系都被需要；多连一条联系，恰使它跨过的联系不再被需要。'
              '系统需要一个条件，恰在参与者只经它相遇之处。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom and no premise beyond the relation in the general laws. On the base, splitting sharing a '
               'condition into sharing c and sharing another needs equality of conditions decided, given as '
               'DecidableEq C; withinSystem_two_takers_iff takes the list of c\'s takers as its hypothesis.',
         'zh': '一般规律除关系本身外不加公理、不加前提。在基上，把共享条件分成共享 c 与共享其他条件，需要条件相等可判定，'
               '以 DecidableEq C 给出；withinSystem_two_takers_iff 以 c 的参与者为假设。'},
    ],
    'does_not_show': [
        {'en': 'Which links form or are cut, when, or what a cut or a join takes; the laws take the relation as given.',
         'zh': '哪些联系形成或被切断、何时，或切断与连接耗去什么；这些规律以关系为给定。', 'kind': 'scope'},
        {'en': 'Growth by attachment read on the base: the laws of a list of attachments are stated on any relation, '
               'and read only in the periphery, on bodies grown by division.',
         'zh': '依附式生长在基上的读法：一列依附的规律对任何关系陈述，只在外围、在经分裂生长的身体上被读。',
         'kind': 'scope'},
        {'en': 'That keeping, cutting or adding a link supports 生生; a needed link is needed by a closure, not by a '
               'valuation.',
         'zh': '保持、切断或添上一条联系支持生生；被需要的联系是闭包所需，不是评价所需。', 'kind': 'non-implication'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'decidability', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the 31 declarations of '
              'Becoming.Cuts, 24 of them theorems, have empty axiom reports; the checker verifies core purity. The '
              'growth-constrained-fragmentation record holds the periphery instances. Author self-review in study '
              'section 190; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.Cuts 的 31 项声明（24 项定理）公理报告为空；'
              '检查器并核对核心纯净。外围实例见 growth-constrained-fragmentation。作者自审见研究第 190 节；未经独立审查。'},
    'next_delta': {
        'en': 'Growth by attachment read on the base, a world in which each new formation takes part only in a '
              'condition shared with one earlier formation; several joins at once and the count of links a whole '
              'needs; how links form and are cut along a run; an independent review.',
        'zh': '依附式生长在基上的读法：每个新形成只参与与一个先前形成共享的条件的世界；同时多处连接，以及一个整体所需的联系数；'
              '联系如何沿一次运行形成与被切断；独立审查。'},
    'correspondence': {
        'en': f'GrownFragmentation proved its bypass and its certified tree cuts for two hand-built bodies by kernel '
              f'computation. Ren, 19 October 2026, asked "why these numbers? is this really a proof?", then which of '
              f'its theorems are general laws, then {GO} (provenance, not warrant). Reading (the AI\'s): a link is '
              f'needed by a closure exactly where nothing else carries what it carries; growth by attachment alone '
              f'makes every link needed, and a link that closes a loop makes needless exactly the links on it.',
        'zh': f'GrownFragmentation 以内核计算对两个手工构造的身体证明了其绕行与经认证的树切割。Ren，2026年10月19日，'
              f'先问 "why these numbers? is this really a proof?"，又问其中哪些定理是一般规律，然后说 {GO}（来历，不是根据）。'
              f'读法（AI 的）：一条联系为闭包所需，恰在别无他物承载它所承载之处；仅有依附式生长使每条联系都被需要，'
              f'闭合一个回路的联系恰使回路上的联系不再被需要。'},
    'canonical_source': SRC,
    'aliases': ['which links a closure needs', '闭包需要哪些联系', 'cut changes no closure exactly where bypassed',
                '被绕过的切断不改变闭包', 'every link grown by attachment is needed', '依附式生长的每条联系都被需要',
                'which conditions a system needs', '系统需要哪些条件',
                'Becoming.Cuts.closure_unchanged_iff_bypassed', 'Becoming.Cuts.attached_link_separates',
                'Becoming.Flow.system_unchanged_without_iff'],
    'dependencies': [
        {'id': 'levels-of-closure', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses ClosedUnder, WithinClosure and its laws, Flow.TakesPart, Flow.Shares and '
                          'Flow.WithinSystem; the delta states which links and which conditions a closure needs.',
                    'zh': '复用 ClosedUnder、WithinClosure 及其规律、Flow.TakesPart、Flow.Shares 与 Flow.WithinSystem；'
                          '增量是陈述闭包需要哪些联系、系统需要哪些条件。'},
         'interface': {'output': {'en': 'Closures under a relation, and a formation\'s system as the closure under '
                                        'sharing a condition.',
                                  'zh': '关系下的闭包，以及作为共享条件之闭包的形成之系统。'},
                       'input': {'en': 'A relation with links removed or joined, and sharing split at one condition.',
                                 'zh': '去掉或连上联系的关系，以及在一个条件处分开的共享。'},
                       'conditions': {'en': 'DecidableEq C for the split at one condition.',
                                      'zh': '在一个条件处分开时需要 DecidableEq C。'},
                       'evidence': FEEDBACK}},
    ],
    'related': [
        {'id': 'growth-constrained-fragmentation',
         'detail': {'en': 'Its certified tree cuts and its bypass are cases: every bond of a body grown by division '
                          'is needed, and the reinforced chain\'s join frees the middle bond it crosses.',
                    'zh': '其经认证的树切割与绕行都是情形：经分裂生长的身体的每条键都被需要，加固链的连接使它跨过的中间键不再被需要。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(cut_decls), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': FEEDBACK, 'role': 'proof',
         'declarations': ['Becoming.ClosedUnder', 'Becoming.WithinClosure', 'Becoming.Flow.TakesPart',
                          'Becoming.Flow.Shares', 'Becoming.Flow.WithinSystem'], 'sha256': sha(FEEDBACK)},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(CHAPTER)},
        {'path': SOURCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(SOURCE)},
    ],
    'proof_bindings': [
        {'source': SRC, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Cuts',
         'success_pointer': '/status', 'success_value': 'passed'},
        {'source': FEEDBACK, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Feedback',
         'success_pointer': '/status', 'success_value': 'passed'},
    ],
    'history': [
        {'en': f'19 October 2026: added (K1), on Ren\'s {GO}, after his questions on GrownFragmentation\'s bypass '
               f'theorems; study section 190.',
         'zh': f'2026年10月19日：新增（K1），按 Ren 的 {GO}，在他就 GrownFragmentation 的绕行定理提问之后；研究第 190 节。'},
    ],
}
for item in (record['statement'],):
    assert len(item['en']) <= 300 and len(item['zh']) <= 150, (len(item['en']), len(item['zh']))
(RECORDS / 'which-links-a-closure-needs.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')

# growth-constrained-fragmentation: the instances, the new receipt and the reuse of the core laws.
NEW_INST = i('adjacent_iff_links', 'connected_iff_links', 'AttachedBelow', 'divide_attached', 'develop_attached',
             'initial_attached', 'cut_attached', 'bond_cut_separates', 'every_grown_bond_separates',
             'aggregate_cut_unchanged_iff', 'reinforced_cut_unchanged')
NOTE = (f'K1 added to PreparationCorrespondence a section reading Becoming.Cuts (study section 190; Ren, 19 October '
        f'2026: {GO}); the earlier declarations are unchanged')


def restate(rid, cited_new, note_en, note_zh):
    path = RECORDS / f'{rid}.json'
    r = json.loads(path.read_text())
    for ref in r['references']:
        if ref['path'] == INST:
            ref['sha256'] = sha(INST)
            ref['declarations'] = ref['declarations'] + [d for d in cited_new if d not in ref['declarations']]
        if ref['path'] == INST_CHECKER:
            ref['sha256'] = sha(INST_CHECKER)
    if not any(ref['path'] == inst_receipt for ref in r['references']):
        at = next(k for k, ref in enumerate(r['references']) if ref['path'] == INST) + 1
        r['references'].insert(at, {'path': inst_receipt, 'role': 'receipt', 'sha256': sha(inst_receipt),
                                    'declarations': []})
    for b in r['proof_bindings']:
        if b['source'] == INST:
            b['receipt'] = inst_receipt
    r['history'].append({'en': note_en, 'zh': note_zh})
    r['reviewed_at_utc'] = NOW
    return r


g = restate('growth-constrained-fragmentation', NEW_INST,
            f'19 October 2026, K1: {NOTE}. The example theorems are now cases of general laws: every bond of every '
            f'body grown by division separates its ends when cut (bond_cut_separates, every_grown_bond_separates, by '
            f'Cuts.attached_link_separates), and after one aggregation a grown bond is bypassed exactly where the '
            f'aggregated bond crosses it (aggregate_cut_unchanged_iff, by Cuts.joined_cut_unchanged_iff), the '
            f'reinforced chain being a case (reinforced_cut_unchanged). Instance receipt {inst_id}; the claim and its '
            f'scope are unchanged.',
            f'2026年10月19日，K1：PreparationCorrespondence 新增一节读 Becoming.Cuts（研究第 190 节）。示例定理成为一般规律的情形：'
            f'经分裂生长的每个身体的每条键被切断时两端分开，一次聚合后生长出的键被绕过恰在聚合键跨过它之处，加固链是一例。'
            f'实例回执 {inst_id}；论断与范围不变。')
cuts_ref = {'path': SRC, 'role': 'proof', 'sha256': sha(SRC),
            'declarations': c('attached_link_separates', 'joined_cut_unchanged_iff')}
if not any(ref['path'] == SRC for ref in g['references']):
    g['references'].append(cuts_ref)
    g['references'].append({'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt), 'declarations': []})
    g['proof_bindings'].append({'source': SRC, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Cuts',
                                'success_pointer': '/status', 'success_value': 'passed'})
g['dependencies'].append({
    'id': 'which-links-a-closure-needs', 'relation': 'formal-reuse',
    'detail': {'en': 'Reuses Cuts.attached_link_separates and Cuts.joined_cut_unchanged_iff: the bonds read both ways '
                     'are Cuts.Links, division keeps them grown by attachment, so every grown bond separates its ends '
                     'and the reinforced chain\'s bypass is the join law (PreparationCorrespondence.bond_cut_separates, '
                     'aggregate_cut_unchanged_iff).',
               'zh': '复用 Cuts.attached_link_separates 与 Cuts.joined_cut_unchanged_iff：双向读的键即 Cuts.Links，'
                     '分裂使它们保持依附式生长，所以每条生长出的键都分开其两端，加固链的绕行即连接规律。'}})
for alias in ['Becoming.PreparationCorrespondence.bond_cut_separates',
              'Becoming.PreparationCorrespondence.aggregate_cut_unchanged_iff']:
    if alias not in g['aliases']:
        g['aliases'].append(alias)
(RECORDS / 'growth-constrained-fragmentation.json').write_text(json.dumps(g, ensure_ascii=False, indent=2) + '\n')

m = restate('material-preparation-output', [],
            f'19 October 2026, K1: PreparationCorrespondence re-pointed after reading the change: {NOTE}, the '
            f'declarations this record cites among them. Instance receipt {inst_id}; the claim is unchanged.',
            f'2026年10月19日，K1：读过改动后，PreparationCorrespondence 重新指向：新增一节读 Becoming.Cuts，'
            f'本记录所引声明不变。实例回执 {inst_id}；论断不变。')
(RECORDS / 'material-preparation-output.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n')
print('written', len(cut_decls), 'core declarations;', len(NEW_INST), 'instance declarations')
