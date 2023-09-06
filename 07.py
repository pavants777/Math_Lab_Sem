# -*- coding: utf-8 -*-
"""
Evaluate approximately ∫
𝟏
𝟏+𝒙
𝟐 𝒅𝒙 𝟏
𝟎
by Trapezoidal Rule.

"""

def f(x):
 return 1/(1 + x**2)
def trapezoidal(x0,xn,n):
 h = (xn - x0) / n
 integration = f(x0) + f(xn)

 for i in range(1,n):
  k = x0 + i*h
  integration = integration + 2 * f(k)
 integration = integration * h/2
 return integration
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )
