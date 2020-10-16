import math
#waktu pinjam
rental1 = 6
rental2 = 0
kembali1 = 23
kembali2 = 50

#sewa
awal = 200000
kelanjutan = 10000
menit = 10000/60

#penghitungan waktu
waktupinjam = math.floor(kembali1 - rental1 + (kembali2/60) - (rental2/60))

#penghitungan sewa
print("biaya sewa = Rp.", (waktupinjam - 12)*kelanjutan + awal)
