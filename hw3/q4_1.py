import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from q2 import SVD_Solve
eps = 10**(-3)

def sampleDt(data,N=20):
    sampleId = (np.random.rand(10)*len(data)).astype(int)
    return data[sampleId]

def getC(data):
    b = np.copy(data[:,2])
    A = np.copy(data)
    A[:,2] = np.ones(len(data))
    return SVD_Solve(A,b)[0]

def getZ(X,Y,C):
    return C[0]*X+C[1]*Y+C[2]

def onPlane(C,dt,d=0.1):
    return (abs(getZ(dt[0],dt[1],C)-dt[2])<d)

def score(C,data,d=0.1):
    sc = 0
    onPlaneSet = []
    for i in range(len(data)):
        if onPlane(C,data[i],d):
            sc += 1
            onPlaneSet.append(i)
    return (sc,onPlaneSet)

def getBestC(data,N=20,n=10,d=0.1):
    C,sc = [],[]
    for i in range(n):
        C.append( getC(sampleDt(data,N)) )
        sc.append( score(C[-1],data,d)[0] )
        #plotPlane(data,C[-1])
    onPlaneSet = score(C[np.argmax(sc)],data,d)[1]
    print onPlaneSet
    return getC(data[onPlaneSet])

def plotPlane(data,C):
    x,y,z = data[:,0], data[:,1], data[:,2]
    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    pX,pY=np.meshgrid(np.linspace(min(x),max(x),10),np.linspace(min(y),max(y),10))
    pZ = getZ(pX,pY,C)
    ax.plot_wireframe(pX,pY,pZ,color='c')
    ax.scatter(x,y,z,c='b',marker='.')
    plt.show()

def pltPlane(ax,C,x0,x1,y0,y1,ng):
    pX,pY=np.meshgrid(np.linspace(x0,x1,ng),np.linspace(y0,y1,ng))
    pZ = getZ(pX,pY,C)
    ax.plot_wireframe(pX,pY,pZ,color='c')
    ax.scatter(x,y,z,c='b')
    plt.show()

def iniK(K=4):
    C=[]
    C.append( np.array([1.0/eps,0,-0.5/eps]) )
    C.append( np.array([1.0/eps,0,-2/eps]) )
    C.append( np.array([0,1.0/eps,-0.5/eps]) )
    C.append( np.array([0,1.0/eps,-2/eps]) )
    return C



def q4a():
    data = np.loadtxt("clear_table.txt")
    C = getC(data)
    print C
    plotPlane(data,C)

def q4c():
    data = np.loadtxt("cluttered_table.txt")
    C = getBestC(data,20,10,0.001)
    print C
    plotPlane(data,C)
    print data


def q4d():
    data = np.loadtxt("cluttered_table.txt")
    data = np.loadtxt("clean_hallway.txt")
    C = getBestC(data,10,1000,0.05)
    print C
    plotPlane(data,C)

def q4dd():
    data = np.loadtxt("cluttered_table.txt")#data = np.loadtxt("clean_hallway.txt") #data = np.loadtxt("cluttered_hallway.txt")

    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0], data[:,1], data[:,2],c='b')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    #ax.set_xlim(0,2.5)
    #ax.set_ylim(0,2.5)
    #ax.set_zlim(1,2.6)
    plt.show()


q4dd()


#
