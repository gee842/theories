# Numerical contact spike

This is a fixed-pose quasi-static feasibility check, using SciPy's HiGHS linear
programming solver. It checks force and moment equilibrium, declared signed
contact force/couple boxes, and optional actuator torque inequalities. It is not
a structural validator, hardware qualification, or dynamic robot controller.

## Run

From `experiments/circular-construction/demo`:

```sh
python3 -m venv numerical/.venv
numerical/.venv/bin/python -m pip install -r numerical/requirements.txt
numerical/.venv/bin/python numerical/contact_solver.py numerical/fixtures/triangle.request.json
numerical/.venv/bin/python -m unittest discover -s numerical -v
```

The current host passed the smoke test with Python 3.11.2, NumPy 2.3.3 and SciPy
1.16.2 on macOS arm64. Dependencies are pinned. The local `.venv` is disposable.
The solver also accepts a single JSON document on stdin and emits one on stdout.
Use `--output path.json` to write a result file. A valid failed/unverified model
result exits zero; malformed input exits 2 and emits an error JSON. Missing SciPy
produces `unverified`, an aggregate required-support wrench, and no feasibility
claim. No software is installed implicitly by the CLI.

## Contract v1

Coordinates are engineering Z-up, all values SI. Wrenches and limits use global
XYZ axes. Positions are relative to one declared common origin. Local contact
capacity boxes must be transformed by the caller conservatively; rotating a
box's three limits alone does not produce an equivalent global box.

```json
{
  "schema_version": 1,
  "request_id": "stance-123",
  "world_revision": 7,
  "input_fingerprint": "caller-defined-complete-input-hash",
  "gravity_m_s2": [0, 0, -9.81],
  "loads": [
    {"id": "robot", "mass_kg": 60, "position_m": [0, 0.15, 1]},
    {"id": "tool", "mass_kg": 5, "position_m": [0.4, 0.2, 1]}
  ],
  "contacts": [
    {
      "id": "dock-A",
      "position_m": [-0.5, 0, 0],
      "kind": "point",
      "force_bounds_N": {
        "lower": [-1000, -1000, -1000],
        "upper": [1000, 1000, 1000]
      }
    }
  ]
}
```

That single point contact is an illustrative input, not a feasible stance: the
offset center of mass needs a moment the contact cannot supply. See the fixtures
for complete feasible and infeasible inputs.

`loads` represents the robot, limb masses, parked or held tool, carried load
share, and externally applied reactions. Every load requires `position_m`.
`mass_kg` defaults to zero, while `force_N` and `moment_Nm` default to zero. A
load's total force is `mass × gravity + force_N`. The external moment about the
origin includes `position × total_force + moment_Nm`. Explicit `force_N` is
additional to gravity; supplying weight there as well double-counts it.

Each contact force is the **frame's force on the robot**. `point` supplies force
only: its contact couple is exactly zero. `keyed` may supply moments with
`moment_bounds_Nm: {lower: [...], upper: [...]}`. Moments do not arise by counting
attachments; they require stated keyed-clamp capacities. Finite signed lower
and upper bounds are independent for each axis. Zero limits disable an axis.
An absent bound, missing array, or `null` element is a missing capacity, relaxed
for the solve and explicitly listed in `missing_capacities`. Such an input can
never pass. If its relaxed model is still impossible, it fails.

The witness gives an admissible set of contact forces and couples, together with
their negatives as `frame_reaction_force_N` and `frame_reaction_moment_Nm` at each
contact position. Those opposite reactions must enter a separate structural
stage model. A moment about the global origin also includes the contact force's
lever arm; `frame_reaction_moment_Nm` is the local applied couple only.

Optional fixed-pose actuator rows use:

```json
{
  "require_actuator_limits": true,
  "actuator_constraints": [{
    "id": "left-shoulder",
    "gravity_torque_Nm": 3,
    "wrench_coefficients": [{
      "contact_id": "dock-A",
      "force_to_torque_m": [0, 0, 0.4],
      "moment_to_torque": [0, 0, 1]
    }],
    "lower_Nm": -50,
    "upper_Nm": 50
  }]
}
```

The torque is `gravity_torque + Σ(force_to_torque · contact_force +
moment_to_torque · contact_couple)`. Coefficients encode a supplied pose-dependent
Jacobian row and its sign convention; the solver does not derive that Jacobian.
An empty `wrench_coefficients` array represents a constant torque constraint,
used for a free limb with no contact reaction. The caller must provide every
required joint and any load gravity terms. Missing
requested rows or torque limits produce `unverified`. With no rows requested,
actuator checks remain `outside_scope` even if contact equilibrium passes.

## Result and evidence

Results echo the schema version, request ID, world revision and caller fingerprint
and add `request_sha256` for the exact canonicalized JSON plus the model version
and solver package versions. The caller must match revision and fingerprints
before committing a result; this CLI does not know the current world revision.

- `passed`: a witness satisfied equilibrium and every known required constraint
  within the reported tolerance, with no missing requested capacities.
- `failed`: HiGHS found the specified model infeasible, including an infeasible
  model after any missing bounds were relaxed.
- `unverified`: required data is missing, the numerical package is unavailable,
  the solver returned an uncertain status, or independent residual checks failed.

The LP represents each signed wrench coordinate as a difference of nonnegative
variables. It minimizes their sum with explicit normalization of 1 N and 1 N m.
This selects a reproducible low-demand witness; its wrench is **not** an optimum
hardware capacity for each grip. The result separately reports total required
support force and moment about the origin, a necessary aggregate demand rather
than proof of an achievable grasp distribution.

Every successful witness is independently checked by recomputing equilibrium,
capacity violations, and actuator torques from original contact positions and
loads. The fixed numerical acceptance tolerance is 1e-7 N and 1e-7 N m. It is
not a physical fit tolerance, load factor or certification allowance. HiGHS uses
1e-9 primal and dual feasibility tolerances. Infeasibility is a numerical solver
conclusion under this bounded linear model, not an exact rational certificate.

Tests independently derive symmetric and offset beam reactions, signed tension,
triangle force shares, joint torque, aggregate capacity failure, and the
collinear-anchor roll mechanism. The latter cannot be rescued by arbitrarily
large force capacities: three points on the x axis generate no moment about x.
A keyed fixture with declared couple capacity changes that result explicitly.

The contact box excludes coupled friction/force limits, clamp closure, compliance,
slip, deformation, dynamic loads and detailed hardware behavior. A feasible box
model is conditional on those capacities representing the hardware conservatively.
No `passed` result asserts that the robot can reach the anchors, avoid collisions,
move at a given speed, or that the supporting building can carry its reactions.

The TypeScript [fixed-pose bridge](../src/integration/contactAdapter.md) derives
24 conservative shoulder/elbow resultant rows from the robot's two-link geometry
and self-weight. Its checked three-grip standoff fixture conditionally passes;
actual beam guiding remains unverified because beam contact and loads are absent.
The Cartesian torque boxes are inner approximations to assumed norm capacities;
their infeasibility does not prove infeasibility of the original norm-bounded
robot. Wrist transmission/orientation and host-rail adequacy remain unverified.
