hitung = 0
sum = 0
for i in range(100):
    if i % 2 == 1:
        hitung = hitung + 1
        sum = sum + i
        print(i)
print('banyaknya bilangan ganjil: ' + str(hitung))  
print('jumlah seluruh bilangan  : ' + str(sum))    
    
