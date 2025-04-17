# Fibonacci dizisini hesaplayan ve 
  # sonucu belirli bir sınıra kadar sayı içeren 
    # bir liste olarak döndüren bir döngü nasıl oluşturulur?

# Fibonacci dizisi, her sayının kendisinden önceki iki sayının toplamı olduğu bir dizidir.
limit=100
fibonacci=[0,1]

while fibonacci[-1]+fibonacci[-2]<=limit:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)
