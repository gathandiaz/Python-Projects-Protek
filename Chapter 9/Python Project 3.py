import math
try:
    print('masukkan n:angka ganjil')
    x = int(input('berapa n ? n:'))
except ValueError:
    print('Bukan Angka')
    exit()
def bintang(x):
    if x > 0 :
        if (x%2 != 0):
                x = math.ceil(x/2)
                for y in range(x):
                    z = '*' + '**'*y
                    print(z.center(20,' '))
                pp = 0
                q = x -1
                for r in range(q):
                    pp += 1
                    s = '*' + '**'*(q - pp)
                    print(s.center(20,' '))
        else:
            print('Angka negatif atau Bil Ganjil Tidak Bisa')
bintang(x)
