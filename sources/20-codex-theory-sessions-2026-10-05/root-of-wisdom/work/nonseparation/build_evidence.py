"""Package the additive research record and verify preservation of earlier work."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/nonseparation'
REPORT = ROOT / 'outputs/nonseparation-and-selfhood.md'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(path, include_text=False):
    item = {'path': str(path), 'sha256': sha(path)}
    if include_text:
        item['text'] = path.read_text()
    return item


manifest = json.loads((WORK / 'preservation-manifest.json').read_text())
preserved = []
for relative, before in manifest.items():
    path = ROOT / relative
    after = sha(path)
    assert before == after, f'Existing research changed: {relative}'
    preserved.append({'path': str(path), 'before_sha256': before,
                      'after_sha256': after, 'unchanged': True})

corpus = []
corpus_root = Path('/Users/ren/theories/sources/06-zhishan/writing-program')
for relative, ranges, role in [
    ('causal-chain/v5/independent-en.md', [(89, 91)],
     'Historical formulation of answerability without incorporation; not the newest revision.'),
    ('causal-chain/v7/independent-en.md', [(77, 89)],
     'Later treatment retains distinct personhood, injury, refusal, and responsibility.'),
    ('causal-chain/v8/independent-en.md', [(75, 77), (157, 159)],
     'Current corpus synthesis distinguishes traditions and preserves multiple centers in a common world.'),
    ('context/meta-attractor-foundational-context.md', [(490, 530)],
     'Shared conditions and reciprocal formation retain agency, refusal, and differentiated participants.'),
]:
    path = corpus_root / relative
    item = record(path)
    lines = path.read_text().splitlines()
    item.update(role=role, evidence_type='User-owned other-session research; interpretive synthesis, not independent empirical validation.',
                excerpts=[{'start_line': start, 'end_line': end,
                           'text': '\n'.join(lines[start-1:end])}
                          for start, end in ranges])
    corpus.append(item)

external = [
    {'title': 'SN 22.59, Anattalakkhana Sutta',
     'url': 'https://www.dhammatalks.org/suttas/SN/SN22_59.html',
     'scope': 'Full short discourse read; aggregate impermanence, vulnerability, and identification. Translation by Thanissaro Bhikkhu.'},
    {'title': 'Nagarjuna, Mulamadhyamakakarika, chapter 24',
     'url': 'https://www.wisdomlib.org/buddhism/book/mulamadhyamaka-karika-english/d/doc79738.html',
     'scope': 'Verses 8-10 and 16-20 reviewed; Batchelor translation. Root verses distinguished from later commentary.'},
    {'title': 'Chandogya Upanishad 6.8, with Shankara commentary',
     'url': 'https://www.wisdomlib.org/hinduism/book/chandogya-upanishad-shankara-bhashya/d/doc1145311.html',
     'scope': 'Section opened; 6.8.7 and its commentary verified. Ganganatha Jha translation. Claims explicitly attributed to this reading.'},
    {'title': 'Zhuangzi, chapter 2, Legge translation',
     'url': 'https://ratmachines.com/philosophy/chuang-tzu-legge/chapter-2',
     'scope': 'Chapter opened and unity/language passages verified; translator introduction distinguished from primary text.'},
]
for item in external:
    item['read_date'] = '2026-10-05'
    item['status'] = 'Primary text in translation consulted; selected passage comparison, not an exhaustive tradition survey.'

formal_result = json.loads((WORK / 'formal-checks.json').read_text())
self_result = json.loads((WORK / 'self-maintenance-checks.json').read_text())
assert formal_result['status'] == 'all assertions passed'
assert self_result['status'] == 'all exact checks passed'
self_math = (WORK / 'self-audit.md').read_text().split('## The observer and controller remain within the account')[0]

evidence = {
    'title': 'Nonseparation and the conditions of selfhood: evidence record',
    'date': '2026-10-05',
    'report': record(REPORT),
    'status': 'Additive research branch complete; conditional proofs and constructed checks, philosophical synthesis remains a hypothesis.',
    'mathematical_evidence': {
        'boundary_balance_and_autonomy': {
            'proof_note': record(WORK / 'formal-audit.md', True),
            'check_program': record(WORK / 'check_formal.py', True),
            'result_file': record(WORK / 'formal-checks.json'),
            'results': formal_result,
        },
        'maintenance_and_material_turnover': {
            'proof_source': record(WORK / 'self-audit.md'),
            'proof_text': self_math,
            'check_program': record(WORK / 'check_self_maintenance.py', True),
            'result_file': record(WORK / 'self-maintenance-checks.json'),
            'results': self_result,
        },
    },
    'proof_vs_checks': 'General algebraic arguments establish the stated conditional results. Finite exact-arithmetic checks corroborate calculations within specified constructed families; they are not experimental evidence of universal monism or human no-self.',
    'external_primary_sources': external,
    'other_session_corpus': corpus,
    'additional_research_notes': [record(WORK / 'traditions.md'), record(WORK / 'self-audit.md')],
    'reviews': [
        {'reviewer': 'monism_universality', 'verdict': 'No mathematical errors found.',
         'scope': 'Boundary balance, partitions, all-preparation autonomy, Lyapunov identity and convergence, replacement assumptions, and philosophical scope.'},
        {'reviewer': 'monism_noself_traditions', 'verdict': 'No substantive source or interpretation errors found.',
         'scope': 'Four primary-text comparisons, distinctions among traditions, and explicit status of synthesis and ethical bridge.'},
        {'reviewer': 'primary agent', 'verdict': 'Proofs, check programs, and results inspected; equilibrium wording clarified and connection to noticing omitted conditions added.',
         'scope': 'Final integration, exact sources of claims, and preservation.'},
    ],
    'preservation': {'expected_file_count': 21, 'verified_file_count': len(preserved),
                     'all_prior_outputs_unchanged': True, 'files': preserved},
    'limits': [
        'The balance law assumes additive quantities, antisymmetric transfer currents, and stated production/loss terms.',
        'Exact nonautonomy is proved for a specified connected symmetric exchange system across unrestricted nonnegative preparations.',
        'The maintenance model assumes supplied fresh material, positive rate constants, held environmental conditions, and no recycling of old labels into new components.',
        'Organizational persistence does not establish human personal identity, phenomenal consciousness, or a religious doctrine of no-self.',
        'Common physical conditions alone do not establish a moral ranking; the ethical premise is explicit.',
        'No new physical, psychological, or contemplative experiment was performed.',
    ],
    'next_question': 'Which mechanisms create and maintain a boundary and a situated viewpoint, and when does treating that boundary as autonomous hide a consequential dependency?',
}
assert len(preserved) == 21
destination = ROOT / 'outputs/nonseparation-evidence.json'
destination.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')

links = re.findall(r'\]\(([^)]+)\)', REPORT.read_text())
local = [link for link in links if not link.startswith(('https://', 'http://', '#'))]
for link in local:
    assert (REPORT.parent / link).exists(), f'Missing report link: {link}'

print(json.dumps({'report_words': len(REPORT.read_text().split()),
                  'evidence_bytes': destination.stat().st_size,
                  'prior_outputs_preserved': len(preserved),
                  'local_links_valid': len(local),
                  'report_sha256': sha(REPORT)}, indent=2))
