'''import sympy as sym
import numpy as np

sym.init_printing()
x,y,z = sym.symbols('x,y,z', real=True)
e,c1 = sym.symbols('c1,e')


f = sym.Eq(e**x+y,1)
g = sym.Eq(y+c1-1,1)
h = sym.Eq(x+z,3)
'''
import sympy as sym
import numpy as np

x,y,z,w = sym.symbols('x,y,z,w',real=True)

def f(x):
    return c1**(x)

f = sym.Eq(x**2,4)
g = sym.Eq(y**2,4)
h = sym.Eq(float(x==y),0)


ans=sym.solve([f,g,h],(x,y))

print ans

###########################

x1,x2,a,b,c = sym.symbols('x1,x2,a,b,c')
def f(x):
    return sym.sinh(x)*2 + 1.0/3
def p(x):
    return a+b*x+c*x**2
def e(x):
    return f(x)-p(x)
def e1(x):
    return sym.exp(x)+sym.exp(-x)-b-2*c*x
eq = []
eq.append( sym.Eq( e(3) , -e(-3) ) )
eq.append( sym.Eq( e(3) , -e(x1) ) )
eq.append( sym.Eq( e(3) , e(x2) ) )
eq.append(  )
eq.append( sym.Eq( e1(x1) , 0 ) )
eq.append( sym.Eq( e1(x2) , 0 ) )

ans=sym.solve(eq,(x1,x2,a,b,c))
print ans
