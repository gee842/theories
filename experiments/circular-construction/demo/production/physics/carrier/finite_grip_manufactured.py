"""Evaluate larger manufactured motor/gimbal envelopes with the accepted controller."""
import argparse,json,xml.etree.ElementTree as E
import finite_grip_continuous as base
_original_model=base.model

def model(payload=92.928,mu=.65):
    root=E.fromstring(_original_model(payload,mu))
    for n in base.NAMES:
        for label,parent,typ,size,quat in [
            ('hip_motor_envelope',f'limb_{n}_upper','cylinder','.116 .094','.70710678 .70710678 0 0'),
            ('knee_motor_envelope',f'limb_{n}_lower','cylinder','.086 .094','.70710678 .70710678 0 0'),
            ('wrist_gimbal_envelope',f'limb_{n}_wrist_yaw','sphere','.105',None)]:
            attrs={'name':n+'_'+label,'type':typ,'size':size,'mass':'0'}
            if quat:attrs['quat']=quat
            E.SubElement(root.find(f".//body[@name='{parent}']"),'geom',attrs)
    return E.tostring(root,encoding='unicode')
base.model=model

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['hold','limb','step'],default='step');ap.add_argument('--duration',type=float,default=130);a=ap.parse_args()
    xml,metrics,trace=base.simulate(a.mode,92.928,.65,4000,a.duration,shift_x=.16)
    metrics['manufacturedHousingEnvelopes']=True
    metrics['housingEnvelopeScope']='Conservative0.105m wrist sphere,0.116m hip reducer and0.086m knee reducer radii; existing inertias retained so no duplicate mass.'
    stem=f'candidate-manufactured-{a.mode}-92.928kg-mu0.65-sx0.16'
    (base.HERE/(stem+'.xml')).write_text(xml)
    (base.HERE/(stem+'-metrics.json')).write_text(json.dumps(metrics,indent=2,allow_nan=False)+'\n')
    (base.HERE/(stem+'-trace.json')).write_text(json.dumps(trace,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(metrics,indent=2,allow_nan=False))
