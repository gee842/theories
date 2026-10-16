from pathlib import Path
import copy,hashlib,json,sys
r=Path('/Users/ren/theories');sys.path.insert(0,str(r));from tools.research import generative_chain as chain
s=r/'_process/research/2026-10-05-generative-foundation-review/root-foundation';l=r/'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
def sha(b):return hashlib.sha256(b).hexdigest()
def rel(p):return str(p.relative_to(r))
proof=r/json.loads((l/'inferential-substitution-verification.json').read_text())['receipt'];study=s/'RECOGNITIONAL-BINDING-INTEGRATION.md';record=r/'theories/shengsheng-buxi-generative-existence/results/records/binding-preserving-substitution.json'
raw=chain.DATA.read_bytes();d=json.loads(raw);old=copy.deepcopy(d);e=next(e for sec in d['sections'] for e in sec['entries'] if e['id']=='F01');before=copy.deepcopy(e)
e['claim_zh']+=' 代入接续构造嵌套绑定中的替换：全部消费者求值保真，当且仅当各替换项供给原位置的根据；单假设代入及先后组合由此接通。'
e['claim_en']+=' Constructed substitution under nested binders preserves evaluation for every consumer exactly when each replacement supplies its original position ground; single insertion and successive composition are connected.'
e['scope_zh']+=' 再增9项定理／19项含继承审计，13空、6仅Quot.sound；同类型误接可改答案，同值可掩盖误接。有限语法、绑定解释、假设保证及实际输入满足公开；求值同一不独自给出完整意义／来源同一，无前提元逻辑仍未完成。'
e['scope_en']+=' Nine further theorems / 19 total audits: 13 empty, 6 only Quot.sound. Same-type capture can change answers; coincident values can conceal it. Finite grammar, binding interpretation, hypothetical guarantees and satisfied input criteria remain explicit. Denotational agreement alone does not identify full content or provenance; presuppositionless metalogic remains unfinished.'
for p,zh,en in [(record,'代入精确判据成果','Canonical substitution criterion'),(l/'InferentialSubstitution.lean','嵌套代入与误接边界','Nested substitution and capture controls'),(proof,'代入实查冻结回执','Frozen substitution receipt')]:e['links'].append(dict(path=rel(p),label_zh=zh,label_en=en))
paths=[r/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-LOGIC.md',r/'sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md',study,l/'InferentialSubstitution.lean',proof,record]
fingerprints={rel(p):sha(p.read_bytes()) for p in paths};d['reviewed_sources'].update(fingerprints)
oldtext=chain.OUTPUT.read_text();oldrow=next(x for x in oldtext.splitlines() if x.startswith('| F01 |'));assert oldrow==next(x for x in chain.render(old).splitlines() if x.startswith('| F01 |'));newrow=next(x for x in chain.render(d).splitlines() if x.startswith('| F01 |'));newtext=oldtext.replace(oldrow,newrow,1)
others=lambda d:[e for sec in d['sections'] for e in sec['entries'] if e['id']!='F01'];assert others(d)==others(old);assert newtext.replace(newrow,oldrow,1)==oldtext
assert chain.DATA.read_bytes()==raw and chain.OUTPUT.read_text()==oldtext
chain.DATA.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');chain.OUTPUT.write_text(newtext)
p=s/'GENERATIVITY-CHAIN-INDEX-RECORD.md';oldnote=p.read_text();fragment='**保留绑定的假设代入 / Binding-preserving substitution，2026-10-09。** F01接续[现有绑定研究第9节](RECOGNITIONAL-BINDING-INTEGRATION.md#binding-preserving-substitution)：9项新定理／19项含继承审计，13空、6仅Quot.sound；误接与偶然同值边界保留。/ One canonical result drives generated navigation. Only the owned F01 additions, three links and six read/authored source versions change; other entries, rows and pending reviews remain. [Owned edits](INFERENTIAL-SUBSTITUTION-INDEX-EDITS.json); [scoped checks](INFERENTIAL-SUBSTITUTION-CHECKS.json). No full-table or complete presuppositionless certification.\n\n';cut=oldnote.index('\n\n')+2;newnote=oldnote[:cut]+fragment+oldnote[cut:];assert newnote.replace(fragment,'',1)==oldnote;p.write_text(newnote)
edits=dict(scope='Owned substitution additions only; generated overview pages are rendered through canonical records',entry_before=before,entry_after=e,old_rendered_row=oldrow,new_rendered_row=newrow,other_entries_preserved=True,other_rendered_lines_preserved=True,authored_fingerprints=fingerprints,discovery_unchanged=d['known_discovery_paths']==old['known_discovery_paths'],shared_fragments=[dict(path=rel(p),text=fragment,before_sha256=sha(oldnote.encode()),after_sha256=sha(newnote.encode()),insertion_only=True)])
(s/'INFERENTIAL-SUBSTITUTION-INDEX-EDITS.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
(s/'INFERENTIAL-SUBSTITUTION-CHECKS.json').write_text('{"status":"pending scoped integration checks"}\n')
print('Maintained only F01 and read/authored versions; retained all other chain rows and pending reviews.')
