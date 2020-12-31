def Nkripsi(x, y) :
    listx = list(x)
    for i in range(len(listx)) :
        if(listx[i] != " ") :
            if(ord(listx[i]) + y < 91) :
                ascii = ord(listx[i])
                z = ascii + y
                listx[i] = chr(z)
            else :
                ascii = ord(listx[i])
                z = (ascii + y) - 26
                listx[i] = chr(z)
        else :
            continue
    hasil = "".join(listx)
    return hasil
try :
    p = input("File yang akan di enkripsi (contoh(d:/___.txt)): ")
    file = open(p,"r")
    s = (file.read())
    q = int(input("Jumlah geseran enkripsi : "))
    hasil = Nkripsi(s, q)
    r = open("d:/sandi.txt","a")
    r.write(hasil)
    r.close()
    print("\nHasil pengenkripsian teks {0} adalah : {1}".format(s, hasil),
          ("\n\n\tHasilnya Ini Bisa Kita lihat pada (d:/sandi.txt)"))
except ValueError :
    print("Masukkan Bilangan Bulat")
