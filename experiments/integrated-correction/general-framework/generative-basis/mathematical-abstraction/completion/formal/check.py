#!/usr/bin/env python3
"""Fresh-kernel compilation and declaration audits for the completion study.

This source screen supports this package's simple namespace/declaration style;
it is not a general Lean parser. Kernel compilation, not the screen, checks proofs.
No installed .olean from the research package is trusted or reused.
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
TOOLCHAIN = 'leanprover/lean4:v4.29.1'
STANDARD = {'propext', 'Quot.sound', 'Classical.choice'}
MODULES = ['IdealWarrant', 'CompletionRole', 'PrefixSafety',
           'CompletionExamples', 'HistoryIdeals', 'FiniteBranching', 'CompletionBoundaries']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def code_only(source):
    """Remove nested comments and strings, preserving newlines for scanning."""
    out, i, depth, string = [], 0, 0, False
    while i < len(source):
        pair, char = source[i:i+2], source[i]
        if depth:
            if pair == '/-':
                depth += 1
                out.append('  ')
                i += 2
            elif pair == '-/':
                depth -= 1
                out.append('  ')
                i += 2
            else:
                out.append('\n' if char == '\n' else ' ')
                i += 1
        elif string:
            if char == '\\' and i + 1 < len(source):
                out.append('  ')
                i += 2
            else:
                string = char != '"'
                out.append('\n' if char == '\n' else ' ')
                i += 1
        elif pair == '/-':
            depth = 1
            out.append('  ')
            i += 2
        elif pair == '--':
            end = source.find('\n', i)
            end = len(source) if end == -1 else end
            out.append(' ' * (end - i))
            i = end
        elif char == '"':
            string = True
            out.append(' ')
            i += 1
        else:
            out.append(char)
            i += 1
    assert depth == 0 and not string, 'Unclosed source comment/string'
    return ''.join(out)


def declarations(source):
    code = code_only(source)
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b', code)
    scopes, names = [], []
    for line in code.splitlines():
        match = re.match(r'^\s*(namespace|section)\b\s*(\S*)', line)
        if match:
            scopes.append((match[1], match[2]))
            continue
        if re.match(r'^end(?:\s|$)', line):
            assert scopes, line
            scopes.pop()
            continue
        match = re.match(r'^(?:(?:noncomputable|protected|private)\s+)?'
                         r'(theorem|def|abbrev|structure|inductive)\s+([\w.]+)', line)
        if match:
            assert 'private ' not in line, 'Audit needs a publicly named declaration'
            prefix = '.'.join(name for kind, name in scopes if kind == 'namespace')
            names.append((match[1], prefix + '.' + match[2] if prefix else match[2]))
    assert not scopes, scopes
    assert len(names) == len({name for _, name in names})
    return names


def run(args, cwd, env):
    result = subprocess.run(args, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
    assert result.returncode == 0, result.stdout
    assert 'sorryAx' not in result.stdout, result.stdout
    return result.stdout


def main():
    assert (HERE / 'lean-toolchain').read_text().strip() == TOOLCHAIN
    sources = {name: (HERE / (name + '.lean')).read_bytes() for name in MODULES}
    named = {name: declarations(data.decode()) for name, data in sources.items()}
    receipts = HERE / 'verification'
    receipts.mkdir(exist_ok=True)
    env = dict(os.environ)
    with tempfile.TemporaryDirectory(prefix='completion-lean-') as scratch:
        work = Path(scratch)
        env['LEAN_PATH'] = str(work)
        for name, data in sources.items():
            (work / (name + '.lean')).write_bytes(data)
        version = run(['lean', '+' + TOOLCHAIN, '--version'], work, env).strip()
        for name in MODULES:
            log = run(['lean', '+' + TOOLCHAIN, '-o', name + '.olean', name + '.lean'], work, env)
            (receipts / (name + '.txt')).write_text(log)
        commands = ['import ' + name for name in MODULES]
        commands += ['#print axioms ' + name for entries in named.values() for _, name in entries]
        audit_source = '\n'.join(commands) + '\n'
        (work / 'CompletionAudit.lean').write_text(audit_source)
        audit = run(['lean', '+' + TOOLCHAIN, 'CompletionAudit.lean'], work, env)
    (receipts / 'CompletionAudit.lean').write_text(audit_source)
    (receipts / 'CompletionAudit.txt').write_text(audit)
    observed = {}
    pattern = r"'([^']+)' (does not depend on any axioms|depends on axioms:\s*\[([^]]*)\])"
    for match in re.finditer(pattern, audit):
        axioms = [x.strip() for x in (match[3] or '').split(',') if x.strip()]
        assert set(axioms) <= STANDARD, (match[1], axioms)
        assert match[1] not in observed
        observed[match[1]] = axioms
    expected = {name for entries in named.values() for _, name in entries}
    assert set(observed) == expected, (expected - set(observed), set(observed) - expected)
    for name, frozen in sources.items():
        assert (HERE / (name + '.lean')).read_bytes() == frozen, 'Source changed during check'
    report = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'toolchain': TOOLCHAIN, 'compiler': version, 'fresh_build': True,
        'modules': len(MODULES), 'audited_declarations': len(observed),
        'theorems': sum(kind == 'theorem' for entries in named.values() for kind, _ in entries),
        'custom_axioms': [], 'proof_holes': False,
        'standard_axioms_used': sorted({a for axioms in observed.values() for a in axioms}),
        'scope': 'Kernel-checked mathematical statements under their explicit hypotheses; no ethical or metaphysical warrant inferred',
        'source_sha256': {name + '.lean': digest(data) for name, data in sources.items()},
        'checker_sha256': digest(Path(__file__).read_bytes()),
        'axiom_audits': observed,
    }
    (HERE / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items()
                      if k not in {'axiom_audits', 'source_sha256', 'checker_sha256'}}))


if __name__ == '__main__':
    main()
