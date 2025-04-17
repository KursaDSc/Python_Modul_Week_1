#Kullanıcıdan pozitif bir tam sayı girişi alan ve faktöriyelini hesaplayan bir Python programı yazın. 
 # Faktöriyel, bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır. 
   # Örneğin: kullanıcı 5 girdiyse, program aşağıdaki çıktıyı vermelidir: Kullanıcıdan bir sayı girin: 5 Faktöriyel: 120

# Kullanıcıdan pozitif bir tam sayı girişi al
sayi=int(input("Pozitif bir tam sayı girin: "))
faktoriyel=1
# Faktöriyel hesaplama
for i in range (1,sayi+1):
    faktoriyel*=i
# Sonucu yazdır
print("Faktöriyel: ", faktoriyel)