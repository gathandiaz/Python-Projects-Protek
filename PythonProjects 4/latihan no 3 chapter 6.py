def faktorial(n):
    hasil = 1
    for i in range (2, n+1):
        hasil *= i
    return hasil

def kombinasi (x,y):
    hasil = faktorial(x)//(faktorial(x-y)*faktorial(y))
    print('a. C(',x,',',y,')=',hasil)
def permutasi (x,y):
    hasil = faktorial(x)//(faktorial(x-y))
    print('b. P(',x,',',y,')=',hasil)

kombinasi(5,3)
permutasi(10,7)
