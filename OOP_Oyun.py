import random,sys,time

def noktaEkle():
    print(".")
    time.sleep(.3)
    print("..")
    time.sleep(.3)
    print("...")
def hataliGiris():
    print("Hatalı tuş.")

class Oyuncu:
    def __init__(self,isim,power,can=100,puan=0):
        self.isim=isim
        self.power=power
        self.can=can
        self.puan=puan
    def bilgileriGoster(self):
        print("""
        İsim={}
        Gücü={}
        Can={}
        Puan={}
        """.format(self.isim,self.power,self.can,self.puan))

    def savun_saldir(self):#Savunma ya saldırı olduğunda 1 gelirse kazanır 2 gelirse kaybeder diye rastgele belirliyoruz
        return random.randint(1,2)

    def savun(self,dusman):
       r= self.savun_saldir()
       # Savunmada başarılı olursak düşmanın canı bizim gücümüz kadar azalır.
       # Puanımız 10 artar,düşmanın gücü 10 azalır,düşmanın puanı 5 azalır
       if(r==1) :
        print("Savunma başladı")
        noktaEkle()
        print("Savunma başarılı")
        dusman.can-=self.power
        self.puan+=10
        dusman.puan-=5
        dusman.power-=10
        self.bilgileriGoster()
        dusman.bilgileriGoster()
       else:
           # Savunmada başarısız olursak bzim canımız düşmanın gücü kadar azalır.
           # Düşmanın puanı 10 artar,bizim puanımız 5 azalır.Düşmanın gücü 10 azaldı
           print("Savunma başladı")
           noktaEkle()
           print("Savunma başarısız")
           self.can -= dusman.power
           dusman.puan += 10
           self.puan -= 5
           dusman.power-=10
           self.bilgileriGoster()
           dusman.bilgileriGoster()

    def saldir(self,dusman):
       r=self.savun_saldir()
    #Biz Saldırıya geçiyoruz başarılı olursak puanımız 10 artıyor gücümüz 10 azalır
    #Düşmanın ise bizim gücümüz kadar canı azalır,düşmanın 5 puanı azalır
       if (r == 1):
           print("Saldırı başladı")
           noktaEkle()
           print("Saldırı başarılı")
           dusman.can -= self.power
           self.puan += 10
           dusman.puan -= 5
           self.power-=10
           self.bilgileriGoster()
           dusman.bilgileriGoster()
     # Biz Saldırıya geçiyoruz başarısız  olursak puanımız 5 azalıyor gücümüz 10 azalır
     # Canımız ise düşmanın gücü kadar azalır.
       else:
           print("Saldırı başladı")
           noktaEkle()
           print("Saldırı başarısız")
           self.can -= dusman.power
           dusman.puan += 10
           self.puan -= 5
           self.power-=10
           self.bilgileriGoster()
           dusman.bilgileriGoster()
    def exit(self):
        print("===Çıkış Yapılıyor===")
        noktaEkle()
        sys.exit()

#Güçlerini random olarak atadık.
name=input("İsminiz :")
dusman_ismi=input("Düşmanın ismi ne olsun:")
O = Oyuncu(name,random.randint(1,100))
O1 = Oyuncu(dusman_ismi,random.randint(1,100))
O.bilgileriGoster()
O1.bilgileriGoster()

while True:
   sec=input("""
        Hangi işlemi yapmak istiyorsunuz?
        1-Savunma
        2-Saldır
        3-Çıkış
        Hamle Seçimi
        """)
   if sec == "1":
       O.savun(O1)
   elif (sec == "2"):
       O.saldir(O1)
   elif (sec == "3"):
       O.exit()
   else:
       hataliGiris()
   if(O.puan==100 or O.can<=0 or O.power<=0):
     print(O1.isim,"KAZANDI")
     break
   if (O1.puan == 100 or O1.can < 0 or O1.power<=0):
     print(O.isim, "KAZANDI")
     break















