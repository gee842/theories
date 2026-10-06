"""Supplemental producer regressions on preserved first-run states.

This is not the independently authored oracle. No main experiment is rerun.
"""
from pathlib import Path
from copy import deepcopy
import gzip
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('_evaluation_selfcheck',HERE/'model.py')
model=importlib.util.module_from_spec(spec);sys.modules[spec.name]=model;spec.loader.exec_module(model)


def main():
    model.verify_freeze()
    files=json.loads((HERE/'result-files.json').read_text())
    assert model.digest(HERE/files['file'])==files['compressed_sha256']
    raw=gzip.decompress((HERE/files['file']).read_bytes())
    import hashlib
    assert hashlib.sha256(raw).hexdigest()==files['uncompressed_sha256']
    data=json.loads(raw);catalog=data['parent_catalog'];counts=dict(conventional_paths=0,
        matched_training_paths=0,faithful_three_word_paths=0,no_fourth_native=0,
        no_reused_assessment=0,no_second_replacement=0,funded_reuse_obstructions=0)
    reached={};witnesses=[]
    for name,case in data['cases'].items():
        cfg=case['config'];reached[name]={}
        for prod in ('variable','conventional','fixed_normal'):
            shared=case['arms']['shared']['producers'][prod]['paths']
            conventional=case['arms']['conventional']['producers'][prod]['paths']
            gated=case['arms']['identity_gated']['producers'][prod]['paths']
            assert shared==conventional
            counts['conventional_paths']+=len(shared)
            commands=set();missing=0;inconsistent=0
            for a,b in zip(shared,gated):
                assert a['predecessor_ref']==b['predecessor_ref']
                def teaching(row):
                    return [x for x in row['runtime_trace'] if x['event'].startswith('native.') or
                            x['event']=='extension.at_actual_parent_prefix']
                assert teaching(a)==teaching(b)
                counts['matched_training_paths']+=1
                for step in a['runtime_trace']:
                    if step['event']!='native.write' or step['state']['native']['count']!=3:continue
                    if name.startswith('signals_'):
                        assert step['state']['native']['n']==sum((1<<i)*bit for i,bit in enumerate(cfg['native_signals']))
                        counts['faithful_three_word_paths']+=1
                s=a['state'];entry=catalog[a['predecessor_ref']]
                if s['outcomes']['native_complete']:
                    cmd=model.command(s,catalog)
                    if cmd is None:missing+=1
                    elif cmd!=model.parent.identification.read(s['core']['q'],'recipient'):inconsistent+=1
                    else:commands.add(cmd)
                    prior=deepcopy(s);scratch=[]
                    assert not model.native_lesson(s,cfg,catalog,scratch)
                    assert s==prior;counts['no_fourth_native']+=1
                    if s['port']['mode']=='consumed':
                        try:model.recipient_trial(s,cfg,catalog,a['observer']['actual_work_law'],2,[])
                        except AssertionError:pass
                        else:raise AssertionError('Consumed port admitted another trial')
                        assert s==prior;counts['no_reused_assessment']+=1
                        if s['core']['fuel']>=8 and s['core']['source']>=10 and s['core']['active']:
                            counts['funded_reuse_obstructions']+=1
                    if s['outcomes']['replaced']:
                        assert not model.replace_port(s,[])
                        assert s==prior;counts['no_second_replacement']+=1
                if name=='signals_111' and prod=='variable' and entry['observer']['strict_parent']:
                    assert s['core']['fuel']==0 and s['core']['recipient']==60
                    assert sum(s['native']['packets'])==6 and model.retained(s)==66
                    witnesses.append(dict(parent_ref=s['parent_ref'],command=model.command(s,catalog),
                        retained=66,recipient=60,n=s['native']['n'],new_spent=sum(s['new_spent'].values())))
            reached[name][prod]=dict(reached_supported_commands=sorted(commands),
                completed_native_without_supported_command=missing,
                completed_native_command_disagreements=inconsistent)
    assert reached['signals_111']['variable']['reached_supported_commands']==[0,1]
    assert {x['command'] for x in witnesses}=={0,1}
    assert counts['funded_reuse_obstructions']>0
    report=dict(status='passed',scope='Supplemental producer checks on exact preserved first outputs; independent oracle remains separate.',
        source_sha256={str((HERE/f).relative_to(model.REPO)):model.digest(HERE/f)
                       for f in ('model.py','check_producer.py','results.json.gz','result-files.json','first-run-receipt.json')},
        counts=counts,strict_reached_witnesses=witnesses,support_by_case_and_producer=reached)
    (HERE/'producer-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(counts,sort_keys=True))


if __name__=='__main__':main()
