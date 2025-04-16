uz=int(input("Uzunlugnuzu Girin: "))
kilo=int(input("Kilonuzu Girin: "))
uz2= uz / 100
index= kilo / (uz2 * uz2)
if index < 25:
    print("Zayıf")
if index >= 25 and index < 30:
    print("Normal")
if index >= 30 and index < 40:
    print("Kilolu")
if index >= 40:
    print("Obez")
