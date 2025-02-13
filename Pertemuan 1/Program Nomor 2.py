#Program Klasifikasi Nilai Suhu
def klasifikasi_suhu(suhu):
    if suhu < 0:
        return "Membeku"
    elif suhu < 10:
        return "Sangat Dingin"
    elif suhu < 20:
        return "Sejuk"
    elif suhu < 30:
        return "Hangat"
    elif suhu < 40:
        return "Panas"
    else:
        return "Sangat Panas"

suhu = float(input("Masukkan suhu dalam derajat Celcius: "))
print(klasifikasi_suhu(suhu))