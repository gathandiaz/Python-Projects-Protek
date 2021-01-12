import datetime
x = open("d:/DatPerpus1.txt", "r")
data  = []
data2 = []
data3 = []
data4 = []
data5 = []

for line in x:
    psh = line.split("|")
    data.append(psh[0])
    data2.append(psh[1])
    data3.append(psh[2])
    data4.append(psh[3])
    data5.append(psh[4].strip())

mil = str(input("Masukkan kode member yang mau dicari : "))
if mil in data:
    dapat = True
    a = data.index(mil)
    skrg = datetime.datetime.now()
    y = data5[a]
    from datetime import datetime
    y = datetime.strptime(y, "%Y-%m-%d")
    form = y - skrg
    from datetime import *
    kembali = datetime.date(skrg)
    maks = datetime.date(y)
if dapat == True:
    form = datetime.date(skrg) - maks
    form = int(form.days)
    denda = 0
    if form >= 0:
        denda = 2000 *(form)
        form = abs(form)
    elif form <= 0:
        form = 0

    print("\nData Peminjaman Buku\n"
         "\nKode Member                    : ",data[a],
         "\nNama Member                    : ",data2[a],
         "\nJudul Buku                     : ",data3[a],
         "\nTanggal Peminjaman             : ",data4[a],
         "\nTanggal Maks Peminjaman        : ",data5[a],
         "\nTanggal Pengembalian           : ",kembali,
         "\ntelat                          : ",form,"Hari",
         "\nTotal denda                    :  Rp.",denda)

else:
    print("Data tidak ditemukan")
