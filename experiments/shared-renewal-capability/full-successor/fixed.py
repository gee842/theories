"""Directed 96-bit fixed-point uniformization using safe int64 limbs.

Rows of M are nonnegative integer numerators with common sum gamma.
The scale is (2^32)^3-1. Each sparse product is below gamma*2^32.
"""
from fractions import Fraction
from math import isqrt
import numpy as np
from scipy.sparse import eye
BASE=2**32;SCALE=BASE**3-1;WSCALE=2**256

def step(M,digits,gamma,up=False):
    a=M@digits
    # Normalize product digits, retaining a small fourth leading digit.
    a[:,1]+=a[:,0]//BASE;a[:,0]%=BASE
    a[:,2]+=a[:,1]//BASE;a[:,1]%=BASE
    carry=a[:,2]//BASE;a[:,2]%=BASE
    out=np.empty_like(a)
    for j in (2,1,0):
        value=carry*BASE+a[:,j]
        out[:,j]=value//gamma;carry=value%gamma
    if up:
        out[:,0]+=(carry>0)
        out[:,1]+=out[:,0]//BASE;out[:,0]%=BASE
        out[:,2]+=out[:,1]//BASE;out[:,1]%=BASE
    assert np.min(out)>=0 and np.max(out)<BASE
    return out

def unpack(row):return sum(int(row[i])*BASE**i for i in range(3))
def pack(values):return np.array([[(int(v)//BASE**i)%BASE for i in range(3)] for v in values],dtype=np.int64)

def poisson(mu,order):
    lo=[0]*(order+1);hi=[0]*(order+1);lo[mu]=hi[mu]=WSCALE
    for n in range(mu,0,-1):lo[n-1]=lo[n]*n//mu;hi[n-1]=(hi[n]*n+mu-1)//mu
    for n in range(mu,order):lo[n+1]=lo[n]*mu//(n+1);hi[n+1]=(hi[n]*mu+n)//(n+1)
    tail=Fraction(hi[order]*mu,order+1)/(1-Fraction(mu,order+2))
    dl=sum(lo);du=Fraction(sum(hi))+tail
    assert tail/dl<Fraction(1,10**50)
    return lo,hi,tail,dl,du

def certify(Q,reward,deadline=10,start=0,progress=None):
    gamma=int(max(-Q.diagonal()));mu=gamma*deadline;assert isinstance(mu,int) and mu>0
    order=mu+20*isqrt(mu)+150
    M=(Q+gamma*eye(Q.shape[0],format='csr',dtype=np.int64)).tocsr();M.eliminate_zeros()
    assert M.dtype==np.int64 and min(M.data)>=0 and np.all(np.asarray(M.sum(axis=1)).ravel()==gamma)
    assert (gamma+1)*BASE+gamma<2**63
    wl,wu,tail,dl,du=poisson(mu,order)
    v=pack([SCALE if r else 0 for r in reward]);lower=v.copy();upper=v.copy();nl=0;nu=0
    for n in range(order+1):
        nl+=wl[n]*unpack(lower[start]);nu+=wu[n]*unpack(upper[start])
        if n<order:lower=step(M,lower,gamma);upper=step(M,upper,gamma,True)
        if progress and n%1000==0:progress(n,order)
    lo=Fraction(nl,SCALE)/du;hi=(Fraction(nu,SCALE)+tail)/dl
    return {'lower_exact':str(lo),'upper_exact':str(hi),'lower_decimal':float(lo),'upper_decimal':float(hi),'width_decimal':float(hi-lo),'uniformization_rate':gamma,'poisson_mean':mu,'poisson_order':order,'poisson_tail_upper_exact':str(tail/dl),'probability_scale':str(SCALE),'limb_safe_upper':str((gamma+1)*BASE+gamma)}
