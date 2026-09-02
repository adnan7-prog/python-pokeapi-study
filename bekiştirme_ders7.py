# class Hayvan:
#     def __init__(self,isim,ses):
#         self.isim = isim
#         self.ses = ses
#     def sesli_çikar(self):
#         print(f"{self.isim} diyorki : {self.ses} cikar")
# class Kedi(Hayvan):
#     def __init__(self):
#         super().__init__("Kedi","Miyavvv")
#     def sesli_çikar(self):
#         print(f" {self.ses} cikar")
# hayvanlar=Hayvan("Karabas","Miyavvv")
# hayvanlar.sesli_çikar()
# kedi=Kedi()
# kedi.sesli_çikar()



# while True:
#     sayi=input("bolunecek sayiyi  giriniz: ")
#     sayi1=input("bolen sayiyi giriniz: ")
#     try:
#         sayim=int(sayi)/int(sayi1)
#         print(f"bolme isleminin sonucu: {sayim}")
#         break
#     except ValueError:
#         print("sayi girmeyiniz, tekrar deneyin")

#     except ZeroDivisionError:
#         print("bolen 0 olamaz")



# import json
# import os


# FILENAME="veriler.json"

# class Islem:
#     def __init__(self):
#         if not os.path.exists(FILENAME):
#             with open(FILENAME,"w",encoding="utf-8") as f:
#                 json.dump([],f,ensure_ascii=False,indent=4)
#     def okuma(self):
#         try:
#             with open(FILENAME,"r",encoding="utf-8") as f:
#                 return json.load(f)
#         except (json.JSONDecodeError, FileNotFoundError):
#             return []
#     def yazma(self,bilgi):
#         with open(FILENAME,"w",encoding="utf-8") as f:
#             json.dump(bilgi,f,ensure_ascii=False,indent=4)    
#     def ekle(self):
#         eklemek=self.okuma()
#         print("----------gelir-gider ekleme işlemi--------")
#         işlem=input("işlem türü (gelir/gider): ")
#         miktar=int(input("miktar: "))
#         birleştir={"işlem":işlem,
#                    "miktar":miktar}
#         eklemek.append(birleştir)
#         self.yazma(eklemek)
#         print(" ekleme işlemi tamamlandı \n")
#     def listele(self):
#         liste=self.okuma()
#         if not liste:
#             print("daha once hiç bir bilgi girmediniz\n")
#         else:
#             for item in liste:
#                 print(f"    İşlem türü: {item['işlem']}  \n    Miktar: {item['miktar']}\n")
#     def sil(self):
#         liste=self.okuma()
#         if not liste:
#             print("daha once hiç bir bilgi girmediniz\n")
#             return []
#         print("----------gelir-gider silme işlemi--------")
#         nesilmek=input("neyi silmek isiyorsunuz (işlemin): ")
#         durum=False
#         for liste_valeu in liste:
#             if liste_valeu.get("işlem") == nesilmek:
#                 liste.remove(liste_valeu)
#                 durum=True
#                 break
#         if durum :
#             self.yazma(liste)
#             print("işlem tamamlandi")
#         else:
#             print(f"{nesilmek} adinda hiç bir bilgi bulamadik.")


# class Dosyalar:
#     def __init__(self):
#         self.islem=Islem()
#     def işlemler(self):
#         while True:
#             print("1-işlem ekle")
#             print("2-işlem listele")
#             print("3-işlem sil")
#             print("4-cıkış")
#             secim=input("seciminiz: ")
#             try:
#                 secimin=int(secim)
#             except ValueError:
#                 print("lütfen bir rakam giriniz !!\n")
#                 continue
#             if secimin == 1:
#                 self.islem.ekle()
#             elif secimin == 2:
#                 self.islem.listele()
#             elif secimin == 3:
#                 self.islem.sil()
#             elif secimin == 4:
#                 break
#             else:
#                 print("gecersiz secim\n")

