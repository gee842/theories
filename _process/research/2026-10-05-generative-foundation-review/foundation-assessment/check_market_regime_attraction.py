#!/usr/bin/env python3
"""Check this study's documentary links, preservation and actual proof receipt.

This does not rerun science or certify freshness of unrelated chain sources.
"""
from datetime import datetime, timezone
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    edits = json.loads((HERE/'MARKET-REGIME-ATTRACTION-EDITS.json').read_text())
    spec = importlib.util.spec_from_file_location(
        'chain', HERE.parent/'root-foundation/build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    preservation, links, errors = {}, [], []
    for name, entry in edits['files'].items():
        path = ROOT/name
        raw = path.read_bytes()
        if entry['edit'] == 'append':
            n = entry['before_bytes']
            end = n+entry['append_bytes']
            assert sha(raw[:n]) == entry['before_sha256'], name
            assert sha(raw[:end]) == entry['after_owned_sha256'], name
            fragment = raw[n:end].decode()
            preservation[name] = 'exact earlier prefix and owned append retained'
        else:
            fragment = entry['owned_fragment']
            text = raw.decode()
            assert text.count(fragment) == 1, name
            inverse = text.replace(fragment, '', 1).encode()
            preservation[name] = (
                'exact insertion inverse verified' if sha(inverse) == entry['before_sha256']
                else 'owned insertion retained; subsequent concurrent edits differ from pre-insertion snapshot')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)\s]+)\)', fragment):
            if target.startswith(('https://', 'http://', 'mailto:')):
                continue
            relative, _, anchor = target.partition('#')
            resolved = (path.parent/relative).resolve() if relative else path
            links.append({'source': name, 'target': target})
            if not resolved.exists():
                errors.append('missing '+str(resolved))
            elif anchor and resolved.suffix == '.md' and anchor not in chain.heading_ids(resolved):
                errors.append('missing anchor '+str(resolved)+'#'+anchor)
    assert not errors, errors
    formal = ROOT/'experiments/market-generativity/formal'
    receipt = json.loads((formal/'attraction-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert len(receipt['theorems']) == 38
    assert len(receipt['new_audits']) == 52
    assert len(receipt['inherited_audits']) == 66
    assert receipt['checker_sha256'] == sha((formal/'check_attraction.py').read_bytes())
    for name, digest in receipt['sources'].items():
        assert digest == sha((formal/name).read_bytes()), name
        assert digest == sha((formal/'attraction-verification'/name).read_bytes()), name
    for name, digest in receipt['log_hashes'].items():
        assert digest == sha((formal/'attraction-verification'/(name+'.txt')).read_bytes())
    figure = json.loads((formal/'figures/regime-fixed-states.json').read_text())
    assert figure['proof_receipt_sha256'] == sha((formal/'attraction-verification.json').read_bytes())
    assert figure['script_sha256'] == sha((formal/'plot_regime_states.py').read_bytes())
    for name, digest in figure['outputs'].items():
        assert digest == sha((formal/'figures'/name).read_bytes()), name
    data = json.loads((ROOT/'theories/shengsheng-buxi-generative-existence/results/data/generativity-chain.json').read_text())
    schema_errors = chain.validate(data)
    assert not schema_errors, schema_errors
    entry = next(e for section in data['sections'] for e in section['entries'] if e['id'] == 'M20')
    inverse = copy.deepcopy(entry)
    for field, addition in edits['chain']['field_additions'].items():
        assert inverse[field].count(addition) == 1, field
        inverse[field] = inverse[field].replace(addition, '', 1)
    for link in edits['chain']['added_links']:
        assert inverse['links'].count(link) == 1
        inverse['links'].remove(link)
    entry_inverse_same = sha(json.dumps(inverse, ensure_ascii=False, sort_keys=True).encode()) == edits['chain']['entry_before_sha256']
    canonical = next(line for line in chain.render(data).splitlines() if line.startswith('| M20 |'))
    rendered = (ROOT/'theories/shengsheng-buxi-generative-existence/results/GENERATIVITY-CHAIN.md').read_text()
    assert [line for line in rendered.splitlines() if line.startswith('| M20 |')] == [canonical]
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'edits_sha256': sha((HERE/'MARKET-REGIME-ATTRACTION-EDITS.json').read_bytes()),
        'preservation': preservation, 'local_links_checked': len(links), 'link_errors': errors,
        'actual_lean_receipt_matches_current_and_frozen_sources': True,
        'new_theorems': 38, 'new_audits': 52, 'inherited_audits': 66,
        'inherited_theorems': 58, 'figure_bound_to_receipt_and_script': True,
        'm20_matches_canonical_render': True, 'm20_exact_inverse_matches_snapshot': entry_inverse_same,
        'other_entries_preserved_at_write': edits['chain']['other_entries_preserved'],
        'other_rendered_lines_preserved_at_write': edits['chain']['other_rendered_lines_preserved'],
        'schema_link_errors': schema_errors, 'pending_separate_reviews': chain.changes(data),
        'scope': 'Owned documentary and proof-receipt checks only. Concurrent work retained. '
                 'No new scientific run, independent acceptance, empirical validation or full-table freshness.'}
    (HERE/'MARKET-REGIME-ATTRACTION-CHECKS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'local_links': len(links),
                      'new_theorems': 38, 'new_audits': 52, 'inherited_audits': 66,
        'inherited_theorems': 58, 'figure_bound_to_receipt_and_script': True,
                      'm20_exact_inverse': entry_inverse_same}, ensure_ascii=False))


if __name__ == '__main__':
    main()
