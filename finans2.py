

# import sqlite3
# import time
# import random
# import datetime
# dosya=sqlite3.connect("işçi_gunleri.db")
# oluştur=dosya.cursor()

# def taplo_oluştur():
#     oluştur.execute("CREATE TABLE IF NOT EXISTS zamanlama( zaman REAL,tarih TEXT,değer TEXT)")
# def değerler():
#     zaman=time.time()
#     tarih=str(datetime.datetime.fromtimestamp(zaman).strftime("%y-%m-%d %H:%M:%S"))
#     değer="adnan"
#     oluştur.execute("INSERT INTO zamanlama (zaman,tarih,değer) VALUES(?,?,?) ",(zaman,tarih,değer))
#     dosya.commit()
# def değer_al():
#     oluştur.execute("SELECT * FROM zamanlama WHERE değer='adnan'")
#     data=oluştur.fetchall()
#     a=1
#     for i in data:
#         print(a,".",i)
#         a+=1
# değer_al()
# dosya.close()
import time
import finans as finans

print("..._ Finans Takip Sistemine Hoş Geldiniz _...")

while True:
    print("\n" + "="*30)
    while True:
        try:
            islem = input("1-Gelir Ekle\n2-Gider Ekle\n3-Rapor Göster\n4-Çıkış\nSeçiminiz (rakam olarak yazınız): ")
            print("="*30)
            break
        except:
            print("boş yada harf girmeyiniz.")
    
    if islem == "1":
        finans.gelir_ekle()
        
    elif islem == "2":
        finans.gider_ekle()
        
    elif islem == "3":
        # Birinci sayfadan hesaplama sonuçlarını alıyoruz
        top_gelir, top_gider, net_bakiye = finans.durum_raporu()
        
        print(f"\n--- GENEL DURUM RAPORU ---")
        print(f"Toplam Gelir: {top_gelir:.0f} TL")
        print(f"Toplam Gider: {top_gider:.0f} TL")
        print(f"Güncel Bakiyeniz: {net_bakiye:.0f} TL")
        
        # Kategori bazlı özet çıkarma fonksiyonunu çağırıyoruz
        gider_raporu = finans.kategori_ozeti_hesapla()
        
        print(f"\n--- KATEGORİ BAZLI HARCAMALARINIZ ---")
        if not gider_raporu:
            print("Henüz bir gider kaydı bulunmuyor.")
        else:
            for kat, miktar in gider_raporu.items():
                print(f"* {kat}: {miktar:.0f} TL")
                
        time.sleep(1)
        
    elif islem == "4":
        print("İyi günler dileriz! Verileriniz temizlendi.")
        break
        
    else:
        print("Geçersiz seçim! Lütfen menüdeki rakamlardan birini giriniz.")