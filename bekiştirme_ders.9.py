# ==============================================================================
# 🗺️ KONUM VE GEZİNTİ KOMUTLARI
# ==============================================================================

# 📍 1. pwd (Print Working Directory)
# Kısaca: "Ben neredeyim?" komutu.
# Fare Karşılığı: Klasörün en üstündeki uzun adres çubuğuna bakmak.
# Not: Terminalde kaybolursan o an hangi klasörde olduğunu söyler.

# 👁️ 2. ls (List)
# Kısaca: "Bu klasörde ne var?" komutu.
# Fare Karşılığı: Bir klasörün içine gözünle bakmak.
# Not: İçerideki tüm dosya ve klasörleri ekrana listeler.

# 🚶 3. cd (Change Directory)
# Kısaca: "Klasör değiştir" komutu.
# Fare Karşılığı: Klasöre çift tıklayıp girmek veya geri okuna basıp çıkmak.
# Kritik Kullanımlar:
# cd klasor_adi  -> O klasörün içine girer.
# cd ..          -> Bir üst klasöre (geri) çıkar.


# ==============================================================================
# 🛠️ DOSYA VE KLASÖR YÖNETİMİ
# ==============================================================================

# 📁 4. mkdir (Make Directory)
# Kısaca: "Yeni klasör aç" komutu.
# Fare Karşılığı: Boş yere sağ tıklayıp Yeni -> Klasör demek.
# Not: Yanına yazdığın isimde boş bir klasör oluşturur.

# 🧹 5. rm (Remove)
# Kısaca: "Kalıcı olarak sil" komutu.
# Fare Karşılığı: Shift + Delete yapmak (Çöp kutusuna gitmez, direkt yok olur!).
# Kritik Kullanımlar:
# rm dosya.txt       -> Dosyayı siler.
# rm -r klasor_adi   -> Klasörü ve içindeki her şeyi komple siler.

# 📄 6. cp (Copy)
# Kısaca: "Kopyala - Yapıştır" komutu.
# Fare Karşılığı: Dosyaya sağ tıklayıp Kopyala ardından Yapıştır demek.
# Not: Her zaman 2 isim ister: cp eski_dosya.txt yeni_kopya.txt

# 🚚 7. mv (Move)
# Kısaca: "Kes - Yapıştır" VEYA "Ad Değiştir" komutu.
# Fare Karşılığı: Dosyayı tutup başka klasöre taşımak VEYA sağ tıklayıp Yeniden Adlandır demek.
# Kritik Kullanımlar:
# mv dosya.txt klasor/  -> Dosyayı klasörün içine taşır.
# mv eski.txt yeni.txt    -> Dosyanın ismini değiştirir.


# ==============================================================================
# 👁️ İÇERİK OKUMA KOMUTLARI
# ==============================================================================

# 🐱 8. cat (Concatenate)
# Kısaca: "Dosya içine hızlıca bak" komutu.
# Fare Karşılığı: Dosyayı Not Defteri ile açıp, okuyup hemen kapatmak.
# Not: Dosyanın içindeki tüm yazıyı direkt terminal ekranına fırlatır. Küçük dosyalar içindir.

# 📄 9. less
# Kısaca: "Büyük dosyaları sayfa sayfa oku" komutu.
# Fare Karşılığı: Uzun bir dosyayı fare tekerleğiyle kaydırarak okumak.
# Not: Terminali kirletmez, okuma ekranı açar. Yön oklarıyla gezilir. q tuşuna basarak çıkılır.
# ==============================================================================


# ==============================================================================
# 🔐 DOSYA İZİNLERİ VE GÜVENLİK KOMUTLARI
# ==============================================================================

# Kural 1: İzin Türleri -> r (Okuma), w (Yazma), x (Çalıştırma)
# Kural 2: Kişiler     -> u (Sahibi), g (Grup), o (Yabancılar)

