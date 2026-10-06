"""Additive inquiry revision on the preserved actual plasticity runtime.

The original source is imported unchanged. Only its trace emitter is replaced
in this isolated module instance so that the converted spare pair and reused
latches are accounted for. Original pair, assessment and service laws execute.
"""
from copy import deepcopy
from pathlib import Path
import datetime
import gzip
import hashlib
import importlib.util
import itertools
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('_inquiry_original_plasticity', BASE / 'model.py')
old = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = old
spec.loader.exec_module(old)
EXTRA_COSTS = ('inquiry_assembly', 'inquiry_read', 'inquiry_commit')
REF = 'primary/variable/11/37'
MODES = ('absent', 'idle', 'observed', 'missing', 'stale', 'committed')
CHANNELS = ('faithful', 'missing', 'zero', 'falsePositive', 'wrongBinding')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def material(s):
    i = s['inventory']
    pairs = (i['memory_cells'] + int(i['adapter']) + int(s['port']['built'])
             + i['omitted_pairs'] + sum(i['free_primary'])
             + int(i['replacement_free']) + len(s['retired'])
             + sum(x is not None for x in s['links'])
             + int(s['inquiry']['mode'] != 'absent'))
    return 42 + 2 * pairs


def emit(s, event, trace):
    assert s['inquiry']['mode'] in MODES
    assert 0 <= s['native']['n'] <= 7 and 0 <= s['native']['count'] <= 6
    assert material(s) == 68, event
    c = s['core']
    assert min(*(c[k] for k in ('fuel', 'recipient', 'source', 'escrow')),
               *s['reserves'].values(), *s['packets']['own'], *s['packets']['recipient']) >= 0
    objects = [x for x in s['links'] if x is not None] + s['retired']
    assert len({x['id'] for x in objects}) == len(objects)
    assert all(x['sign'] in (-1, 0, 1) for x in objects)
    total = old.retained(s) + sum(s['costs'].values()) + s['waste']
    assert total == s['accounting']['initial_retained'], (event, total)
    assert total + s['accounting']['parent_spent'] + s['accounting']['extra_construction_spent'] == 505
    for cell in s['native']['latches'].values():
        assert isinstance(cell['value'], bool)
        assert cell['mode'] in ('empty', 'return', 'shortfall', 'missing', 'occupancy')
        if cell['mode'] in ('empty', 'missing'):
            assert not cell['value']
    trace.append(dict(event=event, state=deepcopy(s)))


old.emit = emit


def load_fixture():
    with gzip.open(BASE / 'results.json.gz', 'rt') as f:
        saved = json.load(f)
    catalog = saved['parent_catalog']
    config = saved['cases']['aligned_revision']['config']
    variants = json.loads((BASE / 'cases.json').read_text())['variants']
    return saved, catalog, config, variants


def prefix(fixture, own=(1, 0, 0, 1), affected=(1, 0, 0, 1), variant='active'):
    saved, catalog, base_config, variants = fixture
    cfg = deepcopy(base_config)
    cfg['own_shortfalls'][:4] = own
    cfg['recipient_shortfalls'][:4] = affected
    s = old.initialize(REF, cfg, variants[variant], saved['preparations']['aligned_revision'], catalog)
    s['inquiry'] = dict(mode='absent')
    s['costs'].update(dict.fromkeys(EXTRA_COSTS, 0))
    trace = []
    emit(s, 'extension.at_actual_parent_prefix', trace)
    assert old.admitted(s, catalog)
    completed = True
    for _ in range(4):
        if not old.pair(s, cfg, trace):
            completed = False
            break
    return s, trace, cfg, completed


def clear_bits(s):
    for cell in s['native']['latches'].values():
        cell.update(value=False, mode='empty')


def release(s):
    """Invalidate acquired monitor evidence before an inherited event."""
    mode = s['inquiry']['mode']
    if mode in ('observed', 'missing', 'stale'):
        clear_bits(s)
        s['inquiry']['mode'] = 'idle'


def context(s, catalog):
    return bool(s['native']['count'] == 4 and s['native']['phase'] == 'ready'
                and s['controls']['training_limit'] == 6 and not s['retired']
                and old.admitted(s, catalog) and old.applicable(s, catalog)
                and s['binding']['permission'])


def enabled(s, event, catalog):
    mode = s['inquiry']['mode']
    common = context(s, catalog) and s['core']['fuel'] >= 1
    if event == 'assemble':
        return common and mode == 'absent' and s['inventory']['replacement_free']
    if event.startswith('inspect:'):
        assert event.split(':')[1] in CHANNELS
        return common and mode in ('idle', 'missing', 'stale')
    if event in ('commit', 'shamCommit'):
        return common and mode == 'observed' and all(x['value'] for x in s['native']['latches'].values())
    raise ValueError(event)


