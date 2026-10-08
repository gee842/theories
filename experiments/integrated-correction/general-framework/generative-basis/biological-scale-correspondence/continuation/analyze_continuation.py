#!/usr/bin/env python3
"""Read-only published-data analysis. See analysis-plan.json for scope."""
from pathlib import Path
import csv, hashlib, json, platform, zipfile, xml.etree.ElementTree as ET
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.special import expit
import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
SOURCES = ROOT/'sources/biological-scale-correspondence'
F = SOURCES/'elife-103191/elife-103191-fig4-data3-v1.xlsx'
B = SOURCES/'anderson-2018/rstb20170255_si_001.xlsx'
SEED = 20261008
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def plain(o):
    if isinstance(o, np.ndarray): return o.tolist()
    if isinstance(o, np.generic): return o.item()
    raise TypeError(type(o))

# Independent XML numeric extraction checks every analyzed cell against openpyxl.
# The original bytes are never written by this program.
def xml_numeric(path, sheet_index=1):
    ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    result={}
    with zipfile.ZipFile(path) as z, z.open(f'xl/worksheets/sheet{sheet_index}.xml') as stream:
        for _, elem in ET.iterparse(stream, events=('end',)):
            if elem.tag==ns+'c':
                v=elem.find(ns+'v')
                if elem.attrib.get('t','n')=='n' and v is not None:
                    result[elem.attrib['r']]=float(v.text)
                elem.clear()
    return result

def load_foraging():
    w=openpyxl.load_workbook(F, read_only=True, data_only=True)
    s=w.active
    header=next(s.iter_rows(min_row=46,max_row=46,values_only=True))
    assert list(header[1:14])==['worm #','replicate #','sensed encounter #',
       'label (10^ρ_k)','label (10^ρ_h)','label (10^ρ_e)',
       'ρ_k','τ_s','ρ_h','ρ_e','no history','with history','observed']
    rows=[]; checked=0; raw=xml_numeric(F)
    for row in s.iter_rows(min_row=47, max_col=14):
        if row[1].value is None: continue
        values=[]
        for c in row[1:14]:
            assert isinstance(c.value,(int,float)) and np.isfinite(c.value)
            assert float(c.value)==raw[c.coordinate], c.coordinate
            values.append(c.value);checked+=1
        rows.append(values)
    # Frozen coefficients in C7:C9 and D7:D11; these predate mixed-density test.
    small=np.array([s.cell(i,3).value for i in range(7,10)])
    full=np.array([s.cell(i,4).value for i in range(7,12)])
    published_ll=[s.cell(16,j).value for j in (2,3)]
    w.close()
    return np.array(rows,dtype=float), small, full, published_ll, checked

d, beta_small, beta_full, published_ll, nchecked=load_foraging()
worm=d[:,0].astype(int); rep=d[:,1].astype(int); y=d[:,12]
assert np.all((y>=0)&(y<=1)) and np.all((d[:,10:12]>0)&(d[:,10:12]<1))
assert len(np.unique(d[:,:3],axis=0))==len(d)
worms, wi=np.unique(worm,return_inverse=True)
groups, gi=np.unique(d[:,:2],axis=0,return_inverse=True)
group_n=np.bincount(gi)
group_wi=np.searchsorted(worms,groups[:,0])
groups_per_worm=np.bincount(group_wi,minlength=len(worms))
weights=1/(group_n[gi]*groups_per_worm[wi]*len(worms))
assert abs(weights.sum()-1)<1e-12

def by_worm(values):
    group_mean=np.bincount(gi,weights=values,minlength=len(groups))/group_n
    return np.bincount(group_wi,weights=group_mean,minlength=len(worms))/groups_per_worm
def losses(pred):
    p=np.clip(pred,1e-12,1-1e-12)
    return -y*np.log(p)-(1-y)*np.log1p(-p),(p-y)**2
def score(pred):
    ll,se=losses(pred)
    return dict(soft_cross_entropy=float(by_worm(ll).mean()),
                soft_target_mse=float(by_worm(se).mean()),
                encounter_weighted_cross_entropy=float(ll.mean()),
                average_prediction=float(by_worm(pred).mean()),
                average_soft_target=float(by_worm(y).mean()))

