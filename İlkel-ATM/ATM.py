class Atm:
    def __init__(self, bakiye, istenilenpara, borc):
        self.bakiye = bakiye
        self.istenilenpara = istenilenpara
        self.borc = borc

    def para_cekme(self):
        if self.bakiye < self.istenilenpara:
            print("\n\nYetersiz bakiye")
            return self.bakiye
        else:
            self.bakiye = self.bakiye - self.istenilenpara
            print("\n\nİŞLEMİNİZ BAŞARIYLA GERÇEKLEŞTİ")
            return self.bakiye

    def para_yatirma(self):
        self.bakiye = self.bakiye + self.istenilenpara
        print("\n\nİŞLEMİNİZ BAŞARIYLA GERÇEKLEŞTİ")
        return self.bakiye

    def bakiye_sorgu(self):
        print("\n\n Bakiye durumunuz", self.bakiye)

    def borc_odeme(self):
        if (self.istenilenpara > self.borc or self.istenilenpara > self.bakiye) or self.borc == 0:
            print("\n\nBakiyeniz yetersiz veya ödenecek tutar bilgisi yalnış")
        else:
            self.borc = self.borc - self.istenilenpara
            self.bakiye = self.bakiye - self.istenilenpara
            print("\n\nİŞLEMİNİZ BAŞARIYLA GERÇEKLEŞTİ")
        return self.bakiye, self.borc



    def borc_sorgu(self):
        if self.borc > 0:
            print("\n\nborcunuzun tutarı= ", self.borc)
        else:
            print("\n\nborcunuz bulunmamaktadır")