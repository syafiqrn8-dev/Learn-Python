# Sebelumnya kita telah membuat array numpy, tapi yang kita buat adalah array 1 Dimensi

import numpy as np

np_height = np.array([186.2, 182.9, 169.7, 166.3, 167.1])
np_weight = np.array([67.4, 64.3, 58.9, 68.2, 66.2])

print(type(np_height))  # hasil = <class 'numpy.ndarray'>
print(type(np_weight))  # hasil = <class 'numpy.ndarray'>
# numpy.ndarray, artinya data tersebut adalah objek khusus dari NumPy yang menyimpan kumpulan elemen dengan tipe data yang sama (homogen) dalam satu atau banyak dimensi (seperti 1D, 2D, atau 3D).

# Array Numpy 2D

np_2D = np.array([[186.2, 182.9, 169.7, 166.3, 167.1],
                 [67.4, 64.3, 58.9, 68.2, 66.2]]) # Ada 2 Array di dalam Array :)  

# kita bisa liat informasi tentang kolom dan baris Array 2D yang kita buat dengan attribut khusus ArrayNumpy 2D '.shape' 
print(np_2D.shape) # hasil = (2, 5) maksudnya (baris, kolom)
print(np_2D[0]) # Memanggil baris pertama 
print(np_2D[0][2]) # Baris 1 Kolom 3 (ini untuk mengambil nilai spesifik pada tabel)
print(np_2D[0, 2]) # Baris 1 Kolom 3 (sama seperti (np_2D[0][2]) )
print(np_2D[:, 1:3]) # memanggil beberapa kolom dan baris, dibaca nya [seluruh baris, kolom 2 dan 3] cetak! dan liat hasilnya di run
print(np_2D[1, :]) # mencetak 1 baris dan semua kolom, dibaca nya [baris index 1(baris ke-2), semua kolom]


#    1      2      3       4      5   = Kolom
#([[186.2, 182.9, 169.7, 166.3, 167.1], 1 = Baris 1 (index 0)
# [67.4, 64.3, 58.9, 68.2, 66.2]])      2 = Baris 2 (index 1)

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_basketball = np.array([[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]])

# Print out the type of np_baseball
print(type(np_basketball))


# Print out the shape of np_baseball
print(np_basketball.shape)


baseball = [ [74, 215], [72, 210], [72, 210], [73, 188], [69, 209], [71, 200], [76, 231], [71, 180], [73, 180], [74, 185], [74, 160], [69, 180], [73, 189], [75, 185], [78, 219], [79, 230], [74, 230], [76, 195], [72, 180], [71, 192], [77, 203], [74, 195], [73, 182], [74, 188]
]

np_baseball = np.array(baseball)

# Print out the 20th row of np_baseball
print(np_baseball[19])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 24th player
print(np_baseball[23, 0])

import numpy as np

# 1. DATA UTAMA: baseball (Tinggi dalam inci, Berat dalam pon)
# Berisi 130 data pemain (Cukup untuk mencari pemain ke-124)
football = [[74, 215], [72, 210], [72, 210], [73, 188], [69, 176], [69, 209], [71, 200], [76, 231], [71, 180], [73, 180], [74, 185], [74, 160], [69, 180], [70, 185], [73, 189], [75, 185], [78, 219], [79, 230], [74, 230], [76, 225], [72, 190], [71, 225], [75, 185], [77, 160], [74, 200], [73, 210], [74, 222], [73, 234], [75, 220], [73, 170], [75, 220], [75, 210], [74, 225], [69, 180], [71, 185], [74, 260], [73, 200], [76, 250], [74, 210], [74, 203], [70, 210], [72, 210], [77, 210], [74, 210], [70, 186], [75, 198], [76, 175], [76, 200], [78, 210], [75, 215], [73, 211], [77, 244], [74, 180], [72, 200], [72, 195], [71, 220], [73, 211], [75, 200], [73, 180], [67, 165], [67, 175], [76, 216], [74, 220], [70, 218], [75, 215], [70, 195], [72, 240], [77, 215], [79, 235], [78, 223], [74, 220], [75, 213], [77, 225], [76, 244], [75, 220], [76, 210], [74, 215], [76, 198], [78, 220], [75, 215], [73, 216], [74, 215], [72, 210], [73, 215], [75, 195], [75, 200], [74, 215], [72, 229], [74, 270], [72, 200], [73, 190], [74, 220], [74, 210], [77, 230], [75, 221], [74, 205], [73, 215], [77, 250], [73, 210], [74, 215], [74, 190], [73, 220], [77, 211], [74, 220], [77, 228], [75, 235], [77, 250], [75, 210], [74, 180], [70, 205], [73, 190], [73, 200], [75, 250], [73, 210], [72, 215], [74, 200], [74, 210]
]

