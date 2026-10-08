#!/usr/bin/env python3
"""Freeze and kernel-check action-aware tracking and its inherited tracking module against pinned Mathlib.

Uses the existing cache without installs; audits all explicit declarations.
The projection, evidence bounds and ethical application remain premises.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'ActionAwareTracking.lean'
SOURCES = {'SituatedTracking': HERE / 'SituatedTracking.lean', 'ActionAwareTracking': SOURCE}
SUPPORT = HERE.parents[1] / 'universal-ethics/generative-capacity/check.py'
TOOLCHAIN = 'leanprover/lean4:v4.30.0-rc2'
MATHLIB_REV = 'ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa'
IMPORTS = {'Mathlib.Analysis.SpecificLimits.Basic', 'Mathlib.Tactic', 'SituatedTracking'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    retained = HERE / 'action-aware-tracking-checks' / stamp
    retained.mkdir(parents=True)
    sources = {name: p.read_bytes() for name, p in SOURCES.items()}
    helpers = {'check_action_aware_tracking.py': Path(__file__).read_bytes(),
               'declaration_audit_support.py': SUPPORT.read_bytes()}
    for name, source in sources.items():
        (retained / (name+".lean")).write_bytes(source)
    for name, b in helpers.items():
        (retained / name).write_bytes(b)
    receipt = {'status': 'checking', 'utc': stamp, 'retained_run': str(retained.relative_to(HERE)),
               'source_sha256': {name: sha(source) for name, source in sources.items()},
               'checker_sha256': {n: sha(b) for n, b in helpers.items()},
               'support_source': str(SUPPORT), 'toolchain': TOOLCHAIN,
               'scope': 'Acquired action-response prediction and amplified-error bounds, conditional continuation and finite versus expanding relation coverage. The fixed-response calibration/use law and error correspondence remain supplied; no empirical calibration, general awareness, ethical permission or whole-frontier convergence is certified.'}
    try:
        spec = importlib.util.spec_from_file_location('declaration_audit_support', retained / 'declaration_audit_support.py')
        audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(audit)
        registries = {}
        for name, source in sources.items():
            imports = re.findall(r'^import\s+(.+)$', audit.code_only(source.decode()), re.M)
            assert set(imports) <= IMPORTS
            assert set(imports) == ({'SituatedTracking'} if name == 'ActionAwareTracking' else IMPORTS-{'SituatedTracking'})
            scanner_text = re.sub(r'^import .+$', 'import Std', source.decode(), flags=re.M)
            scanner_text = scanner_text.replace('noncomputable section', 'section')
            registries[name] = audit.declarations(scanner_text)
        project = Path(os.environ.get('SYSTEMS_MATHLIB_PROJECT', str(Path.home() / 'repos/生生不息')))
        manifest_path = project / 'lake-manifest.json'
        manifest_bytes = manifest_path.read_bytes()
        manifest = json.loads(manifest_bytes)
        assert next(p for p in manifest['packages'] if p['name'] == 'mathlib')['rev'] == MATHLIB_REV
        packages = project / manifest.get('packagesDir', '.lake/packages')
        mathlib = packages / 'mathlib'
        assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=mathlib, text=True).strip() == MATHLIB_REV
        assert (mathlib / 'lean-toolchain').read_text().strip() == TOOLCHAIN
        compiler = Path.home() / '.elan/toolchains/leanprover--lean4---v4.30.0-rc2/bin/lean'
        compiler_hash = sha(compiler.read_bytes())
        libraries = sorted(p / '.lake/build/lib/lean' for p in packages.iterdir()
                           if (p / '.lake/build/lib/lean').is_dir())
        with tempfile.TemporaryDirectory(prefix='action-aware-tracking-lean-') as scratch:
            work = Path(scratch)
            env = {**os.environ, 'LEAN_PATH': ':'.join([str(work), *map(str, libraries)])}
            for name, source in sources.items():
                (work / (name+".lean")).write_bytes(source)

            def run(args, log):
                p = subprocess.run([str(compiler), *args], cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0 and not re.search(r'\b(error|warning):', p.stdout), p.stdout
                return p.stdout

            receipt['lean_version'] = run(['--version'], 'version.log').strip()
            assert 'version 4.30.0-rc2,' in receipt['lean_version']
            modules = []
            for module, registry in registries.items():
                run(['-o', module+'.olean', module+'.lean'], module+'.log')
                for suffix, command, items in [('AxiomAudit', '#print axioms', registry),
                                                ('Signatures', '#check', [x for x in registry if x['kind'] == 'theorem'])]:
                    name = module + suffix
                    contents = 'import '+module+'\n' + '\n'.join(command+' '+x['name'] for x in items)+'\n'
                    (work / (name+'.lean')).write_text(contents)
                    (retained / (name+'.lean')).write_text(contents)
                    output = run([name+'.lean'], name+'.log')
                    if suffix == 'AxiomAudit':
                        dependencies = {}
                        for x in registry:
                            full = x['name']
                            if "'"+full+"' does not depend on any axioms" in output:
                                deps = []
                            else:
                                m = re.search("'"+re.escape(full)+r"' depends on axioms:\s*\[([^]]*)\]", output)
                                assert m, full
                                deps = [a.strip() for a in m[1].split(',') if a.strip()]
                            assert set(deps) <= {'propext', 'Classical.choice', 'Quot.sound'}, (full, deps)
                            dependencies[full] = deps
                modules.append({'module':module, 'kernel_checked': True,
                                'theorems':sum(x['kind']=='theorem' for x in registry),
                                'declarations':registry, 'axiom_dependencies':dependencies})
            dep_log = run(['--deps', 'SituatedTracking.lean'], 'dependencies.log')
            dep_hashes = {line: sha(Path(line).read_bytes()) for line in dep_log.splitlines() if Path(line).is_file()}
        assert all(SOURCES[name].read_bytes() == source for name, source in sources.items())
        assert Path(__file__).read_bytes() == helpers['check_action_aware_tracking.py']
        assert SUPPORT.read_bytes() == helpers['declaration_audit_support.py']
        assert sha(compiler.read_bytes()) == compiler_hash and manifest_path.read_bytes() == manifest_bytes
        assert all(sha(Path(p).read_bytes()) == h for p, h in dep_hashes.items())
        receipt.update(status='passed', source_unchanged_during_check=True,
                       lean_binary_sha256=compiler_hash, mathlib_revision=MATHLIB_REV,
                       manifest_sha256=sha(manifest_bytes), direct_import_sha256=dep_hashes,
                       upstream_rebuilt=False, inherited_project_theorems_rebuilt=15,
                       modules=modules,
                       artifact_sha256={p.name:sha(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()})
    except Exception as error:
        receipt.update(status='failed', error=str(error))
        raise
    finally:
        serialized = json.dumps(receipt, indent=2)+'\n'
        (retained / 'verification.json').write_text(serialized)
        (HERE / 'action-aware-tracking-verification.json').write_text(serialized)
    model = next(m for m in receipt['modules'] if m['module'] == 'ActionAwareTracking')
    print(json.dumps({'status':receipt['status'], 'new_theorems':model['theorems'],
                      'new_audits':len(model['declarations']), 'artifacts':len(receipt['artifact_sha256'])}))


if __name__ == '__main__':
    main()
