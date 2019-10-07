import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('pg.txt')

X = np.arange(0,10.01,0.1)
plt_x0, plt_x1 = 0-1,10+1
plt_y0, plt_y1 = 0-1,30+1
plt.plot([-3.2,3.2],[0,0],'k')
plt.plot([0,0],[-22,22],'k')
plt.plot(X,data,'.',label='')
plt.xlabel('x')
plt.ylabel('y')
plt.title('')
plt.ylim((plt_y0, plt_y1))
plt.xlim((plt_x0, plt_x1))
#plt.legend(loc='bottom right')
plt.show()
