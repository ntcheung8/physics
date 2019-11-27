import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


data = pd.read_excel("xRayDiffraction/data.xlsx")

plt.figure()
data = data.sort_values(by='theta')
plt.plot(data['theta'], data['intensity'])
plt.ylabel('intensity')
plt.xlabel('theta')

peaks = []
for i in range(len(data['intensity'])):
    if(data['intensity'][i] > 20):
        peaks.append(i)
for i in range(len(peaks)):
    plt.plot(data['theta'][peaks[i]], data['intensity'][peaks[i]], 'o')

plt.show()

d = []
print(data['theta'][peaks])

d.append(138 * 1e-12 / (2 * np.sin(data['theta'][peaks[0]] * np.pi / 180)))
d.append(154 * 1e-12 / (2 * np.sin(data['theta'][peaks[1]] * np.pi / 180)))
d.append(138 * 1e-12 / (2 * np.sin(data['theta'][peaks[2]] * np.pi / 180)))
d.append(154 * 1e-12 / (2 * np.sin(data['theta'][peaks[3]] * np.pi / 180)))
print('Distance values = ')
print(d)

