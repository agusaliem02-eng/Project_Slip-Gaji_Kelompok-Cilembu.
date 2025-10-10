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

