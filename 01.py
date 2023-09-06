#Evaluate the integral ∫ ∫ ∫ (𝒙𝒚𝒛)𝒅𝒛 𝒅𝒚 𝒅𝒙 𝟑−𝒙−𝒚

"""
𝟎
𝟑−𝒙
𝟎
𝟑
𝟎
Python Code:
    """
    
from sympy import *
x,y,z=symbols('x,y,z')
w2=integrate((x*y*z),(z,0,3-x-y),(y,0,3-x),(x,0,3))
print('Answer=',w2)

