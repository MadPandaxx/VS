import ipywidgets as widgets
import numpy as np

# Skor awal
player_score = 0
computer_score = 0

# Fungsi untuk menentukan hasil permainan
def determine_result(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        return "Seri"
    elif (player_choice == "batu" and computer_choice == "gunting") or \
         (player_choice == "gunting" and computer_choice == "kertas") or \
         (player_choice == "kertas" and computer_choice == "batu"):
        player_score += 1
        if player_score == 10:
            return "Anda Menang!"
        else:
            return "Anda Menang ronde ini!"
    else:
        computer_score += 1
        if computer_score == 10:
            return "Anda Kalah!"
        else:
            return "Komputer Menang ronde ini!"

# Fungsi yang akan dipanggil saat tombol ditekan
def play_game(choice):
    global player_score, computer_score
    if player_score == 10 or computer_score == 10:
        output_label.value = "Permainan telah berakhir. Silakan klik tombol 'Mainkan!' untuk memulai kembali."
        player_score = 0
        computer_score = 0
    else:
        player_choice = choice
        computer_choice = np.random.choice(["batu", "gunting", "kertas"])
        result = determine_result(player_choice, computer_choice)
        output_label.value = f"Anda memilih: {player_choice}\nKomputer memilih: {computer_choice}\n{result}\n\nSkor Anda: {player_score}\nSkor Komputer: {computer_score}"

# Widget untuk menampilkan hasil dan skor
output_label = widgets.Label(
    value="Klik tombol untuk memulai permainan",
)

# Tombol untuk memilih batu
btn_batu = widgets.Button(description='Batu', button_style='success')
btn_batu.on_click(lambda b: play_game("batu"))

# Tombol untuk memilih gunting
btn_gunting = widgets.Button(description='Gunting', button_style='warning')
btn_gunting.on_click(lambda b: play_game("gunting"))

# Tombol untuk memilih kertas
btn_kertas = widgets.Button(description='Kertas', button_style='danger')
btn_kertas.on_click(lambda b: play_game("kertas"))

# Tampilkan widget
widgets.VBox([btn_batu, btn_gunting, btn_kertas, output_label])
