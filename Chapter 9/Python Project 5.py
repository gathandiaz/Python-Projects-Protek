nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*45,'\nNIM\tNAMA\t\tN.MID\t\tN.UAS\n','-'*44)
p = 0
for q in nilai:
    print(nilai[p]['nim'],end="")
    r = len(nilai[p]['nama'])
    print(nilai[p]['nama'].rjust(3+r),end="")
    s = str(nilai[p]['mid'])
    print(s.rjust(22-r),end="")
    s = str(nilai[p]['uas'])
    print(s.rjust(16))
    p += 1
print("-"*45)
