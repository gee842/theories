"""Prespecified exact comparisons and paid prediction/action witnesses."""
from dataclasses import replace
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import model as m

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'AGENTS.md').exists())
SOURCES=[HERE/'model.py',HERE/'check.py',HERE/'PROTOCOL.md',HERE.parent/'model.py',
         HERE.parents[2]/'process.py',HERE.parents[3]/'model.py']


def hashes():
    return {str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in SOURCES}


def witness():
    law=m.Law()
    preparations,_=m.prepare(law)
    entrance=sum((Q(x['probability']) for x in preparations if x['commissioned']),Q(0))
    assert entrance==Q(2,9)
    assert {x['reserve'] for x in preparations if x['commissioned']}=={20}
    s=m.State(20)
    probability=Q(1,2)  # specified initial hidden orientation1
    steps=[]
    spent=waste=0
    for t in range(10):
        z=1 if t<6 else 0
        candidates=m.advance(law,s,'variable',z,t>=6)
        def selected(x):
            out,p,inc=x
            return out.gate==(0 if t<8 else 1) and (t!=0 or out.last==1)
        chosen=[x for x in candidates if selected(x)]
        assert len(chosen)==1,(t,chosen)
        out,p,inc=chosen[0]
        d=dict(zip(m.MOMENTS,inc))
        probability*=p;spent+=d['spent'];waste+=d['waste']
        steps.append({'exposure':t+1,'before_fuel':s.fuel,'after_fuel':out.fuel,
                      'q_before':s.q,'q_after':out.q,'gate_after':out.gate,
                      'action':out.last,'capture':d['captures'],
                      'paid_write':d['writes'],'strict_witness':out.witness})
        s=out
    assert s.fuel==18 and s.q==0 and s.witness
    assert probability==Q(1,16)
    # Includes actual old preparation/adapter and all legacy/retrofit bills.
    remaining=s.fuel+2*law.packet
    assert 145==4+1+spent+waste+remaining
    return {'path':steps,'conditional_commissioned_prefix_probability':str(probability),
            'unconditional_prefix_probability':str(entrance*probability),
            'remaining_source_packets':2,'remaining_energy':remaining,
            'preparation_spent':4,'adapter_spent':1,
            'all_operational_spent_and_waste':spent+waste}


def checks():
    # Controller equivalence for every finite register state and observation.
    for q in range(5):
        for last in range(2):
            assert m.command(q,last)==m.conventional_command(q,last)
        for gate in range(2):
            for label in range(2):
                assert m.learned(gate,q,label)==m.conventional_learned(gate,q,label)
    # Change only the register, with all physical balances and source fixed.
    s=m.State(10,gate=0,gate_life=2,stage=2,life=6,q=4,last=1,written=True)
    assert m.command(s.q,s.last)==1 and m.command(0,s.last)==0
    ordinary=m.advance(m.Law(),s,'fixed_slow',0,True)
    clamped=m.advance(m.Law(),replace(s,q=0),'fixed_slow',0,True)
    assert sum(p*d[m.MOMENTS.index('captures')] for _,p,d in ordinary)==0
    assert sum(p*d[m.MOMENTS.index('captures')] for _,p,d in clamped)==1
    # No return from an available but incompatible source versus a source outage.
    a=m.advance(m.Law(),replace(s,q=0,last=0),'fixed_slow',1,False)
    b=m.advance(replace(m.Law(),availability=Q(0)),replace(s,q=0,last=0),'fixed_slow',0,False)
    # Complete local physical/controller outcomes coincide; only analyst decoder-error differs.
    assert [(x,p) for x,p,_ in a]==[(x,p) for x,p,_ in b]
    ia=m.MOMENTS.index('decoder_errors')
    assert [d[:ia]+d[ia+1:] for _,_,d in a]==[d[:ia]+d[ia+1:] for _,_,d in b]
    assert a[0][2][ia]==0 and b[0][2][ia]==1
    # Same-last comparison prevents attributing hysteresis-only change to a write.
    assert m.issued('inverted_action',2,0)!=m.issued('inverted_action',2,1)
    # Corrective route funding: three failed paid Slow writes, one gate replacement,
    # then rent+work before the first changed action's return.
    boundary=[]
    for fuel in (20,21):
        st=m.State(fuel,gate=0,gate_life=2,stage=2,life=6,q=4,last=1,written=True,prelearn=True)
        path=[]
        for t in range(4):
            branches=m.advance(m.Law(),st,'fixed_slow',0,True)
            assert len(branches)==1
            st,p,d=branches[0];path.append(dict(zip(m.MOMENTS,d)))
        capture=sum(d['captures'] for d in path)
        assert capture==int(fuel==21)
        boundary.append({'fuel':fuel,'captures':capture,'final_fuel':st.fuel,
                         'final_q':st.q,'correction':st.witness})
    return {'finite_controller_tables':'passed','same_state_register_clamp':'passed',
            'outage_record_ambiguity':'passed','specified_slow_route_boundary':boundary,
            'complete_paid_witness':witness()}


def main():
    frozen=hashes()
    diagnostics=checks()
    results={}
    for name,law in m.cases().items():
        results[name]=m.compare(law)
        row=results[name]['arms']['variable']
        print(json.dumps({'case':name,'captures':row['metrics']['captures'],
                          'correction':row['metrics']['p_correction'],
                          'max_states':row['maximum_distribution_states']}),flush=True)
    assert hashes()==frozen
    record={'status':'passed','arithmetic':'exact rational forward moment-valued distribution',
            'source_sha256':frozen,'cases':results,'diagnostics':diagnostics,
            'case_arms':len(results)*len(m.ARMS),
            'scope':'finite synthetic law; probability/implementation separate from Lean; no empirical calibration'}
    (HERE/'results.json').write_text(json.dumps(record,indent=2)+'\n')
    print('passed; results.json saved',flush=True)


if __name__=='__main__':
    main()
