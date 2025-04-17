#Kullanıcıdan başlangıç ​​ve bitiş değerini alıp, 
# bu değerler arasındaki tüm sayıları (bitiş değeri dahil) ekrana yazdıran bir Python kodu yazınız.

# kullanıcıdan başlangıç ve bitiş değerlerini al:
balangic=int(input("Baslangic degeri giriniz:"))
bitis=int(input("Bitis degeri giriniz:"))
for i in range (balangic, bitis+1):
    print(i)