# input jumlah
mhsLaki = int(input("jumlah mhs laki laki ="))
mhsPerempuan = int(input("jumlah mhs perempuan ="))

outputLaki = int(mhsLaki//10)
outputPerempuan = int(mhsPerempuan//10)

#diagram
print("Diagram batang horizontal jumlah Mahasiswa PTIK dalam satu bintangnya(*) mewakili 10 orang =")
print("Mahasiswa Laki-laki =", outputLaki*"*")
print("Mahasiswa Perempuan =", outputPerempuan*"*")
