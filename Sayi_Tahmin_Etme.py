



#Düz sayı tahmin oyunu
'''
import random
r=random.randint(1,101)
while True:
    num = int(input("1-100 arası sayı tahmininde bulunun:"))
    if num<r:
        print("Daha büyük bir sayı girin")
    elif r<num:
        print("Daha küçük bir sayı girin")
    elif r==num:
        print("Tebriklerrr")
        break'''

#Puanlı sayı tahmin oyunu
'''import random
r=random.randint(1,101)
puan=100
print(r)
while True:
    num = int(input("1-100 arası sayı tahmininde bulunun:"))
    if num<r:
        print("Daha büyük bir sayı girin")
        puan-=10
    elif r<num:
        print("Daha küçük bir sayı girin")
        puan-=10
    elif r==num:
        print("Tebriklerrr..")
        print("{} puan kazandınız".format(puan))
        break '''

#Canlı sayı tahmin oyunu
import random
r=random.randint(1,101)
can=3
print(r)
while True:
    num = int(input("1-100 arası sayı tahmininde bulunun:"))
    if num<r:
        print("Daha büyük bir sayı girin")
        can-=1
        if can == 0:
            print("Kaybettiniz..")
            break
        print("Kalan canınız:",can)
    elif r<num:
        print("Daha küçük bir sayı girin")
        can -= 1
        print("Kalan canınız:", can)
        if can == 0:
            print("Kaybettiniz..")
            break

    elif r==num:
        print("Tebriklerrr..")
        break
