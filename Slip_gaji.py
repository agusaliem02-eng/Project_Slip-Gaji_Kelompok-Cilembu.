def garis():
    print("=" * 45)

def hitung_gaji(jabatan):
    # Gaji pokok sesuai jabatan
    if jabatan == "magang":
        gaji_pokok = 1_500_000
    elif jabatan == "karyawan":
        gaji_pokok = 3_500_000
    elif jabatan == "manajer":
        gaji_pokok = 7_000_000
    else:
        print("Jabatan tidak dikenal!")
        gaji_pokok = 0
    return gaji_pokok

def tambah_bonus(gaji):
    bonus = int(input("Masukkan jumlah bonus : Rp "))
    gaji += bonus
    print(f"Bonus sebesar Rp {bonus:,} berhasil ditambahkan.")
    print(f"Total gaji sementara: Rp {gaji:,}")
    return gaji

def potong_gaji(gaji):
    potongan = int(input("Masukkan jumlah potongan : Rp "))
    if potongan > gaji:
        print("Potongan melebihi total gaji! Tidak dapat diproses.")
    else:
        gaji -= potongan
        print(f"Potongan sebesar Rp {potongan:,} berhasil dikurangkan.")
        print(f"Gaji setelah potongan: Rp {gaji:,}")
    return gaji
    
def tampilkan_slip(nama, jabatan, gaji):
    garis()
    print("SLIP GAJI KARYAWAN")
    garis()
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Bersih   : Rp {gaji:,}")
    garis()
    print("Terima kasih atas kerja keras Anda.")
    garis()

def main():
    garis()
    print("PROGRAM SLIP GAJI KARYAWAN")
    garis()
    nama = input("Masukkan nama karyawan : ").title()
    jabatan = input("Masukkan jabatan (Magang/Karyawan/Manajer): ").lower()
    gaji = hitung_gaji(jabatan)

    while True:
        garis()
        print("PILIH MENU DI BAWAH INI!")
        garis()
        print("1. Tambah Bonus")
        print("2. Tambah Potongan")
        print("3. Cetak Slip Gaji")
        print("4. Keluar Program")
        garis()
        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            gaji = tambah_bonus(gaji)
        elif pilihan == '2':
            gaji = potong_gaji(gaji)
        elif pilihan == '3':
            tampilkan_slip(nama, jabatan, gaji)
        elif pilihan == '4':
            garis()
            print("Program selesai. Terima kasih.")
            garis()
            break
        else:
            print("Pilihan tidak valid!")

main()
