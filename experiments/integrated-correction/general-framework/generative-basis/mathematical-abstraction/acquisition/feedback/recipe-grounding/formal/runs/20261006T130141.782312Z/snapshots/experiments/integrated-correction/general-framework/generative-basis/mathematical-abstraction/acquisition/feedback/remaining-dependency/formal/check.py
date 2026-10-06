#!/usr/bin/env python3
"""Fresh Lean checks of the saved native suffix; never execute its producer.

The independent receipt supplies the source-bound ancestral/runtime audit. This
checker translates the complete saved new state into explicit Lean literals,
checks every saved step and real denial guard, and constructs each finite core
trace. It does not prove arbitrary Python execution equivalent to the total
Lean event-attempt law, nor re-formalize the original sensory-learning prefix.
"""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').is_file())
FEEDBACK = HERE.parents[1]
CORE = ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean'
LEAN = Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
LEAN_SHA = 'b48bc5ab229bd8b320a224b87e20fc428dba6fa8a1c054bd4fa6def846e19997'
RESULT = FEEDBACK/'remaining-dependency-results.json'
INDEPENDENT = FEEDBACK/'remaining-dependency-independent-check.json'
STANDARD_AXIOMS = {'propext', 'Quot.sound', 'Classical.choice'}
SCALE = 65536
MODES = {k: '.'+v for k,v in {
    'component_complete':'componentComplete', 'awaiting_assay':'awaitingAssay',
    'unresolved':'unresolved', 'no_supported_route':'noSupportedRoute',
    'component_complete_stop':'componentCompleteStop', 'selected_bypass':'selectedBypass',
    'selected_relay':'selectedRelay', 'service_issued':'serviceIssued'}.items()}
