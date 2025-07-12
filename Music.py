import csv
import os

FILENAME = 'musik.csv'

def tambah_lagu():
    print("\n== Tambah Lagu Baru ==")
    id_lagu = input("ID: ")
    judul = input("Judul Lagu: ")
    artis = input("Artis: ")
    album = input("Album: ")
    durasi = input("Durasi (mm:ss): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_lagu, judul, artis, album, durasi])
        print("✅ Lagu berhasil ditambahkan!\n")

def tampilkan_semua():
    print("\n== Daftar Lagu ==")
    if not os.path.exists(FILENAME):
        print("❌ Belum ada lagu yang ditambahkan.")
        return

    with open(FILENAME, newline='') as file:
        reader = csv.reader(file)
        print(f"{'ID':<5} {'Judul':<20} {'Artis':<20} {'Album':<20} {'Durasi'}")
        print("-" * 70)
        for row in reader:
            if row:  # skip empty rows
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]}")

def cari_lagu():
    print("\n== Cari Lagu ==")
    kata_kunci = input("Masukkan judul/artis: ").lower()
    ditemukan = False

    with open(FILENAME, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if kata_kunci in row[1].lower() or kata_kunci in row[2].lower():
                print(f"\n🎵 Ditemukan: {row}")
                ditemukan = True

    if not ditemukan:
        print("❌ Lagu tidak ditemukan.")

def putar_lagu():
    print("\n== Simulasi Putar Lagu ==")
    id_cari = input("Masukkan ID lagu: ")

    with open(FILENAME, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == id_cari:
                print(f"\n▶️ Memutar: {row[1]} - {row[2]} ({row[4]})")
                return
    print("❌ Lagu tidak ditemukan.")

def menu():
    while True:
        print("\n=== APLIKASI MUSIK CSV ===")
        print("1. Tambah Lagu")
        print("2. Tampilkan Semua Lagu")
        print("3. Cari Lagu")
        print("4. Putar Lagu")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            tambah_lagu()
        elif pilihan == '2':
            tampilkan_semua()
        elif pilihan == '3':
            cari_lagu()
        elif pilihan == '4':
            putar_lagu()
        elif pilihan == '5':
            print("👋 Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("❌ Pilihan tidak valid!")

# Inisialisasi file jika belum ada
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Judul', 'Artis', 'Album', 'Durasi'])

# Jalankan menu utama
menu()
