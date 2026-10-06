"""Fresh kernel checks connecting saved applicability histories to Lean.

Only saved artifacts are read: this script never executes the Python producer
or overwrites the accepted Python independent-check receipt.  Generated finite
fixtures are checked against the separately authored Lean event law.
"""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
APP = HERE.parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
CORE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
COMPILER = Path('/Users/ren/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean')
COMPILER_SHA256 = 'b48bc5ab229bd8b320a224b87e20fc428dba6fa8a1c054bd4fa6def846e19997'
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def units(value):
    amount = Fraction(value) * 65536
    check(amount.denominator == 1 and amount >= 0, ('nonintegral/negative fuel units', value))
    return amount.numerator


def verify_native_bindings():
    data = json.loads((APP / 'results.json').read_text())
    native_check = json.loads((APP / 'independent-check.json').read_text())
    check(native_check['accepted'] and native_check['hashes_stable'], 'native acceptance required')
    check(native_check['traces'] == 65 and native_check['state_comparisons'] == 2033,
          'native checked scope changed')
    bound = dict(data['source_hashes'])
    for path, expected in native_check['source_hashes'].items():
        check(digest(ROOT / path) == expected, ('native check binding', path))
        if path in bound:
            check(bound[path] == expected, ('inconsistent native binding', path))
        bound[path] = expected
    for path, expected in bound.items():
        check(digest(ROOT / path) == expected, ('current native source', path))
    for filename in ['results.json', 'independent-check.json', 'independent_check.py']:
        path = APP / filename
        bound[str(path.relative_to(ROOT))] = digest(path)
    return data, native_check, bound


def lean_list(values):
    return '[' + ', '.join(map(str, values)) + ']'


def imports_of(source):
    return re.findall(r'^import\s+(\S+)\s*$', source, re.M)


def fresh_build(sources, attempt):
    """Compile exclusively from frozen source bytes in a new empty directory."""
    check(digest(COMPILER) == COMPILER_SHA256, 'pinned Lean compiler changed')
    version = subprocess.check_output([str(COMPILER), '--version'], text=True).strip()
    check(version.startswith('Lean (version 4.29.1,'), ('Lean version', version))
    imports, requests = {}, {}
    for module, data in sources.items():
        source = data.decode()
        check(not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', source),
              ('prohibited proof escape', module))
        check(not re.search(r'^\s*(axiom|constant|opaque)\s', source, re.M),
              ('custom assumption/opaque declaration', module))
        imports[module] = imports_of(source)
        check(set(imports[module]) <= {'Std', *sources}, ('unbound import', module))
        requests[module] = re.findall(r'^#print axioms (\S+)\s*$', source, re.M)
        check(len(requests[module]) == len(set(requests[module])), ('duplicate audit', module))
    ordering, done = [], {'Std'}
    while len(ordering) < len(sources):
        ready = [name for name in sources if name not in done and set(imports[name]) <= done]
        check(bool(ready), 'module cycle or missing dependency')
        ordering.extend(ready)
        done.update(ready)
    records = []
    with tempfile.TemporaryDirectory(prefix='applicability-lean-correspondence-') as temporary:
        directory = Path(temporary)
        for module, data in sources.items():
            (directory / (module + '.lean')).write_bytes(data)
        environment = dict(os.environ, LEAN_PATH=str(directory))
        for module in ordering:
            command = [str(COMPILER), '-o', module + '.olean', module + '.lean']
            completed = subprocess.run(command, cwd=directory, env=environment, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)
            log = attempt / (module + '.log')
            log.write_text(completed.stdout)
            audits = [(name, sorted(a.strip() for a in dependencies.split(',') if a.strip()))
                      for name, dependencies in AUDIT.findall(completed.stdout)]
            matched = len(audits) == len(requests[module]) and all(
                actual == requested or actual.endswith('.' + requested)
                for (actual, _), requested in zip(audits, requests[module]))
            success = (completed.returncode == 0 and 'warning:' not in completed.stdout
                       and matched and all(not dependencies for _, dependencies in audits))
            record = dict(module=module, command=command, exit_code=completed.returncode,
                          passed=success, audit_complete=matched,
                          axioms_by_declaration=dict(audits),
                          source_sha256=sha256(sources[module]).hexdigest(),
                          log=str(log.relative_to(ROOT)), log_sha256=digest(log))
            records.append(record)
            print(json.dumps(dict(module=module, passed=success, audits=len(audits))), flush=True)
            if not success:
                print(completed.stdout, flush=True)
                break
    return version, records


