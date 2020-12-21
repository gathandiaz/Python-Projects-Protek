try:
    print('masukkan n:angka,(max n:10)')
    x = int(input("berapa n ? n:"))
except ValueError:
    print('Bukan Angka')
    exit()
def bintang(x):
    if x > 0 :
        for y in range(x):
            z = '*' + '**'*y
            print(z.center(20,' '))
    else:
        print('Angka Negatif Tidak Bisa')
bintang(x)

