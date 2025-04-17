grades = {"Math":[],
          "Physics":[],
          "Chemistry":[], 
          "English":[]}

def get_input(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Lütfen geçerli bir sayısal deger giriniz!")

def get_allgrades():

    for lesson, points in grades.items():
        mes_midterm = (f"{lesson} dersi vize puanınızı giriniz: ")
        mes_final = (f"{lesson} dersi final puanınızı giriniz: ")
        points.append(get_input(mes_midterm))
        points.append(get_input(mes_final)) 

get_allgrades()
print("Ders\t\tVize\tFinal\tOrtalama\tBaşarı Durumu")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

for lesson, points in grades.items():
    av = 0.4 * points[0] + 0.6 * points[1] 
    print(f"{lesson:<10}\t {points[0]} \t{points[1]}\t{av:.2f}\t\t{'Başarısız' if av<50 else 'Başarılı'}")