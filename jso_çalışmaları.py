import json
import os
# import time

FILE_NAME = "kitaplar.json"

class KutuphaneYonetimi:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME,"w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False,indent=4)

    def kitaplari_yukle(self):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
                # Eğer dosya boşsa veya bozuksa, burası çalışır:
                # Dosyanın içine hemen boş bir liste [] yazar ve programa [] döndürür.
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)
            return []

    def kitaplari_kaydet(self, kitap_listesi):
        with open(FILE_NAME,"w",encoding="utf-8") as f:
            json.dump(kitap_listesi,f,ensure_ascii=False,indent=4)

    def kitap_ekle(self):
        kitap1=input("kitap adi: ")
        yazar1=input("yazar adi: ")
        sayfa1=int(input("sayfa sayisi: "))
        bilgiler={"kitap":kitap1,"yazar":yazar1,"sayfa":sayfa1}
        kitaplar=self.kitaplari_yukle()
        kitaplar.append(bilgiler)
        self.kitaplari_kaydet(kitaplar)
        print("bilgiler kaydedildi! \n")

    def kitap_sil(self):
        kitaplar=self.kitaplari_yukle()
        silmek=input("silmek istediğiniz kitabn adini yaziniz: ")
        result=[item for item in kitaplar if item["kitap"] != silmek]
        if len(result) == len(kitaplar):
            print(f"{silmek} bulunmadi tekrar denmyiniz")
        else:
            self.kitaplari_kaydet(result)
            print("başariyla tamamlandi.")
    def kitaplari_listele(self):
        kitaplar=self.kitaplari_yukle()
        if not kitaplar:
            print("kutubhane boş")
        else:
            for item in kitaplar:
                print(f'\nkitap adi: {item["kitap"]}, yazar adi: {item["yazar"]}, sayfa sayisi :{item["sayfa"]}\n')
class Menu:
    def __init__(self):
        self.aboo=KutuphaneYonetimi()
    def calistir(self):
        while True:
            print("1.ekle")
            print("2.sil")
            print("3.listele")
            print("4.çikiş")
            sayi=(input(" sayi seçiniz: ")).strip()
            if sayi =="1":
                self.aboo.kitap_ekle()
            elif sayi =="2":
                self.aboo.kitap_sil()
            elif sayi =="3":
                self.aboo.kitaplari_listele()
            elif sayi=="4":
                print("çikiliyor...")
                # time.sleep(1)
                break
            else:
                print("litfen geçerli sayi giriniz!!!!!!1")

if __name__ == "__main__":
    app=Menu()
    app.calistir()
