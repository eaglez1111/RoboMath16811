import numpy as np
from matplotlib import pyplot as plt
import sys
import q1
import q2


rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm
npa = np.array


def getEdge(ch):
    Edge = []
    n = len(ch)
    for i in range(n):
        j = (i+1)%n
        Edge.append(npa(ch[j])-npa(ch[i]))
    return Edge

def expandObstacle(CH,rb):
    CH_new = []
    Edge_rb = npa(getEdge(rb))*(-1)
    n_rb = len(Edge_rb)
    print(Edge_rb)
    for ch in CH:
        ch_new = [ ch[np.argmax(npa(ch).T[0])] ]
        Edge = np.append(Edge_rb,getEdge(ch),axis=0)
        print(Edge)

        Tht = np.arctan(Edge.T[1]/Edge.T[0]) - np.pi*(Edge.T[0]<0)
        sorted_indices = np.argsort(Tht)
        for i in sorted_indices[:-1]:
            ch_new.append(ch_new[-1]+Edge[i])
        CH_new.append(ch_new)
    return CH_new





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
        N = int(rdm()*4+8)
        X, Y = rdm(N)-1, rdm(N)-1
        robot = q1.getCH(X,Y)
        np.save('temp',(Obstacles,robot))
    else:
        (Obstacles,robot) = np.load('./map_q3.npy',allow_pickle = True)

    Obstacles_expanded = expandObstacle(Obstacles, robot)

    pStart, pEnd = robot[0], (10,10)

    Path,V,costMat = q2.getPath(pStart,pEnd,Obstacles_expanded)

    robot = npa(robot)
    plt.fill(robot.T[0],robot.T[1],'k')
    for ch in Obstacles_expanded:
        n = len(ch)
        ch = npa(ch)
        plt.fill(ch.T[0],ch.T[1],'c')
        for i in range(n):
            j = (i+1)%n
            #plt.plot(ch.T[0][[i,j]], ch.T[1][[i,j]],'-k',label='')
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
