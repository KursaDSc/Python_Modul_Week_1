def get_input(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("Lütfen geçerli bir sayısal deger giriniz!")


mes_weight = ("Vücut ağırlığınızı 'kg' olarak giriniz: ")
mes_height = ("Boyunuzu 'metre' olarak giriniz: ")

weight = get_input(mes_weight)
height = get_input(mes_height)

bwi = weight/(height**2)

if bwi < 25: 
    print("Zayıfsınız...")
elif 25 <= bwi < 30: 
    print("Normalsiniz...")
elif 30 <= bwi < 40: 
    print("Fazla kilolusunuz...")
elif 40 <= bwi: 
    print("Obeziteye dikkat...")