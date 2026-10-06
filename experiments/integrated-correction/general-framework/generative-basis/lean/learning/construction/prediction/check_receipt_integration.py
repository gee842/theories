#!/usr/bin/env python3
"""Reconcile receipt-study links and recorded evidence without rerunning science."""

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[2]
ROOT = CORE.parents[4]
REVIEW = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
ARCHIVE = CORE / 'verification-history/2026-10-06-before-receipt-identification'
MANIFEST_SHA = '9dc9b7122716dec42c90c0e2692382a22656dd702d63a28d385f0cdafae5a0d7'
DEST = REVIEW / 'RECEIPT-IDENTIFICATION-CHECKS.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def headings(path):
    text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    result, counts = set(), {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    result.update(re.findall(r'(?:id|name)=[\"\x27]([^\"\x27]+)', text))
    return result


def main():
    errors = []
    parallel_links = []
    def check(condition, message):
        if not condition:
            errors.append(message)

    # This path is linked by the integration note. A pending artifact makes a
    # first run's path check independent of whether a prior receipt exists.
    if not DEST.exists():
        DEST.write_text('{"passed": false, "status": "pending"}\n')
    changes = read(REVIEW / 'RECEIPT-IDENTIFICATION-DOC-EDITS.json')['files']
    docs = sorted({ROOT / row['path'] for row in changes} | {
        REVIEW / f'RECEIPT-IDENTIFICATION-{suffix}.md'
        for suffix in ('INTEGRATION', 'EVIDENCE', 'REVIEW')})
    links = fragments = 0
    for path in docs:
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for raw in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            raw = raw.strip().strip('<>')
            ref = urlsplit(raw)
            if ref.scheme or raw.startswith('//'):
                continue
            target = (path.parent / unquote(ref.path)).resolve() if ref.path else path
            links += 1
            message = f'Missing link: {path.relative_to(ROOT)} -> {raw}'
            if not target.exists() and target == REVIEW / 'NONDUAL-CORE-INTEGRATION.md':
                # This separately authored note was already linked by the
                # concurrent nondual branch before these additions. Preserve
                # that work and report the incomplete full scan explicitly.
                parallel_links.append(message)
            else:
                check(target.exists(), message)
            if ref.fragment and target.is_file() and target.suffix == '.md':
                fragments += 1
                check(unquote(ref.fragment) in headings(target),
                      f'Missing fragment: {path.relative_to(ROOT)} -> {raw}')

    original = read(REVIEW / 'V73-INTEGRATION-CHECKS.json')['source_sha256']
    for path, expected in original.items():
        check(digest(ROOT / path) == expected, f'Original V7.3 source changed: {path}')

    check(digest(ARCHIVE / 'manifest.json') == MANIFEST_SHA, 'Archive manifest changed')
    archived = read(ARCHIVE / 'manifest.json')['files']
    for row in archived:
        check(digest(ROOT / row['snapshot']) == row['sha256'], f'Archive changed: {row["snapshot"]}')
        check(digest(ROOT / row['source']) == row['sha256'], f'Inherited input changed: {row["source"]}')

    # Reconstruct the disjoint inherited audit map from both preserved suites.
    inherited = {}
    for tag in ('core', 'acquired'):
        prior = read(ARCHIVE / tag / 'verification.json')
        for module in prior['modules']:
            name = module['module']
            log = (ARCHIVE / tag / 'logs' / (name + '.txt')).read_text()
            entries = {n: sorted(a.strip() for a in deps.split(',') if a.strip())
                       for n, deps in re.findall(
                           r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", log)}
            check(bool(entries), f'Missing baseline audits: {name}')
            if name in inherited:
                check(inherited[name] == entries, f'Baseline audit conflict: {name}')
            inherited[name] = entries

    receipt = read(HERE / 'receipt-identification-verification.json')
    check(receipt['status'] == 'passed', 'Lean receipt failed')
    check(digest(HERE / 'check_receipt_lean.py') == receipt['checker_sha256'], 'Lean checker changed')
    check(digest(CORE / 'lean-toolchain') == receipt['toolchain_sha256'], 'Toolchain changed')
    check(receipt['baseline_manifest_sha256'] == MANIFEST_SHA, 'Receipt baseline mismatch')
    new_audits = {}
    for module in receipt['modules']:
        name = module['module']
        check(digest(ROOT / module['source']) == module['source_sha256'], f'Lean source changed: {name}')
        check(digest(HERE / module['output']) == module['output_sha256'], f'Lean log changed: {name}')
        check(module['clean'] and module['exit_code'] == 0, f'Module failed: {name}')
        if module['new_module']:
            new_audits.update(module['audits'])
            check(all(not deps for deps in module['audits'].values()), f'New axiom dependency: {name}')
        else:
            check(module['audits'] == inherited.get(name), f'Inherited audits changed: {name}')
    check(len(receipt['modules']) == 24 and receipt['audits'] == 349, 'Unexpected combined counts')
    check(len(inherited) == 21 and len(new_audits) == 32, 'Unexpected new/inherited counts')
    check(receipt['new_axiom_dependencies'] == [], 'New dependency summary mismatch')

    evidence = read(HERE / 'receipt-identification-results.json')
    check(evidence['all_checks_passed'], 'Evidence check failed')
    for path, expected in evidence['input_hashes'].items():
        check(digest(ROOT / path) == expected, f'Evidence input changed: {path}')
    check(len(evidence['truth_cases']) == 8, 'Truth-case count mismatch')
    check(sum(row['records'] for row in evidence['finite_records_stable_regime']) == 87381,
          'Finite-record count mismatch')
    check(evidence['adaptive_all_failure']['complete_deterministic_policies'] == 128,
          'Policy count mismatch')
    counts = evidence['saved_outage_reanalysis']['counts']
    check(counts['positive_tape_records_replayed'] == 6640 and counts['unique_saved_calls'] == 830,
          'Saved replay count mismatch')
    check(counts['ambiguous_paid_writes'] == counts['ambiguous_paid_writes_changing_score'] == 2452,
          'Ambiguous-write count mismatch')
    check(counts['wrong_labels_paid_for'] == counts['wrong_paid_labels_changing_score'] == 1180,
          'Wrong-write count mismatch')

    diff = subprocess.run(['git', 'diff', '--check', '--', *[str(p.relative_to(ROOT)) for p in docs]],
                          cwd=ROOT, text=True, capture_output=True)
    check(diff.returncode == 0, 'Whitespace check: ' + diff.stdout + diff.stderr)
    output = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Receipt-contribution source reconciliation, preservation and links; unresolved concurrent-branch links reported separately. No proof or scientific rerun.',
                  documents_checked=len(docs), local_links_checked=links, fragments_checked=fragments,
                  original_v73_files_checked=len(original), archived_files_checked=len(archived),
                  inherited_modules_unchanged=len(inherited), combined_modules=len(receipt['modules']),
                  combined_audits=receipt['audits'], new_empty_dependency_audits=len(new_audits),
                  evidence_input_hashes_checked=len(evidence['input_hashes']),
                  lean_receipt_sha256=digest(HERE / 'receipt-identification-verification.json'),
                  evidence_receipt_sha256=digest(HERE / 'receipt-identification-results.json'),
                  checker_sha256=digest(Path(__file__)),
                  documents_sha256={str(p.relative_to(ROOT)): digest(p) for p in docs},
                  unresolved_parallel_links=parallel_links,
                  complete_document_scan_passed=not errors and not parallel_links,
                  errors=errors, passed=not errors)
    DEST.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ('documents_checked', 'local_links_checked', 'fragments_checked',
                                           'new_empty_dependency_audits', 'unresolved_parallel_links',
                                           'complete_document_scan_passed', 'errors', 'passed')}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
