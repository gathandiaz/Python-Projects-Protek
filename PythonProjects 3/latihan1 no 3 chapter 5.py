bi  = int(input("nilai Bahasa Indonesia = "))
ipa = int(input("nilai ipa              = "))
mtk = int(input("nilai Matematika       = "))


if((bi>=60)and(bi<=100)and(mtk>=70)and(mtk<=100)and(ipa>=60)and(ipa<=100)):
    print("Status Kelulusan : LULUS")
elif((bi<0)or(bi>100)and(mtk<0)or(mtk>100)or(ipa<0)and(ipa>100)):
    print("Maaf input ada yang tidak valid")
else:
    print("Status Kelulusan : TIDAK LULUS")
    print("Sebab            :")
    print("- Nilai bahasa indonesia kurang dari 60")
    print("- Nilai matematikanya kurang dari 70")
