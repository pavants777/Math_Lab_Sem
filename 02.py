"""
:Find the volume of the tetrahedron bounded by the planes
𝒙 = 𝟎, 𝒚 = 𝟎 𝒂𝒏𝒅 𝒛 = 𝟎,
"""

from sympy import*
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
w2 = integrate (1 ,(z,0,c*(1-x/a-y/b)) ,(y,0,b*(1-x/a)) ,(x,0,a))
print ('Answer=',w2)
