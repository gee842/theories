#!/usr/bin/env python3
"""Validate articulation links and the existing evidence actually cited.

No Lean compilation, simulation, empirical reanalysis or philosophical
certification is performed. The older broad core/tree receipt is used only for
the unchanged transitive GenerativeEpisode closure; unrelated evolved roots
are reported separately rather than falsely certified against that receipt.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
PREDICTION = ROOT / 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction'
PLASTICITY = PREDICTION / 'recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity'
CAPACITY = LEAN / 'universal-ethics/generative-capacity'
DOCS = [THEORY / 'SHENGSHENG.md', HERE / 'SHENGSHENG-ARTICULATION-RECORD.md',
        ROOT / 'sources/15-codex-theory-conversations/2026-10-08-shengsheng-articulation.md']
REPORT = HERE / 'SHENGSHENG-ARTICULATION-CHECKS.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


def load(path):
    return json.loads(path.read_text())


def bound(path, expected):
    assert path.is_file(), path
    actual = sha(path)
    assert actual == expected, (rel(path), actual, expected)
    return {'path': rel(path), 'sha256': actual}


def receipt(path, selected_root=None):
    data = load(path)
    assert data['status'] == 'passed', path
    modules = {m['module']: m for m in data['modules']}

    def source(m):
        if 'source' in m:
            return ROOT / m['source']
        if m['module'] == 'GenerativeCore':
            return LEAN / 'GenerativeCore.lean'
        return path.parent / (m['module'] + '.lean')

    chosen = set(modules)
    if selected_root:
        chosen = set()

        def visit(name):
            if name == 'Std':
                return
            assert name in modules, ('uncovered import', name)
            if name in chosen:
                return
            chosen.add(name)
            for module in re.findall(r'^import\s+(.+)$', source(modules[name]).read_text(), re.M):
                for imported in module.split():
                    visit(imported)

        visit(selected_root)
    sources, artifacts, outside_changes = [], [], []
    for name, m in modules.items():
        expected = m.get('source_sha256', m.get('sha256', data.get('source_sha256', {}).get(name)))
        assert expected, name
        if name not in chosen:
            if sha(source(m)) != expected:
                outside_changes.append(rel(source(m)))
            continue
        sources.append(bound(source(m), expected))
        if 'exit_code' in m:
            assert m['exit_code'] == 0
        logfile = m.get('output', m.get('log'))
        loghash = m.get('output_sha256', m.get('log_sha256'))
        if logfile:
            artifacts.append(bound(path.parent / logfile, loghash))
    if 'snapshot' in data:
        run = ROOT / data['snapshot']
        assert load(run / 'verification.json') == data
        for name in chosen:
            m = modules[name]
            artifacts.append(bound(run / 'sources' / (name + '.lean'), m['source_sha256']))
        for name, h in data['log_sha256'].items():
            artifacts.append(bound(run / name, h))
    if 'artifact_sha256' in data:
        run = path.parent / data['retained_run']
        for name, h in data['artifact_sha256'].items():
            artifacts.append(bound(run / name, h))
    return {'receipt': rel(path), 'sha256': sha(path),
            'selected_root': selected_root, 'sources': sources, 'saved_artifacts': artifacts,
            'outside_selected_closure_changed_since_historical_receipt': outside_changes,
            'scope': 'Current cited source closure and retained successful build evidence; no fresh compilation.'}


def main():
    spec = importlib.util.spec_from_file_location('chain_builder', HERE / 'build_generative_chain.py')
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    initial = {p: p.read_bytes() for p in DOCS}
    links, references = [], {}
    for path, raw in initial.items():
        for reference in re.findall(r'\]\(([^)]+)\)', raw.decode()):
            if re.match(r'https?://', reference):
                continue
            target, _, fragment = reference.partition('#')
            resolved = (path.parent / unquote(target)).resolve() if target else path
            if resolved == REPORT:
                # Written by this run after all checks pass. Do not create a
                # recursive claim that the report contains its own final hash.
                assert not fragment
                links.append({'from': rel(path), 'target': reference, 'generated_by_this_run': True})
                continue
            assert resolved.is_relative_to(ROOT) and resolved.is_file(), (path, reference)
            if fragment:
                assert resolved.suffix == '.md'
                assert unquote(fragment) in builder.heading_ids(resolved), (path, reference)
            links.append({'from': rel(path), 'target': reference})
            references[rel(resolved)] = sha(resolved)

    proofs = [receipt(PREDICTION / 'formal/verification.json'),
              receipt(LEAN / 'inquiry-root/core-tree-verification.json', 'GenerativeEpisode'),
              receipt(LEAN / 'new-possibilities-verification.json'),
              receipt(PLASTICITY / 'formal/verification.json'),
              receipt(CAPACITY / 'practical-judgment-verification.json'),
              receipt(CAPACITY / 'routes-verification.json')]
    correspondence_path = PLASTICITY / 'formal-correspondence.json'
    correspondence = load(correspondence_path)
    assert correspondence['status'] == 'fourteen_selected_compiled_milestones_match'
    assert (correspondence['count'], correspondence['coordinates']) == (14, 25)
    correspondence_sources = [bound(PLASTICITY / name, h)
                              for name, h in correspondence['source_sha256'].items()]
    milestones = {m['name']: m['values'] for m in correspondence['milestones']}
    assert milestones['entry']['recipient'] == 40
    assert milestones['aligned_trained']['recipient'] == 36
    assert milestones['aligned_final']['recipient'] == 46
    assert milestones['inert_final']['recipient'] == 36
    assert milestones['gated_final']['recipient'] == 36

    method_path = HERE / 'development/consequence-organization/METHOD-EVIDENCE.json'
    method = load(method_path)
    assert method['status'] == 'passed' and not method['source_mismatches']
    method_sources = [bound(ROOT / name, h) for name, h in method['artifact_sha256'].items()]
    method_results = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/metarevision/methods/formation'
    independent = load(method_results / 'independent-check.json')
    # Keep the original checker's source contract, rather than treating the
    # later extraction as an independent reconstruction of the mechanism.
    assert independent['histories'] == 448
    assert independent['statuses'] == {'complete': 448}
    assert independent['checked_producer_results_sha256'] == sha(method_results / 'results.json')
    method_sources.extend(bound(ROOT / name, h) for name, h in independent['source_hashes'].items())

    chain = builder.read_data()
    assert not builder.validate(chain), builder.validate(chain)
    assert builder.OUTPUT.read_text() == builder.render(chain)
    row = next(e for s in chain['sections'] for e in s['entries'] if e['id'] == 'C01')
    assert any(x['path'] == rel(THEORY / 'SHENGSHENG.md') for x in row['links'])
    for p, raw in initial.items():
        assert p.read_bytes() == raw, ('concurrent owned edit', p)
    for name, h in references.items():
        assert sha(ROOT / name) == h, ('concurrent linked edit', name)
    report = {'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Owned links, exact cited inherited proof closures, selected correspondence, saved method evidence and paired navigation. Semantic review is separately recorded; no new proof or science run.',
              'new_theorems': 0, 'compiler_runs_this_study': 0,
              'documents': {rel(p): sha(p) for p in DOCS},
              'checker_sha256': sha(Path(__file__)), 'local_links': links,
              'linked_versions_at_check': references,
              'proof_evidence': proofs,
              'plasticity_correspondence': {'path': rel(correspondence_path), 'sha256': sha(correspondence_path),
                                           'bound_sources': correspondence_sources, 'milestones': 14,
                                           'scope': correspondence['scope']},
              'method_evidence': {'path': rel(method_path), 'sha256': sha(method_path),
                                  'bound_sources': method_sources, 'scope': method['scope']},
              'chain_row': 'C01', 'chain_changes_remaining': builder.changes(chain)}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'local_links': len(links), 'proof_receipts': len(proofs),
                      'source_bindings': sum(len(p['sources']) for p in proofs),
                      'new_theorems': 0, 'compiler_runs_this_study': 0}))


if __name__ == '__main__':
    main()
