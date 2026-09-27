// for =       for(var a = 10 ; a < 51 ; a++) {
      //   console.log(a)
      // }

// while =       var a = 10 ;
//       while (a <= 50) {
//         console.log("///",a)
//         a +=5
//       }


/*******************************************************************************
 * 💡 EK DETAYLAR, GİZLİ KALMIŞ TUZAKLAR VE EN SIK KULLANILAN NOTLAR
 *******************************************************************************/

// =============================================================================
// let ve const İÇİN EK DETAY: SCOPE (KAPSAM) MANTIĞI
// =============================================================================
/*
   Mantık: Süslü parantezler { } birer odadır. 
   let ve const ile bir odanın içinde yaratılan değişken, odanın dışından okunamaz!
*/
{
    let odaIci = "Gizli Yazı";
    console.log(odaIci); // Bu oda içinde çalışır.
}
// console.log(odaIci); // ⚠️ TUZAK: "odaIci is not defined" hatası! Dışarıdan erişemezsiniz.


// =============================================================================
// VERİ TİPLERİ İÇİN EK DETAY: ARRAYS (DİZİLERDE SIK KULLANILANLAR)
// =============================================================================
/*
   Mantık: Dizilerdeki elemanları saymaya her zaman 0'dan başlarız.
*/
let arabalar = ["BMW", "Audi", "Tesla"];
console.log(arabalar[0]); // Çıktı: BMW (İlk eleman 0'dır, 1 değil!)

// Diziye yeni eleman ekleme (push):
arabalar.push("Fiat"); // Listenin en sonuna "Fiat" ekler.


// =============================================================================
// DOM İÇİN EK DETAY: classList.toggle() MANTIĞI
// =============================================================================
/*
   Mantık: toggle() komutu tam bir "ışık anahtarı" gibidir. 
   Varsa siler, yoksa ekler. Gece/Gündüz modu (Dark Mode) yaparken çok kullanılır.
*/
// document.body.classList.toggle("karanlik-tema"); 


// =============================================================================
// JSON İÇİN EK DETAY: JSON NEDEN ZORUNLUDUR?
// =============================================================================
/*
   Mantık: Bilgisayarlar arası internet trafiğinde sadece "düz metin (string)" taşınabilir.
   JavaScript nesnesini ({isim: "Mert"}) olduğu gibi kabloyla gönderemezsiniz. 
   Bu yüzden JSON.stringify ile metne çevirip göndeririz.
*/


// =============================================================================
// ASYNC / AWAIT İÇİN EK DETAY: try - catch MANTIĞI
// =============================================================================
/*
   Mantık: async/await kullanırken internet kesilirse kod tamamen donar ve çöker.
   Bunu engellemek için kodlarımızı try { ... } (Dene) bloğuna yazarız. 
   Hata çıkarsa catch { ... } (Yakala) bloğu devreye girer ve hatayı yumuşatır.
*/


// =============================================================================
// NODE.JS VE NPM İÇİN EK DETAY: package.json NEDİR?
// =============================================================================
/*
   Mantık: "npm init -y" yazdığınızda oluşan "package.json" dosyası, projenizin 
   alışveriş listesidir. İndirdiğiniz tüm dış paketlerin isimleri ve versiyonları 
   buraya yazılır. Başka bir yazılımcıya projenizi verirken node_modules klasörünü 
   silip sadece bu dosyayı verirsiniz. O kişi "npm install" yazarak listeyi otomatik indirir.
*/
