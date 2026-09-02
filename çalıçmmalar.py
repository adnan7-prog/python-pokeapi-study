import json
import os

FILE_NAME = "adnan.json" # Türkçe karakter hatası olmaması için büyük I yerine I kullandık.

class Person: # Sınıf isimleri genellikle büyük harfle başlar
    def __init__(self):
        # Program ilk açıldığında adnan.json dosyası var mı diye bakar. Yoksa boş bir liste [] oluşturur.
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def read_people(self):
            try:
                # Dosyayı normal şekilde okumaya çalış
                with open(FILE_NAME, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.decoder.JSONDecodeError, FileNotFoundError):
                # Eğer dosya boşsa veya bozuksa, burası çalışır:
                # Dosyanın içine hemen boş bir liste [] yazar ve programa [] döndürür.
                with open(FILE_NAME, "w", encoding="utf-8") as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                return []
    def save_person(self, people):
        # Yeni listeyi adnan.json dosyasına kalıcı olarak kaydeder.
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(people, f, ensure_ascii=False, indent=4)
    def search_person(self):
        name = input("Aratmak istediğiniz kişinin adı: ")
        people = self.read_people() # self sayesinde yukarıdaki okuma fonksiyonunu çağırdık
        found = False

        for item in people:
            if item["name"].lower() == name.lower(): # Büyük/küçük harf duyarlılığını kaldırdık
                print(f"👉 Bulundu! İsim: {item['name']}, Yaş: {item['age']}, Şehir: {item['city']}")
                found = True
        
        if not found:
            print(f"❌ {name} isimli biri kayıtlarda yok.")   

    def add_person(self):
        # Kullanıcıdan bilgileri alır.
        name = input("İsim: ")
        age = int(input("Yaş: "))
        city = input("Şehir: ")
        
        # Bilgileri bir paket (sözlük) haline getirir.
        new_person = {"name": name, "age": age, "city": city}

        # Mevcut insanları okur, yenisini ekler ve kaydeder.
        people = self.read_people()
        people.append(new_person)
        self.save_person(people)
        print(f"{name} başarıyla eklendi.")

    def deleted_person(self):
        name = input("Silmek istediğiniz kişinin adını yazınız: ")
        people = self.read_people()
        
        # İsmi eşleşmeyen kişileri yeni bir listeye alır (Böylece yazılan isim silinmiş olur)
        del_per = [item for item in people if item["name"] != name]

        if len(del_per) == len(people):
            print(f"{name} bulunamadı.")
        else:
            self.save_person(del_per)
            print(f"{name} başarıyla silindi.")

    def show_people(self):
        # Kayıtlı herkesi ekrana alt alta yazdırır.
        people = self.read_people()
        if not people:
            print("Kayıtlı kimse bulunamadı.")
        else:
            for item in people:
                print(f"İsim: {item['name']}, Yaş: {item['age']}, Şehir: {item['city']}")

class App:
    def __init__(self):
        self.manager = Person()

    def run_person(self):
        # Sonsuz bir döngü başlatır, kullanıcı 4'e basana kadar menüyü gösterir.
        while True:
            print("\n1. Kişi Ekle")
            print("2. Kişi Sil")
            print("3. Kişileri Göster")
            print("4. Kişi Ara") # Yeni ekledik
            print("5. Çıkış")
            choose = input("Seçiminiz: ")
            
            if choose == "1": 
                self.manager.add_person()
            elif choose == "2":
                self.manager.deleted_person()
            elif choose == "3":
                self.manager.show_people()
            elif choose == "4":
                self.manager.search_person
            elif choose == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Lütfen geçerli bir numara girin.")

if __name__ == "__main__":
    app = App()
    app.run_person() 






    




