import q2
import q3
import numpy as np
from random import random

def genTransMat(rand=1,ax=0,ay=0,az=0,tx=0,ty=0,tz=0): #ax is the Angle rotating around x-axis, tx is the translation on x-axis
    if rand:
        ax,ay,az = random()*np.pi*2,random()*np.pi*2,random()*np.pi*2
        tx,ty,tz = random()*2000-1000,random()*2000-1000,random()*2000-1000
    M = np.zeros([4,4],dtype='float32')
    M[0,0],M[0,1],M[0,2] = c(ay)*c(az),                     -c(ay)*s(az),                       s(ay)
    M[1,0],M[1,1],M[1,2] = s(ax)*s(ay)*c(az) + c(ax)*s(az), -s(ax)*s(ay)*s(az) + c(ax)*c(az),   -s(ax)*c(ay)
    M[2,0],M[2,1],M[2,2] = -c(ax)*s(ay)*s(az) + s(ax)*s(az), c(ax)*s(ay)*s(az) + s(ax)*c(az),   c(ax)*c(ay)
    M[0,3],M[1,3],M[2,3] = tx,ty,tz
    M[3,0],M[3,1],M[3,2],M[3,3] = 0,0,0,1
    return M,ax,ay,az,tx,ty,tz

def genPQ(M,length):
    P,Q = np.zeros([length,3],dtype='float32'),np.zeros([length,3],dtype='float32')
    for i in range(length):
        P[i,0],P[i,1],P[i,2] = random()*2000-1000,random()*2000-1000,random()*2000-1000
        Q[i] = np.matmul(M,np.append(P[i],1))[0:3]
    return P,Q

def getMean(X):  # X is nx3 matrix, return an array
    return np.average(X,axis=0)

def getXY(P,Q,p_mean,q_mean):
    X = (P-p_mean).transpose()
    Y = (Q-q_mean).transpose()
    return X,Y

def getR(X,Y):
    S=np.matmul(X,Y.transpose())
    U,Sigma,VT = q2.svdFactorize(S)
    det = np.linalg.det(np.matmul(VT.transpose(),U.transpose()))
    print 'det:',det
    I_ = np.array([[1,0,0],[0,1,0],[0,0,det]],dtype='float32')
    R = np.matmul( np.matmul(VT.transpose(),I_) , U.transpose() )
    return R

def get_t(p_mean,q_mean,R):
    return (q_mean.transpose()-np.matmul(R,p_mean.transpose()))


def main():
    M,ax,ay,az,tx,ty,tz = genTransMat() # genTransMat(0,rad(45),0,0,1,1,1) #
    print 'Rotation Matrix R:\n', M[:3,:3]
    print 'Translation Vector t:\n', M[:3,3:4]
    P,Q = genPQ(M,5)
    print '\n\nData set (before & after transformation)'
    for i in range(len(P)):
        print P[i], ' -> ', Q[i]

    p_mean,q_mean = getMean(P),getMean(Q)
    print 'Mean:\n',p_mean,'\n',q_mean

    X,Y = getXY(P,Q,p_mean,q_mean)
    print 'X^T&Y^T:\n',X.transpose(),'\n',Y.transpose()

    R = getR(X,Y)
    t = get_t(p_mean,q_mean,R)
    print '\n\nCaculated R:'
    print R
    print '\n\nCaculated t:'
    print t.transpose()


def s(x):
    return np.sin(x)

def c(x):
    return np.cos(x)

def deg(rad):
    return 1.0*rad*180/np.pi

def rad(deg):
    return 1.0*deg/180*np.pi


'''
# Wrong Approach for Finding the Best Affine Matrix #

def formAb(P,Q):
    length = len(P)
    A,b = np.zeros([length*3,12],dtype='float32'),np.zeros([length*3],dtype='float32')
    for i in range(length):
        b[i*3:i*3+3] = Q[i]
        for j in range(3):
            A[i*3+j,j*4:j*4+4] = np.append(P[i],1)
    return A,b

def constructM(x):
    M = np.zeros([4,4],dtype='float32')
    M[0,0],M[0,1],M[0,2] = x[0], x[1], x[2] # Rotation row1
    M[1,0],M[1,1],M[1,2] = x[4], x[5], x[6] # Rotation row2
    M[2,0],M[2,1],M[2,2] = x[8], x[9], x[10] # Rotation row3
    M[0,3],M[1,3],M[2,3] = x[3], x[7], x[11] # Translation
    M[3,0],M[3,1],M[3,2],M[3,3] = 0,0,0,1 # row4
    return M
'''


if __name__ == "__main__":
    main()
