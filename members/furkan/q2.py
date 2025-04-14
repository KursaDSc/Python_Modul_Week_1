a=[]
giris=int(input("Bir tam sayı girin: "))
for i in range(1, giris+1):
    if i % 2 == 0:
        a.append(i)
print(a)
