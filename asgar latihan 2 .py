def hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas):
    total_nilai_kehadiran = kehadiran * 16
    total_nilai_tugas = sum(nilai_tugas)
    nilai_akhir = total_nilai_kehadiran + total_nilai_tugas + nilai_uts + nilai_uas
    return nilai_akhir

def tentukan_hasil_nilai(nilai_akhir):
    if nilai_akhir >= 90:
        return "A"
    elif nilai_akhir >= 80:
        return "B"
    elif nilai_akhir >= 70:
        return "C"
    elif nilai_akhir >= 60:
        return "D"
    else:
        return "E"

def main():
    kehadiran = int(input("Masukkan jumlah kehadiran mahasiswa: "))
    nilai_tugas = []
    for i in range(1, 9):
        nilai = float(input("Masukkan nilai tugas ke-{}: ".format(i)))
        nilai_tugas.append(nilai)
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas)
    hasil_nilai = tentukan_hasil_nilai(nilai_akhir)

    print("Nilai akhir mahasiswa:", nilai_akhir)
    print("Hasil nilai:", hasil_nilai)

if __name__ == "__main__":
    main()
