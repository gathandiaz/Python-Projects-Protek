try:
    buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
    print("Daftar Harga Buah/Kg :")
    no = 1
    for n,m in buah.items():
        print(no,'.', n,'= Rp.',m)
        no += 1
    a = 0
    x = 'y'
    while x == 'y':
        pilih = input("Nama buah yang dibeli : ")
        if(pilih in buah):
            timbang = float(input('Berapa Kg             : '))
            a += (buah[pilih] * timbang)
            x = input('Beli buah yang lain (y/n)?')
        else:
            print('{0} tidak ada dalam daftar buah yang dijual'.format(pilih))
            break
except ValueError:
    print('Data yang anda masukan bukan nominal angka')
print('------------------------------------')
print("Total harga           : Rp.",a)
