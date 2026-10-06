#!/usr/bin/env python3
"""Fresh exact-law correspondence with frozen calibration-revision outcomes.

No producer or reviewer transition implementation is executed. Pure formatting,
comment stripping, audit-log parsing and old-state serialization are reused from
the source-bound preceding formal checker; their source bytes are frozen too.
The independent runtime receipt supplies the checked ancestry/control-flow basis.
"""
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

HERE = Path(__file__).resolve().parent
FEEDBACK = HERE.parents[1]
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').is_file())
OLD = FEEDBACK/'remaining-dependency/formal'
spec=importlib.util.spec_from_file_location('previous_formal_serializer',OLD/'check.py')
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
sha,tick,b,opt,pair,ls,datum = (getattr(helper,n) for n in ('sha','tick','b','opt','pair','ls','datum'))
CORE=helper.CORE
LEAN=helper.LEAN
RESULT=FEEDBACK/'calibration-revision-results.json'
INDEPENDENT=FEEDBACK/'calibration-revision-independent-check.json'
APPLICATION={'unobserved':'.unobserved','full_evidence_unavailable':'.unavailable',
             'tested_prediction_supported':'.supported','tested_prediction_failed':'.failed'}
DIAGNOSIS={'unobserved':'.unobserved','fresh_evidence_unavailable':'.unavailable',
    'same_setting_discrepancy':'.discrepancy','old_weak_report_contradicted':'.oldContradicted',
    'current_same_setting_agreement':'.currentAgreement'}
PHASE={'old_interface':'.oldInterface','formed':'.formed','application_revised':'.applicationRevised',
       'diagnostic_committed':'.committed','diagnosis_revised':'.diagnosisRevised'}


def encode_mask(mask):
    if mask is None: return None
    assert len(mask)==16 and all(type(x) is bool for x in mask)
    code=sum(2**i for i,v in enumerate(mask) if v)
    assert [bool((code>>i)&1) for i in range(16)]==mask
    return code


def config(case):
    p=case['parameters']
    fault=lambda f: '.faithful' if f is None else helper.FAULTS[f]
    assert p['policy'] in ('learned','clamped','conventional')
    return '{fullFault := '+fault(p['full_fault'])+', weakFault := '+fault(p['weak_fault'])+', clamp := '+b(p['policy']=='clamped')+'}'


def encode_state(s,parent,cfg):
    a,n,c=(s[k] for k in ('account','native','controller'))
    assert Fraction(a['income'])==0 and a['workspace']==0
    assert Fraction(a['fuel'])+Fraction(a['spent'])==Fraction(a['start'])
    assert Fraction(s['whole_account'])==145
    account=('{fuel := '+str(tick(a['fuel']))+', start := '+str(tick(a['start']))+
        ', spent := '+str(tick(a['spent']))+', live := '+str(a['live'])+', peak := '+str(a['peak'])+
        ', capacity := '+str(a['capacity'])+'}')
    body=('{account := '+account+', stocks := ⟨'+', '.join(str(n[k]) for k in ('source','load','waste'))+'⟩'+
        ', context := '+str(n['context'])+', relay := '+b(n['relay'])+', pending := '+datum(n['pending'])+
        ', held := '+b(n['held'])+', installed := '+b(c['installed'])+', retained := '+b(c['retained'])+
        ', mask := '+opt(encode_mask(c['mask']))+', fullRecord := '+datum(c['full_record'])+
        ', weakRecord := '+datum(c['weak_record'])+', contact := '+datum(c['contact'])+
        ', application := '+APPLICATION[c['application']]+', diagnosis := '+DIAGNOSIS[c['diagnosis']]+
        ', proposal := '+opt(c['proposal'],b)+', activation := '+opt(c['activation'],b)+
        ', phase := '+PHASE[c['phase']]+'}')
    return '{parent := '+parent+', config := '+cfg+', body := '+body+'}'


def operation(kind,detail,before):
    names={'calibration_installation':'.install','full_stock_contact':'.fullContact',
        'full_record_write':'.fullWrite','filter_full':'.filterFull','revise_application':'.reviseApplication',
        'choose_diagnostic':'.choose','commit_diagnostic':'.commit',
        'diagnostic_weak_challenge':'.challenge','fresh_weak_contact':'.weakContact',
        'fresh_record_write':'.weakWrite','filter_weak':'.filterWeak','revise_diagnosis':'.reviseDiagnosis',
        'calibration_retention':'.retain'}
    if kind in names: return names[kind]
    if kind=='incurred_wait': return '(.wait '+str(detail['interval'])+')'
    if kind=='diagnostic_relay_command':
        return '(.command '+b(detail.get('setting',before['controller']['activation']))+')'
    raise AssertionError(kind)


