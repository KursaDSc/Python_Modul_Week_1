ara1=int(input("İlk arasınav notunu giriniz: "))
ara2=int(input("İkinci arasınav notunu giriniz: "))
ara3=int(input("Üçüncü arasınav notunu giriniz: "))
final=int(input("Final notunu giriniz: "))
ort=(ara1+ara2+ara3)/3
notu = ort+final/2
ort40= ort/100 *40
final60 = final/100 *60
ortalama = ort40 + final60
if ortalama < 50:
    print("BASARISIZ")
elif ortalama >= 50:
    print("BASARILI")
