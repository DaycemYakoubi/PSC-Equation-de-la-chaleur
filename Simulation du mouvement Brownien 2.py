import numpy as np
import matplotlib.pyplot as plt



t_max = 10
n = 20000

Y=np.random.choice([-1,1],size=n)
S=np.cumsum(Y)
T=np.linspace(0,t_max,n)
W_div_n=S/n
W_div_sqrt_n=S/np.sqrt(n)
W_no_scaling=S.astype(float)

ymin, ymax = W_div_sqrt_n.min(), W_div_sqrt_n.max()
marge = 0.1 * (ymax - ymin)
ylim = (ymin - marge, ymax + marge)

fig,axes=plt.subplots(3,1,sharex=True,sharey=True,figsize=(8, 9))
axes[0].plot(T,W_div_n)
axes[0].set_title("Divisé par n")
axes[1].plot(T,W_div_sqrt_n)
axes[1].set_title("Divisé par √n")
axes[2].plot(T,W_no_scaling)
axes[2].set_title("Pas de scaling")

for ax in axes:
    ax.set_ylim(ylim)

plt.tight_layout()
plt.show()