def Dkripsi(x, y) :
    listx = list(x)
    for i in range(len(listx)) :
        if(listx[i] != " ") :
            if(ord(listx[i]) - y >= 65) :
                ascii = ord(listx[i])
                z = ascii - y
                listx[i] = chr(z)
            else :
                ascii = ord(listx[i])
                z = (ascii + 26) - y
                listx[i] = chr(z)
        else :
            continue
    hasil = "".join(listx)
    return hasil
try :
    p = input("File yang akan di dekripsi (contoh(d:/___.txt)): ")
    file = open(p,"r")
    s = (file.read())
    q = int(input("Jumlah geseran dekripsi : "))
    hasil = Dkripsi(s, q)
    r = open("d:/asli.txt","a")
    r.write(hasil)
    r.close()
    print("\nHasil pendekripsian teks {0} adalah : {1}".format(s, hasil),
          ("\n\n\tHasilnya Ini Bisa Kita lihat pada (d:/asli.txt)"))
except ValueError :
    print("Masukkan Bilangan Bulat")
