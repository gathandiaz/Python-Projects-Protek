nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*70,'\nNIM\tNAMA\t\tN.MID\tN.UAS\t\tN.AKHIR\t\tSTATUS\n','-'*69)
p = 0
for q in nilai:
    print(nilai[p]['nim'],end="")
    r = len(nilai[p]['nama'])
    print(nilai[p]['nama'].rjust(3+r),end="")
    s = str(nilai[p]['mid'])
    print(s.rjust(22-r),end="")
    s = str(nilai[p]['uas'])
    print(s.rjust(8),end="")
    NA = round((nilai[p]['mid'] + 2*nilai[p]['uas'])/3)
    s = str(NA)
    print(s.rjust(16),end="")
    if (NA >= 60):
        print("lulus".rjust(17))
    p += 1
print("-"*70)
