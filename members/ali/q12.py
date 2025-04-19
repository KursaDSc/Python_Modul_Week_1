for i in range(1, 5):  # 4 ders için
    print(f"{i}. Ders")
    vize = float(input("Vize notunu giriniz: "))
    final = float(input("Final notunu giriniz: "))

    ortalama = (vize * 0.4) + (final * 0.6)
    print("Ortalama:", ortalama)  #buraya round(ortalama, 2) kullanabilirz.

    if ortalama >= 50:
        print("SUCCESSFUL (BAŞARILI)")
    else:
        print("FAILED (BAŞARISIZ)")
    
    print("=" * 50)  # Ayraç çizgisi