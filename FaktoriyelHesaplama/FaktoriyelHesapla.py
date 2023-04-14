"""
Girilen sayının faktoriyelini bulan program.
"""
sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
faktoriyel = 1
for i in range(sayi):
    faktoriyel = faktoriyel * (i + 1)

print("Girdiğiniz sayının faktoriyeli: ", faktoriyel)