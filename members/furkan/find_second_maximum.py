if __name__ == '__main__':
    tablo=[]
    tablo2=[]
    n = int(input())
    arr = map(int, input().split())
    tablo=[]
    tablo2=[]
    tablo = [arr]
    tabset = set(arr)
    tablo2 = list(tabset)
    en=max(tablo2)
    tablo2.remove(en)
    en2=max(tablo2)
    print(en2)








#Buda benim VS Code üzerinde yazdığım hali:
tablo=[]
tablo2=[]
a1=int(input("Yarismaci 1'in scorunu giriniz: "))
a2=int(input("Yarismaci 2'in scorunu giriniz: "))
a3=int(input("Yarismaci 3'in scorunu giriniz: "))
a4=int(input("Yarismaci 4'in scorunu giriniz: "))
a5=int(input("Yarismaci 5'in scorunu giriniz: "))
tablo = [a1,a2,a3,a4,a5]
tabset = set(tablo)
tablo2 = list(tabset)
en=max(tablo2)
tablo2.remove(en)
en2=max(tablo2)
print("Runner up scoru: ",en2)
