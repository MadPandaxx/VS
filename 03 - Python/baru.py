import random
import tkinter as tk

class HeartRateMonitor:
    def __init__(self):
        self.heart_rate = 0
        self.status = ""
        self.alarm = "OFF"
        self.threshold_low = 60
        self.threshold_high = 100

    def measure_heart_rate(self):
        self.heart_rate = random.randint(50, 120)

    def check_status(self):
        if self.heart_rate < self.threshold_low:
            self.status = "Rendah"
            self.alarm = "ON"
        elif self.heart_rate > self.threshold_high:
            self.status = "Tinggi"
            self.alarm = "ON"
        else:
            self.status = "Normal"
            self.alarm = "OFF"

    def set_threshold(self, low, high):
        self.threshold_low = low
        self.threshold_high = high

    def display_data(self):
        print("===== Monitor Denyut Jantung =====")
        print(f"Denyut Jantung: {self.heart_rate} bpm")
        print(f"Status: {self.status}")
        print(f"Alarm: {self.alarm}")
        print("==================================")

def start_monitoring():
    print("Memulai pemantauan denyut jantung...")
    monitor = HeartRateMonitor()
    monitor_window = tk.Tk()
    monitor_window.title("Heart Rate Monitor")

    heart_rate_label = tk.Label(monitor_window, text="Denyut Jantung: ")
    heart_rate_label.pack()
    status_label = tk.Label(monitor_window, text="Status: ")
    status_label.pack()
    alarm_label = tk.Label(monitor_window, text="Alarm: ")
    alarm_label.pack()

    def update_data():
        monitor.measure_heart_rate()
        monitor.check_status()
        heart_rate_label.config(text="Denyut Jantung: {} bpm".format(monitor.heart_rate))
        status_label.config(text="Status: {}".format(monitor.status))
        alarm_label.config(text="Alarm: {}".format(monitor.alarm))
        monitor_window.after(1000, update_data)

    def set_threshold():
        low = int(low_entry.get())
        high = int(high_entry.get())
        monitor.set_threshold(low, high)

    low_threshold_label = tk.Label(monitor_window, text="Threshold Rendah: ")
    low_threshold_label.pack()
    low_entry = tk.Entry(monitor_window)
    low_entry.pack()

    high_threshold_label = tk.Label(monitor_window, text="Threshold Tinggi: ")
    high_threshold_label.pack()
    high_entry = tk.Entry(monitor_window)
    high_entry.pack()

    set_threshold_button = tk.Button(monitor_window, text="Set Threshold", command=set_threshold)
    set_threshold_button.pack()

    update_data()
    monitor_window.mainloop()

# Memulai program
start_monitoring()
