"""Independent applicability continuation reconstruction.

This checker does not import the producer, its controller, native port, or
account implementation.  It treats the saved ancestral acquisition as a
previously accepted boundary, checks its exact event ledger and observations,
and independently reconstructs the new protocol's continuation.
"""
from collections import deque
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def exact(actual, expected, location):
    require(actual == expected,
            f'{location}: actual={actual!r}, expected={expected!r}')


def answer(machine, word):
    q = machine['initial']
    for letter in word:
        q = machine['transitions'][q][machine['alphabet'].index(letter)]
    return machine['outputs'][q]


def sensor_equivalence(learned, physical, flip):
    """All-word test by exhausting the reachable finite product graph."""
    todo = deque([(learned['initial'], physical['initial'])])
    seen = set()
    while todo:
        left, right = todo.popleft()
        if (left, right) in seen:
            continue
        seen.add((left, right))
        exact(learned['outputs'][left], physical['outputs'][right] ^ flip,
              'all-word sensory output')
        exact(learned['alphabet'], physical['alphabet'], 'product alphabet')
        for column in range(len(learned['alphabet'])):
            todo.append((learned['transitions'][left][column],
                         physical['transitions'][right][column]))
    return len(seen)


def ancestral_boundaries(ancestor):
    """Recheck saved charges and native readings; do not rerun old learning."""
    tariff = {k: F(v) for k, v in ancestor['tariffs'].items()}
    target = ancestor['primary_target']
    result = {}
    for name, flip in [('primary_unary', 0), ('inverted_sensor', 1)]:
        case = ancestor['cases'][name]
        fuel, spent, live, peak = F(36), F(0), 0, 0
        totals = {}
        for i, event in enumerate(case['events']):
            kind, work = event['kind'], event['work']
            new_live = event['live']
            temporary = event['temporary']
            envelope = max(live, new_live) + event['workspace'] + temporary
            extra = {'installation': tariff['install'],
                     'target_reset': tariff['reset'],
                     'target_action': tariff['action'],
                     'endpoint_read': tariff['read'],
                     'extraction_work': tariff['read']}.get(kind, F(0))
            if kind == 'retention_epoch':
                extra = tariff['final_rent'] * new_live
            bill = tariff['scale'] * (
                extra + tariff['work'] * work
                + tariff['rent'] * envelope * (work + 1)
                + tariff['write'] * max(0, new_live - live))
            require(envelope <= 256 and fuel >= bill, (name, i, 'affordability'))
            exact(event['peak'], envelope, (name, i, 'peak'))
            exact(event['duration'], work + 1, (name, i, 'duration'))
            exact(F(event['bill']), bill, (name, i, 'bill'))
            fuel -= bill
            spent += bill
            live, peak = new_live, max(peak, envelope)
            totals[kind] = totals.get(kind, F(0)) + bill
            exact(F(event['fuel']), fuel, (name, i, 'fuel'))
        exact(F(case['fuel']), fuel, (name, 'final ancestral fuel'))
        exact(F(case['spent']), spent, (name, 'ancestral expenditure'))
        exact(case['peak_cells'], peak, (name, 'ancestral peak'))
        exact({k: F(v) for k, v in case['costs'].items()}, totals,
              (name, 'ancestral cost categories'))
        for query in case['queries']:
            exact(query['output'], answer(target, query['word']) ^ flip,
                  (name, 'actual endpoint observation', query['word']))
        word = case['use']['word']
        prefix = case['events'][:-(len(word) + 2)]
        tail = case['events'][-(len(word) + 2):]
        exact([e['kind'] for e in tail],
              ['target_reset'] + ['target_action'] * len(word) + ['extraction_work'],
              (name, 'first use suffix'))
        exact(answer(case['model'], word), 1, (name, 'inherited planned reading'))
        require(case['certified'] and case['retained'], (name, 'inherited certificate'))
        product_states = sensor_equivalence(case['model'], target, flip)
        result[name] = dict(events=prefix, model=case['model'], word=word,
                            fuel=prefix[-1]['fuel'], source=20, live=15,
                            phase=len(case['queries'][-1]['word']) % 3,
                            product_states=product_states,
                            checked_events=len(case['events']))
    return result


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


