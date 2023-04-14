import random
print("Sayı tahmini programına hoşgeldiniz.\nProgram 0 ile 25 arasında bir sayı tutup tahmin etmenizi bekliyor.")

sayi = random.randint(0, 25)
sayac = 0
secim = 0

while True:
    tahmin = int(input("Tahmininizi giriniz"))
    sayac = sayac + 1
    if tahmin == sayi:
        print(sayac, ". tahmininizde sayıyı doğru bildiniz")
        break
    else:
        print("Tahmininiz yalnış")
        secim = int(input("Yeniden tahmin oluşturmak için 1 giriniz"))
    if secim == 1:
        break