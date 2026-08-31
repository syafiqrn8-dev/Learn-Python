# Method: Fungsi yang termasuk dalam objek
# Dalam Python semua adalah Objek dan Objek memiliki Method tertentu tergantung tipe data nya
# Ada beberapa Method yang bisa untuk beberapa tipe data, salah satu nya index() (Bisa untuk string dan Array)


Name = "Syafiq" # Contoh Method: capitalize(), replace()

Height = 170.8 # Contoh Method: bit_length(), conjugate()

Murid_XII_C = ["Andre", "Bayu", "Chaerul", "Dewi", "Elza", "Fikri", "Gibran"] # Contoh Method: index(), count()

print(Murid_XII_C.index("Chaerul")) # Panggil Method index() di Array, Chaerul = 2 (index ke-2)
print(Murid_XII_C.append("Hilman")) # .append(Data Baru) menambahkan data
print(Murid_XII_C.reverse()) # Membalikkan urutan Array

Nilai_Rapot = [90, 91, 90, 94, 88, 85, 97]
print(Nilai_Rapot.count(90)) # Count menghitung angka yang dipilih ada berapa angka yang seperti itu, di dalam Array Nilai_Rapot ada 2 nilai 90 jadi hasil nya count(90) = 2

# Method str

Username = "neura seona"
print(Username.capitalize()) # Memberikan huruf Kapital di awal kalimat saja
print(Username.title()) # Memberikan huruf kapital di tiap kata 
print(Username.upper()) # Memberikan semua huruf Kapital dalam tiap kata
print(Username.replace("seona", "launa")) # Menggantikan/mengubah kata
