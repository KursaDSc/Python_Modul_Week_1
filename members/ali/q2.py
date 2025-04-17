#Kullanıcıdan bir sayı girişi alın ve ekrana bu sayıya kadar çift sayıları yazdıran bir Python programı yazın. 
# Bunu önce 'for' ile sonra da 'while' döngüleriyle yapın.
        # 1-for ile:
sayi=int(input("Lutfen bir sayi giriniz:"))
for i in range (sayi):
    if i %2==0:
        print(i)
        # 2-while ile:
sayi=int(input("Lutfen bir sayi giriniz:"))
i=0
while i<=sayi:
    if i%2==0:
        print(i)
    i+=1