"""Prop 2.3(2): cap exactly at K* -- local stability fails when Gamma > n/(n-1) (delta_f=0)."""
def phi(K,Kbar,n,r,beta,kap,Om,k0,dK):
    return kap*Om*((1-beta)*K**r/(K**r+(n-1)*Kbar**r)+beta/n)+k0-dK*K
for (n,r,beta,k0) in [(2,3.0,0.0,0.0),(2,1.5,0.0,0.0),(4,2.0,0.0,0.0),(4,1.2,0.0,0.0)]:
    kap,Om,dK=0.5,1.0,0.2
    Ks=(kap*Om/n+k0)/dK; G=(1-beta)*r*(kap*Om/(kap*Om+n*k0))
    vals=[phi(Ks*(1-e),Ks,n,r,beta,kap,Om,k0,dK) for e in (1e-3,1e-2)]
    print(f"n={n}, r={r}: Gamma={G:.2f} vs n/(n-1)={n/(n-1):.2f}; phi just below the cap K*: {vals[0]:+.2e}, {vals[1]:+.2e} -> laggard {'returns' if vals[0]>0 else 'falls away'}")
