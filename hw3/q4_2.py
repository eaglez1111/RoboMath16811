import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from q2 import SVD_Solve
eps = 10**(-3)
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
clr = ['c','r','y','g','k']
def sampleDt(data,N=20):
    sampleId = (np.random.rand(N)*len(data)).astype(int)
    return sampleId

def getC(data):
    b = np.ones(len(data))#np.copy(data[:,2])
    A = data#np.copy(data)
    return SVD_Solve(A,b)[0]

def getDis(C,dt):
    ans = abs(np.sum(dt*C)-1)/np.sqrt(C[0]**2+C[1]**2+C[2]**2)
    return ans

def getZ(X,Y,C):
    return (1-C[0]*X-C[1]*Y)/C[2]

def onPlane(C,dt,d=0.1):
    return getDis(C,dt)<d

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
        spl = sampleDt(data,N)
        c = getC(data[spl])
        Spl = score(c,data,d)[1]
        C.append( getC(data[Spl]) )
        sc.append( score(C[-1],data,d)[0] )
    onPlaneSet = score(C[np.argmax(sc)],data,d)[1]
    #print onPlaneSet
    return getC(data[onPlaneSet])

def getPlaneSet(data,C,d=0.01):
    setOff,setOn = [],[]
    for i in range(len(data)):
        if getDis(C,data[i])>d:
            setOff.append(i)
        else:
            setOn.append(i)
    return setOff,setOn

def get4C(_data,N=3,n=50,d=0.01,d2=0.1):
    data = np.copy(_data)
    C = []
    SetOn = []
    for i in range(4):
        C.append(getBestC(data,N,n,d))
        setOff,setOn = getPlaneSet(data,C[-1],d2)
        SetOn.append(setOn)
        ax = plotOnePlane(data[setOn],C[-1],clr[i])
        data = data[setOff]
    return C

def plotOnePlane(data,C,clr):
    #pX,pY=np.meshgrid([min(data[:,0]),max(data[:,0])],[min(data[:,1]),max(data[:,1])])
    pX,pY=np.meshgrid(np.linspace(min(data[:,0]),max(data[:,0]),10),np.linspace(min(data[:,1]),max(data[:,1]),10))
    pZ = getZ(pX,pY,C)
    ax.plot_wireframe(pX,pY,pZ,color=clr)
    return ax

def plotPlane(data,C_set,spl=[],Spl=[]):
    x,y,z = data[:,0], data[:,1], data[:,2]
    pX,pY=np.meshgrid(np.linspace(min(data[:,0]),max(data[:,0]),10),np.linspace(min(data[:,1]),max(data[:,1]),10))
    #pX,pY=np.meshgrid([min(x),max(x)],[min(y),max(y)])
    if len(C_set)==1:
        for C in C_set:
            pZ = getZ(pX,pY,C)
            ax.plot_wireframe(pX,pY,pZ,color='c') # plot_wireframe
    ax.scatter(x,y,z,c='b',marker='.')
    if not spl==[]:
        ax.scatter(Spl[:,0],Spl[:,1],Spl[:,2],c='y',marker='o')
        ax.scatter(spl[:,0],spl[:,1],spl[:,2],c='r',marker='s')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    return ax

def getAveDis(data,C):
    sum=0
    for dt in data:
        sum += getDis(C,dt)
    return sum/len(data)

def q4a():
    data = np.loadtxt("clear_table.txt")
    #data = np.loadtxt("cluttered_table.txt")

    C = getC(data)
    print C
    print "aveDis:",getAveDis(data,C)
    ax=plotPlane(data,[C])
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(0.1,0.55)
    ax.set_zlim(1.4,2.4)

def q4c():
    data = np.loadtxt("cluttered_table.txt")
    C = getBestC(data,20,10,0.01)
    print C
    ax=plotPlane(data,[C])
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(0.1,0.55)
    ax.set_zlim(1.4,2.4)

def q4de():
    data = np.loadtxt("cluttered_hallway.txt")
    #data = np.loadtxt("clean_hallway.txt")
    #C = [[0.17290822,0.07288623,0.36293502],[0.1872733,0.05990955,0.39486518],[0.25901386,-0.01574054,0.39176089],[0.01669373,  1.68261343, -0.16236896]]
    C = get4C(data,3,100,0.03,0.3)
    print C
    for i in range(4):
        setOn = getPlaneSet(data,C[i],0.3)[1]
        print "plane",i,'score:',getAveDis(data[setOn],C[i])

    ax=plotPlane(data,C)
    if len(data)>16000:
        ax.set_xlim(0,2.5)
        ax.set_ylim(0,2.5)
        ax.set_zlim(1,2.6)
    else:
        ax.set_xlim(-2.0,1.5)#ax.set_xlim(0,2.5)
        ax.set_ylim(-0.5,1.5)#ax.set_ylim(0,2.5)
        ax.set_zlim(1.5,6)#ax.set_zlim(1,2.6)
#[array([ 0.02216374,  1.69752064, -0.17077004]), array([-0.03379324, -1.8835516 ,  0.17118392]), array([ 1.0705971 ,  0.20375598, -0.14358503]), array([-0.69391627, -0.01848449,  0.08702992])]


q4a()

plt.show()

#
