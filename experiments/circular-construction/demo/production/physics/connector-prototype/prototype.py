"""Isolated contact-only pin/dog experiment. Does not modify production assets."""
from pathlib import Path
import argparse
import json
import math
import mujoco
import numpy as np

HERE = Path(__file__).resolve().parent


def model_xml(offset=0.0, timestep=0.0005):
    # Convex annular sectors preserve an open bore: a single concave mesh would
    # be convex-hulled by MuJoCo and fill the hole. Radii match the Blender hole.
    assets = []
    for kind, thick in [('beam', .03), ('bracket', .02)]:
        for i in range(16):
            a, b = 2*math.pi*i/16, 2*math.pi*(i+1)/16
            vertices = [(x, r*math.cos(t), r*math.sin(t))
                        for x in [-thick/2, thick/2]
                        for r, t in [(.024,a),(.060,a),(.060,b),(.024,b)]]
            assets.append(f'<mesh name="{kind}_{i}" vertex="' + ' '.join(str(v) for p in vertices for v in p) + '"/>')
    def ring(kind, x, y, z):
        return ''.join(f'<geom name="{kind}_bore_{i}" type="mesh" mesh="{kind}_{i}" pos="{x} {y} {z}" density="7850" rgba=".5 .6 .7 1"/>' for i in range(16))
    return f'''<mujoco model="isolated pin and spring dog retention prototype">
      <compiler angle="radian" autolimits="true"/>
      <option timestep="{timestep}" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10"/>
      <visual><headlight diffuse=".8 .8 .8" ambient=".3 .3 .3"/></visual>
      <default><geom friction="0 0 0" condim="1" solref=".003 1" solimp=".99 .999 .0001"/><joint damping="3"/></default>
      <asset>{''.join(assets)}</asset>
      <worldbody>
        <light pos="-.5 -1 2"/>
        <camera name="connector" pos="-.4 -.55 .65" xyaxes=".8 -.6 0 .3 .4 .866"/>
        <geom name="seat_left" type="box" pos="0 0 -.06" size=".25 .32 .06"/>
        <geom name="seat_right" type="box" pos="5.6 0 -.06" size=".25 .32 .06"/>
        <body name="support_bracket">{ring('bracket',-.03,.085,.3375)}</body>
        <body name="beam" pos="2.8 {offset} .225">
          <freejoint name="beam_free"/>
          <geom name="bottom_flange" type="box" pos="0 0 -.216" size="2.8 .15 .009" density="7850" rgba=".9 .4 .05 1"/>
          <geom name="web" type="box" size="2.8 .0045 .207" density="7850" rgba=".9 .4 .05 1"/>
          <geom name="top_flange" type="box" pos="0 0 .216" size="2.8 .15 .009" density="7850" rgba=".9 .4 .05 1"/>
          {ring('beam',-2.785,.085,.1125)}
        </body>
        <body name="pin" pos="-.105 .085 .3375">
          <joint name="insertion" type="slide" axis="1 0 0" limited="false" damping="6"/>
          <geom name="pin_shaft" type="cylinder" pos="-.0075 0 0" size=".012 .0425" quat=".7071067811865476 0 .7071067811865475 0" mass=".4" rgba=".8 .8 .85 1"/>
          <geom name="pin_nose" type="cylinder" pos=".0475 0 0" size=".012 .0025" quat=".7071067811865476 0 .7071067811865475 0" mass=".03" rgba=".8 .8 .85 1"/>
          <geom name="pin_slot_top" type="box" pos=".04 0 .010" size=".005 .006 .002" mass=".01" rgba=".8 .8 .85 1"/>
          <geom name="pin_slot_bottom" type="box" pos=".04 0 -.010" size=".005 .006 .002" mass=".01" rgba=".8 .8 .85 1"/>
          <geom name="pin_head" type="box" pos="-.055 0 0" size=".006 .036 .026" mass=".15" rgba=".3 .4 .5 1"/>
          <body name="retention_dog" pos=".04 .006 0">
            <joint name="dog_extension" type="slide" axis="0 1 0" range="0 .03" stiffness="1000" springref=".03" damping="5" solreflimit=".002 1" solimplimit=".9999 .9999 .0001"/>
            <geom name="dog" type="box" size=".005 .006 .007" mass=".08" rgba=".9 .75 .1 1"/>
          </body>
          <body name="retention_dog_opposite" pos=".04 -.006 0">
            <joint name="dog_extension_opposite" type="slide" axis="0 -1 0" range="0 .03" stiffness="1000" springref=".03" damping="5" solreflimit=".002 1" solimplimit=".9999 .9999 .0001"/>
            <geom name="dog_opposite" type="box" size=".005 .006 .007" mass=".08" rgba=".9 .75 .1 1"/>
          </body>
        </body>
      </worldbody>
      <actuator>
        <motor name="insertion_motor" joint="insertion" ctrlrange="-500 500" forcerange="-500 500"/>
        <motor name="dog_retractor" joint="dog_extension" ctrlrange="-100 100" forcerange="-100 100"/>
        <motor name="dog_retractor_opposite" joint="dog_extension_opposite" ctrlrange="-100 100" forcerange="-100 100"/>
      </actuator>
    </mujoco>'''


