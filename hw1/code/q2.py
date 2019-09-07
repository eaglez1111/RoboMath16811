import numpy as np
np.set_printoptions(suppress=True)

def getMatrices(A):
    A.append(np.array([[10,9,2],[5,3,1],[2,2,2]],dtype='float32'))
    A.append(np.array([[16,16,0,0],[4,0,-2,0],[0,1,-1,0],[0,0,0,1],[0,0,1,1]],dtype='float32'))
    A.append(np.array([[10,6,4],[5,3,2],[1,1,0]],dtype='float32'))
    return A

def svdFactorize(A):
    M,N = len(A),len(A[0])
    U,S_diag,VT = np.linalg.svd(A)
    S = np.zeros((M,N))
    for i in range(min(M,N)):
        I[i,i]=1

    return U,S,VT

def displayLDU(P,A,L,D,U):
    print 'P:\n',P,'\n','A:\n',A,'\n\n'
    print 'L:\n',L,'\n','D:\n',D,'\n','U:\n',U,'\n\n'
    print 'PA:\n',np.matmul(P,A)
    print 'LDU:\n',np.matmul(np.matmul(L,D),U)


def main():
    A = [] # q1.getMatrices()
    A = getMatrices()
    for i in range(len(A)):
        P,L,D,U,A_upper = lduFactorize(A[i])



if __name__ == "__main__":
    main()
