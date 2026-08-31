# Numpy (Numeric Python) adalah paackage yang diantara lain menyediakan alternatif untuk Array Python biasa
# Dengan Numpy kamu bisa menghitung semua array dengan array lain yang membuat lebih mudah dan cepat

import numpy as np

name = ["Arkan", "Berus", "Chaerul", "Denis", "Ehsan"]
height = [186.2, 182.9, 169.7, 166.3, 167.1]
weight = [67.4, 64.3, 58.9, 68.2, 66.2]

np_height = np.array(height)
np_weight = np.array(weight)

# bmi = body mass index, mungkin berat badan ideal
bmi = np_weight / np_height ** 2

print(bmi) # [0.00194402 0.00192213 0.00204527 0.00246604 0.00237086]

# Subsetting(Pemanggilan/Pengambilan) Data Array

print(bmi[1]) # Mengambil salah satu data yang sudah di jumlahkan tadi menjadi bmi dan diambil salah satu data nya
# hasil = 0.001922133562275483

print(bmi > 0.0020)  # Memfilter data dengan operator perbandingan yang hasilnya akan True(jika data seusai syarat) dan False(jika data tidak sesuai syarat)
# hasil = [False False True True True]

print(bmi[bmi > 0.0020]) # untuk melakukan cetak data  yang index nya sesuai dengan syarat
# hasil = [0.00204527 0.00246604 0.00237086]

print(bmi[1:5]) # Mencetak berdasarkan urutan index di dalam Array nya

