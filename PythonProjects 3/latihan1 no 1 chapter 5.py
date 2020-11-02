bi  = int(input("nilai Bahasa Indonesia = "))
ipa = int(input("nilai Ipa              = "))
mtk = int(input("nilai Matematika       = "))


if((bi>=60)and(bi<=100)and(ipa>=70)and(ipa<=100)and(mtk>=60)and(mtk<=100)):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")
