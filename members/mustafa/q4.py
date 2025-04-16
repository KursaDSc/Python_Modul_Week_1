sayi = int(input("Bir sayı giriniz: "))
while sayi < 0:
    print("Pozitif bir sayı giriniz.")
    sayi = int(input("Bir sayı giriniz: "))

if sayi % 2 == 1:
    print("Girdiğiniz sayı tek sayıdır.")
else:
    print("Girdiğiniz sayı çift sayıdır.")


