import itertools
def pairAt(k):
    # Cantor order: diagonal d = i+q, within it q = 0..d, i = d-q
    d=0
    while (d+1)*(d+2)//2 <= k: d+=1
    q=k-d*(d+1)//2
    return (d-q,q)
def hist(vals,i,q,T):
    o=list(vals)
    while len(o)<T: o.append(o[len(o)-(q+1)])
    return o
def rest(o,T):
    k=0; last_wrong=-1
    for t in range(T):
        i,q=pairAt(k)
        claim = o[t-(q+1)] if i+q+1<=t else None
        if claim!=o[t]: last_wrong=t
        if claim is not None and claim!=o[t]: k+=1
    return last_wrong+1
def R(N,T=None):
    T=T or 6*N*N*N+20
    best=0;arg=None
    for i in range(N):
        for q in range(N-i):
            L=i+q+1
            for vals in itertools.product(range(N),repeat=L):
                o=hist(vals,i,q,T)
                r=rest(o,T)
                if r>best: best,arg=r,(vals,i,q)
    return best,arg
if __name__=="__main__":
 for N in range(1,7):
    print(N,R(N))
