#!/usr/bin/env python3
"""Bind a completed research round to checked sources and preserved genealogy.

This checks documentary integration, not new scientific or ethical claims.
Historical note prefixes and prior formal results are preserved independently.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PACKAGE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"
BASELINE = {'_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md': {'bytes': 21030, 'sha256': '76d031ed60d7aecaeb1835ad71b1ee2297b10dff76f54dc2bba4c75659c44019'}, '_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-ETHICAL-ARGUMENT.md': {'bytes': 37804, 'sha256': '07e6bbe9a0786f4bd6b6af698ff08c0574cf5bbfd6f3306764abc426782d7a4a'}, '_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-COMPARATORS.md': {'bytes': 27935, 'sha256': 'b89f241984474cabcb15072f713cd2b60ed6d4a9f9d6924f5e454ab9e22ad263'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean': {'bytes': 17824, 'sha256': 'e04fbba5fa726eb8c4430ce48bd2b6c0a14213f5c134e0628fe116d7a2bb1b47'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean': {'bytes': 19136, 'sha256': '99f075dc281d26d8bcc2d713805a17a407396ff86b4fe1b6d16460cb41a5d34e'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/verification.json': {'bytes': 18849, 'sha256': 'a8cb243f68cf196a420db1f895de89341b2808ee121fe6decda3c5d6ac6f858e'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/routes-verification.json': {'bytes': 19897, 'sha256': '28cab74bc6be5f7f38c67539dbc13e37a6661cc2ad6ad935053b07b5092826db'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correspondence-verification.json': {'bytes': 19102, 'sha256': '045c0d636a0f54662aebf4bc0589c94ca73b0e20bfe9c7eb198221d74b7be127'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/routes-correspondence-verification.json': {'bytes': 106973, 'sha256': 'acea0d40e84acc399545c32a9456164062e49dce178ab0cbb82049ff40061325'}}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def anchors(text):
    result=set(); seen={}
    for heading in re.findall(r"^#{1,6}\s+(.+)$",text,re.M):
        heading=re.sub(r"\[([^]]*)\]\([^)]*\)",r"\1",heading)
        base=re.sub(r"[^\w -]","",heading.strip().lower()).replace(" ","-")
        count=seen.get(base,0); seen[base]=count+1
        result.add(base if count==0 else f"{base}-{count}")
    return result


def main():
    preserved=[]
    for rel,old in BASELINE.items():
        now=(ROOT/rel).read_bytes()
        assert digest(now[:old['bytes']])==old['sha256'],rel
        if not rel.endswith('.md'): assert len(now)==old['bytes'],rel
        preserved.append({'path':rel,**old,'preserved':True})
    proof_path=PACKAGE/'reconfiguration-verification.json'
    replay_path=PACKAGE/'reconfiguration-correspondence-verification.json'
    proof=json.loads(proof_path.read_text()); replay=json.loads(replay_path.read_text())
    for receipt in (proof,replay):
        assert receipt['status']=='passed'
        for name,sha in receipt['source_sha256'].items():
            fname=name if name.endswith('.lean') else name+'.lean'
            path=PACKAGE.parents[1]/fname if fname=='GenerativeCore.lean' else PACKAGE/fname
            assert digest(path.read_bytes())==sha,(path,'source')
        for name,sha in receipt['checker_sha256'].items():
            assert digest((PACKAGE/name).read_bytes())==sha,(name,'checker')
    retained=PACKAGE/proof['retained_run']
    for name,sha in proof['artifact_sha256'].items():
        assert digest((retained/name).read_bytes())==sha,(name,'retained')
    module=next(m for m in proof['modules'] if m['module']=='ReconfigurableRoutes')
    assert module['kernel_checked']
    axioms=sorted({a for aa in module['axiom_dependencies'].values() for a in aa})
    assert set(axioms)<={'propext','Quot.sound'}
    documents={HERE/name:None for name in ['GENERATIVE-CAPACITY-INTEGRATION.md',
      'GENERATIVE-CAPACITY-ETHICAL-ARGUMENT.md','GENERATIVE-CAPACITY-COMPARATORS.md']}
    documents[PACKAGE/'README.md']=None
    theory=ROOT/'theories/shengsheng-buxi-generative-existence'
    for path in [ROOT/'RESEARCH.md',theory/'README.md',
                 theory/'unified-2026-10-05/GENERATIVE-GROUNDING.md',HERE/'README.md']:
        text=path.read_text()
        documents[path]='\n'.join(p for p in text.split('\n\n') if '重组与建设性结束' in p)
        assert documents[path],path
    canonical=theory/'unified-2026-10-05/UNIFIED-ETHICAL-GROUNDING.md'
    text=canonical.read_text(); start=text.index('## Reconfiguration and constructive endings')
    end=text.find('\n## ',start+4)
    documents[canonical]=text[start:end if end!=-1 else None]
    universal=HERE/'UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md'
    text=universal.read_text(); start=text.index('## 17. Reconfiguration and constructive endings')
    documents[universal]=text[start:]
    links=[]; document_hashes={}
    for path,selected in documents.items():
        data=path.read_bytes(); text=data.decode() if selected is None else selected
        document_hashes[str(path.relative_to(ROOT))]=digest(data)
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)",text):
            if ':' in target.split('/')[0]: continue
            file,_,fragment=unquote(target).partition('#')
            dest=(path.parent/file).resolve() if file else path
            assert dest.exists(),(path,target)
            if fragment and dest.suffix=='.md':
                assert fragment in anchors(dest.read_text()),(path,target,'anchor')
            links.append({'from':str(path.relative_to(ROOT)),'target':target})
    source_paths=[ROOT/'sources/15-codex-theory-conversations'/name for name in
      ['2026-10-07-shengsheng-ethical-direction.md','2026-10-07-generativity-future-horizon.md']]
    source_hashes={str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in source_paths}
    old=json.loads((HERE/'FORMATION-ROUTES-CHECKS.json').read_text())
    assert source_hashes==old['human_sources'], 'Primary source changed since prior round'
    # Explicit shengsheng source digest also preserves Ren's primary wording.
    assert source_hashes[str(source_paths[0].relative_to(ROOT))]=='c453e4e37c57a09f6f2304b210898ceeb884a759ca7b0a49668c4fc941ca5a59'
    receipt={'status':'passed','utc':datetime.now(timezone.utc).isoformat(),
      'scope':'Documentary links, source/receipt correspondence and preservation; not an additional theorem or empirical test.',
      'new_theorems':module['theorems'],'new_declaration_audits':len(module['declarations']),
      'axioms':axioms,'matched_state_records':replay['matched_state_records'],
      'proof_receipt_sha256':digest(proof_path.read_bytes()),
      'replay_receipt_sha256':digest(replay_path.read_bytes()),
      'model_sha256':digest((PACKAGE/'ReconfigurableRoutes.lean').read_bytes()),
      'checker_sha256':digest(Path(__file__).read_bytes()),'prior_preservation':preserved,
      'source_sha256':source_hashes,'document_sha256':document_hashes,
      'local_links_checked':len(links),'links':links,'errors':[]}
    (HERE/'RECONFIGURATION-CHECKS.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','new_declaration_audits',
                                           'matched_state_records','local_links_checked']}))


if __name__=='__main__': main()
