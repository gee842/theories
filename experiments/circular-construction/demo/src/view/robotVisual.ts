import * as THREE from 'three';
import { DEFAULT_ROBOT_CONFIG, solveRobotPose, assessStance, toolDockPosition } from '../robotics';
import type { RobotConfig, RobotState, Vec3, GripMode } from '../robotics';

export interface RobotVisual {
  group:THREE.Group;
  update(state:RobotState):void;
  setDiagnostics(visible:boolean):void;
  dispose():void;
}
const COLORS:Record<GripMode,number>={free:0x8095a5,approaching:0xe9b75b,captured:0xe9b75b,locked:0x76c4d9,load_verified:0x68e5b4,tooling:0xa393ee,fault:0xfa5f4d};
const v=(p:Vec3)=>new THREE.Vector3(...p);
const Y=new THREE.Vector3(0,1,0);

/** Procedural articulated machine. Each elbow is parented to its shoulder pivot,
 * and each wrist to its elbow, so visible joints follow the numerical IK solution. */
export function createRobotVisual(options:Partial<RobotConfig>={}):RobotVisual {
  const config={...DEFAULT_ROBOT_CONFIG,...options};
  const group=new THREE.Group();group.name='Four-limb rail assembler';
  const materials:THREE.Material[]=[],geometries:THREE.BufferGeometry[]=[];
  const mat=(color:number,metalness=0.55,roughness=0.35)=>{const m=new THREE.MeshStandardMaterial({color,metalness,roughness});materials.push(m);return m;};
  const dark=mat(0x172b34),steel=mat(0xb5c8c9,0.85,0.25),orange=mat(0xe9a344),rubber=mat(0x24383e,0.1,0.65),white=mat(0xe0ebdb,0.3,0.4);
  const sensor=mat(0x60d7b8,0.2,0.22);sensor.emissive.setHex(0x267a69);sensor.emissiveIntensity=0.6;
  const geometry=<T extends THREE.BufferGeometry>(g:T):T=>{geometries.push(g);return g;};
  const mesh=(g:THREE.BufferGeometry,m:THREE.Material,parent:THREE.Object3D,p:[number,number,number]=[0,0,0])=>{
    const object=new THREE.Mesh(g,m);object.position.set(...p);object.castShadow=true;object.receiveShadow=true;parent.add(object);return object;
  };
  const box=(size:[number,number,number],m:THREE.Material,parent:THREE.Object3D,p:[number,number,number]=[0,0,0])=>mesh(geometry(new THREE.BoxGeometry(...size)),m,parent,p);
  const cyl=(r:number,len:number,m:THREE.Material,parent:THREE.Object3D,p:[number,number,number]=[0,0,0])=>mesh(geometry(new THREE.CylinderGeometry(r,r,len,14)),m,parent,p);
  const sphereGeometry=geometry(new THREE.SphereGeometry(0.088,16,12));
  const torso=box([config.bodyWidth,config.bodyDepth,config.bodyHeight],dark,group);torso.name='Battery and controller chassis';
  // Protective panels, fasteners, cooling fins, and detachable battery modules.
  box([config.bodyWidth*0.85,0.025,config.bodyHeight*0.75],orange,group,[0,-config.bodyDepth/2-0.018,0]);
  box([0.21,0.055,0.23],dark,group,[0,-config.bodyDepth/2-0.058,0.02]);
  for(const x of [-0.19,0.19])box([0.12,0.19,0.16],white,group,[x,0,-config.bodyHeight/2-0.035]);
  for(let i=0;i<6;i++)box([0.26,0.015,0.012],rubber,group,[0,-config.bodyDepth/2-0.035,-0.07+i*0.025]);
  for(const x of [-0.23,0.23])for(const z of [-0.15,0.15])cyl(0.016,0.035,steel,group,[x,-config.bodyDepth/2-0.025,z]);
  const lidar=cyl(0.09,0.065,dark,group,[0,0,config.bodyHeight/2+0.055]);lidar.rotation.x=Math.PI/2;
  const lidarGlass=cyl(0.092,0.012,sensor,group,[0,0,config.bodyHeight/2+0.057]);lidarGlass.rotation.x=Math.PI/2;
  box([0.26,0.065,0.08],dark,group,[0,config.bodyDepth/2+0.015,0.08]);
  for(const x of [-0.085,0.085])cyl(0.025,0.03,sensor,group,[x,config.bodyDepth/2+0.06,0.08]);
  const dock=new THREE.Group();dock.name='Captive tool parking dock';group.add(dock);
  box([0.1,0.1,0.13],dark,dock);box([0.58,0.05,0.055],steel,group,[0.53,-0.12,0.4]);
  box([0.05,0.05,0.22],steel,group,[0.27,-0.12,0.29]);
  const dockTool=new THREE.Group();dock.add(dockTool);
  cyl(0.047,0.18,orange,dockTool,[0,-0.1,0]);cyl(0.022,0.13,steel,dockTool,[0,0.035,0]);
  const limbs=Array.from({length:4},(_,i)=>{
    const shoulder=new THREE.Group();shoulder.name=`Limb ${i+1} shoulder pivot`;group.add(shoulder);
    mesh(sphereGeometry,dark,shoulder);
    const upper=cyl(config.linkRadius,1,orange,shoulder,[0,0.5,0]);upper.scale.y=config.upperLength;upper.position.y=config.upperLength/2;
    const upperRib=box([0.045,config.upperLength*0.65,0.05],steel,shoulder,[0,config.upperLength/2,-0.04]);
    const elbow=new THREE.Group();elbow.name=`Limb ${i+1} elbow pivot`;elbow.position.y=config.upperLength;shoulder.add(elbow);
    mesh(sphereGeometry,steel,elbow).scale.setScalar(0.9);
    const fore=cyl(config.linkRadius*0.82,1,white,elbow,[0,0.5,0]);fore.scale.y=config.foreLength;fore.position.y=config.foreLength/2;
    const piston=cyl(0.014,config.foreLength*0.65,steel,elbow,[0.047,config.foreLength/2,0]);
    const wrist=new THREE.Group();wrist.name=`Limb ${i+1} wrist and keyed clamp`;wrist.position.y=config.foreLength;elbow.add(wrist);
    const clampBase=box([0.18,0.08,0.12],dark,wrist,[0,-0.115,0]);clampBase.name='Positive locking rail clamp';
    const jaws=[-1,1].map(side=>{
      const jaw=new THREE.Group();jaw.position.x=side*0.08;wrist.add(jaw);
      box([0.035,0.2,0.14],steel,jaw,[0,-0.02,0]);box([0.035,0.035,0.13],rubber,jaw,[-side*0.017,0.065,0]);
      return jaw;
    });
    const indicator=mat(COLORS.load_verified,0.2,0.3);indicator.emissive.setHex(COLORS.load_verified);indicator.emissiveIntensity=0.35;
    cyl(0.025,0.018,indicator,wrist,[0,-0.168,0.01]);
    const collar=mesh(geometry(new THREE.TorusGeometry(0.115,0.007,6,24)),indicator,wrist);collar.name='Verified grip indicator';
    const tool=new THREE.Group();tool.visible=false;wrist.add(tool);
    cyl(0.045,0.16,orange,tool,[0,0,0]);cyl(0.019,0.16,steel,tool,[0,0.15,0]);
    return {shoulder,elbow,wrist,upper,upperRib,fore,piston,jaws,indicator,collar,tool};
  });
  const diagnostics=new THREE.Group();diagnostics.visible=false;group.add(diagnostics);
  const arrows=Array.from({length:4},()=>{const a=new THREE.ArrowHelper(new THREE.Vector3(0,0,1),new THREE.Vector3(),0.5,0x67d7b6,0.08,0.04);diagnostics.add(a);return a;});
  const trajectory=new THREE.Line(geometry(new THREE.BufferGeometry()),new THREE.LineBasicMaterial({color:0xf4d18b,transparent:true,opacity:0.7}));materials.push(trajectory.material as THREE.Material);diagnostics.add(trajectory);
  const local=(p:Vec3,state:RobotState)=>v(p).sub(v(state.position)).applyAxisAngle(new THREE.Vector3(0,0,1),-state.yaw);
  return {group,setDiagnostics(visible){diagnostics.visible=visible;},update(state){
    group.position.set(...state.position);group.rotation.set(0,0,state.yaw);group.userData.robotId=state.id;group.userData.status=state.status;
    const pose=solveRobotPose(state),invYaw=new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0,0,1),-state.yaw);
    dock.position.copy(local(toolDockPosition(state),state));dockTool.visible=state.toolDocked;
    for(const [i,p] of pose.limbs.entries()){
      const visual=limbs[i],limb=state.limbs[i],s=local(p.shoulder,state),e=local(p.elbow,state),w=local(p.wrist,state);
      const upperDirection=e.clone().sub(s).normalize(),foreDirection=w.clone().sub(e).normalize();
      const upperQ=new THREE.Quaternion().setFromUnitVectors(Y,upperDirection),foreQ=new THREE.Quaternion().setFromUnitVectors(Y,foreDirection);
      visual.shoulder.position.copy(s);visual.shoulder.quaternion.copy(upperQ);
      visual.elbow.position.set(0,state.config.upperLength,0);visual.elbow.quaternion.copy(upperQ.clone().invert().multiply(foreQ));
      visual.wrist.position.set(0,state.config.foreLength,0);
      const inward=limb.anchor?v(limb.anchor.normal).negate().applyQuaternion(invYaw):Y.clone();
      const wristQ=new THREE.Quaternion().setFromUnitVectors(Y,inward);
      visual.wrist.quaternion.copy(foreQ.clone().invert().multiply(wristQ));
      visual.upper.scale.y=state.config.upperLength;visual.upper.position.y=state.config.upperLength/2;
      visual.fore.scale.y=state.config.foreLength;visual.fore.position.y=state.config.foreLength/2;
      const open=['free','approaching','fault'].includes(limb.mode);
      visual.jaws.forEach((jaw,j)=>jaw.position.x=(j===0?-1:1)*(open?0.135:0.081));
      visual.indicator.color.setHex(COLORS[limb.mode]);visual.indicator.emissive.setHex(COLORS[limb.mode]);
      visual.collar.visible=diagnostics.visible&&limb.mode==='load_verified';visual.tool.visible=limb.tool;
      visual.wrist.userData={robotId:state.id,limb:i,mode:limb.mode,anchorId:limb.anchor?.id};
    }
    if(diagnostics.visible){
      const stance=assessStance(state);
      for(let i=0;i<4;i++){const force=stance.loads.find(l=>l.index===i&&Math.hypot(...l.force)>1e-6);arrows[i].visible=!!force;if(force){arrows[i].position.copy(local(state.limbs[i].position,state));arrows[i].setDirection(v(force.force).normalize().applyQuaternion(invYaw));arrows[i].setLength(Math.max(0.12,v(force.force).length()/850),0.07,0.035);}}
      trajectory.visible=!!state.motion;
      if(state.motion)trajectory.geometry.setFromPoints(state.motion.samples.map(p=>local(p,state)));
    }
  },dispose(){
    for(const g of geometries)g.dispose();for(const m of materials)m.dispose();
    for(const arrow of arrows){arrow.line.geometry.dispose();arrow.cone.geometry.dispose();(arrow.line.material as THREE.Material).dispose();(arrow.cone.material as THREE.Material).dispose();}
    group.removeFromParent();
  }};
}
