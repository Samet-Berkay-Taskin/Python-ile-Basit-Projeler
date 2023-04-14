"""
1'den kullanıcının girdiği sayıya kadar olan tek ve çift sayıların toplamını
ayrı ayrı bulan ve sonucu ekrana gösteren program
"""
num = int(input("Sayıyı giriniz"))
cift = 0
tek = 0

for i in range(2, num, 2):
    cift = cift + i
for j in range(1, num, 2):
    tek = tek + j

if num % 2 == 0:
    cift = cift + num
else:
    tek = tek + num
print("Çift sayıların toplamı ", cift)
print("Tek sayıların toplamı ", tek)