# 🔑 chmod (Change Mode)
# Kısaca: Dosyanın okuma, yazma, çalıştırma izinlerini değiştirir.
# Kritik Kullanımlar:
# chmod u+x adnan.py     -> Dosya sahibine çalıştırma (execute) yetkisi verir.
# chmod 755 adnan.py     -> Sahibe tam yetki (7), diğerlerine okuma/çalıştırma (5) verir.

# 👑 chown (Change Owner)
# Kısaca: Dosyanın sahibini (patronunu) değiştirir.
# Kritik Kullanım:
# chown ahmet adnan.py   -> Dosyanın sahipliğini "ahmet" kullanıcısına devreder.
# ==============================================================================


# ==============================================================================
# 📊 SÜREÇ YÖNETİMİ (PROCESS MANAGEMENT) KOMUTLARI
# ==============================================================================

# Kural: Her çalışan programın bir PID (Process ID) yani Kimlik Numarası vardır.

# 📋 1. ps (Process Status)
# Kısaca: Arka planda çalışan programları listeler.
# Kritik Kullanım:
# ps aux            -> Bilgisayardaki tüm gizli ve açık süreçleri detaylı listeler.

# 📊 2. top (Table of Processes)
# Kısaca: İşlemci ve RAM kullanımını canlı izleme ekranı açar.
# Not: Çok kasma yapan programları tespit etmek için kullanılır. "q" ile çıkılır.

# 🎯 3. kill
# Kısaca: Kimlik numarasını (PID) verdiğiniz programı zorla kapatır.
# Kritik Kullanımlar:
# kill 4512         -> 4512 PID numaralı programı kapatır.
# kill -9 4512      -> Kilitlenmiş programı acımadan, kesin olarak zorla kapatır.
# ==============================================================================



# ==============================================================================
# 🌐 SSH İLE UZAK SUNUCUYA BAĞLANMA (SECURE SHELL)
# ==============================================================================

# Mantık: Dünyanın başka yerindeki bir Linux bilgisayara terminalden bağlanıp yönetmek.
# Kural: Şifre yazarken güvenlik nedeniyle ekranda karakterler veya yıldızlar GÖZÜKMEZ.

# 🚀 En Temel Bağlantı Komutu:
# ssh kullanici_adi@ip_adresi -> Uzak sunucuya bağlantı tüneli açar.
# Örnek: ssh root@95.213.255.10

# 🚪 Sunucudan Çıkış Komutu:
# exit                        -> Uzak sunucu bağlantısını kapatır, eve döner.
# ==============================================================================


# ==============================================================================
# ⚙️ ORTAM DEĞİŞKENLERİ (ENVIRONMENT VARIABLES)
# ==============================================================================

# Mantık: İşletim sisteminin ve kodların ortak kullandığı küresel hafıza kutularıdır.
# Güvenlik: Şifreler ve gizli ayarlar kodun içine yazılmaz, buraya gizlenir.

# 👁️ 1. Değişken Değerini Okuma:
# echo $DEGISKEN_ADI       -> Değişkeni okumak için başına "$" işareti konur.
# Örnek: echo $USER        -> Aktif kullanıcı adını ekrana yazar.
# Örnek: echo $PATH        -> Sistemdeki programların kurulu olduğu yolları listeler.

# ✍️ 2. Yeni Değişken Tanımlama (Geçici):
# export ISIM="DEGER"      -> Hafızaya yeni bir bilgi kaydeder.
# Örnek: export SIFRE="123"
# ==============================================================================



# ==============================================================================
# 📜 BASH SCRIPT'LERE GİRİŞ (OTOMASYON)
# ==============================================================================

# Mantık: Birden fazla terminal komutunu bir dosyaya yazıp otomatik çalıştırmaktır.
# Dosya Uzantısı: .sh (Örn: yedekle.sh)

# 🚀 Bir Bash Script Nasıl Başlar?
# Dosyanın en ilk satırına "#!/bin/bash" yazılarak başlanır.

# 🏃 Çalıştırma Komutu:
# bash dosya_adi.sh      -> İçindeki tüm komutları sırayla jet hızında çalıştırır.
# ==============================================================================

print("TEBRİKLER! Bütün Linux ve Terminal rehberiniz eksiksiz kaydedildi.")
