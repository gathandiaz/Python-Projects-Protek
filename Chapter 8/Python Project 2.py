def datastat(x):
    banyak = len(x)
    jumlah = sum(x)
    a = jumlah/banyak
    b = max(x)
    c = min(x)
    datastat = [a,b,c]
    print(datastat)

x = {0,7,4,6,8,9,1,6,4}
datastat(x)