PHASE = dict(uninstalled=0, installed=1, executing=2, updated=3, selected=4, retained=5)
CHARGED = dict(applicability_installation='install', prepare_use_word='prepare',
    native_reset='reset', native_a='advance', native_read='sense',
    check_sensory_prediction='checkSensor', native_probe='extract',
    arrival_receipt='readReceipt', commit_applicability='commit',
    scan_applicability_word='scan', retain_selected_word='select',
    clamped_repeat_selection='clamp', retain_applicability='retain')
COMPLETED = dict(installed='install', route_opened='prepare',
    sensory_prediction_confirmed='checkSensor', applicability_updated='commit',
    candidate_word_scanned='scan', next_question_selected='select',
    reader_clamped='clamp', interpretation_retained='retain', actual_arrival='extract')


def opt(value):
    return 0 if value is None else 1 + int(value)


def vector(state):
    a, p, c = (state[k] for k in ['account', 'physical', 'controller'])
    record = c['record']
    if record is not None:
        check(record['valid'] is True, 'committed record validity')
    check(set(c['word']) <= {'a'}, 'unary word')
    return [*(units(a[k]) for k in ['start', 'fuel', 'spent', 'income']),
            *(a[k] for k in ['live', 'workspace', 'peak', 'capacity']),
            *(p[k] for k in ['phase', 'source', 'transferred', 'wasted']),
            len(c['word']), c['attempts'], PHASE[c['phase']], int(c['retained']), c['base'],
            opt(c['expected']), opt(record['sensor'] if record else None),
            opt(record['receipt'] if record else None), len(c['candidates']), *c['candidates']]


def bool_lean(x):
    check(x in (0, 1, False, True), ('not a Boolean', x))
    return 'true' if x else 'false'


def machine_lean(m):
    check(m['alphabet'] == ['a'], 'unary machine')
    return '{ outputs := ' + lean_list(map(bool_lean, m['outputs'])) + ', transitions := ' + \
        lean_list(row[0] for row in m['transitions']) + ', initial := ' + str(m['initial']) + ' }'


def initial_lean(state, config):
    a, p, c = (state[k] for k in ['account', 'physical', 'controller'])
    account = ', '.join(k + ' := ' + str(units(v) if k in ['start','fuel','spent','income'] else v)
                        for k, v in a.items())
    physical = ', '.join(k + ' := ' + str(p[k]) for k in ['phase','source','transferred','wasted'])
    denial = {None:'none', 'commit_applicability':'commit', 'retain_applicability':'retain'}[config['deny_kind']]
    cfg = 'environment := ' + machine_lean(p['environment']) + ', ' + ', '.join(
        name + ' := ' + bool_lean(p[key]) for name,key in [('tau','tau'),('sigma','sigma'),
        ('brokenReset','broken_reset'),('blocked','blocked')]) + \
        ', receiptMode := .' + p['receipt_mode'] + ', clamp := ' + bool_lean(config['clamp']) + \
        ', deny := .' + denial
    check(c['record'] is None and not c['candidates'] and c['expected'] is None and
          c['attempts'] == 0 and not c['retained'] and c['phase'] == 'uninstalled', 'initial control')
    return '{ H := ' + machine_lean(c['H']) + ', config := { ' + cfg + \
        ' }, body := { account := { ' + account + ' }, physical := { ' + physical + \
        ' }, control := { word := ' + str(len(c['word'])) + ', base := ' + str(c['base']) + ' } } }'


def verify_charge(before, event):
    """Check every saved microcharge, independent of formal macro-operation fees."""
    details = event['details']
    a, b = before['account'], event['state']['account']
    work, live, temporary, rewrites = [details[k] for k in ['work','live','temporary','rewrites']]
    peak = max(a['live'], live) + a['workspace'] + temporary
    bill = 1024*work + peak*(work+1) + 1024*(max(0,live-a['live'])+rewrites) + units(details['extra'])
    check(units(details['bill']) == bill, ('microcharge tariff', details))
    expected = dict(a, fuel=str(Fraction(units(a['fuel'])-bill,65536)),
                    spent=str(Fraction(units(a['spent'])+bill,65536)), live=live, peak=max(a['peak'],peak))
    check(b == expected and peak <= a['capacity'] and units(a['fuel']) >= bill,
          ('microcharge mutation or guard', details))
    return bill


