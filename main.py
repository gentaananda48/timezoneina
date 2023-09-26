import tkinter as tk
from tkinter import ttk
from time_utils import calculate_times

# Fungsi untuk membuat antarmuka pengguna


def create_ui(root):
    def submit():
        # Mengambil jam, menit, dan zona waktu yang dipilih oleh pengguna
        hours = hour_var.get()
        minutes = minute_var.get()
        timezone = timezone_var.get()

        # Menghitung waktu di zona waktu yang dipilih
        result = calculate_times(hours, minutes, timezone)

        # Menampilkan hasil waktu di label-label sejajar dengan input
        wib_label.config(text=f"WIB: {result['WIB']}")
        wita_label.config(text=f"WITA: {result['WITA']}")
        wit_label.config(text=f"WIT: {result['WIT']}")

    root.geometry("350x350")  # Menetapkan ukuran jendela
    root.resizable(False, False)  # Mencegah jendela dapat diubah ukurannya

    frame = ttk.Frame(root)  # Membuat frame dalam jendela utama
    frame.pack(padx=20, pady=20)  # Menempatkan frame dengan jarak padding

    # Dropdown untuk memilih jam
    hours = [str(i).zfill(2) for i in range(24)]
    hour_var = tk.StringVar()
    ttk.Label(frame, text="Jam:").pack()
    hour_dropdown = ttk.Combobox(frame, textvariable=hour_var, values=hours)
    hour_dropdown.pack()
    hour_dropdown.set(hours[0])  # Nilai default

    # Dropdown untuk memilih menit
    minutes = [str(i).zfill(2) for i in range(60)]
    minute_var = tk.StringVar()
    ttk.Label(frame, text="Menit:").pack()
    minute_dropdown = ttk.Combobox(
        frame, textvariable=minute_var, values=minutes)
    minute_dropdown.pack()
    minute_dropdown.set(minutes[0])  # Nilai default

    # Label instruksi zona waktu
    ttk.Label(frame, text="Zona waktu:").pack()

    # Dropdown untuk memilih zona waktu
    timezones = ["WIB", "WITA", "WIT"]
    timezone_var = tk.StringVar()
    timezone_dropdown = ttk.Combobox(
        frame, textvariable=timezone_var, values=timezones)
    timezone_dropdown.pack()
    timezone_dropdown.set(timezones[0])  # Nilai default

    # Tombol "Submit" untuk menghitung waktu
    ttk.Button(frame, text="Submit", command=submit).pack(pady=10)

    # Label-label untuk menampilkan hasil waktu sejajar dengan input
    wib_label = ttk.Label(frame, text="", anchor="w")
    wib_label.pack(fill="x")
    wita_label = ttk.Label(frame, text="", anchor="w")
    wita_label.pack(fill="x")
    wit_label = ttk.Label(frame, text="", anchor="w")
    wit_label.pack(fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Zona Waktu Indonesia")
    create_ui(root)  # Membuat antarmuka pengguna
    root.mainloop()  # Menjalankan loop utama Tkinter