class Stopped(Exception):
    pass


class Reference:
    """Protocol-level reference: explicit stores, truth tables and event log.

    All physical outcomes come from the declared environment and event law.
    Selection sees only the acquired pair and retained function indices.
    No output from a producer transition is used here.
    """
    functions = ((0, 1), (1, 0), (0, 0))

    def __init__(self, boundary, physical, config):
        self.cfg = deepcopy(config)
        self.b = boundary
        self.machine = deepcopy(boundary['model'])
        environment = (dict(alphabet=['a'], outputs=[0, 0, 0, 1],
                            transitions=[[1], [2], [3], [0]], initial=0)
                       if config['outside_family'] else deepcopy(physical))
        start = F(boundary['fuel'] if config['fuel'] is None else config['fuel'])
        source = boundary['source'] if config['source'] is None else config['source']
        capacity = boundary['capacity'] if config['capacity'] is None else config['capacity']
        self.a = dict(start=start, fuel=start, spent=F(0), income=F(0),
                      live=boundary['live'], workspace=0, peak=boundary['live'],
                      capacity=capacity)
        self.p = dict(phase=boundary['physical_phase'], source=source,
                      transferred=0, wasted=0, tau=config['tau'],
                      sigma=int(boundary['invert']) ^ config['sigma'],
                      broken_reset=config['broken_reset'], blocked=config['blocked'],
                      receipt_mode=config['receipt_mode'], environment=environment)
        self.c = dict(H=deepcopy(self.machine), word=boundary['pending_word'], candidates=[],
                      record=None, expected=None, attempts=0, phase='uninstalled',
                      retained=False, base=boundary['live'] + 8)
        self.trace, self.account_events, self.native_trace = [], [], []
        self.initial_source = source
        self.emit('continuation_boundary', withheld_fuel=F(boundary['fuel']) - start,
                  withheld_source=boundary['source'] - source, config=config)

    def snapshot(self):
        return serial(deepcopy(dict(account=self.a, physical=self.p, controller=self.c)))

    def emit(self, event, **details):
        self.trace.append(dict(event=event, details=serial(details), state=self.snapshot()))

    def size(self, candidates=None, word=None):
        return (self.c['base'] + len(self.c['candidates'] if candidates is None else candidates)
                + len(self.c['word'] if word is None else word) + 1)

    def charge(self, kind, work=0, live=None, temporary=0, extra=F(0), rewrites=0):
        old = self.a['live']
        live = old if live is None else live
        details = dict(kind=kind, work=work, live=live, temporary=temporary,
                       extra=extra, rewrites=rewrites)
        peak = max(old, live) + self.a['workspace'] + temporary
        bill = (F(work, 64) + F(peak * (work + 1), 65536)
                + F(max(0, live-old) + rewrites, 64) + extra)
        reason = None
        if self.cfg['deny_kind'] == kind:
            reason = 'interruption:' + kind
        elif peak > self.a['capacity']:
            reason = 'capacity:' + kind
        elif bill > self.a['fuel']:
            reason = 'funding:' + kind
        if reason:
            self.emit('operation_denied', reason=reason, **details)
            raise Stopped(reason)
        self.a['fuel'] -= bill
        self.a['spent'] += bill
        self.a['live'] = live
        self.a['peak'] = max(self.a['peak'], peak)
        self.account_events.append(serial(dict(kind=kind, work=work, live=live,
            temporary=temporary, workspace=self.a['workspace'], peak=peak,
            rewrites=rewrites, extra=extra, bill=bill, fuel=self.a['fuel'])))
        self.emit('charge', bill=bill, **details)

    def native(self, command):
        try:
            self.charge('native_' + command, extra=F(1, 4), temporary=2)
            observation = None
            if command == 'reset':
                if not self.p['broken_reset']:
                    self.p['phase'] = self.p['environment']['initial']
            elif command == 'a':
                self.p['phase'] = self.p['environment']['transitions'][self.p['phase']][0]
            elif command == 'read':
                observation = (self.p['environment']['outputs'][self.p['phase']]
                               ^ self.p['tau'] ^ self.p['sigma'])
            elif command == 'probe':
                if self.p['source'] < 10:
                    raise Stopped('source_unavailable')
                self.p['source'] -= 10
                actual = ((self.p['environment']['outputs'][self.p['phase']] ^ self.p['tau'])
                          * (1-self.p['blocked']))
                if actual:
                    self.p['transferred'] += 10
                    self.a['fuel'] += 10
                    self.a['income'] += 10
                    self.account_events.append(serial(dict(kind='actual_arrival', amount=10,
                                                           fuel=self.a['fuel'])))
                    self.emit('actual_arrival', amount=10)
                else:
                    self.p['wasted'] += 10
                attempt = dict(command=command, observation='receipt_not_acquired')
                self.native_trace.append(attempt)
                self.charge('arrival_receipt', extra=F(1, 4), temporary=2)
                observation = actual ^ int(self.p['receipt_mode'] == 'complemented')
                attempt['observation'] = observation
                if self.p['receipt_mode'] == 'missing':
                    observation = None
                    attempt['observation'] = 'missing'
            else:
                raise AssertionError(command)
            if command != 'probe':
                self.native_trace.append(dict(command=command, observation=observation))
            self.emit('native_result', command=command, observation=observation)
            return observation
        except Stopped as error:
            self.emit('native_interrupted', command=command, reason=str(error))
            raise

    def attempt(self):
        word = self.c['word']
        self.charge('prepare_use_word', work=len(word)+1, temporary=len(word)+3)
        self.c['expected'] = answer(self.machine, word)
        previous_workspace = self.a['workspace']
        self.a['workspace'] += len(word)+3
        self.c['phase'] = 'executing'
        self.emit('route_opened')
        try:
            for command in ['reset'] + list(word):
                self.native(command)
            observed = self.native('read')
            self.charge('check_sensory_prediction', work=1, temporary=2)
            if observed != self.c['expected']:
                raise Stopped('sensory_prediction_mismatch')
            self.emit('sensory_prediction_confirmed', expected=self.c['expected'], observed=observed)
            receipt = self.native('probe')
            if receipt is None:
                raise Stopped('receipt_missing')
            self.emit('receipt_acquired_uncommitted', sensor=observed, receipt=receipt)
            old = list(self.c['candidates'])
            survivors = [i for i in old if self.functions[i][observed] == receipt]
            self.charge('commit_applicability', work=2*len(old)+1,
                        live=self.size(candidates=survivors), temporary=2*len(old)+2,
                        rewrites=len(survivors)+4)
            self.c['candidates'] = survivors
            self.c['record'] = dict(sensor=observed, receipt=receipt, valid=True)
            self.c['attempts'] += 1
            self.c['phase'] = 'updated'
            self.emit('applicability_updated')
            if not survivors:
                raise Stopped('applicability_family_inadequate')
        finally:
            self.a['workspace'] = previous_workspace
            self.emit('route_closed')

    def decide(self):
        if self.c['record']['receipt']:
            self.emit('stop_after_acquired_arrival')
            return False
        if self.cfg['clamp']:
            word = self.c['word']
            self.charge('clamped_repeat_selection', work=len(word)+1, temporary=len(word)+3)
            self.c['phase'] = 'selected'
            self.emit('reader_clamped', word=word, expected=answer(self.machine, word))
            return True
        for length in range(len(self.machine['outputs'])):
            word = 'a' * length
            count = len(self.c['candidates'])
            self.charge('scan_applicability_word', work=2*(length+1)+count,
                        temporary=length+3+count)
            bit = answer(self.machine, word)
            predictions = sorted({self.functions[i][bit] for i in self.c['candidates']})
            self.emit('candidate_word_scanned', word=word, bit=bit, predictions=predictions)
            if predictions == [0, 1]:
                self.charge('retain_selected_word', work=length+1,
                            live=self.size(word=word), rewrites=length+2, temporary=length+3)
                self.c['word'], self.c['phase'] = word, 'selected'
                self.emit('next_question_selected', word=word, bit=bit)
                return True
        self.emit('no_discriminating_productive_word')
        return False

    def run(self):
        status, checkpoint = 'complete', None
        try:
            self.charge('applicability_installation', work=8, live=self.size(candidates=[0, 1, 2]),
                        temporary=8, extra=F(1))
            self.c['candidates'], self.c['phase'] = [0, 1, 2], 'installed'
            self.emit('installed')
            self.attempt()
            checkpoint = self.snapshot()
            self.emit('post_first_update_checkpoint')
            if self.decide():
                self.attempt()
            self.charge('retain_applicability', work=1, extra=F(self.a['live'], 64))
            self.c['retained'], self.c['phase'] = True, 'retained'
            self.emit('interpretation_retained')
        except Stopped as error:
            status = str(error)
            self.c['retained'] = False
            self.emit('halt', reason=status)
        result = dict(status=status, retained=self.c['retained'], candidates=self.c['candidates'],
            record=self.c['record'], word=self.c['word'], committed_attempts=self.c['attempts'],
            actual_attempts=(self.initial_source-self.p['source'])//10,
            fuel=self.a['fuel'], spent=self.a['spent'], income=self.a['income'],
            source=self.p['source'], wasted=self.p['wasted'], phase=self.p['phase'],
            live=self.a['live'], peak=self.a['peak'], original_H_unchanged=True)
        return serial(dict(config=self.cfg, result=result, checkpoint=checkpoint,
                           trace=self.trace, account_events=self.account_events,
                           native_trace=self.native_trace))


