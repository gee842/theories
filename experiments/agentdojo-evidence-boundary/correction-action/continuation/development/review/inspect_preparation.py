"""Independent read-only pre-execution cohort check; no study implementation imports."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
STUDY = HERE.parents[1]
ROOT = STUDY.parents[3]
SOURCE = Path('sources/28-agentdojo-evidence-2026-10-06')
AUDIT = Path('experiments/agentdojo-evidence-boundary')


def load(p):
    return json.loads(p.read_bytes())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inv(base):
    result = {}
    for p in sorted(base.rglob('*')):
        assert not p.is_symlink()
        if p.is_file():
            result[str(p.relative_to(base))] = {'sha256': sha(p), 'bytes': p.stat().st_size}
    return result


def main():
    manifest = load(STUDY / 'case-manifest.json')
    cohort = load(STUDY / 'COHORT.json')
    assert manifest['cohort_sha256'] == sha(STUDY / 'COHORT.json')
    assert manifest['preparer_sha256'] == sha(STUDY / 'prepare_cohort.py')
    assert [(x['id'], x['policy'], x['branch']) for x in manifest['episodes']] == [(x['id'], x['policy'], x['branch']) for x in cohort['episodes']]
    closure = {}
    for name in ('manifest.json', 'historical-manifest.json'):
        d = load(ROOT / SOURCE / name)
        for entry in d['files'] + d.get('metadata', []):
            rel = SOURCE / entry['path']; p = ROOT / rel
            assert p.resolve().is_relative_to((ROOT / SOURCE).resolve())
            assert sha(p) == entry['sha256']
            closure[str(rel)] = {'sha256': sha(p), 'bytes': p.stat().st_size}
        p = ROOT / SOURCE / name
        closure[str(SOURCE / name)] = {'sha256': sha(p), 'bytes': p.stat().st_size}
    for name in ('REPLAY-CONTRACT.md','REPLAY-SOURCE-CLARIFICATIONS.md','REPLAY-LOADER-CORRECTION.md','replay-source-freeze.json','replay-loader-correction-freeze.json','REPLAY-COUNTERPARTY-REVIEW.md','check_replay.py','replay-verification-initial.json'):
        p = ROOT / AUDIT / name
        closure[str(AUDIT / name)] = {'sha256': sha(p), 'bytes': p.stat().st_size}
    initial = dict(closure)
    preservation = load(ROOT / AUDIT / 'review-history/counterparty-uniqueness/preservation.json')
    for name in ('replay.py','replay-results.json','replay-receipt.json'):
        p = ROOT / AUDIT / 'review-history/counterparty-uniqueness' / name
        assert sha(p) == preservation['files'][name]['sha256']
        initial[str(AUDIT / name)] = {'sha256': sha(p), 'bytes': p.stat().st_size}
    checked, prompts = [], []
    for e in manifest['episodes']:
        case = Path(e['case_dir']); p = case / 'preparation.json'
        assert sha(p) == e['preparation']['sha256'] and p.stat().st_size == e['preparation']['bytes']
        prep = load(p); state = load(case / 'state.json'); current = load(case / 'current.json')
        assert prep['branch'] == e['branch']
        assert state['preparation_sha256'] == sha(p)
        assert state['attempts'] == state['event_seq'] == 0 and state['event_head'] == '0'*64
        assert not state['authority_triggered'] and not state['finished']
        assert all(not state[k] for k in ('requests','runs','candidates','checks','deliveries'))
        assert not (case / 'events.jsonl').exists()
        assert state['authority'] == e['initial_observation']['authority'] and state['authority']['epoch'] == 0
        assert current == e['initial_observation']['current'] and current['version'] == 'v0'
        assert current['version_sha256'] == sha(case / 'versions/v0/version.json')
        assert load(case / 'input-inventory.json') == inv(case / 'inputs') == closure
        assert load(case / 'versions/v0/inventory.json') == inv(case / 'versions/v0/tree') == initial
        assert prep['source_origins'] == {k: {'path': k, **v} for k,v in closure.items()}
        for origin, d in prep['implementation'].items():
            assert d['path'] == origin and sha(ROOT / origin) == d['sha256']
        for name in ('input_inventory','initial_version','recipe'):
            d=prep[name]; assert sha(case / d['path']) == d['sha256']
        prompt = (STUDY / e['prompt']['path']).read_bytes()
        assert hashlib.sha256(prompt).hexdigest() == e['prompt']['sha256'] and len(prompt) == e['prompt']['bytes']
        wanted = (STUDY / 'TASK.txt').read_text() + '\nInitial interface observation:\n' + json.dumps(e['initial_observation'], indent=2, ensure_ascii=False) + '\n'
        assert prompt == wanted.encode()
        prompts.append(prompt)
        checked.append({'id':e['id'],'policy':e['policy'],'branch':e['branch'],'preparation_sha256':sha(p),'input_files':len(closure),'v0_files':len(initial),'prompt_sha256':e['prompt']['sha256'],'zero_attempts_confirmed':True})
    assert len(checked)==4 and len(set(prompts))==1
    record={'status':'pass','scope':'Read-only exact cohort/source/prompt verification before any conventional or learned episode; no program or controller execution.', 'script_sha256':sha(Path(__file__)), 'case_manifest_sha256':sha(STUDY/'case-manifest.json'),'protocol_sha256':sha(STUDY/'PROTOCOL.md'),'task_sha256':sha(STUDY/'TASK.txt'),'broker_sha256':sha(STUDY/'broker.py'),'baseline_sha256':sha(STUDY/'baseline.py'),'episodes':checked}
    target=HERE/'preparation-review-01.json'; assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'pass','episodes':4,'source_files_per_case':len(closure),'v0_files_per_case':len(initial),'receipt_sha256':sha(target)}))


if __name__=='__main__':main()
