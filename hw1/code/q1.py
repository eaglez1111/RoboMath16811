import numpy as np
np.set_printoptions(suppress=True)


def lduFactorize(A_):
    A = np.copy(A_) #A_ #
    N=len(A)

    # Initialize L, D, and U
    I=np.zeros((N,N))
    for i in range(N):
        I[i,i]=1
    P = np.copy(I)
    L = np.zeros((N,N))
    D = np.copy(I)
    U = np.copy(I)

    # get P and L
    for j in range(0,N-1): #Column
        for i in range(j+1,N): #Row
            L[i,j] = A[i,j]/A[j,j]
            A[i] = A[i] - L[i,j]*A[j]
        if j<N-1 and A[j+1,j+1]==0:
            for i in range(j+2,N): #Row
                if A[i,i-1]!=0:
                    P[[j+1,i]] = P[[i,j+1]]
                    L[[j+1,i]] = L[[i,j+1]]
                    A[[j+1,i]]= A[[i,j+1]]
                    break

    # get D and U
    for i in range(N): #Row
        D[i,i] = A[i,i]
        for j in range(i,N): #Column
            U[i,j]=A[i,j]/A[i,i]

    L = L+I
    return (P,L,D,U,A)



if __name__ == "__main__":

    A1 = np.array([[4,-20,-12],[-8,45,44],[20,-105,-79]],dtype='float32')
    A2 = np.array([[3,9],[15,49]],dtype='float32')
    A3 = np.array([[4,-20,-12],[20,-105,-79],[-8,40,44]],dtype='float32')
    A4 = np.array([[4,-20,-12],[-8,40,44],[20,-105,-79]],dtype='float32')
    A5 = np.array([[4,-20,-12,-23,6],[-8,40,44,44,3],[22,77-187,20,-105,-79],[2,0,0,0,0],[1,2,3,4,5]],dtype='float32')

    A = A5

    P,L,D,U,A_upper = lduFactorize(A)

    print A_upper

    print 'P:\n',P,'\n','A:\n',A,'\n\n'
    print 'L:\n',L,'\n','D:\n',D,'\n','U:\n',U,'\n\n'

    print 'PA:\n',np.matmul(P,A)
    print 'LDU:\n',np.matmul(np.matmul(L,D),U)
