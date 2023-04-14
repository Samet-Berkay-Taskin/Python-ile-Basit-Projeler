"""
2 tane zar atılsın ve her iki zarın değeri de 6 olduğunda program dursun.
iki zar da 6 gelene kadar kaç kez zar atıldığını göstersin.
"""

import random

i = 1
while True:
    deger1 = random.randint(1, 6)
    deger2 = random.randint(1,6)
    print(i, "Birinci zar ", deger1, "İkinci zar ", deger2)
    if (deger1 == 6 and deger2 == 6):
        print(i, " defa zar atıldı ve en sonda zarlar düşeş geldi")
        break
    i = i + 1