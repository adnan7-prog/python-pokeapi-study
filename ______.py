# import sqlite3

# # 1. VERİTABANI BAĞLANTISI VE DOSYA OLUŞTURMA
# con = sqlite3.Connection("okul_veritabani.db")
# cursor = con.cursor()

# # 2. 9, 10, 11 VE 12. SINIFLARDAN OLUŞAN 80 KİŞİLİK YENİ DEV LİSTE
# hazir_sinif_listesi = [
#     ("Adnan", "Sönmez", 582, "11-A", "Erkek"),
#     ("Meltem", "Aksoy", 104, "10-B", "Kız"),
#     ("Burak", "Yılmaz", 312, "9-A", "Erkek"),
#     ("Gamze", "Korkmaz", 425, "12-C", "Kız"),
#     ("Gökhan", "Öztürk", 201, "11-B", "Erkek"),
#     ("Gizem", "Aydın", 512, "10-A", "Kız"),
#     ("Volkan", "Demir", 118, "9-C", "Erkek"),
#     ("Büşra", "Çetin", 303, "12-B", "Kız"),
#     ("Serkan", "Yıldırım", 615, "11-A", "Erkek"),
#     ("Dilan", "Aslan", 142, "10-C", "Kız"),
#     ("Kaan", "Şahin", 255, "9-B", "Erkek"),
#     ("Ceren", "Yıldız", 490, "12-A", "Kız"),
#     ("Oğuz", "Polat", 333, "11-C", "Erkek"),
#     ("Seda", "Güneş", 217, "10-B", "Kız"),
#     ("Tuna", "Avcı", 501, "9-A", "Erkek"),
#     ("Eren", "Kaya", 701, "12-D", "Erkek"),
#     ("Celin", "Taş", 702, "11-D", "Kız"),
#     ("Mert", "Yurt", 703, "10-D", "Erkek"),
#     ("Ayla", "Bulut", 704, "9-D", "Kız"),
#     ("Arda", "Şen", 705, "12-D", "Erkek"),
#     ("Beyza", "Uçar", 115, "11-A", "Kız"),
#     ("Caner", "Öz", 222, "10-B", "Erkek"),
#     ("Damla", "Tekin", 345, "9-C", "Kız"),
#     ("Emre", "Yıldız", 412, "12-A", "Erkek"),
#     ("Füsun", 'Koç', 555, "11-B", "Kız"),
#     ("Hakan", "Sarı", 621, "10-C", "Erkek"),
#     ("Işıl", "Akar", 133, "9-A", "Kız"),
#     ("Levent", "Kartal", 244, "12-B", "Erkek"),
#     ("Mine", "Savaş", 366, "11-C", "Kız"),
#     ("Nihat", "Zengin", 477, "10-A", "Erkek"),
#     ("Oya", "Yücel", 588, "9-B", "Kız"),
#     ("Pınar", "Deniz", 699, "12-C", "Kız"),
#     ("Rıza", "Soylu", 188, "11-A", "Erkek"),
#     ("Sinem", "Yalçın", 299, "10-B", "Kız"),
#     ("Tolga", "Güler", 400, "9-C", "Erkek"),
#     ("Umut", "Yılmaz", 706, "12-D", "Erkek"),
#     ("Yağmur", "Çelik", 707, "11-D", "Kız"),
#     ("Zafer", "Korkut", 708, "10-D", "Erkek"),
#     ("Zehra", "Yıldırım", 709, "9-D", "Kız"),
#     ("Bora", "Arslan", 710, "12-D", "Erkek"),
#     ("Alper", "Gezer", 801, "11-E", "Erkek"),
#     ("Buse", "Yılmaz", 802, "10-E", "Kız"),
#     ("Cem", "Güneş", 803, "9-E", "Erkek"),
#     ("Deniz", "Soyer", 804, "12-E", "Kız"),
#     ("Ege", "Korkmaz", 805, "11-E", "Erkek"),
#     ("Feridun", "Yıldız", 806, "10-E", "Erkek"),
#     ("Gül", "Aslan", 807, "9-E", "Kız"),
#     ("Harun", "Demir", 808, "12-E", "Erkek"),
#     ("İrem", "Öztürk", 809, "11-E", "Kız"),
#     ("Kadir", "Çetin", 810, "10-E", "Erkek"),
#     ("Lale", "Aydın", 811, "9-E", "Kız"),
#     ("Murat", "Polat", 812, "12-E", "Erkek"),
#     ("Naz", "Şahin", 813, "11-E", "Kız"),
#     ("Onur", "Güler", 814, "10-E", "Erkek"),
#     ("Pelin", "Yücel", 815, "9-E", "Kız"),
#     ("Remzi", "Akar", 816, "12-E", "Erkek"),
#     ("Sude", "Tekin", 817, "11-E", "Kız"),
#     ("Tarık", "Koç", 818, "10-E", "Erkek"),
#     ("Ufuk", "Sarı", 819, "9-E", "Erkek"),
#     ("Vildan", "Zengin", 820, "12-E", "Kız"),
#     ("Okan", "Deniz", 513, "11-A", "Erkek"),
#     ("Ayşe", "Sönmez", 514, "10-A", "Kız"),
#     ("Fatma", "Aksoy", 223, "9-B", "Kız"),
#     ("Ali", "Yılmaz", 224, "12-B", "Erkek"),
#     ("Hüseyin", "Korkmaz", 346, "11-C", "Erkek"),
#     ("Zeliha", "Öztürk", 347, "10-C", "Kız"),
#     ("Osman", "Aydın", 711, "9-D", "Erkek"),
#     ("Hatice", "Demir", 712, "12-D", "Kız"),
#     ("Süleyman", "Çetin", 821, "11-E", "Erkek"),
#     ("Havva", "Yıldırım", 822, "10-E", "Kız"),
#     ("Yusuf", "Aslan", 515, "9-A", "Erkek"),
#     ("Meryem", "Şahin", 516, "12-A", "Kız"),
#     ("Mustafa", "Yıldız", 225, "11-B", "Erkek"),
#     ("Zeynep", "Polat", 226, "10-B", "Kız"),
#     ("Ömer", "Güneş", 348, "9-C", "Erkek"),
#     ("Asiye", "Avcı", 349, "12-C", "Kız"),
#     ("Halil", "Kaya", 713, "11-D", "Erkek"),
#     ("Emine", "Taş", 714, "10-D", "Kız"),
#     ("İbrahim", "Yurt", 823, "9-D", "Erkek"),
#     ("Fadime", 'Bulut', 824, "12-E", "Kız"),
# ]


