#Kullanıcıdan sayı al ve o sayıya kadar çift sayıları yazdır
num = int(input("Bir sayı girin: "))
for i in range(2, num + 1, 2):
    print(i)
