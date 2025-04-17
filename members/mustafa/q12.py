anayasa_v = int(input("Anayasa Dersi Vize Notunu Giriniz: "))
anaysa_f = int(input("Anayasa Dersi Final Notunu Giriniz: "))
medeni_v = int(input("Medeni Hukuk Dersi Vize Notunu Giriniz: "))
medeni_f = int(input("Medeni Hukuk Dersi Final Notunu Giriniz: "))
ceza_v = int(input("Ceza Hukuku Dersi Vize Notunu Giriniz: "))
ceza_f = int(input("Ceza Hukuku Dersi Final Notunu Giriniz: "))
borclar_v = int(input("Borclar Dersi Vize Notunu Giriniz: "))
borclar_f = int(input("Borclar Dersi Final Notunu Giriniz: "))

if (
    (anayasa_v*40/100 + anaysa_f*60/100) >= 50 and 
    (medeni_v*40/100 + medeni_f*60/100) >= 50 and 
    (ceza_v*40/100 + ceza_f*60/100) >= 50 and 
    (borclar_v*40/100 + borclar_f*60/100) >= 50
):
    print("GEÇTİNİZ")
else:
    print("KALDINIZ")

                