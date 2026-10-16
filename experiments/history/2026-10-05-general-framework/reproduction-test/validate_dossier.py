"""Check stored provenance and local links, then record the completed dossier."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parent
checks = []


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


for folder in ['discrimination', 'adaptive-evidence']:
    base = ROOT / folder
    data = json.loads((base / 'analysis.json').read_text())
    check(folder + ' protocol unchanged', digest(base / 'PROTOCOL.md') == data['protocol_sha256'])
    check(folder + ' analysis source unchanged', digest(base / 'analyze.py') == data['code_sha256'])
discrimination = json.loads((ROOT/'discrimination/analysis.json').read_text())
check('earlier formation source unchanged', digest(ROOT.parent/'gap-resolution/formation-coupled/analyze.py') == discrimination['source_sha256'])
data = json.loads((ROOT/'empirical/results/analysis.json').read_text())['provenance']
check('empirical frozen protocol unchanged', digest(ROOT/'empirical/PROTOCOL.md') == data['protocol_sha256'])
check('empirical analysis source unchanged', digest(ROOT/'empirical/analyze.py') == data['analysis_sha256'])
for name, expected in data['data_sha256'].items():
    check('raw input unchanged: ' + name, digest(ROOT/'empirical/data'/name) == expected)

for path in sorted(ROOT.rglob('*.md')):
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', path.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        dest = target.split('#')[0].strip('<>')
        if not dest or dest == 'MANIFEST.json':
            continue
        check(str(path.relative_to(ROOT)) + ': ' + dest, (path.parent/dest).exists())
for path in sorted(ROOT.rglob('*.json')):
    json.loads(path.read_text())
    check('valid JSON: ' + str(path.relative_to(ROOT)), True)

validation = {'checks_passed': len(checks), 'checks': checks,
              'scope': 'Provenance, stored JSON and local links; substantive numerical audits are separate.'}
(ROOT/'VALIDATION.json').write_text(json.dumps(validation, indent=2)+'\n')
manifest = {'task_date': '2026-10-05', 'note': 'Content hashes record local artifact identity; they do not independently timestamp protocol freezing or certify empirical claims.', 'files': {}}
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and '__pycache__' not in path.parts and path.name != 'MANIFEST.json':
        manifest['files'][str(path.relative_to(ROOT))] = {'sha256': digest(path), 'bytes': path.stat().st_size}
(ROOT/'MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(json.dumps({'checks_passed': len(checks), 'files_recorded': len(manifest['files'])}))
