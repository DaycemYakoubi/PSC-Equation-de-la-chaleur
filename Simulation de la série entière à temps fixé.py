import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from math import comb, factorial

def f(t, y):
    N = len(y)-1
    z = np.concatenate((y, np.zeros(2)))
    res=np.zeros(N+1)
    for k in range(N+1):
        for j in range(k+1):
            res[k]+=1/2*comb(k,j)*z[j+1]*z[k-j+1]
        res[k]+=1/2*z[k+2]
    return res

#seuil de trancature
N=20
y0=np.zeros(N+1)
'''#Polynôme de degré 1
y0[1]=1'''


'''#Polynôme de degré 2
y0[2]=-2'''

#Polynôme de degré 4
y0[4]=-24

#nombre de points de temps
n_t=1000
#intervalle de temps
T=0.1
temps=np.linspace(0,T,n_t)
Y=np.zeros((n_t,N+1))
#pas de temps
h=temps[1]-temps[0]
for i in range(0,n_t):
    if i==0:
        Y[i]=y0
    else:
        Y[i]=Y[i-1]+h*f(temps[i-1],Y[i-1])
#temps à considérer pour le plot
i_0=500
#nombre de points de l'espace
n_x=1000
#intevalle de x à considérer pour le plot
x_max=2
X=np.linspace(-x_max,x_max,n_x)
'''#Polynôme de degré 1
U_exact=np.exp(-X + temps[i_0]/2)'''
'''#Polynôme de degré 2
p0, p1, p2 = 0, 0, -1
U_exact = (1 - 2*p2*temps[i_0])**(-0.5) * np.exp(p0 + (p2*X**2 + p1*X + p1**2*temps[i_0]/2) / (1 - 2*p2*temps[i_0]))'''
#Polynôme de degré 4
def P(x):
    return -x**4

t = temps[i_0]
z, w = np.polynomial.hermite_e.hermegauss(200)   
w = w / np.sqrt(2*np.pi)                          

U_ref = np.zeros(n_x)
for i in range(n_x):
    U_ref[i] = np.sum(w * np.exp(P(X[i] + np.sqrt(t)*z)))
Z=np.zeros(n_x)
for i in range(n_x):
    for k in range(N+1):
        Z[i]=Z[i]+Y[i_0,k]*X[i]**k/factorial(k)
U=np.exp(Z)
plt.figure(figsize=(8,6))
plt.plot(X,U,label="série entière (N = %d)" % N)
plt.plot(X,U_ref, '--', label="référence Feynman-Kac")
plt.title("t = %.3f" % temps[i_0])
plt.show()

    
