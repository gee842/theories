"""Extra robustness cases for s2_mpe (r<1, sharing, shared loss, patience, grid)."""
import s2_mpe
th=lambda L: -L/(2+L)
cases=[dict(r=0.5,Gamma=0.45,d=0.2),dict(r=0.5,Gamma=0.45,d=0.05),dict(r=1.5,Gamma=0.6,d=0.2,beta=0.5),dict(r=1.5,Gamma=0.6,d=0.2,l=0.5),
       dict(r=1.5,Gamma=0.6,d=0.2,delta=0.5),dict(r=1.5,Gamma=0.6,d=0.2,delta=0.97),dict(r=1.5,Gamma=0.6,d=0.2,N=1600)]
for kw in cases:
    r=kw.pop('r'); G=kw.pop('Gamma')
    res=s2_mpe.run(r,G,**kw)
    print(f"r={r} Gamma={G} {kw}: Gd={res['Gd']:.3f} lambda formula {res['lam']:.4f} fixed {res['lam_fixed']:.4f} MPE {res['lam_mpe']:.4f} ratio {res['lam_mpe']/res['lam']:.3f} | theta_G {th(res['lam']):+.3f} theta_MPE {th(res['lam_mpe']):+.3f} | de2/ds {res['de2']:+.3f} | conv {res['conv'][0]}")