def step(s, event, catalog, trace):
    """Disabled events are recorded without a state mutation or charge."""
    if not enabled(s, event, catalog):
        emit(s, 'inquiry.' + event + '.blocked', trace)
        return False
    s['core']['fuel'] -= 1
    if event == 'assemble':
        s['costs']['inquiry_assembly'] += 1
        s['inventory']['replacement_free'] = False
        s['inquiry']['mode'] = 'idle'
    elif event.startswith('inspect:'):
        s['costs']['inquiry_read'] += 1
        channel = event.split(':')[1]
        occupancy = sum(x is not None for x in s['links'])
        values = (occupancy >= 1, occupancy >= 2)
        if channel in ('missing', 'zero', 'wrongBinding'):
            values = (False, False)
        elif channel == 'falsePositive':
            values = (True, True)
        for key, value in zip(('own', 'recipient'), values):
            s['native']['latches'][key].update(value=value, mode='occupancy')
        s['inquiry']['mode'] = {'missing': 'missing', 'wrongBinding': 'stale'}.get(channel, 'observed')
    else:
        s['costs']['inquiry_commit'] += 1
        clear_bits(s)
        if event == 'commit':
            s['controls']['training_limit'] = 4
            s['inquiry']['mode'] = 'committed'
        else:
            s['inquiry']['mode'] = 'idle'
    emit(s, 'inquiry.' + event, trace)
    return True


def inherited_cut(s, kind, value, trace):
    release(s)
    if kind in ('scope', 'permission', 'delivery'):
        s['binding'][kind] = value
    else:
        raise ValueError(kind)
    if s['port']['mode'] != 'idle':
        s['port']['mode'] = 'consumed'
    s['port']['read_command'] = None
    emit(s, 'inherited.' + kind + ':' + str(value).lower(), trace)


def response(s, catalog, trace):
    release(s)
    if old.assess(s, catalog, trace):
        if s['port']['mode'] == 'assessed_help':
            old.service(s, catalog, catalog[REF]['observer']['final_law'], trace)
        else:
            s['port']['mode'] = 'consumed'
            emit(s, 'evaluation.abstain', trace)


def summary(s):
    return dict(n=s['native']['n'], count=s['native']['count'], fuel=s['core']['fuel'],
                affected=s['core']['recipient'], energy=old.retained(s), material=material(s),
                limit=s['controls']['training_limit'], mode=s['inquiry']['mode'],
                occupied=sum(x is not None for x in s['links']),
                signs=[x['sign'] if x is not None else None for x in s['links']],
                service=s['outcomes']['completed'], captured=s['outcomes']['captured'],
                assessment=s['outcomes']['assessment'], costs=deepcopy(s['costs']))


def original_projection(s):
    r = deepcopy(s)
    del r['inquiry']
    for key in EXTRA_COSTS:
        del r['costs'][key]
    return r


