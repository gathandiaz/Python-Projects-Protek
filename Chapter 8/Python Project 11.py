buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def tampilkan(data):
    print("Daftar Harga Buah/Kg :")
    no = 1
    for n,m in buah.items():
        print(no,'.', n,'= Rp.',m)
        no += 1
tampilkan(buah)
print('=========================')
menu = ["Menu:",
"A. Tambah data buah",
"B. Beli buah"]
for z in menu:
    print(z)
print('-------------------------')
pil = input('pilihan menu (A/B) : ')
print('-------------------------')

if pil == 'A':
    x = input('Masukkan nama buah    :')
    if(x in buah):
        print('Buah sudah ada')
    else:
        while True:
            try:
                y = int(input('Masukkan harga satuan :'))
                buah[x] = y
                tampilkan(buah)
                break
            except ValueError:
                print('Data yang anda masukkan bukan nominal angka')

                
elif pil == 'B':
    tampilkan(buah)
    a = 0
    x = 'y'
    while x == 'y':
        pilih = input("Nama buah yang dibeli : ")
        if(pilih in buah):
            while True:
                try:
                    timbang = float(input('Berapa Kg             : '))
                    a += (buah[pilih] * timbang)
                    x = input('Beli buah yang lain (y/n)?')
                    break
                except ValueError:
                    print('Data yang anda masukan bukan nominal angka')
        else:
            print('{0} tidak ada dalam daftar buah yang dijual'.format(pilih))

    print('------------------------------------')
    print("Total harga           : Rp.",a)

