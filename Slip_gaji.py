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

