"""Record the scoped philosophical assessment; preserve shared chain entries."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
from tools.research import generative_chain as chain

STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
MAIN = 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-LOGIC.md'
REVIEW = STUDY + '/RECOGNITIONAL-BINDING-INTEGRATION.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md'
RECORDS = 'theories/shengsheng-buxi-generative-existence/results/records/'
NEW = RECORDS + 'constitutive-binding-assessment.json'
OLD = RECORDS + 'binding-preserving-substitution.json'

def pair(zh, en): return dict(zh=zh, en=en)
def sha(path): return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
def write(path, data): (ROOT / path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

assert not (ROOT / NEW).exists(), 'One-time migration, not a freshness refresh'
now = datetime.now(timezone.utc).isoformat()
record = dict(
    schema_version=1, id='constitutive-binding-assessment', kind='assessment',
    status='reviewed-scoped', family='F11', reviewed_at_utc=now,
    title=pair('绑定的构成性说明及无前提推广的限度', 'Constitutive binding and the limits of presuppositionless promotion'),
    claim=pair('新引用可由引入活动设立；实际承接及代入在内容与认可要求保持时，解释局部根据传递，无需逐次另加认可命题。这项构成性说明没有证明解释它所用的全部元推理资源均已无前提正当化。',
               'A fresh reference can be instituted by its introduction; actual retention and insertion under unchanged content and assessment explain local support transmission without a fresh endorsement proposition at each use. This account does not justify every metainferential resource used to explain it without presuppositions.'),
    hypotheses=[pair('以当前表达与承接的实际活动为起点；公开使用既有语言、辨认和假设比较，不以新命名保证所有实际接入成功。',
                     'Begins with actual expression and continuation, openly using existing language, identification and hypothetical comparison; fresh designation does not guarantee every uptake.'),
                pair('局部传递保持内容、指定依存与认可要求；假设保证及输入根据的充分性另须成立。',
                     'Local transmission retains content, designated dependence and assessment; the hypothetical guarantee and adequacy of the supplied ground must also hold.')],
    correspondence=pair('引入、承接、辨认和推理根据是同一活动中的不同关系。形式代入刻画给定语言下的求值保持，不直接证明实际指向、历史身份或完整的认识根据。',
                        'Introduction, continuation, recognition and inferential warrant distinguish relations within one activity. Formal substitution characterizes evaluation preservation in the supplied language, not actual reference, historical identity or complete epistemic entitlement.'),
    canonical_source=MAIN, aliases=[],
    dependencies=[dict(id='binding-preserving-substitution', relation='interpretive',
        detail=pair('复用已有代入机制及误接界限；解释性连接不把形式定理升级为构成性奠基证明。', 'Reuses the substitution mechanism and capture bounds; this interpretive connection does not upgrade the theorem into a constitutive grounding proof.'),
        interface=dict(
            output=pair('给定解释下，保留原位置根据的代入保持所有消费者求值；误接及偶然同值控制。', 'Under the supplied interpretation, position-preserving substitution retains every consumer evaluation, with capture and coincident-value controls.'),
            input=pair('局部构成性解释中，生产出的根据怎样继续消费者原指定的依存。', 'How a produced ground continues the consumer’s designated dependence in the local constitutive account.'),
            conditions=pair('语法、绑定解释及认可条件不变；实际角色和推理根据的哲学说明保持独立义务。', 'Syntax, binding interpretation and assessment remain unchanged; the philosophical account of actual roles and warrant remains a separate obligation.'),
            evidence=REVIEW))], related=[],
    counterexamples=[dict(path=REVIEW, detail=pair('保留绑定但采用更严格结论标准的对手；同类型误接、同值遮蔽及不受约束的用语自我担保，分别限制不同推广。', 'Retained binding with a stricter conclusion standard, same-type capture, coincident values and unrestricted constitutive self-certification restrict distinct generalizations.'))],
    limitations=pair('局部论证的完整评估，不是严格无前提元逻辑奠基的完成，也不是其不可能性证明。未建立一般语言、辨认、假设推理和充分根据评估的全套无前提正当性。',
                     'A completed assessment of the local argument, neither completed presuppositionless metalogic nor an impossibility proof. It does not supply comprehensive presuppositionless warrant for language, identification, hypothetical inference and assessment of adequate grounds.'),
    validation_scope=pair('作者实质反审及Carroll、Boghossian原典比较；零新增数学声明。复核三份既有Lean实查回执与源码绑定，未重编，未认领独立验收。',
                         'Author counterreview and primary-source comparison with Carroll and Boghossian; zero new mathematical claims. Checks three existing Lean receipts against their source bindings, without recompilation or independent acceptance.'),
    references=[dict(path=p, role=role, sha256=sha(p), declarations=[]) for p,role in [(MAIN,'statement'),(REVIEW,'review'),(SOURCE,'provenance')]],
    proof_bindings=[],
    next_delta=pair('严格目标仍缺从局部引用构成到本论证所用元推理资源之充分根据的连接；须正面说明此连接，不能重复代入定理或把能够反对等同接受整套逻辑。',
                    'The strict target still lacks the passage from local reference constitution to adequate warrant for the metainferential resources used here; repeating substitution or equating intelligible challenge with acceptance of the entire logic does not supply it.'),
    history=[pair('2026-10-09：迁移并完成既有绑定研究第2、5、7、9节候选的第10节评估；区分设立、执行、辨认和根据，撤下笼统的绑定最终证书要求。不是新的独立数学成果。',
                  '2026-10-09: migrates and completes in section 10 the candidate from sections 2, 5, 7 and 9, distinguishing institution, execution, recognition and warrant and retiring the vague final-certificate demand. Not a new independent mathematical result.')])
write(NEW, record)

p = ROOT / OLD
raw = p.read_bytes()
old = json.loads(raw)
before = json.loads((ROOT / STUDY / 'development/binding-constitution-before/binding-preserving-substitution.json').read_text())
assert old == before, 'Concurrent change requires fresh reconciliation'
for ref in old['references']:
    if ref['path'] in (MAIN, REVIEW, SOURCE): ref['sha256'] = sha(ref['path'])
old['reviewed_at_utc'] = now
old['next_delta'] = record['next_delta']
old['related'].append(dict(id=record['id'], detail=pair('局部构成性解释已完成评估；未证明完整元逻辑无前提根据。本定理的数学声明与实查保持原范围。', 'The local constitutive explanation has been assessed; complete presuppositionless metalogic remains unproved. This theorem and its checks retain their scope.')))
old['history'].append(pair('2026-10-09：阅读并接入构成性评估；只调和三份文档来源、新后继与相关评估。定理、证明绑定及冻结回执未变、未重编。', '2026-10-09: reconciles three read documentary sources, the successor question and related constitutive assessment. Theorems, proof bindings and frozen receipts are unchanged and not recompiled.'))
assert p.read_bytes() == raw
write(OLD, old)

data_raw = chain.DATA.read_bytes()
data = json.loads(data_raw)
data_before = copy.deepcopy(data)
entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'F01')
entry_before = copy.deepcopy(entry)
entry['claim_zh'] += ' 构成性评估现区分引用的设立、执行、辨认与根据：局部承接无需逐次新增认可命题，但不因此获得全部元推理资源的无前提正当性。'
entry['claim_en'] += ' The constitutive assessment now distinguishes institution, execution, recognition and warrant: local retention needs no fresh endorsement proposition per use, but does not thereby justify every metainferential resource without presuppositions.'
entry['scope_zh'] += ' 本次完成的是既有候选的哲学评估，零新增定理、未重编；先前笼统的绑定最终根据问题由具体的元推理推广不足取代。三条推广路线与实质对手已评估；严格目标未完成，也未证明不可能。'
entry['scope_en'] += ' This continuation completes the philosophical assessment of the existing candidate, with zero new theorems or recompilation. The vague ultimate-binding gap is replaced by a specific insufficiency in promotion to metainferential warrant. Three routes and substantive rivals are assessed; the strict target remains unmet, not proved impossible.'
entry['links'].append(dict(path=NEW, label_zh='构成性绑定范围评估', label_en='Scoped constitutive-binding assessment'))
fingerprints = {p:sha(p) for p in (MAIN,REVIEW,SOURCE,OLD,NEW)}
data['reviewed_sources'].update(fingerprints)
old_lines = chain.OUTPUT.read_text().splitlines(keepends=True)
row = next(x for x in chain.render(data).splitlines() if x.startswith('| F01 |'))
old_row = next(x.rstrip('\n') for x in old_lines if x.startswith('| F01 |'))
new_lines = [row+'\n' if x.startswith('| F01 |') else x for x in old_lines]
other_before = [e for s in data_before['sections'] for e in s['entries'] if e['id'] != 'F01']
other_after = [e for s in data['sections'] for e in s['entries'] if e['id'] != 'F01']
assert other_before == other_after
assert chain.DATA.read_bytes() == data_raw and chain.OUTPUT.read_text().splitlines(keepends=True) == old_lines
chain.DATA.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
chain.OUTPUT.write_text(''.join(new_lines))

maintenance = STUDY + '/GENERATIVITY-CHAIN-INDEX-RECORD.md'
fragment = '**绑定的构成性根据 / Constitutive binding，2026-10-09。** F01接入[既有候选的完整评估](RECOGNITIONAL-BINDING-INTEGRATION.md#constitutive-binding-assessment)：区分引用设立、实际承接、辨认与推理根据，保留强目标。/ The local account needs no fresh endorsement proposition at every use; promotion to comprehensive presuppositionless metainferential warrant remains unsupported. Zero new mathematics or recompilation. [Owned edits](BINDING-CONSTITUTION-INDEX-EDITS.json) preserve other entries; [scoped evidence checks](BINDING-CONSTITUTION-CHECKS.json) verify unchanged prior receipts without certifying the full table.\n\n'
mp = ROOT / maintenance
mr = mp.read_text()
assert fragment not in mr
head,rest = mr.split('\n\n',1)
assert mp.read_text() == mr
mp.write_text(head+'\n\n'+fragment+rest)
write(STUDY+'/BINDING-CONSTITUTION-INDEX-EDITS.json', dict(
    entry_before=entry_before, entry_after=entry, old_rendered_row=old_row, new_rendered_row=row,
    other_entries_preserved=True, other_rendered_lines_preserved=True, discovery_unchanged=True,
    authored_fingerprints=fingerprints, shared_fragments=[dict(path=maintenance,text=fragment,insertion_only=True)],
    new_theorems=0, complete_presuppositionless_grounding=False))
print(json.dumps(dict(record=NEW,prior_theorem_unchanged=True,paired_entry='F01',new_theorems=0)))
