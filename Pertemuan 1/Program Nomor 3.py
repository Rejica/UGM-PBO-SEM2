#Program Menentukan Nilai Siswa Dengan Alur yang Ditentukan
def hitung_nilai_akhir(nilai_tugas, nilai_laporan, nilai_ujian):
    rata_rata_tugas_laporan = (nilai_tugas + nilai_laporan) / 2
    if rata_rata_tugas_laporan < 40:
        return "K"
    nilai_akhir = (0.25 * nilai_tugas) + (0.25 * nilai_laporan) + (0.5 * nilai_ujian)
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

niu = input("Masukkan NIU (6 digit): ")
if len(niu) != 6 or not niu.isdigit():
    print("NIU harus berupa 6 digit angka.")
else:
    tugas = float(input("Masukkan nilai tugas: "))
    laporan = float(input("Masukkan nilai laporan: "))
    ujian = float(input("Masukkan nilai ujian: "))
    
    nilai_huruf = hitung_nilai_akhir(tugas, laporan, ujian)
    print(f"NIU: {niu}, Nilai Akhir: {nilai_huruf}") 