for x in range(1,11):
    print(x, end=" ")

class Araba:
    def __init__(self, max_hiz, yakit_turu):
        self.max_hiz = max_hiz
        self.yakit_turu = yakit_turu
        print(f"Yeni bir araba oluşturuldu! 🚗")
        print(f"Maksimum Hız: {self.max_hiz} km/s")
        print(f"Yakıt Türü: {self.yakit_turu}")
        print("-----------------------------")

# Örnek kullanım:
araba1 = Araba(220, "Benzin")
araba2 = Araba(180, "Dizel")
araba3 = Araba(250, "Elektrik")