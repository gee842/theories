import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gekko import GEKKO
import random
import time
import threading

#########################################################
# Initialize Model
#########################################################
# load data and parse into columns
data = pd.read_csv('data.txt')
t = data['Time']
u = data[['Q1','Q2']]
y = data[['T1','T2']]

# generate time-series model
m = GEKKO(remote=False)

##################################################################
# system identification
na = 2 # output coefficients
nb = 2 # input coefficients
print('Identify model')
yp,p,K = m.sysid(t,u,y,na,nb,objf=10000,shift='init',\
                 scale=False,diaglevel=1,pred='model')
# load disturbances
ld1 = data['T1'].values - yp[:,0]
ld2 = data['T2'].values - yp[:,1]

##################################################################
# PID simulation
# FOPDT Model
Kp = 0.9200270657559153
tauP = 175.1814480958061
thetaP = 15.622280726988599

# Aggressive IMC Controller (PI control)
tauC = max(0.1*tauP,0.8*thetaP)
Kc   = tauP/(Kp*(thetaP+tauC))
tauI = tauP # sec
tauD = 0.0  # sec

######################################################
# PID Controller                                     #
######################################################
# inputs -----------------------------------
# sp = setpoint
# pv = current temperature
# pv_last = prior temperature
# ierr = integral error
# dt = time increment between measurements
# outputs ----------------------------------
# op = output of the PID controller
# P = proportional contribution
# I = integral contribution
# D = derivative contribution
def pid(sp,pv,pv_last,ierr,dt,Kc,tauI,tauD):
    # Parameters in terms of PID coefficients
    KP = Kc
    KI = Kc/tauI
    KD = Kc*tauD
    # ubias for controller (initial heater)
    op0 = 0 
    # upper and lower bounds on heater level
    ophi = 100
    oplo = 0
    # calculate the error
    error = sp-pv
    # calculate the integral error
    ierr = ierr + KI * error * dt
    # calculate the measurement derivative
    dpv = (pv - pv_last) / dt
    # calculate the PID output
    P = KP * error
    I = ierr
    D = -KD * dpv
    op = op0 + P + I + D
    # implement anti-reset windup
    if op < oplo or op > ophi:
        I = I - KI * error * dt
        # clip output
        op = max(oplo,min(ophi,op))
    # return the controller output and PID terms
    return [op,P,I,D]

def myObj(Kc,tauI):
    loops = len(data['TSP1'])
    dt = 1.0
    ierr = 0.0
    Q1 = np.ones(loops) * 0.0
    Q2 = np.ones(loops) * 0.0
    T1 = np.ones(loops) * data['T1'][0] # simulated T (degC)
    T2 = np.ones(loops) * data['T2'][0] # simulated T (degC)
    Tsp1 = data['TSP1'].values
    Tsp2 = data['TSP2'].values
    m = GEKKO(remote=False,server='http://byu.apmonitor.com',\
              name='Kc'+str(Kc)+'_tauI'+str(tauI))
    y,u = m.arx(p)
    m.options.IMODE = 1
    m.time = [0,1]
    m.solve(disp=False)
    m.options.IMODE = 4
    m.solve(disp=False)
    mv_obj = 0.0
    for i in range(loops):
        [Q1[i],P,ierr,D] = pid(Tsp1[i],T1[i],T1[i-1],ierr,dt,Kc,tauI,tauD)
        u[0].value = Q1[i]
        m.solve(disp=False)
        if i<loops-1:
            T1[i+1] = y[0].value[1]+ld1[i+1]
            T2[i+1] = y[1].value[1]+ld2[i+1]
        if i>=1:
            mv_obj += Q1[i]-Q1[i-1]
    # calculate objective
    cv_obj = np.sum(np.abs(Tsp1-T1))
    obj = (0.5*mv_obj + cv_obj)/loops
    m.cleanup()
    return obj,Q1,Q2,T1,T2

class ThreadClass(threading.Thread):
    def __init__(self, id, Kc, tauI):
        s = self
        s.id = id
        s.Kc = Kc
        s.tauI = tauI
        s.obj = 0.0
        threading.Thread.__init__(s)

    def run(self):

        # Don't overload server by executing all scripts at once
        sleep_time = random.random()
        time.sleep(sleep_time)

        print('Running application ' + str(self.id) + '\n')

        obj,Q1,Q2,T1,T2 = myObj(self.Kc,self.tauI)
        self.obj = obj

# Optimize at mesh points
x = np.arange(5.0, 80.1, 5.0)
y = np.arange(5.0, 80.1, 5.0)
# for testing
#x = [20.0,100.0]
#y = [5.0,55.0]
a, b = np.meshgrid(x, y)