rho,t,h,e=d[:,6],d[:,7],d[:,8],d[:,9]
published_predictions={
    'no_density_history':expit(np.column_stack([np.ones(len(d)),rho,t])@beta_small),
    'history':expit(np.column_stack([np.ones(len(d)),rho,t,h,e])@beta_full)}
verification={}
for i,(name,pred) in enumerate(published_predictions.items()):
    err=float(np.max(np.abs(pred-d[:,10+i])))
    ll=-float(losses(pred)[0].sum())
    assert err<2e-14 and abs(ll-published_ll[i])<1e-6
    verification[name]=dict(max_prediction_difference=err,
                            computed_log_likelihood=ll,
                            published_log_likelihood=published_ll[i])

features={
    'constant':np.empty((len(d),0)),
    'current_density':rho[:,None],
    'density_satiety':np.column_stack([rho,t]),
    'history':np.column_stack([rho,t,h,e]),
    'nonlinear_no_density_history':np.column_stack([rho,t,rho**2,t**2])}
rng=np.random.default_rng(SEED)
fold_by_worm=np.empty(len(worms),dtype=int)
fold_by_worm[rng.permutation(len(worms))]=np.arange(len(worms))%5
fold=fold_by_worm[wi]
predictions={};fits={}
for name,xx in features.items():
    out=np.full(len(d),np.nan);fits[name]=[]
    for f in range(5):
        train=fold!=f;test=~train
        ww=weights[train];ww=ww/ww.sum()
        mu=np.average(xx[train],axis=0,weights=ww)
        sd=np.sqrt(np.average((xx[train]-mu)**2,axis=0,weights=ww))
        assert np.all(sd>1e-12)
        x=np.column_stack([np.ones(train.sum()),(xx[train]-mu)/sd])
        yt=y[train]
        def objective(b):
            z=x@b
            return float(np.dot(ww,np.logaddexp(0,z)-yt*z)), x.T@(ww*(expit(z)-yt))
        opt=minimize(objective,np.zeros(x.shape[1]),jac=True,method='BFGS',
                     options={'gtol':1e-8,'maxiter':500})
        grad=float(np.max(np.abs(objective(opt.x)[1])))
        assert np.isfinite(opt.fun) and grad<1e-6, (name,f,opt.message,grad)
        xt=np.column_stack([np.ones(test.sum()),(xx[test]-mu)/sd])
        out[test]=expit(xt@opt.x)
        fits[name].append(dict(fold=f,training_worms=len(np.unique(worm[train])),
            held_out_worms=len(np.unique(worm[test])),parameters=x.shape[1],
            center=mu,scale=sd,coefficients=opt.x,objective=opt.fun,
            gradient_max=grad,optimizer_message=str(opt.message)))
    assert np.all(np.isfinite(out))
    predictions[name]=out

def comparison(pred_a,pred_b):
    # Positive means B improves over A. Conditional bootstrap of held-out scores.
    differences=by_worm(losses(pred_a)[0]-losses(pred_b)[0])
    rng=np.random.default_rng(SEED)
    boot=np.mean(differences[rng.integers(0,len(worms),(5000,len(worms)))],axis=1)
    return dict(mean_cross_entropy_improvement=float(differences.mean()),
        paired_worm_percentiles_2_5_97_5=np.quantile(boot,[.025,.975]),
        worms_improving=int((differences>0).sum()),worms=len(worms))

def calibration(pred):
    # Fixed bins, weights inherited from declared equal-worm weighting.
    out=[]
    for k in range(10):
        take=(pred>=k/10)&(pred<(k+1)/10 if k<9 else pred<=1)
        if take.any():out.append(dict(lower=k/10,upper=(k+1)/10,
            weight=float(weights[take].sum()),
            prediction=float(np.average(pred[take],weights=weights[take])),
            soft_target=float(np.average(y[take],weights=weights[take]))))
    return out

