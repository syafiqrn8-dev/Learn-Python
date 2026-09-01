# Plot Dasar yang di pelajari di Matplotlib:
# Visualisasi Data
# Struktur Data
# Struktur Kendali yang menyesuaikan dengan script dan Algortima

# Visualisasi Data
# - Eksplorasi Data
# - Wawasan Laporan

# SUB PACKAGE MATPLOTLIB
# - Pyplot

import matplotlib.pyplot as plt
import random

# CONTOH

# Mari kita cari Wawasan tentang Evolusi Populasi Manusia di Dunia
year = [1950, 1970, 1990, 2010]
populations = [2.696, 3.404, 5.200, 6.106] 

# Membuat Plot Bagan Garis dengan plot(Bagan Garis Horizontal, Bagan Garis Vertikal), plot() didalam kurungnya disebut Argumen
plot_bagan_garis = plt.plot(year, populations)

# Setelah membuat Plot(),Python tidak akan langsung menampilkan visual bagan garis nya, jadi kita harus plt.show() untuk mrnampilkan visual bagan garis nya
plt.show()
print(plot_bagan_garis)

# DIAGRAM SEBAR : menampilkan Visualisasi dengan diagram dengan tik-titik, beda dengan plot yang menampilkannya dengan garis naik-turun
diagram_sebar = plt.scatter(year, populations)
plt.show()
print(diagram_sebar)

# SKALA LOGARITMATIK : xscale('log') xscale maksudnya skala x horizontal memberikan jarak angka data yang dikalikan jadi 1, 10, 100, 1000,... 
# Ini sangat cocok ketika data yang kita miliki perbandingan nilai nya mepet-mepet dan nilai nya bisa ribuan, sehingga mereka harus diberikan skala jarak agar tidak terlalu mepet dan diagram bisa di baca dengan baik

# 1. CONTOH PERBEDAANNYA NO XSCALE DENGAN XSCALE
gdp_cap = [999.3, 1921.1, 1571.2, 1357.9, 649.6, 649.6, 492.9, 1785.9, 1361.8, 1532.9, 432.9, 1951.9, 1731.9, 739.7, 690.9, 693.4, 886.8, 1239.6, 1091.1, 866.0, 1379.0, 623.2, 867.4, 986.2, 1129.7, 1656.3, 719.5, 1222.8, 1347.9, 474.3, 1372.1, 672.8, 504.1, 1918.2, 1945.0, 1693.4, 887.4, 556.3, 1494.8, 1104.2, 3586.5, 8437.3, 2447.1, 13821.2, 5364.1, 10612.8, 6052.2, 8760.9, 9107.2, 4403.1, 14604.6, 12076.7, 14213.5, 13632.8, 9772.7, 13984.4, 3150.4, 4547.8, 2588.0, 6229.3, 7052.8, 5527.5, 12773.6, 6637.8, 5652.1, 9055.0, 3832.0, 12428.6, 2969.2, 14829.5, 12039.2, 4583.3, 2071.8, 12601.0, 11189.1, 11477.1, 12026.5, 2962.6, 6660.1, 3506.3, 13220.3, 10102.9, 6301.7, 2826.3, 6042.8, 6227.4, 11484.9, 10288.2, 13533.8, 8138.8, 3554.7, 11272.2, 11890.2, 9296.6, 12022.6, 8419.3, 8795.5, 7558.0, 2330.4, 3402.6, 17985.8, 75459.0, 44863.8, 63314.2, 101218.8, 38682.8, 53986.4, 86777.4, 36735.8, 22313.1, 42526.4, 30316.0, 103321.3, 91771.4, 75173.4, 97788.8, 91348.8, 32724.2, 99793.1, 66237.5, 91706.8, 100128.7, 45210.3, 25454.9, 36653.8, 55575.2, 92711.4, 96769.4, 15660.5, 63521.0, 54654.0, 36100.2, 26387.2, 47073.4, 104576.4, 45704.3, 64285.1, 81786.8, 49544.8, 107319.3, 106432.5, 38919.3, 62238.6, 43583.4, 42059.8, 18504.3, 72908.6, 62754.5, 19890.5, 41471.4]

life_exp = []
for gdp in gdp_cap:
    if gdp < 2000:
        base = random.uniform(68.0, 78.0)
    elif gdp < 15000:
        base = random.uniform(78.0, 84.0)
    else:
        # Negara kaya bervariasi alami antara 81.0 sampai 85.5 (tidak mentok 85.0 terus)
        base = random.uniform(81.0, 85.5) 
    life_exp.append(base)


# 2. PROSES PEMBUATAN GRAFIK BERDAMPINGAN
plt.figure(figsize=(12, 5))

# --- Grafik Kiri (Linear) ---
plt.subplot(1, 2, 1)
plt.scatter(gdp_cap, life_exp, color='crimson', alpha=0.7)
plt.title("Skala Biasa (Linear)\nData Menumpuk Parah di Kiri", fontsize=12, fontweight='bold')
plt.xlabel("GDP per Kapita")
plt.ylabel("Angka Harapan Hidup (Tahun)")
plt.grid(True, linestyle='--', alpha=0.5)

# --- Grafik Kanan (Logaritmik) ---
plt.subplot(1, 2, 2)
plt.scatter(gdp_cap, life_exp, color='teal', alpha=0.7)
plt.xscale('log') # Kunci pengubah skala
plt.title("Skala Logaritmik ('log')\nData Menyebar & Pola Terlihat", fontsize=12, fontweight='bold')
plt.xlabel("GDP per Kapita (Skala Kelipatan)")
plt.ylabel("Angka Harapan Hidup (Tahun)")
plt.grid(True, which="both", linestyle='--', alpha=0.5) # "both" untuk garis grid log

plt.tight_layout()
plt.show()