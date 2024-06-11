import os

def f(x):
    return x**3 - (0.165 * x**2) - (3.993 * x * 10**-4)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bisection(a, b, e):
    if f(a) * f(b) > 0:
        print("Interval ini tidak valid.")
        return None
    
    while (b - a) < e:
        c = (a + b) / 2
        if f(c) == 0.0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def regula_falsi(a, b, e):
    if f(a) * f(b) > 0:
        print("Interval ini tidak valid.")
        return None

    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < e:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

def main():
    a = 0
    b = 0.11
    e = 0.0001

    # Memeriksa apakah selang yang diberikan cukup untuk minimal satu akar
    if f(a) * f(b) > 0:
        print("Interval ini tidak valid. Tidak ada akar dalam selang yang ditentukan.")
        return

    while True:
        print("\nf(x) = x^3 - 0.165x^2 - 3.993x * 10^-4")
        print("\nPilih Metode:")
        print("1. Bagi Dua")
        print("2. Regula Falsi")
        print("3. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            clear_screen()
            print("\nMetode Bagi Dua:")
            result_bisection = bisection(a, b, e)
            if result_bisection is not None:
                print("Akar dengan metode bagi dua:", result_bisection)
                print("-----------------------")
            else:
                print("Tidak dapat menemukan akar dengan metode bagi dua.")
                print("-----------------------")
        elif choice == '2':
            clear_screen()
            print("\nMetode Regula Falsi:")
            result_regula_falsi = regula_falsi(a, b, e)
            if result_regula_falsi is not None:
                print("Akar dengan metode regula falsi:", result_regula_falsi)
                print("-----------------------")
            else:
                print("Tidak dapat menemukan akar dengan metode regula falsi.")
                print("-----------------------")
        elif choice == '3':
            clear_screen()
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")

if __name__ == "__main__":
    main()
