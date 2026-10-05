"""Exact checks and deterministic illustrations; no psychological data.

Run with Python 3. Matplotlib is needed only with --plot.
All output paths are relative to this file's project parent unless --out is given.
"""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import argparse
import csv
import hashlib
import json
import math

parser = argparse.ArgumentParser()
default_out = (Path(__file__).resolve().parent if Path(__file__).name == 'reproduce.py'
               else Path(__file__).resolve().parents[1] / 'outputs')
parser.add_argument('--out', type=Path, default=default_out)
parser.add_argument('--plot', action='store_true')
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
checks = []

def check(name, condition, detail):
    assert condition, name
    checks.append({'name': name, 'passed': True, 'detail': detail})

def trajectory(mode, n=30, d=Q(0)):
    a, k, b, lam = Q(4,5), Q(1,2), Q(1), Q(1,2)
    x, h = Q(2), Q(-1) if mode == 'wrong' else Q(0)
    rows = []
    for t in range(n+1):
        m = x+b
        rows.append((t,x,h,m))
        next_x = a*x-k*(m-h)
        if mode == 'learn':
            z = x+d
            h = (1-lam)*h+lam*(m-z)
        x = next_x
    return rows

a,k,b,lam = Q(4,5),Q(1,2),Q(1),Q(1,2)
eq = -k*b/(1-a+k)
wrong_eq = -k*(b+1)/(1-a+k)
check('equilibria', eq == Q(-5,7) and wrong_eq == Q(-10,7),
      {'naive':str(eq),'wrong_meta_model':str(wrong_eq),'calibrated':'0'})
for mode, target in [('naive',eq),('wrong',wrong_eq),('learn',Q(0))]:
    tr=trajectory(mode,200)
    check('trajectory_limit_'+mode, abs(tr[-1][1]-target)<Q(1,10**50),
          {'at_step_200':float(tr[-1][1]),'target':float(target)})
    for t,x,h,m in tr[:-1]:
        delta=b-h
        if mode == 'learn':
            xn,hn=tr[t+1][1:3]
            check_condition = xn == (a-k)*x-k*delta and b-hn == (1-lam)*delta
            assert check_condition
check('joint_linear_recurrence', True, 'All 200 calibration steps match the derived matrix exactly.')
biased=trajectory('learn',200,Q(1,4))
biased_target=-k*Q(1,4)/(1-a+k)
check('biased_reference',abs(biased[-1][1]-biased_target)<Q(1,10**50),
      {'reference_offset':'1/4','residual_equilibrium':str(biased_target)})
check('gain_stability', a-k==Q(3,10) and a-4*k==Q(-6,5),
      {'base_multiplier':str(a-k),'overcorrection_multiplier':str(a-4*k)})

def mi(records, ix, iy):
    # records consist of (tuple, exact probability).
    px,py,pxy=defaultdict(Q),defaultdict(Q),defaultdict(Q)
    for rec,p in records:
        x,y=rec[ix],rec[iy]
        px[x]+=p;py[y]+=p;pxy[x,y]+=p
    return sum(float(p)*math.log2(float(p/(px[x]*py[y]))) for (x,y),p in pxy.items())

records=[]
for f in [0,1]:
    for e in [0,1]:
        m=f^e
        records.append(((f,m,m^e,(m,e)),Q(1,4)))
info1,info2,infopair=mi(records,0,1),mi(records,0,2),mi(records,0,3)
check('side_information',info1==0 and info2==1 and infopair==1,
      {'I_F_M1_bits':info1,'I_F_M2_bits':info2,'I_F_pair_bits':infopair})
feedback=[((f,m,m),Q(1,4)) for f in [0,1] for m in [0,1]]
check('intervention_agreement',mi(feedback,0,1)==0 and mi(feedback,2,1)==1,
      'Independent M sets future F1=M. I(F0;M)=0; I(F1;M)=1 bit.')

truth=Q(3,5)
q=truth
confidence=[]
exact_risks=[]
for depth in range(7):
    risk=truth*(1-q)**2+(1-truth)*q**2
    identity=truth*(1-truth)+(q-truth)**2
    assert risk==identity
    exact_risks.append(risk)
    confidence.append({'depth':depth,'q':float(q),'brier':float(risk),
                       'accuracy_of_same_binary_answer':float(truth)})
    q=q*q/(q*q+(1-q)*(1-q))
