#!/usr/bin/env python3
"""Fresh source-bound kernel correspondence; no native producer is executed.

Reuses the preceding formal checkers only for serialization, lexical audit and
compiler-log parsing. Their unchanged bytes and prior receipts are preserved.
"""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
STUDY=HERE.parent
FEEDBACK=STUDY.parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').is_file())
PRIOR=FEEDBACK/'calibration-revision/formal'
spec=importlib.util.spec_from_file_location('calibration_formal_serializer',PRIOR/'check.py')
cal=importlib.util.module_from_spec(spec);spec.loader.exec_module(cal)
helper=cal.helper
sha,tick,b,opt,pair,ls,datum=(getattr(helper,n) for n in ('sha','tick','b','opt','pair','ls','datum'))
LEAN,CORE=helper.LEAN,helper.CORE
RESULT=STUDY/'results.json'; INDEPENDENT=STUDY/'independent-check.json'
PHASE={'absent':'.absent','reference_formation':'.referenceFormation','ready':'.ready',
       'unresolved':'.unresolved','active':'.active'}

def table(xs):
    assert len(xs)==2 and all(x in (0,1) for x in xs)
    return '⟨'+b(xs[0])+', '+b(xs[1])+'⟩'

def config(case):
    p=case['parameters'];fault=lambda x: '.faithful' if x is None else helper.FAULTS[x]
    return ('{referenceMap := '+table(p['transducer'])+', initialUseMap := '+table(p['use_map'] or p['transducer'])+
      ', referenceFaults := '+pair(p['reference_faults'],fault)+', misforce := '+b(p['misforce'])+
      ', formationClamp := '+b(p['policy']=='formation_clamped')+', rawClamp := '+b(p['policy']=='raw_clamped')+'}')

def state(s,parent,cfg):
    original=s['controller']['phase'];t=deepcopy(s)
    if original=='reference_formation': t['controller']['phase']='old_interface'
    encoded=cal.encode_state(t,parent,'{}')
    body=encoded.split(', body := ',1)[1][:-1]
    r=s['recipe']
    recipe=('{wires := '+pair(r['wires'],lambda x:opt(x,b))+
        ', references := '+pair(r['references'],datum)+', issued := '+opt(r['issued'],b)+
        ', jig := '+opt(r['jig'],b)+', contact := '+datum(r['contact'])+
        ', ready := '+b(r['ready'])+', conflict := '+b(r['conflict'])+', cursor := '+str(r['cursor'])+
        ', activated := '+b(r['activated'])+', address := '+opt(r['address'],b)+', phase := '+PHASE[r['phase']]+'}')
    return ('{parent := '+parent+', config := '+cfg+', body := '+body+', recipe := '+recipe+
      ', useMap := '+table(s['physical_transducer']['use_map'])+
      ', referenceFormation := '+b(original=='reference_formation')+'}')

def event(kind,detail,before):
    names={'decoder_assembly':'.assemble','reader_readiness':'.readiness','activate_calibration':'.activate',
           'formed_decoder_read':'.decode','unbind_decoder_row':'.unbind','transducer_boundary_change':'.boundaryChange'}
    if kind in names:return names[kind]
    names={'reference_force':'force','reference_contact':'contact','reference_record':'recordReference','bind_decoder_row':'bindRow'}
    if kind in names:return '(.'+names[kind]+' '+b(detail.get('setting',before['recipe']['cursor']))+')'
    return cal.operation(kind,detail,before)

def arguments(kind,detail,before):
    live=before['account']['live']
    prices={'decoder_assembly':(26,60,8,65536,0),'reference_force':(1,live,2,16384,0),
      'reference_contact':(0,live,2,16384,0),'reference_record':(1,live,2,0,2),
      'bind_decoder_row':(1,live,2,0,1),'reader_readiness':(2,live,2,0,1),
      'activate_calibration':(16,live,2,0,16),'formed_decoder_read':(1,live,1,0,0),
      'unbind_decoder_row':(1,live,1,0,1)}
    return prices[kind] if kind in prices else cal.arguments(kind,detail,before)

