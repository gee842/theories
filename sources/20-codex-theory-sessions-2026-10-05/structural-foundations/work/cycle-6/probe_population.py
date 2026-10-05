from dataclasses import dataclass
@dataclass(frozen=True)
class S:
 n:int=2
 p:int=1
 r:int=0
 m:int=0

def step(s,regime,query=False,free=False,blind=False):
 if not s.n:return s
 cost=(14 if query and not free else 0)
 revise=(query and regime or blind) and s.m==0
 cost+=24 if revise and not free else 0
 p=(0 if (s.m or revise) else 1)
 ret=((100,136),(118,106))[regime][s.p]
 pool=s.r+(148+ret)*s.n-2-cost
 if pool<0:return S(0,s.p,0,s.m)
 n=min(4,pool//260);r=min(259,pool-260*n)
 return S(n,p,r,int(s.m or revise))
for d in [1,27,28,31,32]:
 s=S()
 for t in range(1,d+1):s=step(s,1,query=t==d)
 print('delay',d,s)
for q in [1,2,5,10,20,27,28,40,60]:
 bad=[]
 for onset in range(1,5*q+20):
  s=S()
  for t in range(1,onset+q+2):
   s=step(s,int(t>=onset),query=(t%q==0 and not s.m))
   if not s.n:bad.append(onset);break
  assert not s.n or s.m
 print('q',q,'bad',bad[:10],len(bad))
s=S()
for t in range(1,11):
 s=step(s,0,query=True)
 print('pre q1',t,s)
