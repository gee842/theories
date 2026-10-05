"""Descriptive, prespecified scoring; no independent-trial inference."""
from pathlib import Path
import json
from collections import defaultdict

ROOT = Path(__file__).resolve().parent

def analyze(key, batches):
    lookup = {c['id']: c for c in key['cases']}
    assert len(lookup) == 12
    eligible = {c['id'] for c in key['cases'] if c.get('primary_scope_eligible', False)}
    assert len(eligible) == 4, eligible
    families = {c['family'] for c in key['cases']}
    assert len(families) == 6
    for family in families:
        members = [c for c in key['cases'] if c['family'] == family]
        assert len(members) == 2
        assert {c['initial_claim_should_change'] for c in members} == {True, False}
    rows=[]
    summaries=[]
    for batch in batches:
        answers=batch['response']['answers']
        ids=[a.get('id') for a in answers if isinstance(a,dict)]
        duplicate_ids={i for i in ids if ids.count(i)>1}
        unknown_ids=[i for i in ids if i not in lookup]
        by_id={a['id']:a for a in answers if isinstance(a,dict) and a.get('id') in lookup and a.get('id') not in duplicate_ids}
        current=[]
        for identifier, k in lookup.items():
            a=by_id.get(identifier,{})
            choice=a.get('choice')
            correct=choice == k['gold']
            confidence=a.get('confidence')
            confidence_valid=isinstance(confidence,int) and not isinstance(confidence,bool) and 0 <= confidence <= 100
            reason=a.get('reason',None)
            reason_valid=isinstance(reason,str) and bool(reason.strip())
            word_count=len(reason.split()) if isinstance(reason,str) else None
            row={'batch':batch['batch'],'condition':batch['condition'],
                 'replicate':batch['replicate'],'id':identifier,'family':k['family'],
                 'requires_revision':k['initial_claim_should_change'],
                 'choice':choice,'gold':k['gold'],'correct':correct,
                 'scope_eligible':identifier in eligible,
                 'scope_overclaim':choice in k.get('scope_overclaim_options',[]) if identifier in eligible else None,
                 'false_scope_rejection':choice in k.get('false_rejection_options',[]) if identifier in eligible else None,
                 'missing_or_invalid_choice':choice not in ('A','B','C','D'),
                 'confidence':confidence,'confidence_valid':confidence_valid,
                 'binary_correctness_brier':((confidence/100)-int(correct))**2 if confidence_valid else None,
                 'reason_words':word_count,'reason_valid':reason_valid,'word_cap_compliant':reason_valid and word_count is not None and word_count <= 30,
                 'reason':reason}
            current.append(row)
        pairs={f:all(r['correct'] for r in current if r['family']==f) for f in families}
        summary={'batch':batch['batch'],'condition':batch['condition'],'replicate':batch['replicate'],
                 'correct':sum(r['correct'] for r in current),'total':12,
                 'scope_overclaims':sum(bool(r['scope_overclaim']) for r in current),
                 'scope_denominator':4,
                 'valid_scope_denominator':sum(r['scope_eligible'] and not r['missing_or_invalid_choice'] for r in current),
                 'missing_scope_choices':sum(r['scope_eligible'] and r['missing_or_invalid_choice'] for r in current),
                 'scope_error_or_missing':sum(r['scope_eligible'] and (bool(r['scope_overclaim']) or r['missing_or_invalid_choice']) for r in current),
                 'false_scope_rejections':sum(bool(r['false_scope_rejection']) for r in current),
                 'correct_pairs':sum(pairs.values()),'pairs_total':6,
                 'revision_correct':sum(r['correct'] for r in current if r['requires_revision']),
                 'revision_total':6,
                 'retention_correct':sum(r['correct'] for r in current if not r['requires_revision']),
                 'retention_total':6,
                 'missing_or_invalid_choices':sum(r['missing_or_invalid_choice'] for r in current),
                 'word_cap_violations':sum(not r['word_cap_compliant'] for r in current),
                 'duplicate_ids':sorted(str(i) for i in duplicate_ids),'unknown_ids':unknown_ids,
                 'mean_binary_correctness_brier':sum(r['binary_correctness_brier'] for r in current)/12 if all(r['confidence_valid'] for r in current) else None,
                 'pairs':pairs}
        rows.extend(current);summaries.append(summary)
    aggregate=[]
    for condition in ('ordinary','reflection','discipline'):
        ss=[s for s in summaries if s['condition']==condition]
        if not ss: continue
        result={'condition':condition,'batches':len(ss)}
        for field in ('correct','total','scope_overclaims','scope_denominator','valid_scope_denominator','missing_scope_choices','scope_error_or_missing','false_scope_rejections','correct_pairs','pairs_total','revision_correct','revision_total','retention_correct','retention_total','missing_or_invalid_choices','word_cap_violations'):
            result[field]=sum(s[field] for s in ss)
        aggregate.append(result)
    return {'status':'descriptive exploratory pilot, not general efficacy evidence',
            'aggregate':aggregate,'batches':summaries,'item_scores':rows}

if __name__=='__main__':
    key=json.loads((ROOT/'key.json').read_text())
    batches=[json.loads(p.read_text()) for p in sorted((ROOT/'responses').glob('*.json'))]
    results=analyze(key,batches)
    (ROOT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results['aggregate'],indent=2))
