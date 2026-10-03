# Growing steel-frame equilibrium study

This is an executable **OpenSeesPy 3.8.0 concept study**, not an engineered tower design or a construction authorization. It analyses independent 11-, 12-, and 20-storey partial-height models of the 36 × 24 m tower on the 6 m grid, at 3.6 m per storey. `results.json` and `public/assets/tower-structure.json` contain the same machine-readable results.

From the demo directory, reproduce the export and run its eight checks:

```sh
cd /Users/ren/theories/experiments/circular-construction/demo
numerical/.venv/bin/python production/structure/opensees/analyze.py --public
numerical/.venv/bin/python -m unittest discover -s production/structure/opensees -p 'test_*.py' -v
```

The missing-seat analysis deliberately emits an OpenSees convergence warning. It is an expected negative result; the process still returns zero when the export completes. Python dependencies are the existing numerical virtual environment and `openseespy` with an OpenSees 3.8.0 binary. `--output PATH` redirects the source export, and `--public` also updates the public asset.

## Model and load path

Each floor has 35 six-degree-of-freedom nodes, actual three-dimensional elastic beam-column elements, fixed foundation nodes, and explicit perimeter X bracing. I-section area, both second moments, Saint-Venant torsional constant, E and G are calculated from the Blender dimensions. Column profiles change above storey ten. The thin-wall open-section formula approximates J and excludes warping. Members span node centrelines; visual end setbacks, splice plates and joint offsets are not modelled. Beam-column joints are assumed rigid. These assumptions require engineered verification before any real application.

Horizontal members use local z vertically, so Iy is their strong-axis inertia. Columns use local z along global Y, matching the source extrusion. The nominal frame includes **assumed temporary Y-plane X braces on both X faces**; these are required modelling additions to the visual structure. Braces use the visible 52 mm solid circular radius, elastic axial stiffness and geometric corotational transformation. Compression buckling and connection capacity are not evaluated. The visible concrete core has **no stiffness, mass or gravity in this steel-frame subsystem model**. Consequently the results are not a calculation of the complete depicted building.

Gravity includes steel member self-weight, assumed deck dead load of 2.25 kPa and construction live load of 0.75 kPa. Deck areas distribute their load to four corner nodes. Member self-weight also distributes to end nodes; local bending under distributed floor/member gravity is therefore excluded from the tower analysis. This is useful for global axial and lateral load-path response, but cannot establish beam gravity capacity. The two floor-12 openings remain unloaded. Above floor twelve, the 20-storey scenario assumes future decks, although those decks are not present in the current construction visual.

The floor-12 active bay is omitted from the moment frame. The beam has no frame-stiffness credit before fastening. Measured final MuJoCo seat reactions (approximately 3132.15 N each) transfer to the two adjacent floor-12 column nodes with their ±0.2 m eccentric moments. The 137 kg robot transfers to the x=6, y=-12 column with its 0.6 m eccentric gravity moment. These quantities come from `production/physics/mujoco/nominal-validation.json`; its SHA-256 hash is recorded. The model does not transfer time-varying limb/rail loads or crane forces. The two engines are coupled through this static load extraction, not through a simultaneous solve.

Gravity ramps through ten steps and is held constant. A second pattern ramps the beam/robot loads and a **0.5 kPa horizontal pressure probe in both axes simultaneously**, distributed by floor projected area. The probe is an assumed comparison load, not a site wind design or code combination. Frame P-Delta transformations represent second-order effects; material response stays elastic. Each height is rebuilt from zero independently: these are staged equilibrium snapshots, not stress-free member activation, carried construction history, creep or shrinkage.

## Independent checks and negative cases

The checks require converged stage equilibria, global force balance, correct introduction of floor-12 loads, positive three-dimensional section stiffnesses, consistent beam mass across engines, and agreement of a separate beam model with an analytical benchmark. The local active beam is a 5.6 m pin/roller-supported I450 × 300 beam with a 9 mm web and 18 mm flanges, discretized into ten elements. Its area is 0.014526 m²; at 7850 kg/m³ the bare section weighs 638.56296 kg, matching the imported MuJoCo beam mass. An export gate requires agreement within a relative tolerance of 1e-10, and a negative test verifies rejection of a mismatched mass. This idealization omits additional connection hardware mass and local hardware stresses. Its uniform-load midspan deflection is checked against `5 w L^4 / (384 E Iy)`; the two support reactions are checked against half its weight and the MuJoCo values.

The **missing east-face temporary brace system** case removes 48 diagonal truss members at the 12-storey stage. It still has rigid-joint frame action and west-face bracing, so it need not become a mechanism; the test requires a meaningful increase in roof displacement. Removing the whole system also removes its self-weight, as appropriate to an omitted construction component. This case is distinct from failure of one individual brace.

The **missing right beam seat** case releases the right vertical support. The left pin then admits a rigid-body rotation about global Y. Gravity performs nonzero virtual work in that mode, producing an unbalanced `weight × span / 2` moment. This establishes the mechanism independently of platform-specific sparse-solver behavior. Any resulting numerical displacements are suppressed instead of being presented as physical results. It does not model impact after support loss or restraint from partially installed fasteners.

## Reproduced results

With the corrected active I450 × 300 × 9 × 18 mm section, the local beam deflects **0.128494 mm** at midspan, with **3132.151319 N** at each seat. Its analytical deflection relative error is 4.64e-15 and its section-derived/imported mass relative difference is 1.78e-16. All eight checks pass. The active beam contributes only its unchanged seat loads to the tower, so the tower equilibria remain unchanged:

| Storeys | Roof maximum horizontal displacement | Maximum resultant storey drift ratio |
| --- | ---: | ---: |
| 11 | 14.810 mm | 0.00061523 |
| 12 | 17.422 mm | 0.00066573 |
| 20 | 46.804 mm | 0.00106721 |

The largest relative force-balance residual is 1.69e-14. Omitting the east-face temporary brace system increases the 12-storey roof displacement by 10.65%, to 19.277 mm. The missing-seat negative returns solver code −3 and has an unbalanced gravity moment of 17.540 kN·m. These are response results for the stated assumptions, without engineering acceptance thresholds.

JSON floor profiles provide mean horizontal translation, maximum horizontal displacement, minimum vertical displacement and maximum resultant interstorey drift. Base reactions, applied forces, balance residuals, brace-force ranges and all solver codes are retained. A successful solver status means equilibrium under the stated assumptions; it is not a member-capacity, stability or serviceability pass. The study excludes yielding, lateral-torsional/local buckling, brace buckling, joint slip and flexibility, bolt preload, diaphragm behavior, foundation/soil response, seismic effects, dynamic wind, crane interaction, and construction sequence stability certification.

Element and transformation references: [OpenSees 3D elastic beam-column](https://opensees.github.io/OpenSeesDocumentation/user/manual/model/elements/elasticBeamColumn.html), [OpenSees P-Delta transformation](https://openseesdocumentation.readthedocs.io/en/latest/user/manual/model/geomTransf/PDelta.html).
