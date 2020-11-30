try:
    x = input("Masukkan nama file: ")
    file = open(x,"r")
    print("Isi file",x,"adalah: ")
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