def arguments(kind,detail,before):
    live=before['account']['live']
    params={'calibration_installation':(24,58,8,65536,0),
      'full_stock_contact':(0,live,2,16384,0), 'full_record_write':(1,live,2,0,2),
      'filter_full':(16,live,2,0,16), 'revise_application':(2,live,2,0,1),
      'choose_diagnostic':(32,live,3,0,1), 'commit_diagnostic':(1,live,2,0,1),
      'diagnostic_relay_command':(1,live,2,16384,0), 'diagnostic_weak_challenge':(1,live,2,16384,0),
      'fresh_weak_contact':(0,live,2,16384,0), 'fresh_record_write':(1,live,2,0,2),
      'filter_weak':(16,live,2,0,16), 'revise_diagnosis':(2,live,2,0,1),
      'calibration_retention':(1,live,0,1024*live,0)}
    if kind=='incurred_wait': return (0,live,0,65536*detail['interval'],0)
    return params[kind]


def generate(results):
    out=['import CalibrationRevision','namespace CalibrationRevisionSaved','open CalibrationRevision',
        'set_option maxRecDepth 65536','set_option maxHeartbeats 8000000',
        '/- Generated from frozen saved states. A 16-entry Boolean mask is losslessly encoded as a 16-bit Nat; distinct observed encodings are also kernel checked. -/']
    names=[];rows=[];events_total=charges=denials=0
    def theorem(name,statement,proof='by decide'):
        names.append(name)
        out.append('theorem '+name+' :\n  '+statement+' := '+proof+'\n')
    for name,parent in results['parents'].items():
        cfg='parent_'+name+'_config';state='parent_'+name
        out.append('def '+cfg+' : RemainingDependency.Config := '+helper.config(parent))
        out.append('def '+state+' : RemainingDependency.State := '+helper.state(parent['final'],cfg))
    for name,constant in [('calibration_break','mismatchParent'),('false_dependence','oldReportErrorParent'),('law_01_learned','positiveParent')]:
        theorem('parent_'+name+'_matches_prior_formal_construction','parent_'+name+' = '+constant)
    masks={}
    for case in results['cases']:
        for e in case['trace']:
            mask=e['state']['controller']['mask']
            if mask is not None: masks[encode_mask(mask)]=mask
    for code,mask in sorted(masks.items()):
        theorem('mask_encoding_'+str(code), '(List.range 16).map ('+str(code)+' : Nat).testBit = '+ls(mask,b))
    for case in results['cases']:
        name=case['name'];assert re.fullmatch(r'[a-z][a-z0-9_]*',name)
        cfg=name+'_config';parent='parent_'+case['parameters']['parent']
        out.append('def '+cfg+' : Config := '+config(case))
        trace=case['trace'];old=results['parents'][case['parameters']['parent']]['final']
        assert trace[0]['kind']=='entrance' and trace[0]['charge'] is None
        assert trace[-1]['state']==case['final']
        for i,e in enumerate(trace):
            s=e['state']
            assert s['inherited']==old['inherited'] and s['old_controller']==old['controller']
            for k in ('source','load','waste','test_law','full_law','context'):
                assert s['native'][k]==old['native'][k]
            out.append('def '+name+'_s'+str(i)+' : State := '+encode_state(s,parent,cfg))
        theorem(name+'_actual_entrance','entrance '+parent+' '+cfg+' = '+name+'_s0')
        inherited=tick(case['inherited_consumption'])
        theorem(name+'_initial_whole_account','wholeTotal '+str(inherited)+' '+name+'_s0 = 145 * RemainingDependency.ticks')
        plan=[]
        for i in range(1,len(trace)):
            e,before=trace[i],trace[i-1]['state']
            s,t=name+'_s'+str(i-1),name+'_s'+str(i)
            kind,detail=e['kind'],e['detail']
            if kind=='denied':
                denials+=1;assert e['charge'] is None
                reason=detail['reason']
                if reason=='entrance_not_retained_full_operation':
                    statement=('('+s+'.parent.body.retained = false ∨ '+s+'.parent.body.mode ≠ .serviceIssued ∨ '+
                        s+'.parent.body.selected = none ∨ '+s+'.body.stocks.source ≠ 0) ∧ '+s+' = '+t)
                    theorem(name+'_event_'+str(i),statement)
                    continue
                reason,kind=reason.split(':');assert reason in ('funding','capacity')
                ev=operation(kind,{},before);args=' '.join(map(str,arguments(kind,{},before)))
                statement='(RemainingDependency.charge '+s+'.body.account '+args+').2 = .'+reason+' ∧ step '+s+' '+ev+' = '+t
            else:
                charges+=1
                ev=operation(kind,detail,before);args=arguments(kind,detail,before)
                q=e['charge'];assert q and q['kind']==kind and q['workspace']==0
                w,l,tmp,extra,rw=args
                assert (q['work'],q['live'],q['temporary'],tick(q['extra']),q['rewrites'])==args
                assert q['peak']==max(before['account']['live'],l)+tmp
                assert Fraction(q['fuel'])==Fraction(e['state']['account']['fuel'])
                if kind=='incurred_wait': assert detail['interval']==case['parameters']['wait']
                text_args=' '.join(map(str,args))
                statement=('step '+s+' '+ev+' = '+t+' ∧ RemainingDependency.tariff '+s+'.body.account '+text_args+
                    ' = '+str(tick(q['bill']))+' ∧ (RemainingDependency.charge '+s+'.body.account '+text_args+').2 = .none')
            theorem(name+'_event_'+str(i),statement)
            plan.append(ev);events_total+=1
        word='['+', '.join(plan)+']';end=name+'_s'+str(len(trace)-1)
        theorem(name+'_saved_run','run '+name+'_s0 '+word+' = '+end)
        theorem(name+'_core_trace','Generative.Trace process '+name+'_s0 '+word+' '+end,
                'by\n  rw [← '+name+'_saved_run]\n  exact run_is_core_trace _ _')
        theorem(name+'_final_whole_account','wholeTotal '+str(inherited)+' '+end+' = 145 * RemainingDependency.ticks')
        rows.append(dict(name=name,states=len(trace),event_attempts=len(plan)))
    out.extend('#print axioms '+name for name in names)
    out.append('end CalibrationRevisionSaved\n')
    return '\n'.join(out),dict(case_count=len(rows),cases=rows,state_count=sum(r['states'] for r in rows),
        event_attempts=events_total,saved_edges=sum(r['states']-1 for r in rows),charged_events=charges,
        denied_events=denials,parent_construction_equalities=3,mask_encoding_equalities=len(masks),
        theorem_count=len(names))


