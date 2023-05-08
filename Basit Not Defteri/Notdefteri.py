import keyboard
from sınıf import Dosya
dosya = Dosya()  # dosya isminde nesne oluşturuldu
while True:
    print("\ndosya oluşturmak için '1'\ndosya açmak için '2'\nSadece dosyaya ekleme yapmak için '3'"
          "\nuygulamadan çıkmak istiyorsanız '4' rakamını giriniz")

    secim = int(input("Seçiminiz olan rakamı giriniz = "))

    if secim == 1:
        dosya_adi = input("Oluşturmak istediğiniz dosya adını giriniz(türüyle birlikte örnek:Metin.txt)= ")
        dosya.dosya_olustur(dosya_adi)
    elif secim == 2:
        dosya_adi = input("Açmak istediğiniz dosya adını giriniz(türüyle birlikte örnek:Metin.txt)= ")
        dosya.dosya_acma(dosya_adi)
    elif secim == 3:
        dosya_adi = input("Üzerine eklemek istediğiniz dosya adını giriniz(türüyle birlikte örnek:Metin.txt)= ")
        dosya.dosya_yazma(dosya_adi)
    elif secim == 4:
        if keyboard.read_key() == "4":
            exit()
            break

