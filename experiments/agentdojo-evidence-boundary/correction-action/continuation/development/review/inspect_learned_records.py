"""Inspect retained learned records without executing/importing study programs."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
STUDY = HERE.parents[1]


def load(path):
    return json.loads(path.read_bytes())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()


def main():
    freeze = load(STUDY / 'DISPATCH-FREEZE.json')
    for name, rec in freeze['files'].items():
        assert sha(STUDY / name) == sha(STUDY / rec['snapshot']) == rec['sha256'], name
    manifest = load(STUDY / 'case-manifest.json')
    cases = []
    for item in manifest['episodes']:
        if item['id'] not in ('w01', 'w02'):
            continue
        case = Path(item['case_dir'])
        assert sha(case / 'preparation.json') == item['preparation']['sha256']
        state = load(case / 'state.json')
        assert state['finished'] and state['preparation_sha256'] == item['preparation']['sha256']
        checked = set()

        def descriptor(rec):
            path = case / rec['path']
            assert sha(path) == rec['sha256'] and path.stat().st_size == rec['bytes'], rec['path']
            checked.add(rec['path'])

        def walk(value):
            if isinstance(value, dict):
                if {'path', 'sha256', 'bytes'} <= value.keys():
                    descriptor(value)
                for v in value.values():
                    walk(v)
            elif isinstance(value, list):
                for v in value:
                    walk(v)

        walk(state)
        for inv, root in [(case / 'input-inventory.json', case / 'inputs')]:
            for name, rec in load(inv).items():
                descriptor({'path': str((root / name).relative_to(case)), **rec})
        for v in state['versions'].values():
            for name, rec in load(case / v['inventory']['path']).items():
                descriptor({'path': str(Path(v['tree']) / name), **rec})
        for run in state['runs']:
            before = load(case / run['input_inventory']['path'])
            after = load(case / run['output_inventory']['path'])
            assert all(after.get(n) == r for n, r in before.items())
            for name, rec in after.items():
                descriptor({'path': str(Path(run['tree']) / name), **rec})
            if run['operation'] == 'replay':
                assert not any(n.endswith(('replay-results.json', 'replay-receipt.json', 'replay-verification.json')) for n in before)
            else:
                assert not any(n.endswith('/replay-verification.json') for n in before)

        events = [json.loads(line) for line in (case / 'events.jsonl').read_text().splitlines()]
        previous = '0' * 64
        for seq, event in enumerate(events, 1):
            digest = event['event_sha256']
            body = {k: v for k, v in event.items() if k != 'event_sha256'}
            assert event['seq'] == seq and event['prev_sha256'] == previous
            assert hashlib.sha256(canonical(body)).hexdigest() == digest
            previous = digest
            walk(event)
        assert state['event_head'] == previous and state['event_seq'] == len(events)
        assert sum(e['type'] == 'authority_update' for e in events) == 1
        rows = []
        for i, folder in enumerate(sorted((case / 'attempts').iterdir()), 1):
            request = load(folder / 'request.json')
            response = load(folder / 'response.json')
            transcript = STUDY / 'transcripts' / item['id'] / f'{i:02d}'
            assert transcript.with_suffix('.reply.txt').read_bytes() == (folder / 'raw.txt').read_bytes()
            assert transcript.with_suffix('.response.json').read_bytes() == (folder / 'response.json').read_bytes()
            assert json.loads((folder / 'raw.txt').read_text()) == request
            assert response['status'] == 'ok' and not response['cached']
            ee = [e for e in events if e['attempt_id'] == folder.name]
            assert ee[0]['type'] == 'attempt' and ee[-1]['type'] == 'response'
            assert len([e for e in ee if e['type'] == 'admission']) == 1
            assert len([e for e in ee if e['type'] == 'settlement']) == 1
            rows.append({'attempt': folder.name, 'operation': request['operation'],
                         'version': request.get('version'), 'epoch_on_response': response['authority']['epoch']})
        assert len(rows) == state['attempts']
        finish = folder / 'request.json'
        assert request['operation'] == 'finish'
        assert load(case / 'final.json')['declaration'] == {k: request[k] for k in ['diagnosis', 'repair', 'explanation']}
        note = next(d['artifact'] for d in state['deliveries'] if d['kind'] == 'note')
        runs = []
        for r in state['runs']:
            proc = load(case / r['process']['path'])
            runs.append({'run': r['id'], 'operation': r['operation'], 'version': r['version'],
                         'python': proc['argv'][0], 'returncode': proc['returncode'],
                         'started': proc['started'], 'timeout': proc['timeout']})
        if item['id'] == 'w01':
            assert [r['operation'] for r in rows] == ['read', 'check', 'read', 'check', 'read', 'read', 'read', 'read', 'note', 'finish']
            assert not state['candidates'] and set(state['versions']) == {'v0'}
            aborted = load(case / 'attempts/a0002/response.json')['result']
            assert not aborted['complete'] and aborted['delivery'] is None
            assert not (case / 'runs/r0001/tree/experiments/agentdojo-evidence-boundary/replay-verification.json').exists()
            assert 'No module named' in (case / 'runs/r0001/stderr.txt').read_text()
            assert rows[1]['epoch_on_response'] == 0 and rows[3]['epoch_on_response'] == 1
        else:
            assert [r['operation'] for r in rows] == ['check', 'read', 'read', 'stage', 'replay', 'check', 'publish', 'read', 'read', 'read', 'read', 'note', 'finish']
            assert load(case / 'current.json')['version'] == 'v1'
            assert len(state['candidates']) == 1 and set(state['versions']) == {'v0', 'v1'}
            assert load(case / 'deliveries/r0003-diagnosis-v1.json')['status'] == 'pass'
        cases.append({'case': item['id'], 'preparation_sha256': sha(case / 'preparation.json'),
                      'note_sha256': note['sha256'], 'finish_request_sha256': sha(finish),
                      'events_sha256': sha(case / 'events.jsonl'), 'final_sha256': sha(case / 'final.json'),
                      'state_sha256': sha(case / 'state.json'), 'current': load(case / 'current.json'),
                      'bound_case_files_checked': len(checked), 'events': len(events), 'attempts': rows, 'runs': runs})
    result = {'status': 'pass', 'scope': 'Independent read-only reconstruction and artifact binding; no scientific program or scorer executed, no native-host isolation claim.',
              'script_sha256': sha(Path(__file__)), 'dispatch_freeze_sha256': sha(STUDY / 'DISPATCH-FREEZE.json'),
              'frozen_current_and_snapshot_pairs': len(freeze['files']), 'cases': cases}
    target = HERE / 'learned-record-review-01.json'
    assert not target.exists(), 'Preserve earlier review output.'
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'receipt_sha256': sha(target),
                      'case_files_checked': sum(c['bound_case_files_checked'] for c in cases)}))


if __name__ == '__main__':
    main()
