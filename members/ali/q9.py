# Kullanıcıdan bir kelime girişi alan ve 
    # bu kelimenin bir palindrom olup olmadığını(geriye doğru okunduğunda da aynı) 
    # kontrol eden bir döngü ve 
    # koşullu ifade kombinasyonu nasıl oluşturulur?

while True:
    kelime=input("Lutfen bir kelime giriniz ya da cikmak icin q basiniz:")
    if kelime =="q":
        print("cikis yaptiniz...")
        break
    if kelime==kelime[::-1]:
        print("Bu kelime palindromdur.")
    else:
        print("Bu kelime palindrom degildir.")
        print("Tekrar deneyin...")