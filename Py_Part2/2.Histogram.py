# HISTOGRAM : Jenis visualisasi yang sangat berguna untuk mengeksplorasi data, ini membantu untuk memahami sebaran variabel

import matplotlib.pyplot as plt
import numpy as np

# help(plt.hist) # Kiita bisa pakai fungsi hist() untuk membuat Histogram
# Dalam hist ada 2 argumen dari pertama yang penting
# hist(x, bins=None) 
# x = berisi daftar nilai yang ingin dibuat histogram
# bins = untuk memberi tahu Python menjadi berapa bin (kolom jangka) data harus di bagi, jika kita tidak menggunakan bin (nilai nya akan menjadi 10 secara default)

values = [0, 0, 6 ,1 ,4 ,1 ,6 ,2.2 ,2.5 ,2.6 ,3.2 ,3.5 ,3.9 ,4.2, 6] # Data Acak
hasil_bins3 = plt.hist(values, bins=3)
plt.show()
plt.clf()
print(hasil_bins3)

hasil_bins5 = plt.hist(values, bins=3)
plt.show()
plt.clf()
print(hasil_bins3)


# CONTOH HISTOGRAM RAPIH TENTANG DISTRIBUSI UMUR KARYAWAN PERUSAHAAN

# 1. MASUKKAN DATA DARI ATASAN DI SINI
# Ganti angka di bawah ini dengan data asli yang kamu miliki
data_manual = [
    22, 25, 25, 26, 28, 28, 29, 30, 30, 31, 
    32, 32, 33, 34, 35, 35, 35, 36, 37, 38, 
    39, 40, 41, 42, 42, 43, 45, 46, 48, 52,
    24, 27, 29, 31, 33, 34, 35, 36, 38, 40,
    30, 32, 35, 37, 39, 41, 43, 45, 47, 50
]

# 2. Mengatur Ukuran Kanvas Grafik
plt.figure(figsize=(9, 5))

# 3. Mengatur Interval Batang (Bins) Secara Manual agar Jelas
# range(20, 60, 5) artinya batang akan dikelompokkan tiap kelipatan 5: [20-25], [25-30], dst.
bins_range = range(20, 60, 5)

# 4. Membuat Histogram
plt.hist(
    data_manual, 
    bins=bins_range,     # Menggunakan range yang sudah kita buat
    color='#10b981',     # Warna hijau emerald modern
    edgecolor='#064e3b', # Warna garis tepi hijau tua
    alpha=0.85, 
    rwidth=0.85          # Memberikan celah antar batang
)

# 5. Desain Tambahan agar Rapi & Profesional
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title('Distribusi Umur Karyawan Perusahaan', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Kategori Umur (Tahun)', fontsize=11, labelpad=10)
plt.ylabel('Jumlah Karyawan (Orang)', fontsize=11, labelpad=10)

# Menyelaraskan angka di sumbu X dengan batas kelompok data (bins)
plt.xticks(bins_range)

# Menghapus garis tepi atas dan kanan
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 6. Menampilkan Grafik
plt.tight_layout()
plt.show()
plt.show()
plt.clf()