# if __name__=="__main__":
#     app=Dosyalar()
#     app.işlemler()
        
        


# def fonkudsyon_ekle(func):
#     def degiştir(*args,**kwargs):
#         orjinal=func(*args,**kwargs)
#         yeni=orjinal.replace("adnan","ekrem")
#         print("fonksuyon guncellenndi")
#         return yeni
#     return degiştir

# @fonkudsyon_ekle
# def sabit_hiz():
#     return "adnan ucar mi ucar"
    
# print(sabit_hiz())


# def ekmek_fabrikasi():
#     print("🥖 1. ekmek fırından çıkıyor...")
#     yield "Sıcak Ekmek 1"
    
#     print("🥖 2. ekmek fırından çıkıyor...")
#     yield "Sıcak Ekmek 2"
    
#     print("🥖 3. ekmek fırından çıkıyor...")
#     yield "Sıcak Ekmek 3"

# # Fonksiyonu çağırdığımızda hemen çalışmaz, bize bir GENERATOR nesnesi verir.
# firin = ekmek_fabrikasi()
# print(firin) # Çıktı: <generator object ekmek_fabrikasi at ...>
# print(next(firin))  
# print(next(firin))  
# print(next(firin))  
# print(next(firin))  

# def sayi_ureten():
#     for birler in range(10):
#         for onlar in range(10):
#             for yuzler in range(10):
#                 for binler in range(10):
#                     yield f"{binler}{yuzler}{onlar}{birler}"
# benim_şifrem="1520"
# for sayi_bul in sayi_ureten():
#     if sayi_bul == benim_şifrem:
#         print(f"🔓 Kasa açıldı! Doğru şifre: {benim_şifrem}")
#         break
#     else:
#         print("bulamadik")
#         break



# def yieldm():
#     yield "biinci"
#     yield "ikincş"
#     yield "ucuncu"
# fonksyın=yieldm()
# while True:
#     try:
#         print(next(fonksyın))
#     except StopIteration:
#         print("bittti")
#         break 

# import time
# def urun_getirici(toplam_sayfa):
#     for sayfa in range(1, toplam_sayfa + 1):
#         print(f"🌐 İnternetten {sayfa}. sayfa indiriliyor...")
#         time.sleep(0.7)
#         yield [f"Ürün_S{sayfa}_1", f"Ürün_S{sayfa}_2"]

# veri_akisi = urun_getirici(toplam_sayfa=3)

# for urunler in veri_akisi:
#     print(f"📦 Alınan Ürünler İşleniyor: {urunler}")




# import random

# def sicaklik():
#     while True:
#         sicak_seviye=random.randint(0,100)
#         yield sicak_seviye
# for x in sicaklik():
#     print(f"  sicakli seviyesi {x}")
#     if x == 50:
#         print(f"guncel sicaklik {x}")
#         print("herkes denize!!!")
#         break



# import random 
# def fatura_basligi(func):
#     def iç_fonksyon(*agrs,**kwargs):
#         print("===bizim petrol faturasi===")
#         return func(*agrs,**kwargs)
#     return iç_fonksyon

# @fatura_basligi
# def yakit_pompasi(toplam_litre):
#     while toplam_litre > 0:
#         yield toplam_litre
#         toplam_litre-=1

        
# depo=yakit_pompasi(3)
# while True:
#     try:
#         sonuc=next(depo)
#         print(sonuc ,"L benzin kaldi")
#     except StopIteration:
#         print("benzin kalmadi "
#               )
#         break 

# import random 

# # 1. 'maden_kontrol' adında bir decorator fonksiyonu yaz (Parametre olarak 'func' alsın)
# # 2. İçine 'ic_fonksiyon' aç (*args, **kwargs alsın)
# # 3. 'ic_fonksiyon' içinde İLK ÖNCE ekrana "⛏️ Madencilik Başlatıldı, Bloklar taranıyor..." yazdır
# # 4. Altına 'return func(*args, **kwargs)' yazarak orijinal fonksiyonu döndür
# def maden_kontrol(func):
#     def iç_fonksyon(*args,**kwargs):
#         print("⛏️ Madencilik Başlatıldı, Bloklar taranıyor...")
#         return func(*args,**kwargs)
#     return iç_fonksyon
# # --- DECORATOR BİTTİ, GENERATOR KISMI ---