def project(case, prefix, label):
    trace, config = case['trace'], case['config']
    boundary = trace[0]['state']
    check(trace[0]['event'] == 'continuation_boundary', label)
    check(boundary['controller']['H'] == prefix['model'] and
          boundary['controller']['word'] == prefix['pending_word'] and
          boundary['physical']['phase'] == prefix['physical_phase'] and
          boundary['account']['live'] == prefix['live'], ('ancestral boundary', label))
    check(units(boundary['account']['start']) + units(trace[0]['details']['withheld_fuel']) == units(prefix['fuel']) and
          boundary['physical']['source'] + trace[0]['details']['withheld_source'] == prefix['source'],
          ('boundary withholding', label))
    immutable_physical = {k:v for k,v in boundary['physical'].items()
                          if k not in ['phase','source','transferred','wasted']}
    for entry in trace:
        check(entry['state']['controller']['H'] == boundary['controller']['H'], ('H mutation',label))
        check({k:v for k,v in entry['state']['physical'].items() if k in immutable_physical} == immutable_physical,
              ('configuration mutation',label))
    events, vectors, locations = [], [vector(boundary)], [dict(kind='observed', index=0)]
    observations = [[0,0,0]]
    local_sensor, local_receipt, actual_arrival = None, None, False
    pending = None
    counts = dict(native_snapshots=len(trace), charges=0, reconstructed_extractions=0,
                  projected_operations=0, observed_operation_states=0)
    def append(op, state, index, kind='observed'):
        nonlocal actual_arrival
        current = vector(state)
        if op == 'extract' and current[9] == vectors[-1][9]-10:
            actual_arrival = current[10] == vectors[-1][10]+10
        events.append(op); vectors.append(vector(state)); locations.append(dict(kind=kind,index=index))
        observations.append([opt(local_sensor),opt(local_receipt),int(actual_arrival)])
        counts['projected_operations'] += 1
        counts['observed_operation_states'] += kind == 'observed'
    def complete(op, state, index, kind='observed'):
        nonlocal pending
        check(pending == op, ('mismatched pending operation',label,index,pending,op))
        append(op,state,index,kind); pending = None
    for i, entry in enumerate(trace[1:],1):
        name, details, state = entry['event'],entry['details'],entry['state']
        if name in ['charge','operation_denied']:
            op = CHARGED[details['kind']]
            if pending == 'extract' and op == 'readReceipt':
                # A failed extraction has no standalone Python snapshot. The next
                # receipt charge records its physical effect. Undo ONLY that fee;
                # extraction's outcome/source change is copied from that observation.
                prior = deepcopy(state)
                if name == 'charge':
                    bill = units(details['bill'])
                    prior['account']['fuel'] = str(Fraction(units(prior['account']['fuel'])+bill,65536))
                    prior['account']['spent'] = str(Fraction(units(prior['account']['spent'])-bill,65536))
                    for k in ['live','peak']:
                        prior['account'][k] = trace[i-1]['state']['account'][k]
                complete('extract',prior,i,'reconstructed_before_receipt_charge')
                counts['reconstructed_extractions'] += 1
            check(pending is None, ('unfinished operation at charge',label,i,pending))
            pending = op
            if name == 'charge':
                verify_charge(trace[i-1]['state'],entry)
                counts['charges'] += 1
            else:
                check(state == trace[i-1]['state'], ('denial changed stored state',label,i))
                complete(op,state,i)
        elif name in COMPLETED:
            if name == 'route_opened':
                local_sensor, local_receipt = None, None
            complete(COMPLETED[name],state,i)
        elif name == 'native_result':
            op = dict(reset='reset',a='advance',read='sense',probe='readReceipt')[details['command']]
            if op == 'sense': local_sensor = details['observation']
            if op == 'readReceipt': local_receipt = details['observation']
            complete(op,state,i)
        elif name == 'native_interrupted':
            if pending is not None:
                complete(pending,state,i)
        elif name == 'route_closed':
            if pending is not None:
                check(pending == 'checkSensor', ('unexpected unfinished operation',label,i,pending))
                complete(pending,trace[i-1]['state'],i-1)
            append('closeRoute',state,i)
        elif name in ['stop_after_acquired_arrival','no_discriminating_productive_word']:
            check(pending is None, ('pending at stop',label,i))
            append('stop' if name == 'stop_after_acquired_arrival' else 'finish',state,i)
        else:
            check(name in ['receipt_acquired_uncommitted','post_first_update_checkpoint','halt'],
                  ('unmapped source event',label,i,name))
            if name == 'receipt_acquired_uncommitted':
                check(details == dict(sensor=local_sensor,receipt=local_receipt),
                      ('uncommitted payload differs from actual return',label,i))
    check(pending is None, ('unfinished final operation',label,pending))
    check(vectors[-1] == vector(trace[-1]['state']), ('final state not covered',label))
    check(len(events) < 100, ('policy horizon insufficient',label))
    reason = next((e['details']['reason'] for e in trace if e['event']=='halt'),None)
    error = 'none'
    if reason:
        error = ('funding' if reason.startswith('funding:') else
                 'capacity' if reason.startswith('capacity:') else
                 dict(source_unavailable='source',receipt_missing='missing',
                      sensory_prediction_mismatch='mismatch', applicability_family_inadequate='emptyFamily',
                      **{'interruption:commit_applicability':'commitDenied',
                         'interruption:retain_applicability':'retentionDenied'})[reason])
    return dict(label=label,initial=initial_lean(boundary,config),events=events,vectors=vectors,
                observations=observations,final_error=error,source_halt_reason=reason,
                source_locations=locations,counts=counts)


