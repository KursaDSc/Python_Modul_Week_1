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
