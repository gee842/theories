#!/usr/bin/env python3
"""Build the nondual presentation, formation and compatibility interfaces; never rewrite prior receipts."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
BASIS = ROOT.parent
TOOLCHAIN = 'leanprover/lean4:v4.29.1'
SOURCES = [BASIS/'lean/GenerativeCore.lean', BASIS/'lean/NondualCore.lean',
           BASIS/'lean/conditional/ResourceContinuation.lean',
           ROOT/'PatientConcern.lean', ROOT/'GroundingContract.lean',
           ROOT/'NondualFormation.lean', ROOT/'NondualConcernAdapter.lean']
ALLOWED = {'propext', 'Quot.sound', 'Classical.choice'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    version = run(['lean', '+'+TOOLCHAIN, '--version'], ROOT, env)
    version.check_returncode()
    assert 'version 4.29.1,' in version.stdout
    frozen = {p: p.read_bytes() for p in SOURCES}
    preserved = {p: sha(p.read_bytes()) for p in
                 [ROOT/'verification.json', ROOT/'root-verification.json',
                  ROOT/'root-independent-review.json', ROOT/'check.py', ROOT/'Cases.lean']}
    for p,data in frozen.items():
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', data.decode()), p
        assert not re.search(r'^\s*(axiom|constant)\s', data.decode(), re.M), p
    logs = ROOT/'nondual-verification'
    logs.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix='nondual-core-') as temporary:
        build = Path(temporary)
        for p,data in frozen.items():
            (build/p.name).write_bytes(data)
        build_env = dict(env, LEAN_PATH=str(build))
        for p in SOURCES:
            result = run(['lean', '+'+TOOLCHAIN, '-o', p.stem+'.olean', p.name],
                         build, build_env)
            log = logs/(p.stem+'.txt')
            log.write_text(result.stdout)
            audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", result.stdout)
            expected = len(re.findall(r'^#print axioms ', frozen[p].decode(), re.M))
            dependencies = sorted({x.strip() for _,xs in audits for x in xs.split(',') if x.strip()})
            clean = (result.returncode == 0 and 'warning:' not in result.stdout
                     and 'sorryAx' not in result.stdout and len(audits) == expected
                     and expected > 0 and set(dependencies) <= ALLOWED)
            results.append(dict(module=p.stem, source=str(p.relative_to(BASIS)),
                                source_sha256=sha(frozen[p]), exit_code=result.returncode,
                                dependency_audits=len(audits), axioms=dependencies,
                                clean=clean, log=str(log.relative_to(ROOT)),
                                log_sha256=sha(log.read_bytes()),
                                audited_declarations=[name for name,_ in audits]))
            if not clean:
                print(result.stdout)
                break
    unchanged = all(p.read_bytes() == data for p,data in frozen.items())
    old_unchanged = all(sha(p.read_bytes()) == h for p,h in preserved.items())
    passed = len(results) == len(SOURCES) and all(r['clean'] for r in results) and unchanged and old_unchanged
    record = dict(status='passed' if passed else 'failed',
                  checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  toolchain=TOOLCHAIN, lean_version=version.stdout.strip(),
                  fresh_temporary_build=True, sources_unchanged=unchanged,
                  old_receipt_and_cases_preserved=old_unchanged,
                  preserved_files={str(p.relative_to(ROOT)):h for p,h in preserved.items()},
                  checker_sha256=sha(Path(__file__).read_bytes()), modules=results,
                  new_dependency_audits=sum(r['dependency_audits'] for r in results if r['module'] in {'NondualCore','NondualFormation','NondualConcernAdapter'}),
                  scope='Exact history/readout presentations of the existing Process, a specified overlapping signal-support formation and role-change example, report sufficiency, and a separately located C2 compatibility adapter. No generated phenomenal self, moral direction, acquired internal role model, independently derived signal law, or assumption-free ontology.')
    (ROOT/'nondual-verification.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['status','new_dependency_audits','sources_unchanged','old_receipt_and_cases_preserved']}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
