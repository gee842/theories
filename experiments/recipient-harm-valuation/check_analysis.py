#!/usr/bin/env python3
"""Independent reconstruction of the frozen recipient-harm archive contrast.

Uses only original CSV bytes and standard-library arithmetic; never imports or
executes the producer. Schema-specific comparison is defined separately below.
"""
from __future__ import annotations
import copy
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'sources/30-recipient-harm-valuation-2026-10-06/original'
LABELS = ('baseline', 'shock1', 'shock2', 'shock3')
CATEGORIES = {'preferred': 2, 'alternative': 1, 'nonperformed': 0, 'unknown': None}
RANGES = {
    'NoHarm': range(1, 15),
    'ContingentHarmMale': range(15, 27),
    'ContingentHarmFemale': range(27, 39),
    'RandomHarm': range(39, 47),
    'NonPreExposed': range(47, 61),
    '1vs2Pellets': range(61, 68),
    '1vs3Pellets': range(68, 79),
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def mean(values):
    values = [v for v in values if v is not None]
    return sum(values, Fraction()) / len(values) if values else None

def jsonify(value):
    if isinstance(value, Fraction):
        return float(value)
    if isinstance(value, dict):
        return {str(k): jsonify(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonify(v) for v in value]
    return value

def scope(row):
    counts = {name: row.count(code) for name, code in CATEGORIES.items()}
    counts['offered'] = len(row)
    counts['completed'] = counts['preferred'] + counts['alternative']
    assert sum(counts[k] for k in CATEGORIES) == len(row)
    return {
        'counts': counts,
        'rates': {name: Fraction(counts[name], len(row)) for name in CATEGORIES},
        'completed_rate': Fraction(counts['completed'], len(row)),
        'conditional': Fraction(counts['preferred'], counts['completed']) if counts['completed'] else None,
    }

def derive_actor(actor_id, metadata, trials):
    phases = {name: scope(trials[i * 20:(i + 1) * 20]) for i, name in enumerate(LABELS)}
    phases['shock_all'] = scope(trials[20:])
    changes = {}
    b = phases['baseline']
    for name in LABELS[1:] + ('shock_all',):
        p = phases[name]
        changes[name] = {
            'rates': {k: p['rates'][k] - b['rates'][k] for k in CATEGORIES},
            'completed_rate': p['completed_rate'] - b['completed_rate'],
            'conditional': p['conditional'] - b['conditional'] if p['conditional'] is not None and b['conditional'] is not None else None,
        }
    return {'actor_id': actor_id, 'metadata': metadata, 'trials': trials, 'phases': phases, 'changes': changes}

def group(actors):
    out = {'n': len(actors), 'actor_ids': [a['actor_id'] for a in actors], 'phases': {}, 'changes': {}}
    for phase in LABELS + ('shock_all',):
        scopes = [a['phases'][phase] for a in actors]
        out['phases'][phase] = {
            'total_counts': {k: sum(s['counts'][k] for s in scopes) for k in scopes[0]['counts']},
            'rates': {k: mean([s['rates'][k] for s in scopes]) for k in CATEGORIES},
            'completed_rate': mean([s['completed_rate'] for s in scopes]),
            'conditional': mean([s['conditional'] for s in scopes]),
            'conditional_n': sum(s['conditional'] is not None for s in scopes),
        }
    for phase in LABELS[1:] + ('shock_all',):
        scopes = [a['changes'][phase] for a in actors]
        out['changes'][phase] = {
            'rates': {k: mean([s['rates'][k] for s in scopes]) for k in CATEGORIES},
            'completed_rate': mean([s['completed_rate'] for s in scopes]),
            'conditional': mean([s['conditional'] for s in scopes]),
            'conditional_n': sum(s['conditional'] is not None for s in scopes),
        }
    return out

def contrast(first, second):
    return {
        phase: {
            'rates': {key: first['changes'][phase]['rates'][key] - second['changes'][phase]['rates'][key] for key in CATEGORIES},
            'completed_rate': first['changes'][phase]['completed_rate'] - second['changes'][phase]['completed_rate'],
            'conditional': first['changes'][phase]['conditional'] - second['changes'][phase]['conditional'] if first['changes'][phase]['conditional'] is not None and second['changes'][phase]['conditional'] is not None else None,
        } for phase in LABELS[1:] + ('shock_all',)
    }

def reconstruct():
    freeze = json.loads((HERE / 'protocol-freeze.json').read_text())
    assert digest(HERE / 'PROTOCOL.md') == freeze['protocol_sha256']
    for relative, expected in freeze['source_sha256'].items():
        assert digest(ROOT / relative) == expected, relative
    clarity = json.loads((HERE / 'schema-clarification-freeze.json').read_text())
    for relative, expected in clarity['files'].items():
        assert digest(HERE / relative) == expected, relative
    with (SOURCE / 'dataMainPaper.csv').open(newline='', encoding='utf-8-sig') as f:
        meta = {}
        for row in csv.DictReader(f):
            raw_id = row['Animal Number'].strip()
            if not raw_id:
                continue
            actor_id = int(raw_id)
            assert actor_id not in meta
            meta[actor_id] = row
    assert len(meta) == 142
    with (SOURCE / 'TrialByTrialChoicesMainPaper.csv').open(newline='', encoding='utf-8-sig') as f:
        rows = list(csv.reader(f))
    assert len(rows[0]) == 88
    for offset in (3, 23, 43, 63):
        assert rows[1][offset:offset + 20] == [f'Trial {n}' for n in range(1, 21)]
    animals = {}
    summary_checks = []
    supplied_nonperformance = []
    unknown_cells = []
    for row_index, row in enumerate(rows[2:], 3):
        if not any(cell.strip() for cell in row):
            continue
        actor_id = int(row[1])
        assert actor_id not in animals
        md = {key: meta[actor_id][key].strip() for key in ('SBL#', 'Rat Number', 'Animal Number', 'Condition', 'Group', 'Gender')}
        assert md['Condition'] == row[2].strip()
        assert md['Gender'] == ('Female' if 27 <= actor_id <= 38 else 'Male')
        trials = []
        for j, cell in enumerate(row[3:83]):
            if cell.strip() == '':
                value = None
                unknown_cells.append({'actor_id': actor_id, 'phase': LABELS[j // 20], 'trial': j % 20 + 1, 'csv_row': row_index, 'csv_column': j + 4})
            else:
                value = int(cell)
                assert value in (0, 1, 2)
            trials.append(value)
        assert len(trials) == 80
        actor = derive_actor(actor_id, md, trials)
        animals[actor_id] = actor
        for i, phase in enumerate(LABELS):
            supplied = int(row[83 + i]) if row[83 + i].strip() else None
            actual = actor['phases'][phase]['counts']['nonperformed']
            supplied_nonperformance.append({'actor_id': actor_id, 'phase': phase, 'supplied': supplied, 'derived': actual, 'matches': supplied == actual})
        supplied = int(row[87]) if row[87].strip() else None
        actual = trials.count(0)
        supplied_nonperformance.append({'actor_id': actor_id, 'phase': 'total', 'supplied': supplied, 'derived': actual, 'matches': supplied == actual})
        conditional = [actor['phases'][name]['conditional'] for name in LABELS]
        for field, value in zip(('Baseline', 'Shock 1', 'Shock 2', 'Shock 3'), conditional):
            raw = meta[actor_id][field].strip()
            archived = Fraction(raw) if raw and raw.lower() != 'nan' else None
            derived = 100 * value if value is not None else None
            difference = derived - archived if derived is not None and archived is not None else None
            summary_checks.append({'actor_id': actor_id, 'field': field, 'archived': archived, 'derived': derived, 'difference': difference, 'flagged': (derived is None) != (archived is None) or (difference is not None and abs(difference) > Fraction(11, 1000))})
        raw = meta[actor_id]['AverageShock'].strip()
        archived = Fraction(raw) if raw and raw.lower() != 'nan' else None
        daily = conditional[1:]
        derived = 100 * mean(daily) if all(v is not None for v in daily) else None
        difference = derived - archived if derived is not None and archived is not None else None
        summary_checks.append({'actor_id': actor_id, 'field': 'AverageShock', 'archived': archived, 'derived': derived, 'difference': difference, 'flagged': (derived is None) != (archived is None) or (difference is not None and abs(difference) > Fraction(11, 1000))})
    assert set(animals) == set(range(1, 79))
    assert [(c['actor_id'], c['phase'], c['trial']) for c in unknown_cells] == [(70, 'shock3', 11)]
    groups = {name: group([animals[i] for i in ids]) for name, ids in RANGES.items()}
    pairs = {
        'primary': ('ContingentHarmMale', 'NoHarm'),
        'prior_exposure': ('ContingentHarmMale', 'NonPreExposed'),
        'sex': ('ContingentHarmFemale', 'ContingentHarmMale'),
        'two_pellets': ('1vs2Pellets', 'ContingentHarmMale'),
        'three_pellets': ('1vs3Pellets', 'ContingentHarmMale'),
        'random_harm': ('ContingentHarmMale', 'RandomHarm'),
    }
    comparisons = {name: contrast(groups[a], groups[b]) for name, (a,b) in pairs.items()}
    primary_ids = list(range(1,27))
    leave_actor = {}
    for omitted in primary_ids:
        a = group([animals[i] for i in range(15,27) if i != omitted])
        b = group([animals[i] for i in range(1,15) if i != omitted])
        leave_actor[omitted] = {'n_first': a['n'], 'n_second': b['n'], 'difference': contrast(a,b)}
    leave_label = {}
    for label in sorted({animals[i]['metadata']['SBL#'] for i in primary_ids}):
        kept = lambda ids: [animals[i] for i in ids if animals[i]['metadata']['SBL#'] != label]
        a,b = group(kept(range(15,27))),group(kept(range(1,15)))
        leave_label[label] = {'n_first': a['n'], 'n_second': b['n'], 'omitted_ids': [i for i in primary_ids if animals[i]['metadata']['SBL#'] == label], 'difference': contrast(a,b)}
    completions = {}
    for code in (0,1,2):
        row = animals[70]['trials'].copy(); assert row[70] is None; row[70] = code
        modified = dict(animals); modified[70] = derive_actor(70, animals[70]['metadata'], row)
        g = group([modified[i] for i in range(68,79)])
        completions[code] = {'actor': modified[70], 'group': g, 'contrast': contrast(g,groups['ContingentHarmMale'])}
    return {
        'actors': animals, 'groups': groups, 'comparisons': comparisons,
        'leave_actor': leave_actor, 'leave_sbl_label': leave_label,
        'completions': completions, 'summary_checks': summary_checks,
        'supplied_nonperformance': supplied_nonperformance, 'unknown_cells': unknown_cells,
        'summary_only': [{k: row[k].strip() for k in ('Animal Number','Condition','Group','Gender','SBL#','Rat Number')} for i,row in meta.items() if i not in animals],
        'source_hashes': {p.name:digest(p) for p in SOURCE.iterdir() if p.is_file()},
        'protocol_sha256': digest(HERE/'PROTOCOL.md'),
        'clarification_sha256': digest(HERE/'SCHEMA-CLARIFICATION.md'),
    }

# Producer-schema comparison is appended after its public JSON schema is available.

GROUP_NAMES = dict(zip(RANGES, (
    'no_harm_male','contingent_harm_male','contingent_harm_female',
    'random_harm_male','not_pre_exposed_male','one_vs_two_pellets','one_vs_three_pellets')))
METRICS = ('preferred_offered','alternative_offered','nonresponse_offered','unknown_offered','preferred_completed')

def rational(value):
    return None if value is None else str(value)

def metrics(record):
    return dict(zip(METRICS, [rational(record['rates'][key]) for key in CATEGORIES] + [rational(record['conditional'])]))

def phase_record(record):
    counts = dict(record['counts'])
    counts['nonresponse'] = counts.pop('nonperformed')
    return counts | metrics(record)

def expected_schema(independent):
    animals = independent['actors']
    with (SOURCE/'dataMainPaper.csv').open(newline='',encoding='utf-8-sig') as f:
        raw_metadata = {int(r['Animal Number']):r for r in csv.DictReader(f) if r['Animal Number'].strip()}
    with (SOURCE/'TrialByTrialChoicesMainPaper.csv').open(newline='',encoding='utf-8-sig') as f:
        raw_trials = {int(r[1]):r for r in list(csv.reader(f))[2:] if any(c.strip() for c in r)}
    actors = []
    actor_to_group = {i: GROUP_NAMES[g] for g, ids in RANGES.items() for i in ids}
    for actor_id, a in animals.items():
        actors.append({
            'actor': actor_id, 'group': actor_to_group[actor_id], 'source_group': a['metadata']['Condition'],
            'metadata': {k:raw_metadata[actor_id][k] for k in a['metadata'] if k != 'Animal Number'},
            'codes': a['trials'],
            'phases': {p:phase_record(s) for p,s in a['phases'].items()},
            'changes': {p:metrics(s) for p,s in a['changes'].items()},
            'supplied_nonperformance': raw_trials[actor_id][83:88],
        })
    groups = {}
    for name, g in independent['groups'].items():
        def means_for(phase, changes=False):
            s = g['changes' if changes else 'phases'][phase]
            m = metrics(s)
            return {k:{'known':s['conditional_n'] if k=='preferred_completed' else g['n'],
                       'unknown':g['n']-s['conditional_n'] if k=='preferred_completed' else 0,
                       'exact':v} for k,v in m.items()}
        totals = {}
        for phase,s in g['phases'].items():
            totals[phase] = dict(s['total_counts'])
            totals[phase]['nonresponse'] = totals[phase].pop('nonperformed')
        groups[GROUP_NAMES[name]] = {
            'actors':g['actor_ids'], 'n':g['n'],
            'sbl_labels':dict(Counter(animals[i]['metadata']['SBL#'] for i in g['actor_ids'])),
            'totals':totals,
            'means':{phase:means_for(phase) for phase in g['phases']},
            'changes':{phase:means_for(phase,True) for phase in g['changes']},
        }
    def pair(left_ids, right_ids):
        left,right = group([animals[i] for i in left_ids]),group([animals[i] for i in right_ids])
        phase_diff = {}
        for p in LABELS + ('shock_all',):
            phase_diff[p] = {}
            l,r = metrics(left['phases'][p]), metrics(right['phases'][p])
            for k in METRICS:
                phase_diff[p][k] = rational(Fraction(l[k])-Fraction(r[k])) if l[k] is not None and r[k] is not None else None
        return {'left_actors':list(left_ids),'right_actors':list(right_ids),
                'phase_differences':phase_diff,
                'change_differences':{p:metrics(s) for p,s in contrast(left,right).items()}}
    contrasts = {}
    contrast_ids = {
        'primary_harm_minus_no_harm':(range(15,27),range(1,15)),
        'secondary_exposed_minus_not_exposed':(range(15,27),range(47,61)),
        'secondary_female_minus_male':(range(27,39),range(15,27)),
        'secondary_two_pellets_minus_one':(range(61,68),range(15,27)),
        'secondary_three_pellets_minus_one':(range(68,79),range(15,27)),
        'descriptive_random_minus_contingent':(range(39,47),range(15,27)),
    }
    for name,(left,right) in contrast_ids.items(): contrasts[name]=pair(left,right)
    leave_actor={str(i):pair([n for n in range(15,27) if n!=i],[n for n in range(1,15) if n!=i]) for i in range(1,27)}
    leave_label={s:pair([n for n in range(15,27) if animals[n]['metadata']['SBL#']!=s],[n for n in range(1,15) if animals[n]['metadata']['SBL#']!=s]) for s in independent['leave_sbl_label']}
    summaries={(r['actor_id'],r['field']):r for r in independent['summary_checks']}
    np_counts={(r['actor_id'],r['phase']):r for r in independent['supplied_nonperformance']}
    audit=[]
    for i in range(1,79):
        for f in ('Baseline','Shock 1','Shock 2','Shock 3','AverageShock'):
            x=summaries[(i,f)]
            audit.append({'actor':i,'field':f,'given':raw_metadata[i][f],
                          'computed':rational(x['derived']),
                          'absolute_difference':rational(abs(x['difference'])) if x['difference'] is not None else None,
                          'agree':not x['flagged']})
        for j,phase in enumerate(LABELS+('total',)):
            x=np_counts[(i,phase)]
            audit.append({'actor':i,'field':'nonperformance_'+phase,'given':raw_trials[i][83+j],
                          'computed':x['derived'],'agree':x['matches']})
    return {
        'schema_version':1,
        'protocol_sha256':independent['protocol_sha256'],
        'clarification_sha256':independent['clarification_sha256'],
        'source_sha256':json.loads((HERE/'protocol-freeze.json').read_text())['source_sha256'],
        'actors':actors,'groups':groups,'contrasts':contrasts,
        'primary_leave_one_actor_out':leave_actor,
        'primary_leave_one_sbl_label_out':leave_label,
        'actor70_unknown_completion_sensitivity':{str(k):{phase:phase_record(s) for phase,s in v['actor']['phases'].items()} for k,v in independent['completions'].items()},
        'source_summary_audit':{'comparisons':audit,'discrepancies':[x for x in audit if not x['agree']], 'tolerance_percentage_points':'11/1000'},
        'source_coverage':{
            'trial_actors':len(animals),'summary_actors':len(raw_metadata),'primary_actors':26,
            'offered_trial_slots':sum(len(a['trials']) for a in animals.values()),
            'unknown_trial_slots':sum(a['trials'].count(None) for a in animals.values()),
            'summary_only_actor_ids':sorted(set(raw_metadata)-set(animals)),
            'summary_only_conditions':dict(Counter(raw_metadata[i]['Condition'].strip() for i in set(raw_metadata)-set(animals))),
        },
        'new_animal_experiments':0,
    }

def compare(actual, expected, path='results'):
    """Strict nested equality; root permits only the named documentary extras."""
    checked=0
    if isinstance(expected,dict):
        assert isinstance(actual,dict),(path,'not object')
        extras={'status','analysis_sha256','interpretation'} if path=='results' else set()
        assert set(actual)-extras == set(expected),(path,'key mismatch',set(actual)-extras,set(expected))
        for key in expected: checked+=compare(actual[key],expected[key],f'{path}.{key}')
    elif isinstance(expected,list):
        assert isinstance(actual,list) and len(actual)==len(expected),(path,'list length')
        for i,(a,e) in enumerate(zip(actual,expected)): checked+=compare(a,e,f'{path}[{i}]')
    else:
        assert type(actual) is type(expected) and actual==expected,(path,actual,expected)
        checked=1
    return checked

def fault_tests(actual, expected):
    cases=[]
    def one(name,mutation):
        damaged=copy.deepcopy(actual); mutation(damaged)
        try: compare(damaged,expected)
        except AssertionError as error: cases.append({'name':name,'rejected':True,'at':str(error)[:220]})
        else: raise AssertionError(('fault escaped',name))
    one('omitted_actor',lambda x:x['actors'].pop())
    one('inverted_source_lever_code',lambda x:x['actors'][0]['codes'].__setitem__(0,1))
    one('wrong_baseline',lambda x:x['actors'][0]['phases']['baseline'].__setitem__('preferred_offered','1/2'))
    one('wrong_group_denominator',lambda x:x['groups']['contingent_harm_male'].__setitem__('n',24))
    one('unknown_replaced_by_nonresponse',lambda x:x['actors'][69]['codes'].__setitem__(70,0))
    one('zero_response_as_harmless_choice',lambda x:x['actors'][36]['phases']['shock3'].__setitem__('alternative',20))
    one('pseudoreplicated_animal_count',lambda x:x['groups']['contingent_harm_male']['means']['shock_all']['preferred_offered'].__setitem__('known',720))
    one('pooled_sexes_primary',lambda x:x['contrasts']['primary_harm_minus_no_harm']['left_actors'].append(27))
    one('wrong_contrast_sign',lambda x:x['contrasts']['primary_harm_minus_no_harm']['change_differences']['shock_all'].__setitem__('preferred_offered','841/5040'))
    one('missing_influence_case',lambda x:x['primary_leave_one_sbl_label_out'].pop('SBL049'))
    one('hidden_source_percentage_mismatch',lambda x:x['source_summary_audit']['discrepancies'].pop())
    one('wrong_source_digest',lambda x:x.__setitem__('protocol_sha256','0'*64))
    return cases

def main():
    independent=reconstruct()
    expected=expected_schema(independent)
    (HERE/'independent-reconstruction.json').write_text(json.dumps(expected,indent=2,allow_nan=False)+'\n')
    (HERE/'independent-detail.json').write_text(json.dumps(jsonify(independent),indent=2,allow_nan=False)+'\n')
    actual=json.loads((HERE/'results.json').read_text())
    assert actual['analysis_sha256']==digest(HERE/'analysis.py')
    checks=compare(actual,expected)
    faults=fault_tests(actual,expected)
    from datetime import datetime,timezone
    receipt={
        'status':'passed','time_utc':datetime.now(timezone.utc).isoformat(),
        'checker_sha256':digest(Path(__file__)), 'producer_results_sha256':digest(HERE/'results.json'),
        'independent_reconstruction_sha256':digest(HERE/'independent-reconstruction.json'),
        'independent_detail_sha256':digest(HERE/'independent-detail.json'),
        'protocol_sha256':independent['protocol_sha256'],'clarification_sha256':independent['clarification_sha256'],
        'comparison_count':checks,'actors':78,'raw_trial_slots':6240,'groups':7,'contrasts':6,
        'leave_one_actor':26,'leave_one_sbl_label':4,'hypothetical_completions':3,
        'source_audit_comparisons':len(expected['source_summary_audit']['comparisons']),
        'source_audit_flags':len(expected['source_summary_audit']['discrepancies']),
        'source_audit_flag_kinds':{'missing_total_nonperformance_fields':32,'undefined_session_aggregation':1,'percentage_denominator_difference':6},
        'fault_checks':faults,'producer_imported':False,
        'scope':'Independent original-CSV reconstruction; descriptive archived-cohort statistics only. Does not establish random assignment, cage independence, latent motives, or normative validity.',
    }
    (HERE/'independent-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','comparison_count','actors','raw_trial_slots','source_audit_flags']}))

if __name__=='__main__': main()
