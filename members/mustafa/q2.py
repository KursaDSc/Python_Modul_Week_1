#for döngüsü ile
sayi = int(input("Bir sayı Giriniz: "))
for i in range(0,sayi+1):
    if i % 2 == 0:
        print(i)

#while döngüsü ile
sayi = int(input("Bir sayı Giriniz: "))
i = 0
while i <= sayi:
    if i % 2 == 0:    
        print(i)
    i += 1  
     
