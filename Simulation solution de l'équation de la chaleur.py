import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

def f(y):
    return (y>0).astype(float)

t=1.0
N=100000
xs=np.linspace(-3,3,100)

u_exact=0.5*(1+erf(xs/(2*np.sqrt(t))))

u_mc=[]
for x in xs:
    Wt=np.random.normal(loc=x,scale=np.sqrt(2*t),size=N)  
    u_mc.append(np.mean(f(Wt)))

plt.plot(xs,u_exact,label="solution exacte (intégrale)")
plt.plot(xs,u_mc,'.',label="Monte Carlo (simulation)",alpha=0.5)
plt.legend()
plt.show()