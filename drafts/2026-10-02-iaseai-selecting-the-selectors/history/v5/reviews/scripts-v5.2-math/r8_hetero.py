"""Heterogeneous self-models in the r=1 contest: three actors widen to theta=2.9, one keeps theta=-1."""
from r5_commitment import eq, material
n, Om, c, l = 4, 1.0, 1.0, 0.3
for ths in ([-1.0, -1.0, -1.0, -1.0], [-1.0, 2.9, 2.9, 2.9], [0.4, 2.9, 2.9, 2.9], [2.9, 2.9, 2.9, 2.9]):
    e = eq(ths, n, Om, c, l); E = sum(e)
    w = [x / E for x in e]
    print(f"thetas={ths}: total intensity {E:.4f}; win probs {[round(x,3) for x in w]}; material {[round(x,3) for x in material(e,n,Om,c,l)]}")