# @maden_kontrol
# def kripto_kazici():
#     while True:
#         rasgel_sayi=random.randint(0,10)
#         if rasgel_sayi == 0:
#             raise ValueError("⚠️ Grafik kartı aşırı ısındı!")
#             break
#         else:
#             yield rasgel_sayi
# # 5. Yazdığın '@maden_kontrol' decorator'ını aşağıdaki fonksiyona uygula
# # 6. 'kripto_kazici' adında bir fonksiyon tanımla (Parametre almasın)
# # 7. İçine 'while True' sonsuz döngüsü aç
# # 8. Döngünün içinde 'random' kütüphanesini kullanarak 0 ile 10 arasında rastgele bir sayı üret
# # 9. Eğer üretilen sayı 0 ise, 'raise ValueError("⚠️ Grafik kartı aşırı ısındı!")' diyerek yapay bir hata fırlat!
# # 10. Eğer sayı 0 değilse, 'yield sayı' diyerek o sayıyı (kazılan kripto miktarını) fırlat
# maden=kripto_kazici()
# while True:
#     try:
#         x= next(maden)
#         print(f"Bitcoin kazıldı: {x}")
#     except ValueError as e:
#         print(e)
#         break
# --- ANA PROGRAM (TEST KISMI) ---


# 11. 'maden = kripto_kazici()' diyerek generator nesnesini oluştur
# 12. Sonsuz bir 'while True' döngüsü daha aç (Dışarıda verileri çekmek için)
# 13. Bir 'try' bloğu aç ve içinde 'next(maden)' ile gelen kazanç sayısını ekrana "Bitcoin kazıldı: X" şeklinde bas
# 14. Bir 'except ValueError as e:' bloğu aç, ekrana hatayı (e) bas ve 'break' ile madenciliği durdur



# DECAROTR Başlığı: makine_isigi (Fonksiyon çalışmadan önce ekrana bir hazırlık yazısı basmalı).
# Generator Başlığı: kahve_degirmeni (Her adımda bardağa mililitre cinsinden kahve fırlatmalı).
# Hata Fırlatma Şartı: Kahve miktarı belirli bir sınırı aşarsa ValueError ile taşma hatası fırlatmalı.
# Ana Program Döngüsü: Dışarıda try-except ile bu hatayı yakalayıp makineyi güvenle durdurmalı.
# import random
# import time
# def makine_isigi(func):
#     def yazi_dondur(*args,**kwargs):
#         print("---program başliyor---")
#         return func(*args,**kwargs)
#     return yazi_dondur

# @makine_isigi
# def kahve_akisi():
#     while(True):
#         kahve_sec=random.randint(0,1000)
#         if kahve_sec <900:
#             time.sleep(0.1)
#             yield f"-----------{kahve_sec}m  kavhe atildi.-----------"
#         else:
#             raise ValueError(f"‼{kahve_sec}m , siniri açti")
# kahve_yaz=kahve_akisi()
# while (True):
#     try:
#         sonraki=next(kahve_yaz)
#         print(sonraki)
#     except ValueError as e:
#         print(e)
#         break





# 1. 'BankaKasasi' adında bir sınıf (class) tanımla

# 2. Sınıfın '__enter__' metodunu yaz. İçinde ekrana "🔓 Kasa kilidi açıldı, içeri girildi." bassın ve 'return self' yapsın

