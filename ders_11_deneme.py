# import sqlite3

# con = sqlite3.Connection("kutuphane.db")
# kitap = con.cursor()


# def temizle_ve_olustur():
#     kitap.execute("DROP TABLE IF EXISTS kitaplar")
#     kitap.execute("DROP TABLE IF EXISTS yazarlar")
#     kitap.execute("CREATE TABLE IF NOT EXISTS kitaplar (id INTEGER PRIMARY KEY AUTOINCREMENT, kitap_adi TEXT, sayfa_sayisi INT, puan INT, yazar_id INT)")
#     kitap.execute("CREATE TABLE IF NOT EXISTS yazarlar (id INTEGER PRIMARY KEY AUTOINCREMENT, yazar_adi TEXT)")
#     con.commit()


# def insert():
#     print("\n--- YENİ YAZAR VE KİTAP EKLEME ---")
#     yazar_adi = input("Yazar adını giriniz: ")
#     kitap.execute("INSERT INTO yazarlar (yazar_adi) VALUES(?)", (yazar_adi,))
#     con.commit()
#     son_yazar_id = kitap.lastrowid
#     kitap_adi = input("Kitap adını yazınız: ")
#     sayfa_sayisi = int(input("Sayfa sayısını giriniz: "))
#     puan = int(input("Verdiğiniz puan (1-10): "))

#     kitap.execute(
#         "INSERT INTO kitaplar (kitap_adi, sayfa_sayisi, puan, yazar_id) VALUES(?,?,?,?)",
#         (kitap_adi, sayfa_sayisi, puan, son_yazar_id),)
#     con.commit()
#     print(" Veri başarıyla kaydedildi!\n" + "-" * 24)


# def bul():
#     print("\n--- KİTAP ARA ---")
#     aranan = input("Aramak istediğiniz kitap adını girin: ")
#     kitap.execute("SELECT * FROM kitaplar WHERE kitap_adi = ?", (aranan,))
#     sonuclar = kitap.fetchall()

#     if not sonuclar:
#         print("Aradığınız kitap bulunamadı.")
        
#     for satir in sonuclar:
#         print(satir)
#     print("-" * 24)


# def sirala():
#     sorgu = """
#         SELECT kitaplar.id, kitaplar.kitap_adi, kitaplar.sayfa_sayisi, kitaplar.puan, yazarlar.yazar_adi 
#         FROM kitaplar 
#         INNER JOIN yazarlar ON kitaplar.yazar_id = yazarlar.id
#     """
#     kitap.execute(sorgu)
#     save = kitap.fetchall()
#     print("\n--- KİTAPLAR LİSTESİ ---")
#     if not save:
#         print("[Tablo şu an boş Lütfen önce 1'e basıp kitap ekleyin]")
#         return
#     for i in save:
#         print(f"id: {i[0]}, kitap: {i[1]}, sayfa: {i[2]}, puan: {i[3]} , yazar_id: {i[4]}")
#     print("-" * 24)


# def yazar_puan_ortalamalari():
#     sorgu = """
#         SELECT yazarlar.yazar_adi, AVG(kitaplar.puan)
#         FROM kitaplar
#         INNER JOIN yazarlar ON kitaplar.yazar_id = yazarlar.id
#         GROUP BY yazarlar.yazar_adi
#         ORDER BY AVG(kitaplar.puan) DESC
#     """
#     kitap.execute(sorgu)
#     save = kitap.fetchall()
#     print("\n--- YAZAR BAZLI ORTALAMA PUANLAR ---")
#     if not save:
#         print("[Hesaplanacak veri yok Lütfen önce kitap ekleyin]")
#         return
#     for i in save:
#         print(f"Yazar: {i} | Ortalama Puanı: {round(i[1], 2)}")
#     print("-" * 24)


# def kutuphane_toplamlari():
#     # COUNT(id) tüm kitapları sayar, SUM(sayfa_sayisi) tüm sayfaları toplar
#     sorgu = "SELECT COUNT(id), SUM(sayfa_sayisi) FROM kitaplar"
#     kitap.execute(sorgu)
#     sonuc = (kitap.fetchone())  # Tek satır özet döneceği için fetchone kullandık

