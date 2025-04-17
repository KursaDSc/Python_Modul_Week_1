boy = float(input("Boyunuzu Giriniz(Cm): ")) /100
kilo = float(input("Kilonuzu Giriniz(Kg): "))
indeks = round(kilo/(boy**2),1)
print(indeks)
if indeks < 25:
    print("Zayıf")
elif 25 <= indeks < 30:
    print("Normal")
elif 30 <= indeks < 40:
    print("Kilolu")
else:
    print("Aşırı Kilolu")

