import numpy as np
import matplotlib.pyplot as plt


rdm = np.random.random_sample
gsn = np.random.normal
dist = np.linalg.norm
npa = np.array

source_location = npa([[0,0],[0,10],[10,0]])


def loadPath(file):
    data = np.loadtxt(file)
    n = int(len(data)/2)
    Path = np.empty([n,len(data[0]),2])
    #X = np.empty([n,len(data[0])],dtype='float32')
    #Y = np.copy(X)
    for i in range(n):
        #X[i],Y[i]=data[i*2],data[i*2+1]
        Path[i,:,0],Path[i,:,1] = data[i*2],data[i*2+1]
    return Path[0]


def getMes(source_location, path):
    T = len(path)
    mes = np.zeros([3,T-1])
    for i in range(3):
        _d = dist(path-source_location[i],axis=1)
        mes[i] = _d[1:]-_d[0]
    return mes


def getData():
    path = loadPath('paths.txt')
    return source_location, path, getMes(source_location, path)


if __name__ == "__main__" :
    source_location, path,mes = getData()


#
