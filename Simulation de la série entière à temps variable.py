import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from math import comb, factorial


def f(t, y):
    N = len(y) - 1
    z = np.concatenate((y, np.zeros(2)))
    res = np.zeros(N + 1)
    for k in range(N + 1):
        for j in range(k + 1):
            res[k] += 1/2 * comb(k, j) * z[j+1] * z[k-j+1]
        res[k] += 1/2 * z[k+2]
    return res


# seuil de troncature
N = 7
# Polynôme de degré 4 : P(x) = -x^4  ->  b_4(0) = P''''(0) = -24
y0 = np.zeros(N + 1)
y0[4] = -24


def P(x):
    return -x**4


# Euler
T = 0.3
n_t = 3000
temps = np.linspace(0, T, n_t)
h = temps[1] - temps[0]
Y = np.zeros((n_t, N + 1))
Y[0] = y0
i_max = n_t - 1                      # dernier indice avant explosion
for i in range(1, n_t):
    Y[i] = Y[i-1] + h * f(temps[i-1], Y[i-1])
    if not np.all(np.isfinite(Y[i])):
        i_max = i - 1
        print("explosion du système tronqué vers t =", temps[i])
        break

# grille en x et référence 
x_max = 2.5
n_x = 400
X = np.linspace(-x_max, x_max, n_x)

z, w = np.polynomial.hermite_e.hermegauss(200)
w = w / np.sqrt(2 * np.pi)


def u_ref(t):
    return np.array([np.sum(w * np.exp(P(x + np.sqrt(t) * z))) for x in X])


def u_serie(i):
    Z = np.zeros(n_x)
    for k in range(N + 1):
        Z += Y[i, k] * X**k / factorial(k)
    with np.errstate(over="ignore"):
        return np.exp(Z)


# animation
indices = np.linspace(0, int(0.97 * i_max), 80).astype(int)   # 80 images, on s arrete juste avant l explosion

fig, ax1 = plt.subplots(figsize=(8, 5))
l_serie, = ax1.plot([], [], lw=2, label=f"série entière (N = {N})")
l_ref, = ax1.plot([], [], "--", lw=2, label="référence Feynman-Kac")
ax1.set_xlim(-x_max, x_max); ax1.set_ylim(-0.05, 1.5)
ax1.set_xlabel("x"); ax1.set_ylabel("u(t,x)"); ax1.legend(loc="upper right")
titre = ax1.set_title("")


def update(n):
    i = indices[n]
    t = temps[i]
    l_serie.set_data(X, u_serie(i))
    l_ref.set_data(X, u_ref(t))
    titre.set_text(f"$g(x)=e^{{-x^4}}$,  t = {t:.3f}")
    return l_serie, l_ref, titre


anim = FuncAnimation(fig, update, frames=len(indices), interval=100)
fig.subplots_adjust(top=0.9, bottom=0.12)
anim.save("animation_serie_entiere.gif", writer=PillowWriter(fps=10))
plt.show()