sayi = int(input("Bir sayı giriniz: "))
f =1
while sayi < 0:
    print("Pozitif bir sayı giriniz.")
    sayi = int(input("Bir sayı giriniz: "))
for i in range(1, sayi+1):
    f *= i
print(f)


