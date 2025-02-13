#Program Menghitung Luas dan Keliling Lingkaran dengan Input Jari-jari
import math

def hitung_lingkaran(r):
    keliling = 2 * math.pi * r
    luas = math.pi * r ** 2
    return keliling, luas

r = float(input("Masukkan jari-jari lingkaran: "))
keliling, luas = hitung_lingkaran(r)

print("Keliling: %.2f" % keliling)
print("Luas: %.2f" % luas)
