# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:30:56 2019

@author: Nicholas Cheung
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Import data for Hydrogen
H = np.genfromtxt('Hydrogen00000.txt')
Hx = []
Hy = []
for i in range(len(H)):
    Hx.append(H[i][0])
    Hy.append(H[i][1])
plt.figure()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Radiation (counts)")
plt.title("Atomic Spectra H")
plt.plot(Hx,Hy)
plt.show()
[HPeaksx, HPeaksy] = find_peaks(Hy, height = 5)
print("Wavelengths of peaks: ")
for i in range(len(HPeaksx)):
    HPeaksx[i] = Hx[HPeaksx[i]]
print(HPeaksx)
HEnergyLevelDifference = 1239.8/HPeaksx
print("Energy Level Difference at Peaks")
print(HEnergyLevelDifference)
plt.figure()
plt.title("Energy Level Difference vs. Wavelength")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Energy Level Difference (eV)")
plt.plot(HPeaksx, HEnergyLevelDifference)

# Import data for Helium
He = np.genfromtxt('Helium00000.txt')
Hex = []
Hey = []
for i in range(len(H)):
    Hex.append(He[i][0])
    Hey.append(He[i][1])
plt.figure()
plt.title("Atomic Spectra He")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Radiation (counts)")
plt.plot(Hex,Hey)
plt.show()
[HePeaksx, HePeaksy] = find_peaks(Hy, height = 5)
print("Wavelengths of peaks: ")
for i in range(len(HePeaksx)):
    HePeaksx[i] = Hx[HePeaksx[i]]
print(HePeaksx)
HeEnergyLevelDifference = 1239.8/HePeaksx
print("Energy Level Difference at Peaks")
print(HeEnergyLevelDifference)

# Import data for Argon
Ar = np.genfromtxt('Argon00000.txt')
Arx = []
Ary = []
for i in range(len(H)):
    Arx.append(Ar[i][0])
    Ary.append(Ar[i][1])
plt.figure()
plt.plot(Arx,Ary)
plt.title("Atomic Spectra Ar")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Radiation (counts)")
plt.show()
[ArPeaksx, ArPeaksy] = find_peaks(Hy, height = 5)
print("Wavelengths of peaks: ")
for i in range(len(ArPeaksx)):
    ArPeaksx[i] = Hx[ArPeaksx[i]]
print(ArPeaksx)
ArEnergyLevelDifference = 1239.8/ArPeaksx
print("Energy Level Difference at Peaks")
print(ArEnergyLevelDifference)

# Import data for Krypton
Kr = np.genfromtxt('Krypton00000.txt')
Krx = []
Kry = []
for i in range(len(H)):
    Krx.append(Kr[i][0])
    Kry.append(Kr[i][1])
plt.figure()
plt.title("Atomic Spectra Kr")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Radiation (counts)")
plt.plot(Krx,Kry)
plt.show()
[KrPeaksx, KrPeaksy] = find_peaks(Hy, height = 5)
print("Wavelengths of peaks: ")
for i in range(len(KrPeaksx)):
    KrPeaksx[i] = Hx[KrPeaksx[i]]
print(KrPeaksx)
print("Energy Level Difference at Peaks")
KrEnergyLevelDifference = 1239.8/KrPeaksx
print(KrEnergyLevelDifference)
