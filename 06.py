# -*- coding: utf-8 -*-
"""
Verify that Beta(m, n) = Gamma(m)Gamma(n)/Gamma(m + n) for
 m=5 and n=7
"""

from sympy import beta , gamma
m=5;
n=7;
m= float (m);
n= float (n);
s= beta (m,n);
t=( gamma (m)* gamma (n))/ gamma (m+n);
print('LHS = Beta(m,n)=',s,'\nRHS = Gamma(m)*Gamma(n))/Gamma(m+n)=',t)
if (abs (s-t)<=0.00001 ):
 print ('Beta and Gamma are related ')
else :
 print ('Given values are wrong ')


