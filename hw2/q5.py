import numpy as np
import cmath
import matplotlib.pyplot as plt

import q1

def MullerFindRoot(f,xn2,xn1,xn0,res=10**-8):
    while(abs(f(xn0)) > res):
        X = np.array([xn2,xn1,xn0])
        Y = np.array([f(xn2),f(xn1),f(xn0)])
        F = q1.updateF([],X,Y)

    	q = (xn0 - xn1)/(xn1 - xn2)
    	a = F[5]
    	b = F[4]+F[5]*(xn0-xn1)
        c = F[3]
    	r0 = xn0 - 2*c / (b+cmath.sqrt(b**2-4*a*c))
    	r1 = xn0 - 2*c / (b-cmath.sqrt(b**2-4*a*c))

        r = r0 if abs(f(r0))<abs(f(r1)) else r1
    	xn2,xn1,xn0 = xn1,xn0,r
    return xn0



def q5():

    r=[]

    def f(x):
        return x**3 - 5*x**2 + 11*x - 15
    r.append( MullerFindRoot(f,2.5,3.5,4.5) )

    def g(x):
        return f(x)/(x-r[0])
    r.append( MullerFindRoot(g,0,1,2) )

    def h(x):
        return g(x)/(x-r[1])
    r.append( MullerFindRoot(h,0,1,2) )

    print 'The roots are:\n',r



def main():
    q5()


if __name__ == '__main__':
    main()
