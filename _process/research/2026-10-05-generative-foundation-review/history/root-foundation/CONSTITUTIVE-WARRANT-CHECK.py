#!/usr/bin/env python3
"""Verify this philosophical assessment's owned integration; no scientific rerun."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import unquote
import hashlib, importlib.util, json, re, sys
sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').is_file())
DOC=HERE/'CONSTITUTIVE-WARRANT-ARGUMENT.md'
EDITS=HERE/'CONSTITUTIVE-WARRANT-INDEX-EDITS.json'
OUTPUT=HERE/'CONSTITUTIVE-WARRANT-CHECKS.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    spec=importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    assert sha(DOC)=='ba30f28abc1ffaff8d14f50e736649765448d24ba718db614f2919ca89111564'
    edits=json.loads(EDITS.read_text());assert len(edits['shared_fragments'])==5
    texts=[(DOC,DOC.read_text())]
    for f in edits['shared_fragments']:
        p=ROOT/f['path'];assert p.read_text().count(f['text'])==1,f['path']
        texts.append((p,f['text']))
    links=[]
    for p,text in texts:
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
            if re.match(r'^[a-zA-Z]+:',ref):continue
            name,_,fragment=ref.partition('#');q=(p.parent/unquote(name)).resolve() if name else p
            assert q.is_relative_to(ROOT)
            assert q.is_file() or q==OUTPUT,(p,ref)
            if fragment:assert unquote(fragment) in chain.heading_ids(q),(p,ref)
            links.append({'from':str(p.relative_to(ROOT)),'reference':ref})
    data=chain.read_data();entries={e['id']:e for sec in data['sections'] for e in sec['entries']}
    assert entries['C01']==edits['rows_after']['C01']
    canonical=[l for l in chain.render(data).splitlines() if l.startswith('| C01 |')]
    current=[l for l in chain.OUTPUT.read_text().splitlines() if l.startswith('| C01 |')]
    assert len(canonical)==1 and current==canonical
    for p,expected in edits['owned_reviewed_sources'].items():
        assert sha(ROOT/p)==expected==data['reviewed_sources'][p]
    assert edits['other_rows_unchanged'] and edits['generated_other_rows_unchanged']
    result={'passed':True,'checked_at_utc':datetime.now(timezone.utc).isoformat(),
      'scope':'Philosophical assessment, five owned fragments, source binding, local links and C01 only. No new theorem, experiment, Lean run or universal completion.',
      'argument_sha256':sha(DOC),'independent_assessment_present':'## 7.' in DOC.read_text(),
      'owned_fragments':5,'owned_rows':['C01'],'local_links_checked':len(links),'links':links,
      'other_rows_preservation_attested_by_manifest':True,'concurrent_global_changes_not_certified':chain.changes(data),
      'artifact_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [DOC,EDITS,Path(__file__),HERE/'build_generative_chain.py']}}
    assert result['independent_assessment_present']
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':True,'links':len(links),'fragments':5,'new_theorems':0,'universal_completion':False}))
if __name__=='__main__':main()
