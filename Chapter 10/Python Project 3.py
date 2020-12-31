teks = open("d:/2.txt", "r")
baris = teks.readlines()
teks = len(baris)
p = {}
x=0
for tks in range(0,teks):
        m = baris[x]
        psh = m.split("|")
        m = psh[0]
        n = psh[1]
        o = psh[2].replace("\n", "")
        x += 1
        daftar = {"nim":m,"nama":n,"alamat":o}
        q = {x : daftar}
        p.update(q)
print('dataMhs = ',end='')
print(p)
