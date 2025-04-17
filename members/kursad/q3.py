num1 = int(input("Bir sınır değer giriniz  :"))
num2 = int(input("Diğer sınır değeri giriniz :"))

minn = min(num1,num2)
maxn = max(num1,num2)

for x in range(minn, maxn+1) :
    print(x, end=" ")