def check_prefixes(report, ancestor):
    boundaries = ancestral_boundaries(ancestor)
    for label, old_name, inverted in [('ordinary', 'primary_unary', False),
                                     ('inverted', 'inverted_sensor', True)]:
        expected = boundaries[old_name]
        saved = report['prefixes'][label]
        exact(saved['original'], ancestor['inherited'], (label, 'ancestral preparation'))
        for key in ['events', 'model', 'fuel', 'source', 'live']:
            exact(saved[key], expected[key], (label, 'exact original prefix', key))
        exact(saved['pending_word'], expected['word'], (label, 'pending original word'))
        exact(saved['physical_phase'], expected['phase'], (label, 'physical cursor'))
        exact(F(saved['spent']), F(36)-F(expected['fuel']), (label, 'prefix spent'))
        exact(saved['invert'], inverted, (label, 'inversion history'))
        exact(saved['capacity'], 256, (label, 'capacity'))
        exact(saved['discarded_archive_sizes'], [0, 0, 0], (label, 'unavailable old archive'))
        exact(saved['queries'], [[q['word'], q['output']] for q in ancestor['cases'][old_name]['queries']],
              (label, 'original acquired observations'))
        require(saved['certified'] and saved['retained'] and saved['original_event_prefix_exact'],
                (label, 'boundary claims'))
    original = ancestor['inherited']
    exact(sum(original[k] for k in ['preparation_spent', 'old_adapter_spent',
                                  'operational_spent', 'waste', 'fuel', 'source']),
          original['original_energy'], 'inherited energy partition')
    exact(ancestor['cases']['inverted_sensor']['analyst_model_exact'], False,
          'preserved raw-target audit differs from sensor correspondence')
    require(answer(ancestor['cases']['inverted_sensor']['model'], '')
            != answer(ancestor['primary_target'], ''),
            'inverted sensor model is not the raw readiness table')
    return boundaries


