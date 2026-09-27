import sqlite3
import time
import random
import datetime

con = sqlite3.Connection("zaman_tarih.dp")
cursor=con.cursor()

def olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS zamanlama (zaman REAL, tarih TEXT, yazi TEXT , deger REAL)")

def ekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime("%Y-%m-%d %H:%M:%S"))
    yazi = "going"
    deger = random.randrange(1,30,3)
    cursor.execute("INSERT INTO zamanlama (zaman,tarih,yazi,deger) VALUES (?,?,?,?)",(zaman,tarih,yazi,deger))
    con.commit()

def al():
    cursor.execute("SELECT * FROM zamanlama where deger = 9.0")
    date=cursor.fetchall()
    for i in date:
        print(i)

def deger_sil():
    cursor.execute("SELECT * FROM zamanlama")
    date=cursor.fetchall()
    print("_-_"*19)

    for i in date:
        print(i)
    cursor.execute("UPDATE zamanlama SET yazi = ' adnan' WHERE yazi = 'going'")
    cursor.execute("SELECT * FROM zamanlama")
    con.commit()
    date=cursor.fetchall()
    print("_-_"*19)

    for i in date:
        print(i)
# deger_sil()

def deleted():
    cursor.execute("SELECT * FROM zamanlama")
    date=cursor.fetchall()
    print("_-_"*19)

    for i in date:
        print(i)
    cursor.execute("DELETE  FROM zamanlama WHERE deger = 2")
    con.commit()
    cursor.execute("SELECT * FROM zamanlama")
    date=cursor.fetchall()
    print("_-_"*19)

    for i in date:
        print(i,"\n")
 # --------------------------------------------------------------
def filtrele_ve_goster_where():
    """WHERE: Sadece degeri 10'dan büyük olan satırları filtreler."""
    cursor.execute("SELECT * FROM zamanlama WHERE deger > 10")
    data = cursor.fetchall()
    print("\n--- DEĞERİ 10'DAN BÜYÜK OLANLAR ---")
    for satir in data:
        print(satir)


def sirala_ve_goster_orderby():
    """ORDER BY: Verileri zamana göre en yeniden en eskiye doğru sıralar."""
    cursor.execute("SELECT * FROM zamanlama ORDER BY zaman DESC")
    data = cursor.fetchall()
    print("\n--- EN YENİDEN EN ESKİYE SIRALI ---")
    for satir in data:
        print(satir)


def sinirla_ve_goster_limit():
    """LIMIT: Tablodan sadece en güncel olan ilk 2 satırı getirir."""
    cursor.execute("SELECT * FROM zamanlama ORDER BY zaman DESC LIMIT 2")
    data = cursor.fetchall()
    print("\n--- EN GÜNCEL 2 SATIR ---")
    for satir in data:
        print(satir)




# def insert_ornek():
#     """INSERT: Kullanıcıdan alınan verilerle yeni bir yazar ekler.

#     (Daha önce virgül hatası yaptığın yer, burada düzeltildi).
#     """
#     yazar_adi = input("Eklenecek yazar adını giriniz: ")
#     # Yazım hatası olmaması için sonuna virgül ekledik
#     kitap.execute("INSERT INTO yazarlar (yazar_adi) VALUES(?)", (yazar_adi,))
#     con.commit()  # Kalıcı olması için commit şart!
#     print("Yeni yazar başarıyla eklendi.")


# def update_ornek():
#     """UPDATE: İsmi girilen kitabın puanını günceller.

#     Syntax hatası yapmamak için SET ve WHERE kalıpları düzgün kuruldu.
#     """
#     hedef_kitap = input("Puanını güncellemek istediğiniz kitabın adı: ")
#     yeni_puan = int(input("Yeni puanı giriniz (1-10): "))

#     # UPDATE tablo SET sütun = yeni_değer WHERE şart
#     kitap.execute(
#         "UPDATE kitaplar SET puan = ? WHERE kitap_adi = ?",
#         (yeni_puan, hedef_kitap),
#     )
#     con.commit()  # Değişikliği kaydet
#     print(f"'{hedef_kitap}' isimli kitabın puanı {yeni_puan} olarak güncellendi.")


# def delete_ornek():
#     """DELETE: İsmi girilen kitabı tablodan kalıcı olarak siler.

#     Eğer WHERE yazmazsanız tablodaki TÜM kitaplar silinir (Büyük Mantık Hatası!).
#     """
#     silinecek_kitap = input("Silmek istediğiniz kitabın adı: ")

#     # DELETE FROM tablo WHERE şart
#     kitap.execute(
#         "DELETE FROM kitaplar WHERE kitap_adi = ?", (silinecek_kitap,)
#     )
#     con.commit()  # Silme işlemini kaydet
#     print(f"'{silinecek_kitap}' isimli kitap başarıyla silindi.")





def inner_join_ornek():
    """INNER JOIN: Sadece siparişi olan müşterileri ve siparişlerini getirir.

    Eşleşmeyen satırlar tamamen elenir.
    """
    sorgu = """
        SELECT Musteriler.isim, Siparisler.urun 
        FROM Musteriler
        INNER JOIN Siparisler ON Musteriler.id = Siparisler.musteri_id
    """
    cursor.execute(sorgu)
    data = cursor.fetchall()
    print("--- INNER JOIN SONUÇLARI ---")
    for satir in data:
        print(satir)


def left_join_ornek():
    """LEFT JOIN: Sipariş vermiş olsun ya da olmasın TÜM müşterileri getirir.

    Eğer müşterinin siparişi yoksa, ürün kısmı 'None' (NULL) görünür.
    """
    sorgu = """
        SELECT Musteriler.isim, Siparisler.urun 
        FROM Musteriler
        LEFT JOIN Siparisler ON Musteriler.id = Siparisler.musteri_id
    """
    cursor.execute(sorgu)
    data = cursor.fetchall()
    print("\n--- LEFT JOIN SONUÇLARI ---")
    for satir in data:
        print(satir)


def right_join_alternatifi():
    """RIGHT JOIN Alternatifi (SQLite için):

    SQLite 'RIGHT JOIN' desteklemediği için tabloların yerini değiştirip
    LEFT JOIN kullanarak aynı mantığı yakalıyoruz.
    Müşterisi olmayan siparişler dahil TÜM siparişleri getirir.
    """
    sorgu = """
        SELECT Musteriler.isim, Siparisler.urun 
        FROM Siparisler
        LEFT JOIN Musteriler ON Siparisler.musteri_id = Musteriler.id
    """
    cursor.execute(sorgu)
    data = cursor.fetchall()
    print("\n--- RIGHT JOIN MUADİLİ SONUÇLAR ---")
    for satir in data:
        print(satir)


# # Fonksiyonları burada sırayla çağırıp test edebilirsin:
# filtrele_ve_goster_where()
# sirala_ve_goster_orderby()
# sinirla_ve_goster_limit()

# İşimiz bitince bağlantıyı kapatıyoruz
olustur()
con.close()