# 2. DATA PERUBAHAN: updated (Pertambahan/perubahan nilai untuk setiap pemain)
# Format biasanya sama [perubahan_tinggi, perubahan_berat] untuk operasi matriks (np_baseball + np_updated)
updated = [
    [1.2, 2.3], [0.5, -1.1], [2.1, 0.4], [-0.5, 3.2], [1.0, -2.0], [0.8, 1.5], [-1.2, 0.0], [0.4, 2.1], [1.5, -3.4], [0.0, 1.2],
    [1.1, 2.0], [-0.4, 1.1], [0.9, -0.5], [2.3, 3.1], [-1.0, 1.0], [0.5, -2.1], [1.4, 0.8], [0.2, 1.9], [-0.8, -1.5], [1.7, 2.5],
    [0.6, 0.4], [-1.1, 3.0], [0.3, -2.2], [1.5, 1.1], [-0.4, 0.9], [1.2, -1.0], [2.0, 3.4], [-0.5, 1.5], [0.7, -0.8], [1.1, 2.1],
    [0.2, 1.1], [-1.4, 2.5], [0.9, -1.2], [1.3, 0.4], [-0.2, 3.1], [1.0, -2.0], [0.5, 1.5], [-1.1, 0.0], [0.4, 2.1], [1.6, -3.4],
    [1.2, 2.0], [-0.5, 1.1], [0.8, -0.5], [2.2, 3.1], [-0.9, 1.0], [0.4, -2.1], [1.3, 0.8], [0.1, 1.9], [-0.7, -1.5], [1.6, 2.5],
    [0.5, 0.4], [-1.0, 3.0], [0.2, -2.2], [1.4, 1.1], [-0.3, 0.9], [1.1, -1.0], [1.9, 3.4], [-0.4, 1.5], [0.6, -0.8], [1.0, 2.1],
    [0.1, 1.1], [-1.3, 2.5], [0.8, -1.2], [1.2, 0.4], [-0.1, 3.1], [0.9, -2.0], [0.4, 1.5], [-1.0, 0.0], [0.3, 2.1], [1.5, -3.4],
    [1.1, 2.0], [-0.4, 1.1], [0.7, -0.5], [2.1, 3.1], [-0.8, 1.0], [0.3, -2.1], [1.2, 0.8], [0.0, 1.9], [-0.6, -1.5], [1.5, 2.5],
    [0.4, 0.4], [-0.9, 3.0], [0.1, -2.2], [1.3, 1.1], [-0.2, 0.9], [1.0, -1.0], [1.8, 3.4], [-0.3, 1.5], [0.5, -0.8], [0.9, 2.1],
    [0.0, 1.1], [-1.2, 2.5], [0.7, -1.2], [1.1, 0.4], [0.0, 3.1], [0.8, -2.0], [0.3, 1.5], [-0.9, 0.0], [0.2, 2.1], [1.4, -3.4],
    [1.0, 2.0], [-0.3, 1.1], [0.6, -0.5], [2.0, 3.1], [-0.7, 1.0], [0.2, -2.1], [1.1, 0.8], [-0.1, 1.9], [-0.5, -1.5], [1.4, 2.5],
    [0.3, 0.4], [-0.8, 3.0], [0.0, -2.2], [1.2, 1.1], [-0.1, 0.9], [0.9, -1.0], [1.7, 3.4], [-0.2, 1.5], [0.4, -0.8], [0.8, 2.1],
    [1.1, 2.0], [-0.4, 1.1], [0.7, -0.5], [2.1, 3.1], [-0.8, 1.0], [0.3, -2.1], [1.2, 0.8], [0.0, 1.9], [-0.6, -1.5], [1.5, 2.5]
]

# Konversi ke NumPy Array 2D
np_football = np.array(football)
np_updated = np.array(updated)

# Contoh 1: Cetak baris ke-50 (Indeks 49)
print("Baris ke-50:\n", np_football[49, :])

# Contoh 2: Ambil kolom kedua (Berat badan)
np_weight_lb = np_football[:, 1]

# Contoh 3: Cetak TINGGI badan pemain ke-80 (Baris indeks 80, Kolom indeks 0)
print("\nTinggi pemain ke-80:", np_football[79, 0])

# Contoh 4: Penjumlahan Matriks (Mengupdate data baseball)
np_football_baru = np_football + np_updated[:len(np_football), :] # Menyesuaikan panjang baris sesuai panjang baris di kolom sebelahnya
print("\nData 5 pemain pertama setelah diupdate:\n", np_football_baru[0:5, :])
