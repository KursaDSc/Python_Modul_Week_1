for i in range(1, 5):
    print(f"{i}. ders:")
    vize = float(input("Vize notunu girin: "))
    final = float(input("Final notunu girin: "))
    ortalama = (vize * 0.4) + (final * 0.6)
    if ortalama >= 50:
        print("BAŞARILI - Ortalama:", ortalama)
    else:
        print("BAŞARISIZ - Ortalama:", ortalama)
    print("-" * 20)

#hatali olabilir!!!!!
