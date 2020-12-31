def listnya():
    file = open("d:/1.txt", "r")
    x = []
    for num in file:
        x.append(int(num))
    return x


p = open("d:/1.txt", "w")
p.write("100\n102\n99\n89\n192\n938\n107\n241\n")
p.close()

data = listnya()
x = 0
gnp = 0
gjl = 0
for num in data:
    q = data[x]
    if num % 2 == 0:
        gnp += 1
    if num % 2 == 1:
        gjl += 1
    x += 1


#output akhir :)
print("Outputnya:\nBanyaknya bilangan genap : ", gnp,
      "\nBanyaknya bilangan ganjil: ",gjl)
