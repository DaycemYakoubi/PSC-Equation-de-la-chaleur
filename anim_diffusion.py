import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import erf

xs = np.linspace(-5, 5, 300)
ts = np.linspace(0.02, 3, 90)

fig, ax = plt.subplots(figsize=(7, 5))
line, = ax.plot(xs, 0.5 * (1 + erf(xs / (2 * np.sqrt(ts[0])))), lw=2, color='crimson')
ax.set_ylim(0, 1)
ax.set_xlabel('x')
ax.set_ylabel('u(x,t)')
title = ax.set_title("")
ax.axhline(0.5, color='gray', lw=0.5, ls='--')

def update(frame):
    t = ts[frame]
    line.set_ydata(0.5 * (1 + erf(xs / (2 * np.sqrt(t)))))
    title.set_text(f"u(x,t) au temps t = {t:.2f}")
    return line, title

ani = animation.FuncAnimation(fig, update, frames=len(ts), interval=60, blit=False)
ani.save('diffusion.gif', writer='pillow', fps=20)
print("gif saved")
