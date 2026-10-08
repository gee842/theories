"""Independent stdlib Fraction controller replay and Householder-QR ARX fit.
Never imports the numerical producer/checker or invokes hardware. No NumPy/SVD.
"""
from pathlib import Path
from fractions import Fraction as Q
import csv,datetime,hashlib,json,math,sys,zipfile,urllib.request
OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file())
SRC=ROOT/'sources/tclab-benchmark'
EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report=json.loads((EXP/'tclab-results.json').read_text())
manifest=json.loads((SRC/'PROVENANCE.json').read_text())
remote=[]
with zipfile.ZipFile(SRC/'CACE_2020_source.zip') as z:
 for row in manifest['originals']+manifest['extracted_members']:
  p=ROOT/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
  if 'member' in row:assert z.read(row['member'])==p.read_bytes()
for row in manifest['originals']:
 try:
  data=urllib.request.urlopen(row['url'],timeout=45).read()
  assert hashlib.sha256(data).hexdigest()==row['sha256']
  remote.append({'path':row['path'],'status':'remote bytes match pinned original','sha256':row['sha256']})
 except Exception as e:remote.append({'path':row['path'],'status':'fetch failed','error':str(e)})
def load(p,kind=float):
 with p.open() as f:return [{k:kind(v) for k,v in row.items()} for row in csv.DictReader(f)]
def close(a,b,tol=1e-9):assert abs(a-b)<=tol,(a,b,tol)
replays=[]
for run in report['physical_runs']:
 data=load(ROOT/run['path'],Q)
 if run['label']=='initial':
  tau=Q('175.1814480958061');delay=Q('15.622280726988599');gain=tau/(Q('0.9200270657559153')*(delay+max(tau/10,delay*Q('0.8'))))
 else:tau,gain=Q(55),Q(10)
 # Retain integrated error, unlike producer's already gain-weighted integral.
 acc=Q(0);worst=Q(0);intervals=[];moves=[];exposure=Q(0)
 for a,b in zip(data,data[1:]):
  dt=b['Time']-a['Time'];assert dt>0
  e=b['TSP1']-b['T1'];proposed=acc+e*dt;raw=gain*e+(gain/tau)*proposed
  cmd=min(Q(100),max(Q(0),raw))
  if Q(0)<=raw<=Q(100):acc=proposed
  worst=max(worst,abs(cmd-b['Q1']));intervals.append(dt);moves.append(b['Q1']-a['Q1']);exposure+=a['Q1']*dt
 assert worst<Q(1,10**9)
 tracking=sum(abs(r['TSP1']-r['T1']) for r in data);motion=sum(abs(v) for v in moves);net=sum(moves);n=len(data)
 assert net==data[-1]['Q1']-data[0]['Q1'];m=run['metrics']
 vals={'samples':n,'mean_absolute_tracking_error_celsius':float(tracking/n),'mean_absolute_command_movement_percent':float(motion/n),'paper_absolute_objective':float((tracking+motion/2)/n),'archived_search_signed_objective_on_observations':float((tracking+net/2)/n),'commanded_percent_seconds_left_hold':float(exposure),'interval_seconds_min':float(min(intervals)),'interval_seconds_max':float(max(intervals))}
 for k,v in vals.items():close(v,m[k],1e-7 if k=='commanded_percent_seconds_left_hold' else 1e-9)
 replays.append({'label':run['label'],'commands':n-1,'max_exact_command_error_percent':float(worst),'metrics':vals})

def design(data,ch,second):
 rows=[];targets=[]
 for k in range(2,len(data)):
  rows.append([1.,data[k-1][ch],data[k-2][ch],data[k-1]['H1'],data[k-2]['H1']]+([data[k-1]['H2'],data[k-2]['H2']] if second else []));targets.append(data[k][ch])
 return rows,targets

def householder(A,b):
 R=[row[:] for row in A];z=b[:];m=len(R);n=len(R[0])
 for j in range(n):
  v=[R[k][j] for k in range(j,m)];norm=math.sqrt(math.fsum(t*t for t in v));assert norm>1e-12
  v[0]+=math.copysign(norm,v[0]);den=math.fsum(t*t for t in v);assert den>0
  for k in range(j,n):
   scale=2*math.fsum(v[i-j]*R[i][k] for i in range(j,m))/den
   for i in range(j,m):R[i][k]-=scale*v[i-j]
  scale=2*math.fsum(v[i-j]*z[i] for i in range(j,m))/den
  for i in range(j,m):z[i]-=scale*v[i-j]
 beta=[0.]*n
 for j in reversed(range(n)):
  beta[j]=(z[j]-math.fsum(R[j][k]*beta[k] for k in range(j+1,n)))/R[j][j]
 return beta

def errors(y,p):
 es=[a-b for a,b in zip(y,p)]
 return {'rmse_celsius':math.sqrt(math.fsum(e*e for e in es)/len(es)),'mae_celsius':math.fsum(abs(e) for e in es)/len(es),'max_absolute_error_celsius':max(abs(e) for e in es)},es
train=load(SRC/'extracted/1_Model/2_Heaters/initial_models.csv');valid=load(SRC/'extracted/1_Model/2_Heaters/validation.csv')
fits=[]
for expected in report['identification']:
 ch=expected['channel'];second=expected['second_heater_included'];X,y=design(train,ch,second);Xv,yv=design(valid,ch,second)
 beta=householder(X,y);difference=max(abs(a-b) for a,b in zip(beta,expected['parameters']));assert difference<1e-8
 predict=lambda A:[math.fsum(a*b for a,b in zip(row,beta)) for row in A]
 training,tr=errors(y,predict(X));test,te=errors(yv,predict(Xv));roll=[valid[0][ch],valid[1][ch]]
 for k in range(2,len(valid)):
  row=[1.,roll[k-1],roll[k-2],valid[k-1]['H1'],valid[k-2]['H1']]+([valid[k-1]['H2'],valid[k-2]['H2']] if second else [])
  roll.append(math.fsum(a*b for a,b in zip(row,beta)))
 rollout,_=errors(yv,roll[2:]);radius=max(abs(e) for e in tr);exceed=[k+2 for k,e in enumerate(te) if abs(e)>radius]
 assert len(exceed)==expected['training_max_radius_validation_exceedances']
 for name,value in [('training_one_step',training),('validation_one_step',test),('validation_free_rollout',rollout)]:
  for metric,v in value.items():close(v,expected[name][metric],1e-7)
 fits.append({'channel':ch,'second_heater_included':second,'fit_method':'independent standard-library Householder QR','coefficients':beta,'max_coefficient_difference_from_SVD':difference,'training_one_step':training,'validation_one_step':test,'validation_free_rollout':rollout,'training_radius_exceeded_at_csv_data_indices_zero_based':exceed})
receipt={'status':'passed','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'review_script_sha256':sha(Path(__file__)),'producer_sha256':sha(EXP/'analyze_tclab.py'),'producer_results_sha256':sha(EXP/'tclab-results.json'),'alternate_checker_sha256':sha(EXP/'check_tclab.py'),'alternate_receipt_sha256':sha(EXP/'tclab-checks.json'),'provenance_sha256':sha(SRC/'PROVENANCE.json'),'remote_provenance':remote,'physical_runs':replays,'total_commands':sum(r['commands'] for r in replays),'independent_fits':fits,'scope':'Archived data analysis; no new physical experiment or future-error guarantee. QR uses training only; validation measurements occur only in one-step tests or first two rollout states. Input timing is recorded index, not a calibrated continuous-time model.'}
(OUT/'numerical-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'passed','commands':receipt['total_commands'],'remote':remote,'fits':fits},indent=2))
