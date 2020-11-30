data = []
x = int(input('Banyak bilangan yang mau diinput? : '))
y = 0
for y in range (0,x):
    y += 1
    try :
        angka = int(input("Masukan bilangan ke-"+ str(y) + " : "))
        data.append(angka)
    except ValueError:
        print("Data yang anda masukkan bukan bilangan/angka")
        break
data.sort(reverse = True)
print("Descending(Urutan dari bilangan yang terbesar) :", data)
