import numpy as np
import cmath
import matplotlib.pyplot as plt
from hw2q1 import updateF

def q1b():
    def f(x):
        return ( np.sinh(x)*2 + 1.0/3 )
    X = np.arange(-3,3.1,0.1)
    Y = f(X)
    plt.plot([-3.2,3.2],[0,0],'k')
    plt.plot([0,0],[-22,22],'k')
    b = 5.4686119370669015 #3.809077479970746#3.89486#
    #plt.plot([-4,4],[1.0/3-b*4,1.0/3+b*4],'r')
    plt.plot(X,Y,'-',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()


def err(x,b=0):
    return ( 2*np.sinh(x) - ( b*x ) )

def LInfErrMu(b,itv=0.1):
    X = np.arange(-3,3+10**(-10),itv)
    return np.max(np.abs(err(X,b)))

def L2ErrNu(b,itv=0.1):
    X = np.arange(-3,3+10**(-10),itv)
    return np.sqrt( np.sum(err(X,b)**2*itv) )

def L2ErrMa(b):
    def preInt(x):
        return (np.exp(2*x)-np.exp(-2*x))/2 - 2*x -2*(np.exp(x)*b*(x-1)+np.exp(-x)*b*(x+1))+(b**2)*(x**3)/3
    return np.sqrt( preInt(3)-preInt(-3) )


def q1c():
    print "\n\n **** Q1c **** "
    def MullerFindRoot(f,xn2,xn1,xn0,res=10**-9):
        while(abs(f(xn0)) > res):
            X = np.array([xn2,xn1,xn0])
            Y = np.array([f(xn2),f(xn1),f(xn0)])
            F = updateF([],X,Y)
            q = (xn0 - xn1)/(xn1 - xn2)
            a = F[5]
            b = F[4]+F[5]*(xn0-xn1)
            c = F[3]
            r0 = xn0 - 2*c / (b+cmath.sqrt(b**2-4*a*c))
            r1 = xn0 - 2*c / (b-cmath.sqrt(b**2-4*a*c))
            r = r0 if abs(f(r0))<abs(f(r1)) else r1
            xn2,xn1,xn0 = xn1,xn0,r
        return xn0
    def f(b):
        r = 1.0*(b+cmath.sqrt(b**2-4))/2
        x = np.log(r)
        eb = r-1/r-b*x
        return np.sinh(3)*2-b*3+eb
    b=MullerFindRoot(f,1.0,1.2,2.5).real
    print '\bb=',b #b=5.38724
    print "\nMathmatical LInf:\n", err(3,b)
    print "\nNumerical LInf:\n", LInfErrMu(b,10**-5)
    print "\nMathmatical L2:\n", L2ErrMa(b)
    print "\nNumerical L2:\n", L2ErrNu(b,10**-5)

def q1d():
    print "\n\n\n\n\n **** Q1d **** "
    def fInt(x):
        return np.exp(x)*(x-1)+np.exp(-x)*(x+1)
    b=(fInt(3)-fInt(-3))/18
    print '\nb=', b
    r = np.log( [ (b+np.sqrt(b**2-4))/2, (b-np.sqrt(b**2-4))/2 ] )
    print '\nrootForZeroDErr:',r
    print "\nMathmatical LInf:\n", max(max(err(r,b)),err(3,b))
    print "\nNumerical LInf:\n", LInfErrMu(b,10**-5)
    print "\nMathmatical L2:\n", L2ErrMa(b)
    print "\nNumerical L2:\n", L2ErrNu(b,10**-5)


if __name__ == '__main__':
    q1b()
    q1c()
    q1d()
    print '\n\n\n'









#
