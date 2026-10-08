import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gekko import GEKKO

#########################################################
# Initialize Model
#########################################################
# load data and parse into columns
data = pd.read_csv('initial_models.csv')
t = data['Time']
u = data[['H1','H2']]
y = data[['T1','T2']]

##################################################################
# system identification
m = GEKKO()
na = 2 # output coefficients
nb = 2 # input coefficients
print('Identify model')
yp,p,K = m.sysid(t,u,y,na,nb,objf=10000,scale=False,diaglevel=1,pred='model',shift='init')

# SAE results
sae = 0.0
for i in range(len(data)):
    sae += np.abs(data['T1'][i]-yp[i,0])
    sae += np.abs(data['T2'][i]-yp[i,1])
print('Fit')
print('SAE ARX: ' + str(sae))

##################################################################
# plot sysid results
plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t,data['H1'],'r-')
plt.plot(t,data['H2'],'g:')
plt.legend([r'$Q_1$',r'$Q_2$'])
plt.ylabel('MVs')
plt.subplot(2,1,2)
plt.plot(t,data['T1'],'r.')
plt.plot(t,yp[:,0],'k--',lw=2)
plt.plot(t,data['T2'],'.',color='orange')
plt.plot(t,yp[:,1],'k:',lw=2)
plt.legend([r'$T_{C1,meas}$',r'$T_{C1,pred}$',\
            r'$T_{C2,meas}$',r'$T_{C2,pred}$'])
plt.ylabel('CVs')
plt.xlabel('Time (sec)')
plt.savefig('tclab_farxid.png')
plt.savefig('tclab_farxid.eps')

##################################################################
# test model
v = GEKKO()
yv,uv = v.arx(p)

data = pd.read_csv('validation.csv')
t = data['Time']
u = data[['H1','H2']]
y = data[['T1','T2']]

uv[0].value = 0.0
uv[1].value = 0.0
v.options.IMODE = 1
v.solve(disp=False)
uv[0].value = u['H1'].values
uv[1].value = u['H2'].values
v.options.IMODE = 7
v.time = t.values
v.solve(disp=False)

# SAE results
sae = 0.0
for i in range(len(data)):
    sae += np.abs(data['T1'][i]-yv[0].value[i])
    sae += np.abs(data['T2'][i]-yv[1].value[i])
print('Validation')
print('SAE ARX Validation: ' + str(sae))

##################################################################
# plot validation results
plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t,data['H1'],'r-')
plt.plot(t,data['H2'],'g:')
plt.legend([r'$Q_1$',r'$Q_2$'])
plt.ylabel('MVs')
plt.subplot(2,1,2)
plt.plot(t,data['T1'],'r.')
plt.plot(t,yv[0].value,'k--',lw=2)
plt.plot(t,data['T2'],'.',color='orange')
plt.plot(t,yv[1].value,'k:',lw=2)
plt.legend([r'$T_{C1,meas}$',r'$T_{C1,pred}$',\
            r'$T_{C2,meas}$',r'$T_{C2,pred}$'])
plt.ylabel('CVs')
plt.xlabel('Time (sec)')
plt.savefig('tclab_farxid_validation.png')
plt.savefig('tclab_farxid_validation.eps')

plt.show()

