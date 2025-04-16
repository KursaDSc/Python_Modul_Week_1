kelime = input("Bir Kelime Giriniz: ")
kelime = kelime.lower()
yeni_kelime = kelime[::-1]

if kelime == yeni_kelime:
    print("Palindrom!!!")
else:
    print("Palindrom Değil.")