buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}

def rerataHarga(x):
    listPrice = list(x.values())
    jumlah = sum(listPrice)
    banyak = len(listPrice)
    rerata = jumlah/banyak
    return rerata

print(rerataHarga(buah))
