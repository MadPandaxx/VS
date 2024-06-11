import sys

while True:
    x = float(input("Masukkan nilai tegangan (0-5 volt): "))

    if x < 0 or x > 5:
        print("Nilai tegangan harus berada dalam range 0-5 volt!")
        continue
        
    y = 10 * x + 3
    print(f"Nilai suhu dalam derajat Celsius: {y} C")
    
    satuan = input("Pilih satuan suhu (F/K/R): ")
    
    if satuan == "F":
        y = (9/5) * y + 32
        print(f"Nilai suhu dalam derajat Fahrenheit: {y} F")
    elif satuan == "K":
        y += 273.15
        print(f"Nilai suhu dalam derajat Kelvin: {y} K")
    elif satuan == "R":
        y = (4/5) * y
        print(f"Nilai suhu dalam derajat Reamur: {y} R")
    else:
        print("Pilihan satuan suhu tidak valid!")
    
    ulangi = input("Apakah ingin mengulangi? (y/t): ")
    if ulangi.lower() == "t":
        break
