bil = [3,4,1,6,9]
def kuadrat(bil):
    bilnya = []
    for hasil in bil:
        bilnya.append(hasil ** 2)
    print(bilnya)
print('bil               = ', bil)
print('hasil kuadrat bil = ',end='')
kuadrat(bil)
