"""Package completed research and its audit trail without altering prior outputs."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/correctable-regeneration'
REPORT = ROOT / 'outputs/regeneration-and-effective-correction.md'
DEST = ROOT / 'outputs/regeneration-and-effective-correction-evidence.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(path, *, include_text=True):
    path = Path(path)
    item = {'path': str(path), 'sha256': digest(path)}
    if include_text:
        item['text'] = path.read_text()
    return item


baseline = json.loads((WORK / 'preservation-before.json').read_text())
preservation = []
for rel, before in baseline.items():
    path = ROOT / rel
    after = digest(path) if path.is_file() else None
    preservation.append({'path': str(path), 'before_sha256': before,
                         'after_sha256': after, 'unchanged': before == after})

model_results = json.loads((WORK / 'model-checks.json').read_text())
independent_results = json.loads((WORK / 'independent-results.json').read_text())
assert model_results['status'] == 'all_exact_checks_passed'
assert independent_results['status'] == 'all_exact_independent_checks_passed'

report_text = REPORT.read_text()
local_links = []
for target in re.findall(r'\]\(([^)]+)\)', report_text):
    if target.startswith(('https://', 'http://')):
        continue
    path = Path(target)
    if not path.is_absolute():
        path = REPORT.parent / path
    path = path.resolve()
    # The evidence destination is created by this invocation.
    assert path == DEST or path.is_file(), f'Missing linked file: {path}'
    local_links.append(str(path))

prior_paths = [
    ROOT / 'work/alignment-and-regeneration/model.md',
    Path('/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/continuing-participation-math.md'),
    Path('/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/plural-correction-math.md'),
    Path('/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/selection-of-renewal.md'),
]

evidence = {
    'title': 'Regeneration and effective correction: completed mechanism evidence',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'completed_bounded_mechanism_study',
    'report': {**snapshot(REPORT), 'word_count_whitespace': len(report_text.split()),
               'local_links_validated': local_links},
    'scope': {
        'established': [
            'An explicit productive arrangement can preserve shared support while depleting a dispensable affected participant.',
            'A supplied funded binding claim protocol can preserve the participant floor through an exactly recurring full-state cycle.',
            'For that protocol, recurring funding, prefunded capacity, phase-specific initialization, and positive-delay timing impose distinct sharp constraints.',
        ],
        'assumptions': [
            'Continuing supplied energy/feedstock; production and allocation templates are given.',
            'Current-return replacement selects the incumbent-favorable allocation when no binding mandate operates.',
            'Participant standing, the protected end-round capacity floor, automatic filing, truthful signal, funding earmark, and binding authority are specified.',
            'No borrowing or automatic reconstruction of a failed corrective carrier.',
        ],
        'not_established': [
            'Historical emergence, strategic acceptance, or legitimacy of the institution.',
            'Protection against arbitrary capture of funding or authority.',
            'A universal price of justice, optimum across all protocols, or derivation of goodness from persistence.',
            'Empirical biological, clinical, or social validation.',
        ],
    },
    'exact_results': model_results,
    'independent_results': independent_results,
    'verification_provenance': {
        'author': 'correction_mechanism: exact finite-state enumeration and ledger checks; completed and reported all checks passed.',
        'independent': 'correction_adversary: separate Fraction recurrence; 149 safe parameter cases; audit reports 45-round direct match against author transitions.',
        'scope_review': 'relational_ethics_audit: source and normative-claim review.',
        'parent': 'Read implementations and reviews, incorporated reporting corrections, checked references and preservation; no redundant numerical rerun after prose-only edits.',
        'review_corrections': [
            'The timing formula and author timing sweep exclude zero delay; the original boundary error did not affect the main two-round case.',
            'Prefunding includes both upkeep and activation, requiring capacity three.',
            'Initial reserve 23/9 applies at B=6 in the specified ordinary phase.',
            'Participant floor is evaluated at round end; current receipts may fund ordinary needs, while filing and carrier bills are prefunded.',
            'Distinguished the incumbent operator from the material carrier of correction.',
            'Distinguished joint effective claim access from separately identified sensing and actuation mechanisms.',
            'Restricted necessity claims to the supplied replacement protocol; enforceability does not create moral standing.',
        ],
    },
    'reproducible_materials': [snapshot(WORK / name) for name in
        ['model.md', 'check_model.py', 'independent_check.py', 'audit.md',
         'source-and-ethics.md', 'final-scope-review.md']],
    'inherited_work': {
        'records': [snapshot(p, include_text=False) for p in prior_paths],
        'use': 'Reused prior renewal, participation, liquidity and plural-requirement distinctions. No previous-session experiments were rerun or relabeled as new results.',
        'read_scope': 'Participation and plural-requirement sources read by source and mathematical reviewers; parent inspected selected sections. Other predecessors are identified in the source audit.',
    },
    'external_primary_sources': [
        {'title': 'Social learning promotes institutions for governing the commons',
         'authors_year': 'Sigmund, De Silva, Traulsen, and Hauert, 2010',
         'url': 'https://www.nature.com/articles/nature09203',
         'full_text_url': 'https://personal.math.ubc.ca/~hauert/publications/reprints/sigmund_nature10.pdf',
         'access': 'Three-page article directly read by source reviewer; parent PDF request timed out.',
         'claim_scope': 'Prior modeling of costly institutional support and second-order free riding; no empirical replication or legitimacy inference.'},
        {'title': 'Democratic decisions establish stable authorities that overcome the paradox of second-order punishment',
         'authors_year': 'Hilbe, Traulsen, Röhl, and Milinski, 2014',
         'url': 'https://doi.org/10.1073/pnas.1315273111',
         'full_text_url': 'https://pure.mpg.de/rest/items/item_1909829/component/file_1909830/content',
         'access': 'Five-page article directly read by source reviewer; parent PDF request returned 403.',
         'claim_scope': 'Prior model and experiment on institutional choice procedures; no claim that majority rule protects every participant.'},
    ],
    'preservation': {
        'baseline': snapshot(WORK / 'preservation-before.json', include_text=False),
        'count': len(preservation),
        'all_unchanged': all(p['unchanged'] for p in preservation),
        'files': preservation,
    },
}

DEST.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
assert json.loads(DEST.read_text())['status'] == 'completed_bounded_mechanism_study'
print(json.dumps({'evidence_path': str(DEST), 'report_words': len(report_text.split()),
                  'prior_outputs_checked': len(preservation),
                  'all_prior_outputs_unchanged': evidence['preservation']['all_unchanged'],
                  'changed_prior_outputs': [p['path'] for p in preservation if not p['unchanged']],
                  'local_links_checked': len(local_links)}, indent=2))
