while True:
    try:
        data = open("d:/2.txt", "a+")
        nim = input("\nMasukkan NIM		: ")
        nama = str(input("Masukkan Nama Mhs	: "))
        almt = input("Masukkan Alamat	        : ")
        p = nim + "|"
        q = nama + "|"
        data.write(p)
        data.write(q)
        data.write(almt+"\n")
        data.close
        ulang = input("\nUlangi input lagi(y/n)? :")
        if ulang == "n":
            data = open("d:/2.txt", "r")
            print("\nDATA MAHASISWA :")
            baca = data.read()
            print(baca)
            break
        elif ulang == "y" :
            continue
    except ValueError:
        print("input salah")
