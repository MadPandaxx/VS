import sys

from Tugas_Besar import celsius_ke_fahrenheit, celsius_ke_kelvin

while True:
    x = float(input("Masukan nilai tegangan (0-5 volt): "))

    if x < 0 or x > 5:
        print("Nilai tegangan harus berada dalam range 0-5!")
        continue

    y = 10 * x + 3
    print(f"Nilai suhu dalam Celcius: {y} C")

    satuan = input("Pilih satuan suhu yang diinginkan (F/K/R): ")

    if satuan == "F":
        print(celsius_ke_fahrenheit())
    elif satuan == "K":
        print(celsius_ke_kelvin())

    ulangi = input("Apakah ingin mengulangi? (y/t): ")
    if ulangi.lower() == "t":
        break