import numpy as np
np.set_printoptions(suppress=True)

def getMatrices(A):
    A.append(np.array([[3,2,2],[2,3,-2]],dtype='float32'))
    A.append(np.array([[10,9,2],[5,3,1],[2,2,2]],dtype='float32'))
    A.append(np.array([[16,16,0,0],[4,0,-2,0],[0,1,-1,0],[0,0,0,1],[0,0,1,1]],dtype='float32'))
    A.append(np.array([[10,6,4],[5,3,2],[1,1,0]],dtype='float32'))
    return A

def svdFactorize(A):
    M,N = len(A),len(A[0])
    U,S_diag,VT = np.linalg.svd(A)
    S = np.zeros((M,N))
    for i in range(min(M,N)):
        S[i,i]=S_diag[i]
    return U,S,VT

def displaySVD(A,U,S,VT):
    print 'U:\n',U,'\n','S:\n',S,'\n','VT:\n',VT,'\n\n'
    print 'A:\n',A,'\n\n'
    print 'US(VT):\n',np.matmul(np.matmul(U,S),VT)


def main():
    A = [] # q1.getMatrices()
    A = getMatrices(A)
    for i in range(len(A)):
        print '\n\n\n\n************ A [',i,'] ************\n'
        U,S,VT = svdFactorize(A[i])
        displaySVD(A[i],U,S,VT)

if __name__ == "__main__":
    main()
