import numpy as np
from matplotlib import pyplot as plt
import q1

test_new = 0


rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm

def intersected(p0,p1,q0,q1):
    return True


if test_new:
    Obstacles = []
    N_Obstacles = int(rdm()*5+10)
    for i in range(N_Obstacles):
        N = int(rdm()*10+10)
        X, Y = rdm(N)*abs(gsn(2.5,1))+rdm()*10, rdm(N)*abs(gsn(2.5,1))+rdm()*10
        ch = q1.getCH(X,Y)
        Obstacles.append( np.array(ch) )
    np.save('Obstacles',Obstacles)
else:
    Obstacles = np.load('./Obstacles_0.npy',allow_pickle = True)

pStart, pEnd = (0,0), (10,10)
V = [pStart]
for ch in Obstacles:
    for p in ch:
        V.append(p)
V.append(pEnd)

nV = len(V)
costMat = np.inf*np.ones([nV,nV])
for i in range(nV):
    for j in range(nV):
        if

''' Plot '''
#plt.plot(X, Y,'.b',label='')
for ch in Obstacles:
    n = len(ch)
    for i in range(n):
        j = (i+1)%n
        plt.plot(ch.T[0][[i,j]], ch.T[1][[i,j]],'-r',label='')
plt.xlabel('x')
plt.ylabel('y')
plt.title('')
#plt.legend(loc='bottom right')
plt.show()
