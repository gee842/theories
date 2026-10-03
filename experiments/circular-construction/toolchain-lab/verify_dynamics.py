"""Executable integration checks, not a construction robot qualification.

Mink owns a separate reference configuration. Only mj_step advances the real
MuJoCo state after initialization; motor forces are bounded by the model.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mink
import mujoco
import numpy as np

HERE = Path(__file__).resolve().parent
DT = 0.001
CONTROL_DT = 0.01
JOINTS = ("yaw", "shoulder", "elbow")
TORQUES = np.array([120.0, 120.0, 80.0])


def arm_xml(payload: float, dt: float = DT) -> str:
    return f'''<mujoco model="Bounded actuator and inverse kinematics integration fixture">
      <compiler angle="radian" autolimits="true"/>
      <option timestep="{dt}" gravity="0 0 -9.81" integrator="implicitfast"
              solver="Newton" iterations="80" tolerance="1e-10"/>
      <default>
        <joint damping="2" armature="0.08"/>
        <geom friction="0.6 0.01 0.001" solref="0.008 1" rgba="0.8 0.45 0.12 1"/>
      </default>
      <worldbody>
        <geom name="floor" type="plane" size="3 3 .1" rgba=".15 .18 .21 1"/>
        <geom name="pedestal" type="box" pos="0 0 .56" size=".12 .12 .56"/>
        <body name="yaw_body" pos="0 0 1.2">
          <joint name="yaw" axis="0 0 1" range="-2.5 2.5"/>
          <geom name="yaw_housing" type="sphere" size=".07" mass="4"/>
          <body name="upper" pos="0 0 0">
            <joint name="shoulder" axis="0 1 0" range="-1.7 1.4"/>
            <geom name="upper_link" type="capsule" fromto="0 0 0 .55 0 0" size=".045" mass="4"/>
            <body name="forearm" pos=".55 0 0">
              <joint name="elbow" axis="0 1 0" range=".05 2.7"/>
              <geom name="forearm_link" type="capsule" fromto="0 0 0 .45 0 0" size=".035" mass="3"/>
              <body name="tool" pos=".45 0 0">
                <geom name="payload_fixture" type="box" size=".055 .065 .065" mass="{payload}" rgba=".18 .23 .27 1"/>
                <site name="tcp" size=".012"/>
              </body>
            </body>
          </body>
        </body>
      </worldbody>
      <actuator>
        <motor name="yaw_motor" joint="yaw" ctrlrange="-120 120" forcerange="-120 120"/>
        <motor name="shoulder_motor" joint="shoulder" ctrlrange="-120 120" forcerange="-120 120"/>
        <motor name="elbow_motor" joint="elbow" ctrlrange="-80 80" forcerange="-80 80"/>
      </actuator>
    </mujoco>'''


def run_arm(payload: float, dt: float = DT, solver: str = "daqp") -> dict:
    model = mujoco.MjModel.from_xml_string(arm_xml(payload, dt))
    data = mujoco.MjData(model)
    data.qpos[:] = [0, -.65, 1.25]  # Initial condition only.
    mujoco.mj_forward(model, data)
    initial_q = data.qpos.copy()
    configuration = mink.Configuration(model, q=initial_q.copy())
    task = mink.FrameTask("tcp", "site", position_cost=1., orientation_cost=0., lm_damping=1.)
    posture = mink.PostureTask(model, cost=1e-4)
    posture.set_target(initial_q)
    limits = [mink.ConfigurationLimit(model),
              mink.VelocityLimit(model, {name: .5 for name in JOINTS})]
    tcp = model.site("tcp").id
    start = data.site_xpos[tcp].copy()
    finish = start + np.array([-.12, .15, .12])
    velocity = np.zeros(model.nv)
    interval = round(CONTROL_DT/dt)
    samples, peak_torque, saturation_steps = [], np.zeros(model.nu), 0
    peak_velocity = 0.
    peak_joint_violation = 0.
    for step in range(round(6/dt)):
        if step % interval == 0:
            u = float(np.clip(data.time/3, 0, 1))
            target = start + (finish-start)*(3*u*u-2*u*u*u)
            task.set_target(mink.SE3.from_rotation_and_translation(mink.SO3.identity(), target))
            # This is an independent planning state, never copied to data.qpos.
            velocity = mink.solve_ik(configuration, [task, posture], CONTROL_DT,
                                     solver=solver, limits=limits, safety_break=True)
            configuration.integrate_inplace(velocity, CONTROL_DT)
        desired = (np.array([600., 900., 650.])*(configuration.q-data.qpos)
                   + np.array([65., 95., 70.])*(velocity-data.qvel)
                   + data.qfrc_bias)
        data.ctrl[:] = np.clip(desired, -TORQUES, TORQUES)
        mujoco.mj_step(model, data)
        # Refresh derived body/site poses to correspond exactly to this qpos.
        mujoco.mj_forward(model, data)
        peak_torque = np.maximum(peak_torque, np.abs(data.actuator_force))
        peak_velocity = max(peak_velocity, float(np.max(np.abs(data.qvel))))
        peak_joint_violation = max(peak_joint_violation,
                                   float(np.max(model.jnt_range[:,0]-data.qpos)),
                                   float(np.max(data.qpos-model.jnt_range[:,1])))
        saturation_steps += int(np.any(np.abs(desired) > TORQUES))
        if not np.all(np.isfinite(data.qpos)):
            raise AssertionError("Nonfinite dynamic state")
        if step % round(.02/dt) == 0:
            samples.append({"time": float(data.time), "q": data.qpos.tolist(),
                            "referenceQ": configuration.q.tolist(),
                            "tcp": data.site_xpos[tcp].tolist(),
                            "target": target.tolist(), "torqueNm": data.actuator_force.tolist(),
                            "bodies": {model.body(i).name: {"position": data.xpos[i].tolist(),
                                       "quaternionWxyz": data.xquat[i].tolist()}
                                       for i in range(1, model.nbody)}})
    return {"payloadKg": payload, "dt": dt, "ikSolver": solver,
            "finalErrorM": float(np.linalg.norm(data.site_xpos[tcp]-finish)),
            "finalTcpM": data.site_xpos[tcp].tolist(),
            "peakMotorTorqueNm": peak_torque.tolist(), "motorLimitsNm": TORQUES.tolist(),
            "peakJointVelocityRadS": peak_velocity,
            "saturationFraction": saturation_steps/round(6/dt),
            "maxJointLimitViolationRad": peak_joint_violation,
            "warningCount": int(sum(w.number for w in data.warning)),
            "frames": samples}


def contact_check(dt: float = DT) -> dict:
    xml = f'''<mujoco><option timestep="{dt}" gravity="0 0 -9.81" integrator="implicitfast"/>
      <default><geom solref=".002 1" solimp=".999 .999 .0001"/></default>
      <worldbody><geom name="seat" type="plane" size="2 2 .1"/>
        <body pos="0 0 .3"><freejoint/>
          <geom name="load" type="box" size=".15 .12 .1" mass="25"/>
        </body></worldbody></mujoco>'''
    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)
    forces, penetration, max_contacts = [], 0., 0
    for _ in range(round(2/dt)):
        mujoco.mj_step(model, data)
        total = 0.
        max_contacts = max(max_contacts, data.ncon)
        for i in range(data.ncon):
            force = np.zeros(6)
            mujoco.mj_contactForce(model, data, i, force)
            world_force = data.contact[i].frame.reshape(3, 3).T @ force[:3]
            total += float(world_force[2])
            penetration = max(penetration, -float(data.contact[i].dist))
        if data.time > 1.5:
            forces.append(total)
    return {"meanVerticalSupportN": float(np.mean(forces)), "expectedWeightN": 25*9.81,
            "peakPenetrationM": penetration, "maxContacts": max_contacts,
            "finalCenterHeightM": float(data.qpos[2]),
            "warningCount": int(sum(w.number for w in data.warning))}


def verify(output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    nominal = run_arm(3.)
    overloaded = run_arm(40.)
    finer = run_arm(3., dt=.0005)
    repeated = run_arm(3.)
    alternative = run_arm(3., solver="osqp")
    contact = contact_check()
    checks = {
        "nominal_tracks_within_3mm": nominal["finalErrorM"] < .003,
        "overload_cannot_fake_success": overloaded["finalErrorM"] > .10,
        "overload_saturates_motors": overloaded["saturationFraction"] > .10,
        "torque_bounds": all(np.all(np.array(r["peakMotorTorqueNm"]) <= TORQUES+1e-9)
                             for r in (nominal, overloaded, finer, alternative)),
        "finite_no_solver_warnings": all(r["warningCount"] == 0
                                          for r in (nominal, overloaded, finer, contact, alternative)),
        "timestep_final_position_agreement_1mm": float(np.linalg.norm(np.array(nominal["finalTcpM"])-finer["finalTcpM"])) < .001,
        "nominal_joint_velocity_under_limit": nominal["peakJointVelocityRadS"] <= .5,
        "nominal_joint_limits": nominal["maxJointLimitViolationRad"] < .001,
        "deterministic_repeat": nominal == repeated,
        "osqp_tracks_within_3mm": alternative["finalErrorM"] < .003,
        "contact_supports_weight": abs(contact["meanVerticalSupportN"]-contact["expectedWeightN"]) < 1.,
        "contact_penetration_under_2mm": contact["peakPenetrationM"] < .002,
    }
    report = {"status": "passed" if all(checks.values()) else "failed", "checks": checks,
              "nominal": {k:v for k,v in nominal.items() if k != "frames"},
              "overload": {k:v for k,v in overloaded.items() if k != "frames"},
              "halfTimestep": {k:v for k,v in finer.items() if k != "frames"},
              "contact": contact,
              "scope": "Fixed-base three-joint toolchain fixture; no climbing, grasp, connection or tower qualification."}
    for name, result in [("nominal", nominal), ("overload", overloaded)]:
        (output/f"{name}-trace.json").write_text(json.dumps(result))
        (output/f"{name}.xml").write_text(arm_xml(result["payloadKg"]))
    (output/"dynamics-report.json").write_text(json.dumps(report, indent=2)+"\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE/"output")
    args = parser.parse_args()
    result = verify(args.output)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "passed" else 1)
