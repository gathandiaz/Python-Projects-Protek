def starFormation1(n):
    for i in range (n):
        for j in range (i+1):
            print('*', end='')
        print()
n=4
starFormation1(n)

def starFormation2(n):
    for i in reversed (range (n)):
        for j in range (i+1):
            print('*', end='')
        print()
n=3
starFormation2(n)
