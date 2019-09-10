import numpy as np
import q1

P=np.array([[0,0,1],[0,1,0],[1,0,0]],dtype='float32')
A=np.array([[10.0,9,2],[5,3,1],[2,2,2]],dtype='float32')
L=np.array([[1,0,0],[2.5,1,0],[5,0.5,1]],dtype='float32')
D=np.array([[2,0,0],[0,-2,0],[0,0,-6]],dtype='float32')
U=np.array([[1,1,1],[0,1,2],[0,0,1]],dtype='float32')
'''
P=np.array([[1,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,1,0,0,0]],dtype='float32')
A=np.array([[16,16,0,0],[4,0,-2,0],[0,1,-1,0],[0,0,0,1],[0,0,1,1]],dtype='float32')
L=np.array([[1.0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0.25,-4,-6,6,1]],dtype='float32')
D=np.array([[16.0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],dtype='float32')
U=np.array([[1.0,1,0,0],[0,1,-1,0],[0,0,1,1],[0,0,0,1],[0,0,0,0]],dtype='float32')
'''

P=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype='float32')
A=np.array([[10,6,4],[5,3,2],[1,1,0]],dtype='float32')
L=np.array([[1,0,0],[0.1,1,0],[0.5,0,1]],dtype='float32')
D=np.array([[10,0,0],[0,0.4,0],[0,0,1]],dtype='float32')
U=np.array([[1,0.6,0.4],[0,1,-1],[0,0,0]],dtype='float32')

q1.displayLDU(P,A,L,D,U)

def main():
    print(rad())

def rad():
    return 3

if __name__ == "__main__":
    main()
