#!/usr/bin/env python3
"""Check this study's document links and frozen proof bindings; do not rerun Lean."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ANALYSIS = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
THEORY = ROOT / 'theories/becoming/chapters'
DOCS = [THEORY / 'RELATIONS-ACROSS-SCALES.md', HERE / 'RELATIONS-ACROSS-SCALES-INTEGRATION.md',
        HERE / 'RELATIONS-ACROSS-SCALES-PROOF.md',
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
    receipt = json.loads((ANALYSIS / 'scales-verification.json').read_text())
    if not (receipt['status'] == 'passed' and receipt['inputs_unchanged'] and
            receipt['new_audits'] == 21 and receipt['replayed_inherited_audits'] == 42):
        errors.append('Proof receipt scope/status mismatch')
    if sha(ANALYSIS / 'check_scales.py') != receipt['checker_sha256']:
        errors.append('Checker changed after proof run')
    if sha(ANALYSIS / 'lean-toolchain') != receipt['toolchain_sha256']:
        errors.append('Toolchain changed after proof run')
    source_paths = {'GenerativeCore': ANALYSIS.parent.parent / 'GenerativeCore.lean',
                    'SystemsOrganization': ANALYSIS.parent / 'SystemsOrganization.lean',
                    'RelationsAcrossScales': ANALYSIS / 'RelationsAcrossScales.lean'}
    for module in receipt['modules']:
        name = module['module']
        current = source_paths[name]
        frozen = ANALYSIS / 'scales-verification/sources' / (name + '.lean')
        output = ANALYSIS / 'scales-verification' / (name + '.txt')
        if sha(current) != module['source_sha256'] or sha(frozen) != module['source_sha256']:
            errors.append('Source binding failed: ' + name)
        if sha(output) != module['output_sha256']:
            errors.append('Output binding failed: ' + name)
        if not module['passed'] or len(module['audits']) != len({a['name'] for a in module['audits']}):
            errors.append('Audit failure: ' + name)
        for audit in module['audits']:
            if not set(audit['axioms']) <= {'propext', 'Classical.choice', 'Quot.sound'}:
                errors.append('Unexpected proof dependency: ' + audit['name'])
    edits = json.loads((HERE / 'RELATIONS-ACROSS-SCALES-INDEX-EDITS.json').read_text())
    data = json.loads((ROOT / 'theories/becoming/results/data/generativity-chain.json').read_text())
    entries = {e['id']: e for s in data['sections'] for e in s['entries']}
    for e in edits['added_entries']:
        if entries.get(e['id']) != e:
            errors.append('Owned index entry differs: ' + e['id'])
    record = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'status': 'passed' if not errors else 'failed', 'errors': errors,
              'scope': 'Owned document links, current/frozen proof bindings and owned bilingual index entries; not a fresh Lean run or independent semantic review.',
              'proof_receipt_sha256': sha(ANALYSIS / 'scales-verification.json'),
              'documents': {str(p.relative_to(ROOT)): sha(p) for p in DOCS},
              'links': links, 'index_entries': edits['entry_ids'],
              'new_theorems': receipt['new_audits'], 'inherited_audits': receipt['replayed_inherited_audits']}
    (HERE / 'RELATIONS-ACROSS-SCALES-CHECKS.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': record['status'], 'links': len(links), 'errors': errors, 'index_entries': edits['entry_ids']}))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
