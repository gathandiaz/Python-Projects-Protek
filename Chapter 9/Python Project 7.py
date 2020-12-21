mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*76,'\nNIM\t\tNAMA MAHASISWA\t\tTGL LAHIR\t\tTEMPAT LAHIR\n','-'*75)
p = 0
for q in mhs:
    split = q.split(":")
    print(split[0],end="")
    r = len(split[1])
    print(split[1].rjust(12+r),end="")
    s = split[2]
    t = s.replace("-","/")
    print(t.rjust(34-r),end='')
    r = len(split[3])
    print(split[3].rjust(15+r))
print('-'*76)
