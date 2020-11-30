print('=========================')
menu = ["Menu:",
"A. Tambah data sayur",
"B. Hapus data sayur",
"C. Tampilkan data sayur"]
for z in menu:
    print(z)
print('-------------------------')

pil = input('Pilihan anda (A/B/C) : ')

print('-------------------------')

if pil == 'A':
    print('Daftar Sayuran : ')
    x = ["kacang", "sawi", "terong" , "cabai" , "kangkung", "seledri", "bawang"]
    for y in x:
        print(y)
    print('-----------------------------------------------')
    tmbh = input('Nama sayur yang ingin ditambahakan : ')
    x.append(tmbh)
    print('-----------------------------------------------')
    print('Jadi sayur yang ada sekarang : ', x)
elif pil == "B":
    try:
        print('Daftar Sayuran : ')
        x = ["kacang", "sawi", "terong" , "cabai" , "kangkung", "seledri", "bawang"]
        for y in x:
            print(y)
        print('-----------------------------------------------')
        hps = input('Nama sayur yang ingin dihapus : ')
        print('-----------------------------------------------')
        print('Jadi sayur yang ada sekarang :')
        x.remove(hps)
        for y in x:
            print(y)
    except ValueError:
        print('Data tidak ditemukan')
elif pil == 'C':
    print('Daftar Sayuran : ')
    x = ["kacang", "sawi", "terong" , "cabai" , "kangkung", "seledri", "bawang"]
    for y in x:
        print(y)
else:
    print('Input anda salah')
