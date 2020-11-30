print('==============================')
data = []
x = int(input('Berapa mahasiswa? : '))

def namaMhs(m):
    y = 0
    for y in range (0,x):
        y += 1
        angka = str(input('Masukan nama mahasiswa ke-'+ str(y) + " : "))
        n = 0
        for y in angka :
            n += 1
        formula = angka + '(' + str(n) + ' karakter)'
        data.append(formula)
    print('------------------------------')
    print('Pendataan mahasiswa =')
    data.sort()
    for a in data:
        print(a)

print('------------------------------')
print('Data mahasiswa =')
print('------------------------------')

namaMhs(data)