def config(**updates):
    values = dict(tau=0, sigma=0, blocked=0, broken_reset=0,
                  receipt_mode='faithful', clamp=False, deny_kind=None,
                  fuel=None, capacity=None, source=None, outside_family=False)
    values.update(updates)
    return values


NAMED = {
    'primary_changed': config(tau=1, sigma=1),
    'primary_reader_clamped': config(tau=1, sigma=1, clamp=True),
    'stable': config(),
    'blocked': config(blocked=1),
    'missing_receipt': config(tau=1, sigma=1, receipt_mode='missing'),
    'misleading_receipt': config(tau=1, sigma=1, receipt_mode='complemented'),
    'interrupted_first_write': config(tau=1, sigma=1, deny_kind='commit_applicability'),
    'interrupted_final_retention': config(tau=1, sigma=1, deny_kind='retain_applicability'),
    'sensor_mismatch': config(sigma=1),
    'reset_mismatch': config(tau=1, sigma=1, broken_reset=1),
    'outside_family': config(tau=1, sigma=1, outside_family=True),
    'fuel_zero': config(tau=1, sigma=1, fuel='0'),
    'fuel_three': config(tau=1, sigma=1, fuel='3'),
    'capacity_24': config(tau=1, sigma=1, capacity=24),
    'one_packet': config(tau=1, sigma=1, source=10),
    'source_exhausted': config(tau=1, sigma=1, source=0),
    'inverted_prefix': config(),
}