def run():
    fixture = load_fixture()
    saved, catalog, _, _ = fixture
    source_paths = [BASE/'model.py', BASE/'results.json.gz', BASE/'cases.json',
                    BASE/'formal/PairedPlasticity.lean', BASE/'formal/PlasticityWitness.lean',
                    HERE/'model.py', HERE/'PROTOCOL.md']
    source_hashes = {str(p.relative_to(REPO)): digest(p) for p in source_paths}
    histories = {}
    def arm(name, own=(1, 0, 0, 1), affected=(1, 0, 0, 1), channel='faithful',
            mutation=None, sham=False, cut=None, reacquire=False, omit_read=False):
        s, trace, cfg, complete = prefix(fixture, own, affected)
        assert complete
        entry = len(trace)-1
        if mutation == 'no_part':
            s['inventory']['replacement_free'] = False
            s['inventory']['omitted_pairs'] += 1
            emit(s, 'fixture.withheld_spare_pair', trace)
        elif mutation is not None and mutation.startswith('fuel:'):
            amount = int(mutation.split(':')[1])
            s['reserves']['idle_common'] += s['core']['fuel']-amount
            s['core']['fuel'] = amount
            emit(s, 'fixture.withheld_fuel', trace)
        if cut == 'before_scope':
            inherited_cut(s, 'scope', False, trace)
        if cut == 'before_permission':
            inherited_cut(s, 'permission', False, trace)
        step(s, 'assemble', catalog, trace)
        if not omit_read:
            step(s, 'inspect:'+channel, catalog, trace)
        if cut in ('scope', 'permission', 'delivery', 'noop', 'restore'):
            kind = cut if cut in ('scope', 'permission', 'delivery') else 'scope'
            inherited_cut(s, kind, cut == 'noop', trace)
            if cut == 'restore':
                inherited_cut(s, 'scope', True, trace)
            if reacquire:
                step(s, 'inspect:faithful', catalog, trace)
        step(s, 'shamCommit' if sham else 'commit', catalog, trace)
        response(s, catalog, trace)
        histories[name] = dict(entry_index=entry, own=list(own), affected=list(affected),
            channel=channel, mutation=mutation, cut=cut, reacquire=reacquire,
            omit_read=omit_read, sham=sham, trace=trace, result=summary(s))
        return s

    arm('faithful')
    arm('opposed', affected=(0, 1, 1, 0))
    arm('mixed', affected=(1, 1, 0, 0))
    arm('zero_history', affected=(0, 0, 0, 0))
    arm('one_history', affected=(1, 0, 0, 0))
    for channel in ('missing', 'zero', 'wrongBinding'):
        arm(channel, channel=channel)
    arm('false_positive_zero_history', affected=(0, 0, 0, 0), channel='falsePositive')
    arm('sham', sham=True)
    arm('omitted_read', omit_read=True)
    arm('no_part', mutation='no_part')
    for f in (0, 1, 2, 3, 12):
        arm('fuel_'+str(f), mutation='fuel:'+str(f))
    for cut in ('before_scope', 'before_permission', 'scope', 'permission', 'delivery', 'noop', 'restore'):
        arm('cut_'+cut, cut=cut)
    arm('reacquired', cut='restore', reacquire=True)

    # Exact immutable continuing prefix: no sibling entry was substituted.
    actual = next(r for r in saved['cases']['aligned_revision']['variants']['active']['producers']['variable']['paths']
                  if r['predecessor_ref'] == REF)
    trace = histories['faithful']['trace']
    for expected, observed in zip(actual['runtime_trace'], trace[:33]):
        assert expected['event'] == observed['event']
        assert expected['state'] == original_projection(observed['state'])
    assert len(trace[:33]) == 33
    main = histories['faithful']['result']
    assert (main['count'], main['fuel'], main['affected'], main['energy'], main['material']) == (4, 1, 46, 75, 68)
    assert main['captured'] and main['service'] and main['limit'] == 4
    assert all(row['state']['core']['recipient'] >= 36 for row in trace[32:])

    enumeration = []
    for own in itertools.product((0, 1), repeat=4):
        for affected in itertools.product((0, 1), repeat=4):
            s, rows, cfg, complete = prefix(fixture, own, affected)
            before = summary(s)
            revised = False
            if complete:
                assert s['core']['recipient'] + 2*sum(x is not None for x in s['links']) == 40
                step(s, 'assemble', catalog, rows)
                step(s, 'inspect:faithful', catalog, rows)
                revised = step(s, 'commit', catalog, rows)
                response(s, catalog, rows)
            enumeration.append(dict(own=list(own), affected=list(affected), complete=complete,
                                    before=before, revised=revised, after=summary(s), trace=rows))
    assert sum(x['complete'] for x in enumeration) == 176
    assert sum(x['revised'] for x in enumeration) == 96
    assert source_hashes == {str(p.relative_to(REPO)): digest(p) for p in source_paths}
    result = dict(protocol='PROTOCOL.md', source_sha256=source_hashes, parent_ref=REF,
                  source_parent_sha256=catalog[REF]['state_sha256'],
                  histories=histories, enumeration=enumeration)
    raw = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    data = gzip.compress(raw, mtime=0)
    (HERE/'results.json.gz').write_bytes(data)
    report = dict(status='producer_passed_pending_independent_review',
                  source_sha256=source_hashes, histories=len(histories),
                  enumeration=len(enumeration), completed=176, blocked=80, revised=96,
                  result_sha256=hashlib.sha256(data).hexdigest(),
                  cases={k:v['result'] for k,v in histories.items()})
    (HERE/'reporting.json').write_text(json.dumps(report, indent=2)+'\n')
    return report


if __name__ == '__main__':
    attempts = HERE/'attempts'
    attempts.mkdir(exist_ok=True)
    path = attempts/(datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
    try:
        result = run()
        path.write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k not in ('cases','source_sha256')}))
    except BaseException as error:
        path.write_text(json.dumps(dict(status='failed', error=str(error), traceback=traceback.format_exc(),
            model_sha256=digest(__file__)), indent=2)+'\n')
        raise
