# Contoh Package: Direktori yang berisi script python, setiap script disebut modul

# pkg/
#   mod1.py
#   mod2.py
#   ...

# Modul-modul tersebut berikian beberapa fungsi, metode, dan tipe python baru untuk memecahkan masalah tertentu
# Ada 1000+ package Python yang tersedia di internet dan siap diinstall
# Diantaranya adalah:
# Package untuk Data Science :
# - Numpy (untuk bekerja efisien dengan Array)
# - Matplotlib (untuk visualisasi data)
# - Scikit-Learn (untuk Machine Learning)
# Tidak semua paket(packages) ini tersedia di Python secara default

# Untuk memakai Packages Python, kamu harus install terlebih dahulu di sistem operasi, lalu menambahkan kode di script Python untuk membuat alias(panggilan) untuk script itu ketika ingin di panggil/digunakan pada kode/tugas tertentu di codingan

from math import pi
import math
from numpy import array  # kita ambil fungsi array dari package numpy
# Memberikan alias np agar ketika kita ingin gunakan packages numpy cukup panggil alias nya np
import numpy as np
np.array([1, 2, 3])  # np = Numpy

# Contoh penggunaan pada biasanya
KartuKeluarga = ["Seon", "Lena", "Grace", "Yuno", "Gibran"]

KartuKeluarga_Baru = KartuKeluarga + ["Lylia", "Kyle"]

print(str(len(KartuKeluarga_Baru)))

# Sebenarnya dengan np bisa lebih mudah di pahami code nya ketimbang hanya pakai fungsi spesifik misal form numpy import array coba saja bandingkan dengan contoh dibawah, karena di code ini kita tahu pakai np panggil fungsi .array()
np_KartuKeluarga = np.array(KartuKeluarga_Baru)
print(np_KartuKeluarga)

# kita bisa mengambil fungsi tertentu dari package
# dengan begini cukup ketik array saja dan itu tidak akan terjadi error
array([6, 7, 8])

Murid_7A = ["Andy", "Bahlil", "Cleo", "Drian", "Ethan"]

Murid_7a_New = Murid_7A + ["Frida", "Gisel"]

print(str(len(Murid_7a_New)))

# Untuk pemula yang masih belum memahami packages mereka akan bingung kenapa tidak terjadi error ketika ia hanya mengetik array() disitu padahal kalau di coba error karena di tidak tahu -pemanggilan fungsi di packages Python
array_Murid_7A = array(Murid_7a_New)
print(array_Murid_7A)

# Contoh lain package Python
# Import the math package

# Kalkulasi C
C = 2 * 0.43 * math.pi

# Kalkulasi A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Import pi function dari package math

# Kalkulasi C
C = 2 * 0.43 * pi

# Kalkulasi A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Berbagai cara impor
# Ada beberapa cara untuk mengimpor paket dan modul ke dalam Python. Tergantung pada cara mengimpornya, Anda harus menggunakan kode Python yang berbeda.

# Misalkan Anda ingin menggunakan fungsi 'inv()' , yang berada di dalam 'linalg' sub package dari 'scipy' package . Anda ingin dapat menggunakan fungsi ini sebagai berikut:

# from scipy.linalg import inv as my_inv
# my_inv([[1,2], [3,4]])