# Array of threads
threads = []

# Calculate objective at all meshgrid points

# Load applications
id = 0
for i in range(a.shape[0]):
    for j in range(b.shape[1]):
        # Create new thread
        threads.append(ThreadClass(id, a[i,j], b[i,j]))
        # Increment ID
        id += 1

# Run applications simultaneously as multiple threads
# Max number of threads to run at once
max_threads = 8
for thr in threads:
    while (threading.activeCount()>max_threads):
        # check for additional threads every 0.1 sec
        time.sleep(0.1)
    # start the thread
    thr.start()

### Check for completion
##mt = 300000.0 # max time
##it = 0.0 # incrementing time
##st = 1.0 # sleep time
##while (threading.activeCount()>=1):
##    time.sleep(st)
##    it = it + st
##    print('Active Threads: ' + str(threading.activeCount()))
##    # Terminate after max time
##    if (it>=mt):
##        break

# Wait for all threads to complete
for thr in threads:
    thr.join()
print('Threads complete')

# Initialize array for objective
obja = np.empty_like(a)

# Retrieve objective results
id = 0
for i in range(a.shape[0]):
    for j in range(b.shape[1]):
        obja[i,j] = threads[id].obj
        id += 1

# plot 3D figure of results
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure(1,figsize=(8,6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(a, b, obja, \
                       rstride=1, cstride=1, cmap=cm.coolwarm, \
                       vmin = np.min(obja)-0.1, vmax = np.max(obja)+0.1,
                       linewidth=1, antialiased=False)

ax.set_xlabel(r'$K_c$')
ax.set_ylabel(r'$\tau_I$')
ax.set_zlabel('Obj')
plt.savefig('pid_3d_contour.png')
plt.savefig('pid_3d_contour.eps')

# Create a contour plot
plt.figure(2,figsize=(10,7))
# Specify contour lines
lines = np.round(np.linspace(np.floor(np.min(obja)*10.0)/10.0,\
                             np.ceil(np.max(obja)*10.0)/10.0,11),2)
# Plot volume contours
CS = plt.contour(a,b,obja,lines)
# Label contours
plt.clabel(CS, inline=1, fontsize=10)
# Add some text to the plot
plt.xlabel(r'$K_c$')
plt.ylabel(r'$\tau_I$')
plt.savefig('pid_contour.png')
plt.savefig('pid_contour.eps')

# re-simulate with best Kc,tauI
obj_best = 1.0e10
for i in range(np.size(obja,0)):
    for j in range(np.size(obja,1)):
        if obja[i,j]<=obj_best:
            obj_best = obja[i,j]
            Kc_best = a[i,j]
            tauI_best = b[i,j]
obj,Q1,Q2,T1,T2 = myObj(Kc_best,tauI_best)

print('best Kc: ' + str(Kc_best))
print('best tauI:' + str(tauI_best))

# load validation/verification PID data (run 2_validate_PID.py)
valid = pd.read_csv('validate.txt')

##################################################################
# plot sysid results
plt.figure(3,figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t,data['Q1'],'r-')
plt.plot(t,Q1,'k:')
plt.plot(valid['Time'],valid['Q1'],'r:')
plt.plot(t,data['Q2'],'b-')
plt.legend([r'$Q_1$ Original',r'$Q_1$ Optimal',r'$Q_1$ Verified',\
            r'$Q_2$'],loc=1)
plt.ylabel('MVs')
plt.subplot(2,1,2)
plt.plot(t,data['TSP1'],'k-')
plt.plot(t,data['T1'],'r.')
plt.plot(t,T1,'k:')
plt.plot(valid['Time'],valid['T1'],'r:')
plt.plot(t,yp[:,0],'k--',lw=2)
plt.plot(t,data['TSP2'],'k:')
plt.plot(t,data['T2'],'.',color='orange')
plt.plot(t,T2,':',color='orange')
plt.plot(t,yp[:,1],'k:',lw=2)
plt.legend([r'$T_{SP1}$','$T_{C1,meas}$',\
            r'$T_{C1,optimal}$',r'$T_{C1,verified}$',r'$T_{C1,pred}$',\
            r'$T_{SP2}$','$T_{C2,meas}$',\
            r'$T_{C2,optimal}$',r'$T_{C2,pred}$'],loc=4)
plt.ylabel('CVs')
plt.xlabel('Time (sec)')
plt.savefig('tclab_farxid.png')
plt.savefig('tclab_farxid.eps')
plt.show()
