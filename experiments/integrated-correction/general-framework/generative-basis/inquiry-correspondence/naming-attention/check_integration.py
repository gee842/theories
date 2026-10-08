"""Check owned links, records and M26 without certifying concurrent research."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
BASE = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
spec = importlib.util.spec_from_file_location('chain', BASE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    files = [HERE / 'README.md', HERE / 'PLAN.md',
             ROOT / 'sources/developmental-attention/yu-2021/README.md',
             BASE / 'ACQUIRED-SEGMENTATION-INTEGRATION.md',
             ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/COGNITION-LEARNING-AND-EVOLUTION.md']
    record_dir = ROOT / 'theories/shengsheng-buxi-generative-existence/results/records'
    ids = ['acquired-binding-compositional-use', 'enacted-scene-binding',
           'encounter-selection-and-revision', 'naming-attention-coverage']
    files += [record_dir / (name + '.md') for name in ids]
    links = []
    for path in files:
        for ref in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if ref.startswith(('http://', 'https://')):
                continue
            name, _, fragment = ref.partition('#')
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT) and target.exists(), (path, ref)
            if fragment and target.suffix == '.md':
                assert unquote(fragment) in chain.heading_ids(target), (path, ref)
            links.append((str(path.relative_to(ROOT)), ref))
    edits = json.loads((HERE / 'index-edits.json').read_text())
    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M26')
    assert entry == edits['updated_entry']
    assert all(x in entry['links'] for x in edits['before_entry']['links'])
    for p, sha in edits['reviewed_owned_sources'].items():
        assert digest(ROOT / p) == sha == data['reviewed_sources'][p]
    row = next(x for x in chain.render(data).splitlines() if x.startswith('| M26 |'))
    assert row in chain.OUTPUT.read_text().splitlines()
    for name in ids:
        rec = json.loads((record_dir / (name + '.json')).read_text())
        for ref in rec['references']:
            assert digest(ROOT / ref['path']) == ref['sha256']
    numeric = json.loads((HERE / 'verification.json').read_text())
    assert numeric['status'] == 'passed'
    for p, sha in numeric['source_sha256'].items():
        assert digest(ROOT / p) == sha, p
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Owned links, four result source bindings, current M26 and empirical receipt. Shared navigation is checked by the registry command. Unrelated source drift is not accepted.',
                  local_links_checked=len(links), result_ids=ids, owned_entry='M26',
                  empirical_receipt_sha256=digest(HERE / 'verification.json'),
                  files_sha256={str(p.relative_to(ROOT)): digest(p) for p in files},
                  full_goal_complete=False, independent_agent_review=False)
    (HERE / 'integration-checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'files_sha256'}, indent=2))


if __name__ == '__main__':
    main()
