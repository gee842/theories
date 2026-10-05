"""Package this branch without modifying any earlier or parallel output."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/generative-conditions'
REPORT = ROOT / 'outputs/generation-generating-generation.md'
TARGET = ROOT / 'outputs/generation-generating-generation-evidence.json'

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def snapshot(name, include=True):
    path = WORK / name
    item = {'path': str(path.relative_to(ROOT)), 'sha256': digest(path)}
    if include:
        item['content'] = json.loads(path.read_text()) if path.suffix == '.json' else path.read_text()
    return item

before = json.loads((WORK / 'preservation-before.json').read_text())
preservation = [
    {'path': name, 'before_sha256': old,
     'after_sha256': digest(ROOT/name) if (ROOT/name).is_file() else None}
    for name, old in before.items()
]
for item in preservation:
    item['unchanged'] = item['before_sha256'] == item['after_sha256']

links = []
for href in re.findall(r'\]\(([^)]+)\)', REPORT.read_text()):
    if href.startswith(('https://', 'http://', '#')):
        continue
    path = (REPORT.parent/href).resolve()
    links.append({'target': href, 'exists_or_current_package': path.is_file() or path == TARGET})
assert all(x['exists_or_current_package'] for x in links)

data = {
    'title': 'Generation generating generation: evidence and scope',
    'packaged_utc': datetime.now(timezone.utc).isoformat(),
    'report': {'path': str(REPORT.relative_to(ROOT)), 'sha256': digest(REPORT)},
    'status': 'Conditional mechanism and elementary reachability proof; not a universal law or scientific-priority claim.',
    'mechanism': snapshot('mechanism.md'),
    'conceptual_audit': snapshot('critique.md'),
    'check_program': snapshot('check_cascade.py'),
    'check_results': snapshot('cascade-checks.json'),
    'review': snapshot('review.md'),
    'review_scope': 'Internal AI conceptual review and parent inspection; not independent external peer review.',
    'source_note': snapshot('sources.md', include=False),
    'sources': [
        {'url': 'https://www.nature.com/articles/378767a0',
         'scope': 'Source agent read publisher abstract only; parent direct open failed with an access redirect. No full protocol reading or replication claimed.'},
        {'url': 'https://pubmed.ncbi.nlm.nih.gov/27792958/',
         'primary_full_text': 'https://www.ecotoneinc.com/wp-content/uploads/2020/12/eurasain-beaver-attenuate-flow-2017.pdf',
         'scope': 'Source agent read primary PDF abstract, site/design, results 3.1-3.2. Single monitored reintroduction site; no cross-site randomized intervention claimed.'},
        {'url': 'https://wikisource.org/wiki/Dao_De_Jing',
         'scope': 'Parent checked Chinese chapter 25, including 道法自然. Philosophical application is labeled interpretation.'},
        {'url': 'https://www.shidianguji.com/zh/book/SK2153/chapter/1l9o8e03atwl2',
         'scope': 'Parent and source agent checked Wang Bi commentary, especially lines 13-15. One historical interpretation, not consensus over every tradition.'},
    ],
    'other_session_sources': [
        {'path': str(p), 'sha256_at_packaging': digest(p)}
        for p in [ROOT/'outputs/generative-becoming.md',
                  ROOT/'outputs/changing-the-interface.md',
                  ROOT/'outputs/identity-through-change.md',
                  Path('/Users/ren/theories/_process/research/2026-10-05-generative-health/succession/ANSWER.md')]
    ],
    'scope': {
        'main_example': 'The report shows the first two stages of the three-stage checked cascade.',
        'conservation': 'Assigned material mass only; no energy/free-energy or chemical-feasibility derivation.',
        'finite_feed': 'Every productive event consumes one feed token; closure alone cannot remove exhaustion.',
        'reachability': 'Fixed complete dynamics and concatenable permitted paths; no reset of budgets or deadlines.',
        'classical_language': 'Interpretive resonance; neither classical text is asserted to state the mathematical model.',
        'generation': 'Continued production, increasing option counts, and increasing prevalence remain separate claims.',
    },
    'preservation': {
        'baseline_output_count': len(before),
        'all_unchanged_at_packaging': all(x['unchanged'] for x in preservation),
        'files': preservation,
        'concurrency': 'Another user-owned chat was active in this same directory. This branch edited only its two new outputs and work/generative-conditions. Hash changes in earlier files, if any, are reported rather than overwritten.',
    },
    'local_links': links,
}
TARGET.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({'report_words': len(REPORT.read_text().split()),
                  'evidence_bytes': TARGET.stat().st_size,
                  'baseline_outputs': len(before),
                  'earlier_outputs_changed': [x['path'] for x in preservation if not x['unchanged']],
                  'checked_local_links': len(links)}, indent=2))
