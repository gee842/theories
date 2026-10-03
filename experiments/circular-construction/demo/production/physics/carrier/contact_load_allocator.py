"""Bounded static contact-force plan used only to compute motor feedforward.

The optimizer never applies contact forces to MuJoCo. Finite contacts determine
actual loads; the plan is rejected unless measured retained supports are loaded.
"""
import numpy as np
from scipy.optimize import linprog

def allocate(grasp,bias,actuator_dofs,limits,mu,normal_sum,allow_downward=False):
    k=grasp.shape[1]//3
    Aeq=np.pad(grasp[:6],((0,0),(0,1)))
    torque_jac=grasp[actuator_dofs]
    b=bias[actuator_dofs]
    rows=[];rhs=[]
    for row,own,limit in zip(torque_jac,b,limits):
        rows.append(np.r_[-row,-limit]);rhs.append(-own)
        rows.append(np.r_[row,-limit]);rhs.append(own)
    for i in range(k):
        if not allow_downward:
            row=np.zeros(3*k+1);row[3*i+2]=-1;rows.append(row);rhs.append(-400.)
        # Eight conservative tangent-plane friction facets; Y is the jaw normal.
        for angle in np.arange(8)*np.pi/4:
            row=np.zeros(3*k+1);row[3*i]=np.cos(angle);row[3*i+2]=np.sin(angle)
            rows.append(row);rhs.append(mu*normal_sum*np.cos(np.pi/8))
        for sign in (-1,1):
            row=np.zeros(3*k+1);row[3*i+1]=sign;rows.append(row);rhs.append(normal_sum*.5)
    c=np.r_[np.zeros(3*k),1.]
    result=linprog(c,A_ub=rows,b_ub=rhs,A_eq=Aeq,b_eq=bias[:6],bounds=[(None,None)]*(3*k)+[(0,None)],method='highs')
    if not result.success:return None,{'success':False,'message':result.message}
    return result.x[:-1],{'success':True,'peakPlannedTorqueFraction':float(result.x[-1]),'plannedForcesN':result.x[:-1].reshape(-1,3).tolist()}
