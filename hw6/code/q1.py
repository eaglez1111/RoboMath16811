import numpy as np
from matplotlib import pyplot as plt

''' Helper Functions '''
def isLeft(p0,p1,p2):
    return (p0[0]*p1[1]+p2[0]*p0[1]+p1[0]*p2[1]-p2[0]*p1[1]-p1[0]*p0[1]-p0[0]*p2[1])>0


''' get Convex Hull'''
def getCH(X,Y):
    N = len(X)
    p0_ind = np.argmin(X)
    p0 = (X[p0_ind],Y[p0_ind])
    X, Y = np.delete(X,p0_ind), np.delete(Y,p0_ind)

    Tht = (Y-p0[1])/(X-p0[0])
    ind = np.argsort( Tht )
    X, Y = X[ind], Y[ind]

    p1 = (X[0],Y[0])
    X, Y, Tht = np.delete(X,0), np.delete(Y,0), np.delete(Tht,0)

    ch = [p0,p1]
    i = 0
    while i<N-2:
        if isLeft(ch[-2],ch[-1],(X[i],Y[i])):
            ch.append((X[i],Y[i]))
            i+=1
        else:
            ch.pop()
    return ch




if __name__ == "__main__":
    ''' Test '''
    N = 100000
    X, Y = np.random.random_sample(N)*3.5, np.random.random_sample(N)*3.5
    X, Y = np.sin(Y) , Y + np.exp(X)


    ch = getCH(X,Y)
    ch = np.array(ch)


    ''' Plot '''
    plt.plot(X, Y,'.b',label='')
    n = len(ch)
    for i in range(n):
        j = (i+1)%n
        plt.plot(ch.T[0][[i,j]], ch.T[1][[i,j]],'-r',label='')
    plt.fill(ch.T[0],ch.T[1],'y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()

    plt.plot(X, Y,'.b',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    #plt.legend(loc='bottom right')
    plt.show()
