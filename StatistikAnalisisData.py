# Disini kita akan menjumlahkan, mencari rata-rata, median, dan lain-lain untuk visualisasi bagaimana Data Analis itu

import numpy as np

#SURVEI SKALA KOTA

# Kita Buat Data Dummy untuk Latihan
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
# np.random.normal(...): Fungsi untuk menghasilkan angka acak berdasarkan distribusi normal (statistika):
#     1.75: Nilai rata-rata (mean) tinggi badan, yaitu 1,75 meter.
#     0.20: Simpangan baku atau sebaran data (standard deviation), yaitu 0,20 meter.
#     5000: Jumlah total data angka acak yang dibuat.
# np.round(..., 2): Fungsi untuk membulatkan setiap angka hasil acakan tadi menjadi dua angka di belakang koma.

weight = np.round(np.random.normal(60.32, 15, 5000), 2)

# Menempelkan kedua Variabel agar menjadi satu tabel dengan 2 kolom [[height, weight]]
np_city = np.column_stack((height, weight))
print(np_city)

# Mencari rata-rata Tinggi orang-orang di kota, Subsetting: [semua baris, kolom 1(height)]
mean_height = np.mean(np_city[:, 0])
print(mean_height)

# Mencari nilai tengah dari urutan terkecil hingga terbesar Tinggi orang-orang di kota, Subsetting: [semua baris, kolom 1(height)]
median_height = np.median(np_city[:, 0])
print(median_height)

# Memeriksa apakah Tinggi dan Berat (kolom1 & kolom2) nilai nya saling berkolerasi
cek_korelasi = np.corrcoef(np_city[:, 0], np_city[:, 1])
print(cek_korelasi)

# Mencari nilai Standar Devisi dari tinggi badan orang-orang di Kota, Standar Devisi ini melacak jarak persebaran data yang terkadang mean saja bisa meleset dalam perhitungannya
cek_standar_devisi = np.std(np_city[:, 0])
print(cek_standar_devisi)

# Kita Coba Memahami apa itu Standar Devisi
# 1. Membuat data array tinggi badan (dalam cm)
tim_basket = np.array([179, 180, 181])
kelas_acak = np.array([110, 170, 260])

# 2. Menghitung Rata-rata (Mean)
mean_basket = np.mean(tim_basket)
mean_acak = np.mean(kelas_acak)

# 3. Menghitung Standar Deviasi (STD)
std_basket = np.std(tim_basket)
std_acak = np.std(kelas_acak)

# 4. Menampilkan Hasil
print(f"--- TIM BASKET ---")
print(f"Rata-rata Tinggi : {mean_basket} cm")
print(f"Standar Deviasi   : {std_basket:.2f} cm") 

print(f"\n--- KELAS ACAK ---")
print(f"Rata-rata Tinggi : {mean_acak} cm")
print(f"Standar Deviasi   : {std_acak:.2f} cm")

# Tim Basket (STD = 0.82 cm): Angka ini sangat mendekati nol. Artinya, rata-rata 180 cm pada tim basket adalah representasi yang sangat akurat untuk seluruh anggota kelompok. Hampir tidak ada ketimpangan tinggi badan di tim ini.

# Kelas Acak (STD = 61.64 cm): Angka standar deviasinya sangat besar. Ini menjadi peringatan kritis bahwa nilai rata-rata 180 cm di kelompok ini menipu. Kenyataannya, tidak ada satu pun orang di dalam kelompok tersebut yang tingginya benar-benar mendekati 180 cm.

# Merapihkan urutan data Tinggi Badan dari angka terkecil hingga terbesar yang ada di Kota
urut_data_height = np.sort(np_city[:, 0])
print(urut_data_height)

# Menjumlahkan seluruh Tinggi Badan orang-orang Kota
total_jumlah_height = np.sum(np_city[:, 0])
print(total_jumlah_height)

# Sebenarnya di python biasa ada sum(), sort(), dan lainnya, tetapi jika menggunakan Numpy itu bedanya Numpy lebih cepat dalam pemrosesan Data, dikarenakan Numpy memproses Array yang hanya memiliki 1 Tipe Data