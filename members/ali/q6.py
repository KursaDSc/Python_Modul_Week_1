#Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazın.
#Asal sayılar 1 ve kendisi dışında hiçbir pozitif tam böleni olmayan sayılardır.

sayi=int(input("Bir sayı girin: "))
asal=True
for i in range(2,sayi):
    if sayi%i==0:
        asal=False
        break
if asal:
    print(sayi,"asal bir sayıdır.")    
else:
    print(sayi,"asal bir sayı değildir.")    
    
    