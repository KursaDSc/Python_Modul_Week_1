#Boy ve kilo bilgileri al, kilo endeksini hesapla ve sonucu degerlendir:

#kullanicidan bilgileri al:
boy=float(input("Lutfen boyunuzu m cinsinden giriniz: "))
kilo=float(input("Lutfen kilonuzu kg olarak giriniz: "))

#kilo endeksi hesapla: kilo/boy**2 (m cinsinden).

#boyu m cinsine cevirme:
vucut_kitle_indeksi=kilo/(boy**2)

#sonucu ekrana yazdirma:
print("Vucut Kitle Indeksiniz: ",vucut_kitle_indeksi)
print("Bunlarin sonucuna gore:")
if vucut_kitle_indeksi<25:
    print("Zayif!!")
elif 25 <=vucut_kitle_indeksi <30:
    print("Normal!")
elif 30<=vucut_kitle_indeksi<40:
    print("Kilolu...")   
else:
    print("Fazla kilolusunuz..")