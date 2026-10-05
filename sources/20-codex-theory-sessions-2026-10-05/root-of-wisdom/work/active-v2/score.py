"""Prespecified descriptive aggregation; no estimated independent item sample size."""
from pathlib import Path
from fractions import Fraction as F
import json

ROOT=Path(__file__).resolve().parent
PAIRS=[['A01','A02'],['A03','A04'],['A05','A06']]

def summarize(states):
    episodes=[ep for s in states for ep in s['episodes'].values()]
    assert episodes and all(ep['closed'] for ep in episodes)
    events=[e for ep in episodes for e in ep['events']]
    initial=[ep['events'][0] for ep in episodes]
    terminal=[ep['events'][-1] for ep in episodes]
    queries=[e for e in events if e['effective_kind']=='query']
    return {
        'contexts':len(states),'episodes':len(episodes),
        'initial_optimal':sum(e['optimal_command'] for e in initial),
        'initial_total':len(initial),
        'initial_bellman_gap_sum':str(sum((F(e['bellman_gap']) for e in initial),F(0))),
        'matched_pair_success':sum(all(s['episodes'][i]['events'][0]['optimal_command'] for i in pair) for s in states for pair in PAIRS),
        'matched_pair_total':len(states)*len(PAIRS),
        'visited_optimal':sum(e['optimal_command'] for e in events),'visited_total':len(events),
        'strict_unnecessary_continuations':sum(e['strict_unnecessary_continuation'] for e in queries),
        'queries':len(queries),
        'query_fees':str(sum((F(ep['query_spending']) for ep in episodes),F(0))),
        'action_fees':str(sum((F(ep['action_fee']) for ep in episodes),F(0))),
        'final_elapsed_sum':sum(ep['final_elapsed'] for ep in episodes),
        'terminal_conditional_excess_sum':str(sum((F(e['terminal_conditional_excess']) for e in terminal),F(0))),
        'local_bellman_gap_sum':str(sum((F(e['bellman_gap']) for e in events),F(0))),
        'realized_total_loss':str(sum((F(ep['realized_total_loss']) for ep in episodes),F(0))),
        'invalid_commands':sum(e['invalid'] for e in events),
        'over_word_cap':sum(e['reason_words'] is not None and e['reason_words']>35 for e in events),
        'missing_or_empty_reasons':sum(not isinstance(e['submitted'].get('reason'),str) or not e['submitted'].get('reason','').strip() for e in events),
        'extra_id_events':sum(len(f['extra_ids']) for s in states for f in s.get('format_events',[])),
        'duplicate_id_events':sum(len(f['duplicate_ids']) for s in states for f in s.get('format_events',[])),
        'parse_failures':sum(len(s.get('parse_failures',[])) for s in states)
    }

def main():
    manifest=json.loads((ROOT/'run-manifest.json').read_text())
    states=[json.loads((ROOT/'runs'/b['batch']/'state.json').read_text()) for b in manifest['batches']]
    result={'by_condition':{c:summarize([s for s in states if s['condition']==c]) for c in manifest['conditions']},
            'by_batch':{s['batch']:summarize([s]) for s in states},'all':summarize(states)}
    (ROOT/'scores.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['by_condition'],indent=2))

if __name__=='__main__': main()
