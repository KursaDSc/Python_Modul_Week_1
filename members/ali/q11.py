# Kullanıcının girdiği üç sayıdan en büyüğünü bulan bir Python programı yazalim..

# Kullanıcıdan üç sayı alalım
sayi1 = float(input("Lutfen birinci sayıyı giriniz: "))
sayi2 = float(input("Lutfen ikinci sayıyı giriniz: "))
sayi3 = float(input("Lutfen üçüncü sayıyı giriniz: "))

# En büyük sayıyı bulalım
if sayi1 >= sayi2 and sayi1 >= sayi3:
    enBuyuk = sayi1
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

print("En büyük sayı: ", enBuyuk)        

#2. metod:
# Kullanıcıdan üç sayı aldik varsyalim;
# sayi1, sayi2, sayi3
# En büyük sayıyı bulmak için max() fonksiyonunu kullanabiliriz:
# max(sayi1, sayi2, sayi3) şeklinde yazabiliriz.
print("En büyük sayı: ", max(sayi1, sayi2, sayi3))