#     print("\n--- KÜTÜPHANE GENEL TOPLAMLARI ---")
#     if sonuc[0] == 0:
#         print("[Kütüphane bomboş, sayılacak veri yok!]")
#         return

#     print(f"Kütüphanedeki Toplam Kitap Sayısı (COUNT): {sonuc[0]}")
#     print(f"Okunan Toplam Sayfa Sayısı (SUM): {sonuc[1]}")
#     print("-" * 24)


# def chois():
#     temizle_ve_olustur()

#     while True:
#         print("\n1.ekle")
#         print("2.bul")
#         print("3.listele")
#         print("4.yazar istatistikleri (AVG)")
#         print("5.genel toplamlar (COUNT ve SUM)")
#         print("6.cik")

#         try:
#             numper = int(input("enter your chois: "))
#             if numper == 1:
#                 insert()
#             elif numper == 2:
#                 bul()
#             elif numper == 3:
#                 sirala()
#             elif numper == 4:
#                 yazar_puan_ortalamalari()
#             elif numper == 5:
#                 kutuphane_toplamlari()
#             elif numper == 6:
#                 print("Programdan çıkılıyor, iyi günler!")
#                 break
#             else:
#                 print(
#                     "Lütfen 1, 2, 3, 4, 5 veya 6 sayılarından birini girin."
#                 )
#         except ValueError:
#             print(
#                 "\n HATA: Geçersiz bir karakter girdiniz Lütfen sadece SAYI girin."
#             )

# try:
#     chois()
# finally:
#     con.close()


# from sqlalchemy.orm import declarative_base , sessionmaker
# from sqlalchemy import create_engine , Column , String , Integer

# engine = create_engine("sqlite:///okul.db") 

# base = declarative_base()
# # Bir oturum fabrikası kuruyoruz ve bunu motorumuza (veri tabanımıza) bağlıyoruz


# class Ogrenci(base):
#     __tablename__ = "ogrenciler"
#     id = Column(Integer,primary_key = True)
#     isim = Column(String)
#     numara = Column(Integer)
# base.metadata.create_all(engine) 

# Session = sessionmaker(bind=engine)

# # Gerçek sepetimizi açıyoruz. Artık tüm işlemleri "oturum" üzerinden yapacağız.
# oturum = Session()
# # Yeni bir öğrenci nesnesi oluşturduk

# yeni_ogrenci = Ogrenci(isim="ekrem",numara=458)

# # oturum.add(yeni_ogrenci)
# # oturum.commit()

# tum_ogrenciler = oturum.query(Ogrenci).all()
# for i in tum_ogrenciler:
#     print(f"İD : {i.id} - numara : {i.numara} -  isim : {i.isim}")

# print("\n--- ÖZEL FİLTRELEME SONUCU ---")
# # Notu 95 olan ilk öğrenciyi bulalım
# yuksek_notlu = oturum.query(Ogrenci).filter(Ogrenci.numara > 555).all()
# for ogr in yuksek_notlu:
#     print(f"Numarası 500'den büyük olan: {ogr.isim} - Numarası: {ogr.numara}")

# adnan = oturum.query(Ogrenci).filter_by(isim="adnan").first()
# if adnan:
#     adnan.numara = 415
#     oturum.commit()
# sil = oturum.query(Ogrenci).filter_by(isim="ekrem").first()

# if sil:
#     oturum.delete(sil)
#     oturum.commit()
# oturum.close()



# from sqlalchemy.orm import declarative_base , sessionmaker
# from sqlalchemy import create_engine , Column , Integer , String

# BAĞLANTI_LINKI = "postgresql://postgres:who._is_Adnan@localhost:5432/kutuphane_db"
# enginer = create_engine(BAĞLANTI_LINKI)

# base = declarative_base()
# class Kitap(base):
#     __tablename__ = "Kitap"
#     id = Column(Integer,primary_key = True)
#     kitap_adi = Column(String)
#     yazar = Column(String)
#     sayfa_sayisi = Column(Integer)
# base.metadata.create_all(enginer)

# session = sessionmaker(bind=enginer)

