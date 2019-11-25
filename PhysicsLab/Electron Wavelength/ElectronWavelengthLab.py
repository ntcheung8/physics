# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:25:32 2019

@author: Nicholas Cheung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import scipy.constants as const 

# Read in inputs
data = pd.read_excel('data.xlsx')
kV = data['kV']
r1 = data['r1']
r2 = data['r2']
angle1 = []
angle2 = []
wavelength1 = []
wavelength2 = []

# Convert to angle, then wavelength. Store in a list.
for i in range(len(r1)):
    angle1.append(np.arctan(r1[i]))
    angle2.append(np.arctan(r2[i]))
    wavelength1.append(np.sin(angle1[i]) * 0.213)
    wavelength2.append(np.sin(angle2[i]) * 0.123 / 2)

# Get the slope and other information about our data.
m1,b1,r,p,s = stats.linregress(kV, wavelength1)
m2,b2,r,p,s = stats.linregress(kV, wavelength2)

# Plot wavelength 1 vs kV
plt.figure(1)
plt.plot(kV, wavelength1, 'o')
plt.plot(np.unique(kV), np.poly1d(np.polyfit(kV, wavelength1, 1))(np.unique(kV)), 'r')
plt.ylabel('wavelength (nm)')
plt.xlabel('kV (kV)')
plt.title('wavelength vs. voltage')
plt.show()
print('y = ' + str(m1) + 'x + ' + str(b1))

# Plot wavelength 2 vs kV
plt.figure(2)
plt.plot(kV, wavelength2, 'o')
plt.plot(np.unique(kV), np.poly1d(np.polyfit(kV, wavelength2, 1))(np.unique(kV)), 'r')
plt.ylabel('wavelength (nm)')
plt.xlabel('kV (kV)')
plt.title('wavelength vs. voltage')
plt.show()
print('wavelength = ' + str(m2) + ' * kV + ' + str(b2))

# Attempt at plotting debroglie wave calculations
h = const.Planck / (const.elementary_charge)
Eo = .511e6
debrogWave = h/(1/const.speed_of_light) * np.sqrt((Eo+data['kV']*1000)**2 - Eo**2)   

plt.figure(3)
plt.title('wavelength vs. voltage')
plt.plot(np.unique(kV),debrogWave, 'b')
plt.plot(np.unique(kV), np.poly1d(np.polyfit(kV, wavelength2, 1))(np.unique(kV)), 'r')
plt.plot(np.unique(kV), np.poly1d(np.polyfit(kV, wavelength1, 1))(np.unique(kV)), 'r')
plt.ylabel('wavelength (nm)')
plt.xlabel('kV (kV)')
plt.title('wavelength vs. voltage')
plt.show()