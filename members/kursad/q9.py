text = input("Bir kelime giriniz: ")

ind = range(len(text) // 2)
result = True

for x in ind:
    if text[x] != text[-1-x]:
        result = False
        break

if result:
    print(f"'{text}' kelimesi bir palindromdur")
else:
    print(f"'{text}' kelimesi bir palindrom degildir.")