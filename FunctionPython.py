# Function() : Dalam Python banyak sekali fungsi bawaan yang memiliki tujuannya tersendiri

Nilai_Ujian_Syafiq = [90.67, 88.93, 91.40, 95.73, 92.69, 94.54]
print(Nilai_Ujian_Syafiq) # 90.67, 88.93, 91.40, 95.73, 92.69, 94.54

Nilai_Tertinggi = max(Nilai_Ujian_Syafiq) # max() adalah Function untuk mencari nilai tertinggi
print(Nilai_Tertinggi) # 95.73

Nilai_Pembulatan = round(Nilai_Ujian_Syafiq[0]) # round fungsi yang mengubah desimal menjadi bilangan bulat, hasil pembulatan di sesuaikan ole desimal >50 apkaah angka bertambah 1 atau tetap
print(Nilai_Pembulatan) # 90,67 = 91

Pembulatan_dengan_Desimal = round(67.69404, 1) # bisa pembulatan untuk mengurangi angka desimal yang ada
print(Pembulatan_dengan_Desimal) # 67.69404 = 67.7

# Jika ingin tahu tentang suatu fungsi bisa berikan help() atau ?Function
print(help(round)) # Disini dijelaskan Fungsi round() itu bisa diisi dengan round(angka, jumlah digit desimal nya) misal round(40.411, 1) mengubah jadi 40.4
# Jika round(2.59) maka hasilnya akan 3 karena ia membulatkan desimal jika >50 tambah 1 = 3, jika <50 tetapkan = 2

# ada juga Function len(variabel) untuk mengjumlahkan panjang Karakter yang ada di variabel tersebut
Nama = "Syafiq Raihan Nafis"
Tahun_Lahir = 2008

print(len(Nama))
print(len(str(Tahun_Lahir))) # len() tidak bisa menjumlahkan integer jadi kita harus ubah 2008 menjadi string str(2008) = "2008" dan hasil nya 4 (karakter) 2 0 0 8

Merapihkan_Data = sorted(Nilai_Ujian_Syafiq) # dengan function sorted() kita bisa mengurutkan data dengan baik dan rapih
print(Merapihkan_Data) # jika sorted() saja maka ia akan mengurutkan nilai terkecil hingga nilai terbesar

print(help(sorted)) # Ini penjelasan sorted() lebih lengkap