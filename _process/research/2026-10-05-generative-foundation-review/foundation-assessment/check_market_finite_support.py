#!/usr/bin/env python3
"""Check the finite-support obstruction's source-bound receipt and owned documentary links.

No new Lean run, empirical claim, or certification of unrelated registry entries.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
from tools.research import generative_chain as chain
from tools.research import registry


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    formal = ROOT/'experiments/market-generativity/formal'
    receipt = json.loads((formal/'finite-support-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert len(receipt['theorems']) == 17
    assert len(receipt['new_audits']) == 22
    assert len(receipt['inherited_audits']) == 153
    assert sum(map(len, receipt['inherited_theorems'].values())) == 123
    assert receipt['checker_sha256'] == sha(formal/'check_finite_support.py')
    for name, digest in receipt['sources'].items():
        assert sha(formal/name) == digest == sha(formal/'finite-support-verification'/name), name
    for name, digest in receipt['log_hashes'].items():
        assert sha(formal/'finite-support-verification'/(name+'.txt')) == digest, name
    fragments = {
        HERE/'MARKET-INTERNET-DEGENERATION.md': '<a id="finite-support-obstruction"></a>',
        ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MARKETS-AND-GENERATIVE-REGIMES.md': '<a id="finite-support-obstruction"></a>',
        formal/'README.md': '<a id="checked-finite-support-obstruction"></a>',
    }
    links = []
    for path, marker in fragments.items():
        text = path.read_text()
        assert text.count(marker) == 1
        fragment = text[text.index(marker):]
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)\s]+)\)', fragment):
            if target.startswith(('https://', 'http://', 'mailto:')):
                continue
            name, _, anchor = target.partition('#')
            resolved = (path.parent/name).resolve() if name else path
            assert resolved.exists(), (path, target)
            if anchor and resolved.suffix == '.md':
                assert anchor in chain.heading_ids(resolved), (path, target)
            links.append({'source': str(path.relative_to(ROOT)), 'target': target})
    records, load_errors = registry.load_records()
    assert not load_errors, load_errors
    errors, drift = registry.validate(records)
    selected = {'market-protected-continuation', 'market-supported-finite-transition', 'market-partial-correction-boundary', 'market-finite-support-obstruction'}
    own_errors = [e for e in errors if e.split(':')[0] in selected]
    own_drift = [d for d in drift if d['id'] in selected]
    assert not own_errors and not own_drift, (own_errors, own_drift)
    for r in records:
        if r['id'] in selected:
            assert registry.record_path(r).with_suffix('.md').read_text() == registry.render_record(r)
    edits = json.loads((HERE/'MARKET-FINITE-SUPPORT-INDEX-EDITS.json').read_text())
    assert edits['other_entries_unchanged'] and edits['other_rendered_lines_unchanged']
    data = json.loads(chain.DATA.read_text())
    entry = next(e for sec in data['sections'] for e in sec['entries'] if e['id'] == 'M20')
    for field, suffix in edits['suffixes'].items():
        assert suffix in entry[field]
    for link in edits['links_added']:
        assert link in entry['links']
    row = next(l for l in chain.render(data).splitlines() if l.startswith('| M20 '))
    assert row in chain.OUTPUT.read_text().splitlines()
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'new_theorems': 17, 'new_audits': 22, 'inherited_theorems': 123, 'inherited_audits': 153,
        'source_receipt_bindings': 'current and frozen sources, checker and logs match',
        'owned_links': links, 'selected_registry_errors': own_errors, 'selected_source_drift': own_drift,
        'm20_owned_additions_and_render': 'verified; other rows preserved at update',
        'unrelated_registry_errors': [e for e in errors if e not in own_errors],
        'unrelated_registry_drift': [d for d in drift if d['id'] not in selected],
        'current_chain_metadata_errors': chain.validate(data),
        'pending_unrelated_chain_versions': chain.changes(data)['modified_sources'],
        'concurrent_work_seen': {
            'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalBecoming.lean': 'Parallel effective versus eventual capacity work; not imported, duplicated or independently accepted in this proof.',
            '_process/research/2026-10-05-generative-foundation-review/root-foundation/CORE-CONSTRAINT-AND-WISDOM.md': 'Parallel wisdom development; not incorporated as a premise or independently accepted here.',
            '_process/research/2026-10-05-generative-foundation-review/root-foundation/GROWN-FRAGMENTATION-INTEGRATION.md': 'Parallel formed-structure continuation; existing entry records inspected, no market adapter assumed.',
            '_process/research/2026-10-05-generative-foundation-review/root-foundation/EXPLANATORY-JOINING-CONTEXTS-INTEGRATION.md': 'Parallel explanatory joining; not imported into this market proof.'},
        'scope': 'The compiled source is unchanged since the successful 17-theorem receipt. Scoped documentary and receipt checks, not a new proof run or whole-repository acceptance. Concurrent organization, wisdom, inquiry and registry work retains independent scope.'}
    (HERE/'MARKET-FINITE-SUPPORT-CHECKS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'owned_links': len(links),
                      'new_theorems': 17, 'selected_registry_errors': own_errors,
                      'selected_source_drift': own_drift,
                      'pending_chain_metadata_errors': len(result['current_chain_metadata_errors'])}))


if __name__ == '__main__':
    main()