def run(scenario='nominal', timestep=.0005, duration=5.0, save=False, render=False):
    offset = .025 if scenario == 'misaligned' else 0.
    xml = model_xml(offset, timestep)
    m = mujoco.MjModel.from_xml_string(xml)
    d = mujoco.MjData(m)
    mujoco.mj_forward(m, d)
    pinj = m.joint('insertion').id
    dogj = m.joint('dog_extension').id
    pq, pv = m.jnt_qposadr[pinj], m.jnt_dofadr[pinj]
    dq, dv = m.jnt_qposadr[dogj], m.jnt_dofadr[dogj]
    oq = m.jnt_qposadr[m.joint('dog_extension_opposite').id]
    ov = m.jnt_dofadr[m.joint('dog_extension_opposite').id]
    beam = m.body('beam').id
    beamq = m.jnt_qposadr[m.joint('beam_free').id]
    rows, events = [], []
    max_pen = 0.
    peak_insert_force = 0.
    peak_block_force = 0.
    cleared = False
    aborted = False
    retained_contacts = []
    retained_samples = 0
    blocked_since = None
    for step in range(round(duration/timestep)):
        t = d.time
        # All motion after initialization is integrated, with bounded forces.
        target = .114 * np.clip((t-.2)/1.2, 0, 1)
        d.ctrl[0] = np.clip(8000*(target-d.qpos[pq])-90*d.qvel[pv], -500, 500) if t < 2 else 0
        if aborted:
            d.ctrl[0] = np.clip(8000*(0-d.qpos[pq])-90*d.qvel[pv], -100, 100)
        # A passive outward spring is held retracted until the dog's back face
        # has cleared the actual far plate face. No equality is ever enabled.
        beam_far_x = d.xpos[beam,0]-2.77
        dog_back_x = d.xpos[m.body('retention_dog').id,0]-.005
        if not cleared and dog_back_x > beam_far_x+.002 and not aborted:
            cleared = True
            events.append({'time':round(t,6), 'event':'dog physically clear of beam rear face; release retractor'})
        deploy = cleared and scenario != 'no-latch'
        d.ctrl[1] = 0 if deploy else np.clip(-30-2000*d.qpos[dq]-15*d.qvel[dv], -100, 100)
        d.ctrl[2] = 0 if deploy else np.clip(-30-2000*d.qpos[oq]-15*d.qvel[ov], -100, 100)
        if t >= 1.8 and not cleared and not aborted:
            aborted = True
            events.append({'time':round(t,6), 'event':'insertion timeout; retract; retention and proof-load stages inhibited'})
        # Seat friction is exactly zero. Axial retention cannot come from seats.
        load = 2000*np.clip((t-2.5)/.5, 0, 1) if cleared and not aborted else 0
        if t >= 3.0 and scenario == 'pullout':
            load = 0
        d.xfrc_applied[beam,:] = 0
        d.xfrc_applied[beam,0] = load
        # Apply proof load on the bore axis, so this isolates axial retention.
        # A single pin is not claimed to restrain every beam rotation.
        load_point = np.array([d.xipos[beam,0], .085, .3375])
        d.xfrc_applied[beam,3:] = np.cross(load_point-d.xipos[beam], np.array([load,0.,0.]))
        if t >= 3.0 and scenario == 'pullout' and cleared:
            d.xfrc_applied[beam,0] = 0
            d.ctrl[0] = -250
        mujoco.mj_step(m,d)
        mujoco.mj_forward(m,d)
        contacts = []
        insertion_contact_n = 0
        for ci, c in enumerate(d.contact):
            force = np.zeros(6)
            mujoco.mj_contactForce(m,d,ci,force)
            a, b = m.geom(c.geom1).name, m.geom(c.geom2).name
            max_pen = max(max_pen, max(0,-float(c.dist)))
            if force[0] > 1e-3:
                world_force = c.frame.reshape(3,3).T @ force[:3]
                contacts.append({'geomA':a, 'geomB':b, 'normalN':float(force[0]), 'forceOnGeomBWorldN':world_force.tolist(), 'penetrationM':max(0,-float(c.dist))})
                if t < 1.8 and (a.startswith(('pin_', 'dog')) or b.startswith(('pin_', 'dog'))) and ('beam_bore' in a or 'beam_bore' in b):
                    insertion_contact_n += float(force[0])
        peak_block_force = max(peak_block_force, insertion_contact_n)
        if insertion_contact_n > 25 and not cleared:
            if blocked_since is None:
                blocked_since = t
            if t-blocked_since > .03 and not aborted:
                aborted = True
                events.append({'time':round(t,6),'event':'beam interference exceeds 25 N for 30 ms; retract and inhibit latch/proof load','contactNormalN':insertion_contact_n})
        else:
            blocked_since = None
        peak_insert_force = max(peak_insert_force, abs(float(d.actuator_force[0])))
        if t > duration-.25:
            retained_contacts.extend(contacts)
            retained_samples += 1
        if step % max(1,round(.02/timestep)) == 0:
            rows.append({'time':round(float(d.time),6),'insertionM':float(d.qpos[pq]),'dogExtensionM':float(d.qpos[dq]),'beamDisplacementXM':float(d.qpos[beamq]-2.8),'beamPosition':d.xpos[beam].tolist(),'pinPosition':d.xpos[m.body('pin').id].tolist(),'dogPosition':d.xpos[m.body('retention_dog').id].tolist(),'motorForceN':float(d.actuator_force[0]),'dogActuatorForceN':float(d.actuator_force[1]),'loadN':float(load),'contacts':contacts})
            rows[-1].update({'dogOppositeExtensionM':float(d.qpos[oq]), 'dogOppositePosition':d.xpos[m.body('retention_dog_opposite').id].tolist(), 'dogOppositeActuatorForceN':float(d.actuator_force[2])})
    sums = {}
    for c in retained_contacts:
        key = '|'.join(sorted([c['geomA'], c['geomB']]))
        sums[key] = sums.get(key,0)+c['normalN']
    samples = retained_samples
    axial_dog = 0.
    axial_head = 0.
    for c in retained_contacts:
        pair = c['geomA']+'|'+c['geomB']
        if 'dog' in pair and 'beam_bore_' in pair:
            axial_dog += abs(c['forceOnGeomBWorldN'][0])/samples
        if 'pin_head' in pair and 'bracket_bore_' in pair:
            axial_head += abs(c['forceOnGeomBWorldN'][0])/samples
    summary = {'scenario':scenario,'mujocoVersion':mujoco.__version__,'timestepSeconds':timestep,'durationSeconds':float(d.time),'beamMassKg':float(m.body_mass[beam]),'equalityCount':int(m.neq),'beamFreeDofs':6,'pinGuideDofs':1,'cleared':cleared,'aborted':aborted,'finalInsertionM':float(d.qpos[pq]),'finalDogExtensionM':float(d.qpos[dq]),'finalBeamDisplacementXM':float(d.qpos[beamq]-2.8),'maxPenetrationM':max_pen,'peakInsertionActuatorN':peak_insert_force,'peakInsertionBeamContactN':peak_block_force,'meanDogToBeamAxialContactN':axial_dog,'meanHeadToBracketAxialContactN':axial_head,'finalMotorForceN':float(d.actuator_force[0]),'finalDogActuatorForceN':float(d.actuator_force[1]),'finalQuarterSecondMeanContactN':{k:v/samples for k,v in sums.items()},'maxWarningCount':int(max(w.number for w in d.warning)),'finiteState':bool(np.isfinite(d.qpos).all() and np.isfinite(d.qvel).all()),'events':events,'completeRobotFasteningCycle':False}
    summary.update({'finalDogOppositeExtensionM':float(d.qpos[oq]),'finalDogOppositeActuatorForceN':float(d.actuator_force[2])})
    if save:
        (HERE/f'{scenario}.xml').write_text(xml)
        (HERE/f'{scenario}-trace.json').write_text(json.dumps(rows, separators=(',',':'))+'\n')
        (HERE/f'{scenario}-validation.json').write_text(json.dumps(summary,indent=2)+'\n')
    if render:
        # Render the integrated final state without altering any body pose.
        import struct
        import zlib
        cam = mujoco.MjvCamera()
        cam.type = mujoco.mjtCamera.mjCAMERA_FREE
        cam.lookat[:] = [.01,.085,.3375]
        cam.distance, cam.azimuth, cam.elevation = .3, 280, 0
        with mujoco.Renderer(m,480,640) as renderer:
            renderer.update_scene(d,cam)
            pixels = renderer.render()
        def chunk(kind, payload):
            return struct.pack('>I',len(payload))+kind+payload+struct.pack('>I',zlib.crc32(kind+payload)&0xffffffff)
        png = b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',640,480,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(b'\x00'+row.tobytes() for row in pixels)))+chunk(b'IEND',b'')
        (HERE/f'{scenario}-final.png').write_bytes(png)
    return summary, rows


if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--scenario',choices=['nominal','misaligned','no-latch','pullout'],default='nominal')
    ap.add_argument('--timestep',type=float,default=.0005)
    ap.add_argument('--render',action='store_true',help='Render the actual final state; needs an OpenGL context')
    args=ap.parse_args()
    summary,_=run(args.scenario,args.timestep,save=True,render=args.render)
    print(json.dumps(summary,indent=2))
