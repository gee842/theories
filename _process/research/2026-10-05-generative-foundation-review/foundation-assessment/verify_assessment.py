"""Independent finite mathematical and saved-data checks for the assessment.

The graph checks support examples of the stochastic comparison theorem;
they are not a proof assistant or evidence that physical premises always hold.
The CSV checks do not refit or retune the exploratory microbial comparison.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial, sqrt, exp
import csv
import hashlib
import json

HERE=Path(__file__).resolve().parent
checks=[]


def record(name, passed, details):
    assert passed,name
    checks.append({"name":name,"passed":True,"details":details})


def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def dag(n,edges):
    seen=set()
    while len(seen)<n:
        ready={i for i in range(n) if i not in seen and
               all(j in seen for j,k in edges if k==i)}
        if not ready:
            return False
        seen|=ready
    return True


n=4
possible=[(j,i) for j in range(n) for i in range(n) if j!=i]
count=0
for bits in product((0,1),repeat=len(possible)):
    edges={e for e,b in zip(possible,bits) if b}
    if not dag(n,edges):
        continue
    count+=1
    B=[[F((i+j)%3+1,2) if (j,i) in edges else F(0) for j in range(n)] for i in range(n)]
    powers=[eye(n)]
    for k in range(n):
        powers.append(mul(B,powers[-1]))
    assert all(v==0 for row in powers[n] for v in row)
    # Polynomial p(t)=sum B^k t^k/k! obeys p'=Bp coefficient by coefficient.
    for k in range(n-1):
        derivative=[[F(k+1)*v/factorial(k+1) for v in row] for row in powers[k+1]]
        rhs=[[v/factorial(k) for v in row] for row in mul(B,powers[k])]
        assert derivative==rhs
    # Integral of exp((B-lambda I)t) equals (lambda I-B)^-1.
    for lam in (F(1,2),F(1),F(2)):
        integral=[[sum(powers[k][i][j]/lam**(k+1) for k in range(n))
                   for j in range(n)] for i in range(n)]
        decay=[[lam*F(i==j)-B[i][j] for j in range(n)] for i in range(n)]
        assert mul(decay,integral)==eye(n)
record("acyclic_stochastic_comparison_polynomial",count==543,
       {"directed_graphs_enumerated":4096,"acyclic_graphs":count,
        "nilpotent_and_differential_identities":"exact rational arithmetic",
        "decay_rates_per_graph":3})

# Serial replacements attain the population survival and mean extinction bounds.
for n in range(1,9):
    for lam in (F(1,2),F(1),F(2)):
        coeff=[lam**k/F(factorial(k)) for k in range(n)]
        for k in range(n-1):
            assert (k+1)*coeff[k+1]-lam*coeff[k]==0
        assert -lam*coeff[-1]==-(lam**n)/factorial(n-1)
        integrated=sum(coeff[k]*factorial(k)/lam**(k+1) for k in range(n))
        assert integrated==n/lam
record("erlang_sharp_witness",True,{"chain_lengths":list(range(1,9)),
       "rates":["1/2","1","2"],"mean_extinction_time":"n/lambda",
       "meaning":"Constructed continuous-time replacement chain, not measured lifetimes."})

bench=HERE/'benchmark'
a=json.loads((bench/'analysis.json').read_text())
rows=list(csv.DictReader((bench/'predictions.csv').open()))
source=list(csv.DictReader(Path(a['source_path']).open()))
record("protocol_preserved",hashlib.sha256((bench/'PROTOCOL.md').read_bytes()).hexdigest()==a['protocol_sha256'],a['protocol_sha256'])
record("source_preserved",hashlib.sha256(Path(a['source_path']).read_bytes()).hexdigest()==a['source_sha256'],a['source_sha256'])
record("saved_rows_complete",len(rows)==24 and len({r['row_index'] for r in rows})==24,
       {"test_conditions":24,"source_blocks":len({r['source'] for r in rows})})
for fold in a['folds']:
    train=[source[i] for i in fold['train_indices']]
    test=[source[i] for i in fold['test_indices']]
    assert len(train)==36 and len(test)==6
    assert not {r['source'] for r in train}&{r['source'] for r in test}
    assert max(float(r['cycle'])+1 for r in train)<min(float(r['cycle']) for r in test)
    for library in fold['libraries'].values():
        scores=library['validation']
        chosen=library['selected_indices']['selected']
        assert scores[chosen]['mse']<=min(v['mse'] for v in scores)+1e-12
        assert library['selected_candidates']['selected']['family']=='persistence'
        for candidate in scores:
            for inner in candidate['inner_folds']:
                tr=[source[i] for i in inner['train_indices']]
                te=[source[i] for i in inner['test_indices']]
                assert not {r['source'] for r in tr}&{r['source'] for r in te}
                assert max(float(r['cycle'])+1 for r in tr)<min(float(r['cycle']) for r in te)
record("outer_and_inner_source_time_separation",True,
       {"outer_folds":4,"primary_selection":"persistence in both libraries for every fold"})
recalculated={}
for name in a['metrics']:
    err=[float(r[name])-float(r['next_od']) for r in rows]
    metric={"rmse":sqrt(sum(e*e for e in err)/len(err)),"mae":sum(abs(e) for e in err)/len(err)}
    assert all(abs(metric[k]-a['metrics'][name][k])<1e-12 for k in metric)
    recalculated[name]=metric
record("metrics_recalculated_from_saved_predictions",True,recalculated)
record("primary_augmentation_has_zero_increment",all(r['baseline_selected']==r['augmented_selected']==r['persistence'] for r in rows)
       and not a['primary_expectation_met'],
       "Identical primary predictions; secondary ridge gains are not substituted for the failed expectation.")
report={"date":"2026-10-05","status":"passed","check_groups":len(checks),
        "scope":"Independent finite algebra and data/protocol integrity checks. No empirical universality, causal inference, or proof certification.",
        "checks":checks}
tail=lambda t: exp(-t)*(1+t+t*t/2)
left,right=0.0,20.0
for _ in range(60):
    middle=(left+right)/2
    if tail(middle)>.05:
        left=middle
    else:
        right=middle
report['erlang_three_type_illustration']={"mean_extinction_time":3,
    "survival_probability_after_three":tail(3),
    "time_at_five_percent_survival":(left+right)/2,
    "method":"Analytic tail evaluated numerically; threshold by bisection; not measured data."}
(HERE/'INDEPENDENT-CHECKS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({"status":"passed","check_groups":len(checks),"dag_count":count,"primary_metrics":recalculated['baseline_selected']}))
