# -*- coding: utf-8 -*-
"""
Apply the Runge Kutta method to find the solution of
𝑑𝑦/𝑑𝑥 = 𝟏 + 𝑦/𝑥 at 𝑦(𝟐) taking ℎ = 𝟎. 𝟐. Given that 𝑦(𝟏) = 𝟐.

"""

from sympy import *
import numpy as np
def RungeKutta (g,x0 ,h,y0 ,xn):
 x,y= symbols ('x,y')
 f= lambdify ([x,y],g)
 print('Result by RK4 method:')
 print ('y( %3.3f'%x0,') = %3.3f '%y0)
 xt=x0+h
 Y=[y0]
 while xt<=xn:
    k1=h*f(x0 ,y0)
    k2=h*f(x0+h/2, y0+k1/2)
    k3=h*f(x0+h/2, y0+k2/2)
    k4=h*f(x0+h, y0+k3)
    y1=y0+(1/6)*(k1+2*k2+2*k3+k4)
    Y. append (y1)
    print ('y( %3.6f'%xt,') = %3.6f '%y1)
    x0=xt
    y0=y1
    xt=xt+h
 return np. round (Y,2)
RungeKutta ('1+y/x',1,0.2,2,2)
