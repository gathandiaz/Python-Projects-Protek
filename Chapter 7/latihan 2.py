try:
    x = input("Masukkan nama file: ")
    data = open(x,'r')
    z = 'y'
    while z == 'y':
        data = open(x,"a")
        y = input("Data yang mau ditambahkan: ")
        file.write(y)
        z = input("Mau lagi (y/n): ")
        file.close()   
except FileNotFoundError:
        print('File tidak ditemukan')
