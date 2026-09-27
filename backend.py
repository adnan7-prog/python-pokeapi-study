# backend_proje.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. VERİ TABANI SİMÜLASYONU (Gerçekte SQL veri tabanından gelir)
URUN_DEPOSU = {
    "1": {"ad": "Kablosuz Kulaklık", "fiyat": 1500.0, "stok": 5},
    "2": {"ad": "Oyuncu Mouse", "fiyat": 800.0, "stok": 0}, # Stokta yok!
    "3": {"ad": "Mekanik Klavye", "fiyat": 2200.0, "stok": 12}
}

GECERLI_KUPONLAR = {
    "YAZILIMCI20": 0.20,  # %20 indirim sağlar
    "PYTHON10": 0.10      # %10 indirim sağlar
}

# 2. BACKEND ROTASI: Siparişi İşleme Alan Fonksiyon
@app.route('/api/siparis-ver', methods=['POST'])
def siparis_ver():
    # Frontend'den gelen ham veriyi (JSON paketini) havada yakalıyoruz
    veri = request.get_json()
    
    urun_id = veri.get("urun_id")
    adet = veri.get("adet", 1)
    kupon_kodu = veri.get("kupon")

    # KONTROL 1: Ürün bizim veri tabanımızda var mı?
    if urun_id not in URUN_DEPOSU:
        return jsonify({"hata": "Ürün bulunamadı!"}), 404

    urun = URUN_DEPOSU[urun_id]

    # KONTROL 2: Stok yeterli mi?
    if urun["stok"] < adet:
        return jsonify({"hata": f"Yetersiz stok! Mevcut stok: {urun['stok']}"}), 400

    # MATEMATİKSEL HESAPLAMA: Toplam Fiyat
    toplam_fiyat = urun["fiyat"] * adet

    # KONTROL 3: İndirim Kuponu Geçerli mi?
    indirim_orani = 0
    if kupon_kodu:
        if kupon_kodu in GECERLI_KUPONLAR:
            indirim_orani = GECERLI_KUPONLAR[kupon_kodu]
            toplam_fiyat = toplam_fiyat * (1 - indirim_orani)
        else:
            return jsonify({"hata": "Geçersiz veya süresi dolmuş kupon!"}), 400

    # VERİ GÜNCELLEME: Sipariş onaylandığı için stoktan düşüyoruz
    urun["stok"] -= adet

    # RESPONSIVE MESAJ: Frontend'e (arayüze) durum raporu dönüyoruz
    return jsonify({
        "durum": "Başarılı",
        "mesaj": "Siparişiniz başarıyla alındı ve onaylandı.",
        "detay": {
            "urun_adi": urun["ad"],
            "adet": adet,
            "uygulanan_indirim": f"%{int(indirim_orani * 100)}",
            "odenecek_tutar": f"{toplam_fiyat} TL",
            "kalan_stok": urun["stok"]
        }
    }), 200

if __name__ == '__main__':
    # Sunucuyu yerelde (lokalde) başlatıyoruz
    app.run(debug=True, port=5000)
