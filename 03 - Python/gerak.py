import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

q = float(input('Nilai muatan = '))
E = float(input('Medan Listrik = '))
v0 = float(input('Kecepatan awal = '))
B = float(input('Medan Magnet = '))
x0 = float(input('Posisi awal = '))
m = float(input("Massa benda = "))

print(' t       xt       yt       arah')

t_values = []
xt_values = []
yt_values = []
arah_values = []

t = 0
xt = x0
fig, ax = plt.subplots()

ax.set_xlim(0, 1000)
ax.set_ylim(-100, 100)

Circle1 = patches.Circle((xt, 10), 10, color="blue")
Circle2 = patches.Circle((xt, -10), 10, color="black")
Circle3 = patches.Circle((xt, 0), 10, color="red")

ax.add_patch(Circle1)
ax.add_patch(Circle2)
ax.add_patch(Circle3)

def update(i):
    global t, xt, v0, Circle1, Circle2, Circle3

    vt = v0
    Fl = q * vt * B
    Fc = q * E
    a = (Fl - Fc) / m

    if Fl > Fc:
        arah = "belok ke atas"
        xt = x0 + v0 * t + (0.5 * a * t ** 2)
        yt = 10
    elif Fl < Fc:
        arah = "belok ke bawah"
        xt = x0 + v0 * t + (0.5 * a * t ** 2)
        yt = -10
    else:
        arah = "lurus"
        xt = x0 + v0 * t
        yt = 0

    t_values.append(t)
    xt_values.append(xt)
    yt_values.append(yt)
    arah_values.append(arah)

    ax.set_title(f'Pergerakan Partikel - Arah: {arah}')

    Circle1.set_center((xt, 10))
    Circle2.set_center((xt, -10))
    Circle3.set_center((xt, 0))

    if xt > 500:
        ani.event_source.stop()

    t += 0.5

ani = animation.FuncAnimation(fig, update, frames=500, interval=50)

plt.xlabel('Posisi pada sumbu x')
plt.ylabel('Posisi pada sumbu y')
plt.legend()
plt.show()