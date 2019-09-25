import numpy as np
import matplotlib.pyplot as plt
from random import random


def loadPaths(file):
    data = np.loadtxt(file)
    n = len(data)/2
    Path = np.empty([n,len(data[0]),2],dtype='float32')
    #X = np.empty([n,len(data[0])],dtype='float32')
    #Y = np.copy(X)
    for i in range(n):
        #X[i],Y[i]=data[i*2],data[i*2+1]
        Path[i,:,0],Path[i,:,1] = data[i*2],data[i*2+1]
    return Path

def getWeights(X,p):
    A = np.ones([3,3],dtype='float32')
    b = np.ones(3,dtype='float32')
    A[:2,:] = np.array(X).T
    b[:2] = p
    def svdSolve(A,b):
        U,Sigma,V = np.linalg.svd(A)
        c = np.dot(U.T,b)
        w = np.linalg.solve(np.diag(Sigma),c)
        x = np.dot(V.T,w)
        return x
    return svdSolve(A,b)

def get3Nearest(Path,p):
    list = np.argsort(np.linalg.norm(Path[:,0,:]-p,2,1))[:3]
    next = 3
    w = getWeights(Path[list,0,:],p)
    while ( w[0]<0 or w[1]<0 or w[2]<0 ):
        for i in range(3):
            if w[i]<0:
                list[i] = next
                next +=1
        w = getWeights(Path[list,0,:],p)
    return w,list

def genNewTraj(Path,indices,w):
    n = len(Path[0])
    path = np.empty([n,2],dtype='float32')
    Path = Path[indices]
    for i in range(n):
        path[i]=Path[:,i].T.dot(w)
    return path

def getCordnt(path,t):
    T = len(path)
    if t<0:
        return path[0]
    if t>=T-1:
        return path[-1]
    t_int = int(t)
    print t, t_int
    t = t - t_int
    p0,p1 = path[t_int,:],path[t_int+1,:]
    x = p0[0]*(1-t)+p1[0]*(t)
    y = p0[1]*(1-t)+p1[1]*(t)
    return [x,y]

def main():
    Path = loadPaths('paths.txt')
    p0 = [ [0.8,1.8] , [2.2,1.0] , [2.7,1.4] ][0]
    w,indices = get3Nearest(Path,p0)
    pathNew = genNewTraj(Path,indices,w)
    pathDense = np.empty([0,2],dtype='float32')
    for t in np.arange(0,50.2,0.2):
        pathDense = np.append(pathDense,[getCordnt(pathNew,t)],axis=0)

    fig, ax = plt.subplots()
    for i in range(len(Path)):
        cs = 'y.-' if i in indices else 'b.-'
        if (i not in indices):
            continue # pass #
        ax.plot(Path[i,:,0],Path[i,:,1],cs,label='')
    ax.add_artist(plt.Circle((5, 5), 1.5, color='r'))
    ax.plot(pathDense[:,0],pathDense[:,1],'b.-',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()



if __name__ == '__main__':
    main()