FAULTS = {'missing':'.missing', 'context':'.wrongContext', 'setting':'.wrongSetting', 'flip':'.flip'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tick(q):
    n = Fraction(q)*SCALE
    assert n.denominator == 1 and n >= 0, q
    return n.numerator


def b(x):
    assert x in (0,1,False,True)
    return 'true' if x else 'false'


def string(x):
    return json.dumps(x, ensure_ascii=False)


def opt(x, encode=str):
    return 'none' if x is None else '(some '+encode(x)+')'


def pair(xs, encode):
    assert len(xs) == 2
    return '⟨'+', '.join(encode(x) for x in xs)+'⟩'


def ls(xs, encode):
    return '['+', '.join(encode(x) for x in xs)+']'


def datum(x):
    if x is None:
        return 'none'
    c,r,v = x
    return '(some ⟨'+str(c)+', '+b(r)+', '+b(v)+'⟩)'


def config(case):
    p = case['parameters']
    channels = ['.faithful','.faithful']
    if p['fault']:
        kind, at = p['fault']
        for i in (0,1):
            if at == i or at == 'both':
                channels[i] = FAULTS[kind]
    assert p['policy'] in ('learned','clamped','conventional')
    return ('{weak := '+pair(p['law'],b)+', full := '+pair(p['full_law'],b)+
            ', channels := '+pair(channels,str)+', clamp := '+b(p['policy']=='clamped')+'}')


def state(s, cfg):
    a,h,n,c = (s[k] for k in ('account','inherited','native','controller'))
    assert Fraction(a['income']) == 0 and a['workspace'] == 0
    assert Fraction(a['fuel'])+Fraction(a['spent']) == Fraction(a['start'])
    assert Fraction(s['whole_account']) == 145
    assert all(len(row)==1 for row in h['H']['transitions'])
    ancestor = ('{alphabet := '+ls(h['H']['alphabet'],string)+', initial := '+str(h['H']['initial'])+
        ', controlLocation := '+string(h['control_location'])+', outputs := '+ls(h['H']['outputs'],b)+
        ', transitions := '+ls([r[0] for r in h['H']['transitions']],str)+
        ', table := '+ls(h['table'],lambda x:opt(x,b))+', retained := '+b(h['retained'])+
        ', componentDone := '+b(h['component_done'])+'}')
    account = ('{fuel := '+str(tick(a['fuel']))+', start := '+str(tick(a['start']))+
        ', spent := '+str(tick(a['spent']))+', live := '+str(a['live'])+
        ', peak := '+str(a['peak'])+', capacity := '+str(a['capacity'])+'}')
    body = ('{account := '+account+', stocks := ⟨'+', '.join(str(n[k]) for k in ('source','load','waste'))+'⟩'+
        ', context := '+str(n['context'])+', relay := '+b(n['relay'])+', pending := '+datum(n['pending'])+
        ', held := '+b(n['held'])+', installed := '+b(c['installed'])+', retained := '+b(c['retained'])+
        ', mode := '+MODES[c['mode']]+', values := '+pair(c['values'],lambda x:opt(x,b))+
        ', tags := '+pair(c['tags'],lambda x:opt(x,str))+', contact := '+datum(c['contact'])+
        ', candidate := '+opt(c['candidate'],b)+', readMode := '+opt(c['read_mode'],lambda x:MODES[x])+
        ', selected := '+opt(c['selected'],b)+'}')
    return '{ancestor := '+ancestor+', config := '+cfg+', body := '+body+'}'


def operation(kind, detail, before):
    r = before['native']['relay']
    simple = {'dependency_installation':'.install', 'weak_challenge':'.challenge',
        'dependency_read':'.read', 'dependency_commit':'.commit', 'context_change':'.contextChange',
        'relay_hold':'.hold', 'relay_release':'.release', 'full_load_transfer':'.transfer',
        'dependency_retention':'.retain'}
    if kind in simple:
        return simple[kind]
    if kind == 'incurred_wait':
        return '(.wait '+str(detail['interval'])+')'
    if kind == 'relay_command':
        return '(.command '+b(detail.get('setting',r))+')'
    if kind == 'dependency_contact':
        return '(.contact '+b(detail.get('probe',r))+')'
    if kind == 'dependency_slot_write':
        return '(.write '+b(detail.get('setting',r))+')'
    raise AssertionError(kind)


def tariff_arguments(kind, detail, before):
    live = before['account']['live']
    params = {
      'dependency_installation':(8,live+8,8,SCALE,0),
      'relay_command':(1,live,2,16384,0), 'weak_challenge':(1,live,2,16384,0),
      'dependency_contact':(0,live,2,16384,0), 'dependency_slot_write':(1,live,2,0,2),
      'dependency_read':(2,live,2,0,0), 'dependency_commit':(1,live,2,0,2),
      'relay_hold':(1,live,2,16384,0), 'relay_release':(1,live,2,0,0),
      'full_load_transfer':(1,live,2,16384,0), 'dependency_retention':(1,live,0,1024*live,0)}
    if kind == 'incurred_wait':
        return 0,live,0,SCALE*detail['interval'],0
    return params[kind]


def generate(results):
    out = ['import RemainingDependency', 'namespace RemainingDependencySaved',
           'open RemainingDependency', 'set_option maxRecDepth 65536',
           'set_option maxHeartbeats 8000000',
           '/- Generated solely from the frozen saved JSON; capacity_forty is a conditional cut-state guard, not a valid ancestral history. -/']
    names, rows = [], []
    event_count = denied_count = charge_count = 0
    def theorem(name, statement, proof='by decide'):
        names.append(name)
        out.append('theorem '+name+' :\n  '+statement+' := '+proof+'\n')
    for case in results['cases']:
        name = case['name']
        assert re.fullmatch(r'[a-z][a-z0-9_]*',name)
        cfg = name+'_config'
        out.append('def '+cfg+' : Config := '+config(case))
        trace = case['trace']
        assert trace[0]['kind'] == 'entrance' and trace[0]['charge'] is None
        assert trace[-1]['state'] == case['final']
        for i,e in enumerate(trace):
            out.append('def '+name+'_s'+str(i)+' : State := '+state(e['state'],cfg))
            assert e['state']['native']['test_law']==case['parameters']['law']
            assert e['state']['native']['full_law']==case['parameters']['full_law']
        inherited = tick(case['inherited_consumption'])
        theorem(name+'_initial_whole_account',
                'wholeTotal '+str(inherited)+' '+name+'_s0 = 145 * ticks')
        events = []
        for i in range(1,len(trace)):
            e, before = trace[i],trace[i-1]['state']
            s,t = name+'_s'+str(i-1), name+'_s'+str(i)
            kind, detail = e['kind'],e['detail']
            statement = ''
            if kind == 'denied':
                denied_count += 1
                assert e['charge'] is None
                reason = detail['reason']
                if reason == 'entrance_not_retained_component_stop':
                    statement = '('+s+'.ancestor.controlLocation ≠ "reported_episode_complete" ∨ '+s+'.ancestor.retained = false) ∧ '+s+' = '+t
                    theorem(name+'_event_'+str(i),statement)
                    continue
                reason,kind = reason.split(':')
                ev = operation(kind,{},before)
                if reason == 'source_unavailable':
                    assert kind == 'full_load_transfer'
                    guard = s+'.body.stocks.source < 10'
                else:
                    assert reason in ('funding','capacity')
                    args = ' '.join(map(str,tariff_arguments(kind,{},before)))
                    guard = '(charge '+s+'.body.account '+args+').2 = .'+reason
                statement = guard+' ∧ step '+s+' '+ev+' = '+t
            else:
                ev = operation(kind,detail,before)
                statement = 'step '+s+' '+ev+' = '+t
                if kind != 'context_change':
                    charge_count += 1
                    q = e['charge']
                    assert q and q['kind'] == kind and q['workspace'] == 0
                    args = tariff_arguments(kind,detail,before)
                    w,l,tmp,extra,rw = args
                    assert (q['work'],q['live'],q['temporary'],tick(q['extra']),q['rewrites']) == args
                    assert q['peak'] == max(before['account']['live'],l)+tmp
                    assert Fraction(q['fuel']) == Fraction(e['state']['account']['fuel'])
                    text_args = ' '.join(map(str,args))
                    statement += (' ∧ tariff '+s+'.body.account '+text_args+' = '+str(tick(q['bill']))+
                         ' ∧ (charge '+s+'.body.account '+text_args+').2 = .none')
                else:
                    assert e['charge'] is None
            theorem(name+'_event_'+str(i),statement)
            events.append(ev)
            event_count += 1
        plan = '['+', '.join(events)+']'
        end = name+'_s'+str(len(trace)-1)
        theorem(name+'_saved_run', 'run '+name+'_s0 '+plan+' = '+end)
        theorem(name+'_core_trace', 'Generative.Trace process '+name+'_s0 '+plan+' '+end,
                'by\n  rw [← '+name+'_saved_run]\n  exact run_is_core_trace _ _')
        theorem(name+'_final_whole_account', 'wholeTotal '+str(inherited)+' '+end+' = 145 * ticks')
        rows.append(dict(name=name,states=len(trace),event_attempts=len(events),
                         ancestry_admissible=name!='capacity_forty',
                         scope='conditional local cut-state guard; global-capacity ancestry rejected' if name=='capacity_forty' else 'source-bound inherited history; entrance denial retained where applicable'))
    out += ['#print axioms '+name for name in names]
    out.append('end RemainingDependencySaved\n')
    return '\n'.join(out),dict(cases=rows,state_count=sum(r['states'] for r in rows),
        event_attempts=event_count,denied_events=denied_count,charged_events=charge_count,
        theorem_count=len(names),case_count=len(rows),ancestry_admissible_cases=len(rows)-1,
        conditional_suffix_only_cases=['capacity_forty'])


def remove_comments_and_strings(text):
    out=[]; i=0; depth=0; quote=False
    while i<len(text):
        if depth:
            if text.startswith('/-',i): depth+=1; i+=2
            elif text.startswith('-/',i): depth-=1; i+=2
            else:
                if text[i]=='\n': out.append('\n')
                i+=1
        elif quote:
            if text[i]=='\\': i+=2
            elif text[i]=='"': quote=False; out.append(' '); i+=1
            else: i+=1
        elif text.startswith('/-',i): depth=1; out.append(' '); i+=2
        elif text.startswith('--',i):
            j=text.find('\n',i); i=len(text) if j<0 else j
        elif text[i]=='"': quote=True; out.append(' '); i+=1
        else: out.append(text[i]); i+=1
    assert depth==0 and not quote
    return ''.join(out)


def audit_source(text, namespace, inherited=False):
    code=remove_comments_and_strings(text)
    assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b|^\s*axiom\b',code,re.M)
    imports=re.findall(r'^import\s+(\S+)\s*$',code,re.M)
    assert set(imports) <= {'Std','GenerativeCore','RemainingDependency'}
    declarations=re.findall(r'^theorem\s+(\w+)\b',code,re.M)
    audits=re.findall(r'^#print axioms\s+([\w.]+)\s*$',code,re.M)
    assert len(audits)==len(set(audits))
    if not inherited:
        assert declarations==audits, (declarations,audits)
    return [namespace+'.'+a if '.' not in a else a for a in audits]


def parse_log(log, expected):
    findings=[]
    for line in log.splitlines():
        m=re.fullmatch(r"'([^']+)' does not depend on any axioms",line)
        if m:
            findings.append(dict(theorem=m.group(1),axioms=[]));continue
        m=re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]",line)
        if m:
            axioms=[v.strip() for v in m.group(2).split(',') if v.strip()]
            assert set(axioms) <= STANDARD_AXIOMS, (m.group(1),axioms)
            findings.append(dict(theorem=m.group(1),axioms=axioms))
    assert [x['theorem'] for x in findings]==expected
    assert not re.search(r'\b(error|warning):',log)
    return findings


