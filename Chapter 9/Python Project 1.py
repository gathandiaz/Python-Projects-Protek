def ubahHuruf(teks,a,b):
    x = teks
    y = a
    z = b
    for p in range(len(z)):
        x = x.replace(y[p],z[p])
    print(x)

ubahHuruf('MATEMATIKA','T','S')
