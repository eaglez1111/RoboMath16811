import numpy as np
import matplotlib.pyplot as plt


def svdFactorize(A):
    M,N = len(A),len(A[0])
    U,S_diag,VT = np.linalg.svd(A)
    S = np.zeros((M,N))
    for i in range(min(M,N)):
        #S_diag[i]=truncateTrivialDigits(S_diag[i])
        S[i,i]=S_diag[i]
    return U,S,VT


def SVD_Solve(A,b):
    solutionType = 1 # Type 0-NoSolution 1-OneUniqueSulotion 2-ManySolutions
    U,S_inverse,VT = svdFactorize(A)
    M,N = len(A),len(A[0])
    for i in range(min(M,N)):
        if S_inverse[i,i]==0:
            solutionType = 0
        else:
            S_inverse[i,i]=1/S_inverse[i,i]
    S_inverse = S_inverse.transpose()
    x = np.matmul(np.matmul(np.matmul(VT.transpose(),S_inverse),U.transpose()),b)
    b_projection = np.matmul(A,x)
    if solutionType!=1:
        solutionType = 2*int(np.array_equal(b_projection,b))
    return x, b_projection, solutionType

def getLSP(X,b):
    A = np.array([np.ones(len(b)),X,X**2,X**3,X**4,X**5]).transpose()
    C,_v0,_v1 = SVD_Solve(A,b)
    return C

def p(X,C):
    return C[0] + C[1]*X + C[2]*X**2 + C[3]*X**3 + C[4]*X**4 + C[5]*X**5

if __name__ == "__main__":
    data = np.loadtxt('pg.txt')
    X = np.arange(0,10.01,0.1)
    X0,b0 = X[:31],data[:31]
    C0 = getLSP(X0,b0)
    print C0
    X1,b1 = X[30:],data[30:]
    C1 = getLSP(X1,b1)
    print C1

    plt_x0, plt_x1 = 0-1,10+1
    plt_y0, plt_y1 = 0-1,30+1
    plt.plot([-3.2,3.2],[0,0],'k')
    plt.plot([0,0],[-22,22],'k')
    plt.plot(X,data,'.',label='')
    plt.plot(X0,p(X0,C0),'r-',label='')
    plt.plot(X1,p(X1,C1),'r-',label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('')
    plt.ylim((plt_y0, plt_y1))
    plt.xlim((plt_x0, plt_x1))
    #plt.legend(loc='bottom right')
    plt.show()




#
