import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
yt = 0

fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(-100, 100)

ball = patches.Circle((xt, yt), 10, color="blue")
ball2 = patches.Circle((xt, -10), 10, color="black")
ball3 = patches.Circle((xt, 0), 1, color="red")

ax.add_patch(ball)
ax.add_patch(ball2)
ax.add_patch(ball3)

def update(i):
    global t, xt, yt, v0, ball

    vt = v0
    Fl = q * vt * B
    Fc = q * E
    a = (Fl - Fc) / m

    if Fl > Fc:
        arah = "belok ke atas"
    elif Fl < Fc:
        arah = "belok ke bawah"
    else:
        arah = "lurus"

    xt = x0 + v0 * t + (0.5 * a * t ** 2)
    yt = v0 * t + (0.5 * a * t ** 2)  # Adjust the y-coordinate to move upwards

    t_values.append(t)
    xt_values.append(xt)
    yt_values.append(yt)
    arah_values.append(arah)

    ax.set_title(f'Pergerakan Partikel - Arah: {arah}')

    ball.set_center((xt, yt))

    if xt > 500:
        ani.event_source.stop()

    t += 0.5

ani = animation.FuncAnimation(fig, update, frames=500, interval=50)
plt.xlabel('Posisi pada sumbu x')
plt.ylabel('Posisi pada sumbu y')
plt.show()