# Different biological preparation; no individual or time join to foraging data.
bw=openpyxl.load_workbook(B,read_only=True,data_only=True)
bs=bw['Syto13 measurements']; bx=xml_numeric(B,bw.sheetnames.index(bs.title)+1)
assert bs.cell(2,1).value=='standard plate' and bs.cell(2,2).value=='full plate'
burden={}
for col,name in [(1,'standard_plate'),(2,'full_plate')]:
    values=[];cells=[]
    for row in bs.iter_rows(min_row=3,min_col=col,max_col=col):
        c=row[0]
        if c.value is None:continue
        assert float(c.value)==bx[c.coordinate]
        values.append(float(c.value));cells.append(c.coordinate)
    burden[name]=dict(n=len(values),mean=float(np.mean(values)),sd=float(np.std(values,ddof=1)),
                      cells=cells,values=values)
burden['standard_minus_full']=burden['standard_plate']['mean']-burden['full_plate']['mean']
burden['standard_div_full']=burden['standard_plate']['mean']/burden['full_plate']['mean']

# Secondary descriptive mechanism audit, added after the first foraging fit.
# These groups are not paired across sheets or joined to fluorescence animals.
avoidance={}
for sheet in ['% animals off 10% M. nem','% animals off 10% UV336']:
    ss=bw[sheet];raw=xml_numeric(B,bw.sheetnames.index(sheet)+1);out={}
    for col in [1,3,6,7,8]:
        cells=[];values=[]
        for row in ss.iter_rows(min_row=3,min_col=col,max_col=col):
            c=row[0]
            if not isinstance(c.value,(int,float)):continue
            assert float(c.value)==raw[c.coordinate]
            cells.append(c.coordinate);values.append(float(c.value))
        out[ss.cell(2,col).value]=dict(n=len(values),mean=float(np.mean(values)),
            sd=float(np.std(values,ddof=1)),cells=cells,values=values)
    avoidance[sheet]=out
bw.close()

result=dict(status='passed',created_at_utc=datetime.now(timezone.utc).isoformat(),
    plan_sha256=sha(HERE/'analysis-plan.json'),script_sha256=sha(Path(__file__)),
    inputs={str(p.relative_to(ROOT)):sha(p) for p in [F,B]},
    software=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,openpyxl=openpyxl.__version__),
    population=dict(rows=len(d),worms=len(worms),imputations=len(np.unique(rep)),
        rows_per_imputation_min=int(np.min(np.bincount(rep)[1:])),
        rows_per_imputation_max=int(np.max(np.bincount(rep)[1:])),
        worm_imputation_groups=len(groups),numeric_cells_cross_checked=nchecked),
    published_prediction_reproduction=verification,
    published_transfer_scores={n:score(p) for n,p in published_predictions.items()},
    published_transfer_comparison=comparison(*published_predictions.values()),
    cross_validation_scores={n:score(p) for n,p in predictions.items()},
    cross_validation_comparisons={
        'density_satiety_to_history':comparison(predictions['density_satiety'],predictions['history']),
        'nonlinear_to_history':comparison(predictions['nonlinear_no_density_history'],predictions['history'])},
    calibration={n:calibration(p) for n,p in predictions.items()},
    folds={str(int(w)):int(f) for w,f in zip(worms,fold_by_worm)},fits=fits,
    pathogen_fluorescence=burden,pathogen_avoidance_groups=avoidance,
    interpretation='Empirical computations, not Lean proofs. Conditional on published classifications and imputations. No joint cross-study trajectory, new experiment, causal cognitive identification, universal residual bound or ecological renewal measurement.')
(HERE/'results.json').write_text(json.dumps(result,default=plain,indent=2)+'\n')
with (HERE/'worm-scores.csv').open('w') as stream:
    names=list(predictions)
    writer=csv.writer(stream);writer.writerow(['worm','fold']+[n+'_cross_entropy' for n in names])
    vals=np.column_stack([by_worm(losses(predictions[n])[0]) for n in names])
    for w,f,v in zip(worms,fold_by_worm,vals):writer.writerow([int(w),int(f),*v])
print(json.dumps({k:result[k] for k in ['status','population','published_transfer_scores','published_transfer_comparison','cross_validation_scores','cross_validation_comparisons']},default=plain,indent=2))
print('SYTO13 means:',burden['standard_plate']['mean'],burden['full_plate']['mean'])
