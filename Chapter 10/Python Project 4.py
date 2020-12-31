print("\t    ~SELAMAT DATANG~ \nPastikan anda memasukkan NIM dengan benar!\n")
x = open("d:/2.txt", "r")
file = []
file2 = []
file3 = []
for baris in x:
    psh = baris.split("|")
    file.append(psh[0])
    file2.append(psh[1])
    file3.append(psh[2].strip())

y = str(input("Masukkan NIM yang mau dicari : "))
if y in file:
    z = file.index(y)
    print("\nData Mahasiswa\nNIM    :",file[z],"\nNama   :",file2[z],"\nAlamat :",file3[z])
else:
    print("Data mahasiswa tidak ditemukan")
