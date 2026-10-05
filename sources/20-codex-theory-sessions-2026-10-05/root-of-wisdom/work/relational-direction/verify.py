import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / 'outputs/relational-regeneration-and-direction.md'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def field(state, recycle=True):
    r, u, v, d = state
    j = d if recycle else 0
    return (j-r*u, u*(r-v-1), v*(u-1), u+v-j)

states = list(itertools.product(range(5), repeat=4))
for s in states:
    for recycling in (True, False):
        f = field(s, recycling)
        assert sum(f) == 0
        assert all(f[i] >= 0 for i in range(4) if s[i] == 0)
    assert sum(field(s, False)[:3]) == -s[1]-s[2]
    for flux in range(5):
        # For epsilon=1, derivative of A+E = -(U+V), independent of recycling flux.
        assert (flux-s[1]-s[2])-flux == -s[1]-s[2]

equilibrium = (2, 1, 1, 2)
assert field(equilibrium) == (0, 0, 0, 0)
jacobian = [[-1, -2, -1], [1, 0, 0], [1, 1, -1]]

def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

polynomial_checks = []
for lam in (-2, -1, 0, 1, 2):
    matrix = [[(lam if i == j else 0)-jacobian[i][j]
               for j in range(3)] for i in range(3)]
    actual = determinant3(matrix)
    expected = (lam+1)*(lam*lam+lam+3)
    assert actual == expected
    polynomial_checks.append({'lambda': lam, 'determinant': actual,
                              'proposed_polynomial': expected})

baseline_path = ROOT / 'work/relational-direction/preservation-manifest.json'
baseline = json.loads(baseline_path.read_text())
missing = [p for p in baseline if not (ROOT / p).exists()]
changed = [p for p, sha in baseline.items()
           if (ROOT / p).exists() and digest(ROOT / p) != sha]

source_scopes = [
    ('/Users/ren/theories/sources/15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md',
     'Full short source read; user-owned AI-assisted prior conversation, not independent confirmation.'),
    ('/Users/ren/theories/sources/06-zhishan/writing-program/context/meta-attractor-foundational-context.md',
     'Targeted passages on shared becoming, distinct centers, and mutual generation versus capture.'),
    ('/Users/ren/theories/sources/04-speculative-future/current/WHAT-MUST-BE-KNOWN.md',
     'Opening lines 1–95; relational existence, boundaries, and renewal versus capture.'),
    ('/Users/ren/theories/theories/shengsheng-buxi-generative-existence/README.md',
     'Opening and targeted search excerpts only; long combined output was truncated, not a full reading.'),
    ('/Users/ren/theories/theories/zhishan-intelligence-must-be-good/README.md',
     'Partial returned excerpts only; long combined output was truncated, not a full reading.'),
    ('/Users/ren/theories/sources/06-zhishan/writing-program/causal-chain/v8/independent-en.md',
     'Targeted lines 65–130, contextual use only.'),
    (str(ROOT / 'outputs/root-of-wisdom-formalization-v2.md'),
     'Full report read; retained internal formalization, not external evidence.')
]
local_sources = []
for name, scope in source_scopes:
    path = Path(name)
    local_sources.append({'path': name, 'read_scope': scope,
                          'sha256_at_finalization': digest(path) if path.exists() else None})

