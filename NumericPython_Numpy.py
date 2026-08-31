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

print(bmi)

# Jika tanpa numpy akan terjadi error
# Bmi = weight / height ** 2 # ini tanpa numpy dan pasti nya akan error
# print(Bmi)

#  CATATAN : Numpy Arrayy hanya bisa mengisi satu tipe data saja dalam Array 
tesDataType = np.array([2.0, "Rio", True]) # disini ada 3 tipe data
print(tesDataType) # Tapi saat di cetak, semua tipe data itu berubah jadi string semua

# Perlu diketahui Numpy Array hanyalah jenis tipe Python baru (seperti tipe float, string , dan Array sebelumnya) artinya ia memiliki Method sendiri yang bisa berperilaku berbeda
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

merge_python_list = python_list + python_list # Element Array akan di tempelkan menjadi satu (index bertambah)
print(merge_python_list) # hasil = [1, 2, 3, 1, 2, 3]

merge_numpy_array = numpy_array + numpy_array # Jika pakai Numpy Array kita tidak menggabungkan Array (menambahkan index), tapi kita menjumlahkan isi data tersebut
print(merge_numpy_array) # hasil = [2, 4, 6]
# Jadi hati-hati ketika ingin menambahkan Array di Numpy Array, apalagi jika ternyata Array yang di tambahkan berbeda tipe data