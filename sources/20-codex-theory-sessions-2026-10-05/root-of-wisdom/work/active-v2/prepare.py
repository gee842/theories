"""Build six initial states and public-only prompts before any participant dispatch."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json, random
from engine import initialize

ROOT=Path(__file__).resolve().parent
protocol=json.loads((ROOT/'protocol.json').read_text())
public=json.loads((ROOT/'public-cases.json').read_text())
cases={c['case_id']:c for c in public['cases']}
order=list(cases)
random.Random(protocol['order_seed']).shuffle(order)
amendment={
    'recorded_at':datetime.now(ZoneInfo('Asia/Bangkok')).isoformat(),
    'timing':'Before any participant dispatch or outcome collection. Original protocol preserved unchanged.',
    'case_freeze_pending':False,
    'parse_policy':'Parse the exact raw participant response as JSON, allowing ordinary JSON whitespace only. No fence stripping, repairs or retries. Syntax failure is recorded and treated as an empty response, forcing fallback for every open episode.',
    'reason_policy':'Missing, non-string or empty reason invalidates its command. Reasons over 35 whitespace-delimited words are counted as cap violations but the command executes if otherwise feasible.',
    'extra_id_policy':'Commands for unknown or already-closed episode IDs are logged and ignored. A missing required open ID or duplicate required ID forces that episode fallback. Extra IDs do not invalidate otherwise valid required commands.',
    'private_draw_amendment':'Pre-run draft with shared draws within matched pairs was replaced by six sequential independent draws from stated priors, seed 2026100502; old draft preserved. Current draws are fixed across conditions and repetitions; each public case remains independent.',
    'initial_comparison':'Initial exact ties accepted. Invalid commands count as failures even if the effective fallback is optimal. Initial Bellman gap records the effective forced action when invalid.',
    'word_count':'Whitespace-delimited counts; output cap equal across conditions, not a hidden-computation control.'
}
(ROOT/'pre-run-amendments.json').write_text(json.dumps(amendment,indent=2)+'\n')
manifest={'conditions':protocol['conditions'],'order_seed':protocol['order_seed'],'batches':[]}
common_note='\nInterface clarification shared across conditions: a missing or empty reason invalidates a command. An over-35-word reason is recorded as a limit violation, but an otherwise valid command executes. Extra unknown or closed episode IDs are ignored and logged; a missing or duplicate required ID forces fallback for that episode. Return exact JSON without fences or other text; invalid JSON forces fallback for all open episodes.\n'
for repetition in (1,2):
    current_order=order if repetition==1 else list(reversed(order))
    for condition in protocol['conditions']:
        batch=f'r{len(manifest["batches"])+1:02d}'
        dest=ROOT/'runs'/batch
        dest.mkdir(parents=True,exist_ok=False)
        prompt=(ROOT/f'treatment-{condition}.txt').read_text()+common_note+'\n'+public['shared_instructions']+'\n\n'
        prompt+='\n\n'.join(i+'\n'+cases[i]['statement'] for i in current_order)+'\n'
        (dest/'prompt.txt').write_text(prompt)
        state=initialize(batch,condition,repetition,current_order)
        (dest/'state.json').write_text(json.dumps(state,indent=2)+'\n')
        manifest['batches'].append({'batch':batch,'condition':condition,'replicate':repetition,'order':current_order,'prompt_path':str(dest/'prompt.txt')})
(ROOT/'run-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
