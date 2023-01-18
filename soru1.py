''' kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini de bu toplamdan çıkaran ve
geri döndüren fonksiyonu yazınız klavyeden '''

list=[]
a=0
while (a<5):
    sayi = eval(input("sayı giriniz"))
    list.append(sayi)
    a += 1
    print(a)

ters = 0
listem=[]
for x in list:
  while(x> 0):
    gecici = x %10
    ters = (ters *10) + gecici
    x = x //10
    listem.append((ters))

print(list)
print(listem)
toplam=0
for a in listem:
    for b in list:
        if a==b:
            toplam+=a
print(toplam)














