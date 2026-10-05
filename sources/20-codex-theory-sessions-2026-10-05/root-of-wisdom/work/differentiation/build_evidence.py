"""Package proof/check records and verify preservation for the additive branch."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/differentiation'
REPORT = ROOT / 'outputs/differentiation-and-viewpoints.md'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_record(path, text=False):
    data = {'path': str(path), 'sha256': digest(path)}
    if text:
        data['text'] = path.read_text()
    return data


manifest = json.loads((WORK / 'preservation-manifest.json').read_text())
preserved = []
for relative, before in manifest.items():
    path = ROOT / relative
    after = digest(path)
    assert before == after, f'Prior output changed: {relative}'
    preserved.append({'path': str(path), 'before_sha256': before, 'after_sha256': after, 'unchanged': True})
assert len(preserved) == 23

proofs = []
for label, note, script, result in [
    ('Phase domains and symmetry', 'boundary-audit.md', 'check_boundary.py', 'boundary-checks.json'),
    ('Produced barrier and reciprocal maintenance', 'boundary-maintenance.md', 'check_boundary_maintenance.py', 'boundary-maintenance-checks.json'),
    ('Differentiated records and consequential action', 'viewpoint-audit.md', 'check_viewpoints.py', 'viewpoint-checks.json'),
]:
    proofs.append({'subject': label, 'proof_note': file_record(WORK / note, True),
                   'check_program': file_record(WORK / script, True),
                   'result_file': file_record(WORK / result),
                   'results': json.loads((WORK / result).read_text())})

renewal = Path('/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-FOUNDATION.md')
snapshots = WORK / 'source-snapshots'
snapshots.mkdir(exist_ok=True)
renewal_snapshot = snapshots / 'continuing-realizability.md'
renewal_snapshot.write_bytes(renewal.read_bytes())

external = [
    {'title': 'Turing, The Chemical Basis of Morphogenesis, 1952',
     'url': 'https://www.dna.caltech.edu/courses/cs191/paperscs191/turing.pdf',
     'scope': 'Primary paper section 4, particularly journal pages 41-43; symmetry and perturbation discussion. Our finite phase-separation equations are not attributed to this paper.'},
    {'title': 'Hanczyc, Fujikawa and Szostak, Experimental Models of Primitive Cellular Compartments, 2003',
     'url': 'https://www.microeco.ethz.ch/uni/kurs/mikevol03/scinews/Science_302_2003_618.pdf',
     'scope': 'Primary article abstract and indexed full-text assembly, retention, growth and extrusion passages. Supports physical compartment formation components, not our ODE or complete autonomous life.'},
    {'title': 'Cahn and Hilliard, Free Energy of a Nonuniform System I, 1958',
     'url': 'https://doi.org/10.1063/1.1744102',
     'scope': 'Primary abstract reviewed by mathematical audit for phase-field historical context only. Full paper not reviewed; finite graph proofs are derived directly.'},
    {'title': 'Barandiaran, Di Paolo and Rohde, Defining Agency, 2009',
     'url': 'https://xabier.barandiaran.net/wp-content/uploads/2009/07/barandiaran_dipaolo_rohde_-_defining_agency_v_1_0_-_jab_20091.pdf',
     'scope': 'Conceptual auditor read sections 2-3. Context for proposed agency criteria, not a universal test or a consciousness result.'},
    {'title': 'Kolchinsky and Wolpert, Semantic information, autonomous agency, and nonequilibrium statistical physics, 2018',
     'url': 'https://arxiv.org/pdf/1806.08053',
     'scope': 'Conceptual auditor read sections IV-V, including intervention and investigator-chosen viability function limits. Background only; finite-circuit proof derived independently.'},
    {'title': 'Bruineberg and colleagues, The Emperor\'s New Markov Blankets, 2022',
     'url': 'https://manuelbaltieri.com/assets/pdf/EmperorMarkovBlanketsAccepted.pdf',
     'scope': 'Conceptual auditor read abstract, introduction, sections 5.1-5.2. Methodological critique informs boundary criteria; not a universal rejection of statistical boundaries.'},
]
for source in external:
    source['review_date'] = '2026-10-05'

visual_path = Path('/Users/ren/.codex/visualizations/2026/10/04/01a108d0-9667-77f3-a3ac-9438f2fbde99/shared-process-domains.html')
visual_result = json.loads((WORK / 'visual-checks.json').read_text())
assert visual_result['status'] == 'all visual checks passed'
record = {
    'title': 'How shared dynamics produce individuals and viewpoints: evidence record',
    'date': '2026-10-05',
    'report': file_record(REPORT),
    'status': 'Conditional mechanisms established in separate constructed models. Complete physical integration, mechanism genesis, phenomenal experience, and metaphysical monism are not established.',
    'proofs_and_checks': proofs,
    'conceptual_audit': file_record(WORK / 'conceptual-audit.md'),
    'external_primary_sources': external,
    'other_session_sources': [
        {'source': file_record(renewal), 'snapshot': file_record(renewal_snapshot, True),
         'read_scope': 'Primary agent read sections 1-4; conceptual auditor read sections 1-5. Report draws on finite-lifetime renewal and maintenance of implementable interfaces. Other-session checks were not rerun.'},
        {'snapshot': file_record(WORK / 'session-snapshots.json'),
         'contents': json.loads((WORK / 'session-snapshots.json').read_text()),
         'read_scope': 'Read-only review of completed final messages in Articulate Foundation Lenses and Review parallel work connections. Ongoing work is not treated as verified evidence.'},
    ],
    'reviews': [
        {'reviewer': 'boundary_emergence', 'result': 'No mathematical errors found.',
         'scope': 'Phase minima, general graph threshold, exact trajectory, stability, dissolution, active barrier equilibria/interventions, visual formula.',
         'clarification_applied': 'General graph now explicitly requires at least two sites, nonnegative weights, and connected positive-weight edges.'},
        {'reviewer': 'viewpoint_emergence', 'result': 'No substantive errors found.',
         'scope': 'Unique-action criterion, parity impossibility, communication, records/history/interventions, and functional-versus-phenomenal scope.',
         'clarification_applied': 'All-field local regulation explicitly starts with both circuits functioning.'},
        {'reviewer': 'differentiation_audit', 'result': 'No necessary conceptual or source correction found.',
         'scope': 'Substantive explanation, separate-model limits, supplied mechanisms, nonconflation with consciousness, primary source scopes and unfinished-session status.'},
    ],
    'inline_illustration': {'source': file_record(visual_path),
                            'check_program': file_record(WORK / 'check_visual.cjs', True),
                            'checks': visual_result,
                            'visual_inspection': 'Primary agent inspected desktop and 320px rendered screenshots; text fits and values are visible.',
                            'scope': 'Exact amplitude family for kappa=1/4, initial amplitude 0.01, two orientations or exactly zero. Not a generic numerical simulation.'},
    'preservation': {'all_prior_outputs_unchanged': True, 'file_count': len(preserved), 'files': preserved},
    'evidence_types': {'mathematics': 'Displayed proofs plus exact finite arithmetic checks.',
                       'numerics': 'Four barrier ODE trajectory illustrations, RK4 steps 0.02 and 0.01, with analytic asymptotic targets.',
                       'published_experiment': '2003 compartment study reviewed; no new physical experiment or data reanalysis here.',
                       'synthesis': 'Maintained differentiation within shared conditions is the proposed interpretation, not an experimentally established universal law.'},
    'next_integration_test': 'Jointly form compartments, sustain their barriers and sensor/action supports, demonstrate coexisting distinct histories, then interrupt and rescue supports in one physical model or experiment.'
}
output = ROOT / 'outputs/differentiation-evidence.json'
output.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
local_links = [link for link in re.findall(r'\]\(([^)]+)\)', REPORT.read_text()) if not link.startswith(('http://', 'https://', '#'))]
for link in local_links:
    assert (REPORT.parent / link).exists(), f'Missing report link: {link}'
assert len(REPORT.read_text().split()) < 4000
print(json.dumps({'prior_outputs_unchanged': len(preserved), 'local_report_links_valid': len(local_links),
                  'report_words': len(REPORT.read_text().split()), 'evidence_bytes': output.stat().st_size,
                  'report_sha256': digest(REPORT)}, indent=2))
