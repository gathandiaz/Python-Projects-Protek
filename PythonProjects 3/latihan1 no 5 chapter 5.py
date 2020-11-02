kode      = int(input("Masukkan kode karyawan               = "))
nama      = str(input("Masukkan nama karyawan               = "))
gol       = str(input("Masukkan golongan karyawan           = "))
status    = int(input("Masukkan status (1:Menikah 2:Belum)  = "))
if(status == 1):
    statusnya = "Sudah Menikah"
    jmlhAnak  = int(input("Masukkan jumlah anak                 = "))
else:
    statusnya = "Belum Menikah"

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

if(status == 1):
    I = GajiPokok * 10/100
    A = GajiPokok * jmlhAnak * 5/100
if(status == 1):
    GajiKotor = GajiPokok + I + A   
else:
    GajiKotor = GajiPokok

Potongan = GajiPokok * disc/100

GajiBersih = GajiKotor - Potongan

print("==========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------------")
print("Kode Karyawan        = ",kode)
print("Nama Karyawan        = ",nama)
print("Golongan             = ",gol)
print("Status Menikah       = ",statusnya)
if(status == 1):
    print("Jumlah Anak          = ",jmlhAnak)
print("------------------------------------------")
print("Gaji Pokok           = Rp.",GajiPokok)
if(status == 1):
    print("Tunjangan Istri      = RP.",I)
    print("Tunjangan Anak       = RP.",A)
print("------------------------------------------")
print("Gaji Kotor           = RP.",GajiKotor)
print("Potongan ({0}%)      = Rp.({1})".format(disc,Potongan))
print("------------------------------------------")
print("Gaji Bersih          = Rp.",(GajiKotor-Potongan)) 
