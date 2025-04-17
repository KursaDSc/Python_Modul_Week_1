#Palindrom kontrolü
#Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir
word = input("Bir kelime girin: ")

if word == word[::-1]:
    print("Bu bir palindrom.")
else:
    print("Bu bir palindrom değil.")
