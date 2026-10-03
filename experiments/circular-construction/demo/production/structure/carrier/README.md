# Structural feedback for the carrier construction kit

This study evaluates the current main scene's source inventory at completed-storey snapshots. It is a conditional elastic/P–Delta response study, not structural qualification. It has no soil qualification, connection strength/stiffness proof, partial-bay erection acceptance or finite-contact robot/frame coupling.

The exporter executes the actual construction planner and records its parts, positions, installation times, catalogue revision and source dependency hashes. `member_graph.py` derives column, beam and brace connection lines from those parts. Removed stair-bay beams stay absent; delivered headers and landing trimmers become real members. A header endpoint splits its supporting beam or column into analysis segments without creating another physical part. Every segment retains the source part ID.

Visible beam-seat offsets are projected to the nearest half-storey connection datum. The resulting intersections assume rigid connections, including the proposed mid-level column saddles. Their eccentricity, slip, rotational behavior and local attachment strength are not established by this model. Stairs, partitions and floors provide mass but no hidden core or diaphragm stiffness. Catalogue mass is lumped at main frame nodes, so the study does not establish local floor or landing capacity.

## Reproduce

From the demo directory:

```sh
node scripts/exportConstructionPlan.mjs
python3 production/structure/carrier/test_member_graph.py
numerical/.venv/bin/python production/structure/carrier/analyze.py
```

The analysis rejects an export whose recorded source dependencies or shared contract have changed. Results retain both the planning and analysis source hashes. Re-export after changing the kit, routes or assembly schedule; a result remains specific to its recorded revision.

## Interpreting the cases

The baseline uses only the visible frame and braces, assumed fixed pile-head nodes, assumed rigid joints, catalogue dead mass, a declared 3 kPa floor-load probe and four loaded carriers plus four assemblers at the workfront. Simultaneous positive and negative 0.5 kPa pressure probes in both principal directions explore sensitivity; they are not site- or code-selected design loads. Completed-storey snapshots are evaluated at 1, 2, 5, 10 and 20 storeys. Cladding mass follows the recorded installation sequence.

The current single-diagonal layout develops brace compression greater than its ideal pinned Euler screen under reverse loading and substantial lateral displacement. Elastic compression stiffness retained beyond that screen does not make the structure adequate. Solver convergence is reported separately from capacity and stability concerns.

`candidateCrossBraces` is a deliberately separate alternative with additional paired bracing in both axes and negligible compression stiffness. Those added braces are **not in the baseline viewer inventory** and their response must not be presented as the visible building's result. Any selected revision needs matching parts, joints, handling masses, installation tasks and structural checks before integration. A larger-section alternative discussed during design is also unqualified and is not silently substituted here.

The graph tests check absent members and actual header/column connectivity. They do not test structural adequacy. The next engineering steps are a revised visible lateral system, actual connection and member capacity checks, support throughout partial-bay erection, and reaction histories from the accepted robot/load model.
