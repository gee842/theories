#!/usr/bin/env python3
"""Check empirical receipt, documents, owned index and retained Lean bindings."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
from datetime import datetime, timezone
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ANALYSIS = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXPERIMENT = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
DOCS = [THEORY / 'RELATIONS-ACROSS-SCALES.md', HERE / 'BOUND-CALIBRATION-INTEGRATION.md',
        HERE / 'BOUND-CALIBRATION-PROTOCOL.md', EXPERIMENT / 'BOUND-CALIBRATION-PLAN.md',
        ROOT / 'sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    ids, counts = set(), {}
    for line in path.read_text().splitlines():
        m = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not m:
            continue
        title = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', m[1]).lower()
        slug = ''.join(c for c in title if c.isalnum() or c in ' -_').replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        ids.add(slug + ('-' + str(n) if n else ''))
    ids.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', path.read_text()))
    return ids


def main():
    errors, links = [], []
    for path in DOCS:
        for ref in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'[a-z]+:', ref):
                continue
            filename, _, anchor = unquote(ref).partition('#')
            target = (path.parent / filename).resolve() if filename else path
            valid = target.is_file() and (not anchor or anchor in anchors(target))
            links.append({'from': str(path.relative_to(ROOT)), 'ref': ref, 'valid': valid})
            if not valid:
                errors.append(f'Invalid link: {path.name}: {ref}')
    receipt = json.loads((ANALYSIS / 'changing-dependency-verification.json').read_text())
    if not (receipt['status'] == 'passed' and receipt['inputs_unchanged'] and
            receipt['new_audits'] == 25 and receipt['replayed_inherited_audits'] == 161):
        errors.append('Proof receipt scope/status mismatch')
    if sha(ANALYSIS / 'check_changing_dependency.py') != receipt['checker_sha256']:
        errors.append('Checker changed after proof run')
    if sha(ANALYSIS / 'lean-toolchain') != receipt['toolchain_sha256']:
        errors.append('Toolchain changed after proof run')
    source_paths = {'GenerativeCore': ANALYSIS.parent.parent / 'GenerativeCore.lean',
                    'SystemsOrganization': ANALYSIS.parent / 'SystemsOrganization.lean',
                    'RelationsAcrossScales': ANALYSIS / 'RelationsAcrossScales.lean',
                    'ScaleRevision': ANALYSIS / 'ScaleRevision.lean',
                    'InquiryChoice': ANALYSIS / 'InquiryChoice.lean',
                    'ChangingDependency': ANALYSIS / 'ChangingDependency.lean',
                    'RemainingDependency': ANALYSIS.parents[2] / 'mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/RemainingDependency.lean'}
    for module in receipt['modules']:
        name = module['module']
        current = source_paths[name]
        frozen = ANALYSIS / 'changing-dependency-verification/sources' / (name + '.lean')
        output = ANALYSIS / 'changing-dependency-verification' / (name + '.txt')
        if sha(current) != module['source_sha256'] or sha(frozen) != module['source_sha256']:
            errors.append('Source binding failed: ' + name)
        if sha(output) != module['output_sha256']:
            errors.append('Output binding failed: ' + name)
        if not module['passed'] or len(module['audits']) != len({a['name'] for a in module['audits']}):
            errors.append('Audit failure: ' + name)
        for audit in module['audits']:
            if not set(audit['axioms']) <= {'propext', 'Classical.choice', 'Quot.sound'}:
                errors.append('Unexpected proof dependency: ' + audit['name'])
    edits = json.loads((HERE / 'BOUND-CALIBRATION-INDEX-EDITS.json').read_text())
    data = json.loads((ROOT / 'theories/shengsheng-buxi-generative-existence/results/data/generativity-chain.json').read_text())
    entries = {e['id']: e for s in data['sections'] for e in s['entries']}
    for e in edits['updated_entries']:
        if entries.get(e['id']) != e:
            errors.append('Owned index entry differs: ' + e['id'])
    prior_bindings = {
        'RelationsAcrossScales.lean': '24f8eb4269927017b6e65841011c3a4a52002bfe405bf5d09d8a99be7c0cf273',
        'check_scales.py': '1e6569bbc1a3ef56666a9ee4a30f7ab13f41688b99fd285295318ea412f5752e',
        'scales-verification.json': '4066bb9dd83ea1863d3600fc7327fd696c7c95d6de56de1e9cab6354314c1b20'}
    prior_bindings.update({'ScaleRevision.lean': '16d39c9497dba735eeabdd52d3b5b2e6ae256d613f40b73da5fab0b38ed61df5', 'check_scale_revision.py': '13746bb967d37849f3dacc56d024fe7786a1dc9a8aa91f758f60518af6a41df8', 'scale-revision-verification.json': '07fba13a86485ff926cb50e05b35129b02f54dd22965afc5bdf6ebe157325098'})
    prior_bindings.update({'InquiryChoice.lean': '2a2c6571d43f13774a8d27ff473bda6f7c363cdb0e972ecb7ebff3a23a238707', 'check_inquiry_choice.py': 'eefc3c71341555c5a42dce7bf1d59aab7a6f66aae9cc52ef594d7228729fc901', 'inquiry-choice-verification.json': 'b1eababbdde2068494f202cc8ca12c44be95929c98a12355ef140255ee39a4f2'})
    for name, expected in prior_bindings.items():
        if sha(ANALYSIS / name) != expected:
            errors.append('Prior proof artifact changed: ' + name)
    empirical = json.loads((EXPERIMENT / 'bound-calibration-results.json').read_text())
    checked = json.loads((EXPERIMENT / 'bound-calibration-checks.json').read_text())
    if not (checked['status'] == 'passed' and checked['checked_intervals'] == 12440 and
            checked['summary_groups'] == 60 and checked['rate_checks'] == 12):
        errors.append('Empirical receipt scope/status mismatch')
    for key, filename in [('result_sha256', 'bound-calibration-results.json'),
                          ('checker_sha256', 'check_bound_calibration.py'),
                          ('intervals_sha256', 'bound-calibration-intervals.csv')]:
        if sha(EXPERIMENT / filename) != checked[key]:
            errors.append('Empirical checker binding failed: ' + filename)
    for key, filename in [('producer_sha256', 'analyze_bound_calibration.py'),
                          ('plan_sha256', 'BOUND-CALIBRATION-PLAN.md'),
                          ('intervals_sha256', 'bound-calibration-intervals.csv')]:
        if sha(EXPERIMENT / filename) != empirical[key]:
            errors.append('Empirical producer binding failed: ' + filename)
    for path, expected in empirical['sources'].items():
        if sha(ROOT / path) != expected:
            errors.append('Original source changed: ' + path)
    originals = json.loads((ROOT / 'sources/tclab-benchmark/PROVENANCE.json').read_text())['originals']
    for original in originals:
        path = ROOT / original['path']
        if sha(path) != original['sha256'] or path.stat().st_size != original['bytes']:
            errors.append('Original archive/preprint binding failed: ' + original['path'])
    spec = importlib.util.spec_from_file_location('chain_renderer', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    canonical = chain.render(data).splitlines()
    actual_table = chain.OUTPUT.read_text().splitlines()
    for identity in edits['entry_ids']:
        expected_rows = [line for line in canonical if line.startswith('| ' + identity + ' |')]
        actual_rows = [line for line in actual_table if line.startswith('| ' + identity + ' |')]
        if len(expected_rows) != 1 or actual_rows != expected_rows:
            errors.append('Canonical owned table row differs: ' + identity)
    groups = empirical['summary']
    if not (sum(g['n'] for g in groups) == 12440 and
            all(g['width_compatible'] == 0 and g['recorded_band_certificates'] == 0 for g in groups)):
        errors.append('Reported interval count or width conclusion mismatch')
    expected_failures = {('physics', 'T1'): (149, 0), ('physics', 'T2'): (149, 0),
                         ('arx', 'T1'): (299, 0), ('arx', 'T2'): (299, 1),
                         ('ann', 'T1'): (149, 0), ('ann', 'T2'): (149, 1)}
    actual = {(g['run'], g['channel']): (g['n'], g['failures']) for g in groups
              if g['fit_run'] == g['run'] and g['method'] == 'maximum' and g['lag'] == 1}
    if actual != expected_failures:
        errors.append('Reported own-run failure counts mismatch')
    table = json.loads((HERE / 'BOUND-CALIBRATION-TABLE-CHECKS.json').read_text())
    if table['status'] != 'passed' or table['entry_ids'] != ['C28', 'F20']:
        errors.append('Scoped table check failed')
    record = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'status': 'passed' if not errors else 'failed', 'errors': errors,
              'scope': 'Owned document links, empirical computation/source bindings, retained current/frozen Lean bindings and C28/F20 entries; no fresh Lean run, new theorem, physical experiment or independent-agent review.',
              'proof_receipt_sha256': sha(ANALYSIS / 'changing-dependency-verification.json'),
              'documents': {str(p.relative_to(ROOT)): sha(p) for p in DOCS},
              'links': links, 'index_entries': edits['entry_ids'],
              'new_theorems_this_round': 0, 'retained_last_round_theorems': receipt['new_audits'],
              'retained_last_round_inherited_audits': receipt['replayed_inherited_audits'],
              'empirical_receipt_sha256': sha(EXPERIMENT / 'bound-calibration-checks.json'),
              'empirical_intervals': checked['checked_intervals'], 'original_source_bindings': len(empirical['sources']), 'original_archive_and_preprint_bindings': len(originals)}
    (HERE / 'BOUND-CALIBRATION-CHECKS.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': record['status'], 'links': len(links), 'errors': errors, 'index_entries': edits['entry_ids']}))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
