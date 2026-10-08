import tclab
import numpy as np
import time
import matplotlib.pyplot as plt
from gekko import GEKKO

# Connect to Arduino
a = tclab.TCLab()

# Get Version
print(a.version)

# Turn LED on
print('LED On')
a.LED(100)

# Run time in minutes
run_time = 10.0

# Number of cycles with 2 second intervals
loops = int(30.0*run_time)
tm = np.zeros(loops)

# Temperature (K)
T1s = np.ones(loops) * a.T1 # temperature (degC)
Tsp1 = np.ones(loops) * T1s[0] # set point (degC)
T2s = np.ones(loops) * a.T2 # temperature (degC)
Tsp2 = np.ones(loops) * T2s[0] # set point (degC)

# Sleep time
sleep_max = 2.0

# Set point changes
Tsp1[3:] = 50.0
Tsp2[int(80/sleep_max):] = 35.0
Tsp1[int(160/sleep_max):] = 30.0
Tsp2[int(240/sleep_max):] = 50.0
Tsp1[int(320/sleep_max):] = 45.0
Tsp2[int(400/sleep_max):] = 35.0
Tsp1[int(480/sleep_max):] = 60.0

# heater values
Q1s = np.ones(loops) * 0.0
Q2s = np.ones(loops) * 0.0

#########################################################
# Initialize Model
#########################################################
# remote=True for MacOS
m = GEKKO(name='tclab-mpc',remote=False)

# 60 second time horizon, steps of 3 sec
#m.time = np.linspace(0,60,21)
m.time = [0,2,4,6,8,10,12,15,20,25,30,35,40,45,50,55,60]

# Manipulated variables
Q1 = m.MV(value=0)
Q1.STATUS = 1  # use to control temperature
Q1.FSTATUS = 0 # no feedback measurement
Q1.LOWER = 0.0
Q1.UPPER = 100.0
Q1.DMAX = 100.0
Q1.COST = 0.0
Q1.DCOST = 0.1

Q2 = m.MV(value=0)
Q2.STATUS = 1  # use to control temperature
Q2.FSTATUS = 0 # no feedback measurement
Q2.LOWER = 0.0
Q2.UPPER = 100.0
Q2.DMAX = 100.0
Q2.COST = 0.0
Q2.DCOST = 0.1

# Controlled variable
TC1 = m.CV(value=T1s[0])
TC1.STATUS = 1     # minimize error with setpoint range
TC1.FSTATUS = 1    # receive measurement
TC1.TR_INIT = 2    # reference trajectory
TC1.TAU = 10       # time constant for response
TC1.TR_OPEN = 5

# Controlled variable
TC2 = m.CV(value=T2s[0])
TC2.STATUS = 1     # minimize error with setpoint range
TC2.FSTATUS = 1    # receive measurement
TC2.TR_INIT = 2    # reference trajectory
TC2.TAU = 10       # time constant for response
TC2.TR_OPEN = 5

# Parameters from Estimation
U = m.FV(value=5.599,lb=1,ub=20)
Us = m.FV(value=20.3785,lb=5,ub=40)
alpha1 = m.FV(value=0.0129587,lb=0.001,ub=0.03)  # W / % heater
alpha2 = m.FV(value=0.0060915,lb=0.001,ub=0.02) # W / % heater
tau = m.FV(value=20.67971,lb=5.0,ub=60.0)

Ta =23.0+273.15                     # K
mass = 4.0/1000.0                   # kg
Cp = 0.5*1000.0                     # J/kg-K    
A = 10.0/100.0**2                   # Area not between heaters in m^2
As = 2.0/100.0**2                   # Area between heaters in m^2
eps = 0.9                           # Emissivity
sigma = 5.67e-8                     # Stefan-Boltzmann

TH1 = m.SV(value=T1s[0])
TH2 = m.SV(value=T2s[0])

# Heater Temperatures in Kelvin
T1 = m.Intermediate(TH1+273.15)
T2 = m.Intermediate(TH2+273.15)

# Heat transfer between two heaters
Q_C12 = m.Intermediate(Us*As*(T2-T1)) # Convective
Q_R12 = m.Intermediate(eps*sigma*As*(T2**4-T1**4)) # Radiative

# Energy balances
m.Equation(mass*Cp*TH1.dt() == U*A*(Ta-T1) \
                + eps * sigma * A * (Ta**4 - T1**4) \
                + Q_C12 + Q_R12 \
                + alpha1*Q1)

