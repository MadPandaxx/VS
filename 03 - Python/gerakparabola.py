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
ax.set_xlim(0, 500)
ax.set_ylim(-500, 500)
ball = patches.Circle((xt, yt), 10, color="black")
ax.add_patch(ball)

def update(i):
    global t, xt, yt, v0, ball
    
    vt = v0
    Fl = q * vt * B
    Fc = q * E
    a = (Fl - Fc) / m

    if Fl > Fc:
        arah = "belok ke atas"
        xt = x0 + v0 * t
        yt = v0 * t + (0.5 * a * t ** 2)
        t += 0.1
    elif Fl < Fc:
        arah = "belok ke bawah"
        xt = x0 + v0 * t
        yt = v0 * t - (0.5 * a * t ** 2)
        t += 0.1
    else:
        arah = "lurus"
        xt = x0 + v0 * t
        yt = 0
        t += 0.1

    t_values.append(t)
    xt_values.append(xt)
    yt_values.append(yt)
    arah_values.append(arah)

    ax.set_title(f'Pergerakan Partikel - Arah: {arah}')

    ball.set_center((xt, yt))

    if xt > 500:
        ani.event_source.stop()

ani = animation.FuncAnimation(fig, update, frames=500, interval=50)
plt.xlabel('Posisi pada sumbu x')
plt.ylabel('Posisi pada sumbu y')
plt.show()