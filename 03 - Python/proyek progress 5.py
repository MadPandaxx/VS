import numpy as np
import matplotlib.pyplot as plt

k = 1000  #konstanta pegas
m = 50 #massa
At = 0.1  #kenaikan waktu
A = 10  #amplitudo
to = 5  #waktu berhenti osilasi

t = np.arange(0, to, At)
w = np.sqrt(k / m)
Xt = A * np.cos(w * t)
v = -A * w * np.sin(w * t)
a = -A * w**2 * np.cos(w * t)


plt.plot(t, Xt, label='Simpangan (Xt)')
plt.plot(t, v, label='Kecepatan (v)')
plt.plot(t, a, label='Percepatan (a)')
plt.xlabel('Waktu (t)')
plt.ylabel('Nilai')
plt.title('Grafik Osilasi Pegas')
plt.legend()
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle, Circle

k = 1000
m = 50
At = 0.1
A = 10
to = 5

t = np.arange(0, to, At)
w = np.sqrt(k / m)
Xt = A * np.cos(w * t)
v = -A * w * np.sin(w * t)
a = -A * w**2 * np.cos(w * t)

fig, ax = plt.subplots()

line, = ax.plot([0, 0], [40, 40])
rectangle = Rectangle((0, 10), 6, 60, animated=True)
circle = plt.Circle((55, 40), 6, animated=True)

ax.add_patch(rectangle)
ax.add_artist(circle)
ax.set_xlim(0, 80)
ax.set_ylim(0, 70)
ax.set_aspect('equal')

def update(frame):
    x_rect = frame * 6
    x_circle = 55 + Xt[frame]

    rectangle.set_xy((0, 10))
    circle.set_center((x_circle, 40))

    line.set_xdata([0, x_circle])
    line.set_ydata([40, 40])

    return line, rectangle, circle

ani = FuncAnimation(fig, update, frames=len(t), blit=True)
plt.show()