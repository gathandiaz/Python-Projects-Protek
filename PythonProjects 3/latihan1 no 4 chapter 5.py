kode      = int(input("Masukkan kode karyawan               = "))
nama      = str(input("Masukkan nama karyawan               = "))
gol       = str(input("Masukkan golongan karyawan           = "))

if(gol == 'A'):
    GajiPokok = 10000000
    disc = 2.5
elif(gol == 'B'):
    GajiPokok = 8500000
    disc = 2.0
elif(gol == 'C'):
    GajiPokok = 7000000
    disc = 1.5
elif(gol == 'D'):
    GajiPokok = 7000000
    disc = 1.0
else:
    print("Golongan Tidak Ditemukan")
    exit()

Potongan = GajiPokok * disc/100
GajiBersih = GajiPokok - Potongan

print("==========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------------")
print("Kode Karyawan        = ",kode)
print("Nama Karyawan        = ",nama)
print("Golongan             = ",gol)
print("------------------------------------------")
print("Gaji Pokok           = Rp.",GajiPokok)
print("Potongan ({0}%)      = Rp.({1})".format(disc,Potongan))
print("------------------------------------------")
print("Gaji Bersih          = Rp.",GajiBersih) 
