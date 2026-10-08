import pandas as pd
import numpy as np

r1 = pd.read_csv('results_hybrid.csv')
r2 = pd.read_csv('results_farx.csv')
r3 = pd.read_csv('results_ann.csv')

# SAE results
sae = np.zeros(3)
qmv = np.zeros(3)
for i,data in enumerate([r1,r2,r3]):
    for j in range(len(data)):
        sae[i] += np.abs(data['T1'][j]-data['T1SP'][j])
        sae[i] += np.abs(data['T2'][j]-data['T2SP'][j])
        if j>=1:
            qmv[i] += np.abs(data['Q1'][j]-data['Q1'][j-1])
            qmv[i] += np.abs(data['Q2'][j]-data['Q2'][j-1])           
    sae[i] = sae[i] / len(data)
    qmv[i] = qmv[i] / data['Time'].values[-1]
print('Fit')
print('SAE SP Error: ' + str(sae))
print('SAE MV Movement: ' + str(qmv))
