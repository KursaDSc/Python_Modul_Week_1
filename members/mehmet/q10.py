weight = float(input("Kilonuzu girin (kg): "))
height = float(input("Boyunuzu girin (metre): "))

VKI = weight / (height ** 2)
#agirlik bolu uzunlugun karesi

print("Vücut Kitle İndeksi:", round(VKI, 2))

if VKI < 25:
    print("Zayıf")
elif 25 <= VKI < 30:
    print("Normal")
elif 30 <= VKI <= 40:
    print("Kilolu")
else:
    print("Obez")



#Kişinin kilo endeksini hesaplayan ve endeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonucu döndüren kodu yazınız. 
#(Ağırlık endeksi hesaplamasını internetten araştırabilirsiniz) Bunun için kullanıcıdan kilo ve boy ölçümlerini isteyin. 
#Kilo endeksiniz 25'in altındaysa zayıf, 25-30 arasıysa normal, 30-40'ın üzerindeyse kilolusunuz. 
#40 yaşın üzerindeyseniz kilolusunuz demektir.
