class Geometri:
    def __init__(self, kenar1, kenar2, yukseklik):
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.yukseklik = yukseklik

    def kare(self):
        print("Karenin alanı= ", self.kenar1*self.kenar1)

    def dikdortgen(self):
        print("Dikdörtgenin alanı= ", self.kenar1*self.kenar2)

    def paralelkenar(self):
        print("paralelkenarın alanı= ", self.kenar1*self.yukseklik)


