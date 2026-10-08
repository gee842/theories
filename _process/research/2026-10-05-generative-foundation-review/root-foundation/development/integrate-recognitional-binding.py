import copy,hashlib,importlib.util,json
from pathlib import Path
r=Path('/Users/ren/theories');s=r/'_process/research/2026-10-05-generative-foundation-review/root-foundation';l=r/'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
def sha(raw):return hashlib.sha256(raw).hexdigest()
previous=json.loads((s/'REFLECTIVE-IDENTITY-INDEX-EDITS.json').read_text())
fragments=[
'**指回关系与同一规则 / Binding and identity，2026-10-08。** [本轮论证及反审](_process/research/2026-10-05-generative-foundation-review/root-foundation/RECOGNITIONAL-BINDING-INTEGRATION.md)区分构成共同指向与经验再辨认；明确语法中无来源、无周围假设的原子型 A → A 项只能返回所给根据。7项新定理／21项含继承审计全空。/ Source-free transport and atomic endomorphism uniqueness are checked, with ambient/source controls. Binding interpretation and full presuppositionless grounding remain open; existing logical-relations work is credited.\n\n',
'**由绑定说明同一 / Identity through binding，2026-10-08。** [第14节](unified-2026-10-05/GENERATED-LOGIC.md#recognitional-binding)推进共同指向的构成性解释，7项新定理／21项含继承审计全空。/ Every closed source-free atomic endomorphism in the supplied language retains its argument; grammar, evaluation and actual correspondence remain explicit. Full grounding and novelty are not claimed.\n\n',
'**指回关系的接续 / Binding continuation，2026-10-08。** [论证、主来源及反审](RECOGNITIONAL-BINDING-INTEGRATION.md)以既有语言检查无来源传递、原子恒等唯一性及两个替代；7项新定理／21项含继承审计全空。/ The local structural connection is complete; actual binding and hypothetical substitution remain the foundational bridge.\n\n',
'**Recognitional binding, 8 October 2026.** [RecognitionalBinding.lean](RecognitionalBinding.lean) and [checker](check_recognitional_binding.py) check source-free logical relations, closed atomic identity uniqueness, absence of closed atomic grounds and ambient/source alternatives. Seven new theorem audits plus 14 inherited declaration audits are all empty. The syntax and evaluation remain supplied; [integration](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECOGNITIONAL-BINDING-INTEGRATION.md) distinguishes the constitutive candidate from full grounding.\n\n',
'**构成共同指向 / Constituted coreference，2026-10-08。** F01成对接入[绑定、唯一性及反审](RECOGNITIONAL-BINDING-INTEGRATION.md)，7项新定理／21项含继承审计全空。/ Only the owned F01 suffix and links, five read/authored versions and one discovery page change; concurrent entry text, other rows and pending reviews remain. [Edits](RECOGNITIONAL-BINDING-INDEX-EDITS.json); [checks](RECOGNITIONAL-BINDING-CHECKS.json). No whole-table, independent or complete presuppositionless certification.\n\n'
]
owned=[]
for old,text in zip(previous['shared_fragments'],fragments):
 p=r/old['path'];before=p.read_text();anchor=old['text'];assert before.count(anchor)==1;assert text not in before
 after=before.replace(anchor,text+anchor,1);assert after.replace(text,'',1)==before;p.write_text(after)
 owned.append(dict(path=old['path'],text=text,before_sha256=sha(before.encode()),after_sha256=sha(after.encode()),insertion_only=True))
spec=importlib.util.spec_from_file_location('chain',s/'build_generative_chain.py');chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
raw=chain.DATA.read_bytes();d=json.loads(raw);before=copy.deepcopy(d)
e=next(e for sec in d['sections'] for e in sec['entries'] if e['id']=='F01');eb=copy.deepcopy(e)
e['claim_zh']+=' 接续区分由引入／使用构成的共同指向与经验再辨认；给定有限语法中，无来源、无周围假设的原子型 A → A 项必定返回所给根据。'
e['claim_en']+=' A continuation distinguishes constituted binding from independent reidentification: every closed source-free atomic endomorphism in the supplied finite language returns its argument.'
e['scope_zh']+=' 新7项定理／21项含继承声明审计均空；继承14项不重计为新。关系保持由语法归纳得到；额外上下文或来源各有替代输入的见证。use解释、语法及元理论仍给定，实际绑定与假设代入的最终根据未证；非全体复合类型或任意程序的唯一性，不宣称新颖性。'
e['scope_en']+=' Seven new theorems / 21 total declaration audits are empty, including 14 inherited audits. Relation preservation follows by syntax induction; ambient and introduced grounds give controls. Context-use interpretation, syntax and metatheory remain supplied; actual binding and hypothetical-substitution warrant remain open. The uniqueness scope is atomic terms, not all compound types or arbitrary programs; no novelty claim.'
proof=l/'recognitional-binding-checks/20261008T120159.334011Z/receipt.json';study=s/'RECOGNITIONAL-BINDING-INTEGRATION.md'
for p,zh,en in [(study,'绑定论证及反审','Binding argument and counterreview'),(l/'RecognitionalBinding.lean','无来源传递与恒等唯一性','Source-free transport and identity uniqueness'),(proof,'绑定审计冻结回执','Frozen binding audit receipt')]:e['links'].append(dict(path=str(p.relative_to(r)),label_zh=zh,label_en=en))
owned_paths=[r/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-LOGIC.md',r/'sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md',study,l/'RecognitionalBinding.lean',proof]
fingerprints={str(p.relative_to(r)):sha(p.read_bytes()) for p in owned_paths};d['reviewed_sources'].update(fingerprints)
discovery=str(study.relative_to(r));assert discovery not in d['known_discovery_paths'];d['known_discovery_paths'].append(discovery);d['known_discovery_paths'].sort()
oldtext=chain.OUTPUT.read_text();oldrow=next(x for x in oldtext.splitlines() if x.startswith('| F01 |'));assert oldrow==next(x for x in chain.render(before).splitlines() if x.startswith('| F01 |'))
newrow=next(x for x in chain.render(d).splitlines() if x.startswith('| F01 |'));newtext=oldtext.replace(oldrow,newrow,1);assert newtext.replace(newrow,oldrow,1)==oldtext
others=lambda data:[e for sec in data['sections'] for e in sec['entries'] if e['id']!='F01'];assert others(d)==others(before)
assert chain.DATA.read_bytes()==raw;assert chain.OUTPUT.read_text()==oldtext
chain.DATA.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');chain.OUTPUT.write_text(newtext)
edits=dict(scope='Only owned F01 additions, paired rendering, five authored/read hashes and one discovery page; prior and concurrent content retained',shared_fragments=owned,entry_before=eb,entry_after=e,other_entries_preserved=True,old_rendered_row=oldrow,new_rendered_row=newrow,other_rendered_lines_preserved=True,authored_fingerprints=fingerprints,owned_discovery_paths=[discovery])
(s/'RECOGNITIONAL-BINDING-INDEX-EDITS.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print('Integrated five navigation fragments and only F01; preserved all other entries and rendered lines.')
