limit = int(input("Kaça kadar Fibonacci dizisi oluşturulsun? "))
fibonacci = [0, 1]

while True:
    next_num = fibonacci[-1] + fibonacci[-2]
    if next_num > limit:
        break
    fibonacci.append(next_num)

print("Fibonacci dizisi:", fibonacci)

#bunu cok iyi anlamadim
