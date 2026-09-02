#taş kağıt makas 
#mesala 5 tur olsun 
#skorbıard yap ( yaptığı tüm herşey (beraberlik kazanç ve yenilgi))
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print("oyuna hoş geldin")
tur=5
puan=0
arti_puan=20
liste=[]
numper=1
def taş_():
    if yapay == 2:
        print("kağit ,kaybetin ilk turu")
        liste.append(numper,"kaybetmek__")
        return "kaybetmek"
    elif yapay == 3:
        print(Fore.LIGHTGREEN_EX,"makas,teprikler kazandin")
        liste.append(numper,"kazanmak__")
        global puan
        puan+=arti_puan
        return "kazandin"
    else:
        print(numper,"taş,berabere  ")
        liste.append("berabere__")  
        return "berabere"     
def kağit():
    if yapay == 1:
        print(Fore.LIGHTGREEN_EX,"taş,kazandin")
        liste.append(numper,"kazanmak__")
        global puan
        puan+=arti_puan
        return "kazanmak"
    elif yapay ==3:
        print(Fore.LIGHTRED_EX,"makas,kaybettin")
        liste.append("kaybetmek__")
        return "kaybetmek"
    else:      
        print("kağit,berabere")
        liste.append("berabere")
        return "berabere"
def makas():
    if yapay == 2:
        print(Fore.LIGHTGREEN_EX,"kağit,kazandin")
        liste.append("kazanmak__")
        global puan
        puan+=arti_puan
        return "kazanmak"
    elif yapay ==1:
        print("taş,kaybettin")
        liste.append(numper,"kaybetmek__")
        return "kaybetmek"
    else:      
        print(Fore.LIGHTRED_EX,"makas,berabere")
        liste.append(numper,"berabere")
        return "berabere"
while tur>=0:
    try:
        seç=int(input("1.taş 2.kağit 3.makas: "))
        print("oyuna giriş yapiliyor")
        print(Fore.LIGHTMAGENTA_EX,"Loading...")
        time.sleep(0.5)
    except ValueError:
        print(Fore.LIGHTBLUE_EX,"lütfen bir sayi girin")
        continue
    yapay=random.randint(1,4)
    if seç==1:
        taş_()
        time.sleep(0.5)
    elif seç ==2:
        kağit()
        time.sleep(0.5)
    elif seç == 3:
        makas()
        time.sleep(0.5)
        numper+=1
    else:
        print(f"1-3 arasinda bir sayi giriniz lütfen {seç} değil")
        continue
    tur-=1
print(Fore.CYAN,f"puanin:{puan}")
print(Fore.LIGHTBLUE_EX,liste)

with open("oyunu_sonuçlar.txt","w",encoding="utf-8") as o:
    o.write(f"sizin oyun puaniniz:{puan}",fg="blue",bg="yello",font=("italic 13 bold"))
    o.write(f"oyun sonucu denemeleriniz:{liste}",fg="blue",bg="yello",font=("italic 13 bold"))
with open("oyunu_sonuçlar.txt","r",encoding="utf-8") as o:
    okuma=o.read()
print(okuma)

        