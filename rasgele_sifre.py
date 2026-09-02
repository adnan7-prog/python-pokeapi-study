# Rastgele Şifre Oluşturucu
import random
import string
print("-"*20,"merhaba şifre olusturmaya","-"*20)
harf=["k","b","h"]
class SayilariAl:
    def __init__(self) -> None:
        self.sifre=""
    def sayiyi_olustur(self):
        while True:
            try:
                uznluk=int(input("uzunluk: "))
                if uznluk >= 20 or uznluk <= 0:
                    print("Hata : 20 ile 0 arasinda sayi giriniz\n")
                    continue
            except:
                print("bir hata olustu lutfen sayi giriniz\n")
                continue
            break
        while True:       
            try:
                kucuk_buyuk=input("kucuk (k), buyuk (b), hepsi (h): ").strip().lower()
                if len(kucuk_buyuk) > 1 :
                    print("Hata: sadece bir harf giriniz  \n")
                    continue
                if kucuk_buyuk.isdigit() :
                    print("Hata: sadece harf giriniz")
                    continue
                if kucuk_buyuk not in harf:
                    print("lutfen ya (k) , (b) , (h) harflerini seciniz")
                    continue
            except :
                print("bir hata olustu lutfen  harf  giriniz\n")
                continue
            break

        karakterler=""
        if kucuk_buyuk == "b":
            karakterler=string.ascii_uppercase
        elif kucuk_buyuk == "k" :
            karakterler=string.ascii_lowercase
        else:
            karakterler=string.ascii_letters
        karakterler+=string.digits
        sifre="".join(random.choice(karakterler) for i in range(uznluk))
        print("SİFRE TAMAMLANDİ .")
        self.sifre=sifre
    def yazdir(self):
        if not self.sifre:
            print("daha secim yapmadiniz\n")
        else:
            print("\n",self.sifre,"\n")
class Giris:
    def __init__(self) -> None:
        self.usteki=SayilariAl()
    def secimler(self):
        while True:
            print("-1. sayi olustur-")
            print("-2. sayiyi yazdir-")
            print("-3. cikis-")
            while True:
                try :
                    sayi=int(input("sayi gir: ").strip())
                    break
                except:
                    print("bir hata olustu lutfen rakam giriniz!\n")
                    continue
            if sayi == 1 :self.usteki.sayiyi_olustur()
            elif sayi == 2 :self.usteki.yazdir()
            elif sayi == 3 :break
            else:
                print("1-3 arasinda bir sayi giriniz")
                
if __name__ == "__main__":
    app=Giris()
    app.secimler()
                    