# 3. Sınıfın içine 'para_cek' adında bir metot yaz (Parametre olarak 'miktar' alsın).
#    - Ekrana "💵 X TL kasadan çekiliyor..." yazsın.
#    - Eğer miktar 5000'den büyükse, 'raise ValueError("🚨 Yetersiz bakiye veya limit aşımı!")' hatası fırlatsın.

# 4. Sınıfın '__exit__' metodunu yaz (3 sihirli parametreyi unutma!).
#    - İlk önce ekrana "🔒 Kasa kapısı kapatıldı ve kilitlendi." yazsın.
#    - Eğer içeride bir hata çıktıysa (exc_type None değilse), ekrana hatanın mesajını (exc_val) bassın ve 'return True' ile programın çökmesini engellesin.

# --- BAKIYI TEST ETME KISMI (with bloğu) ---

# 5. 'with BankaKasasi() as kasa:' diyerek bloğu başlat

# 6. Kasa içinden önce normal bir para çek (Örn: 2000)

# 7. Hemen altına limiti aşacak bir para çekme komutu yaz (Örn: 6000) ki hata fırlatıp fırlatmadığını görelim
# class Bankakasasi:
#     def __enter__(self):
#         print("banka kasasi acıldi")
#         return self
#     def para_çek(self,miktar):
#         print(miktar,"kasadan çikiliyor")
#         if 5000 < miktar:
#             raise ValueError("yetersiz bakiye")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("kasa kilitlendi")
#         if exc_type is not None:
#             print("hata oldu:",exc_val)
#             return True
#         return False
# with Bankakasasi() as ad:
#     ad.para_çek(2000)
#     ad.para_çek(54545)




# import random
# import time
# from typing import Generator, List, Optional, Dict, Any

# # ==========================================
# # 📌 1. DECORATOR: GÜVENLİK DUVARI VE RAPORLAMA
# # ==========================================
# def guvenlik_tarayıcısı(func: Any) -> Any:
#     """Sistemlerin başlama ve bitiş anını loglayan profesyonel bir decorator."""
#     def ic_fonksiyon(*args: Any, **kwargs: Any) -> Any:
#         print("\n" + "="*50)
#         print("🛡️ [GÜVENLİK DUVARI ACTIVATED] - Ağ Analizi Başlatılıyor...")
#         print("="*50)
        
#         # Orijinal fonksiyonu (generator'ı) çalıştırıp geri döndürüyoruz
#         return func(*args, **kwargs)
        
#     return ic_fonksiyon

# # ==========================================
# # 📌 2. CONTEXT MANAGER: VERİ TABANI LOG SİSTEMİ
# # ==========================================
# class LogVeriTabani:
#     """Yakalanan siber saldırı verilerini tabana yazan Context Manager."""
#     def __init__(self, db_adi: str) -> None:
#         self.db_adi: str = db_adi

#     def __enter__(self) -> "LogVeriTabani":
#         print(f"🗄️ [SİSTEM] {self.db_adi} veri tabanına güvenli bağlantı kuruldu.")
#         return self

#     def log_kaydet(self, log_detayi: Dict[str, Any]) -> None:
#         """Gelen log verisini analiz eder ve kritik durumlarda hata fırlatır."""
#         print(f"💾 [YAZILIYOR] Log veri tabanına işleniyor: {log_detayi['ip']} -> {log_detayi['durum']}")
        
#         # Eğer gelen istek bir DDOS saldırısıysa sistemi korumak için hata fırlatıyoruz!
#         if log_detayi["durum"] == "DDOS SALDIRISI":
#             raise ConnectionRefusedError(f"🚨 KRİTİK TEHLİKE: {log_detayi['ip']} adresinden gelen DDOS engellendi!")

#     def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
#         print(f"🔒 [KAPATILDI] {self.db_adi} bağlantısı kesildi. RAM boşaltıldı.")
        
