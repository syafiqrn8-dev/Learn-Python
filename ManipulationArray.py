# Mengubah isi Array

# Array
Daftar_Keluarga = ["Andi", "Budi", "Elma", "Jenny", "Kiel", "Lawliet"]
print(Daftar_Keluarga)
print(Daftar_Keluarga[0])  # Andi

Daftar_Keluarga[3] = "Juanda"  # Mengubah isi Array di index 3 "Jenny"
print(Daftar_Keluarga[3])  # sekarang isi index 3 bukan Jenny lagi, tapi Juanda

# Bisa Mengubah beberapa index sekaligus
Daftar_Keluarga[0:2] = ["Aldo", "Bryan"]
print(Daftar_Keluarga[0:2])  # Andi, Budi dihapus, ganti jadi Aldo, Bryan

# dengan + kamu bisa menambahkan isi data di dalam Array
Daftar_Keluarga_Baru = Daftar_Keluarga + ["Molly", "Neura"]
print(Daftar_Keluarga_Baru)

del Daftar_Keluarga_Baru[6]  # Menghapus index ke 6 "Molly"
print(Daftar_Keluarga_Baru)


# Array dalam Array
Data_Murid = [
    ["Ardi", "X-C"],
    ["Bensu", "XI-B"],
    ["Clara", "XII-A"]
]
print(Data_Murid)
print(Data_Murid[0])  # ["Ardi", "X-C"]
print(Data_Murid[2][1])  # "XII-A"


# Hal unik dalam Array
x = ["a", "b", "c", "d", "e"]  # x = a, b, c, d, e
y = x  # sekarang y memiliki isi data Array milik x
y[1] = "z"  # y mengubah isi data Array di index 1 "b" menjadi "z"
print(y)  # pasti y = a, z, c, d, e
print(x)  # tapi lihat x juga memiliki data yang sama x = a, z, c, d, e. berarti ketika y mengubah data, data si x juga ikut ke ubah

# Solusinya agar data lama tidak ikut terubah berikan list() atau x[:] lalu ubah data nya
y = list(x)
y[3] = "v"
print(y) # coba bedakan dengan data lama, data ini pasti berbeda dan bisa di sebut data sementara (temporary data)
y = x[:]
y[4] = "p"
print(y) # y temp data sebelumnya y = a, b, c, v, e. Tapi y sekarang ini y = a, b, c, d, p coba running code nya
