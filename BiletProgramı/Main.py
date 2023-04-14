"""
-Kullanıcıya sinema ya da tiyatro tercihi sorulsun.
-Sinema izlemek için 15 Tl, tiyatro için 10 Tl ödenmesi gerekir.
-Öğrencilere %50 indirim yapılsın öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdırsın.
"""
secim1 = int(input("Sinema bileti için 1, tiyatro bileti için 2 sayısını giriniz"))
secim2 = int(input("Öğrenciyseniz 1, değilseniz 2 sayısını giriniz"))

if secim2 == 1:
    if secim1 == 1:
        print("Sinema biletinizin ücreti= ", 15 - 15 / 2)
    elif secim1 == 2:
        print("Tiyatro biletinizin ücreti= ", 10 - 10 / 2)
    else:
        print("Bilet seçiminiz yanlıştır")
elif secim2 == 2:
    if secim1 == 1:
        print("Sinema biletinizin ücreti= ", 15)
    elif secim1 == 2:
        print("Tiyatro biletinizin ücreti= ", 10)
    else:
        print("Bilet seçiminiz yanlıştır")
else:
    print("Öğrenci bilgi seçiminiz yanlıştır")