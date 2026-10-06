#!/usr/bin/env python3
"""Independent prospective evaluative-plasticity interpreter.

Authored from DRAFT-PROTOCOL.md/cases.json and accepted ancestor laws without
reading the new plasticity producer.  No producer transitions are imported.
All new transitions, source accounts, preparation reactions and RI steps below
are independently expressed.  Old saved histories supply archival inputs;
their previous scientific validation is inherited, not rerun or relabelled.

No schedules execute on import.  The initial oracle must be hash-frozen before
execution.  Producer-schema adapters, when needed, are a separate later layer.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import argparse
import datetime
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
REVISION = HERE.parent.parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
BASE_FIELDS = ('core_phase', 'core_target', 'core_action', 'acquired_record')
BILL_NAMES = ('own_operation', 'recipient_operation', 'own_read', 'recipient_read',
              'coupling', 'native_write', 'evaluation_read', 'assessment', 'service')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def object_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load_json(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def pview(parent):
    return parent['parent']['parent']['producer']


def wview(parent):
    return parent['parent']['parent']


def cview(parent):
    return pview(parent)['core']


def parent_retained(s):
    """Resolve all old physical accounts; no producer accounting offset."""
    p, w, a = pview(s), wview(s), s['parent']
    return (sum(p['core'][k] for k in ('fuel', 'recipient', 'source', 'escrow'))
            + sum(p[k] for k in ('archive_fuel', 'reader_fuel', 'idle_fuel',
                                 'archive_escrow', 'packet_inflight'))
            + w['extra_reserve'] + w['external_idle']
            + sum(a[k] for k in ('command_reserve', 'later_reserve', 'source_reserve', 'saved_assembly'))
            + sum(s[k] for k in ('actor_reserve', 'writer_fuel', 'writer_escrow',
                                 'reader_reserve', 'source_reserve', 'idle_fuel',
                                 'idle_source', 'saved_assembly')))


def selected_context(parent):
    return parent['fresh']['epoch'] if parent['selected_bank'] == 'fresh' else pview(parent)['context']


def cache_current(parent):
    p = pview(parent)
    return bool(p['cache_valid'] and p['read_count'] == 3
                and p['cache_context'] == selected_context(parent))


def fresh_current(parent):
    w = wview(parent)
    pub = w['publication']
    return bool(parent['opened'] and parent['selected_bank'] == 'fresh'
                and parent['current_new_reason'] and cache_current(parent)
                and w['publication_current'] and w['phase'] == 'published'
                and pub and pub['context'] == selected_context(parent))


def known_command(parent):
    if not cache_current(parent):
        return None
    w = wview(parent)
    pub = w['publication']
    if not (w['publication_current'] and w['phase'] == 'published' and pub
            and pub['context'] == selected_context(parent)):
        return None
    return {(True, True, False): 0, (True, False, True): 1}.get(tuple(pub['mask']))


def factual_applicable(parent):
    command = known_command(parent)
    return bool(fresh_current(parent) and parent['parent']['scope'] and command is not None
                and command == ((cview(parent)['q'] >> 1) & 1))


def extract_parent(row):
    """First old read's predecessor, otherwise last non-final saved prefix."""
    tr = row['runtime_trace']
    for i, item in enumerate(tr):
        if item['event'] in ('paid_command_read', 'command_read_unavailable'):
            assert i > 0
            return i - 1, deepcopy(tr[i-1]['state'])
    remaining = [(i, item['state']) for i, item in enumerate(tr)
                 if item['event'] != 'continuation_complete']
    assert remaining
    i, parent = remaining[-1]
    return i, deepcopy(parent)


def read_ancestry(specs):
    manifest = load_json(REVISION / 'result-files.json')
    compressed = (REVISION / manifest['file']).read_bytes()
    assert hashlib.sha256(compressed).hexdigest() == manifest['compressed_sha256']
    raw = gzip.decompress(compressed)
    assert hashlib.sha256(raw).hexdigest() == manifest['uncompressed_sha256']
    old = json.loads(raw)
    catalog = {}
    names = sorted({c['config']['parent_revision_case'] for c in specs['cases']})
    for case in names:
        for producer in specs['parent_producers']:
            rows = old['cases'][case]['producers'][producer]['paths']
            assert sum(Fraction(row['probability']) for row in rows) == 1
            for i, row in enumerate(rows):
                j, state = extract_parent(row)
                ref = f'{case}/{producer}/{i}/{j}'
                catalog[ref] = dict(parent_case=case, producer=producer, path_index=i,
                    prefix_index=j, probability=row['probability'],
                    prefix_event=row['runtime_trace'][j]['event'], state=state,
                    state_sha256=object_digest(state), observer=deepcopy(row['observer']),
                    parent_predecessor=deepcopy(row['predecessor']))
    return catalog, old


