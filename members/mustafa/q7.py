sinir = int(input("Bir sınır giriniz:"))

while sinir < 0:
    print("Pozitif bir sayı giriniz.")
    sinir = int(input("Bir sayı giriniz: "))

fibo = []
a, b = 0, 1

while a <= sinir:
    fibo.append(a)
    a, b = b, a+b

print(f"Fibonacci dizisi: {fibo}")