def audit_source(text,namespace,inherited=False):
    code=helper.remove_comments_and_strings(text)
    assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b|^\s*axiom\b',code,re.M)
    imports=re.findall(r'^import\s+(\S+)\s*$',code,re.M)
    assert set(imports)<={'Std','GenerativeCore','RemainingDependency','CalibrationRevision'}
    declarations=re.findall(r'^theorem\s+(\w+)\b',code,re.M)
    audits=re.findall(r'^#print axioms\s+([\w.]+)\s*$',code,re.M)
    assert len(audits)==len(set(audits))
    if not inherited: assert declarations==audits
    return [namespace+'.'+n if '.' not in n else n for n in audits]


def main():
    assert sha(LEAN)==helper.LEAN_SHA
    version=subprocess.check_output([str(LEAN),'--version'],text=True).strip()
    assert '4.29.1' in version
    assert (HERE/'lean-toolchain').read_text()=='leanprover/lean4:v4.29.1\n'
    results=json.loads(RESULT.read_text());independent=json.loads(INDEPENDENT.read_text())
    assert independent['status']=='passed' and independent['results_sha256']==sha(RESULT)
    old_receipt=json.loads((OLD/'verification.json').read_text())
    assert old_receipt['status']=='passed'
    for path in (CORE,OLD/'RemainingDependency.lean',OLD/'check.py'):
        assert sha(path)==old_receipt['source_hashes'][str(path.relative_to(ROOT))]
    hashes={**results['source_hashes'],**independent['source_bindings']}
    for rel,h in hashes.items(): assert sha(ROOT/rel)==h,rel
    previous=json.loads((FEEDBACK/'remaining-dependency-results.json').read_text())
    previous={c['name']:c for c in previous['cases']}
    for name,parent in results['parents'].items():
        assert parent==previous[name]
        assert parent['parameters']['capacity']==256
        assert name!='capacity_forty'
    generated,counts=generate(results)
    assert counts['state_count']==independent['continuation_state_points']==288
    assert counts['charged_events']==independent['successful_charged_events']==257
    assert counts['denied_events']==independent['recorded_denials']==6
    archive=HERE/'runs'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    snapshots=archive/'snapshots';snapshots.mkdir(parents=True)
    paths={ROOT/p for p in hashes}
    paths.update([CORE,OLD/'RemainingDependency.lean',OLD/'check.py',OLD/'verification.json',
                  HERE/'CalibrationRevision.lean',HERE/'lean-toolchain',Path(__file__),RESULT,INDEPENDENT])
    before={str(p.relative_to(ROOT)):sha(p) for p in sorted(paths)}
    for p in sorted(paths):
        dst=snapshots/p.relative_to(ROOT);dst.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,dst);assert sha(dst)==before[str(p.relative_to(ROOT))]
    fixture=archive/'SavedCalibrationCorrespondence.lean';fixture.write_text(generated)
    entries=[('GenerativeCore',CORE,'Generative',True),
        ('RemainingDependency',OLD/'RemainingDependency.lean','RemainingDependency',True),
        ('CalibrationRevision',HERE/'CalibrationRevision.lean','CalibrationRevision',False),
        ('SavedCalibrationCorrespondence',fixture,'CalibrationRevisionSaved',False)]
    modules=[]
    with tempfile.TemporaryDirectory(prefix='calibration-revision-fresh-') as tmp:
        build=Path(tmp);env=os.environ.copy();env['LEAN_PATH']=str(build)
        for name,path,namespace,inherited in entries:
            frozen=fixture if name=='SavedCalibrationCorrespondence' else snapshots/path.relative_to(ROOT)
            source=frozen.read_text();expected=audit_source(source,namespace,inherited)
            (build/(name+'.lean')).write_text(source)
            p=subprocess.run([str(LEAN),'-o',name+'.olean',name+'.lean'],cwd=build,env=env,
                             capture_output=True,text=True,timeout=180)
            log=p.stdout+p.stderr;logpath=archive/(name+'.log');logpath.write_text(log)
            assert p.returncode==0,(name,logpath,log[-4000:])
            audits=helper.parse_log(log,expected)
            modules.append(dict(module=name,source_sha256=sha(frozen),
                log=str(logpath.relative_to(ROOT)),log_sha256=sha(logpath),inherited=inherited,
                theorem_audits=audits,audit_count=len(audits)))
    assert {rel:sha(ROOT/rel) for rel in before}==before
    assert sha(LEAN)==helper.LEAN_SHA
    receipt=dict(status='passed',scope='Exact additive event-attempt law and all saved native calibration-revision histories; no universal Python execution-equivalence claim',
        compiler=dict(path=str(LEAN),version=version,sha256=helper.LEAN_SHA),
        source_hashes=before,source_hashes_stable=True,
        generated_fixture=str(fixture.relative_to(ROOT)),generated_fixture_sha256=sha(fixture),
        independent_runtime_receipt=str(INDEPENDENT.relative_to(ROOT)),independent_runtime_receipt_sha256=sha(INDEPENDENT),
        reused_serialization_helper=str((OLD/'check.py').relative_to(ROOT)),
        mathematical_theorem_count=modules[2]['audit_count'],saved_correspondence_theorem_count=modules[3]['audit_count'],
        inherited_audit_count=modules[0]['audit_count']+modules[1]['audit_count'],
        total_audit_count=sum(m['audit_count'] for m in modules),
        standard_axioms=sorted({a for m in modules for row in m['theorem_audits'] for a in row['axioms']}),
        axiom_free_audits=sum(not row['axioms'] for m in modules for row in m['theorem_audits']),
        custom_axioms=[],proof_holes=[],native_decide_used=False,coverage=counts,modules=modules,
        limitations=[
          'Source-bound independent native checking supplies original ancestry and scheduler validation; no whole ancestral sensory learner or general Python compiler refinement is claimed.',
          'Total event-attempt semantics permits arbitrary words, denial self-loops and reinstallation. Only filtering and the executed schedule claim mask nonexpansion.',
          'The nominal helper is the funded main sequence; saved adverse words check actual abort, denial guards and final retention order.',
          'The immutable parent is historical information, not a second fuel reserve; only the actual current body account enters the 145-unit identity.',
          'The native16 Boolean mask is losslessly encoded as a Nat; every distinct reached encoding is kernel checked.',
          'Current weak versus historical full interpretation requires bound same-setting/context provenance, static weak behavior and the declared stock-reader contract.',
          'Actual proposals recheck the previous full-tested setting. No general differently addressed diagnosis theorem is asserted for arbitrary fallback reuse.',
          'No source or actor income is added, no second full transfer occurs, and weak inquiries cannot identify the untested full coordinate in the declared family.',
          'The reader, candidate family, mismatch trigger and one-recheck policy are supplied local laws, not learned ultimate goals or ethical grounds.'])
    (archive/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    (HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','mathematical_theorem_count','saved_correspondence_theorem_count','inherited_audit_count','total_audit_count','standard_axioms']}))
    print('receipt',archive/'verification.json')


if __name__=='__main__':
    main()
