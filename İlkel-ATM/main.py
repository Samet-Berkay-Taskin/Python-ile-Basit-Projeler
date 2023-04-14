from ATM import Atm

borc = 245
bakiye = 4000
cekim = 0

print(" Para çekmek istiyorsanız 1 giriniz\n Para yatırmak istiyorsanız 2 giriniz\n "
      "Kredi kartı borcunuzu ödemek istiyorsanız 3 giriniz\n Bakiyenizi sorgulamak için 4 giriniz\n "
      "Borcunuzu sorgulamak için 5 giriniz")

secim = int(input("Seçiminizi giriniz"))

if secim == 1:
    cekim = int(input("Çekmek istediğiniz tutarı giriniz= "))
    islem = Atm(bakiye, cekim, borc)
    bakiye = islem.para_cekme()  # Returnu tekrar değişkene döndürüyor

elif secim == 2:
    cekim = int(input("Yatırmak istediğiniz tutarı giriniz= "))
    islem = Atm(bakiye, cekim, borc)
    bakiye = islem.para_yatirma()

elif secim == 3:
    cekim = int(input("Ödemek istediğiniz tutarı giriniz= "))
    islem = Atm(bakiye, cekim, borc)
    bakiye, borc = islem.borc_odeme()  # return hangi sıraylaysa o sırayla atanmalı değişken

elif secim == 4:
    cekim = 0
    islem = Atm(bakiye, cekim, borc)
    islem.bakiye_sorgu()

elif secim == 5:
    cekim = 0
    islem = Atm(bakiye, cekim, borc)
    islem.borc_sorgu()


if secim <= 3:
    print(" Güncel bakiyeniz= ", bakiye, "\n Güncel borcunuz= ", borc)
