# Dapeng Zhao (Eagle)
# dapengz@andrew.cmu.edu or tim.eagle.zhao@gmail.com

import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(0-0.5, 4.0/3+0.5, 1000)
ylist = np.linspace(-2-0.5, 0+0.5, 100)
X, Y = np.meshgrid(xlist, ylist)

Z =  X**3 + Y**3 - 2*X**2 + 3*Y**2 - 8
print np.min(Z),np.max(Z)

plt.figure()

levels = np.linspace(-9.2,-4,26*2+1)
contour = plt.contour(X, Y, Z, levels, colors='k')
plt.clabel(contour, colors = 'k', fmt = '', fontsize=12) # , fmt = '%2.1f'
contour_filled = plt.contourf(X, Y, Z, levels)
plt.colorbar(contour_filled)

plt.title('iso-contours')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



''' Solutions '''
if __name__ == "__main__":
    pass
