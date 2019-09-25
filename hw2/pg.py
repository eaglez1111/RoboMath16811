import numpy as np


def formR():
    p = np.array([1,-4,6,-4])
    q = np.array([1,2,-8])
    A = np.zeros([5,5],dtype='float32')
    A[0,0:4],A[1,1:5] = p,p
    A[2,0:3],A[3,1:4],A[4,2:5] = q,q,q
    print np.linalg.det(A)
    A1 = np.array([[-4,6,-4,0],[1,-4,6,-4],[2,-8,0,0],[1,2,-8,0]])
    A2 = np.array([[1,6,-4,0],[0,-4,6,-4],[1,-8,0,0],[0,2,-8,0]])
    print A1
    print np.linalg.det(A1)
    print A2
    print np.linalg.det(A2)


def main1():
    def f():
        print 1
    func=[f]*2
    func.append(f)



    func[0]()
    func[1]()



def svdSolve(A,b):
    U,Sigma,V = np.linalg.svd(A)
    c = np.dot(U.T,b)
    w = np.linalg.solve(np.diag(Sigma),c)
    x = np.dot(V.T,w)
    return x

def main():
    A = np.array([[10,6,4],[5,3,2],[1,1,0]],dtype='float32')
    b = np.array([2,1,-1],dtype='float32')
    print svdSolve(A,b)


if __name__ == "__main__":
    main()
