import random
import tkinter as tk

class HeartRateMonitor:
    def __init__(self):
        self.heart_rate = 0
        self.hrv = 0
        self.recovery_time = 0
        self.status = ""
        self.alarm = "OFF"
        self.threshold_low = 60
        self.threshold_high = 100
        self.hrv_threshold = 50
        self.recovery_threshold = 120

    def measure_heart_rate(self):
        self.heart_rate = random.randint(50, 120)

    def measure_hrv(self):
        self.hrv = random.randint(20, 200)

    def measure_recovery_time(self):
        self.recovery_time = random.randint(50, 150)

    def check_status(self):
        if self.heart_rate < self.threshold_low or self.heart_rate > self.threshold_high:
            self.status = "Abnormal"
            self.alarm = "ON"
        elif self.hrv < self.hrv_threshold:
            self.status = "Low HRV"
            self.alarm = "ON"
        elif self.recovery_time > self.recovery_threshold:
            self.status = "Delayed Recovery"
            self.alarm = "ON"
        else:
            self.status = "Normal"
            self.alarm = "OFF"

    def set_thresholds(self, low, high, hrv, recovery):
        self.threshold_low = low
        self.threshold_high = high
        self.hrv_threshold = hrv
        self.recovery_threshold = recovery

    def display_data(self):
        print("===== Monitor Denyut Jantung =====")
        print(f"Denyut Jantung: {self.heart_rate} bpm")
        print(f"Tingkat Variabilitas Denyut Jantung (HRV): {self.hrv}")
        print(f"Waktu Pemulihan Denyut Jantung: {self.recovery_time} detik")
        print(f"Status: {self.status}")
        print(f"Alarm: {self.alarm}")
        print("==================================")

def start_monitoring():
    print("Memulai pemantauan denyut jantung...")
    monitor = HeartRateMonitor()

    # Membuat GUI menggunakan Tkinter
    monitor_window = tk.Tk()
    monitor_window.title("Heart Rate Monitor")

    heart_rate_label = tk.Label(monitor_window, text="Denyut Jantung: ")
    heart_rate_label.pack()
    hrv_label = tk.Label(monitor_window, text="HRV: ")
    hrv_label.pack()
    recovery_label = tk.Label(monitor_window, text="Waktu Pemulihan: ")
    recovery_label.pack()
    status_label = tk.Label(monitor_window, text="Status: ")
    status_label.pack()
    alarm_label = tk.Label(monitor_window, text="Alarm: ")
    alarm_label.pack()

    def update_data():
        monitor.measure_heart_rate()
        monitor.measure_hrv()
        monitor.measure_recovery_time()
        monitor.check_status()

        # Update data pada GUI
        heart_rate_label.config(text="Denyut Jantung: {} bpm".format(monitor.heart_rate))
        hrv_label.config(text="HRV: {}".format(monitor.hrv))
        recovery_label.config(text="Waktu Pemulihan: {} detik".format(monitor.recovery_time))
        status_label.config(text="Status: {}".format(monitor.status))
        alarm_label.config(text="Alarm: {}".format(monitor.alarm))

        monitor_window.after(1000, update_data)

    def set_thresholds():
        low = int(low_entry.get())
        high = int(high_entry.get())
        hrv = int(hrv_entry.get())
        recovery = int(recovery_entry.get())
        monitor.set_thresholds(low, high, hrv, recovery)

    low_threshold_label = tk.Label(monitor_window, text="Ambang Batas Rendah: ")
    low_threshold_label.pack()
    low_entry = tk.Entry(monitor_window)
    low_entry.pack()

    high_threshold_label = tk.Label(monitor_window, text="Ambang Batas Tinggi: ")
    high_threshold_label.pack()
    high_entry = tk.Entry(monitor_window)
    high_entry.pack()

    hrv_threshold_label = tk.Label(monitor_window, text="Ambang Batas HRV: ")
    hrv_threshold_label.pack()
    hrv_entry = tk.Entry(monitor_window)
    hrv_entry.pack()

    recovery_threshold_label = tk.Label(monitor_window, text="Ambang Batas Waktu Pemulihan: ")
    recovery_threshold_label.pack()
    recovery_entry = tk.Entry(monitor_window)
    recovery_entry.pack()

    set_thresholds_button = tk.Button(monitor_window, text="Set Ambang Batas", command=set_thresholds)
    set_thresholds_button.pack()

    update_data()
    monitor_window.mainloop()

# Memulai program
start_monitoring()
