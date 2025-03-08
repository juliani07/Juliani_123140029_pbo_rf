# Nama  : Juliani leony Putri Melati Manalu
# NIM   : 123140029
# Kelas : RF

import csv
import os

DATA_FILE = "mahasiswa.csv"

# Load data dari file CSV
def load_data():
    mahasiswa = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    nim, nama, nilai = row
                    mahasiswa[nim] = {"nama": nama, "nilai": int(nilai)}
    return mahasiswa

# Simpan data ke file CSV
def save_data(mahasiswa):
    with open(DATA_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        for nim, data in mahasiswa.items():
            writer.writerow([nim, data["nama"], data["nilai"]])

# Tambah mahasiswa
def tambah_mahasiswa(mahasiswa):
    try:
        nim = input("Masukkan NIM: ").strip()
        if nim in mahasiswa:
            print("NIM sudah ada!")
            return
        nama = input("Masukkan Nama: ").strip()
        nilai = int(input("Masukkan Nilai: ").strip())
        mahasiswa[nim] = {"nama": nama, "nilai": nilai}
        print("Mahasiswa berhasil ditambahkan!")
    except ValueError:
        print("Nilai harus berupa angka!")

# Tampilkan semua mahasiswa dengan sorting
def tampilkan_mahasiswa(mahasiswa):
    if not mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    
    pilihan_sort = input("Urutkan berdasarkan (1: NIM, 2: Nilai tertinggi): ").strip()
    if pilihan_sort == "1":
        sorted_mahasiswa = sorted(mahasiswa.items())
    elif pilihan_sort == "2":
        sorted_mahasiswa = sorted(mahasiswa.items(), key=lambda x: x[1]["nilai"], reverse=True)
    else:
        print("Pilihan tidak valid, menampilkan tanpa sorting.")
        sorted_mahasiswa = mahasiswa.items()
    
    print("\n==== DATA MAHASISWA ====")
    print("NIM      | Nama          | Nilai")
    print("---------------------------------")
    for nim, data in sorted_mahasiswa:
        print(f"{nim:<8} | {data['nama']:<12} | {data['nilai']:<5}")

# Cari mahasiswa berdasarkan NIM
def cari_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin dicari: ").strip()
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print("\nData Mahasiswa:")
        print(f"NIM   : {nim}")
        print(f"Nama  : {data['nama']}")
        print(f"Nilai : {data['nilai']}")
    else:
        print("Mahasiswa tidak ditemukan!")

# Edit data mahasiswa
def edit_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin diedit: ").strip()
    if nim in mahasiswa:
        nama_baru = input("Nama baru (kosongkan jika tidak ingin mengubah): ").strip()
        nilai_baru = input("Nilai baru (kosongkan jika tidak ingin mengubah): ").strip()
        if nama_baru:
            mahasiswa[nim]["nama"] = nama_baru
        if nilai_baru:
            try:
                mahasiswa[nim]["nilai"] = int(nilai_baru)
            except ValueError:
                print("Nilai harus berupa angka!")
                return
        print("Data berhasil diperbarui!")
    else:
        print("Mahasiswa tidak ditemukan!")

# Hapus mahasiswa
def hapus_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin dihapus: ").strip()
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus!")
    else:
        print("Mahasiswa tidak ditemukan!")

# Menu utama
def main():
    mahasiswa = load_data()
    while True:
        print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa Berdasarkan NIM")
        print("4. Edit Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Simpan ke File")
        print("7. Keluar")
        pilihan = input("Pilihan: ").strip()
        if pilihan == "1":
            tambah_mahasiswa(mahasiswa)
        elif pilihan == "2":
            tampilkan_mahasiswa(mahasiswa)
        elif pilihan == "3":
            cari_mahasiswa(mahasiswa)
        elif pilihan == "4":
            edit_mahasiswa(mahasiswa)
        elif pilihan == "5":
            hapus_mahasiswa(mahasiswa)
        elif pilihan == "6":
            save_data(mahasiswa)
            print("Data mahasiswa telah disimpan dalam file 'mahasiswa.csv'")
        elif pilihan == "7":
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")

if __name__ == "__main__":
    main()
