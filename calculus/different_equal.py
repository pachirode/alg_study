from __future__ import division
from sympy import *

x, y, z, t = symbols('x,y,z,t')
k, m, n = symbols('k,m,n', integer=True)
f, g, h = symbols('f,g,h', cls=Function)

print(dsolve(Eq(f(x).diff(x, 3), x ** 2 + 1)))
