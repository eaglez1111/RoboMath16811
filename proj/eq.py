import numpy as np
from scipy.optimize import fsolve
import simulate_data
import matplotlib.pyplot as plt


rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm
npa = np.array

s,path,mes = simulate_data.getData()
mes += rdm([3,49])*0.1
T = len(path)
d = mes[:,:2]
distance = np.zeros(3)

def reformat(z):
    return [z[0:2],z[2:4],z[4:6]]

def Func(z):
    p = reformat(z)
    f = np.empty(6)
    for t in [1,2]:
        for i in [0,1,2]:
            f[i*2+t-1] = dist(p[t]-s[i]) - dist(p[0]-s[i]) - d[i][t-1]
    return f

def Func2(z):
    f = np.empty(2)
    for i in range(2):
        f[i] = dist(z-s[i])-distance[i]
    return f

def plotPath(paths):
    for path in paths:
        plt.plot(path[:,0],path[:,1],'.-',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()

path_solved = np.zeros([T,2])
zGuess = np.array([0.5,0.5,0.75,0.75,1,1])
z = fsolve(Func,zGuess)
path_solved[0] = z[0:2]
distance0 = dist(path_solved[0]-s,axis=1)

for i in range(1,T):
    distance = distance0 + mes[:,i-1]
    zGuess = path_solved[i-1]
    path_solved[i] = fsolve(Func2,zGuess)

plotPath([path,path_solved])
