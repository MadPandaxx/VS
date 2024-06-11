import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib.animation as animation

q = float(input('Nilai muatan = '))
E = float(input('Medan Listrik = '))
v0 = float(input('Kecepatan awal = '))
B = float(input('Medan Magnet = '))
x0 = float(input('Posisi awal = '))
m = float(input("Massa benda = "))

class ParticleAnimation:
    def _init_(self):
        self.t_values = []
        self.xt_values = []
        self.yt_values = []
        self.arah_values = []

        self.t = 0
        self.xt = x0

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 1000)
        self.ax.set_ylim(-100, 100)

        self.Circle1 = patches.Circle((self.xt, 10), 10, color="blue", label="Circle 1")
        self.Circle2 = patches.Circle((self.xt, -10), 10, color="black", label="Circle 2")
        self.Circle3 = patches.Circle((self.xt, 0), 10, color="red", label="Circle 3")

        self.ax.add_patch(self.Circle1)
        self.ax.add_patch(self.Circle2)
        self.ax.add_patch(self.Circle3)

        self.ani = animation.FuncAnimation(self.fig, self.update, frames=500, interval=50)

    def update(self, i):
        

        vt = v0
        Fl = q * vt * B
        Fc = q * E
        a = (Fl - Fc) / m

        if Fl > Fc:
            arah = "belok ke atas"
            self.xt = x0 + v0 * self.t + (0.5 * a * self.t ** 2)
            yt = 10
            vt = (2 * (Fc / q) / m) ** 0.5  # Calculate new velocity
            self.Circle1.set_center((self.xt, 10))
        elif Fl < Fc:
            arah = "belok ke bawah"
            self.xt = x0 + v0 * self.t + (0.5 * a * self.t ** 2)
            yt = -10
            vt = (2 * (Fc / q) / m) ** 0.5  # Calculate new velocity
            self.Circle2.set_center((self.xt, -10))
        else:
            arah = "lurus"
            self.xt = x0 + v0 * self.t
            yt = 0
            vt = v0
            self.Circle3.set_center((self.xt, 0))

        self.t_values.append(self.t)
        self.xt_values.append(self.xt)
        self.yt_values.append(yt)
        self.arah_values.append(arah)

        self.ax.set_title(f'Pergerakan Partikel - Arah: {arah}')

        if self.xt > 500:
            self.ani.event_source.stop()

        self.t += 0.5

        return self.Circle1, self.Circle2, self.Circle3

    def show_animation(self):
        plt.xlabel('Posisi pada sumbu x')
        plt.ylabel('Posisi pada sumbu y')
        plt.legend()
        plt.show()

particle_animation = ParticleAnimation()
particle_animation.show_animation()