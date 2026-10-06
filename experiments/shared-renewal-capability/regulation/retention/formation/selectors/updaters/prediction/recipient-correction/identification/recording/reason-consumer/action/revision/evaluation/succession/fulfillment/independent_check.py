"""Independent reconstruction of the fulfillment-sensitive withdrawal study.

Written from fulfillment/PROTOCOL.md and the accepted succession model's
interface only. The producer (fulfillment/model.py) and its checker were not
read. The accepted succession model is loaded as a separate module instance
and is not edited; its source hash is checked before and after the run.

The register is reconstructed from the accepted trial's own emitted trace for
probe0 (sensing -> bind, acquisition -> latch, write -> four bits). The
register's isolated provision never touches core accounts, so the core
dynamics are those of the accepted model except for the assessment decision,
which is taken at the accepted write point (the accepted `choose` call site).

Run:  python3 -I independent_check.py   (from any directory)
"""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ARMS = ('shared', 'fulfill_k1', 'fulfill_k2_deliver', 'fulfill_k2_hold', 'fulfill_k3')
ARM_K = dict(fulfill_k1=1, fulfill_k2_deliver=2, fulfill_k2_hold=2, fulfill_k3=3)
PROVISION = 6

INTERPRETATIONS = [
    'Register binds iff probe0 actually reaches recipient sensing in the accepted trial and provision >= 1 '
    '(bind costs 1). A source outage (availability False) still reaches sensing in the accepted mechanics, '
    'so it yields a bound, present, receipt-0 record (a certified miss), not an unbound register.',
    'Latch occurs at probe0 actual acquisition: (epoch=1, action, present=int(feedback[0] != missing), '
    'receipt=int(bool(acquired_record))); with a missing channel receipt is 0. Four bits written at probe0 '
    'write if 4 units remain (always true with provision 6).',
    'Register record counts as certified iff complete, epoch-bound (cell0 == 1), present == 1 and receipt == 1; '
    'the action bit does not matter (service meaning is any actual capture). Unknown iff unbound/absent/incomplete '
    'or present == 0. A present receipt-0 record is a certified miss: neither certified nor unknown.',
    'Second-query frame contributes via reader cache entry 1: non-null -> certified 1; null -> counted as unknown '
    'only if the frame itself is absent/unbound/incomplete/present==0, otherwise (present negative) neither. '
    'At a valid assessment cache entry 1 is always non-null, so this choice does not affect decisions.',
    'Status is computed only when the evaluator reaches its paid write (valid assessment), i.e. at the accepted '
    'choose() call site, where the register read (1 isolated unit) is placed. Where the write is not reached, '
    'status is none. Shared arm never reads the register: status none.',
    'register_receipt_forged: after probe0 completes with an actual miss (bound, latched, written), receipt bit '
    'set to 1. Built from the changed config (where the first probe misses for the selected donor).',
    'register_unprovisioned: built from the changed config with register provision 0; no bind, no record -> unknown.',
    'first_feedback_missing_{changed,stable}: feedback[0] = missing in the respective config.',
    'episode deliveries = probe0 capture + probe1 capture + selected capture (actual recipient +10 events).',
    'excess_k = selected capture occurred and probe captures (before it) >= k.',
    'withheld_while_unmet_k = an assessment was written (valid) with value False and probe captures < k; '
    'applies to every arm, including withholdings by the shared rule (n <= 6).',
    'Arm decision: shared: 10n>64. fulfill_k1/k3: shared rule AND pending. k2_deliver: shared AND (pending or unknown). '
    'k2_hold: shared AND pending.',
    'Metric "source" is the core source; "actor" (core fuel) is compared too.',
]


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load_base():
    spec = importlib.util.spec_from_file_location('_indep_fulfillment_base', BASE/'model.py')
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def added_cases(specs):
    by = {r['name']: r['config'] for r in specs['cases']}
    out = []
    for base in ('changed', 'stable'):
        c = deepcopy(by[base]); c['feedback'][0] = 'missing'
        out.append(('first_feedback_missing_'+base, c, dict(forge=False, provision=PROVISION)))
    c = deepcopy(by['changed']); out.append(('register_receipt_forged', c, dict(forge=True, provision=PROVISION)))
    c = deepcopy(by['changed']); out.append(('register_unprovisioned', c, dict(forge=False, provision=0)))
    return out


