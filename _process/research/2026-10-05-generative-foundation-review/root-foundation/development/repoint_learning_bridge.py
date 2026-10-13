#!/usr/bin/env python3
"""Rebind only the two current learning-bridge record scopes after a real recheck.

Usage: python3 -B repoint_learning_bridge.py ROOT BASE [--apply]
BASE must precede the fresh learning-correspondence checker run. Default is a
read-only preview. Run after P58c's source reconciliation and successful core,
CorrectionInquiry and LearningCorrespondence checks. No historical receipt,
study paragraph, proof source hash, claim, or review date is rewritten. The
ordinary landing repointer remains responsible for the other reviewed changes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


LEAN = Path('experiments/integrated-correction/general-framework/generative-basis/lean')
BRIDGE = LEAN / 'universal-ethics/evolution-connectionism'
RECEIPT = BRIDGE / 'learning-correspondence-verification.json'
SOURCE = BRIDGE / 'LearningCorrespondence.lean'
RECORDS = Path('theories/becoming/results/records')
IDS = {'generalization-through-lumping', 'wisdom-root-part-one'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare(root, base):
    old_bytes = subprocess.run(['git', 'show', f'{base}:{RECEIPT.as_posix()}'],
                               cwd=root, check=True, capture_output=True).stdout
    new_bytes = (root / RECEIPT).read_bytes()
    old, new = json.loads(old_bytes), json.loads(new_bytes)
    assert old['status'] == new['status'] == 'passed', 'both receipts must have passed'
    assert old['utc'] != new['utc'], 'run the learning bridge checker first'
    assert new['source_unchanged_during_check'] is True
    for field in ('bridge_module', 'toolchain', 'mathlib_revision'):
        assert old[field] == new[field], ('changed validation basis', field)
    assert new['bridge_module'] == 'LearningCorrespondence'
    retained = root / BRIDGE / new['retained_run'] / 'verification.json'
    assert retained.read_bytes() == new_bytes, 'current and retained receipts differ'
    # This helper is only for a dependency recheck. A changed bridge needs review.
    assert old['source_sha256']['LearningCorrespondence'] == new['source_sha256']['LearningCorrespondence']
    old_module, = old['modules']
    new_module, = new['modules']
    assert new_module['kernel_checked'] is True
    for field in ('module', 'theorems', 'declarations', 'axiom_dependencies'):
        assert old_module[field] == new_module[field], ('bridge scope changed', field)
    for module, path in new['source_paths'].items():
        assert digest((root / LEAN / path).read_bytes()) == new['source_sha256'][module], \
            ('current dependency differs from checked source', module)
    core = json.loads((root / LEAN / 'becoming/becoming-verification.json').read_text())
    assert core['status'] == 'passed'
    for module in set(new['source_sha256']) & set(core['source_sha256']):
        assert new['source_sha256'][module] == core['source_sha256'][module], \
            ('core and bridge checked different sources', module)

    receipt_path, source_path = RECEIPT.as_posix(), SOURCE.as_posix()
    old_sha, new_sha = digest(old_bytes), digest(new_bytes)
    old_run, new_run = old['utc'], new['utc']
    date = f'{new_run[:4]}-{new_run[4:6]}-{new_run[6:8]}'
    history = {
        'zh': f'{date} P58c 后学习桥接重查：当前验证范围指向回执 {new_run}，取代 {old_run}；'
              '桥接源、声明、前提及公理报告不变，当前依赖按源哈希核对。原 P73/P74 回执及研究中的历史验证保留；断言不变。',
        'en': f'{date} learning-bridge recheck after P58c: the current validation scope points to receipt '
              f'{new_run}, replacing {old_run}; the bridge source, declarations, premises and axiom reports '
              'are unchanged, and current dependencies are checked by source hash. The original P73/P74 '
              'receipt and historical study validation are retained; the claim is unchanged.',
    }
    changed, found = {}, set()
    names = {item['name'] for item in new_module['declarations']}
    for path in sorted((root / RECORDS).glob('*.json')):
        data = json.loads(path.read_text())
        receipt_refs = [r for r in data.get('references', []) if r['path'] == receipt_path]
        if not receipt_refs:
            continue
        identity = data['id']
        assert identity in IDS, ('unexpected bridge consumer: review before adding', identity)
        found.add(identity)
        assert len(receipt_refs) == 1 and receipt_refs[0]['role'] == 'receipt'
        assert receipt_refs[0]['sha256'] in {old_sha, new_sha}, ('unrelated receipt drift', identity)
        source_refs = [r for r in data['references'] if r['path'] == source_path]
        assert len(source_refs) == 1 and source_refs[0]['role'] == 'proof'
        assert source_refs[0]['sha256'] == new['source_sha256']['LearningCorrespondence']
        assert set(source_refs[0]['declarations']) <= names
        bindings = [b for b in data['proof_bindings'] if b['source'] == source_path]
        assert len(bindings) == 1
        assert bindings[0]['receipt'] == receipt_path
        assert bindings[0]['sha256_pointer'] == '/source_sha256/LearningCorrespondence'
        assert bindings[0]['success_pointer'] == '/status' and bindings[0]['success_value'] == 'passed'
        for lang in ('zh', 'en'):
            scope = data['validation_scope'][lang]
            assert (scope.count(old_run), scope.count(new_run)) in {(1, 0), (0, 1)}, (identity, lang)
            data['validation_scope'][lang] = scope.replace(old_run, new_run)
        receipt_refs[0]['sha256'] = new_sha
        if history not in data['history']:
            data['history'].append(history)
        changed[path] = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    assert found == IDS, ('missing or changed bridge consumers', found)
    return changed, new


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('base')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    changed, receipt = prepare(root, args.base)
    for path, text in changed.items():
        if args.apply:
            path.write_text(text)
        print(('updated ' if args.apply else 'would update ') + str(path.relative_to(root)))
    print('Current bridge receipt:', receipt['utc'])
    print('Historical receipts, study stamps, proof hashes, claims and review dates retained.')


if __name__ == '__main__':
    main()
