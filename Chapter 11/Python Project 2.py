import datetime
while True:
    file = open("d:/DatPerpus1.txt", "a+")
    code = input("Masukkan Kode Member  = ")
    name = input("Masukkan Nama Member  = ")
    book = input("Masukkan Judul Buku   = ")
    print("\n")
    mil = input("Ulangi lagi (y/n) = ")
    print("\n")

    skrg = datetime.date.today()
    bts = datetime.timedelta(days=7)
    ambil = str(skrg + bts)
    dinoki = str(skrg)
    file2 = open("d:/DatPerpus1.txt", "a+")
    file2.write(code + "|" + name + "|" + book + "|" + dinoki + "|" + ambil + "\n")
    file2.close()

    if mil == "n":
        print("Data-data peminjam buku perpustakaan tersimpan pada (d:/DatPerpus1.txt)")
        break
    elif mil == "y":
        continue
    else:
        print("Input anda salah.")
        exit()
