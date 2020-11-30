print('------------------------------')
print('   PROGRAM HITUNG RATA-RATA   ')
print('------------------------------')

q = 0
sum = 0
while True:
    try:
        x = int(input('Masukkan bilangan bulat: '))
        sum += x
        q += 1
        y = input('Lagi (y/n)? : ')
        if y == 'n':
            avg = sum/q
            print('hasil rata-rata : ',avg)
            break
        elif y != 'y':
            print('Ulangi jalankan script dan jangan menginput selain (y/n) dibagian ini!')
            break
    except ValueError:
        print('Bukan bilangan bulat')
