def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

# Meminta input dari pengguna
angka = int(input("Masukkan angka untuk dihitung faktorial: "))

# Memanggil fungsi faktorial dan mencetak hasilnya
hasil = faktorial(angka)
print(hasil)

print("Faktorial dari", angka, "adalah", hasil)