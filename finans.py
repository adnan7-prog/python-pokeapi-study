
import time

# Listeleri en dışta (global) tanımlıyoruz ki diğer sayfalar da erişebilsin
gelirler = []
gelir_kategorileri = []

giderler = []
gider_kategorileri = []

def gelir_ekle():
    kategori = input("Gelir kategoriniz ne (Maaş, Freelance vb.): ").strip().capitalize()
    while True:
        try:
            maas = float(input("Ne kadar: "))
            break  
        except ValueError:
            print("Lütfen boş bırakmayın ve sadece sayısal bir değer giriniz!")

    gelirler.append(maas)
    gelir_kategorileri.append(kategori)
    print("Gelir kaydediliyor...")
    time.sleep(0.5)

def gider_ekle():
    kategori = input("Neye harcama yaptınız (Yemek, Fatura vb.): ").strip().capitalize()
    while True:
        try:
            gider_miktar = float(input("Ne kadar: "))
            break
        except ValueError:
            print("Lütfen boş bırakmayın ve sadece sayısal bir değer giriniz!")

    giderler.append(gider_miktar)
    gider_kategorileri.append(kategori)
    print("Gider kaydediliyor...")
    time.sleep(0.5)

def durum_raporu():
    toplam_gelir = sum(gelirler)
    toplam_gider = sum(giderler)
    bakiye = toplam_gelir - toplam_gider
    return toplam_gelir, toplam_gider, bakiye

def kategori_ozeti_hesapla():
    """Giderleri kategorilerine göre gruplayıp toplar (Sözlük kullanarak)"""
    ozet = {}
    # zip() fonksiyonu miktar ve kategoriyi eşleştirerek aynı anda döner
    for miktar, kat in zip(giderler, gider_kategorileri):
        if kat in ozet:
            ozet[kat] += miktar  # Kategori zaten varsa üstüne ekle
        else:
            ozet[kat] = miktar   # Kategori ilk defa geldiyse kaydet
    return ozet