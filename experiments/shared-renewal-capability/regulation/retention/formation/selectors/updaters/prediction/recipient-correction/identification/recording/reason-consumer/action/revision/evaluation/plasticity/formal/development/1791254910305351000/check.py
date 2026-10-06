#!/usr/bin/env python3
"""Fresh frozen Lean build; preserve every attempt and audit declarations."""
from pathlib import Path
import hashlib,json,os,re,subprocess,tempfile,time
ROOT=Path(__file__).resolve().parent
REPO=next(p for p in ROOT.parents if (p/'AGENTS.md').exists())
NEW={'PlasticityPreparation','PairedPlasticity','PlasticityWitness'}
PATHS={'GenerativeCore': 'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean', 'FormedSelection': 'experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean', 'RecipientCorrection': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/RecipientCorrection.lean', 'RecipientIdentification': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/formal/RecipientIdentification.lean', 'EmissionArchive': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/formal/EmissionArchive.lean', 'RecipientArchive': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/formal/RecipientArchive.lean', 'ArchivePreparation': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/formal/ArchivePreparation.lean', 'PaidArchiveReader': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/formal/PaidArchiveReader.lean', 'RecordedEvidence': 'experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/formal/RecordedEvidence.lean', 'ReasonReplay': 'experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean', 'RecipientReasons': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/formal/RecipientReasons.lean', 'PaidRecipientReasons': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/formal/PaidRecipientReasons.lean', 'ReasonPreparation': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/formal/ReasonPreparation.lean', 'ReasonReplayBridge': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/formal/ReasonReplayBridge.lean', 'RecipientAction': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/formal/RecipientAction.lean', 'ActionPreparation': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/formal/ActionPreparation.lean', 'ActionWitness': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/formal/ActionWitness.lean', 'PublicationSafety': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/publication-safety/formal/PublicationSafety.lean', 'PublicationBudget': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/publication-safety/formal/PublicationBudget.lean', 'PublicationBridge': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/publication-safety/formal/PublicationBridge.lean', 'RevisionPreparation': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/formal/RevisionPreparation.lean', 'FreshRevision': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/formal/FreshRevision.lean', 'RevisionWitness': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/formal/RevisionWitness.lean', 'PlasticityPreparation': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal/PlasticityPreparation.lean', 'PairedPlasticity': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal/PairedPlasticity.lean', 'PlasticityWitness': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal/PlasticityWitness.lean'}

def sha(b): return hashlib.sha256(b).hexdigest()
def command(argv,cwd,env=None):
    return subprocess.run(argv,cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=240)
def main():
    dev='--development' in __import__('sys').argv
    sources={n:REPO/p for n,p in PATHS.items() if not dev or (REPO/p).exists()}
    attempt=ROOT/'development'/str(time.time_ns())
    attempt.mkdir(parents=True)
    tool=(ROOT/'lean-toolchain').read_bytes()
    assert tool.decode().strip()=='leanprover/lean4:v4.29.1'
    frozen={n:p.read_bytes() for n,p in sources.items()}
    # Freeze all actual transitive source bytes before the first compiler call.
    for n,data in frozen.items(): (attempt/(n+'.lean')).write_bytes(data)
    checker=Path(__file__).read_bytes();(attempt/'check.py').write_bytes(checker)
    (attempt/'lean-toolchain').write_bytes(tool)
    protocol=ROOT.parent/'protocol-freeze.json'
    contract=protocol.read_bytes();(attempt/'protocol-freeze.json').write_bytes(contract)
    declared={}; requested={}
    for n,data in frozen.items():
        text=data.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b',text),n
        assert not re.search(r'^\s*(axiom|constant)\s',text,re.M),n
        assert set(re.findall(r'^import\s+(.+)$',text,re.M))<=({'Std'}|set(sources)),n
        declared[n]=set(re.findall(r'^theorem\s+(\w+)',text,re.M))
        requested[n]=set(re.findall(r'^#print axioms\s+([\w.]+)\s*$',text,re.M))
        short={v.rsplit('.',1)[-1] for v in requested[n]}
        assert (short<=declared[n] if n=='GenerativeCore' else short==declared[n]),n
    original=json.loads(contract)
    frozen_contract={p:(REPO/p).read_bytes() for p in original['source_sha256']}
    assert all(sha(frozen_contract[p])==d for p,d in original['source_sha256'].items())
    (attempt/'source-freeze.json').write_text(json.dumps({'sources':{n:sha(b) for n,b in frozen.items()},'contract':sha(contract)},indent=2)+'\n')
    pref=command(['lean','+leanprover/lean4:v4.29.1','--print-prefix'],ROOT);pref.check_returncode()
    compiler=Path(pref.stdout.strip())/'bin/lean'
    version=command([str(compiler),'--version'],ROOT);version.check_returncode()
    rows=[]
    with tempfile.TemporaryDirectory(prefix='plasticity-lean-') as temp:
        build=Path(temp)
        for n,b in frozen.items():(build/(n+'.lean')).write_bytes(b)
        env=dict(os.environ,LEAN_PATH=str(build))
        for n,p in sources.items():
            r=command([str(compiler),'-o',n+'.olean',n+'.lean'],build,env)
            log=attempt/(n+'.txt');log.write_text(r.stdout)
            audits=re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",r.stdout)
            ax=sorted({a.strip() for _,g in audits for a in g.split(',') if a.strip()})
            passed=r.returncode==0 and 'warning:' not in r.stdout and 'sorryAx' not in r.stdout and {x[0].rsplit('.',1)[-1] for x in audits}=={x.rsplit('.',1)[-1] for x in requested[n]} and len(audits)==len(requested[n]) and set(ax)<={'propext','Quot.sound','Classical.choice'}
            rows.append({'module':n,'source':str(p.relative_to(REPO)),'sha256':sha(frozen[n]),'new':n in NEW,'exit_code':r.returncode,'passed':passed,'declarations':[x[0] for x in audits],'axioms':ax,'log':str(log.relative_to(ROOT)),'log_sha256':sha(log.read_bytes())})
            if not passed:
                print(n+' FAILED\n'+r.stdout,flush=True);break
            print(n+' passed '+str(len(audits)),flush=True)
    unchanged=all(p.read_bytes()==frozen[n] for n,p in sources.items()) and protocol.read_bytes()==contract and all((REPO/p).read_bytes()==b for p,b in frozen_contract.items())
    passed=all(x['passed'] for x in rows) and len(rows)==len(sources) and unchanged
    receipt={'status':'passed' if passed else 'failed','development':dev,'source_unchanged':unchanged,'fresh_frozen_build':True,'toolchain':tool.decode().strip(),'toolchain_sha256':sha(tool),'compiler':str(compiler),'compiler_sha256':sha(compiler.read_bytes()),'version':version.stdout.strip(),'checker_sha256':sha(checker),'protocol_freeze_sha256':sha(contract),'source_freeze':str((attempt/'source-freeze.json').relative_to(ROOT)),'modules':rows,'new_audits':sum(len(x['declarations']) for x in rows if x['new']),'inherited_audits':sum(len(x['declarations']) for x in rows if not x['new'])}
    (attempt/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    if passed and not dev:(ROOT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('RECEIPT '+str(attempt/'receipt.json'),flush=True)
    raise SystemExit(0 if passed else 1)
if __name__=='__main__': main()
