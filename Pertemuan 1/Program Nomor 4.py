#Program Untuk Cek Angka Prima atau Bukan
def cek_prima(n):
    if n < 2:
        return "Bukan angka prima"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Bukan angka prima"
    return "Angka prima"

angka = int(input("Masukkan angka: "))
print(cek_prima(angka))
