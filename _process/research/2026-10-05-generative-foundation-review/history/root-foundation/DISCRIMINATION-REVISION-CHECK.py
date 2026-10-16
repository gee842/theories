"""Verify additive integration, source preservation and links; no model run."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
ASSAY = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/discrimination'
OUTPUT = HERE / 'DISCRIMINATION-REVISION-CHECKS.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchor(text):
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def links(path, content):
    result = []
    for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        raw = raw.strip('<>')
        if urlsplit(raw).scheme:
            continue
        name, _, fragment = raw.partition('#')
        target = (path.parent / unquote(name)).resolve() if name else path
        exists = target.exists() or target == OUTPUT
        valid = True
        if exists and fragment and target.suffix == '.md':
            valid = unquote(fragment) in {
                anchor(h) for h in re.findall(r'^#{1,6} (.+)$', target.read_text(), re.M)
            }
        result.append({'document': str(path.relative_to(ROOT)), 'target': raw,
                       'exists': exists, 'fragment_ok': valid})
    return result


data = json.loads((ASSAY / 'results.json').read_text())
source_checks = [{'file': name, 'matches': digest(ROOT / name) == expected}
                 for name, expected in data['source_hashes'].items()]
edits = json.loads((HERE / 'DISCRIMINATION-REVISION-EDITS.json').read_text())
insertions, local_links = [], []
for item in edits['changes']:
    path = ROOT / item['file']
    insertions.append({'file': item['file'], 'present': item['addition'] in path.read_text()})
    local_links.extend(links(path, item['addition']))
notes = sorted(HERE.glob('DISCRIMINATION-REVISION-*.md'))
for path in [*notes, ASSAY / 'PROTOCOL.md', ASSAY / 'README.md']:
    local_links.extend(links(path, path.read_text()))
independent = ASSAY / 'independent-check.json'
receipt_present = independent.exists()
passed = (all(x['matches'] for x in source_checks)
          and all(x['present'] for x in insertions)
          and all(x['exists'] and x['fragment_ok'] for x in local_links)
          and receipt_present)
report = {'status': 'passed' if passed else 'failed',
          'scope': 'Source bindings, exact additive entries, receipt presence and local links. Independent scientific review has its own receipt and scope; this checker does not rerun or certify it.',
          'source_checks': source_checks, 'insertions': insertions,
          'local_links': local_links, 'note_sha256': {p.name: digest(p) for p in notes},
          'assay_results_sha256': digest(ASSAY / 'results.json'),
          'independent_receipt_sha256': digest(independent) if receipt_present else None,
          'checker_sha256': digest(Path(__file__))}
OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'status': report['status'], 'sources': len(source_checks),
                  'additions': len(insertions), 'links': len(local_links)}))
if not passed:
    raise SystemExit(1)
