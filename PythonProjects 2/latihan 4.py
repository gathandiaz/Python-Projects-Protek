import math
#jarak
AB = 125
AB2 = 62

#kecepatan
BC = 256
BC2 = 70

#penghitungan waktu
jamawal = 6
waktuAB = math.ceil(AB / AB2*60)
waktuBC = math.ceil(BC / BC2*60)
waktuIstirahat = 45
totalwkttempuh = waktuAB + waktuBC + waktuIstirahat
totaljamtempuh = (totalwkttempuh//60)+jamawal
totalmenittempuh = totalwkttempuh%60

#estimasi waktu

print("jika pak amir istirahat dikota B 45 menit dan awal berangkat pukul 06.00, maka")
print("pak amir sampai di kota C pukul",(totaljamtempuh),".",(totalmenittempuh))
