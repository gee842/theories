"""Generate editable MJCF for the active workcell, in SI and Blender Z-up."""
from pathlib import Path
import math

HERE=Path(__file__).resolve().parent

def build():
    limbs=[]; locks=[]; motors=[]; anchors=[]
    for name,y,z in [('fl',-.25,.32),('fr',.25,.32),('rl',-.25,-.32),('rr',.25,-.32)]:
        limbs.append(f'''<body name="limb_{name}_upper" pos="0 {y} {z}" euler="0 -.35 0">
          <joint name="{name}_shoulder" axis="0 1 0" range="-.4 1.1" damping="12" armature=".08"/>
          <geom type="capsule" fromto="0 0 0 .32 0 0" size=".065" mass="8"/>
          <body name="limb_{name}_lower" pos=".32 0 0" euler="0 .35 0">
            <joint name="{name}_elbow" axis="0 1 0" range="-1.1 .4" damping="10" armature=".05"/>
            <geom type="capsule" fromto="0 0 0 .32 0 0" size=".05" mass="6"/>
            <body name="limb_{name}_grip" pos=".32 0 0">
              <geom type="box" size=".065 .08 .075" mass="3"/>
              <site name="grip_{name}" size=".02"/>
            </body>
          </body>
        </body>''')
        anchors.append(f'<body name="anchor_{name}" pos="{5.4+.32*math.cos(.35)+.32} {-12+y} {43.9+z+.32*math.sin(.35)}"/>')
        locks.append(f'<weld name="lock_{name}" body1="limb_{name}_grip" body2="anchor_{name}" solref=".004 1" solimp=".9999 .9999 .0001"/>')
        for j in ['shoulder','elbow']:
            motors.append(f'<motor name="{name}_{j}" joint="{name}_{j}" ctrlrange="-450 450" forcerange="-450 450"/>')
    xml=f'''<mujoco model="Level 12 climbing robot and beam receiving workcell">
    <compiler angle="radian" autolimits="true"/>
    <option timestep=".002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="80" tolerance="1e-9">
      <flag energy="enable" fwdinv="enable"/>
    </option>
    <default><geom friction=".7 .01 .001" solref=".012 1" solimp=".95 .99 .001" rgba=".4 .5 .6 1"/><joint limited="true"/></default>
    <worldbody>
      <light pos="9 -15 50"/> {''.join(anchors)}
      <geom name="rail_left" type="box" pos="6.06 -12.25 43.9" size=".03 .045 1.4" contype="0" conaffinity="0"/>
      <geom name="rail_right" type="box" pos="6.06 -11.75 43.9" size=".03 .045 1.4" contype="0" conaffinity="0"/>
      <body name="seat_left" pos="6.2 -12 43.14"><geom name="seat_left_contact" type="box" size=".25 .32 .06"/></body>
      <body name="seat_right" pos="11.8 -12 43.14"><geom name="seat_right_contact" type="box" size=".25 .32 .06"/></body>
      <body name="robot_chassis" pos="5.4 -12 43.9">
        <freejoint name="robot_free"/>
        <geom type="box" size=".18 .24 .27" mass="65" contype="0" conaffinity="0"/>
        {''.join(limbs)}
        <body name="robot_tool" pos=".25 0 -.55"><joint name="tool_extension" type="slide" axis="1 0 0" range="0 .35" damping="50"/><geom type="capsule" fromto="0 0 0 .12 0 0" size=".035" mass="4" contype="0" conaffinity="0"/></body>
      </body>
      <body name="lifted_beam" pos="9 -12 44.7">
        <freejoint name="beam_free"/>
        <geom name="beam_bottom_flange" type="box" pos="0 0 -.216" size="2.8 .15 .009" density="7850"/>
        <geom name="beam_web" type="box" size="2.8 .0045 .207" density="7850"/>
        <geom name="beam_top_flange" type="box" pos="0 0 .216" size="2.8 .15 .009" density="7850"/>
        <site name="beam_sling_left" pos="-1.6 0 .225"/><site name="beam_sling_right" pos="1.6 0 .225"/>
      </body>
      <body name="hoist_carrier" mocap="true" pos="9 -12 46.45">
        <geom type="capsule" fromto="-1.6 0 0 1.6 0 0" size=".055" contype="0" conaffinity="0"/>
        <site name="hoist_left" pos="-1.6 0 0"/><site name="hoist_right" pos="1.6 0 0"/>
      </body>
    </worldbody>
    <contact>{''.join(f'<exclude body1="robot_chassis" body2="limb_{n}_upper"/>' for n in ['fl','fr','rl','rr'])}</contact>
    <equality>{''.join(locks)}</equality>
    <tendon>
      <spatial name="sling_left" stiffness="0" damping="0" springlength="0 1.4" width=".012"><site site="hoist_left"/><site site="beam_sling_left"/></spatial>
      <spatial name="sling_right" stiffness="0" damping="0" springlength="0 1.4" width=".012"><site site="hoist_right"/><site site="beam_sling_right"/></spatial>
    </tendon>
    <actuator>{''.join(motors)}<motor name="tool_extension" joint="tool_extension" ctrlrange="-500 500" forcerange="-500 500"/></actuator>
    </mujoco>'''
    (HERE/'workcell.xml').write_text(xml)

if __name__=='__main__': build()
