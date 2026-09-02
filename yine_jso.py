import json
import os 
class Work:
    def __init__(self):            
        if not os.path.exists("hesap.json"):
            with open("hesap.json","w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False,indent=4)

    def yazma(self,bilgi):
        with open("hesap.json","w",encoding="utf-8") as f:
            json.dump(bilgi,f,ensure_ascii=False,indent=4)

    def okuma(self):
        with open("hesap.json","r",encoding="utf-8") as f:
            return json.load(f)
        
    def para_ekle(self):
        eklenenler = self.okuma()
        while True:
            try:
                miktar=int(input("ne kadar yatirmak istersiniz: "))
                break
            except ValueError:
                print("     lütfen bir rakam giriniz !!")
                continue
        if not eklenenler:
            uyarisi={"işlem":"para ekle","durum":"gerçekleşti","bakiye":miktar}
        else:
            sonuc=eklenenler[-1]
            kalan_bakiye=sonuc["bakiye"]
            kalan_bakiye+=miktar
            uyarisi={"işlem":"para ekle","durum":"gerçekleşti","bakiye":kalan_bakiye }
            print("işlem tamamlandi.\n")
        eklenenler.append(uyarisi)
        self.yazma(eklenenler)

    def para_çek(self):
        eklenenler=self.okuma()
        while True:
            try:
                çek=int(input("ne kadar almak istiyorsunuz: "))
                break
            except ValueError:
                print("     lütfen bir rakam giriniz !!")
                continue

        if not eklenenler:
            kalan_bakiye = 1000
        else:
            son_islem = eklenenler[-1]
            kalan_bakiye=son_islem["bakiye"]
        if çek > kalan_bakiye:
            print("Yetersiz bakiye!")
        else :
            kalan_bakiye-=çek
            uyarisi={"işlem":"para çek","durum":"gerçekleşti","bakiye":kalan_bakiye}
            eklenenler.append(uyarisi)
            self.yazma(eklenenler)
            print("işlem tamamlandi.\n")

    def guncel_durum(self):
        eklenenler=self.okuma()
        if not eklenenler:
            print("hiç bir işlem yapmadiniz.")
        else:
            for i in eklenenler:
                print(f'yaptiğiniz işlem: {i["işlem"]}, durum: {i["durum"]},guncel bakiyeniz: {i["bakiye"]}')
            print("işlem tamamlandi.\n")
class EveryWork:
    def __init__(self):        
        self.works=Work()
    def tum_içlemler(self):
        while True:
            print("1.para yatir")
            print("2.para çek")
            print("3.bilgileri goster")
            print("4.çik")
            seçim=int(input("seçiminizi yaziniz: "))
            if seçim == 1:
                self.works.para_ekle()
            elif seçim ==2:
                self.works.para_çek()
            elif seçim == 3 :
                self.works.guncel_durum()
            elif seçim == 4 :
                print("çikliyor...")
                break
            else:
                print("         lütfen bir sayi giriniz.")
if __name__ == "__main__":
    app=EveryWork()
    app.tum_içlemler()