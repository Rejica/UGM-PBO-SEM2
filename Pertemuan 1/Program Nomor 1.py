#Program Menerima Input Angka dan Output Hitung Mundur
try:
    num = int(input("Masukkan angka: "))
    print(*range(num, -1, -1))
except ValueError:
    print("Harap masukkan angka yang valid!")
