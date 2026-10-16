#!/usr/bin/env python3
"""Independent compilation and explicit-declaration audit for VariationWarrant.

Adapts this reviewer's earlier scanner, not the author's checker. The scanner is
limited to the inspected one-namespace module and does not count generated
constructors or projections separately. Physical correspondence is not checked.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').is_file())
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
COMMAND = [str(Path.home() / '.elan/bin/lean'), '+leanprover/lean4:v4.29.1']
MODULES = ['GenerativeCore', 'SystemIndividuation', 'VariationWarrant']
POINTER = LEAN / 'deeper/variation-warrant-verification.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def code_only(text):
    out, pos, depth = [], 0, 0
    while pos < len(text):
        if text[pos:pos + 2] == '/-':
            depth += 1
            pos += 2
        elif depth and text[pos:pos + 2] == '-/':
            depth -= 1
            pos += 2
        elif depth:
            out.append('\n' if text[pos] == '\n' else ' ')
            pos += 1
        elif text[pos:pos + 2] == '--':
            end = text.find('\n', pos)
            pos = len(text) if end < 0 else end
        else:
            out.append(text[pos])
            pos += 1
    assert depth == 0
    return ''.join(out)


def main():
    pointer_bytes = POINTER.read_bytes()
    pointer = json.loads(pointer_bytes)
    assert pointer['status'] == 'passed'
    author_path = ROOT / pointer['receipt']
    author_bytes = author_path.read_bytes()
    author = json.loads(author_bytes)
    assert author['status'] == 'passed'
    paths = {m: ROOT / author['source_paths'][m] for m in MODULES}
    sources = {m: p.read_bytes() for m, p in paths.items()}
    assert author['source_sha256'] == {m: sha(b) for m, b in sources.items()}
    for filename, digest in author['artifact_sha256'].items():
        assert sha((author_path.parent / filename).read_bytes()) == digest, filename
    code = code_only(sources['VariationWarrant'].decode())
    assert re.findall(r'^namespace (\w+)$', code, re.M) == ['VariationWarrant']
    assert re.findall(r'^import (\w+)$', code, re.M) == ['SystemIndividuation']
    assert '"' not in code, 'Scanner must be updated if string literals are added.'
    assert not re.search(r'\b(?:axiom|sorry|admit|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC', code)
    declarations = [{'kind': kind, 'name': 'VariationWarrant.' + name}
                    for kind, name in re.findall(r'^(def|theorem|inductive|structure|abbrev) (\w+)', code, re.M)]
    names = [d['name'] for d in declarations]
    assert names and len(names) == len(set(names))
    authored = next(m for m in author['modules'] if m['module'] == 'VariationWarrant')
    assert declarations == authored['declarations']
    theorem_count = sum(d['kind'] == 'theorem' for d in declarations)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    retained = HERE / stamp
    retained.mkdir()
    for m, data in sources.items():
        (retained / (m + '.lean')).write_bytes(data)
    (retained / 'check.py').write_bytes(Path(__file__).read_bytes())
    (retained / 'author-pointer.json').write_bytes(pointer_bytes)
    (retained / 'author-receipt.json').write_bytes(author_bytes)
    receipt = {
        'status': 'checking', 'utc': stamp,
        'source_sha256': {m: sha(b) for m, b in sources.items()},
        'author_receipt': str(author_path.relative_to(ROOT)),
        'author_receipt_sha256': sha(author_bytes),
        'author_artifact_bindings_verified': len(author['artifact_sha256']),
        'declarations': declarations, 'new_theorems': theorem_count,
        'new_declarations': len(declarations),
        'scope': 'Independent fresh compile of three exact sources; all explicit new declarations audited and theorem signatures printed. Inherited audit inventories and empirical science not rerun. No assumption-free foundational certification.'
    }
    try:
        with tempfile.TemporaryDirectory(prefix='variation-warrant-independent-') as temporary:
            work = Path(temporary)
            for m, data in sources.items():
                (work / (m + '.lean')).write_bytes(data)
            env = dict(os.environ, LEAN_PATH=str(work))

            def run(args, log):
                p = subprocess.run(COMMAND + args, cwd=work, env=env, capture_output=True,
                                   text=True, timeout=60)
                output = p.stdout + p.stderr
                (retained / log).write_text(output)
                assert p.returncode == 0 and not re.search(r'\b(?:error|warning):', output), output
                return output

            receipt['lean_version'] = run(['--version'], 'version.log').strip()
            for module in MODULES:
                run(['-o', module + '.olean', module + '.lean'], module + '.log')
            audit = 'import VariationWarrant\n' + '\n'.join('#print axioms ' + n for n in names) + '\n'
            signatures = 'import VariationWarrant\n' + '\n'.join('#check ' + d['name'] for d in declarations if d['kind'] == 'theorem') + '\n'
            for filename, content in [('Audit.lean', audit), ('Signatures.lean', signatures)]:
                (work / filename).write_text(content)
                (retained / filename).write_text(content)
                output = run([filename], filename + '.log')
                if filename == 'Audit.lean':
                    empty = re.findall(r"'([^']+)' does not depend on any axioms", output)
                    assert empty == names
                    assert 'depends on axioms:' not in output
                    receipt['axiom_dependencies'] = {n: [] for n in empty}
        assert all(p.read_bytes() == sources[m] for m, p in paths.items())
        assert POINTER.read_bytes() == pointer_bytes
        receipt['source_unchanged_during_check'] = True
        receipt['status'] = 'passed'
    except Exception as error:
        receipt['status'] = 'failed'
        receipt['error'] = str(error)
        raise
    finally:
        receipt['artifact_sha256'] = {p.name: sha(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()}
        (retained / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'status': receipt['status'], 'receipt': str((retained / 'receipt.json').relative_to(ROOT)),
                      'theorems': theorem_count, 'declarations': len(declarations)}))


if __name__ == '__main__':
    main()
