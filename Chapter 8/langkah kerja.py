print('1.)List ->',' ',end='')
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
print('a :',a,' ',end='')
print('b :',b)

print('2.)Menyisipkan indeks ->',' ',end='')
a.insert(2,10)
b.insert(1,15)
print('a :',a,' ',end='')
print('b :',b)

print('3.)Menyisipkan indeks terakhir ->',' ',end='')
a.append(4)
b.append(8)
print('a :',a,' ',end='')
print('b :',b)

print('4.)Ascending ->',' ',end='')
a.sort()
b.sort()
print('a :',a,' ',end='')
print('b :',b)

print('5.)List baru ->',' ',end='')
c = a[0:8]
d = b[2:10]
print('c :',c,' ',end='')
print('d :',d)

print('6.)List penjumlahan dari list baru ->',' ',end='')
e=[]
x=0
for x in range(len(c)):
    y = c[x]+d[x]
    e = e+[y]
print ('e :',e)

print('7.)Mengubah list kedalam tuple ->',end='')
data = tuple(e)
print(data)

print('8.)Nilai max, min, dan jumlah dari tuple ->')
nilaimax= max(data)
nilaimin= min(data)
hasil= sum(data)
print('A. Nilai Max :',end='')
print(nilaimax)
print('B. Nilai Min :',end='')
print(nilaimin)
print('C. Nilai Jumlah :',end='')
print(hasil)

print('9.)Variable ->','',end='')
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)

penyusun = set(myString)
print('10.)Karakter hurufnya -> ',end='')
print(penyusun)

listnya= list(penyusun)
listnya.sort()
print('11.)Karakter huruf setelah diurutkan -> ', end='')
print(listnya)

