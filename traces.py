import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps,trapz
import os

f =open('Trace.txt','r')
x=[]
y=[]
g=[]
for line in f:
    tmp=line.split('\t')
    x.append(tmp[0])
    y.append(tmp[1])
    g.append(tmp[3])

f.close()

x=x[1:]
y=y[1:]
g=g[1:]

x=map(lambda x: float(x), x)
y=map(lambda x: float(x),y)
g=map(lambda x: float(x),g)

xp = np.asarray(x)
yp = np.asarray(y)
gp = np.asarray(g)

z=np.polyfit(xp,yp,8)
f=np.poly1d(z)

zg = np.polyfit(xp,gp,8)
fg=np.poly1d(zg)

# new x and y
x_new = np.linspace(xp[0],xp[-1],len(xp))
y_new=f(x_new)

yg_new=fg(x_new)

##plot
#print trapz(y_new,dx=50)

plt.plot(xp,yp,'o',x_new,y_new)
plt.plot(xp,gp,'.',x_new,yg_new)
plt.show()
