# -*- coding: utf-8 -*-
"""
Given sin 450=0.7071, sin 500=0.7660, sin 550=0.8192, sin 600=0.8660, find
sin 570 using an appropriate interpolation formula.

"""

import numpy as np
def r_cal(r, n):
    temp = r;
    for i in range(1, n):
        temp = temp * (r + i);
    return temp;

x = np.array([0, 2, 4, 6, 8, 10],float)
y = np.array([0.15, 1.56, 2.15, 2.60, 3, 3.30],float)
print('Difference Table:')
n = len(x)
p = np.zeros([n, n+1])
for i in range(n):
    p[i, 0] = x[i]
    p[i, 1] = y[i]
for i in range(2, n+1):
    for j in range(n+1-i):
        p[j][i] = p[j + 1][i - 1] - p[j][i - 1]
for i in range(n):
    for j in range(n+1-i):
        print(round(p[i][j], 4), end = "\t")
    print("")
z = float(input('Enter the point at which you want to calculate:'))
sum = p[-1][1]
r = (z - x[-1]) / (x[1] - x[0])
for i in range(1,n):
    sum = sum + (r_cal(r, i) * p[n-(i+1)][i+1]) / np.math.factorial(i)
print("\n Value at", z, "is", round(sum, 6))