def generate(results):
    out=['import RecipeNative','namespace RecipeSaved','open RecipeNative',
         'set_option maxRecDepth 65536','set_option maxHeartbeats 12000000']
    names=[];rows=[];charges=denials=requests=boundary=0
    def theorem(name,statement,proof='by decide'):
        names.append(name);out.append('theorem '+name+' :\n  '+statement+' := '+proof+'\n')
    for name,parent in results['parents'].items():
        cfg='parent_'+name+'_config'
        out.append('def '+cfg+' : RemainingDependency.Config := '+helper.config(parent))
        out.append('def parent_'+name+' : RemainingDependency.State := '+helper.state(parent['final'],cfg))
    for name,constant in [('calibration_break','mismatchParent'),('false_dependence','oldReportErrorParent'),('law_01_learned','positiveParent')]:
        theorem('parent_'+name+'_prior_construction','parent_'+name+' = CalibrationRevision.'+constant)
    masks={}
    for case in results['cases']:
        for e in case['trace']:
            mask=e['state']['controller']['mask']
            if mask is not None:masks[cal.encode_mask(mask)]=mask
    for code,mask in sorted(masks.items()):
        theorem('mask_'+str(code),'(List.range 16).map ('+str(code)+' : Nat).testBit = '+ls(mask,b))
    for case in results['cases']:
        name=case['name'];assert re.fullmatch('[a-z][a-z0-9_]*',name)
        cfg=name+'_config';parent='parent_'+case['parameters']['parent']
        out.append('def '+cfg+' : Config := '+config(case))
        trace=case['trace'];old=results['parents'][case['parameters']['parent']]['final']
        assert trace[0]['kind']=='entrance' and trace[-1]['state']==case['final']
        for i,e in enumerate(trace):
            s=e['state'];assert s['inherited']==old['inherited'] and s['old_controller']==old['controller']
            for k in ('source','load','waste','context','test_law','full_law'):assert s['native'][k]==old['native'][k]
            assert s['physical_transducer']['reference_map']==case['parameters']['transducer']
            out.append('def '+name+'_s'+str(i)+' : State := '+state(s,parent,cfg))
        theorem(name+'_entrance','entrance '+parent+' '+cfg+' = '+name+'_s0')
        inherited=tick(case['inherited_consumption'])
        def whole(s):return str(inherited)+' + total '+s+' + '+s+'.body.stocks.total * RemainingDependency.ticks'
        theorem(name+'_initial_account',whole(name+'_s0')+' = 145 * RemainingDependency.ticks')
        plan=[]
        for i in range(1,len(trace)):
            e=trace[i];before=trace[i-1]['state'];kind=e['kind'];detail=e['detail']
            s=name+'_s'+str(i-1);t=name+'_s'+str(i)
            if kind=='denied':
                denials+=1;assert e['charge'] is None
                why=detail['reason']
                if why=='entrance_not_retained_full_operation':
                    guard='('+s+'.parent.body.retained = false ∨ '+s+'.parent.body.mode ≠ .serviceIssued ∨ '+s+'.parent.body.selected = none ∨ '+s+'.body.stocks.source ≠ 0)'
                elif why=='decoder_unresolved':guard=s+'.recipe.ready = false'
                elif why=='decoder_row_unavailable':
                    guard='(∃ address, '+s+'.recipe.address = some address ∧ '+s+'.recipe.wires.get address = none) ∧ '+s+'.body.contact = none'
                    address=before['recipe']['address'];assert address is not None
                    proof='by\n  refine ⟨⟨'+b(address)+', by decide, by decide⟩, by decide, by decide⟩'
                    theorem(name+'_event_'+str(i),guard+' ∧ '+s+' = '+t,proof)
                    continue
                else:
                    reason,operation=why.split(':');assert reason in ('funding','capacity')
                    ev=event(operation,{},before);args=' '.join(map(str,arguments(operation,{},before)))
                    guard='(RemainingDependency.charge '+s+'.body.account '+args+').2 = .'+reason
                    theorem(name+'_event_'+str(i),guard+' ∧ step '+s+' '+ev+' = '+t)
                    plan.append(ev);requests+=1;continue
                theorem(name+'_event_'+str(i),guard+' ∧ '+s+' = '+t);continue
            ev=event(kind,detail,before)
            if kind=='transducer_boundary_change':
                boundary+=1;assert e['charge'] is None
                theorem(name+'_event_'+str(i),'step '+s+' '+ev+' = '+t)
            else:
                charges+=1;q=e['charge'];assert q and q['kind']==kind and q['workspace']==0
                args=arguments(kind,detail,before)
                assert (q['work'],q['live'],q['temporary'],tick(q['extra']),q['rewrites'])==args
                assert q['peak']==max(before['account']['live'],args[1])+args[2]
                assert Fraction(q['fuel'])==Fraction(e['state']['account']['fuel'])
                args=' '.join(map(str,args))
                theorem(name+'_event_'+str(i),'step '+s+' '+ev+' = '+t+
                    ' ∧ RemainingDependency.tariff '+s+'.body.account '+args+' = '+str(tick(q['bill']))+
                    ' ∧ (RemainingDependency.charge '+s+'.body.account '+args+').2 = .none')
            plan.append(ev);requests+=1
        word='['+', '.join(plan)+']';end=name+'_s'+str(len(trace)-1)
        theorem(name+'_saved_run','run '+name+'_s0 '+word+' = '+end)
        theorem(name+'_core_trace','Generative.Trace process '+name+'_s0 '+word+' '+end,
                'by\n  rw [← '+name+'_saved_run]\n  exact run_is_core_trace _ _')
        theorem(name+'_final_account',whole(end)+' = 145 * RemainingDependency.ticks')
        if case['parameters']['policy'] in ('learned','conventional') and case['name'].startswith(('positive_identity_','positive_inversion_','mismatch_identity_','mismatch_inversion_','old_report_error_identity_','old_report_error_inversion_')):
            tm=table(case['final']['recipe']['wires']);ref=table(case['parameters']['transducer'])
            theorem(name+'_actual_formed_decoder','decoder '+end+'.recipe = some '+tm+' ∧ RecipeGrounding.Recovers ('+ref+' : RecipeGrounding.Table).read '+tm,
                    'by\n  constructor\n  · decide\n  · intro input; cases input <;> decide')
        rows.append(dict(name=name,states=len(trace),event_attempts=len(plan),status=case['status'],retention_status=case['retention_status']))
    out.extend('#print axioms '+n for n in names);out.append('end RecipeSaved\n')
    return '\n'.join(out),dict(case_count=len(rows),cases=rows,state_count=sum(r['states'] for r in rows),
       saved_edges=sum(r['states']-1 for r in rows),event_attempts=requests,charged_events=charges,
       denied_events=denials,uncharged_boundary_changes=boundary,parent_construction_equalities=3,
       mask_encoding_equalities=len(masks),theorem_count=len(names))

def audit_source(source,namespace,inherited=False):
    code=helper.remove_comments_and_strings(source)
    assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b|^\s*axiom\b',code,re.M)
    assert set(re.findall(r'^import\s+(\S+)\s*$',code,re.M)) <= {'Std','GenerativeCore','RemainingDependency','CalibrationRevision','RecipeGrounding','RecipeNative'}
    declared=re.findall(r'^theorem\s+(\w+)\b',code,re.M)
    audits=re.findall(r'^#print axioms\s+([\w.]+)\s*$',code,re.M)
    assert len(audits)==len(set(audits))
    if not inherited:assert declared==audits
    return [namespace+'.'+n if '.' not in n else n for n in audits]

def main():
    assert sha(LEAN)==helper.LEAN_SHA
    version=subprocess.check_output([str(LEAN),'--version'],text=True).strip();assert '4.29.1' in version
    assert (HERE/'lean-toolchain').read_text()=='leanprover/lean4:v4.29.1\n'
    results=json.loads(RESULT.read_text());review=json.loads(INDEPENDENT.read_text())
    assert review['status']=='passed' and review['results_sha256']==sha(RESULT)
    old=json.loads((PRIOR/'verification.json').read_text());assert old['status']=='passed'
    inherited_modules=[('GenerativeCore',CORE,'Generative',True),
       ('RemainingDependency',cal.OLD/'RemainingDependency.lean','RemainingDependency',True),
       ('CalibrationRevision',PRIOR/'CalibrationRevision.lean','CalibrationRevision',True)]
    for _,path,_,_ in inherited_modules:assert sha(path)==old['source_hashes'][str(path.relative_to(ROOT))]
    hashes={**results['source_hashes'],**review['source_bindings']}
    for rel,h in hashes.items():assert sha(ROOT/rel)==h,rel
    previous=json.loads((FEEDBACK/'remaining-dependency-results.json').read_text())
    previous={c['name']:c for c in previous['cases']}
    for name,parent in results['parents'].items():
        assert parent==previous[name] and parent['parameters']['capacity']==256
    generated,coverage=generate(results)
    assert coverage['state_count']==review['continuation_state_points']==648
    assert coverage['charged_events']==review['successful_charged_events']==586
    assert coverage['denied_events']==review['recorded_denials']==28
    archive=HERE/'runs'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    snapshots=archive/'snapshots';snapshots.mkdir(parents=True)
    paths={ROOT/p for p in hashes}
    paths.update([CORE,cal.OLD/'RemainingDependency.lean',cal.OLD/'check.py',PRIOR/'CalibrationRevision.lean',
        PRIOR/'check.py',PRIOR/'verification.json',HERE/'RecipeGrounding.lean',HERE/'RecipeNative.lean',
        HERE/'lean-toolchain',Path(__file__),RESULT,INDEPENDENT])
    before={str(p.relative_to(ROOT)):sha(p) for p in sorted(paths)}
    for path in sorted(paths):
        dest=snapshots/path.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,dest)
        assert sha(dest)==before[str(path.relative_to(ROOT))]
    fixture=archive/'SavedRecipeCorrespondence.lean';fixture.write_text(generated)
    entries=inherited_modules+[
       ('RecipeGrounding',HERE/'RecipeGrounding.lean','RecipeGrounding',False),
       ('RecipeNative',HERE/'RecipeNative.lean','RecipeNative',False),
       ('SavedRecipeCorrespondence',fixture,'RecipeSaved',False)]
    modules=[]
    with tempfile.TemporaryDirectory(prefix='recipe-grounding-fresh-') as tmp:
        build=Path(tmp);env={**os.environ,'LEAN_PATH':str(build)}
        for name,path,namespace,inherited in entries:
            frozen=fixture if path==fixture else snapshots/path.relative_to(ROOT)
            source=frozen.read_text();expected=audit_source(source,namespace,inherited)
            (build/(name+'.lean')).write_text(source)
            process=subprocess.run([str(LEAN),'-o',name+'.olean',name+'.lean'],cwd=build,env=env,
                  capture_output=True,text=True,timeout=300)
            log=process.stdout+process.stderr;logpath=archive/(name+'.log');logpath.write_text(log)
            assert process.returncode==0,(name,logpath,log[:3500])
            audits=helper.parse_log(log,expected)
            modules.append(dict(module=name,source_sha256=sha(frozen),log=str(logpath.relative_to(ROOT)),
                 log_sha256=sha(logpath),inherited=inherited,audit_count=len(audits),theorem_audits=audits))
    assert {rel:sha(ROOT/rel) for rel in before}==before and sha(LEAN)==helper.LEAN_SHA
    receipt=dict(status='passed',scope='Exact recipe event-attempt law and saved native words; finite source-bound correspondence, not universal Python refinement',
       compiler=dict(path=str(LEAN),version=version,sha256=helper.LEAN_SHA),
       source_hashes=before,source_hashes_stable=True,generated_fixture=str(fixture.relative_to(ROOT)),
       generated_fixture_sha256=sha(fixture),independent_runtime_receipt=str(INDEPENDENT.relative_to(ROOT)),
       independent_runtime_receipt_sha256=sha(INDEPENDENT),
       reused_helpers=[str((PRIOR/'check.py').relative_to(ROOT)),str((cal.OLD/'check.py').relative_to(ROOT))],
       mathematical_theorem_count=modules[3]['audit_count']+modules[4]['audit_count'],
       saved_correspondence_theorem_count=modules[5]['audit_count'],
       inherited_audit_count=sum(m['audit_count'] for m in modules[:3]),
       total_audit_count=sum(m['audit_count'] for m in modules),coverage=coverage,modules=modules,
       standard_axioms=sorted({a for m in modules for row in m['theorem_audits'] for a in row['axioms']}),
       axiom_free_audits=sum(not row['axioms'] for m in modules for row in m['theorem_audits']),
       custom_axioms=[],proof_holes=[],native_decide_used=False,
       limitations=['Native independent replay supplies ancestry and scheduler validation; arbitrary formal words need not be native schedules.',
          'All four decoder tables belong to the compositional grammar; the fixed two-reference schedule constructs inverses or partial/conflicting wiring, not all four completed tables.',
          'Reference forcing, target binding, same-map use, construction primitives and tariffs remain explicit local laws.',
          'The one-reference impossibility includes constant transductions; independently known bijectivity changes that question.',
          'Parent historical data are not a second support reserve. No source replenishment or full transfer is introduced.',
          'Reference-formation controller phase is encoded by an explicit finite phase coordinate, not an added hardware cell.',
          'The retained positive use and unretained adverse diagnoses are different achievements; resource failure is preserved.'])
    (archive/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    (HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','mathematical_theorem_count','saved_correspondence_theorem_count','inherited_audit_count','total_audit_count')}))
    print(archive)

if __name__=='__main__':main()
