buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}
def hargaBuwah(y):
    price = list(y.values())
    price.sort(reverse = True)
    hargaMahal = price[0]
    for buah, price in y.items():
        if price == hargaMahal:
            return buah
print('harga buah termahal = ',hargaBuwah(buah))