def reaction(state, event, material=68):
    """Direct reconstruction of the relevant frozen FormedSelection channels."""
    a, h, resident, intact, local, fuel, source = state
    precursor = material-a-h-int(resident != 0)
    if event in ('form_a', 'form_h'):
        assert not intact and precursor > 0 and fuel > 0
        a += event == 'form_a'
        h += event == 'form_h'
        fuel -= 1
    elif event in ('bind_a', 'bind_h'):
        assert resident == 0 and fuel > 0
        if event == 'bind_a':
            assert a > 0
            a -= 1
            resident = 1
        else:
            assert h > 0
            h -= 1
            resident = 2
        fuel -= 1
    elif event == 'repair':
        assert resident == 1 and not intact and fuel > 0
        intact = 1
        fuel -= 1
    elif event == 'capture':
        assert intact and not local and source > 0
        source -= 1
        local = 1
    elif event in ('copy_a', 'copy_h'):
        assert local and precursor > 0 and resident == (1 if event == 'copy_a' else 2)
        local = 0
        a += event == 'copy_a'
        h += event == 'copy_h'
    else:
        raise AssertionError(('unhandled formation event', event))
    out = tuple(map(int, (a, h, resident, intact, local, fuel, source)))
    assert min(out) >= 0 and a+h+int(resident != 0) <= material
    return out


def preparation(config, old):
    """Literal controlled M68 lift, including every assembly and old adapter."""
    state = (0, 0, 0, 0, 0, 297, 208)
    spent = 0
    trace = [dict(event='initial', plant=list(state), spent=spent)]
    def advance(event):
        nonlocal state, spent
        nxt = reaction(state, event)
        spent += sum(state[4:])-sum(nxt[4:])
        state = nxt
        assert sum(state[4:])+spent == 505
        trace.append(dict(event=event, plant=list(state), spent=spent))
    for e in ['form_a']*13 + ['form_h']*13:
        advance(e)
    old_rows = [r for r in old['trace'][1:] if 'plant' in r and r['event'] in
                ('form_a', 'form_h', 'bind_a', 'bind_h', 'repair', 'capture', 'copy_a', 'copy_h')]
    for row in old_rows:
        advance(row['event'])
        a,h,r,c,l,f,e = row['plant']
        assert state == (a+13,h+13,r,c,l,f+44,e+24)
    assert state == (33,34,1,1,1,240,194)
    a,h,r,c,l,f,e = state
    assembled = config['memory_cells']+int(config['adapter'])+int(config['initial_port'])
    assert 0 <= assembled <= 10
    for stage, count in (('new_assembly', assembled), ('old_assembly', 20)):
        for i in range(count):
            assert min(a,h,f) > 0
            a-=1; h-=1; f-=1; spent+=1
            trace.append(dict(event=stage, index=i, plant=[a,h,r,c,l,f,e], spent=spent))
    assert r == 1 and h > 0 and f > 0 and l == 1
    h-=1; r=0; f=f-1+l; l=0; spent+=1
    omitted = 10-assembled
    assert (a,h,f,e,spent) == (3+omitted,3+omitted,210+omitted,194,101-omitted)
    assert f-34-omitted == old['trace'][-1]['fuel']
    assert e-24 == old['trace'][-1]['source']
    assert 42+2*assembled+a+h == 68 and f+e+spent == 505
    trace.append(dict(event='adapter_and_projection', free_a=a, free_h=h, fuel=f,
                      source=e, spent=spent, parent_fuel=f-34-omitted, parent_source=e-24))
    return dict(trace=trace, construction_spent=spent, extra_construction_spent=36-omitted,
                omitted_pairs=omitted, saved_assembly=omitted,
                parent_preparation_sha256=object_digest(old))


def total_retained(s):
    stock = s['stocks']
    return (parent_retained(s['parent']) + stock['primary'] + stock['revision']
            + sum(stock['own_packets']) + sum(stock['recipient_packets'])
            + stock['idle_common'] + stock['idle_source'] + stock['saved_assembly'])


