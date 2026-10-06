"""Fulfillment-sensitive withdrawal on the accepted succession model.

Implements PROTOCOL.md. The accepted model is loaded as a separate module
instance; selected functions of that instance are wrapped to add the
first-probe receipt register and the fulfillment evaluator. No accepted file
is edited; its hash is checked before and after the run. Observer facts
(laws, probe captures) never reach a policy decision.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import datetime
import gzip
import hashlib
import importlib.util
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'model.py'
FREEZE = json.loads((HERE / 'protocol-freeze.json').read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


assert sha(HERE / 'PROTOCOL.md') == FREEZE['protocol_sha256'], 'protocol changed after freeze'
assert sha(BASE) == FREEZE['accepted_model_sha256'], 'accepted model changed'
spec = importlib.util.spec_from_file_location('_fulfillment_base', BASE)
acc = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = acc
spec.loader.exec_module(acc)
identification = acc.identification

ARMS = ('shared', 'fulfill_k1', 'fulfill_k2_deliver', 'fulfill_k2_hold', 'fulfill_k3')
CLAIMS = (1, 2, 3)

_orig = dict(initialize=acc.initialize, retained=acc.retained, bind_frame=acc.bind_frame,
             latch_frame=acc.latch_frame, write_frame=acc.write_frame)


# ---------------------------------------------------------------- accounts

def initialize(ref, cfg, catalog, ancestry):
    s = _orig['initialize'](ref, cfg, catalog, ancestry)
    provision = cfg.get('register_provision', 6)
    s['register'] = dict(provision=provision, initial=provision, bound=None, latched=None,
                         cells=[None] * 4, written=0, complete=False, read=None,
                         forge=bool(cfg.get('register_forge', False)))
    s['new_spent']['register'] = 0
    s['accounting']['initial_retained'] += provision
    s['fulfillment'] = None
    return s


def retained(s):
    return _orig['retained'](s) + (s['register']['provision'] if 'register' in s else 0)


def emit(s, event, tr):
    """Accepted snapshot checks with the register provision added to the total."""
    reg = s['register']['provision'] if 'register' in s else 0
    extra = s['register']['initial'] if 'register' in s else 0
    values = [s['core'][k] for k in acc.CORE_MONEY] + list(s['old_accounts'].values()) + list(s['reserves'].values())
    values += list(s['idle_common'].values()) + s['native']['packets'] + [
        s['source_reserve'], s['idle_source'], s['bank']['budget'], s['bank']['escrow'], s['reader']['fuel'], reg]
    assert min(values) >= 0, event
    assert set(s['parts']) == set(acc.COMPONENTS) and all(v in ('held', 'built', 'omitted') for v in s['parts'].values())
    assert retained(s) + sum(s['new_spent'].values()) + s['new_waste'] == s['accounting']['initial_retained'], event
    assert s['accounting']['historical_spent'] + 18 + retained(s) + sum(s['new_spent'].values()) + s['new_waste'] == 590 + extra, event
    if s['owner'] == 'child':
        assert s['donor_status'] == 'retired' and s['retired'] is not None
    if s['copy_latch'] is not None:
        assert s['donor_status'] == 'quiesced' and s['owner'] == 'donor'
    tr.append(dict(event=event, state=deepcopy(s)))


# ---------------------------------------------------------------- register

def bind_frame(s, tr):
    b = s['bank']; g = s['register']; a = s['physical']
    if b['current'] == 0:
        if (s['owner'] == 'child' and s['child_status'] == 'commissioned' and b['live']
                and a['core_phase'] == 'sensed' and a['core_target'] == 'recipient'
                and g['bound'] is None and g['provision'] >= 1):
            g['provision'] -= 1; s['new_spent']['register'] += 1
            g['bound'] = [int(b['epoch']), identification.read(s['core']['q'], 'recipient')]
            emit(s, 'register.bind_probe0', tr)
        else:
            emit(s, 'register.bind_blocked', tr)
    _orig['bind_frame'](s, tr)


def latch_frame(s, tr):
    b = s['bank']; g = s['register']; a = s['physical']
    if (b['current'] == 0 and g['bound'] is not None and g['latched'] is None
            and a['core_phase'] == 'acquired' and a['core_target'] == 'recipient'
            and g['bound'] == [int(b['epoch']), a['core_action']]):
        r = a['acquired_record']
        g['latched'] = g['bound'] + [int(r is not None), int(bool(r))]
        emit(s, 'register.latch_probe0', tr)
        if g['forge'] and g['latched'][2] == 1 and g['latched'][3] == 0:
            # Configured provenance fault, labeled as such (PROTOCOL case 2).
            g['latched'][3] = 1
            emit(s, 'fault.register_receipt_forged', tr)
    _orig['latch_frame'](s, tr)


def write_frame(s, tr):
    b = s['bank']; g = s['register']
    if (b['current'] == 0 and g['latched'] is not None and not g['complete']
            and s['physical']['core_phase'] == 'ready'):
        while g['written'] < 4:
            if g['provision'] < 1:
                emit(s, 'register.write_blocked', tr); break
            i = g['written']; g['cells'][i] = g['latched'][i]; g['written'] += 1
            g['provision'] -= 1; s['new_spent']['register'] += 1
            if g['written'] == 4:
                g['complete'] = True
            emit(s, 'register.write_bit' + str(i), tr)
    _orig['write_frame'](s, tr)


# ---------------------------------------------------------------- evaluator

def arm_claim(arm):
    if arm == 'shared':
        return None, None
    k = int(arm.split('_')[1][1])
    return k, ('hold' if arm.endswith('hold') else 'deliver')


def read_register(s, tr):
    """Paid read of the register during evaluation; returns its record or None."""
    g = s['register']
    if not g['complete']:
        emit(s, 'register.read_unavailable', tr); return None
    if g['provision'] < 1:
        emit(s, 'register.read_blocked', tr); return None
    g['provision'] -= 1; s['new_spent']['register'] += 1
    g['read'] = list(g['cells']); emit(s, 'register.read', tr)
    return g['read']


def status(s, record, k):
    epoch = int(s['bank']['epoch'])
    certified = unknown = 0
    # First probe: register record.
    if record is None or record[0] != epoch or not record[2]:
        unknown += 1
    elif record[3]:
        certified += 1
    # Second query: the reader's validated factual cache entry 1 is non-null
    # exactly for a complete, epoch-bound, present, positive frame.
    if s['reader']['cache'][1] is not None and s['reader']['cache_valid']:
        certified += 1
    else:
        unknown += 1
    if certified >= k:
        return 'fulfilled', certified, unknown
    if certified + unknown < k:
        return 'pending', certified, unknown
    return 'unknown', certified, unknown


def evaluate(s, cfg, arm, law, tr):
    """The accepted paid evaluation with the fulfillment decision added."""
    p = s['port']; c = s['core']
    if not (s['child_status'] == 'commissioned' and s['parts']['port'] == 'built'
            and p['mode'] == 'idle' and p['opportunity'] == 'due'
            and s['physical']['core_phase'] == 'ready' and c['fuel'] >= 1):
        emit(s, 'evaluation.read_blocked', tr); return False
    c['fuel'] -= 1; s['new_spent']['evaluation_read'] += 1
    valid = acc.assessment_valid(s); p['mode'] = 'read' if valid else 'consumed'
    p['read_command'] = acc.current_command(s) if valid else None; emit(s, 'evaluation.read', tr)
    k, unknown_policy = arm_claim(arm)
    record = read_register(s, tr) if (k is not None and valid) else None
    acc.intervene(s, cfg, 'after_evaluation_read', tr)
    if not (p['mode'] == 'read' and acc.assessment_valid(s) and p['read_command'] == acc.current_command(s) and c['fuel'] >= 1):
        emit(s, 'evaluation.write_blocked', tr); return False
    c['fuel'] -= 1; s['new_spent']['evaluation_write'] += 1
    helping = acc.choose(s, 'shared')
    if k is not None:
        st, certified, unknown = status(s, record, k)
        s['fulfillment'] = dict(k=k, status=st, certified=certified, unknown=unknown,
                                acquired_help=helping, unknown_policy=unknown_policy)
        helping = helping and (st == 'pending' or (st == 'unknown' and unknown_policy == 'deliver'))
    p['mode'] = 'assessed_help' if helping else 'assessed_abstain'
    s['outcomes']['assessment'] = helping; emit(s, 'evaluation.write', tr)
    if helping:
        acc.trial(s, cfg, law, cfg['availability'][2], cfg['feedback'][2], 'selected', tr)
    else:
        p.update(mode='consumed', read_command=None); emit(s, 'evaluation.abstain', tr)
    return True


acc.initialize = initialize
acc.retained = retained
acc.emit = emit
acc.bind_frame = bind_frame
acc.latch_frame = latch_frame
acc.write_frame = write_frame
acc.evaluate = evaluate


# ---------------------------------------------------------------- cases

def added_cases(specs):
    base = {r['name']: r['config'] for r in specs['cases']}
    def variant(src, **changes):
        cfg = deepcopy(base[src]); cfg.update(changes); return cfg
    return [
        dict(name='first_feedback_missing_changed', config=variant('changed', feedback=['missing', 'faithful', 'faithful'])),
        dict(name='first_feedback_missing_stable', config=variant('stable', feedback=['missing', 'faithful', 'faithful'])),
        dict(name='register_receipt_forged', config=variant('changed', register_forge=True)),
        dict(name='register_unprovisioned', config=variant('changed', register_provision=0)),
    ]


def metrics(s, catalog):
    out = acc.metrics(s, catalog)
    o = s['outcomes']
    deliveries = o['probe_captures'] + int(o['selected_capture'])
    before = o['probe_captures']
    assessed = o['assessment'] is not None
    for k in CLAIMS:
        out[f'claim_met_end_k{k}'] = int(deliveries >= k)
        out[f'excess_k{k}'] = int(bool(o['selected_capture']) and before >= k)
        out[f'withheld_while_unmet_k{k}'] = int(assessed and o['assessment'] is False and before < k)
    f = s['fulfillment'] or {}
    for st in ('fulfilled', 'pending', 'unknown'):
        out['status_' + st] = int(f.get('status') == st)
    out['acquired_help'] = int(bool(f.get('acquired_help')))
    out['register_complete'] = int(s['register']['complete'])
    out['register_provision_left'] = s['register']['provision']
    out['episode_deliveries'] = deliveries
    out['first_probe_capture'] = int(bool(o['probe_receipts'][:1] and o['probe_receipts'][0]))
    return out


def main():
    acc.verify_freeze()
    before = dict(accepted=acc.sources(), protocol=sha(HERE / 'PROTOCOL.md'), base=sha(BASE), producer=sha(__file__))
    specs = json.loads((BASE.parent / 'cases.json').read_text())
    cases = specs['cases'] + added_cases(specs)
    old, _ = acc.load_parent(); catalog, ancestry = acc.extract_catalog(old, specs)
    output = dict(source_sha256=before, arms=list(ARMS), cases={})
    histories = prefixes = 0
    for row in cases:
        name, cfg = row['name'], row['config']; arms = {}
        for arm in ARMS:
            producers = {}
            for producer in specs['producers']:
                paths = []; totals = defaultdict(Q)
                for ref, entry in catalog.items():
                    if entry['parent_case'] != cfg['parent_case'] or entry['producer'] != producer:
                        continue
                    state, tr = acc.run_case(ref, cfg, arm, catalog, ancestry)
                    m = metrics(state, catalog); mass = Q(entry['probability'])
                    for key, v in m.items():
                        totals[key] += mass * v
                    paths.append(dict(predecessor_ref=ref, probability=str(mass), metrics=m,
                                      fulfillment=state['fulfillment'], register=state['register'],
                                      events=[t['event'] for t in tr],
                                      trace_sha256=acc.object_hash(tr), final_state_sha256=acc.object_hash(state)))
                    histories += 1; prefixes += len(tr)
                assert sum(Q(p['probability']) for p in paths) == 1
                producers[producer] = dict(metrics={k: str(v) for k, v in sorted(totals.items())}, paths=paths)
            arms[arm] = dict(producers=producers)
        output['cases'][name] = dict(config=cfg, arms=arms)
        print(name, 'completed', flush=True)
    acc.verify_freeze()
    after = dict(accepted=acc.sources(), protocol=sha(HERE / 'PROTOCOL.md'), base=sha(BASE), producer=sha(__file__))
    assert after == before, 'sources changed during run'
    raw = (json.dumps(output, sort_keys=True, separators=(',', ':')) + '\n').encode()
    packed = gzip.compress(raw, mtime=0); (HERE / 'results.json.gz').write_bytes(packed)
    counts = dict(cases=len(cases), arms=len(ARMS), producers=len(specs['producers']),
                  histories=histories, prefixes=prefixes)
    files = dict(file='results.json.gz', compressed_sha256=hashlib.sha256(packed).hexdigest(),
                 uncompressed_sha256=hashlib.sha256(raw).hexdigest(), counts=counts)
    (HERE / 'result-files.json').write_text(json.dumps(files, indent=2) + '\n')
    report = {name: {arm: {prod: d['metrics'] for prod, d in a['producers'].items()}
                     for arm, a in c['arms'].items()} for name, c in output['cases'].items()}
    (HERE / 'reporting.json').write_text(json.dumps(dict(source_sha256=before, counts=counts, cases=report), indent=2) + '\n')
    return dict(status='producer_run_complete_pending_checks', source_sha256=before, counts=counts, result_files=files)


if __name__ == '__main__':
    receipt = HERE / 'first-run-receipt.json'
    assert not receipt.exists(), 'Preserve the first run; reruns need a new explicit receipt.'
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        result = main(); result['started_utc'] = started
        receipt.write_text(json.dumps(result, indent=2) + '\n')
    except BaseException:
        failure = dict(status='failed', started_utc=started, error=traceback.format_exc())
        receipt.write_text(json.dumps(failure, indent=2) + '\n')
        raise