# işlemler = session()
# kişi = Kitap(kitap_adi = "kara",yazar = "adnan", sayfa_sayisi = 45)
# kişi1 = Kitap(kitap_adi = "orta",yazar = "oku", sayfa_sayisi = 451)
# kişi2 = Kitap(kitap_adi = "boyraz",yazar = "tıkom", sayfa_sayisi = 268)
# # işlemler.add(kişi)
# # işlemler.add(kişi1)
# # işlemler.add(kişi2)
# # işlemler.commit()

# kitap_ = işlemler.query(Kitap).filter(Kitap.sayfa_sayisi > 200).all()
# print("------- sayfa sayisi 200 den buyuk olanlar--------")
# for i in kitap_:
#     print(f"kitap {i.kitap_adi} , {i.sayfa_sayisi} sayfa sayisina sahiptir.")

# degiştir = işlemler.query(Kitap).filter_by(yazar="adnan").first()
# if degiştir:
#     degiştir.yazar = "zeynep"
#     işlemler.commit()
# sil = işlemler.query(Kitap).filter_by(yazar="oku").first()
# if sil:
#     işlemler.delete(sil)
#     işlemler.commit()
# işlemler.close()
    




import sqlite3

con = sqlite3.Connection("yeni_projem.db")
kaydet = con.cursor()
def kaydet_ve_sil():
    kaydet.execute("DROP TABLE IF  EXISTS bilgiler")
    kaydet.execute("CREATE TABLE IF NOT EXISTS bilgiler (id INTEGER PRIMARY KEY AUTOINCREMENT , ogrenci TXT , ders TXT , notun INT) ")
    con.commit()
def ekle():
    while True:
        try:
            ogrenci = input("ogrenci ad: ")
            ders = input("ders ad: ")
            notun = int(input("notunu giriniz: "))
            break
        except ValueError:
            print("HATA: lutfen dogu yer dogru parametre giriniz !!!")
            continue
    kaydet.execute("INSERT INTO bilgiler (ogrenci , ders , notun) VALUES(?,?,?)",(ogrenci,ders,notun))
    con.commit()
    print("hersey kaydedildi !!!")
def oku():
    secim = input("hepsini (h) , belirli kişi adi : ")
    if secim == "h":
        kaydet.execute("SELECT * FROM bilgiler")
        goster = kaydet.fetchall()
        for i in goster:
            print(f"id: {i[0]} , ogrenci: {i[1]} , ders: {i[2]} , notun: {i[3]} ")
    else:
        kaydet.execute("SELECT * FROM bilgiler WHERE ogrenci = ?",(secim,))
        goster = kaydet.fetchall()
        if goster:
            for i in goster:
                print(i)
            return
        else:
            print(f"{secim} adli ogrenci yok")
def guncelle():
    try:
        guncele = input("degiştirmek isedigin ogrenci adini yazinz: ")
        yeni_not = int(input("yeni notu gir : "))
        kaydet.execute("UPDATE bilgler SET ogrenci = ? where notun = ? ",(guncele,))
        print("Guncellendi.")
    except :
        print("HATA: girdiginz ogrenci ismi mevcut degildir.")
def sil():
    try :
        silmek = input("silmek istedign kişi adini yaziniz: ")
        kaydet.execute("DELETE FROM bilgiler where ogrenci = ?",(silmek,))
        print("basari ile kaydedildi.")
    except :
        print("HATA: girdiginz ogrenci ismi mevcut degildir.")

def chois():
    kaydet_ve_sil()
    while True:
        print("\n1.ekle")
        print("2.oku")
        print("3.guncele")
        print("4.sil")
        print("5.cik")

        try:
            numper = int(input("enter your chois: "))
            if numper == 1:ekle()
            elif numper == 2:oku()
            elif numper == 3:guncelle()               
            elif numper == 4:sil()     
            elif numper == 5:             
                print("Programdan çıkılıyor, iyi günler!")
                break
            else:
                print(
                    "Lütfen 1, 2, 3, 4, 5 veya 6 sayılarından birini girin."
                )
        except ValueError:
            print(
                "\n HATA: Geçersiz bir karakter girdiniz Lütfen sadece SAYI girin."
            )

try:
    chois()
finally:
    con.close()

    
