buka = open("d:/5.txt", "r")
print(buka.read())
buka.close()

buka = open("d:/5.txt", "r")
hasil = open("d:/5jml.txt", "a+")
file = []
file2 = []
x = 0
hasil.write("\n")
hasil.write("Hasil penjumlahan file 5.txt(Bil. diatas) dari ruas kiri dan kanan ialah =\n")
for baris in buka:
    psh = baris.split("|")
    file.append(psh[0])
    file2.append(psh[1].strip())
    jumlah = int(file[x]) + int(file2[x])
    hasil.write(str(jumlah))
    hasil.write("\n")
    x+=1
hasil.write("\n")
buka.close()
hasil.close()

hasil = open("d:/5jml.txt", "r")
print(hasil.read())
hasil.close()
print("\tHasil Penjumlahan ini Bisa Kita Jumpai pada(d:/5jml.txt)")
