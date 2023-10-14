print("\n")
print("=" * 25)
print("  DAFTAR NILAI MAHASISWA")
print("=" * 25, "\n")

# Variabel Yang Ingin Dimasukkan
nama_mahasiswa = str(input("Masukkan Nama Mahasiswa : "))
mata_kuliah = str(input("Masukkan Matkul \t: "))
nilai_tugas = float(input("Masukkan Nilai Tugas \t: "))
nilai_uts = float(input("Masukkan Nilai UTS \t: "))
nilai_uas = float(input("Masukkan Nilai UAS \t: "))

# Matematika Mencari Rata-rata
hasil = float((nilai_tugas + nilai_uts + nilai_uas)//3)

# Variabel output
print("\n")
print("="*30)
print(f"Nama Mahasiswa \t: {nama_mahasiswa}")
print(f"Mata Kuliah \t: {mata_kuliah}")
print(f"Jumlah Nilai \t: {hasil}")
print("="*30)
print("\n")

# Method Untuk Menetukan Grade
print("="*30)
if 85 <= hasil <= 100:
    print("Selamat Anda Mendapatkan Nilai Grade A")
elif 80 <= hasil <= 85:
    print("Selamat Anda Mendapatkan Nilai Grade A-")
elif 75 <= hasil <= 80:
    print("Selamat Anda Mendapatkan Nilai Grade B+")
elif 70 <= hasil <= 75:
    print("Selamat Anda Mendapatkan Nilai Grade B")
elif 65 <= hasil <= 70:
    print("Selamat Anda Mendapatkan Nilai Grade B-")
elif 60 <= hasil <= 65:
    print("Selamat Anda Mendapatkan Nilai Grade C+")
elif 55 <= hasil <= 60:
    print("Selamat Anda Mendapatkan Nilai Grade C")
elif 50 <= hasil <= 55:
    print("Selamat Anda Mendapatkan Nilai Grade D")
else:
    print("Goblok Kok Bisa E !!!")
print("="*30)
