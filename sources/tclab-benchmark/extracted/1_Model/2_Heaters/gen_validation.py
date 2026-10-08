import numpy as np
import pandas as pd
import tclab
import time
import matplotlib.pyplot as plt

# generate step test data on Arduino
filename = 'validation.csv'

# heater steps
Q1d = np.zeros(601)
Q1d[60:320] = 70
Q1d[320:520] = 10
Q1d[520:] = 50

Q2d = np.zeros(601)
Q2d[10:200] = 100
Q2d[200:280] = 60
Q2d[280:400] = 30
Q2d[400:] = 80

# Connect to Arduino
a = tclab.TCLab()
fid = open(filename,'w')
fid.write('Time,H1,H2,T1,T2\n')
fid.close()

# run step test (10 min)
for i in range(601):
    # set heater values
    a.Q1(Q1d[i])
    a.Q2(Q2d[i])
    print('Time: ' + str(i) + \
          ' H1: ' + str(Q1d[i]) + \
          ' H2: ' + str(Q2d[i]) + \
          ' T1: ' + str(a.T1)   + \
          ' T2: ' + str(a.T2))
    # wait 1 second
    time.sleep(1)
    fid = open(filename,'a')
    fid.write(str(i)+','+str(Q1d[i])+','+str(Q2d[i])+',' \
              +str(a.T1)+','+str(a.T2)+'\n')
# close connection to Arduino
a.close()

# read data file
data = pd.read_csv(filename)

# plot measurements
plt.figure()
plt.subplot(2,1,1)
plt.plot(data['Time'],data['H1'],'r-',label='Heater 1')
plt.plot(data['Time'],data['H2'],'b--',label='Heater 2')
plt.ylabel('Heater (%)')
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.plot(data['Time'],data['T1'],'r.',label='Temperature 1')
plt.plot(data['Time'],data['T2'],'b.',label='Temperature 2')
plt.ylabel('Temperature (degC)')
plt.legend(loc='best')
plt.xlabel('Time (sec)')
plt.savefig('gen_data.png')

plt.show()
