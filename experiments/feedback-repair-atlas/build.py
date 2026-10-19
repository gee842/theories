#!/usr/bin/env python3
"""Build the offline atlas from checked source snapshots (Python standard library)."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build():
    components = json.loads((HERE / 'components.json').read_text())['components']
    for component in components:
        source = ROOT / component['path']
        if digest(source) != component['sha256']:
            raise ValueError('Component source changed; review its excerpt and binding: ' + component['path'])
        lines = source.read_text().splitlines()
        if not 1 <= component['line'] <= component['end'] <= len(lines):
            raise ValueError('Invalid source range: ' + component['id'])
        component.update(file=source.name, code='\n'.join(lines[component['line']-1:component['end']]))
    receipts = {}
    for receipt_name, verifier in [('verification.json', 'verify.py'),
                                   ('interaction-verification.json', 'verify_interaction.py'),
                                   ('gradual-verification.json', 'verify_gradual.py')]:
        receipt = json.loads((HERE / 'model' / receipt_name).read_text())
        if receipt['status'] != 'passed' or receipt['axiom_dependencies']:
            raise ValueError('Unverified application: ' + receipt_name)
        if digest(HERE / 'model' / verifier) != receipt['verification_script_sha256']:
            raise ValueError('Verifier changed: ' + verifier)
        for path, expected in receipt['source_sha256'].items():
            if digest(ROOT / path) != expected:
                raise ValueError('Receipt source changed: ' + path)
        receipts[receipt_name] = {k: receipt[k] for k in
                                 ['status', 'checked_at_utc', 'theorems', 'declarations']}
        receipts[receipt_name]['matching_source_hashes'] = len(receipt['source_sha256'])
    data = json.dumps(dict(components=components, receipts=receipts,
                          sourceModel='GradualInteractionTrial'), ensure_ascii=False).replace('</', '<\\/')
    fragment = (HERE / 'src/atlas.fragment.html').read_text()
    if fragment.count('__RETRY_DATA__') != 1:
        raise ValueError('Expected exactly one data placeholder')
    fragment = fragment.replace('__RETRY_DATA__', data)
    dynamics = (HERE / 'src/dynamics.js').read_text()
    # Embed before the atlas script; the delivered page needs no modules, APIs or CDNs.
    fragment = '<script>\n' + dynamics + '\n</script>\n' + fragment
    shell = (HERE / 'src/shell.html').read_text()
    if shell.count('<!--__ATLAS_FRAGMENT__-->') != 1:
        raise ValueError('Expected exactly one fragment placeholder')
    return shell.replace('<!--__ATLAS_FRAGMENT__-->', fragment)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if index.html needs rebuilding')
    args = parser.parse_args()
    result = build()
    output = HERE / 'index.html'
    if args.check:
        if not output.is_file() or output.read_text() != result:
            raise SystemExit('index.html is stale; run python3 -B build.py')
        print('Atlas is reproducible; component, verifier and transitive receipt hashes match.')
    else:
        output.write_text(result)
        print('Built', output.relative_to(ROOT), '(' + str(output.stat().st_size) + ' bytes)')
