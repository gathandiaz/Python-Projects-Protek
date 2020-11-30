try:
    buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
    print("Daftar Harga Buah/Kg :")
    no = 1
    for n,m in buah.items():
        print(no,'.', n,'= Rp.',m)
        no += 1
    pilih = input("Nama buah yang dibeli : ")
    if(pilih in buah):
        timbang = float(input('Berapa Kg             : '))
        print('------------------------------------')
        print("Total harga           : Rp.",buah[pilih] * timbang)
    else:
        print('{0} tidak ada dalam daftar buah yang dijual'.format(pilih))
except ValueError:
    print('Data yang anda masukan bukan nominal angka')
