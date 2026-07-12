print("hello im adnan" )
x=10
z="python"
print(x)
print(z)
print(type(x))
print(type(z))
#ilk denemem 
_KupunToplamHacmi=70
kupun_toplam_hacmi=70
print(_KupunToplamHacmi)
print(kupun_toplam_hacmi)

c,b,n="banana","portakal","bluebery"
print(c)
print(b)
print(n)

print("hello world")
x=7
y="python"
c=str(7)
y=int(7)
m=float(7)
print(x)
print(y)
print(c)
print(y)
print(m)
print(type(m))

h=j=k="blue"
print(h)
print(j)
print(k)

e="adnan "
a="is "
s="handsom "
print(e+'' +a+''+s)

myRange=range(10)
print(*myRange)
myList=['apple','grabe','orange']
print(myList)
myTuple=('red','blue','black')
print(myTuple)
myDict={'name': 'adnan', 'age':12}
print(myDict)
k=None
print(k)
x=19+15
c=10*7
print('sayı:',x,'\nsayı2:',c)

import random

random.seed(10)
print(random.random())
print(random.getrandbits(8))
print(random.randrange(1,10))

text=("fire is not found")
search="grabe"
if search in text:
    print("mevcut")
if search not in text :
    print("yok")

sayı1=int(input("ilk sayi gir "))
sayı2=int(input("ikinci sayi gir "))
işlem=input("yapmak istediğiniz islemi yapın (toplama=+,çıkarma=-,çarpma=*,bölme=/" )

if işlem =="+":
    print(sayı1+sayı2,"işleminizin sonucu budur")
elif işlem =="-":
     print(sayı1-sayı2,"işleminizin sonucu budur")
elif işlem =="*":
     print(sayı1*sayı2,"işleminizin sonucu budur")
elif işlem =="/": 
     print(sayı1/sayı2,"işleminizin sonucu budur")

sayi1=int(input("yasini gir:")) 

if sayi1 >=18 :
    print("ehliyet alabilirsiniz")

else :
    print(("maalesef henüz ehlişyet alamasınız"))
kalan_yil= 18-sayi1
print("ehliyeti alabilmek icin  "+ str(kalan_yil) +" yil daha beklemelisin")

fruit=["bananna","apple","pinapple","cherry"]

print(fruit.replace("bananna", "orange"))
fruit[1:2]="melon"


i=1

while i<=10 :
    print("-python")
    i+=1

import random 
my_random=random.randint(1.100)
remaining_attempts=5
score=100
attempt_count=0
print("gues a numper betwen 1 and 100 ")
print(f"your starting score :{score}")

while remaining_attempts>0 :
    gues=int("enter your gues")

import math 
numper=int(input("enter a numper"))
square_root=math.sqrt(numper)

if (square_root==int(square_root)) :
    print(f"the spare root of {numper} is an integer:{int(square_root)}")
else:
    print(f"the spare root of {numper} is not an integer:{int(square_root)}")

import random 

my_random=random.randint(1,100)
remaining_attempts=6
score=100
attempt_count=0
print("gues a numper betwen 1 and 100 ")
print(f"your starting score :{score}")

while remaining_attempts>0 :
    guess=int(input("enter your guess= "))
    if guess<1 or guess>100:
        print("pleas enter a numper betwen 1 and 100")
        continue
    attempt_count+=1
    if guess==my_random:
        print(f"good jop your guess is correltly on your {attempt_count} attempt")
        print(f"your tootal score is :{score}")
        break
    elif guess<my_random:
        print("try a large numper")
    else :
        print("a smalerr numper")
    remaining_attempts-=1
    score-=15
    if remaining_attempts>0:
        print(f"reaming attempts:{remaining_attempts}")
        print(f"score:{score}")
    else :
        print("unfortunalty you run out of attempts")
        print(f"your score:{score}")

minutes=int(input("enter the call duraciton in minets: "))

fixed_fee=50
free_minutes=4
extra_fee_per_minutes=5

if(minutes<=free_minutes):
    total=fixed_fee
else:
    extra_minutes=minutes-free_minutes
    total=fixed_fee+(extra_minutes*extra_fee_per_minutes)
print(f"total cast for a {minutes} - minute call: {total}")

isim=input("ismini gir: ")

if any(dene.isdigit()for dene in isim):
    print("isminiz rakamlar ve boşluklar içeriyor.")
else:
    if isim.isalpha():
        if isim ==" " :
            print("isminiz rakamlar ve boşluklar içeriyor.")
        else:
            print(f"merhaba {isim} , hoş geldiniz")
        if len(isim)<1:
            print("bu isim gçersiz, başka bir isim girin")
        else:
            print(f"merhaba {isim} , hoş geldiniz")
    else:
        print("isminiz rakamlar ve boşluklar içeriyor.")


#görev: kulanıcıdan yaş,isim ve maaş beklentisi alıp ekrana bşiler yazsın
yaş=input("yaşini gir: ")
name=input("adini gir: ")
maaş=int(input("maaş beklentiniz nedir: "))

print(f"merhaba {name} , sizin yaşiniz {yaş} ve maaş beklentiniz {maaş}.")
print("sizin maaş beklentisi üzerinden bilgi verelim .")

if (maaş>=90000):
    print("bu maaş beklentiniz çok fazla .")
elif (maaş>=50000):
    print("aslinda bu gayet iyi bir maaş beklentisi.")
else:
    print("tamam sizi hemen aliyoruz.")


