# Fixed-pose contact bridge

`createContactRequest(state, options)` converts one checked, motionless `RobotState`
into Python solver schema v1 JSON. Adapter context version `robot-fixed-pose/2`
includes conservative shoulder/elbow resultant moment rows for **self-weight**.
It includes body mass, four uniform upper links, four uniform forearms, four
clamps at their wrists, and one tool at its carried wrist or body dock. All
`load_verified` anchors become contacts. Each global contact force/couple box is
`±limit/√3`, conservatively inside the declared Euclidean magnitude limit.
The fixture's capacities are **assumptions**, not qualified hardware capacities.

For a joint at `q`, wrist at `w`, frame-on-robot contact force `F`, and contact
couple `M`, moment balance of the distal limb gives

```
T(q) = (w − q) × F + M + Σ ((massPoint − q) × mass × gravity)
```

The shoulder sum includes its upper link midpoint, forearm midpoint, clamp, and
carried tool. The elbow sum excludes the upper link. Body mass and a docked tool
act upstream of the joints: they enter whole-robot force/moment equilibrium and
therefore the required contact reactions, without being double-counted in distal
gravity. A tool on a supporting limb is included just as on a free limb.
The motor reaction is `−T`; the symmetric bounds make that sign immaterial.

For each joint and global unit axis `e`, the LP row uses force coefficients
`e × (w − q)`, couple coefficients `e`, and the gravity component `e · Tg`.
Three rows bounded by `±torqueLimit/√3` ensure `||T||₂ ≤ torqueLimit`, since the
sum of their squared bounds is the squared limit. The elbow's full resultant
moment is a conservative upper bound on its hinge-axis projection. This is a
conservative resultant-capacity interpretation of the existing scalar limits;
it is not a motor/transmission or bearing qualification. There are 24 rows:
four limbs × two joints × three axes. Free limbs have empty wrench coefficients
and constant gravity rows, so support redistribution cannot rescue an overloaded
free tool arm. Null limits remain missing capacities and cannot produce a pass.

These inner boxes can reject a pose that fits the original spherical limits.
A `fail` establishes infeasibility of the declared conservative box model, not
physical impossibility of the robot. The separate collinear point-contact
mechanism also fails with unbounded force capacity, independently of these
conservative approximations.

The builder requires callers to declare external-load completeness. Positions
of arbitrary additional loads do not identify which robot member receives them.
If `externalLoads` is nonempty, the adapter sends no joint rows, records
`actuator_rows: missing-external-load-attachment`, and keeps actuator feasibility
unverified. This avoids both omitting opposing joint loads and falsely rejecting
loads that would assist a joint. Extending this needs explicit member attachment
and distal-chain ownership, not guessed Jacobians. Contact equilibrium can still
be checked. Incomplete loads keep the overall assessment unverified even when
the supplied subset is feasible or infeasible.

`assessContactResult(issuedRequest, solverResult, currentRequest)` requires a
fresh request from the current pose/world revision. It checks both fingerprints,
IDs, revision, solver model version, and Python canonical request SHA-256.
Changed geometry, masses, torque rows, bounds, custody, or load scope invalidates
old evidence. A local conditional `pass` additionally requires complete loads,
the self-weight actuator model, included actuator constraints, no missing
capacities, a feasible solver status, and residual/bound errors within 1e-7.
A passed label alone is insufficient. `pass` concerns this fixed-pose model only.

Run from the demo directory:

```sh
node scripts/contactBridge.mjs
node scripts/contactBridge.mjs --write-fixtures
```

The runner derives a real fixture-A guide pose from `RobotTaskTrace` at its event
end and `worldAtTime(...).revision`. Its tool stops **0.25 m short of the beam**.
The recorded three-keyed-grip, 14-mass-point self-weight case conditionally
passes with all 24 actuator rows. A separate request for **actual beam guiding**
explicitly marks interaction loads incomplete: the raw solver passes its
self-weight subset, but the adapter assessment remains **unverified**. This
neither closes the standoff nor verifies guidance. Two collinear point-grip
cases retain their failed equilibrium result, including relaxed force limits.

The runner prefers `CONTACT_PYTHON`, then the local numerical venv, then
`python3`. Missing SciPy/Python or malformed output stays unverified. Recorded
fixtures require expected solver outcomes. Tests compare row coefficients with
independently expanded moment balance, cover tool custody and free-arm overload,
and reject stale or incomplete numerical evidence.

Wrist orientation/torque, clamp closure, friction/slip, dynamic motion, host rail
and bracket capacity, frame reactions, and beam/tool interaction remain
unverified. These results do not commit a beam transaction or certify hardware.
