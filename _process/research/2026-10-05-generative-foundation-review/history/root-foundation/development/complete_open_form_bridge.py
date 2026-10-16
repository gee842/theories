"""Historical one-shot P89 record update, applied on adf335a8 on 13 October 2026.

Preserved for provenance. This records the update before the final study receipt
paragraph; final hashes are maintained by the canonical records. Do not rerun:
the original receipt assertions and additive edits intentionally are not an
idempotent maintenance interface.
"""
raise SystemExit("Historical applied procedure; inspect only, do not rerun.")

from pathlib import Path
import json, hashlib, subprocess
from datetime import datetime, timezone
ROOT=Path('/Users/ren/theories')
BASE='adf335a8'
records=ROOT/'theories/becoming/results/records'
core='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
bridge=core+'Becoming/Bridge.lean'
receipt=core+'becoming-verification.json'
periphery='experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-inquiry-verification.json'
study='_process/research/2026-10-05-generative-foundation-review/root-foundation/RISK-CONDITIONING-INTEGRATION.md'
choice='theories/becoming/chapters/CHOICE-AND-GENERATIVE-CONTEXT.md'
chapter='theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
now=datetime.now(timezone.utc).isoformat()
def pair(zh,en):return {'zh':zh,'en':en}
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def ref(p,role,names=[]):return {'path':p,'role':role,'sha256':sha(p),'declarations':names}
# Freeze unchanged evidence at its original, already retained bytes. Never rewrite a receipt.
old_receipts={}
for p in [receipt,periphery]:
 raw=subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
 d=json.loads(raw); frozen=str(Path(p).parent/d['retained_run']/'verification.json')
 assert (ROOT/frozen).read_bytes()==raw,(p,'retained receipt differs')
 old_receipts[p]=(frozen,hashlib.sha256(raw).hexdigest())
