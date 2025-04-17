numara= int(input("Bir tam sayı girin: "))
fakt=1
if numara >= 0:
    for w in range(1, numara+1):
        fakt*=w
    print(f"{numara} sayısının faktöriyeli:", fakt)
