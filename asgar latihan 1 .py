def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        print("Diskon yang Anda dapatkan: Rp.", diskon)
    else:
        print("Total belanjaan Anda: Rp.", total_belanja)
        print("Maaf, Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000")

# Input total belanjaan dari pengguna
total_belanjaan = float(input("Masukkan total belanjaan Anda: Rp. "))

# Hitung dan tampilkan diskon atau pesan jika tidak mendapat diskon
hitung_diskon(total_belanjaan)
