#!/usr/bin/env python3
"""Compare two declared settling correspondences on the same source geometry.

This is a sensitivity analysis, not measured settling or author-code replication.
The hydrodynamic radius is an explicit proxy. Rank comparisons use exact source
decimal coordinates; absolute speeds use floating-point constants and pi.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SOURCE=ROOT/'sources/evolutionary-selection/day-2022/packing-data.zip'
VC=17.44 # Day 2022 mean cellular volume, cubic micrometers
G=9.81; RHO_CELL=1112.6; RHO_WATER=997; ETA=9.81e-4


def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records=[]; exact={}
    with zipfile.ZipFile(SOURCE) as z:
        for name in sorted(n for n in z.namelist() if '/Snowflake_SEM_positions/particles-' in n and n.endswith('.txt')):
            rows=[line.split() for line in z.read(name).decode().splitlines()]
            xyz=[[F(q) for q in row[1:]] for row in rows];n=len(xyz)
            means=[sum(row[k] for row in xyz)/n for k in range(3)]
            # The centered-squares expression uses the exact exported decimals.
            rg2=sum(sum((row[k]-means[k])**2 for k in range(3)) for row in xyz)/n
            r2=F(5,3)*rg2
            assert r2>0
            radius=math.sqrt(float(r2));envelope=4*math.pi*radius**3/3
            solid=n*VC;phi=solid/envelope
            assert 0<phi<1
            uniform=G*(2*radius*1e-6)**2*(RHO_CELL-RHO_WATER)/(18*ETA)
            material=G*(solid*1e-18)*(RHO_CELL-RHO_WATER)/(6*math.pi*ETA*radius*1e-6)
            assert math.isclose(material,phi*uniform,rel_tol=1e-12)
            tag=Path(name).stem
            rec=dict(cluster=tag,cells=n,radius_squared_um2=str(r2),radius_um=radius,
                     radius_gyration_squared_um2=str(rg2),envelope_volume_um3=envelope,
                     supplied_solid_volume_um3=solid,solid_fraction=phi,
                     uniform_cell_density_speed_mm_min=uniform*60000,
                     material_accounted_sphere_speed_mm_min=material*60000,
                     uniform_reynolds_number=RHO_WATER*uniform*2*radius*1e-6/ETA)
            records.append(rec);exact[tag]=(n,r2)
    disagreements=[]
    for a,b in itertools.combinations(records,2):
        na,ra=exact[a['cluster']];nb,rb=exact[b['cluster']]
        uniform_order=(ra>rb)-(ra<rb)
        mass_left=na**2*rb;mass_right=nb**2*ra
        material_order=(mass_left>mass_right)-(mass_left<mass_right)
        if uniform_order*material_order<0:
            disagreements.append(dict(a=a['cluster'],b=b['cluster'],uniform_a_faster=uniform_order>0,
                                      material_a_faster=material_order>0,
                                      material_squared_crossproducts=[str(mass_left),str(mass_right)]))
    fastest_uniform=sorted(records,key=lambda r:exact[r['cluster']][1],reverse=True)
    fastest_material=sorted(records,key=lambda r:F(exact[r['cluster']][0]**2)/exact[r['cluster']][1],reverse=True)
    result=dict(scope='Matched-geometry correspondence sensitivity; neither velocity law is validated for these clusters',
                code_sha256=digest(Path(__file__)),source_sha256=digest(SOURCE),
                assumptions=dict(cell_volume_um3=VC,gravity_m_s2=G,cell_density_kg_m3=RHO_CELL,
                                 water_density_kg_m3=RHO_WATER,dynamic_viscosity_Pa_s=ETA,
                                 radius='R = sqrt(5/3 * mean squared distance of cell centers from centroid)',
                                 geometry='Point centers omit intracellular inertia and are not a measured hydrodynamic radius',
                                 hydrodynamics='Shared impermeable-sphere drag, no interactions, prescribed water properties',
                                 contrast='Uniform-cell-density envelope versus accounted cell material and water-filled space',
                                 provenance='Geometries and cell-volume mean are Day 2022; constants/form of uniform approximation are from Cedeno-Perez 2026. This is not a joined lineage dataset.'),
                clusters=records,pairs_compared=len(records)*(len(records)-1)//2,
                reversed_pairs=disagreements,
                uniform_ranking=[r['cluster'] for r in fastest_uniform],
                material_ranking=[r['cluster'] for r in fastest_material],
                summary=dict(cluster_count=len(records),cells=sum(r['cells'] for r in records),
                             reversed_pair_count=len(disagreements),
                             solid_fraction_range=[min(r['solid_fraction'] for r in records),max(r['solid_fraction'] for r in records)],
                             uniform_speed_range_mm_min=[min(r['uniform_cell_density_speed_mm_min'] for r in records),max(r['uniform_cell_density_speed_mm_min'] for r in records)],
                             material_speed_range_mm_min=[min(r['material_accounted_sphere_speed_mm_min'] for r in records),max(r['material_accounted_sphere_speed_mm_min'] for r in records)],
                             maximum_uniform_reynolds_number=max(r['uniform_reynolds_number'] for r in records)),
                limitations=['No observed settling velocities, fitness estimates or selection coefficients are produced.',
                             'Permeability, nonsphericity and interactions may change the drag and predicted ordering.',
                             'The two formulae are conventional approximations; disagreement does not demonstrate superiority of our theory.',
                             'Small Reynolds numbers do not validate the radius or impermeable-drag correspondence.',
                             'No arbitrary rescaling is chosen to resolve the earlier Coulter conversion discrepancy.'])
    (HERE/'settling-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],indent=2));print('First reversed pair:',disagreements[0] if disagreements else None)


if __name__=='__main__':main()
