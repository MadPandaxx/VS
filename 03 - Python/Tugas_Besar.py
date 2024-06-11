# impor modul sys untuk mengakses input dari keyboard
import sys

# menampilkan nama pengguna
def show_menu(name, nim):
    print(f"Halo {name}!")
    print(f"Nim = {nim}")

name = input("Masukan namamu : ")
nim = input("Masukan nim kamu : ")

show_menu(name, nim)

# mendefinisikan konstanta suhu referensi
suhu_referensi = 25 # dalam derajat Celsius

# fungsi untuk mengonversi suhu dari Celsius ke Fahrenheit
def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# fungsi untuk mengonversi suhu dari Celsius ke Kelvin
def celsius_ke_kelvin(celsius):
    return celsius + 273.15

# fungsi untuk mengonversi suhu dari Celsius ke Reamur
def celsius_ke_reamur(celsius):
    return celsius * 4/5

#meminta input dari user berupa nilai tegangan (x)
while True:
    try:
        tegangan_input = float(input("Masukkan nilai tegangan (dalam volt): "))
        if tegangan_input < 0 or tegangan_input > 5:
            raise ValueError
        break
    except ValueError:
        print("Input tidak valid. Masukkan nilai tegangan antara 0 dan 5 volt.")

#menghitung suhu berdasarkan nilai tegangan input
suhu = (tegangan_input * 10) + 3

#menampilkan hasil suhu dalam derajat Celsius ke layar
print("Suhu udara saat ini adalah: {:.2f} derajat Celsius".format(suhu))

#meminta pilihan satuan suhu dari pengguna
print("Pilih satuan suhu untuk ditampilkan:")
print("1. Fahrenheit")
print("2. Kelvin")
print("3. Reamur")
while True:
    try:
        pilihan = int(input("Masukkan pilihan (1/2/3): "))
        if pilihan not in (1, 2, 3):
            raise ValueError
        break
    except ValueError:
        print("Input tidak valid. Masukkan pilihan (1/2/3).")

#satuan yang dapat dipilih pengguna
if pilihan == 1:
    suhu_fahrenheit = celsius_ke_fahrenheit(suhu)
    print("Suhu udara saat ini adalah: {:.2f} derajat Fahrenheit".format(suhu_fahrenheit))
elif pilihan == 2:
    suhu_kelvin = celsius_ke_kelvin(suhu)
    print("Suhu udara saat ini adalah: {:.2f} Kelvin".format(suhu_kelvin))
elif pilihan == 3:
    suhu_reamur = celsius_ke_reamur(suhu)
    print("Suhu udara saat ini adalah: {:.2f} derajat Reamur".format(suhu_reamur))
