import numpy as np
import matplotlib.pyplot as plt
from random import random
import q5


def p(x,y):
    return 2*x**2 + 2*y**2 + 4*x + 4*y + 3

def q(x,y):
    return x**2 + y**2 + 2*x*y + 3*x + 5*y + 4


def q7a(rx,ry):

    def findRoots(f,xRange=[-1,1],yRange=[-1,1],res=0.005,n=1000):
        xScale,yScale = xRange[1]-xRange[0],yRange[1]-yRange[0]
        xShift,yShift = xRange[0],yRange[0]
        X,Y=[],[]
        while len(X)<n:
            x = random()*xScale+xShift
            y = random()*yScale+yShift
            #print abs(f(x,y))
            if abs(f(x,y))<res:
                X,Y = np.append(X,x),np.append(Y,y)
        return X,Y

    Xp,Yp = findRoots(p,[-1.8,-0.2],[-1.8,-0.2],0.002,3000)
    Xq,Yq = findRoots(q,[-2,0.25],[-2.25,0],0.001,2000)
    plt.plot(Xp,Yp,'.',label='')
    plt.plot(Xq,Yq,'.',label='')
    plt.plot(rx,ry,'ro',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()
    #plotRoots(q,[-100,100],[-100,100],10,100)


def q7b():

    ''' Find x '''
    rx=[]

    def f(x):
        return 16*x**4 + 80*x**3 + 144*x**2 + 100*x + 19
    rx.append( q5.MullerFindRoot(f,0,1,2) ) # -1,-1.1,-1.2) )

    def g(x):
        return f(x)/(x-rx[0])
    rx.append( q5.MullerFindRoot(g,0,1,2) ) # -1,-1.1,-1.2) )

    def h(x):
        return g(x)/(x-rx[1])
    rx.append( q5.MullerFindRoot(h,0,1,2) ) # -0.25,-0.35,-0.45) )

    def j(x):
        return h(x)/(x-rx[2])
    rx.append( q5.MullerFindRoot(j,0,1,2) ) # -0.25,-0.35,-0.45) )

    print 'The roots for x:'
    for ri in rx:
        print ri



    ''' Find y '''

    ry0=[]
    def py0(y):
        return p(rx[0],y)
    ry0.append( q5.MullerFindRoot(py0,0,1,2) )
    def py0g(y):
        return py0(y)/(y-ry0[0])
    ry0.append( q5.MullerFindRoot(py0g,0,1,2) )

    ry0 = ry0[0] if abs(q(rx[0],ry0[0]))<abs(q(rx[0],ry0[1])) else ry0[1]
    print 'The roots for y0:', ry0

    ry1=[]
    def py1(y):
        return p(rx[1],y)
    ry1.append( q5.MullerFindRoot(py1,0,1,2) )
    def py1g(y):
        return py1(y)/(y-ry1[0])
    ry1.append( q5.MullerFindRoot(py1g,0,1,2) )

    ry1 = ry1[0] if abs(q(rx[0],ry1[0]))<abs(q(rx[0],ry1[1])) else ry1[1]
    print 'The roots for y1:', ry1

    return [rx[0],rx[1]],[ry0,ry1]

def main():
    rx,ry = q7b()
    q7a([],[])
    #q7a(rx,ry)

if __name__ == '__main__':
    main()


    