def initialize(ref, config, variant, prep, catalog):
    parent = deepcopy(catalog[ref]['state'])
    before = parent_retained(parent)
    assert 0 <= config['primary_reserve'] <= 22 and 0 <= config['revision_reserve'] <= 12
    assert len(config['own_packets']) == len(config['recipient_packets']) == 6
    return dict(parent_ref=ref, parent=parent, n=0, count=0, phase='ready',
        own_return=None, recipient_return=None, own_bit=None, recipient_bit=None,
        links=[None,None], retired=[], primary_free=[True,True], replacement_free=True,
        inventory=dict(memory_cells=config['memory_cells'], adapter=config['adapter'],
            primary_access=list(config['primary_link_accessible']),
            replacement_access=config['replacement_accessible'], omitted_pairs=prep['omitted_pairs']),
        stocks=dict(primary=config['primary_reserve'], revision=config['revision_reserve'],
            own_packets=list(config['own_packets']), recipient_packets=list(config['recipient_packets']),
            idle_common=34-config['primary_reserve']-config['revision_reserve'],
            idle_source=24-sum(config['own_packets'])-sum(config['recipient_packets']),
            saved_assembly=prep['saved_assembly']),
        port=dict(built=config['initial_port'], mode='idle', command=None,
            transmission=None, assessment=None), spent=dict.fromkeys(BILL_NAMES,0), waste=0,
        outcomes=dict(admitted=False, training_complete=False, revised=False, attempted=False,
            completed=False, captured=False, scope_lost=False),
        account=dict(parent_spent=411-before, extra_construction=prep['extra_construction_spent'],
                     initial_retained=before+58+prep['saved_assembly']))


def validate(s):
    c, p, i, b = cview(s['parent']), s['port'], s['inventory'], s['stocks']
    assert 0 <= s['n'] <= 7 and 0 <= s['count'] <= 6
    assert min(*(c[k] for k in ('fuel','recipient','source','escrow')),
               b['primary'],b['revision'],b['idle_common'],b['idle_source'],b['saved_assembly'],
               *b['own_packets'],*b['recipient_packets'],*s['spent'].values(),s['waste']) >= 0
    assert len(s['links']) == 2
    held = [link for link in s['links'] if link is not None]+s['retired']
    assert len({x['id'] for x in held}) == len(held)
    assert all(x['sign'] in (-1,0,1) for x in held)
    assert len(held)+sum(s['primary_free'])+int(s['replacement_free']) == 3
    assert 42+2*(i['memory_cells']+int(i['adapter'])+int(p['built'])+i['omitted_pairs']+3) == 68
    assert total_retained(s)+sum(s['spent'].values())+s['waste'] == s['account']['initial_retained']
    assert (s['account']['parent_spent']+s['account']['extra_construction']+total_retained(s)
            +sum(s['spent'].values())+s['waste']) == 505


def admitted(s):
    parent=s['parent'];i=s['inventory']
    return bool(i['memory_cells']==8 and i['adapter'] and cview(parent)['active']
                and pview(parent)['core_phase']=='ready' and parent['parent']['scope']
                and fresh_current(parent))


def transmission(s, filtered=False, table=False):
    signs=tuple(0 if item is None else item['sign'] for item in s['links'])
    if filtered:
        return 0
    if table:
        # Independently enumerated signed port outputs; no hidden outcome input.
        multiplier={(-1,-1):-2,(-1,0):-1,(-1,1):0,(0,-1):-1,(0,0):0,
                    (0,1):1,(1,-1):0,(1,0):1,(1,1):2}[signs]
        return s['n']*multiplier
    return sum(s['n']*sign for sign in signs)


