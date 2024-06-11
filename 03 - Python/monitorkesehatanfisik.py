import json
import os
import sys

class ActivityMonitor:
    def __init__(self):
        self.datafile = "data.json"

    def clear_screen(self):
        if sys.platform.startswith('win'):
            os.system('cls')
        else:
            os.system('clear')

    def read_data(self):
        try:
            with open(self.datafile, "r") as file:
                existing_data = json.load(file)
                return existing_data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def save_data(self, data):
        with open(self.datafile, "w") as file:
            json.dump(data, file, indent=4)

    def calculate_bmr(self, gender, age, weight_kg, height_cm):
        if gender == 'PRIA':
            return (13.387 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
        elif gender == 'WANITA':
            return (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
        else:
            return None

    def calculate_mets(self, activity):
        if activity == 'Jalan':
            return 4.0
        elif activity == 'Lari':
            return 7.0
        else:
            return None

    def determine_category(self, value, categories):
        for category, thresholds in categories.items():
            if thresholds[0] < value <= thresholds[1]:
                return category
        return "Unknown"

    def calculate_calories_burned(self, mets, bmr, duration_hours):
        return mets * bmr * duration_hours

    def calculate_all(self):
        age = int(input('Masukkan usia (tahun): '))
        height_cm = float(input('Masukkan tinggi badan (cm): '))
        weight_kg = float(input('Masukkan berat badan (kg): '))

        self.clear_screen()
        print('---------------------')
        print('Pilih Gender Anda:')
        print('---------------------')
        print('1. PRIA')
        print('2. WANITA')
        print('---------------------')

        gender_choice = int(input())
        if gender_choice == 1:
            gender = 'PRIA'
        elif gender_choice == 2:
            gender = 'WANITA'
        else:
            print("Jenis kelamin tidak valid. Harap masukkan 'pria' atau 'wanita'.")
            return

        bmr = self.calculate_bmr(gender, age, weight_kg, height_cm)
        if bmr is None:
            print("BMR tidak dapat dihitung. Harap periksa kembali masukan Anda.")
            return

        self.clear_screen()
        print('---------------------')
        print('Aktivitas apa yang anda lakukan:')
        print('---------------------')
        print('1. Jalan')
        print('2. Lari')
        print('---------------------')

        activity_choice = int(input())
        if activity_choice == 1:
            activity = 'Jalan'
        elif activity_choice == 2:
            activity = 'Lari'
        else:
            print("Aktivitas tidak valid. Harap pilih 'Jalan' atau 'Lari'.")
            return

        mets = self.calculate_mets(activity)
        if mets is None:
            print("METs tidak dapat dihitung. Harap periksa kembali masukan Anda.")
            return

        self.clear_screen()
        langkah = int(input('Masukkan jumlah langkah: '))
        bpm = int(input('Masukkan heart rate (BPM): '))
        duration_minutes = int(input('Masukkan durasi aktivitas (menit): '))
        duration_hours = duration_minutes / 60.0

        kkal = self.calculate_calories_burned(mets, bmr, duration_hours)
        kkal = round(kkal, 2)

        return dict(langkah=langkah, bpm=bpm, kkal=kkal, activity=activity, gender=gender, age=age)

    def display_monitoring_results(self, data):
        print("==========================================================")
        print("Monitoring Results (", data['activity'], "):")
        print("Jumlah Langkah:", data['langkah'], "(", self.determine_category(data['langkah'], {
            "Sedikit": (0, 5000),
            "Cukup": (5000, 10000),
            "Banyak": (10000, float('inf'))
        }), ")", "Yah langkah mu sangat sedikit, AYOO TINGKATKAN LAGI" if data['langkah']<5000 else "AYOO PERTAHANKAN!!")
        print("Detak Jantung (BPM):", data['bpm'], "BPM (", self.determine_category(data['bpm'], {
            "Rendah": (0, 60),
            "Normal": (60, 100),
            "Tinggi": (100, float('inf'))
        }), ")", "Jangan paksaan dirimu, ISTIRAHAT JUGA PENTING" if data['bpm']>500 else "SEMANGATT!!")
        print("Kalori Terbakar (kkal):", data['kkal'], "KKAL (", self.determine_category(data['kkal'], {
            "Sedikit": (0, 500),
            "Cukup": (500, 1000),
            "Banyak": (1000, float('inf'))
        }), ")", "Kalori yang terbakar sangat sedikit, AYOO TINGKATKAN LAGII!!" if data['kkal']<500 else "AYOO PERTAHANKAN!!")

    def print_all_data(self):
        print("==============================================")
        print("------------------ALL DATA--------------------")
        print("==============================================")
        existing_data = self.read_data()
        for entry in existing_data:
            self.display_monitoring_results(entry)

    def print_specific_data(self, gender=None, age=None, activity=None):
        print("==============================================")
        print("--------------SORTIR", gender or age or activity ,"--------------------")
        print("==============================================")
        existing_data = self.read_data()
        for entry in existing_data:
            if (gender is None or entry['gender'] == gender) and (age is None or entry['age'] == age) and (activity is None or entry['activity'] == activity):
                self.display_monitoring_results(entry)

    def add_data(self, data):
        existing_data = self.read_data()
        existing_data.append(data)
        self.save_data(existing_data)

    def main_screen(self):
        print("==============================================")
        print("--------------MONITORING SCREEN---------------")
        print("==============================================")
        print("1. Lihat Data Aktivitas")
        print("2. Buat Data Aktivitas Baru")
        print("==============================================")

        choose = int(input())
        if choose == 1:
            self.print_choice()
        elif choose == 2:
            self.clear_screen()
            data = self.calculate_all()
            self.add_data(data)
            self.display_monitoring_results(data)
        else:
            return

    def print_choice(self):
        self.clear_screen()
        print("==============================================")
        print("--------------MONITORING SCREEN---------------")
        print("==============================================")
        print("1. Lihat Seluruh Data")
        print("2. Lihat Data Tersortir")
        print("==============================================")

        choose = int(input())
        if choose == 1:
            self.clear_screen()
            self.print_all_data()
        elif choose == 2:
            self.print_tersortir()
        else:
            return

    def print_tersortir(self):
        self.clear_screen()
        print("==============================================")
        print("---------------PILIHAN SORTIR-----------------")
        print("==============================================")
        print("1. Gender")
        print("2. Usia")
        print("3. Aktivitas")
        print("==============================================")
        choose = int(input())
        if choose == 1:
            self.clear_screen()
            print("==============================================")
            print("---------------PILIHAN GENDER-----------------")
            print("==============================================")
            print("1. PRIA")
            print("2. WANITA")
            print("==============================================")
            gender = int(input())
            if gender == 1:
                self.clear_screen()
                self.print_specific_data(gender='PRIA')
            elif gender == 2:
                self.clear_screen()
                self.print_specific_data(gender='WANITA')
            else:
                return
        elif choose == 2:
            self.clear_screen()
            age = int(input("Masukkan umur yang ingin anda cari: "))
            self.print_specific_data(age=age)
        elif choose == 3:
            self.clear_screen()
            print("==============================================")
            print("-------------PILIHAN AKTIVITAS----------------")
            print("==============================================")
            print("1. Jalan")
            print("2. Lari")
            print("==============================================")
            activity = int(input())
            if activity == 1:
                self.clear_screen()
                self.print_specific_data(activity='Jalan')
            elif activity == 2:
                self.clear_screen()
                self.print_specific_data(activity='Lari')
            else:
                return
        else:
            return

    def main_loop(self):
        while True:
            self.main_screen()
            print("======================================================")
            choice = input("Apakah Anda ingin kembali ke menu awal? (y/n): ")
            self.clear_screen()
            if choice.lower() != "y":
                break

monitor = ActivityMonitor()
monitor.main_loop()