m.Equation(mass*Cp*TH2.dt() == U*A*(Ta-T2) \
                + eps * sigma * A * (Ta**4 - T2**4) \
                - Q_C12 - Q_R12 \
                + alpha2*Q2)

# Conduction to temperature sensors
m.Equation(tau*TC1.dt() == TH1-TC1)
m.Equation(tau*TC2.dt() == TH2-TC2)

# Global Options
m.options.IMODE   = 6 # MPC
m.options.CV_TYPE = 1 # Objective type
m.options.NODES   = 3 # Collocation nodes
m.options.SOLVER  = 3 # 1=APOPT, 3=IPOPT
##################################################################

# Main Loop
start_time = time.time()
prev_time = start_time
try:
    for i in range(1,loops):
        sleep = sleep_max - (time.time() - prev_time)
        if sleep>=0.01:
            time.sleep(sleep)
        else:
            print('Warning, Cycle Time Exceeded: ' + str(sleep))
            time.sleep(0.01)

        # Record time and change in time
        t = time.time()
        dt = t - prev_time
        prev_time = t
        tm[i] = t - start_time

        # Read temperatures in Kelvin 
        T1s[i] = a.T1
        T2s[i] = a.T2

        ###############################
        ### MPC CONTROLLER          ###
        ###############################
        TC1.MEAS = T1s[i]
        TC2.MEAS = T2s[i]
        # input setpoint with deadband +/- DT
        DT = 0.2
        TC1.SPHI = Tsp1[i] + DT
        TC1.SPLO = Tsp1[i] - DT
        TC2.SPHI = Tsp2[i] + DT
        TC2.SPLO = Tsp2[i] - DT
        # solve MPC
        m.solve(disp=False)    
        # test for successful solution
        if (m.options.APPSTATUS==1):
            # retrieve the first Q value
            Q1s[i] = Q1.NEWVAL
            Q2s[i] = Q2.NEWVAL
        else:
            # not successful, set heater to zero
            Q1s[i] = 0        
            Q2s[i] = 0        

        # Write output (0-100)
        a.Q1(Q1s[i])
        a.Q2(Q2s[i])

    # Turn off heaters
    a.Q1(0)
    a.Q2(0)

    # Plot
    plt.figure(figsize=(10,7))
    ax=plt.subplot(3,1,1)
    ax.grid()
    plt.plot(tm[0:i],T1s[0:i],'ro',MarkerSize=3,label=r'$T_1$')
    plt.plot(tm[0:i],Tsp1[0:i],'k-',LineWidth=2,label=r'$T_1$ SP')
    plt.ylabel('Temperature (degC)')
    plt.legend(loc='best')
    ax=plt.subplot(3,1,2)
    ax.grid()
    plt.plot(tm[0:i],T2s[0:i],'ro',MarkerSize=3,label=r'$T_2$')
    plt.plot(tm[0:i],Tsp2[0:i],'g-',LineWidth=2,label=r'$T_2$ SP')
    plt.ylabel('Temperature (degC)')
    plt.legend(loc='best')
    ax=plt.subplot(3,1,3)
    ax.grid()
    plt.plot(tm[0:i],Q1s[0:i],'r-',LineWidth=3,label=r'$Q_1$')
    plt.plot(tm[0:i],Q2s[0:i],'b:',LineWidth=3,label=r'$Q_2$')
    plt.ylabel('Heaters')
    plt.xlabel('Time (sec)')
    plt.legend(loc='best')
    plt.savefig('tclab_hybrid.png')
    plt.savefig('tclab_hybrid.eps')
    data = np.vstack((tm,Q1s,Q2s,T1s,T2s,Tsp1,Tsp2)).T
    np.savetxt('results_hybrid.csv',data,delimiter=',',\
               header='Time,Q1,Q2,T1,T2,T1SP,T2SP',comments='')

    print('Shutting down') 


# Allow user to end loop with Ctrl-C           
except KeyboardInterrupt:
    # Disconnect from Arduino
    a.Q1(0)
    a.Q2(0)
    print('Shutting down')
    a.close()

# Make sure serial connection still closes when there's an error
except:           
    # Disconnect from Arduino
    a.Q1(0)
    a.Q2(0)
    print('Error: Shutting down')
    a.close()
    raise
