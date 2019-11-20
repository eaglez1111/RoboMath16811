import numpy as np
from matplotlib import pyplot as plt
import sys
import q1


rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm
npa = np.array


def inPolygon(p,CH):
    N = len(CH)
    for ch in CH:
        if p[0] in npa(ch).T[0]: continue
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
        if p0[0] in npa(ch).T[0] and p1[0] in npa(ch).T[0]:
            a, b, n = np.argwhere(npa(ch).T[0]==p0[0]), np.argwhere(npa(ch).T[0]==p1[0]), len(ch)
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


def updateCost(ind, cost, costLocal,preceedingNodeList):
    for i in range(len(cost)):
        costNew = cost[ind]+costLocal[i]
        if costNew<cost[i]:
            cost[i] = costNew
            preceedingNodeList[i] = ind


def getPath(pStart,pEnd,Obstacles):
    ''' Find all reachable vertices '''
    V = [pStart]
    for ch in Obstacles:
        for p in ch:
            if not inPolygon(p,Obstacles):
                V.append(tuple(p))
    V.append(pEnd)
    nV = len(V)

    ''' Build weighted visiblity graph '''
    costMat = np.inf*np.ones([nV,nV])
    for i in range(nV):
        for j in range(nV):
            if i==j:
                costMat[i,j] = 0
                continue
            cpFlag = commonPolygon(V[i],V[j],Obstacles) # 1 means same polygon not neighboring, 2 means same polygon and neighboring, 0 means different polygon
            if cpFlag==1:
                continue
            if ( cpFlag==0 or cpFlag==2 ) and (not isFreePath(V[i],V[j],Obstacles)):
                continue
            _d = dist(npa(V[i])-npa(V[j]))
            costMat[i,j] = _d
            costMat[j,i] = _d

    ''' Dijkstra '''
    S, U = [0], list(range(1,nV))
    cost = np.inf*np.ones(nV)
    preceedingNodeList = [-1]*nV
    cost[0] = 0
    while(len(U)>0):
        updateCost(S[-1],cost,costMat[S[-1]],preceedingNodeList)
        bestNode_id = np.argmin(cost[U])
        S.append(U[bestNode_id])
        del U[bestNode_id]

    ''' Back trace to find the path '''
    Path = [nV-1]
    while(Path[-1]!=0):
        Path.append(preceedingNodeList[Path[-1]])

    return Path, V, costMat





''' Test '''

if __name__ == "__main__":

    try: newMap = sys.argv[1]
    except: newMap = 0

    if newMap:
        Obstacles = []
        N_Obstacles = int(rdm()*5+10)
        for i in range(N_Obstacles):
            N = int(rdm()*10+10)
            X, Y = rdm(N)*abs(gsn(2.5,1))+rdm()*10, rdm(N)*abs(gsn(2.5,1))+rdm()*10
            ch = q1.getCH(X,Y)
            Obstacles.append( np.array(ch) )
        np.save('temp',Obstacles)
    else:
        Obstacles = np.load('./map_q2.npy',allow_pickle = True)

    pStart, pEnd = (0,0), (10,10)

    Path,V,costMat = getPath(pStart,pEnd,Obstacles)

    for ch in Obstacles:
        n = len(ch)
        plt.fill(ch.T[0],ch.T[1],'y')
        for i in range(n):
            j = (i+1)%n
            plt.plot(ch.T[0][[i,j]], ch.T[1][[i,j]],'-k',label='')
    for i in range(len(V)):
        for j in range(i,len(V)):
            if costMat[i,j]<np.inf:
                plt.plot([V[i][0],V[j][0]], [V[i][1],V[j][1]],'-g',label='')
    for i in range(len(Path)-1):
        V = npa(V)
        Path = npa(Path)
        plt.plot(V.T[0][Path[[i,i+1]]], V.T[1][Path[[i,i+1]]],'-r',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()
