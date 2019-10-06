import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from hw2q5 import MullerFindRoot

def q1b():
    def f(x):
        return ( np.sinh(x)*2 + 1.0/3 )
    X = np.arange(-3,3.1,0.1)
    Y = f(X)
    plt.plot([-3.2,3.2],[0,0],'k')
    plt.plot([0,0],[-22,22],'k')
    plt.plot(X,Y,'-',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()

#def q1c():
def e_x1(b):
    return np.sinh(3)*2-b*3
def f(b):
    r = 1.0*(b-np.sqrt(b**2-4))/2
    x = np.log(r)
    eb = r+1/r-b*x
    return e_x1(b)-eb
b = MullerFindRoot(f,0,1,2)
print b

if __name__ == '__main__':
    pass