def fixtures(projected):
    lines = ['import AcquiredApplicability', 'namespace ApplicabilityFixtures',
             'open AcquiredApplicability', 'set_option maxRecDepth 32768',
             'set_option maxHeartbeats 0']
    for i,p in enumerate(projected):
        stem = 'case' + str(i)
        lines.extend(['-- '+p['label'], 'def '+stem+'Initial : State := '+p['initial'],
          'def '+stem+'Events : List Event := '+lean_list('.'+e for e in p['events']),
          'def '+stem+'Vectors : List (List Nat) := '+lean_list(lean_list(v) for v in p['vectors']),
          'def '+stem+'Observations : List (List Nat) := '+lean_list(lean_list(v) for v in p['observations']),
          'theorem '+stem+'Certified : Runnable '+stem+'Initial '+stem+'Events ∧\n'+
          '    policyWord 100 '+stem+'Initial = '+stem+'Events ∧\n'+
          '    (history '+stem+'Initial '+stem+'Events).map vector = '+stem+'Vectors ∧\n'+
          '    (history '+stem+'Initial '+stem+'Events).map (fun s =>\n'+
          '      [optBoolCode s.body.sensor, optBoolCode s.body.receipt, boolCode s.body.actualArrival]) = '+stem+'Observations ∧\n'+
          '    (run '+stem+'Initial '+stem+'Events).body.error = .'+p['final_error']+' ∧\n'+
          '    nextEvent (run '+stem+'Initial '+stem+'Events) = none := by decide',
          '#print axioms '+stem+'Certified'])
    lines.append('end ApplicabilityFixtures')
    return ('\n\n'.join(lines)+'\n').encode()


def named_declarations(source):
    # Authored modules use one simple top-level namespace each. Compiler-generated
    # auxiliaries are covered transitively, not claimed as separately inventoried.
    namespace = re.search(r'^namespace (\S+)\s*$',source,re.M)
    check(namespace is not None, 'missing declaration namespace')
    return [namespace.group(1)+'.'+name for _,name in re.findall(
        r'^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected)\s+)?'
        r'(def|theorem|lemma|instance|structure|inductive)\s+(\S+)',source,re.M)]


