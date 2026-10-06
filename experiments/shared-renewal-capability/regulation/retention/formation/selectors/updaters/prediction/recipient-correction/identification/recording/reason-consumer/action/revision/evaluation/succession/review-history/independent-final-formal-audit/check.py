"""Read-only receipt/source audit; does not rerun Lean or the model."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent.parent
REPO = next(p for p in STUDY.parents if (p / 'AGENTS.md').exists())
ALLOWED = {'propext', 'Quot.sound', 'Classical.choice'}

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    formal = STUDY / 'formal'
    v = json.loads((formal / 'verification.json').read_text())
    assert v['status'] == 'passed'
    assert v['toolchain'] == 'leanprover/lean4:v4.29.1'
    assert v['source_unchanged_during_check'] and v['fresh_temporary_build']
    assert v['project_objects_only_from_frozen_sources'] and v['protocol_frozen_predecessors_match']
    assert digest(formal / 'check.py') == v['checker_sha256']
    assert digest(formal / 'lean-toolchain') == v['toolchain_sha256']
    assert digest(Path(v['compiler_binary'])) == v['compiler_sha256']
    source_hashes = {}
    new = total = empty = standard = choice = ancestors = 0
    for m in v['modules']:
        source = REPO / m['source']; log = formal / m['output']
        assert digest(source) == m['source_sha256']
        assert digest(log) == m['output_sha256']
        assert m['exit_code'] == 0 and m['clean_dependency_audit']
        text = source.read_text(); output = log.read_text()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text)
        assert not re.search(r'^\s*(axiom|constant)\s', text, re.M)
        assert not re.search(r'\b(error|warning):', output)
        audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output)
        assert len(audits) == m['dependency_audits']
        assert [a for a,_ in audits] == m['audited_declarations']
        for name, deps in audits:
            assert {d.strip() for d in deps.split(',') if d.strip()} <= ALLOWED, name
        total += len(audits)
        if m['role'] == 'new formalization':
            declarations = set(re.findall(r'^theorem\s+(\w+)', text, re.M))
            assert declarations == {a.rsplit('.',1)[-1] for a,_ in audits}
            new += len(audits)
            empty += sum(not deps for _,deps in audits)
            standard += sum(bool(deps) for _,deps in audits)
            choice += sum('Classical.choice' in deps for _,deps in audits)
        else:
            old = subprocess.check_output(['git','show',v['parent_commit']+':'+m['source']], cwd=REPO)
            assert old == source.read_bytes()
            ancestors += 1
        source_hashes[m['source']] = digest(source)
        source_hashes[str(log.relative_to(REPO))] = digest(log)
    assert len(v['modules']) == 29 and ancestors == 26
    assert (new,total,empty,standard,choice) == (92,722,4,88,5)
    assert v['new_audited_declarations'] == new
    c = json.loads((STUDY / 'formal-runtime-crosscheck.json').read_text())
    assert c['status'] == 'passed' and len(c['milestone_comparisons']) == 14
    for group in ('source_sha256','formal_sources_sha256'):
        for name, expected in c[group].items():
            assert digest(REPO / name) == expected, name
    for name, expected in v['protocol_sources_sha256'].items():
        assert digest(REPO / name) == expected, name
    for p in [formal/'verification.json',formal/'check.py',formal/'lean-toolchain',
              STUDY/'formal-runtime-crosscheck.json',STUDY/'crosscheck_witness.py',Path(__file__)]:
        source_hashes[str(p.relative_to(REPO))] = digest(p)
    out = dict(status='passed',
        scope='Independent source/log/ancestry and receipt audit after semantic source review; no fresh compiler or scientific rerun.',
        counts=dict(modules=29,unchanged_ancestors=ancestors,new_audits=new,total_audits=total,
                    new_empty=empty,new_standard_only=standard,new_with_Classical_choice=choice,
                    selected_crosscheck_milestones=14),source_sha256=source_hashes,
        repaired_issues=['One core trial authority per probe attempt; archive flushing does not reopen it.',
                        'Interventions only cut guards; positive birth grants remain supplied.',
                        'Selected crosscheck requires commissioned child, not ownership transfer alone.'])
    (HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['counts']))

if __name__ == '__main__':
    main()
