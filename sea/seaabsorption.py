# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 12:54:14 2015

@author: bard
"""
#import argparse
#parser = argparse.ArgumentParser()
#parser.parse_args()


# Seawater absorption, Ainslie and McColm
def absorption(f=100,T=8,D=0.05,S=35.0,pH=8.0):
    """ Seawater absorption, Ainslie and McColm
    
    Keyword arguments:
    f -- frequency in kHz (default 100.0)
    T -- temperature in Celsius (default 8.0)
    D -- depth in km (default 0.05)
    S -- salinity in ppt (default 35.0)
    pH -- acidity (default 8.0)
    """
  
    from math import exp, sqrt

    # viscous absorption, α as a function of f, T and D"
    viscousabsorption = 0.00049 * f**2 * exp(-T/27.0 - D/17.0) # dB/km

    # Boric acid relaxation frequency, kHz
    f1 = 0.78 * sqrt(S/35.0) * exp(T/26.0)

    # Magnesium sulphate relaxation frequency, kHz
    f2 = 42 * exp(T/17.0)

    boricacid = 0.106 * exp((pH-8.0)/0.56) * \
                ((f1 * f**2)/(f1**2 + f**2))
                
    magnesium = 0.52 * (1+T/43.0) * (S/35.0) * exp(-D/6.0) * \
                ((f2 * f**2)/(f2**2 + f**2))

    absorbed =  boricacid + magnesium + viscousabsorption
                
    #print(absorbed)
    #return absorbed
    return absorbed,boricacid,magnesium,viscousabsorption

if __name__ == "__main__":
    import sys
    numArg = len(sys.argv)
    if numArg == 2:
        a,b,m,v = absorption(float(sys.argv[1]))    
    if numArg == 3:
        a,b,m,v = absorption(float(sys.argv[1]), \
        float(sys.argv[2]))
    if numArg == 4:
        a,b,m,v = absorption(float(sys.argv[1]), \
        float(sys.argv[2]), \
        float(sys.argv[3]))
    if numArg == 5:
        a,b,m,v = absorption(float(sys.argv[1]), \
        float(sys.argv[2]), \
        float(sys.argv[3]), \
        float(sys.argv[4]))
    if numArg == 6:
        a,b,m,v = absorption(float(sys.argv[1]), \
        float(sys.argv[2]), \
        float(sys.argv[3]), \
        float(sys.argv[4]), \
        float(sys.argv[5]))
    print 'Absorption = ', a, ' dB/km'

