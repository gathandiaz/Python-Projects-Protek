from random import randint
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
bil = randint(0,100)
while True:
    bil1 = int(input("tebakan anda ="))
    if (bil1 == bil):
        print ("Yeeee… Bilangan tebakan anda BENAR :-)")
        break
    elif (bil1 > bil):
        print ("Hehehe… Bilangan tebakan anda terlalu besar")
    elif (bil1 < bil):
        print ("Hehehe… Bilangan tebakan anda terlalu kecil")
        
