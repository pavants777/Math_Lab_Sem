# -*- coding: utf-8 -*-
"""
Find Beta(3,5), Gamma(5)

"""

from sympy import beta , gamma
m= input ('m :');
n= input ('n :');
m= float (m);
n= float (n);
s= beta (m,n);
t= gamma (n)
print ('gamma (',n,') is %3.3f '%t)
print ('Beta (',m,',',n,') is %3.3f '%s)
