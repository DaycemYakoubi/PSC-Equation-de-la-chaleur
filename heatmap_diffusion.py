import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

xs = np.linspace(-5, 5, 400)
ts = np.linspace(0.01, 3, 400)  # on évite t=0 exactement (vraie discontinuité)

X, T = np.meshgrid(xs, ts)
U = 0.5 * (1 + erf(X / (2 * np.sqrt(T))))

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.pcolormesh(xs, ts, U, shading='auto', cmap='inferno')
fig.colorbar(im, label='u(x,t)  ("température")')
ax.set_xlabel('x (position)')
ax.set_ylabel('t (temps)')
ax.set_title("Diffusion de la chaleur")
plt.tight_layout()
plt.savefig('heatmap.png', dpi=130)
print("heatmap saved")