check('confidence_without_evidence',all(exact_risks[i+1]>exact_risks[i]
                                      for i in range(6)),
      {'baseline_brier':confidence[0]['brier'],'depth_4':confidence[4]})

# Two states merged now have different coarse successors: no closed deterministic G.
F={0:0,1:2,2:2};r={0:0,1:0,2:1}
check('abstraction_counterexample',r[0]==r[1] and r[F[0]]!=r[F[1]],
      {'F':F,'r':r,'merged_states':[0,1],'coarse_successors':[r[F[0]],r[F[1]]]})
costs=sum((Q(1,2**i) for i in range(1,101)),Q(0))
check('summable_costs',costs==1-Q(1,2**100) and costs<1,
      'First 100 positive costs 2^-k sum to 1-2^-100. Every finite prefix is below 1.')
check('positive_cost_floor',Q(7,5)//Q(1,5)==7,
      'For additive simultaneous costs >=1/5 under budget 7/5, depth <=7.')
check('fixed_point_not_convergence',1-Q(1,2)==Q(1,2) and 1-(1-0)==0,
      'R(m)=1-m has fixed point 1/2 but orbit 0,1,0,1 does not converge.')
check('complementary_computations',Q(1,2)-2*Q(1,10)==Q(3,10),
      'Two complementary fair-bit observations each have zero standalone value; together remove .5 error at .2 total cost.')

with (args.out/'model-trajectories.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['mode','step','state_x','bias_estimate_h','first_model_m'])
    for mode in ['naive','learn','wrong']:
        for t,x,h,m in trajectory(mode):w.writerow([mode,t,float(x),float(h),float(m)])
report={'date':'2026-10-05','status':'synthetic illustrations, not empirical evidence',
        'arithmetic':'Fractions for algebra/trajectories; floating-point logarithms only for mutual information',
        'checks':checks,'check_count':len(checks),'confidence':confidence,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(args.out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':len(checks),'failed':0,'outputs':str(args.out)}))

if args.plot:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
                         'axes.spines.right':False,'axes.titleweight':'bold'})
    fig,axes=plt.subplots(1,3,figsize=(15,4.8))
    colors=['#4063A5','#14836B','#C65C40']
    for mode,label,col in zip(['naive','learn','wrong'],
                             ['Uncorrected bias','Learned bias correction','Mistaken correction'],colors):
        tr=trajectory(mode,18)
        axes[0].plot([r[0] for r in tr],[float(r[1]) for r in tr],label=label,color=col,lw=2.4)
    axes[0].axhline(0,color='#89929e',ls=':',lw=1)
    axes[0].set(title='A  Reflection can repair or worsen bias',xlabel='Time step',ylabel='State proxy x')
    axes[0].legend(frameon=False,fontsize=9,loc='upper right')
    for mult,label,col in [(Q(3,10),'Base feedback',colors[1]),(Q(-6,5),'Excessive correction',colors[2])]:
        axes[1].plot(range(13),[float(Q(2)*mult**t) for t in range(13)],label=label,color=col,lw=2.4)
    axes[1].axhline(0,color='#89929e',ls=':',lw=1)
    axes[1].set(title='B  Another model can destabilize control',xlabel='Time step',ylabel='State proxy x')
    axes[1].legend(frameon=False,fontsize=9,loc='upper left')
    axes[2].plot([r['depth'] for r in confidence],[r['q'] for r in confidence],
                 color=colors[2],label='Reported confidence',lw=2.4,marker='o')
    axes[2].axhline(float(truth),color=colors[0],lw=2.4,label='Actual correctness probability')
    axes[2].set(title='C  Repeating evidence inflates certainty',xlabel='Number of repeated transformations',
                ylabel='Probability',ylim=(.5,1.035))
    axes[2].legend(frameon=False,fontsize=9,loc='lower right')
    for ax in axes:ax.grid(axis='y',alpha=.15)
    fig.suptitle('Recursive self-modeling has no automatic direction of improvement',fontsize=16,fontweight='bold',y=1.02)
    fig.text(.01,-.035,'Constructed mathematical examples. Panel A supplies calibration evidence. These curves are not measurements of feelings or brain activity.',fontsize=10,color='#555555')
    fig.tight_layout()
    fig.savefig(args.out/'recursive-models.png',dpi=180,bbox_inches='tight')
    fig.savefig(args.out/'recursive-models.svg',bbox_inches='tight')
