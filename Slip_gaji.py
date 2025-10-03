print("==========Program Slip Gaji==========")

print('uhuy')

print('mabar')

def pemasukan(jumlah):
    return jumlah

def pengeluaran(jumlah):
    return jumlah

def sisa_saldo(masuk, keluar):
    return masuk - keluar

def tampilkan_slip(nama, pemasukan, pengeluaran, sisa):
    print("\n===============")
    print(f"Money Manajer")
    print("===============")
    print(f"Nama   : {nama}")
    print(f"Pemasukan (20%): Rp {pemasukan:,}")
    print(f"Pengeluaran    : Rp {pengeluaran:,}")
    print("-------------------------------")
    print(f"Sisa saldo : Rp {sisa:,}")
    print("===============================\n")

def main():
    while True:
        nama = input('Masukan nama kamu : ')
        masuk = int(input('Masukan pemasukan : '))
        keluar = int(input('Masukan pengeluaran : '))
        masukan = pemasukan(masuk)
        luaran = pengeluaran(keluar)
        sisa = sisa_saldo(pemasukan, pengeluaran)

        tampilkan_slip(nama, pemasukan, pengeluaran, sisa)

        ulang = input('Buat pemasukan atau pengeluaran baru? (y/n)')
        if ulang == 'y':
            continue
        elif ulang == 'n':
            print("\nTerima kasih! Program selesai.")
            break

main()