def check_one(label, actual, boundary, physical):
    expected = Reference(boundary, physical, actual['config']).run()
    for key in ['config', 'result', 'checkpoint']:
        exact(actual[key], expected[key], (label, key))
    for key in ['trace', 'account_events', 'native_trace']:
        exact(len(actual[key]), len(expected[key]), (label, key, 'length'))
        for i, (observed, reference) in enumerate(zip(actual[key], expected[key])):
            exact(observed, reference, (label, key, i))
    initial = actual['trace'][0]
    withheld_fuel = F(initial['details']['withheld_fuel'])
    withheld_source = initial['details']['withheld_source']
    require(withheld_fuel >= 0 and withheld_source >= 0, (label, 'withheld stock'))
    for i, event in enumerate(actual['trace']):
        account, p, c = (event['state'][key] for key in ['account', 'physical', 'controller'])
        exact(F(account['fuel']) + F(account['spent']),
              F(account['start']) + F(account['income']), (label, i, 'fuel account'))
        require(F(account['fuel']) >= 0, (label, i, 'nonnegative fuel'))
        exact(p['transferred'], F(account['income']), (label, i, 'physical arrival credit'))
        exact(p['source'] + p['wasted'] + p['transferred'] + withheld_source,
              boundary['source'], (label, i, 'source conservation'))
        exact(F(account['fuel']) + F(account['spent']) + p['source'] + p['wasted']
              + withheld_fuel + withheld_source,
              F(boundary['fuel']) + boundary['source'], (label, i, 'joined source/fuel identity'))
        exact(c['H'], boundary['model'], (label, i, 'retained sensor knowledge'))
    return dict(states=len(actual['trace']), charges=len(actual['account_events']),
                native_events=len(actual['native_trace']), status=actual['result']['status'])


