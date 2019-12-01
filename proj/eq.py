import numpy as np
from scipy.optimize import fsolve
import simulate_data

rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm
npa = np.array

s,path,d = simulate_data.getData()


roots = []

def getDenom(z,roots):
    res = 1
    for i in range(len(roots)):
        r = roots[i]
        res *= np.prod(z-r)
    print(res)
    return res


def myFunction(z):
    p = [z[0:2],z[2:4],z[4:6]]
    f = np.empty(6)
    for t in [1,2]:
        for i in [0,1,2]:
            f[i*2+t-1] = dist(p[t]-s[i]) - dist(p[0]-s[i]) - d[i][t-1]
    return f

def myFunction2(z):
    f = myFunction(z)
    f = 1.0*f/getDenom(z,roots)
    return f

def getRoot():
    zGuess = np.array([0,0,0,0,0,0])
    z = fsolve(myFunction2,zGuess)
    print(z)
    print('err:',myFunction(z))
    print('err2:',myFunction2(z))
    roots.append(z)
    return z
