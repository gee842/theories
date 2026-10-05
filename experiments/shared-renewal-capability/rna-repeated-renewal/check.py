#!/usr/bin/env python3
"""Read-only provenance and exact algebra checks; no empirical extraction or fit."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BASE = 'e214ecf'
SOURCE = ROOT / 'sources/24-rna-network-evidence-2026-10-05/repeated-renewal-addition'
C = '_process/research/2026-10-05-support-and-shared-generativity/completion/'
FROZEN_NOTES = [
    'PHYSICAL-EVIDENCE-RNA-NETWORK.md', 'RNA-IDENTIFICATION-CONTRACT.md',
    'RNA-PARTIAL-IDENTIFICATION.md', 'PAID-ACCESS-PHYSICAL-CONSTRAINTS.md',
    'PAID-ACCESS-THERMODYNAMIC-CERTIFICATE.md', 'THERMODYNAMIC-EMBEDDING.md',
    'INTEGRATED-THERMODYNAMICS.md', 'RESOURCE-ALLOCATION-BASELINE.md',
    'PHYSICAL-EVIDENCE-CERONI.md',
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def file_record(path):
    b = path.read_bytes()
    return dict(bytes=len(b), sha256=digest(b))

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

manifest_bytes = (SOURCE / 'MANIFEST.json').read_bytes()
manifest = json.loads(manifest_bytes)
new = []
for entry in manifest['files']:
    actual = file_record(SOURCE / entry['path'])
    assert actual['bytes'] == entry['bytes'], entry['path']
    assert actual['sha256'] == entry['sha256'], entry['path']
    new.append(dict(path=str((SOURCE / entry['path']).relative_to(ROOT)), **actual))
# Compare only pre-existing Source 24 files and named frozen physical notes.
old_paths = git('ls-tree', '-r', '--name-only', BASE, '--',
                'sources/24-rna-network-evidence-2026-10-05').decode().splitlines()
old_paths += [C + name for name in FROZEN_NOTES]
protected = []
for rel in old_paths:
    prior = git('show', BASE + ':' + rel)
    current = (ROOT / rel).read_bytes()
    assert prior == current, 'Frozen bytes changed: ' + rel
    protected.append(dict(path=rel, bytes=len(current), sha256=digest(current)))
# Exact finite witness for the printed covariance inconsistency, not a fit.
atoms = [(F(n), F(b*n), F(1, 4)) for n in (1, 3) for b in (0, 1)]
en = sum(n*w for n, g, w in atoms)
eg = sum(g*w for n, g, w in atoms)
vn = sum((n-en)**2*w for n, g, w in atoms)
vg = sum((g-eg)**2*w for n, g, w in atoms)
cov = sum((n-en)*(g-eg)*w for n, g, w in atoms)
assert (en, eg, vn, vg, cov) == (F(2), F(1), F(1), F(3,2), F(1,2))
assert cov == vn/2 and cov != vn/2 + en**2/4
# All these kernels have identical two-state snapshot marginals; path tasks differ.
kernels = []
for theta in (F(0), F(1,2), F(1)):
    K = [[theta, 1-theta], [1-theta, theta]]
    mu = [F(1,2), F(1,2)]
    assert [sum(mu[i]*K[i][j] for i in range(2)) for j in range(2)] == mu
    kernels.append(dict(theta=str(theta), snapshot=['1/2','1/2'],
                        all_one_at_three_observations=str(F(1,2)*theta**2)))
# Ensure every original source remained byte-identical during the read-only check.
for entry in new + protected:
    assert file_record(ROOT / entry['path']) == {k: entry[k] for k in ('bytes','sha256')}
assert (SOURCE / 'MANIFEST.json').read_bytes() == manifest_bytes
out = dict(
    scope='Read-only exact provenance and algebra; no dataset deserialization, image extraction, author notebook execution, empirical fit or rerun of previous RNA result.',
    base_commit=git('rev-parse', BASE).decode().strip(),
    producer=dict(path=str(Path(__file__).relative_to(ROOT)), **file_record(Path(__file__))),
    manifest=dict(path=str((SOURCE/'MANIFEST.json').relative_to(ROOT)), bytes=len(manifest_bytes), sha256=digest(manifest_bytes)),
    new_original_sources=new,
    frozen_files_unchanged_from_base=protected,
    original_sources_unchanged_during_check=True,
    covariance_witness=dict(mean_N=str(en),mean_G=str(eg),var_N=str(vn),var_G=str(vg),cov_N_G=str(cov),printed_covariance_formula_value=str(vn/2+en**2/4),scope='Exact consequence of printed conditional premise; no claim about author implementation or fitted-parameter impact.'),
    stationary_kernel_witness=kernels,
    result='All provenance and algebra assertions passed.')
(HERE/'check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(result=out['result'],new_source_files=len(new),frozen_files=len(protected),record_sha256=digest((HERE/'check.json').read_bytes())),indent=2))
