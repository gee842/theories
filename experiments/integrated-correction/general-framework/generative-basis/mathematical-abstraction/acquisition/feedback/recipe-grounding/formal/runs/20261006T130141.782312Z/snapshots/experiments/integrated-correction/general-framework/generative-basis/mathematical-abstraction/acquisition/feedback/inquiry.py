"""Acquired completion governs remaining inquiry in an inherited actual history.

The controller reads H and its own acquired table; hidden native fields occur
only in the external harness. Costs are prospective macro envelopes.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import refinement as inherited

previous, d = inherited.previous, inherited.d
ROOT = inherited.ROOT


class Inquiry:
    def __init__(self, H, account, disconnect_completion=False):
        self.H, self.a = H, account
        self.disconnect_completion = disconnect_completion
        self.base = H.cells+16
        self.table = []
        self.installed = self.retained = False
        self.trace = []  # external audit only; never read by the policy

    def install(self):
        self.a.pay('inquiry_installation', work=8, live=self.base, temporary=8,
                   extra=self.a.tariff.installation)
        self.a.pay('form_outcome_table', work=3, live=self.base+3, temporary=3)
        self.table = [None]*3
        self.installed = True

    def acquire(self, word, receipt):
        self.a.pay('bind_phase_word', work=len(word)+1, temporary=2)
        q = self.H.initial
        for letter in word:
            q = self.H.transitions[q][self.H.alphabet.index(letter)]
        assert self.table[q] is None
        out = receipt()
        self.a.pay('write_outcome_slot', work=1, temporary=2, rewrites=1)
        self.table[q] = out
        self.trace.append(dict(kind='record', word=word, phase=q, observed=out,
                               table=list(self.table)))

    def completion(self):
        self.a.pay('read_episode_completion', work=3, temporary=1)
        reported = 1 in self.table
        stop = reported and not self.disconnect_completion
        self.trace.append(dict(kind='completion_read', table=list(self.table),
                               reported=reported, stop=stop))
        return stop

    def inquiry_word(self):
        self.a.pay('begin_inquiry_search', work=1, temporary=2)
        q, word = self.H.initial, ()
        for depth in range(3):
            self.a.pay('inspect_inquiry_slot', work=1, temporary=len(word)+2)
            if self.table[q] is None:
                self.trace.append(dict(kind='selected_inquiry', phase=q, word=word))
                return word
            if depth < 2:
                self.a.pay('extend_inquiry_word', work=len(word)+3,
                           temporary=len(word)+3)
                q = self.H.transitions[q][0]
                word += (self.H.alphabet[0],)
        return None

    def retain(self):
        if self.installed:
            self.a.pay('inquiry_retention', work=1,
                       extra=self.a.tariff.retention*self.a.live)
            self.retained = True


def run(name, *, cut=9, first_policy='shortest', readiness=(0, 1, 0),
        disconnect_completion=False, flip_at=None, lost_first=False):
    ancestor = inherited.ancestry(cut)
    H, word, first, phase, prefix = inherited.acquired_prefix(ancestor, readiness, first_policy)
    before = previous.plain(H.record())
    # Harness contract only: the controller does not acquire this validation.
    assert H.alphabet == ('a',) and len(H.outputs) == 3
    q, reached = H.initial, []
    for _ in range(3):
        reached.append(q)
        q = H.transitions[q][0]
    assert len(set(reached)) == 3 and q == H.initial
    a = d.Account(Q(first['fuel_after_return']), initial_live=15)
    a.workspace = len(word)+2
    effects = inherited.Effects(H, phase, first['source'], a, readiness,
                               int(first['success']), lost_first=lost_first,
                               flip_at=flip_at)
    learner = Inquiry(H, a, disconnect_completion)
    status = 'not_started'
    try:
        learner.install()
        learner.acquire(word, effects.receipt)
        a.workspace = 0
        while True:
            if learner.completion():
                status = 'reported_episode_complete'
                break
            selected = learner.inquiry_word()
            if selected is None:
                status = 'all_phase_outcomes_recorded'
                break
            a.workspace = len(selected)+2
            learner.acquire(selected, lambda: effects.use(selected))
            a.workspace = 0
    except d.Halt as error:
        status = str(error)
    a.workspace = 0
    retention_status = 'not_committed'
    try:
        learner.retain()
        if learner.retained:
            retention_status = 'retained'
    except d.Halt as error:
        retention_status = str(error)
    final = dict(fuel=a.fuel, source=effects._source, extension_spent=a.spent,
                 extension_income=a.income, extension_wasted=effects.wasted,
                 table=learner.table, installed=learner.installed,
                 retained=learner.retained, retention_status=retention_status,
                 live=a.live, peak=a.peak, workspace=a.workspace,
                 actual_episode_fulfilled=bool(first['success'] or effects.transferred))
    total = (ancestor['preparation']['preparation_spent']+ancestor['adapter_spent']+
             ancestor['spent']+ancestor['waste']+Q(prefix['spent'])+first['wasted']+
             a.spent+a.fuel+effects._source+effects.wasted)
    assert total == 145 and previous.plain(H.record()) == before
    return previous.plain(dict(name=name, parameters=dict(cut=cut, first_policy=first_policy,
        readiness=readiness, disconnect_completion=disconnect_completion,
        flip_at=flip_at, lost_first=lost_first), ancestry=ancestor, prefix=prefix,
        model_before=before, model_after=H.record(), account_start=a.start,
        status=status, history=learner.trace, effects=effects.trace, events=a.events,
        final=final, whole_account=[145,total]))


def main():
    cases = [run('completion_sensitive'),
             run('completion_reader_disconnected', disconnect_completion=True),
             run('last_phase_ready', readiness=(0, 0, 1)),
             run('blocked', readiness=(0, 0, 0)),
             run('both_later_ready', readiness=(0, 1, 1)),
             run('both_ready_reader_disconnected', readiness=(0, 1, 1), disconnect_completion=True),
             run('earlier_eight', cut=8), run('later_ten', cut=10),
             run('later_ten_last_phase', cut=10, readiness=(0, 0, 1)),
             run('original_ten_novel', cut=10, first_policy='novel'),
             run('nine_novel', first_policy='novel'),
             run('contact_lost', lost_first=True),
             run('false_positive_first', flip_at=1),
             run('false_negative_second', flip_at=2),
             run('false_positive_second', readiness=(0, 0, 1), flip_at=2)]
    saved = json.loads((HERE.parent/'results.json').read_text())
    for case in cases:
        cut = case['parameters']['cut']
        assert case['ancestry']['path'] == saved['inherited']['path'][:cut]
        assert case['ancestry']['preparation'] == saved['inherited']['preparation_record']
        reference = saved['cases']['inverted_sensor']['events'][:88]
        acquired = case['prefix']['events'][:88]
        assert case['prefix']['acquisition_end']['event_count'] == 88
        for old, actual in zip(reference, acquired):
            assert {k:v for k,v in actual.items() if k != 'fuel'} == {k:v for k,v in old.items() if k != 'fuel'}
            assert Q(actual['fuel']) == Q(old['fuel'])+case['ancestry']['fuel']-36
    assert cases[9]['prefix']['events'] == saved['cases']['inverted_sensor']['events']
    assert cases[9]['prefix']['effect'] == saved['cases']['inverted_sensor']['use']
    paths = [HERE/'INQUIRY-PROTOCOL.md', Path(__file__), HERE/'refinement.py', HERE/'study.py',
             HERE.parent/'model.py', HERE.parent/'results.json', HERE.parent/'access/diagnosis.py',
             inherited.PRED, Path(inherited.pred.upstream.__file__),
             Path(inherited.pred.upstream.old.__file__),
             Path(inherited.pred.upstream.old.arithmetic.__file__)]
    result = dict(scope='Acquired completion and inquiry under a supplied productive-use episode',
                  source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                  cases=cases)
    (HERE/'inquiry-results.json').write_text(json.dumps(result, indent=2)+'\n')
    for case in cases:
        f = case['final']
        print(case['name'], case['status'], f['table'], f['fuel'], f['source'],
              f['actual_episode_fulfilled'], f['retention_status'])


if __name__ == '__main__':
    main()
