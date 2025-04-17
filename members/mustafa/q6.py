sayi = int(input("Bir sayı giriniz: "))
asal = True

if 0< sayi < 2:
    print("Girdiğiniz sayı asal değildir.")

for i in range(2,sayi):
    if sayi % i == 0:
        asal = False
        break

if asal:
    print("Sayı Asaldır")
else:
    print("Sayı Asal Değildir.")
   