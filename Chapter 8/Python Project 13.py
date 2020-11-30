nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaiAkhir(x):
    tertinggi = 0
    data      = {}
    for y in x:
        UAS = y.get('uas')
        MID = y.get('mid')
        calc = (MID + 2*UAS)/3
        if(calc > tertinggi):
            tertinggi = calc
            data['nim']  = y.get('nim')
            data['nama'] = y.get('nama')
    print('='*65)
    print('Nilai tertinggi diraih oleh mahasiswa bernama',data['nama'],'dengan NIM',data['nim'])
    print('-'*65)

nilaiAkhir(nilaiMhs)
