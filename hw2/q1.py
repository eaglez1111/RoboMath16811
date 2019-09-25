# Dapeng Zhao (Eagle)
# dapengz@andrew.cmu.edu or tim.eagle.zhao@gmail.com
# 11 Sep 2019

import numpy as np
import matplotlib.pyplot as plt


def p(A,X,x):
    n = len(A)
    y = 0.0
    if n != len(X):
        return 0
    for i in range(n):
        yi = A[i]
        for j in range(i):
            yi *= (x-X[j])
        y += yi
    return y


def getAFromF(k,F,X,Y): #return f[x_0..x_k]
    index = FIndex(0,k)
    if len(X)<=k:
        return 0,F
    if len(F)<=index:
        F = updateF(F,X,Y)
    return (F[index],F)


def updateF(F,X,Y):
    m = len(F)
    n = len(X)
    for i in range(n):
        if m>FIndex(0,i): # f[x_0...x_i] was computed
            pass
        else:
            F=np.append(F,Y[i])
            for j in range(i):
                newF = dividedDiff( F[FIndex(i-j-1,i-1)], F[FIndex(i-j,i)], X[i-j-1], X[i] )
                F = np.append(F, newF)
    return F

def dividedDiff(f0,f1,x0,x1):
    return (f0-f1)/(x0-x1)

def FIndex(m,n):    # return the index in list 'F' corresponding to f[x_m...x_n]
    return (n+2)*(n+1)/2-(m+1)


def interpolate(X,Y,x):
    n = len(X)
    F = np.array([])
    A = np.zeros(n)
    for i in range(n):
        A[i],F = getAFromF(i,F,X,Y)
    y=np.zeros(len(x),dtype='float32')
    for i in range(len(x)):
        y[i] = p(A,X,x[i])
    return y

def q1a():
    X = np.array([0,1])
    Y = np.array([1,0])
    print interpolate(X,Y,[0,1,10])
    X = np.array([0,1,-1])
    Y = np.array([1,0,4])
    print interpolate(X,Y,[0,1,10])

def q1b():
    print '\nQ1b:'
    X = np.array([0,0.125,0.25,0.5,0.75,1],dtype='float32')
    Y = np.exp(-X)
    y = interpolate(X,Y,[1.0/3])
    print '  At x=1/3, p(x) = ', y[0]
    return 0

def q1c():
    print '\nQ1c:'
    N = [2,4,40]
    for i in range(len(N)):
        X = np.array(range(N[i]+1),dtype='float32')*2/N[i]-1
        Y = 1.0/(1+16*X**2)
        y = interpolate(X,Y,[0.05])
        print '  When n =',N[i],': p(0.05) = ', y[0]
    print '  Real f(0.05) =', 1.0/(1+16*0.05**2)

def q1d():
    print '\nQ1d:'
    N = range(2,21,2)+[40]
    Error,x_arg = np.empty(len(N),dtype='float32'),np.empty(len(N),dtype='int32')
    for i in range(len(N)):
        X = np.array(range(N[i]+1),dtype='float32')*2/N[i]-1
        Y = 1.0/(1+16*X**2)
        x = np.arange(-1,1.01,0.01)
        y = interpolate(X,Y,x)
        f = 1.0/(1+16*x**2)
        e = np.abs(f-y)
        x_arg[i] = np.argmax(e)
        Error[i] = e[x_arg[i]]
        #print '  When n =',N[i],': En = ', Error[i], 'at', x[x_arg[i]]
        print 'E_{',N[i],'} &=', Error[i], '\;\;\\text{at}\; x =', x[x_arg[i]],'\\\\'

def main():
    q1b()
    q1c()
    q1d()

    return 1


if __name__ == '__main__':
    main()