# def tablo_olustur_ve_yukle():
#     """Eski tabloyu siler, yeni tabloyu oluşturur ve 80 yeni öğrenciyi yükler."""
#     cursor.execute("DROP TABLE IF EXISTS ogrenciler")
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS ogrenciler (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             isim TEXT,
#             soyisim TEXT,
#             okul_numarasi INTEGER,
#             sinif TEXT,
#             cinsiyet TEXT
#         )
#     """
#     )

#     cursor.executemany(
#         """
#         INSERT INTO ogrenciler (isim, soyisim, okul_numarasi, sinif, cinsiyet) 
#         VALUES (?, ?, ?, ?, ?)
#     """,
#         hazir_sinif_listesi,
#     )
#     # with yapısı kullandığımız için con.commit() satırlarına artık gerek kalmadı!


# def ogrencileri_listele():
#     """Yüklenen tüm öğrencileri ekrana basar."""
#     cursor.execute("SELECT * FROM ogrenciler")
#     veriler = cursor.fetchall()

#     print("\n--- 80 KİŞİLİK DEV OKUL LİSTESİ ---")
#     for No, isim, soyisim, numara, sinif, cinsiyet in veriler:
#         print(
#             f"Sıra: {No} | Numara: {numara} | {isim} {soyisim} | Sınıf: {sinif} | Cinsiyet: {cinsiyet}"
#         )
#     print("-" * 30)


# # ========================================================
# # KODU ÇALIŞTIRMA ALANI (with yapısıyla otomatik kapatma)
# # ========================================================
# with con:
#     tablo_olustur_ve_yukle()
#     ogrencileri_listele()

# print("\n Veritabanı başarıyla dolduruldu ve bağlantı otomatik kapatıldı.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine , Column , String , Integer

engine = create_engine("sqlite:///okul.db") 

base = declarative_base()

class Don(base):
    __tablename__ = "ogrenciler"
    id = Column(Integer,primary_key = True)
    numara = Column(Integer)
    isim = Column(String)
base.metadata.create_all(engine) 