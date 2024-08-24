from datetime import datetime, timedelta, timezone

# Set timezone to WIB (UTC+7)
WIB = timezone(timedelta(hours=7))

print("============TOKO BUKU NH===============")
pembeli = input("Nama Pembeli : ")
print('Nama Pembeli :', pembeli)

def barang():
    global totalbarang
    global jumlah
    global nama_barang
    print("\n===============Alat Tulis===============")
    print("1. Spidol     - Rp.8000,00")
    print("2. Pensil     - Rp.2000,00")
    print("3. Pulpen     - Rp.2500,00")
    print("4. Tipex      - Rp.3500,00")
    print("5. Penggaris  - Rp.3000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4/5 : "))
    jumlah = int(input("Berapa Jumlah : "))

    if nomor == 1:
        totalbarang = jumlah * 8000
        print(jumlah, 'Spidol = Rp.', totalbarang)
        nama_barang = "Spidol"
    elif nomor == 2:
        totalbarang = jumlah * 2000
        print(jumlah, 'Pensil = Rp.', totalbarang)
        nama_barang = "Pensil"
    elif nomor == 3:
        totalbarang = jumlah * 2500
        print(jumlah, 'Pulpen = Rp.', totalbarang)
        nama_barang = "Pulpen"
    elif nomor == 4:
        totalbarang = jumlah * 3500
        print(jumlah, 'Tipex = Rp.', totalbarang)
        nama_barang = "Tipex"
    elif nomor == 5:
        totalbarang = jumlah * 3000
        print(jumlah, 'Penggaris = Rp.', totalbarang)
        nama_barang = "Penggaris"
    else:
        print('Pilihan tidak ada di daftar barang\nSilahkan pilih kembali !!!')
        barang()

def buku():
    global totalbuku
    global banyak
    global nama_buku
    print("\n===============Buku===============")
    print("1. Komik - Rp.30000,00")
    print("2. Kamus - Rp.50000,00")
    print("3. Novel - Rp.80000,00")
    print("4. Atlas - Rp.75000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    banyak = int(input("Berapa Jumlah : "))

    if nomor == 1:
        totalbuku = banyak * 30000
        print(banyak, 'Komik = Rp.', totalbuku)
        nama_buku = "Komik"
    elif nomor == 2:
        totalbuku = banyak * 50000
        print(banyak, 'Kamus = Rp.', totalbuku)
        nama_buku = "Kamus"
    elif nomor == 3:
        totalbuku = banyak * 80000
        print(banyak, 'Novel = Rp.', totalbuku)
        nama_buku = "Novel"
    elif nomor == 4:
        totalbuku = banyak * 75000
        print(banyak, 'Atlas = Rp.', totalbuku)
        nama_buku = "Atlas"
    else:
        print('Pilihan tidak ada di daftar buku\nSilahkan pilih kembali !!!')
        buku()

barang()
buku()
total_semua = totalbarang + totalbuku

print("\nTotal yang harus dibayar : Rp.", total_semua)

# Pilihan metode pembayaran
print("\nPilih Metode Pembayaran:")
print("1. Tunai")
print("2. Kartu")
metode_pembayaran = int(input("Masukkan Pilihan 1/2: "))

if metode_pembayaran == 1:
    uang = int(input("Uang Tunai Pembeli : Rp."))
    kembali = uang - total_semua
    print("Kembalian : Rp.", kembali)
    metode = "Tunai"
elif metode_pembayaran == 2:
    uang = total_semua  # Jumlah yang dibayarkan sama dengan total tagihan
    kembali = 0  # Tidak ada kembalian
    print("Pembayaran menggunakan kartu berhasil.")
    metode = "Kartu"
else:
    print("Pilihan tidak valid!")
    exit()

# Print struk dengan waktu WIB dan alamat toko
print("\n=============== S T R U K B E L I ===============")
print("Alamat Toko\t:", "Jalan Apel No.123, Jakarta")
print("Tanggal\t\t:", datetime.now(WIB).strftime("%d-%m-%Y %H:%M:%S"))
print("Nama\t\t:", pembeli)
print("Beli\t\t:", jumlah, nama_barang, "(Rp.", totalbarang, ")")
print("\t\t:", banyak, nama_buku, "(Rp.", totalbuku, ")")
print("Tagihan\t\t: Rp.", total_semua)
print("Metode Bayar\t: ", metode)
print("Dibayar\t\t: Rp.", uang)
print("Kembalian\t: Rp.", kembali)

print("==================================================")
print("==================================================")