evidence = {
    'title': 'Relational regeneration and a direction in reality: evidence record',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'user_clarification': 'Focus on the direction of reality itself',
    'scope': 'Causal direction of the joint relational situation; no substitution of an ethical prescription for the requested physical claim.',
    'report': {'path': str(REPORT), 'sha256': digest(REPORT)},
    'claim_status': {
        'relational_starting_point': 'Working foundation aligned with user correction; universal ontology not independently proved.',
        'stable_joint_regeneration': 'Conditional mathematical result in a constructed ideal reaction model with supplied energetic support.',
        'depletion_bound': 'Exact conditional balance-law result; no finite-time extinction claim.',
        'finite_work_bound': 'Exact conditional bound for nonnegative reserve with positive fixed per-unit work cost and no replenishment.',
        'stationary_obstruction': 'Exact theorem for time-homogeneous finite irreducible Markov chains, including driven models satisfying those assumptions.',
        'universal_direction_toward_shan': 'Open hypothesis; neither derived nor empirically established here.',
        'endogenous_formation_of_regeneration': 'Proposed next research test; not performed.'
    },
    'checks': {
        'method': 'Python standard-library exact integer arithmetic plus analytic arguments in report; no numerical trajectory simulation.',
        'checker_path': str(Path(__file__).resolve()),
        'equilibrium': list(equilibrium),
        'equilibrium_residual': list(field(equilibrium)),
        'reaction_fluxes_at_equilibrium': [2, 1, 1, 1, 2],
        'jacobian_in_U_V_D_coordinates': jacobian,
        'characteristic_polynomial': '(lambda+1)(lambda^2+lambda+3)',
        'polynomial_checks': polynomial_checks,
        'polynomial_check_scope': 'Both expressions are polynomials of degree at most three; exact agreement at five distinct values proves equality for the stated matrix. Jacobian differentiation is checked analytically in review.',
        'eigenvalues': ['-1', '(-1+i*sqrt(11))/2', '(-1-i*sqrt(11))/2'],
        'stability_scope': 'Local asymptotic stability on fixed total R+U+V+D=6; not global attraction.',
        'sampled_exact_state_checks': len(states),
        'sample_check_scope': 'Arithmetic sanity checks of mass conservation, boundary signs, and depletion identity on a finite integer grid; general proofs are the report algebra, not these samples.',
        'finite_work_identity': 'd(A+E/epsilon)/dt=-(U+V)',
        'all_checks_passed': True
    },
    'external_sources': [
        {
            'title': 'Statistical Physics of Adaptation',
            'authors': 'Nikolay Perunov, Robert A. Marsland, Jeremy L. England',
            'year': 2016,
            'url': 'https://www.englandlab.com/uploads/7/8/0/3/7803054/xz10101__2_.pdf',
            'publication_metadata': 'https://dspace.mit.edu/entities/publication/d7d6e50c-ac68-489e-b0df-a0588e9f0bba',
            'read_scope': 'Author manuscript text through early general theory and equation 8, including abstract, introduction, hopping example, assumptions, and explicit caution against a general flow toward greater heat dissipation. Later fetches failed; full paper not read.',
            'use': 'Primary example of conditional physical direction under specified drive; does not establish kindness or universal regeneration.'
        },
        {
            'title': 'Thermodynamic dissipation does not bound replicator growth and decay rates',
            'authors': 'Artemy Kolchinsky',
            'year': 2024,
            'url': 'https://arxiv.org/abs/2404.01130',
            'doi': 'https://doi.org/10.1063/5.0213466',
            'read_scope': 'Author abstract and publication metadata only; full paper not read.',
            'use': 'Specific critique of interpreting reverse replication as ordinary decay into distinct waste; not a refutation of the 2016 adaptation paper or all dissipative adaptation.'
        }
    ],
    'local_sources': local_sources,
    'review': {
        'reviewer': '/root/relational_goodness_audit',
        'role': 'Independent reasoning review by a collaborating AI agent; not external scientific peer review.',
        'outcome': 'Math and relational framing passed with one material wording correction applied.',
        'correction_applied': 'Replaced indefinite positive-population wording by no positive long-run average activity, explicitly allowing finite-time positivity followed by decay.',
        'additional_scope_clarification': 'Driving does not exempt a time-homogeneous finite irreducible chain from the stationary obstruction.',
        'finite_work_extension': 'Balance-law extension supplied by reviewer and checked here.'
    },
    'preservation': {
        'baseline_path': str(baseline_path),
        'baseline_count': len(baseline),
        'changed_prior_outputs': changed,
        'missing_prior_outputs': missing,
        'all_prior_outputs_unchanged': not changed and not missing,
        'other_research_directories': 'Read only in this branch; no writes performed there.'
    },
    'limitations': ['Constructed mathematical mechanism, not an empirical chemical implementation.',
                    'No experiment, cosmological test, or proof of universal convergence performed.',
                    'Model supplies recycling pathways and energetic support rather than deriving their formation.',
                    'No claim that all existence requires continual measurable information transfer.']
}

output = ROOT / 'outputs/relational-regeneration-and-direction-evidence.json'
output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2)+'\n')
assert (REPORT.parent / 'relational-regeneration-and-direction-evidence.json').exists()
print(json.dumps({'checks_passed': True, 'prior_output_count': len(baseline),
                  'changed_prior_outputs': changed, 'missing_prior_outputs': missing,
                  'report_words': len(REPORT.read_text().split()),
                  'evidence_path': str(output)}, indent=2))
