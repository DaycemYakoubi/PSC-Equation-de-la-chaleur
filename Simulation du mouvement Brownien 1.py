import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt

t_max=10
nbr=10000
dt=t_max/nbr
T=np.linspace(0,t_max,nbr+1)
W=[0]
for i in range(1,nbr+1):
    W.append(W[-1]+np.random.normal(loc=0.0,scale=np.sqrt(dt),size=None))
plt.plot(T,W)
plt.show()