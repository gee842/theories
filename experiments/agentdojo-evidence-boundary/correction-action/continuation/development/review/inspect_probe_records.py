"""Read-only reconstruction of existing development records, no broker imports/runs."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
STUDY = HERE.parents[1]
ARCHIVE = STUDY / 'development/mechanism/probe-results-01'


def load(path):
    return json.loads(path.read_bytes())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()


def main():
    summary = load(ARCHIVE / 'results.json')
    cases = []
    checked_files = 0
    for case in sorted(p for p in ARCHIVE.iterdir() if p.is_dir()):
        preservation = load(case / 'preservation.json')
        for name, rec in preservation['preserved_files'].items():
            p = case / name
            assert p.is_file() and sha(p) == rec['sha256'] and p.stat().st_size == rec['bytes'], (case.name, name)
            checked_files += 1
        events = [json.loads(line) for line in (case / 'events.jsonl').read_text().splitlines()]
        previous = '0' * 64
        for seq, e in enumerate(events, 1):
            stored = e['event_sha256']
            body = {k: v for k, v in e.items() if k != 'event_sha256'}
            assert e['seq'] == seq and e['prev_sha256'] == previous
            assert hashlib.sha256(canonical(body)).hexdigest() == stored
            previous = stored
        state = load(case / 'state.json')
        assert state['event_head'] == previous and state['event_seq'] == len(events)
        attempts = sorted((case / 'attempts').iterdir())
        assert len(attempts) == state['attempts'] == sum(e['type'] == 'attempt' for e in events)
        rows = []
        for folder in attempts:
            response = load(folder / 'response.json')
            ee = [e for e in events if e['attempt_id'] == folder.name]
            assert ee[0]['type'] == 'attempt' and ee[-1]['type'] == 'response'
            descriptor = ee[-1]['payload']['response']
            assert descriptor['sha256'] == sha(folder / 'response.json')
            admissions = [e for e in ee if e['type'] == 'admission']
            settlements = [e for e in ee if e['type'] == 'settlement']
            cache = [e for e in ee if e['type'] == 'cache_hit']
            assert len(admissions) <= 1 and len(settlements) <= 1
            if response['cached']:
                assert len(cache) == 1 and not admissions and not settlements
            if settlements:
                assert admissions and response['status'] == 'ok'
            rows.append({'attempt': folder.name, 'operation': response['operation'], 'status': response['status'],
                         'cached': response['cached'], 'admitted': bool(admissions), 'settled': bool(settlements),
                         'authority_epoch_on_response': response['authority']['epoch']})
        if case.name == 'ordinary-retained':
            assert [r['operation'] for r in rows] == ['check', 'stage', 'replay', 'check', 'publish', 'note', 'finish']
            assert load(case / 'current.json')['version'] == 'v1'
            assert load(case / 'deliveries/r0001-diagnosis-v0.json')['status'] == 'fail'
            assert load(case / 'deliveries/r0003-diagnosis-v1.json')['status'] == 'pass'
        if case.name == 'ordinary-revoked':
            assert [r['operation'] for r in rows] == ['check', 'note', 'finish']
            assert load(case / 'current.json')['version'] == 'v0'
            assert not {'stage', 'replay', 'publish'} & set(state['authority']['grants'])
        if case.name == 'early-checker-abort':
            r = load(case / 'attempts/a0001/response.json')
            assert r['result']['returncode'] == 1 and not r['result']['complete'] and r['result']['delivery'] is None
            assert state['authority']['epoch'] == 0 and not state['deliveries']
        cases.append({'case': case.name, 'events': len(events), 'attempts': rows, 'head': previous,
                      'final_current': load(case / 'current.json'),
                      'preservation_sha256': sha(case / 'preservation.json')})
    result = {'status': 'pass', 'scope': 'Read-only reconstruction of preserved development records, not new process execution or learned-agent outcomes.',
              'script_sha256': sha(Path(__file__)), 'producer_probe_summary_sha256': sha(ARCHIVE / 'results.json'),
              'checked_preserved_files': checked_files, 'cases': cases}
    target = HERE / 'probe-record-review-01.json'
    assert not target.exists(), 'Preserve prior review result; use a new version for a changed review.'
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'cases': len(cases), 'checked_preserved_files': checked_files,
                      'receipt_sha256': sha(target)}))


if __name__ == '__main__':
    main()