#         # Eğer ConnectionRefusedError (DDOS Hatası) çıktıysa programı çökertme, sustur!
#         if exc_type is ConnectionRefusedError:
#             print(f"\n⚡ [SİBER SAVUNMA HATTI] Hata yakalandı ve engellendi:\n   --> {exc_val}")
#             print("🛡️ Saldırgan IP adresi kara listeye alındı. Sistem çalışmaya devam ediyor.\n")
#             return True # True dönerek programın çökmesini engelliyoruz
            
#         return False

# # ==========================================
# # 📌 3. GENERATOR VE TYPE HINTING: AĞ AKIŞI
# # ==========================================
# @guvenlik_tarayıcısı
# def canlı_ag_akisi(istek_sayisi: int) -> Generator[Dict[str, Any], None, None]:
#     """İnternetten gelen anlık istekleri paket halinde canlı üreten generator."""
#     durumlar: List[str] = ["200 OK", "404 NOT FOUND", "200 OK", "DDOS SALDIRISI", "500 SERVER ERROR"]
    
#     for i in range(1, istek_sayisi + 1):
#         time.sleep(0.4) # Canlı ağ trafiği simülasyonu
        
#         # Rastgele bir IP ve ağ durumu üretiyoruz
#         istek_paketi: Dict[str, Any] = {
#             "id": i,
#             "ip": f"192.168.1.{random.randint(10, 250)}",
#             "durum": random.choice(durumlar)
#         }
        
#         yield istek_paketi

# # ==========================================
# # 📌 4. ANA PROGRAM (TRY-EXCEPT VE KONTROL MERKEZİ)
# # ==========================================
# # 10 adet canlı ağ isteği taramak üzere generator nesnemizi oluşturuyoruz
# ag_trafiği = canlı_ag_akisi(istek_sayisi=10)

# # Veri tabanı bağlam yöneticimizi (Context Manager) başlatıyoruz
# with LogVeriTabani("Siber_Savunma_Log_DB") as db:
#     while True:
#         try:
#             # Generator'dan sıradaki ağ isteğini çekiyoruz
#             gelen_istek = next(ag_trafiği)
            
#             print(f"🌐 [AĞ TRAFİĞİ] İstek No: {gelen_istek['id']} | Gelen IP: {gelen_istek['ip']}")
            
#             # Yakalanan isteği veri tabanına kaydetmesi için gönderiyoruz
#             db.log_kaydet(gelen_istek)
#             print("-" * 40)
            
#         except StopIteration:
#             # Tüm ağ istekleri hatasız bittiğinde generator bu hatayı fırlatır
#             print("✅ [BAŞARILI] Tüm ağ trafiği güvenli bir şekilde tarandı ve bitti.")
#             break

# print("🚀 [FİNAL] Büyük proje çökmeden başarıyla tamamlandı!")
        


# import random
# import time
# from typing import Generator, List, Any, Dict

# # ==========================================
# # 📌 1. ÖZEL EXCEPTION (İSTİSNA) SINIFI
# # ==========================================
# class RoketArizasiError(Exception):
#     """Roket motorlarında veya yakıt tankında kritik arıza olunca fırlatılan özel hata."""
#     pass

# # ==========================================
# # 📌 2. DECORATOR: KONTROL MERKEZİ ANONS SİSTEMİ
# # ==========================================
# def ana_kontrol_anonsu(func: Any) -> Any:
#     """Fırlatma operasyonunun başlangıcını tüm üsse ilan eden decorator."""
#     def ic_fonksiyon(*args: Any, **kwargs: Any) -> Any:
#         print("\n" + "🚀" * 20)
#         print("📢 [KONTROL MERKEZİ]: TÜM SİSTEMLER ATEŞLEME POZİSYONUNA!")
#         print("🚀" * 20 + "\n")
#         return func(*args, **kwargs)
#     return ic_fonksiyon

# # ==========================================
# # 📌 3. CONTEXT MANAGER: GÜVENLİK VE ACİL DURUM KAPISI
# # ==========================================
# class UzayUssuGuvenlik:
#     """Fırlatma esnasında üssü koruyan, hata çıkarsa roketi acilen imha eden Context Manager."""
#     def __init__(self, roket_adi: str) -> None:
#         self.roket_adi: str = roket_adi

