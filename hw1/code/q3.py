import numpy as np
import q2

def getVectors(b):
    b.append(np.array([-2,2,4],dtype='float32'))
    b.append(np.array([2,1,-1],dtype='float32'))
    b.append(np.array([1,3,-1],dtype='float32'))
    return b

def getMatrices(A):
    A = q2.getMatrices(A)
    A[1]=A[2]
    return A

def SVD_Solve(A,b):
    solutionType = 1 # Type 0-NoSolution 1-OneUniqueSulotion 2-ManySolutions
    U,S_inverse,VT = q2.svdFactorize(A)
    M,N = len(A),len(A[0])
    for i in range(min(M,N)):
        if S_inverse[i,i]==0:
            solutionType = 0
        else:
            S_inverse[i,i]=1/S_inverse[i,i]
    x = np.matmul(np.matmul(np.matmul(VT.transpose(),S_inverse),U.transpose()),b)
    b_projection = np.matmul(A,x)
    for i in range(len(x)):
        x[i]=q2.truncateTrivialDigits(x[i])
        b_projection[i]=q2.truncateTrivialDigits(b_projection[i],2)
    if solutionType!=1:
        solutionType = 2*int(np.array_equal(b_projection,b))
    return x, b_projection, solutionType

def displaySVD_Solution(A,b,x,b_projection,solutionType):
    print 'SolutionType:',solutionType,'  (0:NoSolution, 1:OneUniqueSulotion, 2:ManySolutions)'
    print 'A:\n',A,'\n','b:\n',b,'\n'
    print 'x:\n',x,'\n','b_projection:\n',b_projection,'\n'

def main():
    A,b,x = [],[],[]
    A,b = getMatrices(A),getVectors(b)
    for i in range(len(A)):
        print '\n\n\n\n************ A [',i+1,'] ************\n'
        x,b_projection,solutionType = SVD_Solve(A[i],b[i])
        displaySVD_Solution(A[i],b[i],x,b_projection,solutionType)

if __name__ == "__main__":
    main()