def verify(report, ancestor):
    checked_boundaries = check_prefixes(report, ancestor)
    exact(set(report['cases']), set(NAMED), 'prespecified named cases')
    outcomes = {}
    for name, cfg in NAMED.items():
        actual = report['cases'][name]
        exact(actual['config'], cfg, (name, 'prespecified intervention'))
        prefix = 'inverted' if name == 'inverted_prefix' else 'ordinary'
        outcomes[name] = check_one(name, actual, report['prefixes'][prefix], ancestor['primary_target'])
    exact(len(report['grid']), 48, 'complete factorial grid')
    wanted = {(p, t, s, b, r) for p in ['ordinary', 'inverted'] for t in [0, 1]
              for s in [0, 1] for b in [0, 1] for r in ['faithful', 'missing', 'complemented']}
    observed_grid = set()
    for i, item in enumerate(report['grid']):
        p, c = item['prefix'], item['config']
        identifier = (p, c['tau'], c['sigma'], c['blocked'], c['receipt_mode'])
        require(identifier not in observed_grid, ('duplicate grid arm', identifier))
        observed_grid.add(identifier)
        exact(c, config(tau=c['tau'], sigma=c['sigma'], blocked=c['blocked'],
                        receipt_mode=c['receipt_mode']), (i, 'grid scope'))
        outcomes[f'grid/{i}'] = check_one(f'grid/{i}', item, report['prefixes'][p],
                                         ancestor['primary_target'])
    exact(observed_grid, wanted, 'factorial coverage')

    ordinary = report['cases']['primary_changed']
    clamped = report['cases']['primary_reader_clamped']
    exact(ordinary['checkpoint'], clamped['checkpoint'], 'matched causal checkpoint')
    for key in ['account', 'physical', 'controller']:
        exact(ordinary['checkpoint'][key], clamped['checkpoint'][key], ('checkpoint', key))
    exact(ordinary['checkpoint']['controller']['candidates'], [1, 2], 'retained nonarrival ambiguity')
    stop_a = next(i for i,e in enumerate(ordinary['trace']) if e['event']=='post_first_update_checkpoint')
    stop_b = next(i for i,e in enumerate(clamped['trace']) if e['event']=='post_first_update_checkpoint')
    exact(stop_a, stop_b, 'matching prefix lengths')
    for i in range(stop_a+1):
        exact(ordinary['trace'][i]['state'], clamped['trace'][i]['state'], ('causal prefix', i))
        exact(ordinary['trace'][i]['event'], clamped['trace'][i]['event'], ('causal prefix event', i))
        if i:
            exact(ordinary['trace'][i]['details'], clamped['trace'][i]['details'],
                  ('causal prefix detail', i))
    exact(ordinary['result']['word'], '', 'changed next productive question')
    exact(clamped['result']['word'], report['prefixes']['ordinary']['pending_word'],
          'clamped inherited use')
    exact(ordinary['result']['candidates'], [1], 'acquired complement relation')
    exact(clamped['result']['candidates'], [1, 2], 'clamp preserves ambiguity')
    exact(F(ordinary['result']['income']), F(10), 'actual productive second encounter')
    exact(F(clamped['result']['income']), F(0), 'actual unproductive clamped encounter')
    exact(report['cases']['stable']['result']['actual_attempts'], 1, 'success-sensitive stopping')
    exact(report['cases']['stable']['result']['source'], 10, 'unspent stable packet')
    exact(report['cases']['missing_receipt']['result']['candidates'], [0, 1, 2],
          'missing is not zero')
    exact(report['cases']['interrupted_first_write']['result']['candidates'], [0, 1, 2],
          'denied commit leaves acquired interpretation uncommitted')
    require(not report['cases']['interrupted_final_retention']['result']['retained'],
            'denied retention does not claim completed interpretation')
    misleading = report['cases']['misleading_receipt']['result']
    exact(misleading['record'], dict(sensor=1, receipt=1, valid=True),
          'false positive is an actually acquired report')
    exact(misleading['candidates'], [0], 'false positive causes mistaken retained relation')
    exact(misleading['actual_attempts'], 1, 'false positive stops further inquiry')
    exact(F(misleading['income']), F(0), 'false positive does not create actual support')
    exact(misleading['wasted'], 10, 'false positive preserves actual failure')
    exact(misleading['source'], 10, 'false-positive remaining packet')
    exact(report['cases']['sensor_mismatch']['result']['actual_attempts'], 0,
          'sensory mismatch stops before extraction')
    exact(report['cases']['interrupted_first_write']['result']['record'], None,
          'uncommitted receipt is not a retained record')
    exact(F(report['cases']['interrupted_final_retention']['result']['income']), F(10),
          'retention failure does not erase successful physical arrival')
    sensory_products = {}
    for name in ['primary_changed', 'primary_reader_clamped', 'stable', 'inverted_prefix']:
        arm = report['cases'][name]
        boundary = report['prefixes']['inverted' if name == 'inverted_prefix' else 'ordinary']
        physical = arm['trace'][0]['state']['physical']
        sensory_products[name] = sensor_equivalence(boundary['model'], physical['environment'],
                                                     physical['tau'] ^ physical['sigma'])
    return dict(accepted=True, traces=len(outcomes),
                state_comparisons=sum(v['states'] for v in outcomes.values()),
                account_event_comparisons=sum(v['charges'] for v in outcomes.values()),
                native_event_comparisons=sum(v['native_events'] for v in outcomes.values()),
                inherited_ledger_events=sum(v['checked_events'] for v in checked_boundaries.values()),
                matched_prefix_states=stop_a+1, sensor_product_states=sensory_products,
                adverse_controls=dict(false_positive_stops_with_zero_income=True,
                    missing_distinct_from_zero=True, failed_commit_preserves_old_candidates=True,
                    failed_retention_preserves_actual_arrival=True,
                    sensory_mismatch_precedes_extraction=True),
                outcomes=outcomes)


