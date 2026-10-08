#!/usr/bin/env python3
"""Document/link and inherited proof bindings; not philosophical validation."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAN = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
PROOFS = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
OUTPUT = HERE / 'KNOWLEDGE-PHILOSOPHY-CHECKS.json'
DOCUMENTS = [
    HERE / 'SHARED-INQUIRY-AND-STANDING.md',
    HERE / 'KNOWLEDGE-PHILOSOPHY-COMPLETION.md',
    CAN / 'PHILOSOPHICAL-ACCOUNT.md',
    CAN / 'KNOWLEDGE.md',
    HERE / 'G0-AND-KNOWLEDGE.md',
    HERE / 'KNOWLEDGE-SOURCES.md',
    ROOT / 'sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md',
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    errors, count = [], 0
    for document in DOCUMENTS:
        body = document.read_text()
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', body):
            if target.startswith(('https:', 'http:', 'mailto:')):
                continue
            name, _, fragment = target.partition('#')
            path = (document.parent / unquote(name)).resolve() if name else document
            count += 1
            if path == OUTPUT:
                continue
            if not path.is_file():
                errors.append(f'{document.name}: missing {target}')
            elif fragment and path.suffix == '.md' and unquote(fragment) not in chain.heading_ids(path):
                errors.append(f'{document.name}: missing heading {target}')
    proofs = []
    for stem, source, checker in [
        ('knowledge-correspondence', 'KnowledgeCorrespondence.lean', 'check_knowledge_correspondence.py'),
        ('inquiry-adequacy', 'InquiryAdequacy.lean', 'check_inquiry_adequacy.py'),
    ]:
        receipt = PROOFS / f'{stem}-verification.json'
        record = json.loads(receipt.read_text())
        frozen = ROOT / record['snapshot']
        bindings = {
            'successful_historical_receipt': record['status'] == 'passed',
            'current_source': sha(PROOFS / source) == record['source_sha256'],
            'current_checker': sha(PROOFS / checker) == record['checker_sha256'],
            'frozen_source': sha(frozen / source) == record['source_sha256'],
            'frozen_checker': sha(frozen / checker) == record['checker_sha256'],
            'frozen_receipt': sha(frozen / 'verification.json') == sha(receipt),
        }
        for name, digest in record['log_sha256'].items():
            bindings['log_' + name] = sha(frozen / name) == digest
        if not all(bindings.values()):
            errors.append(f'Proof binding failed: {stem}')
        proofs.append({
            'receipt': str(receipt.relative_to(ROOT)), 'receipt_sha256': sha(receipt),
            'bindings': bindings, 'theorems': record['theorems'],
            'declarations': record['explicit_declaration_audits'],
            'dependencies': record['dependencies'], 'scope': record['scope'],
        })
    source = DOCUMENTS[-1].read_text()
    quotes = ['how do we get to the entire philosophical account',
              'keep going alone this line, see how far you can go',
              '2nd round please, go far', '3rd round please',
              'please continue, see if you can reach the finish line']
    for quote in quotes:
        if '\n> ' + quote + '\n' not in source:
            errors.append('Missing exact user quotation: ' + quote)
    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M21')
    versions = {}
    for link in entry['links']:
        path, _ = chain.local_target(link['path'])
        versions[str(path.relative_to(ROOT))] = data['reviewed_sources'].get(str(path.relative_to(ROOT))) == sha(path)
    expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M21 |'))
    actual = next((line for line in chain.OUTPUT.read_text().splitlines() if line.startswith('| M21 |')), '')
    row_matches = expected == actual
    if not row_matches or not all(versions.values()):
        errors.append('Owned M21 paired row/source version mismatch')
    changes = chain.changes(data)
    validation_errors = chain.validate(data)
    record = {
        'status': 'passed_documentary_and_inherited_proof_bindings' if not errors else 'failed',
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Links, exact user quotations, current/frozen inherited proof bindings and the owned paired index row. These checks do not prove philosophical adequacy, ethical warrant or empirical universality.',
        'local_links_checked': count, 'errors': errors,
        'document_sha256': {str(p.relative_to(ROOT)): sha(p) for p in DOCUMENTS},
        'checker_sha256': sha(Path(__file__)),
        'exact_user_quotes_preserved': quotes,
        'new_theorems': 0, 'new_empirical_experiments': 0,
        'new_compiler_run': False, 'independent_agent_acceptance': False,
        'inherited_proof_packages': proofs,
        'chain_maintenance': {
            'owned_entry': 'M21', 'paired_row_matches': row_matches,
            'linked_source_versions': versions, 'remaining_changes': changes,
            'validation_errors': validation_errors,
            'full_table_current': not changes['modified_sources'] and not changes['missing_sources']
                                  and not validation_errors and chain.OUTPUT.read_text() == chain.render(data),
            'scope_note': 'Concurrent entries and unreviewed source versions remain with their owning studies. New discovery pages do not imply a failed current linked-source check.',
        },
        'completion': {
            'defended_connected_proposal': 'delivered; author assessment',
            'universal_validation': 'unestablished',
            'exclusive_whole_theory_necessity': 'unestablished',
            'exhaustive_philosophy': 'not claimed',
        },
    }
    OUTPUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: record[key] for key in ['status', 'local_links_checked', 'errors']}, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