def main():
    assert sha(LEAN)==LEAN_SHA
    version=subprocess.check_output([str(LEAN),'--version'],text=True).strip()
    assert '4.29.1' in version
    assert (HERE/'lean-toolchain').read_text()=='leanprover/lean4:v4.29.1\n'
    results=json.loads(RESULT.read_text())
    independent=json.loads(INDEPENDENT.read_text())
    assert independent['status']=='passed'
    assert independent['results_sha256']==sha(RESULT)
    assert independent['ancestry_admissible_cases']==27
    assert independent['conditional_suffix_only_cases'][0]['name']=='capacity_forty'
    source_bindings={**results['source_hashes'],**independent['source_bindings']}
    for rel,h in source_bindings.items(): assert sha(ROOT/rel)==h,rel
    old=json.loads((FEEDBACK/'inquiry-results.json').read_text())
    old_by_name={x['name']:x for x in old['cases']}
    for name,parent in results['parents'].items(): assert parent==old_by_name[name]
    # Explicit boundary restriction; the independent audit follows each whole
    # ancestor through its actual peak, not only the final inquiry account.
    for case in results['cases']:
        parent=results['parents'][case['parameters']['parent']]
        s=case['trace'][0]['state']
        assert s['account']['fuel']==parent['final']['fuel']
        assert s['native']['source']==parent['final']['source']
        assert s['inherited']['H']==parent['model_after']
        assert s['inherited']['table']==parent['final']['table']
        assert s['inherited']['component_done']==parent['final']['actual_episode_fulfilled']
    generated,counts=generate(results)
    assert counts['state_count']==independent['continuation_state_points']==362
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    archive=HERE/'runs'/stamp
    archive.mkdir(parents=True)
    snapshots=archive/'snapshots';snapshots.mkdir()
    all_paths={ROOT/p for p in source_bindings}
    all_paths.update([CORE,HERE/'RemainingDependency.lean',HERE/'lean-toolchain',Path(__file__),RESULT,INDEPENDENT])
    before={str(p.relative_to(ROOT)):sha(p) for p in sorted(all_paths)}
    for path in sorted(all_paths):
        relative=path.relative_to(ROOT)
        target=snapshots/relative;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,target)
        assert sha(target)==before[str(relative)]
    fixture=archive/'SavedCorrespondence.lean';fixture.write_text(generated)
    entries=[('GenerativeCore',CORE,'Generative',True),
             ('RemainingDependency',HERE/'RemainingDependency.lean','RemainingDependency',False),
             ('SavedCorrespondence',fixture,'RemainingDependencySaved',False)]
    modules=[]
    with tempfile.TemporaryDirectory(prefix='remaining-dependency-fresh-') as temporary:
        build=Path(temporary)
        env=os.environ.copy();env['LEAN_PATH']=str(build)
        for name,path,namespace,inherited in entries:
            frozen=fixture if name=='SavedCorrespondence' else snapshots/path.relative_to(ROOT)
            code=frozen.read_text()
            expected=audit_source(code,namespace,inherited)
            (build/(name+'.lean')).write_text(code)
            p=subprocess.run([str(LEAN),'-o',name+'.olean',name+'.lean'],cwd=build,
                             env=env,capture_output=True,text=True,timeout=180)
            log=p.stdout+p.stderr
            logpath=archive/(name+'.log');logpath.write_text(log)
            assert p.returncode==0, (name,logpath,log[-3000:])
            audits=parse_log(log,expected)
            modules.append(dict(module=name,source_sha256=sha(frozen),
                log=str(logpath.relative_to(ROOT)),log_sha256=sha(logpath),
                inherited=inherited,theorem_audits=audits,audit_count=len(audits)))
    after={rel:sha(ROOT/rel) for rel in before}
    assert after==before
    assert sha(LEAN)==LEAN_SHA
    receipt=dict(status='passed',scope='Fresh exact event-attempt law and all saved native suffix correspondences; no whole-prefix Lean semantics or general Python compiler-refinement claim',
        compiler=dict(path=str(LEAN),version=version,sha256=LEAN_SHA),
        source_hashes=before,source_hashes_stable=True,
        generated_fixture=str(fixture.relative_to(ROOT)),generated_fixture_sha256=sha(fixture),
        independent_runtime_receipt=str(INDEPENDENT.relative_to(ROOT)),
        independent_runtime_receipt_sha256=sha(INDEPENDENT),
        mathematical_theorem_count=modules[1]['audit_count'],
        saved_correspondence_theorem_count=modules[2]['audit_count'],
        inherited_audit_count=modules[0]['audit_count'],
        total_audit_count=sum(m['audit_count'] for m in modules),
        standard_axioms=sorted({a for m in modules for row in m['theorem_audits'] for a in row['axioms']}),
        axiom_free_audits=sum(not r['axioms'] for m in modules for r in m['theorem_audits']),
        custom_axioms=[],proof_holes=[],native_decide_used=False,
        coverage=counts,modules=modules,
        limitations=[
          'The original inquiry endpoint is bound to saved data and its independent source audit, not rederived in this Lean module.',
          'Capacity40 is a rejected global-ancestry claim: its conditional suffix guard alone is verified. The other27 histories remain ancestry-admissible, including entrance denial.',
          'Total requested-event semantics permits arbitrary words and denial self-loops; saved-word correspondence and the independent driver replay establish the executed sequences.',
          'The dormant relay/load extension, physical family, calibration, full-pair gate, two-probe schedule, supplied undertaking and maintenance preference remain declared local inputs.',
          'Actor income and workspace are checked zero at every native snapshot; whole145 account is derived from fixed inherited consumption and explicit actor/source/load/waste coordinates.',
          'No ethical derivation, globally optimal inquiry, empirical identification or acquired final service-success judgment is asserted.'])
    archived=archive/'verification.json';archived.write_text(json.dumps(receipt,indent=2)+'\n')
    (HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','mathematical_theorem_count','saved_correspondence_theorem_count','inherited_audit_count','total_audit_count','standard_axioms']}))
    print('receipt',archived)


if __name__=='__main__':
    main()
