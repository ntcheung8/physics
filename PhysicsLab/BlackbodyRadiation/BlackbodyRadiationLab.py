# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:14:16 2019

@author: Nicholas Cheung
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.optimize import curve_fit

####### CONSTANTS #######
h = 6.626e-34
c = 3e8
k = 1.3806e-23
pi = const.pi
T = 3600 #Guessed temperature for 5.15V
scaleTestData = 190000
scaleYData = 1000

####### IMPORTED DATA #######
data = np.loadtxt('5.15.txt')
dataY = np.zeros(len(data));
test = np.zeros(len(data));
wavelength = np.zeros(len(data));
fit = np.zeros(len(data));
wavelengthInNanometers = np.zeros(len(data));

####### PLANCK EQUATION FUNCTION #######
def planckEquation(wavelength, T):
    num = 8 * pi * h * c
    a = (wavelength ** 5)
    b = (np.exp(h * c / (wavelength * k * T))) - 1
    denom = a * b
    y = num / (denom * scaleTestData) # Scaling here is to ensure our fitting function works as expected (at least get values on the same magnitude).
    return y

####### MODIFIED PLANCK EQUATION FUNCTION #######
def planckEquationModified(frequency, T):
    num = 8 * pi * h * frequency ** 3
    a = (c ** 3)
    b = np.exp(h * frequency / (k * T)) - 1
    denom = a * b
    y = num / denom
    return y * 1.8e27

####### SETUP DATA #######
def setupData(volts):
    data = np.loadtxt(volts + '.txt')
    dataY = np.zeros(len(data));
    wavelength = np.zeros(len(data));
    wavelengthInNanometers = np.zeros(len(data));
    for i in range(len(data)):
        wavelengthInNanometers[i] = np.double(data[i][0])
        wavelength[i] = np.double(data[i][0]) * 1e-9;
        dataY[i] = np.double(data[i][1])
    dataY = dataY / scaleYData
    return([data, dataY, wavelength, wavelengthInNanometers])

####### SETUP DATA MODIFIED #######
def setupDataModified(filename):
    data = np.loadtxt(filename + '.txt')
    frequency = np.zeros(len(data))
    dataY = np.zeros(len(data));
    for i in range(len(data)):
        frequency[i] = c * (np.double(data[i][0])) * 1e2;
        dataY[i] = np.double(data[i][1])
    return([data, dataY, frequency])

####### FITTING DATA AND PLOT #######
def fitting(wavelength, dataY):
    param, param_cov = curve_fit(planckEquation, wavelength, dataY, p0 = 3500)
    perr = np.sqrt(np.diag(param_cov))
    print('Standard Deviation of Error: ' + str(perr))
    print('Best Temperature: ' + str(param[0]))
    plt.plot(wavelengthInNanometers, dataY, '.', label = 'Data')
    plt.plot(wavelengthInNanometers, planckEquation(wavelength, param[0]), 'r', label = 'FittedFunction')
    plt.legend(loc = 'best')
    plt.show()
    return param

####### MODIFIED FITTING DATA AND PLOT #######
def fittingModified(frequency, dataY):
    param, param_cov = curve_fit(planckEquationModified, frequency, dataY, p0 = 1)
    perr = np.sqrt(np.diag(param_cov))
    print('Standard Deviation of Error: ' + str(perr))
    print('Best Temperature: ' + str(param[0]))
    plt.scatter(frequency, dataY, label = 'Data')
    plt.plot(frequency, planckEquationModified(frequency, param[0]), 'r', label = 'FittedFunction')
    plt.legend(loc = 'best')
    plt.show()
    return param

####### 4.15 VOLTS #######
[data, dataY, wavelength, wavelengthInNanometers] = setupData('4.15')
print('Graph for 4.15V')
plt.figure(figsize = (6,4))
plt.title('4.15V')
plt.xlabel('Wavelength (nm)')
fitting(wavelength, dataY)

####### 4.5 VOLTS #######
[data, dataY, wavelength, wavelengthInNanometers] = setupData('4.5')
print('Graph for 4.5V')
plt.figure(figsize = (6,4))
plt.title('4.5V')
plt.xlabel('Wavelength (nm)')
fitting(wavelength, dataY)

####### 5.15 VOLTS (AND FIRST EYEBALLED FIT) #######
for i in range(len(data)):
    wavelengthInNanometers[i] = np.double(data[i][0])
    wavelength[i] = np.double(data[i][0]) * 1e-9;
    dataY[i] = np.double(data[i][1])
    test[i] = planckEquation(wavelength[i], T)
dataY = dataY / scaleYData
print('Eyeballed fit for 5.15V, guess and checked temperature')
plt.plot(wavelengthInNanometers, test, 'r')
plt.plot(wavelengthInNanometers, dataY, 'b')
plt.title('5.15V')
plt.xlabel('Wavelength (nm)')
plt.show()
print('Below shows graph for 5.15V')
plt.figure(figsize = (6,4))
plt.title('5.15V')
plt.xlabel('Wavelength (nm)')
fitting(wavelength, dataY)

####### 5.5 VOLTS #######
[data, dataY, wavelength, wavelengthInNanometers] = setupData('5.5')
print('Below shows graph for 5.5V')
plt.figure(figsize = (6,4))
plt.title('5.5V')
plt.xlabel('Wavelength (nm)')
fitting(wavelength, dataY)

####### 6.5 VOLTS #######
[data, dataY, wavelength, wavelengthInNanometers] = setupData('6.5')
print('Below shows graph for 6.5V')
plt.figure(figsize = (6,4))
plt.title('6.5V')
plt.xlabel('Wavelength (nm)')
fitting(wavelength, dataY)


####### 7.15 VOLTS #######
[data, dataY, wavelength, wavelengthInNanometers] = setupData('7.15')
print('Below shows graph for 7.15V')
plt.figure(figsize = (6,4))
plt.title('7.15V')
plt.xlabel('Wavelength (nm)')
fitting(wavelength, dataY)

####### GIVEN DATA FOR COSMIC MICROWAVE BACKGROUND SPECTRUM #######
[data, dataY, frequency] = setupDataModified('firas_monopole_spec_v1')
plt.figure()
plt.plot(frequency, planckEquationModified(frequency, 3), 'r')
plt.title('My Modified Plank Equation vs. Frequency')
print('Below shows graph for firas_monopole_spec_v1')
plt.figure(figsize = (6,4))
plt.title('Cosmic Microwave Background Spectrum')
plt.xlabel('frequency (Hz)')
fittingModified(frequency, dataY)
