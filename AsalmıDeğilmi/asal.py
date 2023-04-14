# girilen sayının asal olup olmadığını bulma

num = int(input("Herhangi bir sayı giriniz: "))
x = 0
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Girdiğiniz sayı asal değildir")
            x = 1
        if x == 1:
            break
    if x != 1:
        print("Girdiğiniz sayı asaldır")
else:
    print("Birden büyük sayı giriniz")