def mutation_checks(report, ancestor):
    """Check that distinct false scientific records are rejected in memory."""
    mutations = {}
    def trial(name, edit):
        altered = deepcopy(report)
        edit(altered)
        try:
            verify(altered, ancestor)
        except AssertionError:
            mutations[name] = 'detected'
        else:
            raise AssertionError('undetected artifact mutation: ' + name)
    trial('ancestral_fuel_reset', lambda r: r['prefixes']['ordinary'].__setitem__('fuel', '100'))
    trial('free_installation', lambda r: r['cases']['primary_changed']['account_events'][0].__setitem__('bill', '0'))
    trial('altered_sensor_model', lambda r: r['cases']['primary_changed']['trace'][-1]['state']['controller']['H']['outputs'].__setitem__(0, 1))
    trial('missing_native_receipt', lambda r: r['cases']['primary_changed']['native_trace'].__delitem__(
        next(i for i,e in enumerate(r['cases']['primary_changed']['native_trace'])
             if e['command'] == 'probe')))
    trial('invented_clamp_arrival', lambda r: r['cases']['primary_reader_clamped']['result'].__setitem__('income', '10'))
    trial('unmatched_reader_checkpoint', lambda r: r['cases']['primary_reader_clamped']['checkpoint']['controller'].__setitem__('candidates', [0]))
    return mutations


def main():
    source = HERE / 'results.json'
    ancestor_path = PARENT / 'results.json'
    report, ancestor = (json.loads(p.read_text()) for p in [source, ancestor_path])
    bindings = dict(report['source_hashes'])
    for rel, expected in ancestor['source_hashes'].items():
        exact(digest(PARENT / rel), expected, ('ancestral source binding', rel))
    for rel, expected in bindings.items():
        exact(digest(ROOT / rel), expected, ('producer source binding', rel))
    bindings[str(source.relative_to(ROOT))] = digest(source)
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = digest(Path(__file__))
    summary = verify(report, ancestor)
    summary['mutation_checks'] = mutation_checks(report, ancestor)
    for rel, expected in bindings.items():
        exact(digest(ROOT / rel), expected, ('stable source binding', rel))
    summary.update(
        scope='Independent protocol replay of every saved new event/state; no producer imports or transitions.',
        ancestral_scope='Saved accepted preparation is trusted as ancestry; exact saved pre-use prefixes, 197 ancestral tariff events, original observations and finite sensor-product equivalence are independently checked. No rerun of earlier formation or exhaustive old learning.',
        proof_scope='Finite product-graph sensory equivalence and concrete exact rational replay; no Lean certification, generic formal refinement, empirical verification or optimality claim.',
        hashes_stable=True, source_hashes=bindings,
        primary_result=report['cases']['primary_changed']['result'],
        clamp_result=report['cases']['primary_reader_clamped']['result'])
    (HERE / 'independent-check.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ['outcomes','source_hashes']}, indent=2))


if __name__ == '__main__':
    main()
