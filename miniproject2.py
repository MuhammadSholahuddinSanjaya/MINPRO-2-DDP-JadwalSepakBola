import os
import time
import pwinput
from prettytable import PrettyTable

data_users = {
    "admin": {"password": "220708", "role": "admin"},
    "fans" : {"password": "12345678", "role": "user"}
}

jadwal_pertandingan = {
    "J-01": {"pertandingan": "Timnas vs Jepang", "liga": "Kualifikasi PD", "waktu": "15/11/2026 19:00"},
    "J-02": {"pertandingan": "Man Utd vs Arsenal", "liga": "Premier League", "waktu": "16/11/2026 15:00"}
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_data():
    print("DAFTAR JADWAL PERTANDINGAN")
    if not jadwal_pertandingan:
        print("Belum ada data jadwal pertandingan yang tersimpan.")
        return

    table = PrettyTable()
    table.field_names = ["ID Jadwal", "Nama Pertandingan", "Nama Liga", "Waktu (dd/mm/yyyy hh:mm)"]

    for id_jadwal, detail in jadwal_pertandingan.items():
        table.add_row([id_jadwal, detail["pertandingan"], detail["liga"], detail["waktu"]])

    print(table)

def tambah_data():
    print("TAMBAH JADWAL BARU")
    id_baru = input("Masukkan ID Jadwal (misal: J-03) : ")

    if not id_baru:
        print("ID Jadwal tidak boleh kosong!")
        time.sleep(1.5)
        return

    if id_baru in jadwal_pertandingan:
        print("ID Jadwal sudah terdaftar! Gunakan ID lain.")
        time.sleep(1.5)
        return

    pertandingan = input("Nama Pertandingan : ")
    liga = input("Nama Liga         : ")
    waktu = input("Waktu Pertandingan (dd/mm/yyyy hh:mm) : ")

    jadwal_pertandingan[id_baru] = {
        "pertandingan": pertandingan,
        "liga": liga,
        "waktu": waktu
    }

    print("Jadwal pertandingan berhasil ditambahkan dengan ID:", id_baru)
    time.sleep(1.5)

def ubah_data():
    print("UBAH JADWAL PERTANDINGAN")
    tampilkan_data()
    if not jadwal_pertandingan:
        time.sleep(1.5)
        return

    id_cari = input("Masukkan ID Jadwal yang ingin diubah : ")

    if id_cari in jadwal_pertandingan:
        print("Data jadwal pertandingan dengan ID", id_cari, "ditemukan.")

        pertandingan_baru = input("Masukkan Nama Pertandingan Baru : ")
        liga_baru = input("Masukkan Nama Liga Baru         : ")
        waktu_baru = input("Masukkan Waktu Pertandingan Baru (dd/mm/yyyy hh:mm) : ")

        jadwal_pertandingan[id_cari] = {
            "pertandingan": pertandingan_baru,
            "liga": liga_baru,
            "waktu": waktu_baru
        }
        print("Data jadwal pertandingan berhasil diubah.")
    else:
        print("Jadwal pertandingan dengan ID", id_cari, "tidak ditemukan.")
    time.sleep(1.5)

def hapus_data():
    print("HAPUS JADWAL PERTANDINGAN")
    tampilkan_data()
    if not jadwal_pertandingan:
        time.sleep(1.5)
        return

    id_cari = input("Masukkan ID Jadwal yang ingin dihapus : ")

    if id_cari in jadwal_pertandingan:
        konfirmasi = input("Apakah Anda yakin ingin menghapus jadwal pertandingan dengan ID " + id_cari + "? (y/n): ")
        if konfirmasi.lower() == 'y':
            del jadwal_pertandingan[id_cari]
            print("Data jadwal pertandingan berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Jadwal pertandingan dengan ID", id_cari, "tidak ditemukan.")
    time.sleep(1.5)

def login():
    while True:
        clear_screen()
        print("LOGIN")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

        if username in data_users and data_users[username]["password"] == password:
            print("Login berhasil! Selamat datang,", username)
            time.sleep(1.5)
            return data_users[username]["role"]
        else:
            print("Username atau password salah. Silakan coba lagi.")
            time.sleep(1.5)

def main_menu(role):
    while True:
        clear_screen()
        print("MENU UTAMA")
        print("1. Tampilkan Jadwal Pertandingan")
        if role == "admin":
            print("2. Tambah Jadwal Pertandingan")
            print("3. Ubah Jadwal Pertandingan")
            print("4. Hapus Jadwal Pertandingan")
        print("0. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka sesuai menu.")
            time.sleep(1.5)
            continue

        if pilihan == 1:
            tampilkan_data()
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == 2 and role == "admin":
            tambah_data()
        elif pilihan == 3 and role == "admin":
            ubah_data()
        elif pilihan == 4 and role == "admin":
            hapus_data()
        elif pilihan == 0:
            print("Terima kasih telah menggunakan Menu ini.")
            time.sleep(1.5)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            time.sleep(1.5)

while True:
    role_aktif = login()
    main_menu(role_aktif)