#     def __enter__(self) -> "UzayUssuGuvenlik":
#         print(f"🔒 [GÜVENLİK]: {self.roket_adi} için acil durum kilitleri açıldı.")
#         return self

#     def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
#         print(f"\n🔒 [GÜVENLİK]: Fırlatma alanı kilitlendi. Güvenlik protokolü bitti.")
        
#         # Eğer roket çalışırken bizim yazdığımız 'RoketArizasiError' hatası çıkarsa:
#         if exc_type is RoketArizasiError:
#             print(f"🚨 [ACİL DURUM SİRENLERİ]: {exc_val}")
#             print(f"💥 {self.roket_adi} güvenli irtifada havada İMHA EDİLDİ! Mürettebat tahliye kapsülünde.")
#             return True # True döndürerek ana programın (üs binasının) çökmesini engelliyoruz!
            
#         return False

# # ==========================================
# # 📌 4. ITERATOR PROTOKOLÜ: GERİ SAYIM MOTORU
# # ==========================================
# class GeriSayim:
#     """for döngüsüyle uyumlu çalışan, __iter__ ve __next__ içeren geri sayım aracı."""
#     def __init__(self, baslangic: int) -> None:
#         self.sayac: int = baslangic

#     def __iter__(self) -> "GeriSayim":
#         return self

#     def __next__(self) -> int:
#         if self.sayac >= 0:
#             mevcut_saniye = self.sayac
#             self.sayac -= 1
#             return mevcut_saniye
#         else:
#             raise StopIteration # Sayım bitince for döngüsünü durdurur

# # ==========================================
# # 📌 5. GENERATOR VE TYPE HINTING: TELEMETRİ VERİ AKIŞI
# # ==========================================
# @ana_kontrol_anonsu
# def roket_telemetri_akisi(hedef_irtifa: int) -> Generator[Dict[str, Any], None, None]:
#     """Roket yükselirken anlık hız ve irtifa verisi üreten generator."""
#     mevcut_irtifa: int = 0
#     hiz: int = 500
    
#     while mevcut_irtifa < hedef_irtifa:
#         time.sleep(0.4) # Canlı uçuş simülasyonu
#         mevcut_irtifa += random.randint(1000, 3000)
#         hiz += random.randint(200, 500)
        
#         # Eğer roket şans eseri 8000 metreyi geçerse motor arıza riskini simüle ediyoruz
#         if mevcut_irtifa > 8000 and random.random() < 0.4:
#             raise RoketArizasiError("Motor basıncı kritik seviyenin altına düştü!")
            
#         # Dışarıya anlık veri paketi fırlatıyoruz
#         yield {"irtifa": mevcut_irtifa, "hiz": hiz}

# # ==========================================
# # 📌 6. ANA KONTROL MERKEZİ (TRY-EXCEPT BÜTÜNLEŞMESİ)
# # ==========================================

# # Adım A: Iterator Protokolü ile geri sayım başlatılıyor
# print("⏱️ Geri sayım başlatılıyor...")
# for saniye in GeriSayim(3):
#     print(f" T E K S İ N P O Z İ S Y O N : {saniye}")
#     time.sleep(0.5)

# # Adım B: Generator Nesnesi Hazırlanıyor (Hedef 15.000 metre)
# ucus_verileri = roket_telemetri_akisi(hedef_irtifa=15000)

# # Adım C: Context Manager ve Try-Except ile Büyük Uçuş Başlıyor
# with UzayUssuGuvenlik("Falcon-X") as guvenlik:
#     while True:
#         try:
#             # Generator'dan sıradaki uçuş verisini çekiyoruz
#             veri = next(ucus_verileri)
#             print(f"🚀 [UÇUŞ VERİSİ] İrtifa: {veri['irtifa']} m | Hız: {veri['hiz']} km/s")
            
