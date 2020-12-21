import random
def sufflestring(x,n):
    teks = list(x)
    lis = []
    for i in range(n):
        random.shuffle(teks)
        z = ("".join(teks))
        if z not in lis:
            lis.append(z)
    print(lis)
sufflestring("zaid",28)