def build_register(events, opts, feedback0):
    """Register from probe0's actual emitted trace segment."""
    reg = dict(provision=opts['provision'], bound=None, latched=None, cells=[None]*4, written=0,
               complete=False, blocked=[])
    names = [e['event'] for e in events]
    if 'probe0.sense_recipient' in names:
        if reg['provision'] >= 1:
            reg['provision'] -= 1
            work = next(e for e in events if e['event'] == 'probe0.work')
            reg['bound'] = [int(work['state']['bank']['epoch']), work['state']['physical']['core_action']]
        else:
            reg['blocked'].append('bind')
    if 'probe0.acquire' in names and reg['bound'] is not None:
        acq = next(e for e in events if e['event'] == 'probe0.acquire')
        a = acq['state']['physical']
        assert a['core_action'] == reg['bound'][1]
        rec = a['acquired_record']
        assert (rec is None) == (feedback0 == 'missing')
        reg['latched'] = reg['bound'] + [int(rec is not None), int(bool(rec))]
    if 'probe0.write' in names and reg['latched'] is not None:
        for i in range(4):
            if reg['provision'] < 1:
                reg['blocked'].append('write_bit'+str(i)); break
            reg['provision'] -= 1; reg['cells'][i] = reg['latched'][i]; reg['written'] += 1
        reg['complete'] = reg['written'] == 4
        if reg['complete'] and opts['forge'] and reg['cells'][3] == 0:
            # configured provenance mutation after an actual miss
            assert events[[e['event'] for e in events].index('probe0.work')]['state']['outcomes']['probe_receipts'][0] is False
            reg['cells'][3] = 1; reg['forged'] = True
    return reg


def run_one(mod, ref, cfg, arm, catalog, ancestry, opts):
    """Mirror of the accepted run_case schedule with the register and arm decision added."""
    info = dict(status=None, certified=None, unknown=None, assessment_written=False)
    reg_holder = {}
    k = ARM_K.get(arm)

    def decide(s, _arm):
        shared = 10*s['native']['n'] > 64
        if arm == 'shared':
            return shared
        reg = reg_holder['reg']
        # register read (1 isolated unit)
        if reg['provision'] >= 1:
            reg['provision'] -= 1; reg['read'] = list(reg['cells'])
            cells = reg['cells'] if reg['complete'] else None
        else:
            reg['blocked'].append('read'); cells = None
        certified = unknown = 0
        if cells is None or cells[0] != 1 or cells[2] == 0:
            unknown += 1
        elif cells[3] == 1:
            certified += 1
        c1 = s['reader']['cache'][1]
        b = s['bank']
        if c1 is not None:
            certified += 1
        else:
            fr = b['cells'] if b['complete'] else None
            if fr is None or fr[0] != int(b['epoch']) or fr[2] == 0:
                unknown += 1
        if certified >= k: st = 'fulfilled'
        elif certified + unknown < k: st = 'pending'
        else: st = 'unknown'
        info.update(status=st, certified=certified, unknown=unknown)
        if st == 'pending': return shared
        if st == 'unknown' and arm == 'fulfill_k2_deliver': return shared
        return False

    mod.choose = decide
    s = mod.initialize(ref, cfg, catalog, ancestry); tr = []; mod.emit(s, 'extension.at_actual_donor', tr)
    reg_holder['reg'] = dict(provision=opts['provision'], bound=None, latched=None, cells=[None]*4,
                             written=0, complete=False, blocked=[])
    if not s['admitted']:
        return s, tr, info, reg_holder['reg']
    if not mod.assemble(s, cfg, tr) or not mod.copy_candidate(s, cfg, tr) or not mod.bind_access(s, cfg, tr):
        return s, tr, info, reg_holder['reg']
    oldlaw = catalog[ref]['observer']['actual_work_law']
    law = oldlaw ^ (cfg['efficacy_before_probes'] == 'opposite_donor_final_law')
    final_law = law ^ (cfg['efficacy_before_final'] == 'opposite_probe_law')
    start = len(tr)
    mod.trial(s, cfg, law, cfg['availability'][0], cfg['feedback'][0], 'probe0', tr)
    reg_holder['reg'] = build_register(tr[start:], opts, cfg['feedback'][0])
    mod.trial(s, cfg, law, cfg['availability'][1], cfg['feedback'][1], 'probe1', tr)
    mod.read_reasons(s, tr)
    mod.intervene(s, cfg, 'after_consumer', tr)
    mod.evaluate(s, cfg, 'shared', final_law, tr)
    if s['port']['mode'] == 'idle': s['port']['mode'] = 'consumed'
    s['port']['opportunity'] = 'closed'; s['status'] = 'finished'; mod.emit(s, 'continuation.complete', tr)
    return s, tr, info, reg_holder['reg']


