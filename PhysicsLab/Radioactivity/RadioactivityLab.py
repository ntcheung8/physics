# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:04:47 2019

@author: Nicholas Cheung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

avgCtrl = 4

dataHour = pd.read_excel('longTest.xlsx')
xHour = dataHour['Time']
yHour = dataHour['Radiation']
yHour = [y - avgCtrl for y in yHour]
yHour = np.log(yHour)
plt.figure()
slopeHour, interceptHour, r_valueHour, p_valueHour, std_errHour = stats.linregress(xHour,yHour)
HourPlot = sns.regplot(xHour, yHour,line_kws={'label':"Y={0:.5f}x+{1:.5f}".format(slopeHour,interceptHour)})
HourPlot.legend()
plt.title('Radiation vs. Time')
plt.ylabel('Radiation (ln(Counts))')
plt.xlabel('Time (Minutes)')
plt.plot(xHour, yHour, 'o')
plt.show()
print('Halflife = ln(2)/(-0.01213) = 57.14 mins')


dataDens = pd.read_excel('data.xlsx')
xDens = dataDens['Density']
yDens = dataDens['Counts']
yDens = [y - avgCtrl for y in yDens]
yDens = np.log(yDens)
plt.figure()
slopeDens, interceptDens, r_valueDens, p_valueDens, std_errDens = stats.linregress(xDens,yDens)
DensPlot = sns.regplot(xDens, yDens,line_kws={'label':"Y={0:.5f}x+{1:.5f}".format(slopeDens,interceptDens)})
DensPlot.legend()
plt.xlabel('Desnity(Mg/cm^2)')
plt.ylabel('ln(Counts)')
plt.plot(xDens, yDens, 'o')
plt.show()
print('Half Value Thickness = ln(2)/(0.0001) = 6931.47 Mg/cm^2')


dataDist = pd.read_excel('data2.xlsx')
xDist = dataDist['Distance (cm)']
yDist = dataDist['Counts']
yDist = [y - avgCtrl for y in yDist]
yDist = np.log(yDist)
plt.figure()
slopeDist, interceptDist, r_valueDist, p_valueDist, std_errDist = stats.linregress(xDist,yDist)
DistPlot = sns.regplot(xDist, yDist,line_kws={'label':"Y={0:.5f}x+{1:.5f}".format(slopeDist,interceptDist)})
DistPlot.legend()
plt.ylabel('Radiation (counts)')
plt.xlabel('Distance (cm)')
plt.plot(xDist, yDist, 'o')
plt.show()


