num = int(input("Bir sayı giriniz  :"))
result = 1
for x in range(1, num + 1): 
    result *= x

print(f"{num} faktöryel : {result} ") 