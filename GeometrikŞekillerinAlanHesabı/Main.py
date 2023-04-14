# İstenilen geometrik cismin kenar veya yüksekliklerini girerek alanını hesaplayan program
# Nesne oluşturularak yapıldı.

from Sınıf import Geometri
print(" Kare alanı hesaplamak için 1 \n Dikdörtgen alanı hesaplamak için 2 \n Paralelkenar alanını hesaplamak için 3")
secim = int(input("Seçiminizi giriniz= "))

k1 = 0
k2 = 0
y = 0


if secim == 1:
    k1 = int(input("Karenin bir kenarını giriniz= "))
    nesne = Geometri(k1, k2, y)
    nesne.kare()
elif secim == 2:
    k1 = int(input("Dikdörtgenin bir kenarını giriniz= "))
    k2 = int(input("Dikdörtgenin diğer bir kenarını giriniz= "))
    nesne = Geometri(k1, k2, y)
    nesne.dikdortgen()
elif secim == 3:
    k1 = int(input("Paralelkenarın kenarını giriniz= "))
    y = int(input("Paralelkenarın yüksekliğini giriniz= "))
    nesne = Geometri(k1, k2, y)
    nesne.paralelkenar()