def my_metrics(mod, s, info):
    o = s['outcomes']
    pc = o['probe_captures']; sc = int(o['selected_capture'])
    deliveries = pc + sc
    m = dict(positive_assessment=int(o['assessment'] is True), selected_capture=sc,
             recipient=s['core']['recipient'], source=s['core']['source'], actor=s['core']['fuel'],
             n=s['native']['n'], supported_child_command=int(mod.current_command(s) is not None),
             status_fulfilled=int(info['status'] == 'fulfilled'), status_pending=int(info['status'] == 'pending'),
             status_unknown=int(info['status'] == 'unknown'))
    for k in (1, 2, 3):
        m['claim_met_end_k%d' % k] = int(deliveries >= k)
        m['excess_k%d' % k] = int(sc == 1 and pc >= k)
        m['withheld_while_unmet_k%d' % k] = int(o['assessment'] is False and pc < k)
    return m


def main():
    model_hash = sha(BASE/'model.py')
    freeze = json.loads((HERE/'protocol-freeze.json').read_text())
    assert freeze['accepted_model_sha256'] == model_hash, 'accepted model hash differs from protocol freeze'
    mod = load_base()
    specs = json.loads((BASE/'cases.json').read_text())
    old, _ = mod.load_parent(); catalog, ancestry = mod.extract_catalog(old, specs); del old
    cases = [(r['name'], r['config'], dict(forge=False, provision=PROVISION)) for r in specs['cases']]
    cases += added_cases(specs)
    prod = json.loads(gzip.decompress((HERE/'results.json.gz').read_bytes()))
    keys = ['positive_assessment', 'selected_capture', 'recipient', 'source', 'actor', 'n',
            'supported_child_command', 'status_fulfilled', 'status_pending', 'status_unknown']
    keys += ['%s_k%d' % (b, k) for b in ('claim_met_end', 'excess', 'withheld_while_unmet') for k in (1, 2, 3)]
    mismatches = []; compared = paths = 0; config_notes = []
    mine_totals = {}
    for name, cfg, opts in cases:
        pc = prod['cases'].get(name)
        if pc is None:
            mismatches.append(dict(case=name, issue='case missing in producer output')); continue
        pcfg = dict(pc['config'])
        extra = {k: pcfg.pop(k) for k in list(pcfg) if k not in cfg}
        if pcfg != cfg:
            config_notes.append(dict(case=name, issue='producer config differs from reconstruction',
                                     differing={k: [cfg.get(k), pcfg.get(k)] for k in set(cfg) | set(pcfg) if cfg.get(k) != pcfg.get(k)}))
        if extra: config_notes.append(dict(case=name, producer_extra_keys=extra))
        for arm in ARMS:
            for producer in specs['producers']:
                prows = pc['arms'][arm]['producers'][producer]['paths']
                refs = [r for r, e in catalog.items() if e['parent_case'] == cfg['parent_case'] and e['producer'] == producer]
                if len(refs) != len(prows):
                    mismatches.append(dict(case=name, arm=arm, producer=producer, issue='path count', mine=len(refs), producer_count=len(prows)))
                tot = {}
                for i, ref in enumerate(refs):
                    s, tr, info, reg = run_one(mod, ref, cfg, arm, catalog, ancestry, opts)
                    m = my_metrics(mod, s, info); paths += 1
                    mass = Q(catalog[ref]['probability'])
                    for kk, v in m.items(): tot[kk] = tot.get(kk, Q(0)) + mass*v
                    if i >= len(prows): continue
                    pr = prows[i]
                    where = dict(case=name, arm=arm, producer=producer, path=i, ref=ref)
                    if pr['predecessor_ref'] != ref:
                        mismatches.append(dict(where, key='predecessor_ref', mine=ref, producer_value=pr['predecessor_ref']))
                    if Q(pr['probability']) != mass:
                        mismatches.append(dict(where, key='probability', mine=str(mass), producer_value=pr['probability']))
                    for kk in keys:
                        compared += 1
                        pv = pr['metrics'].get(kk)
                        if pv != m[kk]:
                            mismatches.append(dict(where, key=kk, mine=m[kk], producer_value=pv))
                    pstat = (pr.get('fulfillment') or {}).get('status')
                    compared += 1
                    if (pstat or None) != info['status']:
                        mismatches.append(dict(where, key='fulfillment.status', mine=info['status'], producer_value=pstat))
                    if info['status'] is not None:
                        f = pr.get('fulfillment') or {}
                        for kk in ('certified', 'unknown'):
                            compared += 1
                            if f.get(kk) != info[kk]:
                                mismatches.append(dict(where, key='fulfillment.'+kk, mine=info[kk], producer_value=f.get(kk)))
                    # selected capture decision consistent
                mine_totals.setdefault(name, {}).setdefault(arm, {})[producer] = {kk: str(v) for kk, v in sorted(tot.items())}
                pm = pc['arms'][arm]['producers'][producer].get('metrics', {})
                for kk, v in tot.items():
                    if kk in pm:
                        compared += 1
                        if Q(pm[kk]) != v:
                            mismatches.append(dict(case=name, arm=arm, producer=producer, key='mixture.'+kk, mine=str(v), producer_value=pm[kk]))
        print(name, 'done', len(mismatches), flush=True)
    assert sha(BASE/'model.py') == model_hash
    by_key = {}
    for mm in mismatches: by_key[mm.get('key', mm.get('issue'))] = by_key.get(mm.get('key', mm.get('issue')), 0) + 1
    # prediction-style summaries from my reconstruction
    result = dict(
        status='match' if not mismatches else 'mismatch',
        scope='Independent reconstruction from PROTOCOL.md and the accepted succession model interface; producer and its checker not read.',
        accepted_model_sha256=model_hash,
        protocol_sha256=sha(HERE/'PROTOCOL.md'),
        producer_results_sha256=sha(HERE/'results.json.gz'),
        counts=dict(cases=len(cases), arms=len(ARMS), producers=len(specs['producers']), histories=paths,
                    compared_values=compared, mismatches=len(mismatches), mismatches_by_key=by_key),
        config_notes=config_notes,
        mismatches=mismatches[:200],
        interpretations=INTERPRETATIONS,
        mixture_totals_checked='per-arm/producer mixture-weighted totals of the compared metrics also compared against producer metrics where present',
    )
    (HERE/'independent-check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['counts'], indent=1))
    return result


if __name__ == '__main__':
    main()