def run_oracle(ref, config, variant, prep, catalog):
    """Execute only when explicitly called after protocol/source freeze."""
    s=initialize(ref,config,variant,prep,catalog)
    trace=[]
    def emit(event):
        validate(s)
        trace.append(dict(event=event,state=deepcopy(s)))
    def pay(amount, bill):
        c=cview(s['parent'])
        if c['fuel'] < amount:
            return False
        c['fuel']-=amount;s['spent'][bill]+=amount
        return True
    def pair():
        k=s['count'];b=s['stocks'];c=cview(s['parent'])
        bank='primary' if k<4 else 'revision'
        cap=6 if k<4 else (7 if k==4 else 5)
        release=min(cap,b[bank])
        if not (s['phase']=='ready' and k<len(config['own_shortfalls']) and admitted(s)
                and b['own_packets'][k]>=2 and b['recipient_packets'][k]>=2
                and c['recipient']>=2 and c['fuel']+release>=2):
            emit('pair.start_blocked');return False
        b[bank]-=release;c['fuel']+=release-2;s['spent']['own_operation']+=2
        s['phase']='own_paid';emit('pair.own_pay')
        # These two return events alone read exogenous outcome schedules.
        returned=config['own_shortfalls'][k]==0
        if returned:
            b['own_packets'][k]-=2;c['fuel']+=2
        s['own_return']=returned;s['phase']='own_returned';emit('pair.own_return')
        assert c['recipient']>=2
        c['recipient']-=2;s['spent']['recipient_operation']+=2
        s['phase']='recipient_paid';emit('pair.recipient_pay')
        returned=config['recipient_shortfalls'][k]==0
        if returned:
            b['recipient_packets'][k]-=2;c['recipient']+=2
        s['recipient_return']=returned;s['phase']='recipient_returned';emit('pair.recipient_return')
        for kind in ('own','recipient'):
            if not pay(1,kind+'_read'):
                emit('pair.'+kind+'_read_blocked');return False
            mode=config[kind+'_meter'][k]
            assert mode in ('faithful','missing','inverted')
            bit=None if mode=='missing' else int(not s[kind+'_return']) ^ int(mode=='inverted')
            s[kind+'_bit']=bit;s['phase']=kind+'_read'
            emit('pair.'+kind+'_read')
        if s['own_bit'] is None or s['recipient_bit'] is None:
            emit('pair.acquisition_missing');return False
        if s['recipient_bit']==0:
            s['phase']='settled';emit('pair.no_contact')
        else:
            free=next((j for j,link in enumerate(s['links']) if link is None),None)
            learned=1 if s['own_bit'] else -1
            if free is not None:
                if not (s['primary_free'][free] and s['inventory']['primary_access'][free]
                        and c['fuel']>=1):
                    emit('pair.bind_blocked');return False
                pay(1,'coupling');s['primary_free'][free]=False
                sign=0 if variant['link_recipe']=='inert' else learned
                s['links'][free]=dict(id=free,sign=sign)
                s['phase']='settled';emit('pair.bind')
            else:
                if not (config['revision'] and k>=4 and s['replacement_free']
                        and s['inventory']['replacement_access'] and c['fuel']>=2):
                    emit('pair.replace_blocked');return False
                oldest=min(range(2),key=lambda j:s['links'][j]['id'])
                retired=deepcopy(s['links'][oldest])
                sign=retired['sign'] if variant['replacement_rule']=='retired_sign' else learned
                if variant['link_recipe']=='inert':sign=0
                pay(2,'coupling');s['retired'].append(retired);s['replacement_free']=False
                s['links'][oldest]=dict(id=2,sign=sign)
                s['outcomes']['revised']=True;s['phase']='settled';emit('pair.replace')
        if not pay(1,'native_write'):
            emit('pair.write_blocked');return False
        if config['native_updates']:
            s['n']=s['n']//2+4*s['own_bit']
        s['count']+=1;s['phase']='ready'
        for key in ('own_return','recipient_return','own_bit','recipient_bit'):s[key]=None
        emit('pair.write')
        return True
    def action():
        c=cview(s['parent']);p=pview(s['parent']);binding=s['parent']['parent']
        s['outcomes']['attempted']=True
        if not (all(binding[k] for k in ('scope','permission','delivery'))
                and factual_applicable(s['parent']) and p['core_phase']=='ready'):
            s['port']['mode']='consumed';emit('action.guard_blocked');return
        s['port']['mode']='executing';emit('action.initiate')
        if c['source']<10:
            s['port']['mode']='consumed';emit('action.source_blocked');return
        if not c['active'] or c['fuel']<8:
            c['source']-=10;c['active']=False;s['waste']+=10
            s['port']['mode']='consumed';emit('action.miss');return
        c['fuel']-=1;s['spent']['service']+=1;p['core_phase']='rented';emit('action.rent')
        c['fuel']-=1;s['spent']['service']+=1
        p['core_phase']='sensed';p['core_target']='recipient';emit('action.sense')
        assert c['fuel']>=6 and c['escrow']==0
        c['fuel']-=3;c['escrow']=3;p['core_phase']='reserved';emit('action.reserve')
        issued=(c['q']>>1)&1
        # World-only final law reaches physical work, never assessment.
        captured=issued==catalog[ref]['observer']['final_law']
        c['fuel']-=3;c['source']-=10;s['spent']['service']+=3
        p['core_phase']='worked';p['core_action']=issued
        if captured:c['recipient']+=10
        else:s['waste']+=10
        s['outcomes']['captured']=bool(captured);emit('action.work')
        c['escrow']-=1;s['spent']['service']+=1
        p['core_phase']='acquired';p['acquired_record']=bool(captured);emit('action.acquire')
        if not c['last']:
            if captured:c['last']=1
            else:c['q']=(c['q']&1)+2*(1-issued)
        c['escrow']-=2;s['spent']['service']+=2
        p.update(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
        s['port']['mode']='consumed';s['outcomes']['completed']=True;emit('action.write')
    def assess():
        p=s['port'];c=cview(s['parent'])
        if not (s['count']==len(config['own_shortfalls']) and s['phase']=='ready'
                and s['inventory']['memory_cells']==8 and p['built'] and p['mode']=='idle'
                and pview(s['parent'])['core_phase']=='ready' and c['fuel']>=1):
            emit('evaluation.read_blocked');return
        pay(1,'evaluation_read')
        valid=factual_applicable(s['parent'])
        p['command']=known_command(s['parent']) if valid else None
        p['mode']='read' if valid else 'consumed';emit('evaluation.read')
        if not (p['mode']=='read' and factual_applicable(s['parent'])
                and p['command']==known_command(s['parent']) and c['fuel']>=1):
            emit('evaluation.assessment_blocked');return
        pay(1,'assessment')
        value=transmission(s,variant['recipient_filter'],
                           variant['assessment_implementation']=='finite_table')
        p['transmission']=value;p['assessment']=10*value>64
        p['mode']='assessed_help' if p['assessment'] else 'assessed_abstain'
        emit('evaluation.assess')
        if p['assessment']:action()
        else:p['mode']='consumed';emit('action.abstain')
    emit('entry')
    s['outcomes']['admitted']=admitted(s)
    if not s['outcomes']['admitted']:
        emit('admission.blocked')
    else:
        while s['count']<len(config['own_shortfalls']):
            if not pair():break
        if s['count']==len(config['own_shortfalls']):
            s['outcomes']['training_complete']=True
            if config['scope_loss_before_read']:
                s['parent']['parent']['scope']=False;s['outcomes']['scope_lost']=True
                if s['port']['mode'] in ('read','assessed_help','assessed_abstain'):
                    s['port']['mode']='consumed';s['port']['command']=None
                emit('binding.scope_loss')
            assess()
    emit('complete')
    return dict(state=s,trace=trace,metrics=metrics(s))


def metrics(s):
    c=cview(s['parent']);p=s['port'];o=s['outcomes']
    signs=[0 if x is None else x['sign'] for x in s['links']]
    out=dict(final_actor=c['fuel'],final_recipient=c['recipient'],final_source=c['source'],
        retained=total_retained(s),new_spent=sum(s['spent'].values()),new_waste=s['waste'],
        n=s['n'],pairs=s['count'],link_sum=sum(signs),positive_links=signs.count(1),
        negative_links=signs.count(-1),occupied_links=sum(x is not None for x in s['links']),
        retired_links=len(s['retired']),native_complete=int(o['training_complete']),
        admitted=int(o['admitted']),replaced=int(o['revised']),
        assessment_available=int(p['assessment'] is not None),
        positive_assessment=int(p['assessment'] is True),attempted=int(o['attempted']),
        completed=int(o['completed']),captured=int(o['captured']))
    out.update({'spent_'+k:v for k,v in s['spent'].items()})
    return out


def freeze_record():
    """Metadata only: does not load histories, construct plants or run schedules."""
    paths=[Path(__file__),HERE/'DRAFT-PROTOCOL.md',HERE/'cases.json',
           REVISION/'model.py',REVISION/'check_model.py',REVISION/'result-files.json',
           HERE.parent/'model.py',HERE.parent/'check_model.py']
    process=REPO/'_process/research/2026-10-05-generative-foundation-review/root-foundation'
    paths += [process/'EVALUATIVE-PLASTICITY-SCOPE.md',process/'EVALUATIVE-PLASTICITY-ORACLE-CONTRACT.md']
    return dict(status='independent_transition_oracle_authored_not_executed',
        timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        new_producer_inspected=False,new_producer_imports=[],
        schedule_executed=False,ancestral_law_reference='accepted revision/evaluation source; no runtime import',
        source_sha256={str(p.relative_to(REPO)):digest(p) for p in paths})


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--freeze-only',action='store_true')
    args=parser.parse_args()
    if args.freeze_only:
        target=HERE/'oracle-preexecution.json'
        assert not target.exists(), 'preserve prior freeze before replacing'
        target.write_text(json.dumps(freeze_record(),sort_keys=True,indent=2)+'\n')
        print(json.dumps({'status':'source_frozen_without_execution','sha256':digest(Path(__file__))}))
    else:
        parser.error('No schedule CLI before root freeze; this prospective module only defines the oracle.')


if __name__=='__main__':main()
