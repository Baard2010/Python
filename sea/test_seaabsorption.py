# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 15:02:34 2015

@author: bard
"""

import numpy as np
import matplotlib.pyplot as plt
import seaabsorption as sea

f = 100   # f, frequency in kHz
T = 8    # T, temperature in Celsius
D = 0.05    # D, depth in km
S = 35.0    # S, salinity in ppt
pH = 8.0    # pH 

x = np.logspace(-1,3)

#x = np.linspace(0.1,1000)

a,b,m,v = sea.absorption(x,T,D,S,pH)
#a,b,m,v = sa.absorption(x)

#plt.plot(x,y)
plt.figure(facecolor='w')
plt.axes(axisbg='#CDE5FD')
plt.ylabel('Absorption [dB/km]')
plt.xlabel('Frequency [kHz]')
plt.loglog(x,v,c='red', label='Freshwater')
plt.loglog(x,a,c='black', label='Seawater')
plt.loglog(x,b,'c--', label='Boricacid contribution')
plt.loglog(x,m,'g--', label='Magnesium contribution')
plt.xlim(0.1, 1000)
plt.ylim(0.000001, 1000)
plt.grid(b=1, which='minor', axis='y', ls=':', c='0.3')
plt.grid(b=1, which='major', axis='y', ls='-', c='gray')
plt.grid(b=1, axis='x', c='grey')
plt.legend(fontsize='small', shadow='True', loc='upper left')
plt.title('Absorption in Water')


#plt.plot(RL_1, P1,'ro-', label='10 primary windings')
#plt.plot(RL_2, P2, 'bs-', color='#9295FF', label=' 5 primary windings')
#plt.grid(color='0.3')
#plt.legend(fontsize='small', shadow='True', title='RCV transformer')
#plt.title('Power dissipation in Load')

