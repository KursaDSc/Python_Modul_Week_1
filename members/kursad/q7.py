limit_value = int(input("Fibonacci dizisi ust limiti  :"))
ls_fibonacci = [0, 1]

while True :
    new_value = ls_fibonacci[-2] + ls_fibonacci[-1] 
    if new_value <= limit_value:
            ls_fibonacci.append(new_value)
    else:
          break
print(ls_fibonacci)