checked=json.loads((ROOT/receipt).read_text());assert checked['status']=='passed'
new_receipt=str(Path(receipt).parent/checked['retained_run']/'verification.json')
assert (ROOT/new_receipt).read_bytes()==(ROOT/receipt).read_bytes()
assert sha(bridge)==checked['source_sha256']['Becoming.Bridge']
names=['Becoming.Run.novel_by_handoff','Becoming.Run.relevance_by_handoff_of_unrestricted','Becoming.positive_ground_by_bound_of_unrestricted','Becoming.revised_generation_by_bound_of_unrestricted']
m=next(m for m in checked['modules'] if m['module']=='Becoming.Bridge')
for n in names:assert m['axiom_dependencies'][n]==[]
changed=[]; affected=[]; receipt_pins=[]
for f in sorted(records.glob('*.json')):
 original=f.read_text(); d=json.loads(original); ident=d['id']
 has_bridge=any(r['path']==bridge for r in d['references'])
 pins=[]; document_delta=[]
 for r in d['references']:
  if r['path'] in old_receipts:
   old=r['path'];frozen,h=old_receipts[old];assert r['sha256']==h,(ident,old,'unexpected receipt version')
   r['path']=frozen;r['sha256']=h;pins.append(old)
  if r['path'] in [bridge,study,choice,chapter] and r['sha256']!=sha(r['path']):
   document_delta.append(r['path']);r['sha256']=sha(r['path'])
 for b in d.get('proof_bindings',[]):
  if b['receipt'] in old_receipts:
   b['receipt']=new_receipt if b['source']==bridge else old_receipts[b['receipt']][0]
 if has_bridge:
  d['references'].append(ref(new_receipt,'receipt'))
  d['validation_scope']['zh']+=' P89（2026-10-13）：Bridge 的旧声明保持，四项新增适配已实查且公理报告为空；本记录的 Bridge 绑定转到本次冻结回执，其余既有证明保留各自原回执，不将适配另计为独立成果。'
  d['validation_scope']['en']+=' P89 (13 October 2026): prior Bridge declarations remain; four added adapters are checked with empty axiom reports. This record binds Bridge to the new frozen receipt while other proofs retain their original receipts; adapters are not independent results.'
  affected.append(ident)
 if ident=='open-form-realization-under-revision':
  d['claim']['zh']+=' P89 已在共同 Frame／Run 上陈述，并以实际 Lean 调用把原 G0 条件实例化为统一理论从意义取得的正面相关；原有限实现与失败范围不变。'
  d['claim']['en']+=' P89 states the result on the shared Frame/Run and checks the exact instance of the inherited G0 condition using relevance read from significance; the finite-realization and failure scopes are unchanged.'
  d['hypotheses'][1]=pair('完成事件对应同一历史中新形成的真实生成内容；不同历史允许不同内容。历史一般形式以 G0 为显式条件；P89 的统一实例从 Unrestricted 取得 G0，意义条件不由进展证书推导。','Completion corresponds to actual newly formed generative content in the same history, with different content allowed across histories. The historical generic form takes explicit G0; P89 derives its instance from Unrestricted, whose significance condition is not derived from progress.')
  d['aliases']+=names
  d['references'] += [ref(bridge,'proof',names),ref(new_receipt,'receipt')]
  d['proof_bindings'].append({'source':bridge,'receipt':new_receipt,'sha256_pointer':'/source_sha256/Becoming.Bridge','success_pointer':'/status','success_value':'passed'})
  d['dependencies'].append({'id':'one-axiom-yields-g0','relation':'formal-reuse','detail':pair('P89 调用 inventory_g0_of_unrestricted 与 g0_of_unrestricted，补齐旧正面根据的正式实例与共同运行上的形式。','P89 calls inventory_g0_of_unrestricted and g0_of_unrestricted to complete the exact old positive-ground instance and its form on a shared run.'),'interface':{'output':pair('从意义读出的正面相关在 Unrestricted 条件下满足 G0。','Relevance read from significance satisfies G0 under Unrestricted.'),'input':pair('原 positive_ground_by_bound 所需的 G0，以及共同 Frame 中新实现取得 relevance 的条件。','The G0 premise of the original positive_ground_by_bound and the premise giving relevance to novel realization in the shared Frame.'),'conditions':pair('同一有界清单、同一新形成见证、原执行与交接条件；Unrestricted 保持显式。','The same bounded inventory and novel witness, the inherited execution and handoff conditions, with Unrestricted explicit.'),'evidence':bridge}})
  for other,zh,en in [('formed-goal-revision-continuation','已给出有比较根据的目的改变及实际接续，不再列为一般缺口。','Already supplies comparatively warranted end revision and actual continuation; not a generic missing connection.'),('acquired-revision-of-pending-task','已有在途工作改写，原历史损失与支持成本保留。','Existing pending-task rewriting retains historical loss and support costs.'),('pending-task-context-applicability','已有作用前复查；任务保留仍不等于需求满足，具体应用另审。','Existing pre-action checking retains its scope; keeping a task is not satisfying the need, and concrete applications require review.')]:
   d['related'].append({'id':other,'detail':pair(zh,en)})
  d['validation_scope']['zh']+=' P89（2026-10-13）：共享检查器核查四项适配、全部空公理依赖；Bridge 共48项定理／66项源声明审计，75个包模块共4522项定理／6374项审计，另列24个继承模块；77个纯净核心模块的字节及空公理范围保持，实际运行5个Lean步骤、复用348个。无新独立成果或独立验收。'
  d['validation_scope']['en']+=' P89 (13 October 2026): the shared checker verifies four adapters, all axiom-free. Bridge has 48 theorems/66 source declaration audits; 75 package modules have 4522 theorems/6374 audits, with 24 inherited modules separate. The 77 pure core modules retain their bytes and empty-axiom scope; 5 Lean steps ran and 348 were reused. No new independent result or independent acceptance.'
  d['next_delta']=pair('本条的通用有限实现及正式脊柱连接已完成；直接复用既有目的修订、在途改写和复查成果。只有具名实际案例的新需求、有效承担与作用对应才另作应用研究。NP、混合得失排序及更强规范根据不被此结项宣布解决，归统一研究范围。','The generic finite realization and formal spine connection are complete. Reuse acquired-goal revision, pending-task rewriting and applicability checks. Further application work must name a concrete need, undertaking or effect correspondence. NP, mixed-loss ordering and stronger normative warrant remain in the unified programme and are not settled by this closure.')
  d['history'].append(pair('2026-10-13 P89：四项共享桥接适配关闭此前仅有审计说明的连接；已完成的通用目的修订待做项撤出。沿用本成果身份，原定理、反例、历史回执及实际对应限制保留。','13 October 2026, P89: four shared adapters close the previously audit-only connection; completed generic goal-revision work is removed from next steps. The result identity, original theorems, counterexamples, historical receipts and correspondence limits remain.'))
  d['reviewed_at_utc']=now
 if ident=='one-axiom-yields-g0':
  for item in d.get('related',[]):
   if item['id']=='open-form-realization-under-revision':item['detail']=pair('P89 已在 Bridge 写出并检查其正面根据的实例化及完整生成组合，并提供共同 Frame／Run 上的形式；详见该既有成果。','P89 now checks its positive-ground instance and complete generation composition in Bridge, also supplying the shared Frame/Run form; see the existing result.')
  d['limitations']['zh']=d['limitations']['zh'].replace('ProtectionPriorityRival、OpenFutureRevision 与 RenewingFormation 以同一实例化成立而未写成 Lean','ProtectionPriorityRival 与 RenewingFormation 以同一实例化成立而未写成 Lean；OpenFutureRevision 的专门 Lean 适配已由 P89 补齐')
  d['limitations']['en']=d['limitations']['en'].replace('ProtectionPriorityRival, OpenFutureRevision and RenewingFormation hold by the same instantiation without Lean','ProtectionPriorityRival and RenewingFormation hold by the same instantiation without Lean; P89 now supplies the dedicated checked OpenFutureRevision adapters')
  d['history'].append(pair('2026-10-13 P89：更新 OpenFutureRevision 的当前接入状态；公理本身、A/J 及其他未写适配的范围不变。','13 October 2026, P89: updates the current OpenFutureRevision connection; the axiom, A/J and other unwritten adapters keep their scopes.'))
  d['reviewed_at_utc']=now
 if ident=='becoming-spine-instances':
  d['claim']['zh']+=' P89：开放形态有限实现直接作用于共同 Frame 的 Run，同一个新形成见证在显式意义条件下取得 relevance；另两项旧接口适配完成原生成生产端到正面根据消费端的组合。'
  d['claim']['en']+=' P89: bounded open-form realization applies to a Run of the shared Frame, and the same novel witness receives relevance under the explicit significance condition; two inherited-interface adapters complete the generation-to-positive-ground composition.'
  d.setdefault('related',[]).append({'id':'open-form-realization-under-revision','detail':pair('四项适配归该既有结果，不新增成果身份；桥接内声明已检查。','The four checked adapters belong to that existing result, with no new result identity.')})
  d['reviewed_at_utc']=now
 if document_delta or pins:
  d['history'].append(pair('2026-10-13 P89 来源维护：仅核对本轮追加桥接／完成说明的源文差异；未变证明所用的可变汇总回执固定到原有同字节冻结版本。除本记录明示的 P89 接入外，原科学范围与反例不变。','13 October 2026, P89 source maintenance: reviewed only the appended bridge/closure source delta; mutable receipt references for unchanged proofs are pinned to their existing byte-identical frozen versions. Except for an explicitly stated P89 connection in this record, scientific scope and counterexamples are unchanged.'))
 new=json.dumps(d,ensure_ascii=False,indent=2)+'\n'
 if new!=original:f.write_text(new);changed.append(ident)
 if pins:receipt_pins.append(ident)
print(json.dumps({'changed_records':len(changed),'bridge_source_reconciled':affected,'unchanged_evidence_pinned_records':len(receipt_pins),'new_receipt':new_receipt},ensure_ascii=False))
