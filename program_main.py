# main.py

from modul_kalkulator import tambah, kurang, kali, bagi

def main():
    print("Kalkulator Sederhana")
    
    # Meminta input dari pengguna
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Melakukan semua operasi
    hasil_tambah = tambah(angka1, angka2)
    hasil_kurang = kurang(angka1, angka2)
    hasil_kali = kali(angka1, angka2)
    hasil_bagi = bagi(angka1, angka2)

    # Menampilkan hasil
    print(f"Hasil Penjumlahan: {hasil_tambah}")
    print(f"Hasil Pengurangan: {hasil_kurang}")
    print(f"Hasil Perkalian: {hasil_kali}")
    print(f"Hasil Pembagian: {hasil_bagi}")

if __name__ == "__main__":
    main()