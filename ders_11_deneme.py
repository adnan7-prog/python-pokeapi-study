import sqlite3

con = sqlite3.Connection("kutuphane.db")
kitap = con.cursor()


def temizle_ve_olustur():
    kitap.execute("DROP TABLE IF EXISTS kitaplar")
    kitap.execute("DROP TABLE IF EXISTS yazarlar")
    kitap.execute("CREATE TABLE IF NOT EXISTS kitaplar (id INTEGER PRIMARY KEY AUTOINCREMENT, kitap_adi TEXT, sayfa_sayisi INT, puan INT, yazar_id INT)")
    kitap.execute("CREATE TABLE IF NOT EXISTS yazarlar (id INTEGER PRIMARY KEY AUTOINCREMENT, yazar_adi TEXT)")
    con.commit()


def insert():
    print("\n--- YENİ YAZAR VE KİTAP EKLEME ---")
    yazar_adi = input("Yazar adını giriniz: ")
    kitap.execute("INSERT INTO yazarlar (yazar_adi) VALUES(?)", (yazar_adi,))
    con.commit()
    son_yazar_id = kitap.lastrowid
    kitap_adi = input("Kitap adını yazınız: ")
    sayfa_sayisi = int(input("Sayfa sayısını giriniz: "))
    puan = int(input("Verdiğiniz puan (1-10): "))

    kitap.execute(
        "INSERT INTO kitaplar (kitap_adi, sayfa_sayisi, puan, yazar_id) VALUES(?,?,?,?)",
        (kitap_adi, sayfa_sayisi, puan, son_yazar_id),)
    con.commit()
    print(" Veri başarıyla kaydedildi!\n" + "-" * 24)


def bul():
    print("\n--- KİTAP ARA ---")
    aranan = input("Aramak istediğiniz kitap adını girin: ")
    kitap.execute("SELECT * FROM kitaplar WHERE kitap_adi = ?", (aranan,))
    sonuclar = kitap.fetchall()

    if not sonuclar:
        print("Aradığınız kitap bulunamadı.")
    for satir in sonuclar:
        print(satir)
    print("-" * 24)


def sirala():
    sorgu = """
        SELECT kitaplar.id, kitaplar.kitap_adi, kitaplar.sayfa_sayisi, kitaplar.puan, yazarlar.yazar_adi 
        FROM kitaplar 
        INNER JOIN yazarlar ON kitaplar.yazar_id = yazarlar.id
    """
    kitap.execute(sorgu)
    save = kitap.fetchall()
    print("\n--- KİTAPLAR LİSTESİ ---")
    if not save:
        print("[Tablo şu an boş Lütfen önce 1'e basıp kitap ekleyin]")
        return
    for i in save:
        print(f"id: {i[0]}, kitap: {i[1]}, sayfa: {i[2]}, puan: {i[3]} , yazar_id: {i[4]}")
    print("-" * 24)


def chois():
    temizle_ve_olustur()

    while True:
        print("\n1.ekle")
        print("2.bul")
        print("3.listele")
        print("4.cik")
        try:
            numper = int(input("enter your chois: "))
            if numper == 1:
                insert()
            elif numper == 2:
                bul()
            elif numper == 3:
                sirala()
            elif numper == 4:
                print("Programdan çıkılıyor, iyi günler!")
                break
            else:
                print("Lütfen 1, 2, 3 veya 4 sayılarından birini girin.")
        except ValueError:
            print(
                "\n HATA: Geçersiz bir karakter girdiniz Lütfen sadece SAYI girin."
            )

try:
    chois()
finally:
    con.close()