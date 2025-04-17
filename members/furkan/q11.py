a=int(input("Birinci sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))
c=int(input("Üçüncü sayıyı giriniz: "))
if a > b and a > c:
    print("En büyük sayi:", a)
elif b > a and b > c:
    print("En büyük sayi:", b) 
else:
    print("En büyük sayı:", c)
