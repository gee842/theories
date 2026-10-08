#!/usr/bin/env python3
"""Document, source-preservation and frozen-result binding for this ethical round.

No new compiler execution, theorem or empirical test is claimed by this script.
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
BASELINE = {'_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md': {'bytes': 36221, 'sha256': '0173eddbb9667ec33e340e1f3dd884eb491bb3d8894c085c62becd7a3c84e4cd'}, 'sources/15-codex-theory-conversations/2026-10-07-generation-axiom-and-future.md': {'bytes': 2731, 'sha256': 'fc9824eb837482c6253e6eb3f7a8bd2932902033bb305d49f09d4021fab9a515'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean': {'bytes': 19136, 'sha256': '99f075dc281d26d8bcc2d713805a17a407396ff86b4fe1b6d16460cb41a5d34e'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean': {'bytes': 17824, 'sha256': 'e04fbba5fa726eb8c4430ce48bd2b6c0a14213f5c134e0628fe116d7a2bb1b47'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean': {'bytes': 21109, 'sha256': '747929335d04ce9703070af7cfc309bb996a4695f19e96ff5d6dd6392c743141'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/reconfiguration-verification.json': {'bytes': 33604, 'sha256': '4573bc0a1aa5e1dde9ff85b784d99b44412a506c074a2429af2c28c8f5a25edb'}, 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/reconfiguration-correspondence-verification.json': {'bytes': 975102, 'sha256': '80ede2cfb054ef4d28e3b0876983082b0eb5de6929eca77b4d2b0b17b878f00c'}}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def anchors(text):
    found=set(); seen={}
    for h in re.findall(r"^#{1,6}\s+(.+)$",text,re.M):
        h=re.sub(r"\[([^]]*)\]\([^)]*\)",r"\1",h)
        slug=re.sub(r"[^\w -]","",h.strip().lower()).replace(" ","-")
        number=seen.get(slug,0); seen[slug]=number+1
        found.add(slug if number==0 else f"{slug}-{number}")
    return found


def main():
    preserved=[]
    for relative,original in BASELINE.items():
        data=(ROOT/relative).read_bytes()
        assert digest(data[:original['bytes']])==original['sha256'],relative
        if not relative.endswith('GENERATIVE-CAPACITY-INTEGRATION.md'):
            assert len(data)==original['bytes'],relative
        preserved.append({'path':relative,**original,'preserved':True})
    source=ROOT/'sources/15-codex-theory-conversations/2026-10-07-generative-premise-route-approved.md'
    assert re.findall(r'^> (.*)$',source.read_text(),re.M)==['ok，请沿这个方向继续']
    proof_path=PACKAGE/'comparison-verification.json'; proof=json.loads(proof_path.read_text())
    assert proof['status']=='passed' and proof['source_unchanged_during_check']
    for name,sha in proof['source_sha256'].items():
        assert digest((PACKAGE/(name+'.lean')).read_bytes())==sha,name
    for name,sha in proof['checker_sha256'].items():
        assert digest((PACKAGE/name).read_bytes())==sha,name
    retained=PACKAGE/proof['retained_run']
    for name,sha in proof['artifact_sha256'].items():
        assert digest((retained/name).read_bytes())==sha,name
    assert (retained/'verification.json').read_bytes()==proof_path.read_bytes()
    model=next(m for m in proof['modules'] if m['module']=='GenerativeComparison')
    assert model['kernel_checked']
    ax=sorted({a for deps in model['axiom_dependencies'].values() for a in deps})
    assert set(ax)<={'propext','Quot.sound'}
    docs={HERE/name:None for name in ['GENERATIVE-PREMISE-INTEGRATION.md',
        'GENERATIVE-PREMISE-DERIVATION.md','GENERATIVE-PREMISE-REVIEW.md']}
    docs[source]=None
    package_readme=PACKAGE/'README.md'
    docs[package_readme]=package_readme.read_text().split('## Generative premise and situated comparison',1)[1]
    for rel in ['README.md','RESEARCH.md','_process/BRIEF.md','sources/SOURCES.md',
      'theories/becoming/README.md',
      'theories/becoming/chapters/GENERATIVE-GROUNDING.md',
      str((HERE/'README.md').relative_to(ROOT))]:
        path=ROOT/rel
        docs[path]='\n\n'.join(block for block in path.read_text().split('\n\n')
            if 'GENERATIVE-PREMISE' in block or 'generative-premise' in block)
        assert docs[path],rel
    canonical=ROOT/'theories/becoming/chapters/UNIFIED-ETHICAL-GROUNDING.md'
    text=canonical.read_text(); start=text.index('## From the generative premise to situated reasons')
    docs[canonical]=text[start:text.index('\n## ',start+4)]
    for file,heading in [('GENERATIVE-CAPACITY-INTEGRATION.md','## 16. '),
                         ('UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md','## 18. ')]:
        path=HERE/file;text=path.read_text();docs[path]=text[text.index(heading):]
    links=[]
    for path,selection in docs.items():
        text=path.read_text() if selection is None else selection
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)",text):
            if ':' in target.split('/')[0]: continue
            file,_,fragment=unquote(target).partition('#')
            dest=(path.parent/file).resolve() if file else path
            assert dest.exists(),(path,target)
            if fragment and dest.suffix=='.md':
                assert fragment in anchors(dest.read_text()),(path,target,'anchor')
            links.append({'from':str(path.relative_to(ROOT)),'target':target})
    receipt={'status':'passed','utc':datetime.now(timezone.utc).isoformat(),
      'scope':'Frozen proof/source bindings, source quotation and prior-byte preservation, new document links. No extra mathematical or empirical validation.',
      'new_theorems':model['theorems'],'explicit_declaration_audits':len(model['declarations']),
      'axiom_dependencies':ax,'model_sha256':proof['source_sha256']['GenerativeComparison'],
      'proof_receipt_sha256':digest(proof_path.read_bytes()),'source_sha256':digest(source.read_bytes()),
      'checker_sha256':digest(Path(__file__).read_bytes()),'prior_preservation':preserved,
      'document_sha256':{str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in docs},
      'local_links_checked':len(links),'links':links,'errors':[]}
    (HERE/'GENERATIVE-PREMISE-CHECKS.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','new_theorems','explicit_declaration_audits','local_links_checked']}))


if __name__=='__main__': main()
