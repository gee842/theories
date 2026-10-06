#!/usr/bin/env python3
"""Fresh Lean build, dependency audit, runtime cases and independent review."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
BASIS = ROOT.parent
TOOLCHAIN = 'leanprover/lean4:v4.29.1'
SOURCES = [BASIS/'lean/GenerativeCore.lean',
           BASIS/'lean/conditional/ResourceContinuation.lean',
           ROOT/'PatientConcern.lean', ROOT/'GroundingContract.lean', ROOT/'Cases.lean']
ALLOWED = {'propext', 'Quot.sound', 'Classical.choice'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def execute(command, cwd, env):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def main():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    version = execute(['lean','+'+TOOLCHAIN,'--version'], ROOT, env)
    version.check_returncode()
    assert 'version 4.29.1,' in version.stdout
    frozen = {p: p.read_bytes() for p in SOURCES}
    for p, data in frozen.items():
        source = data.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', source), p
        assert not re.search(r'^\s*(axiom|constant)\s', source, re.M), p
    logs = ROOT/'verification'
    logs.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix='noninstrumental-fresh-') as temporary:
        build = Path(temporary)
        for p,data in frozen.items():
            (build/p.name).write_bytes(data)
        build_env = dict(env, LEAN_PATH=str(build))
        for p in SOURCES:
            result = execute(['lean','+'+TOOLCHAIN,'-o',p.stem+'.olean',p.name],build,build_env)
            log = logs/(p.stem+'.txt')
            log.write_text(result.stdout)
            audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",result.stdout)
            expected = len(re.findall(r'^#print axioms ',frozen[p].decode(),re.M))
            axioms = sorted({x.strip() for _,xs in audits for x in xs.split(',') if x.strip()})
            clean = (result.returncode == 0 and 'warning:' not in result.stdout
                     and 'sorryAx' not in result.stdout and len(audits) == expected
                     and expected > 0 and set(axioms) <= ALLOWED)
            item = dict(module=p.stem, source=str(p.relative_to(BASIS)),
                        source_sha256=sha(frozen[p]), exit_code=result.returncode,
                        dependency_audits=len(audits), axioms=axioms,
                        clean=clean, log=str(log.relative_to(ROOT)),
                        log_sha256=sha(log.read_bytes()),
                        audited_declarations=[name for name,_ in audits])
            results.append(item)
            if not clean:
                print(result.stdout)
                break
    runtime = execute([sys.executable,'-B','model.py'],ROOT,env)
    (logs/'runtime.txt').write_text(runtime.stdout)
    independent = None
    if (ROOT/'independent_review.py').exists():
        independent = execute([sys.executable,'-B','independent_review.py'],ROOT,env)
        (logs/'independent.txt').write_text(independent.stdout)
    unchanged = all(p.read_bytes() == data for p,data in frozen.items())
    passed = (len(results) == len(SOURCES) and all(x['clean'] for x in results)
              and unchanged and runtime.returncode == 0
              and independent is not None and independent.returncode == 0)
    record = dict(status='passed' if passed else 'failed',
                  checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  toolchain=TOOLCHAIN, lean_version=version.stdout.strip(),
                  fresh_temporary_build=True, sources_unchanged=unchanged,
                  checker_sha256=sha(Path(__file__).read_bytes()), modules=results,
                  new_dependency_audits=sum(x['dependency_audits'] for x in results if x['module'] not in {'GenerativeCore','ResourceContinuation'}),
                  runtime_exit_code=runtime.returncode,
                  runtime_sha256=sha((ROOT/'model.py').read_bytes()),
                  cases_sha256=sha((ROOT/'cases.json').read_bytes()),
                  independent_exit_code=None if independent is None else independent.returncode,
                  scope='Conditional normative contracts, declared patient-indexed paid process and finite runtime comparisons. No derivation of C1/C2, experience identification, total ethical ordering, automatic helping or general Python-to-Lean refinement.')
    (ROOT/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','new_dependency_audits','runtime_exit_code','independent_exit_code')},indent=2))
    if not passed:
        if independent is not None and independent.returncode: print(independent.stdout)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
