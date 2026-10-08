"""Recompute selected published contrasts from unmodified animal-level source data.

This is numerical source-data checking, not a new experiment or formal proof.
Requires numpy; takes the repository root and extraction directory as arguments.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

ROOT, EXTRACT = map(Path, sys.argv[1:3])
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numeric_tail(row, size):
    assert len(row) >= size + 1
    values = row[1:size+1]
    assert all(isinstance(v,(int,float)) and np.isfinite(v) for v in values)
    assert all(v is None for v in row[size+1:])
    return np.array(values, dtype=float)


f2 = json.loads((EXTRACT/'figure2.json').read_text())
f3 = json.loads((EXTRACT/'figure3.json').read_text())
assert f2['sheet'] == 'figure  2' and f2['ranges'][0]['address'] == 'B55:X72'
r = f2['ranges'][0]['values']
assert r[0][0] == 'Panel C' and r[10][0] == 'Panel D'
assert r[1][1:23] == ['YFP']*22 and r[5][1:22] == ['NpHR']*21
assert [r[i][0] for i in [2,3,6,7]] == ['A','C','A','C']
assert all(r[i] == r[i+10] for i in [1,2,3,5,6,7]), 'Repeated panels must not become extra animals'
a,c = (numeric_tail(r[i],22) for i in [2,3])
b,d = (numeric_tail(r[i],21) for i in [6,7])
delta_control, delta_inhibition = a-c, b-d
n1,n2 = len(a),len(b)
pooled_var = ((n1-1)*np.var(delta_control,ddof=1)+(n2-1)*np.var(delta_inhibition,ddof=1))/(n1+n2-2)
effect = delta_control.mean()-delta_inhibition.mean()
contrast_f = effect**2/(pooled_var*(1/n1+1/n2))

assert f3['sheet'] == 'Figure 3'
assert [x['address'] for x in f3['ranges']] == ['B3:I11','B14:I23']
s,t = [x['values'] for x in f3['ranges']]
assert s[0][1:7] == ['Paired']*6 and s[5][1:8] == ['Unpaired']*7
assert [s[i][0] for i in [1,2,3,6,7,8]] == [1,2,3,1,2,3]
paired = np.stack([numeric_tail(s[i],6) for i in [1,2,3]],axis=1)
unpaired = np.stack([numeric_tail(s[i],7) for i in [6,7,8]],axis=1)
assert np.array_equal(paired[:,0],numeric_tail(t[2],6))
assert np.array_equal(unpaired[:,0],numeric_tail(t[3],7))
groups = [paired,unpaired]
both = np.concatenate(groups)
N,k = both.shape
block_mean,grand = both.mean(0),both.mean()
ss_interaction = sum(len(y)*np.sum((y.mean(0)-y.mean()-block_mean+grand)**2) for y in groups)
ss_residual = sum(np.sum((y-y.mean(1,keepdims=True)-y.mean(0)+y.mean())**2) for y in groups)
df_error = (N-2)*(k-1)
ms_error = ss_residual/df_error
interaction_f = ss_interaction/(k-1)/ms_error
# Equal weighting of the two group marginal means for the block main effect.
# This is the declared Type III contrast; sample sizes are unequal (6 and 7).
marginal = (paired.mean(0)+unpaired.mean(0))/2
effective_n = 4/(1/len(paired)+1/len(unpaired))
block_f = effective_n*np.sum((marginal-marginal.mean())**2)/(k-1)/ms_error
sample_weighted_block_f = N*np.sum((block_mean-grand)**2)/(k-1)/ms_error
consumed_p,consumed_u = numeric_tail(t[8],6),numeric_tail(t[9],7)
consumption_var = ((len(consumed_p)-1)*np.var(consumed_p,ddof=1)+(len(consumed_u)-1)*np.var(consumed_u,ddof=1))/(N-2)
consumption_t = (consumed_u.mean()-consumed_p.mean())/np.sqrt(consumption_var*(1/6+1/7))

comparisons = [
    {'name':'probe cue by group F', 'computed':float(contrast_f), 'reported':4.57, 'df':[1,41]},
    {'name':'devaluation block by group F', 'computed':float(interaction_f), 'reported':4.58, 'df':[2,22]},
    {'name':'devaluation block main effect F, equal group marginals', 'computed':float(block_f), 'reported':4.91, 'df':[2,22]},
    {'name':'consumption absolute t', 'computed':float(consumption_t), 'reported':4.95, 'df':11},
]
for comparison in comparisons:
    comparison['matches_reported_rounding'] = round(comparison['computed'],2)==comparison['reported']
assert all(c['matches_reported_rounding'] for c in comparisons)
manifest = json.loads((ROOT/'sources/knowledge-semantics/manifest.json').read_text())
preservation = {item['file']:sha(ROOT/'sources/knowledge-semantics'/item['file'])==item['sha256'] for item in manifest['files']}
assert all(preservation.values())
receipt = {
    'status':'passed_four_selected_statistic_reproductions',
    'checked_at_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Animal-level published summaries only. No raw timestamp/neural-data reanalysis, fresh experiment, p-value reproduction, ethical proof or semantic-sufficiency proof.',
    'numpy_version':np.__version__,
    'probe':{'n_control':n1,'n_inhibition':n2,'mean_A_control':float(a.mean()),'mean_C_control':float(c.mean()),'mean_A_inhibition':float(b.mean()),'mean_C_inhibition':float(d.mean()),'mean_A_minus_C_control':float(delta_control.mean()),'mean_A_minus_C_inhibition':float(delta_inhibition.mean()),'between_group_contrast_percentage_points':float(effect),'units':'percentage of cue time in food port minus pre-cue baseline'},
    'devaluation':{'n_paired':6,'n_unpaired':7,'first_block_paired':float(paired[:,0].mean()),'first_block_unpaired':float(unpaired[:,0].mean()),'first_block_difference_percentage_points':float(unpaired[:,0].mean()-paired[:,0].mean()),'response_units':'percentage of cue time in food port, without baseline subtraction','consumption_paired_grams':float(consumed_p.mean()),'consumption_unpaired_grams':float(consumed_u.mean()),'alternative_sample_weighted_block_f':float(sample_weighted_block_f),'contrast_note':'The alternative sample-weighted block estimand gives a different F. Equal group marginal weighting matches the reported statistic; arithmetic agreement alone does not establish author software settings.'},
    'statistics':comparisons,
    'preservation':preservation,
    'source_ranges':{'probe_control':"'figure  2'!C57:X58",'probe_inhibition':"'figure  2'!C61:W62",'devaluation_paired':"'Figure 3'!C4:H6",'devaluation_unpaired':"'Figure 3'!C9:I11",'consumption':"'Figure 3'!C22:I23"},
    'assumptions':['Columns within each panel are matched animals across conditions/blocks, as implied by the source layout and repeated-measures design. No cross-figure individual matching is asserted.','Use every supplied animal in the target panels; paper-level exclusions were already applied by the authors.','Repeated display panels are duplicate views, not independent evidence.','Equal-variance contrast and uncorrected repeated-measures model reproduce the specified paper statistics; their empirical assumptions are not proved by arithmetic agreement.'],
    'file_sha256':{str(p.relative_to(ROOT) if p.is_relative_to(ROOT) else p):sha(p) for p in [Path(__file__),HERE/'inspect_source.mjs',EXTRACT/'figure2.json',EXTRACT/'figure3.json']},
}
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':receipt['status'],'statistics':comparisons,'probe_contrast':float(effect)},indent=2))
