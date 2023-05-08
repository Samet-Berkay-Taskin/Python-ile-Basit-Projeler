"""
 Bir metin dosyasındaki belirli bir kelimeyi arayarak bulunduğu satır ve satırdaki kaçıncı kelime olduğunu belirten
"""

with open("Metin.txt", "w", encoding="utf-8") as file:
    file.write("bu birinci satırdaki metin\nBu ikinci satır\nBuda üç olsun")

with open("Metin.txt", "r", encoding="utf-8") as file:
    satirlar = file.readlines()
    aranacak = input("Aramak istediğin kelimeyi giriniz")
    # 'enumerate' fonksiyonu, satırların numarasını 'satir_no' değişkenine, içeriğini ise 'satir' değişkenine atar.
    for satir_no, satir in enumerate(satirlar, 1):
        if aranacak in satir:
            kelimeler = satir.split()
            sütun_no = kelimeler.index(aranacak) + 1
            print(aranacak, "kelimesi", satir_no, ". satırdaki", sütun_no, ". kelimedir")


# NOT: metindeki kelimeyi verdiğinizde satırı ve kelimeyi buluyor fakat bir hata veriyor bu hata 6. satırda metine yazdıklarımızı \n ile ayırdığımız için veriyor şimdilik önemsiz