#         except StopIteration:
#             # Uçuş verileri hatasız bittiğinde generator bu hatayı fırlatır
#             print("\n🌌 [BAŞARILI]: Roket yörüngeye oturdu! Görev başarıyla tamamlandı.")
#             break

# print("\n🏁 [SİSTEM]: Ana program sonlandırıldı.")
# import time
# from typing import Generator, Any


# # 'DosyaBulunamadiHatasi' sınıfını yaz (Exception'dan türet)
# class DosyaBulunamadiHatasi(Exception):
#     pass 

# # 'KritikSatirHatasi' sınıfını yaz (Exception'dan türet)
# class KritikSatirHatasi(Exception):
#     pass


# # 'sure_olcer' decorator'ını tanımla
# # İç fonksiyonu aç, time.time() ile başlangıcı tut, fonksiyonu çalıştır, bitişi ölç ve ekrana bas
# def sure_olcer(func):
#     def iç_fonksyon(*args,**kwargs):
#         başlangış=time.time()
#         funcm=func(*args,**kwargs)
#         son=time.time()
#         print(f"sure olçer {son - başlangış}")
#         return funcm
#     return iç_fonksyon

# # ==========================================
# # 📌 ADIM 3: CONTEXT MANAGER (DOSYA İŞLEYİCİ)
# # ==========================================
# # 'DosyaIsleyici' sınıfını yaz, __init__ ile dosya adını al
# class DosyaIslyici:
#     def __init__(self,dosya:str):
#         self.dosya_ad=dosya
#     def __enter__(self):
#         try :
#             self.d=open(self.dosya_ad,"r",encoding="utf-8")
#             return self.d
#         except FileNotFoundError:
#             raise DosyaBulunamadiHatasi("dosya bulunamadı !!!!!!")
            
#     # __enter__ metodunu yaz. Dosyayı open() ile açmayı dene. 
#     # FileNotFoundError çıkarsa kendi yazdığın 'DosyaBulunamadiHatasi'nı fırlat. Dosya nesnesini döndür.


#     # __exit__ metodunu yaz. Dosyayı kapat. 
#     # Eğer çıkan hata 'KritikSatirHatasi' ise ekrana yazdır ve True döndür.
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.d:
#             self.d.close()
#             print("🔒 Dosya güvenle kapatıldı.")
            
#         # Eğer çıkan hata bizim yazdığımız KritikSatirHatasi ise sustur!
#         if exc_type is KritikSatirHatasi:
#             print(f"⚠️ Hata Yakalandı ve Susturuldu: {exc_val}")
#             return True # Programın çökmesini engeller
#         return False


# # ==========================================
# # 📌 ADIM 4: GENERATOR (SATIR OKUYUCU)
# # ==========================================
# # '@sure_olcer' decorator'ını ekle
# # 'satir_oku' fonksiyonunu tanımla (dosya nesnesi parametre alsın)
# # Döngüyle satırları dön. Eğer satırda "KRİTİK_HATA" varsa 'KritikSatirHatasi' fırlat. Yoksa yield et.
# @sure_olcer
# def satir_oku(dosya):
#     for satir in dosya:
#         if  "KRİTİK_HATA" in satir:
#             raise  KritikSatirHatasi("ola ola kritik hata oluştu")
#         else: 
#             yield satir.strip()

# # ==========================================
# # 📌 ADIM 5: ANA PROGRAM (TEST KISMI)
# # ==========================================
# # 'with DosyaIsleyici("veriler.txt") as f:' bloğunu kur (Önce bilgisayarında veriler.txt oluşturup içine birkaç satır yazabilirsin)
# # İçeride 'satir_oku(f)' generator'ını bir döngüyle veya next() ile tüketerek ekrana bas

# with DosyaIslyici("veriler.txt") as f:
#     for i in satir_oku(f):
#         print(i)




