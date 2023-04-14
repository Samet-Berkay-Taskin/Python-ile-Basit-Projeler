def kare(kenar):
    return kenar * kenar


def dikdortgen(kenar1, kenar2):
    return kenar1 * kenar2


def paralelkenar(kenar, yukseklik):
    return kenar * yukseklik


file = open("Alanlar.txt", "a", encoding="utf-8")

print(" Kare alanı hesaplamak için 1 \n Dikdörtgen alanı hesaplamak için 2 \n Paralelkenar alanını hesaplamak için 3")
secim = int(input("Seçiminizi giriniz= "))

k1 = 0
k2 = 0
y = 0

if secim == 1:
    k1 = int(input("Karenin bir kenarını giriniz= "))
    alan = kare(k1)
    file.write("Karenin Alanı " + str(alan) + "\n")  # write içerisinde int yazılmadığı için int değeri stringe çevrildi

elif secim == 2:
    k1 = int(input("Dikdörtgenin bir kenarını giriniz= "))
    k2 = int(input("Dikdörtgenin diğer bir kenarını giriniz= "))
    alan = dikdortgen(k1, k2)
    file.write("Dikdörtgenin Alanı " + str(alan) + "\n")
elif secim == 3:
    k1 = int(input("Paralelkenarın kenarını giriniz= "))
    y = int(input("Paralelkenarın yüksekliğini giriniz= "))
    alan = paralelkenar(k1, y)
    file.write("ParalelKenarın Alanı "+str(alan) + "\n")
