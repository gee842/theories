# Loaded locomotion for the construction carrier

This local MuJoCo action uses the new construction kit's 320 kg carrier and 92.928 kg beam. The measured run advances 3.2 m through 40 guarded grip transfers in 272.558 s. Its highest rail reaction is 5.20 kN; at least three grips carry positive upward force throughout. The 3,000 Nm shoulder / 2,000 Nm elbow bounds are conceptual hardware inputs, not qualified actuator ratings.

The robot shares the Blender contract's 0.65 m links, hip positions, cradle offset and masses. Its two rows of grips align to the column's 0.32 m saddle pitch. Two installed column segments are needed to reach every support in this local action; the clip cannot climb above the actual installed frame. A rigid coordinate transform may position the whole fixture in a site, but a different route, payload, joint, frame deformation or support arrangement needs new analysis.

The captive beam and engaged rail grips use idealized restraints. The beam contributes mass and inertia to the free robot and is raised through bounded motor torque; it is not moved by prescribing root positions. The grips remain ideal force constraints. Finite jaw contact, wrist alignment, frame/robot collision, payload pickup and supported handoff are **not** demonstrated. The updated Blender jaw contact is offset from the ideal wrist constraint, so the recorded hinge motion is not evidence that the modeled jaws physically engage. The full-site planning viewer also remains authored motion until its corresponding actions are integrated and verified.

A displaced receiver makes this controller reject capture, return to the old receiver and retain the beam. This is one explicit recovery case, not general fault tolerance.

## Load feedback into the kit

The same beam-shaped ballast with 327.858 kg mass (the column kit's mass) fails the first capture and exceeds the proposed 16 kN grip limit. This is a mass-sensitivity result, **not a simulation of the column's actual geometry**. A 139.542 kg and a 177.5 kg ballast each finish one step but temporarily lose the conservative three-positive-upward-support condition. These do not establish qualified floor or column handling. The proposed 350 kg robot capacity therefore remains unproven; reducing part size, revising support/load distribution and qualifying the actual gripper are active design work.

## Reproduce

From `demo`:

```sh
numerical/.venv/bin/python production/physics/carrier/simulate.py --public
numerical/.venv/bin/python production/physics/carrier/simulate.py --scenario missed-grip --cycles 1
numerical/.venv/bin/python production/physics/carrier/simulate.py --payload-kg 327.858 --cycles 1
numerical/.venv/bin/python production/physics/carrier/test_carrier.py
```

The runner checks shared contract geometry before integrating. It reuses the existing guarded climbing controller with explicit, slower gains and action durations. `*-metrics.json` records every-step extrema, support events, motor/constraint work and source hashes; `*-trace.json` contains measured poses and joints. The public export is `public/assets/carrier-loaded-trace.json`. Local metrics are not a whole-building physics certificate.

MuJoCo's [equality constraint semantics](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-connect) explain the ideal point constraints used here. [The shared kit](../../contracts/carrier-construction.json) and [asset sources](../../blender/CARRIER-ASSETS.md) define the currently modeled geometry.
