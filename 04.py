# -*- coding: utf-8 -*-
"""
Apply Milne’s predictor and corrector method to solve
𝑑𝑦
𝑑𝑥
= 𝑥
2 +
𝑦
2
at 𝑦(1.4). Given that 𝑦(1) = 2, 𝑦(1.1) = 2.2156, 𝑦(1.2) = 2.4649, 𝑦(1.3) = 2.7514.
Use corrector formula thrice.

"""

x0=1
y0=2
y1=2.2156
y2=2.4649
y3=2.7514
h=0.1
x1=x0+h
x2=x1+h
x3=x2+h
x4=x3+h
def f(x,y):
 return x ** 2+(y/2)
y10 =f(x0 , y0)
y11 =f(x1 ,y1)
y12 =f(x2 ,y2)
y13 =f(x3 ,y3)
y4p =y0+(4*h/3)*(2*y11-y12+2*y13)
print ('Predicted value of y4 is %3.3f '% y4p)
y14 =f(x4 ,y4p );
for i in range (1,4):
    y4=y2+(h/3)*(y14 +4*y13 +y12 );
    print('Corrected value of y4 after \t iteration %d is \t %3.5f\t'%(i,y4))
    y14=f(x4 ,y4);