ağirlik=int(input("paketin ağirliği ne kadar :"))
şehir=input("hangi şehire gönderilmesini istiyorsunuz :")

if ağirlik<=5:
    fiyat=40
elif ağirlik>5 and ağirlik<20:
    fiyat=90
else:
    fiyat=150

print(f"kargo fiyati {fiyat}.")   

if şehir=="istanbul":
    print(f"kargo fiyati: {fiyat - 10}   yarin teslim olacaktir")
else:
    print("3 gün içinde teslim edilecetir.")


kilo=int(input("kilonu gir: "))
boy=float(input("boyunu gir: "))
vücüt_kitle=(kilo/(boy*boy))

if vücüt_kitle < 18.5:
    durum="Zayif"
elif vücüt_kitle >18.5 and vücüt_kitle <24.9:
    durum="Normal kilolu"
elif vücüt_kitle>25 and vücüt_kitle>29.9:
    durum="Fazla kilolu"
else :
    durum="Obez"
print(f"indexin {vücüt_kitle} ve sağlik durumun {durum}")


yapmak=[]
while True:
    to_do=input("TO DO: ").strip()
    if to_do == "leave":
        break
    elif to_do == "sil":
        yapmak.pop()
    else:
        yapmak.append(to_do)
    
print(yapmak)


print("merhaba oyuna hoş geldiniz . Gizli sayiyi bulmaya çalisin iyi oyunlar.")

gizli_sayi=40
tahminler=[]
deneme=0
deneme_sayisi=10
puan=100

while (True):
    tahmin=int(input("bir sayi gir : "))

    if (tahmin > 1000):
        print("sayi binin altinda")
        continue
    elif (tahmin <= 0):
        print("sayi 0 dan büyük")
        continue
    else:
        deneme+=1
        deneme_sayisi-=1
        puan-=10
        tahminler.append(tahmin)
        if (tahmin==gizli_sayi):
            print(f"teprikler kazandiniz, puan: {puan} , deneme sayisi: {deneme}")
            break
        elif (tahmin > gizli_sayi):
            print("daha küçük bir sayi gir")
        else:
            print("daha büyük bir sayi gir")
        
        if deneme_sayisi==0:
            print("deneme sayilari bitti(elendiniz)")
            break
    print(f"puan:{puan}")
    print(f"kalan deneme sayisi:{deneme_sayisi}")

for deger in tahminler:
    print(deger,end="- ")

print(f"girmiş oldüğünüz sayilar, cevap: {gizli_sayi}")


print("Bankaya hoş geldiniz")
owner=input("hesap sahipini adini giriniz: ")
#account=create_acount(owner)
şifre= 1234
işlem_geşmiş=[]

bakiye= 0
while(True):
    şif=int(input("şifreyi gir"))
    if şif==şifre:
        print("doğru şifre")
        break
    else:
        print("yanlış şifre")
while (True):

    print("'''")
    print("seçenekler")
    print("1.para yatir")
    print("2.para çek")
    print("3.bakiye göster")
    print("4.çikiş")

    choice=int(input("seçiminizi yapiniz: "))
    if choice == 4:
        print("çikildi")
        break
    elif choice == 1:
        print("ne kadar yatirmak istiyorsunuz")
        yatir=float(input(":"))
        bakiye+=yatir
        print("işlem tamamlandi")
        işlem_geşmiş.append(yatir)
    elif choice == 2:
        çek=int(input("ne kadar çekmek istiyorsunuz: "))
        if bakiye<çek:
            print("yetersiz bakiye")
            adnan=""
        else:
            bakiye-=çek
            print("işlem tamamlandi")
            işlem_geşmiş.append(çek)
    elif choice==3:
        print(f"bakiye: {bakiye}")
        işlem_geşmiş.append("bakiye sorgulama")
    else:
        print("lütfen 1-4 sayi gir.")
print(işlem_geşmiş)


ülkeler=[]
kaç=int(input("kaç ülke gireceniz: "))
dictt={}
a=0
while a<kaç:
    ülke_ismi=input("ülke ismi: ")
    ülke_kodu=input("ülke kodu gir: ")
    ülkeler.append({
        "ülkenin ismi": ülke_ismi,
        "ülke kodu": ülke_kodu
    })
    a+=1

for x in ülkeler:
    print(ülkeler)



try:
    sayi=int(input("enter: "))
    sayi2=100
    sonuc= sayi/sayi2
    print(sonuc)
except ZeroDivisionError:
    print("sifira bölunemez")
except ValueError:
    print("hata sayi girilmedi")
except Exception as e :
    print("beklenmedik hata",e)
finally:
    print("------BİTTİ------")



#yazilan şeylewri bir listeye aktar ve istenilen mitar kadar yazdir :
# def yazilar():
#     return yazi*kaç
# yazi="benim\n"
# kaç=4
# print(yazilar())

#yazilan tum sayilari yada metinleri bir listeye aktar ve yaz  sinirsiz olsun :
# def yazilar(*args):
#     liste=[]
#     for i in args:
#         liste.append(i)
#     return liste
# kaç=(1,5,9,7,8,6,2,4,8,"adnan","pınar",True)
# print(yazilar(kaç))


# yazan sayinin tam bölenlerini bir listeye aktarsin ve yasin:
# def sayi(sayi1):
#     liste=[]
#     for i in range(2,sayi1):
#         if %i==0:
#             liste.append(i)
#     return liste
# gizli=100
# print(sayi(gizli))
