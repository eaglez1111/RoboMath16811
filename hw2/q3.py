
import numpy as np
import matplotlib.pyplot as plt

def NewtonFindRoot(f,fd,x,res=0.000001):
    f_ = f(x)
    while(np.abs(f_)>res):
        x -= f_/fd(x)
        f_ = f(x)
    return x

def q3():
    def f(x):
        return np.tan(x)-x
    def fd(x):
        return 1.0/(np.cos(x)**2)-1
    for x0 in [4.5,7.7]:
        print NewtonFindRoot(f,fd,x0)

def main():
    # Observe the plot and Manually select a starting point
    x = np.arange(0,12,0.01)
    y = np.tan(x)
    plt.plot(x,y,'.-',label='')
    plt.plot(x,x,'.-',label='')
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()

    # Newton's method
    q3()

    return 1


if __name__ == '__main__':
    main()
