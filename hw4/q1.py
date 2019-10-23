# Dapeng Zhao (Eagle)
# dapengz@andrew.cmu.edu or tim.eagle.zhao@gmail.com

import numpy as np

rt2 = np.sqrt(2)

''' Implemented Functions '''

def em(x0,y0,f,h,interval):
    n = int(interval/h)+1
    x = np.arange(n)*h+x0
    y = np.empty(n)
    y[0] = y0
    for i in range(n-1):
        y[i+1] = y[i]+f(x[i],y[i])*h
    return x,y

def rk(x0,y0,f,h,interval):
    n = int(interval/h)+1
    x = np.arange(n)*h+x0
    y = np.empty(n)
    y[0] = y0
    for i in range(n-1):
        k1 = h*f(x[i],y[i])
        k2 = h*f(x[i]+h/2,y[i]+k1/2)
        k3 = h*f(x[i]+h/2,y[i]+k2/2)
        k4 = h*f(x[i]+h,y[i]+k3)
        y[i+1] = y[i]+1.0/6*(k1+2*k2+2*k3+k4)
    return x,y

def ab(x0,y0,f,h,interval):
    n = int(interval/h)+1
    x = np.arange(n)*h+x0
    y = np.empty(n)
    y[0] = y0
    fn, fn_1, fn_2 = f(2.05,1.44913767461894), f(2.10,1.48323969741913), f(2.15,1.51657508881031)
    for i in range(n-1):
        fn_1, fn_2, fn_3 = fn, fn_1, fn_2
        fn = f(x[i],y[i])
        y[i+1] = y[i]+h/24*(55*fn-59*fn_1+37*fn_2-9*fn_3)
    return x,y

def printTheTable(x,y,realY):
    for i in range(len(x)):
        yxi = realY(x[i])
        print ('%4.2f & %4.2f & %4.2f & %4.2e \\\\'%(x[i],yxi,y[i],yxi-y[i]) if(i!=0) \
                else '%4.2f & %4.2f & %4.2f & %.2f \\\\'%(x[i],yxi,y[i],0))


''' Inputs from homework question '''

x0, y0 = 2, rt2
h = -0.05
interval = -1

def f(x,y):
    return 1/x

def realY(x):
    return np.log(x)+rt2-np.log(2)


''' Solutions '''
if __name__ == "__main__":
    q1_function = [em,rk,ab]
    for f_i in q1_function:
        x,y = f_i(x0,y0,f,h,interval)
        printTheTable(x,y,realY)
        print '\n\n\n\n'
