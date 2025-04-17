def get_input(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Lütfen geçerli bir sayısal deger giriniz!")

total_numbers = 4
max_num = 0

for x in range(1, total_numbers):
    mes = (f"{x}. sayıyı giriniz: ")
    num = get_input(mes) 
    max_num = num if num > max_num else max_num

print(f"Girdiginiz sayılardan en büyüğü: {max_num}")