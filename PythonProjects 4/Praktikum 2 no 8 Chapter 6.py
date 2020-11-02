def luasSegitiga(a,t):
    luas = a * t / 2
    return luas

print('Luas segitiga dg alas ',10 ,
      'dan tinngi', 20,
      'adalah', luasSegitiga(10,20))
print('Luas segitiga2 dg alas ',15 ,
      'dan tinngi', 45,
      'adalah', luasSegitiga(15,45))

total = luasSegitiga(10,20) + luasSegitiga(15,45)
print("Total jumlah luas kedua segitiga adalah =", str(total))