def supplement_audits(sources):
    requested = set()
    declared = set()
    by_module = {}
    for module,data in sources.items():
        source = data.decode()
        namespace = re.search(r'^namespace (\S+)\s*$',source,re.M).group(1)
        for name in re.findall(r'^#print axioms (\S+)\s*$',source,re.M):
            requested.add(name if name.startswith(namespace+'.') else namespace+'.'+name)
        current = named_declarations(source)
        check(current, ('empty declaration inventory',module))
        by_module[module] = current
        declared.update(current)
    missing = sorted(declared-requested)
    audit = 'import ApplicabilityFixtures\nimport ApplicabilityGrounding\n\n'+\
        '\n'.join('#print axioms '+n for n in missing)+'\n'
    sources['CorrespondenceAudit'] = audit.encode()
    check(len([n for n in declared if n.endswith('Certified')]) == 65, '65 finite certificate declarations')
    return dict(declared=len(declared),already_requested=len(requested),supplemented=len(missing),
                complete_inventory=sorted(declared), inventory_by_module=by_module)


def main():
    started = datetime.now(timezone.utc).isoformat()
    data, native, bindings = verify_native_bindings()
    projected = [project(case,data['prefixes']['inverted' if name=='inverted_prefix' else 'ordinary'],
                         'named:'+name) for name,case in data['cases'].items()]
    projected += [project(case,data['prefixes'][case['prefix']],f'grid:{i}:{case["prefix"]}')
                  for i,case in enumerate(data['grid'])]
    check(len(projected) == 65, '65 source histories')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+str(time.time_ns())
    attempt = HERE/'runs'/stamp
    (attempt/'sources').mkdir(parents=True)
    sources = {'GenerativeCore':(CORE/'GenerativeCore.lean').read_bytes(),
               'AcquiredApplicability':(HERE/'AcquiredApplicability.lean').read_bytes(),
               'ApplicabilityProofs':(HERE/'ApplicabilityProofs.lean').read_bytes(),
               'ApplicabilityGrounding':(HERE/'ApplicabilityGrounding.lean').read_bytes(),
               'ApplicabilityFixtures':fixtures(projected)}
    audits = supplement_audits(sources)
    for module,source in sources.items():
        (attempt/'sources'/(module+'.lean')).write_bytes(source)
    (attempt/'projection.json').write_text(json.dumps(projected,indent=2)+'\n')
    for path in [CORE/'GenerativeCore.lean',CORE/'lean-toolchain',HERE/'AcquiredApplicability.lean',
                 HERE/'ApplicabilityProofs.lean',HERE/'ApplicabilityGrounding.lean',
                 HERE/'lean-toolchain',Path(__file__)]:
        bindings[str(path.relative_to(ROOT))] = digest(path)
    version,records = fresh_build(sources,attempt)
    stable = all(digest(ROOT/path)==value for path,value in bindings.items())
    totals = {key:sum(p['counts'][key] for p in projected) for key in projected[0]['counts']}
    receipt = dict(started=started,completed=datetime.now(timezone.utc).isoformat(),
        accepted=len(records)==len(sources) and all(r['passed'] for r in records) and stable,
        source_hashes_stable=stable, compiler=dict(path=str(COMPILER),sha256=COMPILER_SHA256,version=version),
        finite_histories=len(projected),totals=totals, declaration_audit=audits,builds=records,
        source_hashes=bindings,
        projection=dict(path=str((attempt/'projection.json').relative_to(ROOT)),sha256=digest(attempt/'projection.json')),
        scope=['Kernel-checked finite equations: guarded event word, policy-selected event word, every projected stored state, acquired observation coordinates, final error, and policy termination.',
               'Every saved charge is independently validated against exact work/live/workspace/write tariff.',
               'Unsuccessful extraction intermediate is reconstructed from next snapshot by undoing only receipt fee; separately counted.',
               'Logging strings and duplicate audit/microcharge snapshots are not separate formal events.',
               'Pending sensor/receipt coordinates are reconstructed from native-return payloads and checked separately from committed records; actualArrival is extracted from physical stock changes.',
               'Immutable H and apparatus configuration are checked across all native snapshots.',
               'Every explicit named definition, theorem, instance, structure and inductive declaration is audited, including same-line attributes; generated auxiliaries are covered transitively.',
               'The original acquisition prefix remains bound to the accepted native independent check, not re-proved in Lean.',
               'This is finite history correspondence, not general compiler refinement, physical realization, or universal benefit.'])
    (attempt/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(accepted=receipt['accepted'],receipt=str((attempt/'receipt.json').relative_to(ROOT)),totals=totals)),flush=True)
    if not receipt['accepted']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
