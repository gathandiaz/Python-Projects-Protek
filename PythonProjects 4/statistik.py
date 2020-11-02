def sum (*x):
    y = 0
    for p in x:
        y += p
    print(y)

def average (*x):
    y = 0
    z = 0
    for p in x:
        y += p
        z += 1
    avg = y/z
    print(avg)

def maks (*x):
    y = x[0]
    for z in x:
        if (z > y):
            y = z
    print(y)

def min (*x):
    y = x[0]
    for z  in x:
        if(z < y):
            y = z
    print(y)

