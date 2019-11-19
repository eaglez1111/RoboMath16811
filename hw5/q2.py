import numpy as np
from matplotlib import pyplot as plt
import q1

test_new = 0


rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm
npa = np.array

def inPolygon(p,CH):
    N = len(CH)
    for ch in CH:
        if p in ch: continue
        n = len(ch)
        inFlag = 1
        for j in range(n):
            k = (j+1)%n
            inFlag *= q1.isLeft(ch[j],ch[k],p)
        if inFlag:
            return True
    return False

def commonPolygon(p0,p1,CH):
    N = len(CH)
    for ch in CH:
        if p0 in ch and p1 in ch:
            a, b, n = np.argwhere(ch.T[0]==p0[0]), np.argwhere(ch.T[0]==p1[0]), len(ch)
            if (a==0 and b==n-1) or (b==0 and a==n-1) or (abs(a-b)==1):
                return 2
            else:
                return 1
    return 0

def intersected(p1,p2,p3,p4):  # line p1-p2 and line p3-p4
    if p1[0]==p3[0] or p1[0]==p4[0] or p2[0]==p3[0] or p2[0]==p4[0]:
        return False
    x_1, y_1 = p1
    x_2, y_2 = p2
    x_3, y_3 = p3
    x_4, y_4 = p4
    ta = ( (y_3 - y_4)*(x_1 - x_3) + (x_4 - x_3)*(y_1 - y_3) ) / ( (x_4 - x_3)*(y_1 - y_2) - (x_1 - x_2)*(y_4 - y_3) )
    tb = ( (y_1 - y_2)*(x_1 - x_3) + (x_2 - x_1)*(y_1 - y_3) ) / ( (x_4 - x_3)*(y_1 - y_2) - (x_1 - x_2)*(y_4 - y_3) )
    return ( ta>=0 and ta<=1 and tb>=0 and tb<=1 )


def isFreePath(p0,p1,CH):
    for ch in CH:
        n = len(ch)
        for j in range(n):
            k = (j+1)%n
            if intersected(ch[j],ch[k],p0,p1):
                return False
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
        if not inPolygon(p,Obstacles):
            V.append(tuple(p))
V.append(pEnd)


nV = len(V)
costMat = np.inf*np.ones([nV,nV])
for i in range(nV):
    for j in range(nV):
        if i==j:
            costMat[i,j] = 0
            continue
        cpFlag = commonPolygon(V[i],V[j],Obstacles) # 1 means same polygon not neighboring, 2 means same polygon and neighboring, 0 means different polygon
        if cpFlag==1:
            continue
        if cpFlag==0 and (not isFreePath(V[i],V[j],Obstacles)):
            continue
        d_ = dist(npa(V[i])-npa(V[j]))
        costMat[i,j] = d_
        costMat[j,i] = d_



''' Dijkstra '''
cost = np.inf*np.ones(nV)
S, U = [V[0]], V[1:]
cost[0] = 0
while(len(U)>0):
    updateCost(p,)



''' Plot '''
#plt.plot(X, Y,'.b',label='')
for ch in Obstacles:
    n = len(ch)
    for i in range(n):
        j = (i+1)%n
        plt.plot(ch.T[0][[i,j]], ch.T[1][[i,j]],'-b',label='')
for i in range(len(V)):
    plt.plot(V[i][0], V[i][1],'*r',label='')
    plt.text(V[i][0], V[i][1],str(i),label='')
    for j in range(i,len(V)):
        if costMat[i,j]<np.inf:
            plt.plot([V[i][0],V[j][0]], [V[i][1],V[j][1]],'-g',label='')
plt.xlabel('x')
plt.ylabel('y')
plt.title('')
#plt.legend(loc='bottom right')
plt.show()
