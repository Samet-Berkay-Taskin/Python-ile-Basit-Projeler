class Dosya:
    def dosya_olustur(self, dosya_adi):
        file = open(dosya_adi, "a", encoding="utf-8")
        secim = int(input("Üzerine yazmak istiyorsanız '1' giriniz"))
        if secim == 1:
            yazılacak = input("Yazmak istediğinizi yazın")
            file.write("\n" + yazılacak)
            print("Yazma işlemi gerçekleşti")
        file.close()

    def dosya_acma(self, dosya_adi):
        try:
            with open(dosya_adi, "r", encoding="utf-8") as file:
                satirlar = len(file.readlines())  # kaç satır varsa bu sayıyı satirlara kaydetti
                file.seek(0)  # 14.satırda readlines kullanıldığından imleç satırın sonuna geldi o yüzden sıfırlamak gerek
                liste = file.readlines()  # sıfırlanmasaydı burada liste boş olurdu
                for i in range(satirlar):
                    print(liste[i], end="")
        except FileNotFoundError:
            print("Dosya bulunamadığı için açılamadı.")

    def dosya_yazma(self, dosya_adi):
        file = open(dosya_adi, "a", encoding="utf-8")
        yazılacak = input("Yazmak istediğinizi yazın")
        file.write("\n" + yazılacak)
        print("Yazma işlemi tamamlandı ve ", dosya_adi, " isimli dosya kaydedildi")
        file.close()
