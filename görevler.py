import tkinter as tk
import time
import os
adnan=tk.Tk()
adnan.state("zoomed")
girişler=tk.Frame(adnan)
girişler.place(x=10,y=10)
satir_kullanici = tk.Frame(girişler)
satir_kullanici.pack(anchor="w",pady=5)
şifre_giriş=tk.Frame(girişler)
şifre_giriş.pack(anchor="w",pady=5)
kulanici_ad=tk.Label(satir_kullanici,text="Kullanıcı Adı:",font=("Arial",20),bg="pink")
kulanici_ad.pack(side="left")
şifre_=tk.Label(şifre_giriş,text="Şifre:",font=("Arial",20),bg="pink")
şifre_.pack(side="left",ipadx=47)
kulanici=tk.Entry(satir_kullanici,font=("Arial",20))
kulanici.pack(side="left" ,padx=10)
sifre=tk.Entry(şifre_giriş,font=("Arial",20),show="*")
sifre.pack(padx=10)
deneme=3
giriş_deneme=3
def kaydol():
    global deneme
    kulanici_1=kulanici.get()
    sifre_1=sifre.get()
    if kulanici_1.strip() == "" or sifre_1.strip() =="" or len(kulanici_1) < 5 or len(sifre_1)< 5 or deneme<=0:
        deneme-=1
        if deneme<=0:
            satir_kullanici.pack_forget() 
            şifre_giriş.pack_forget()
            butonlar.place_forget()
            liste.place(x=0, y=0, relwidth=1, relheight=1)
            liste.config(text="3 Defa Hatalı Girdiniz!\nEkran Kilitlendi.", fg="red",bg="orange")
        else:
            return liste.config(text=f"lütfen tüm yerleri doldur veya 5'ten fazla gir\n { deneme} hakiniz kaldi")
           
    else:
        liste.config(text="     kayit başarili")
        with open("kulanicilar.txt","a",encoding="utf-8") as dosya:
            dosya.write(f"{kulanici_1},{sifre_1}\n")
def görevleri_listele_f():
    liste.place_forget()
    for widget in GörevEkleFrame.winfo_children():
        widget.destroy()
    if not os.path.exists("görevler.txt"):
        with open("görevler.txt", "w", encoding="utf-8") as f:
            f.write("")
    with open("görevler.txt", "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
    if len(satirlar) == 0 or (len(satirlar) == 1 and satirlar[0].strip() == ""):
        icerik = "henüz eklenmiş bir içerik yok."
    else:
        icerik = ""
        for satiranlam in satirlar:
            parcalar = satiranlam.strip().split(",")
            if len(parcalar) == 2:
                icerik += f"• Görev: {parcalar[0]} | Öncelik: {parcalar[1]}\n"
    görevleri_listesi = tk.Label(GörevEkleFrame, text=icerik, bg="pink", font=("Arial", 20), justify="left")
    görevleri_listesi.pack(pady=20, anchor="w")
görev_label=tk.Label(adnan,text="")
görev_label.pack()
GörevEkleFrame=tk.Frame()
GörevEkleFrame.place(x=400,y=50)
hata_label = None
başarılı_label = None
def görev_kaydet_f():
    global ekle_entry, ekle_entry_2, hata_label, başarılı_label
    if hata_label is not None:
        hata_label.destroy()
    if başarılı_label is not None:
        başarılı_label.destroy()
    görev_metni = ekle_entry.get().strip()
    öncelik_metni = ekle_entry_2.get().strip()
    if görev_metni == "":
        hata_label = tk.Label(GörevEkleFrame, text="Lütfen görev tanıtımını boş bırakmayın!", fg="red", font=("Arial", 14))
        hata_label.pack(pady=5)
        return
    with open("görevler.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{görev_metni},{öncelik_metni}\n")
    başarılı_label = tk.Label(GörevEkleFrame, text="Görev Başarıyla Kaydedildi! ✔", fg="green", font=("Arial", 16))
    başarılı_label.pack(pady=5)
    ekle_entry.delete(0, "end")
    ekle_entry_2.delete(0, "end")

def görev_ekle_f():
    global ekle_entry, ekle_entry_2
    görev_label.pack_forget()
    for widget in GörevEkleFrame.winfo_children():
        widget.destroy()
    görev_entry = tk.Frame(GörevEkleFrame)
    görev_entry.pack(pady=10)
    ekle = tk.Label(görev_entry, text="Görev tanıtımı: ", bg="skyblue", font=("Times", 20))
    ekle.pack(ipady=5, ipadx=125, side="left")
    ekle_entry = tk.Entry(görev_entry, bg="grey", fg="pink", font=("Arial", 20))
    ekle_entry.pack(ipady=5, ipadx=50, side="left", padx=10)
    görev_entry2 = tk.Frame(GörevEkleFrame)
    görev_entry2.pack(pady=10)
    eklem = tk.Label(görev_entry2, text="Öncelik Derecesi ('yüksek','orta','düşük'): ", bg="skyblue", font=("Times", 20))
    eklem.pack(ipady=5, ipadx=5, side="left")
    ekle_entry_2 = tk.Entry(görev_entry2, bg="grey", fg="pink", font=("Arial", 20))
    ekle_entry_2.pack(padx=10, ipady=5, ipadx=50, side="left")
    kaydet_btn = tk.Button(GörevEkleFrame, text="Görevleri Kaydet", bg="skyblue", activebackground="grey", font=("Arial", 20), command=görev_kaydet_f)
    kaydet_btn.pack(pady=15)

sil_hata_label = None
sil_başarılı_label = None

def görevi_dosyadan_sil_f():
    global sil_entry, sil_hata_label, sil_başarılı_label
    if sil_hata_label is not None:
        sil_hata_label.destroy()
    if sil_başarılı_label is not None:
        sil_başarılı_label.destroy()
    silinecek_isim = sil_entry.get().strip()
    if silinecek_isim == "":
        sil_hata_label = tk.Label(GörevEkleFrame, text="Lütfen silinecek görevin adını yazın!", fg="red", font=("Arial", 14))
        sil_hata_label.pack(pady=5)
        return
    with open("görevler.txt", "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
    yeni_satirlar = []
    görev_bulundu = False
    for satir in satirlar:
        parcalar = satir.strip().split(",")
        if len(parcalar) == 2:
            if parcalar[0] == silinecek_isim:
                görev_bulundu = True
            else:
                yeni_satirlar.append(satir)
    if görev_bulundu:
        with open("görevler.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(yeni_satirlar)
        sil_başarılı_label = tk.Label(GörevEkleFrame, text="Görev başarıyla silindi! ✔", fg="green", font=("Arial", 16))
        sil_başarılı_label.pack(pady=10)
    else:
        sil_hata_label = tk.Label(GörevEkleFrame, text="Böyle bir görev adı bulunamadı! ❌", fg="red", font=("Arial", 16))
        sil_hata_label.pack(pady=10)
    sil_entry.delete(0, "end")
def görev_sil_f():
    global sil_entry
    görev_label.pack_forget()
    for widget in GörevEkleFrame.winfo_children():
        widget.destroy()
    sil_frame = tk.Frame(GörevEkleFrame)
    sil_frame.pack(pady=20)
    sil_lbl = tk.Label(sil_frame, text="Silinecek Görev Adı: ", bg="skyblue", font=("Times", 20))
    sil_lbl.pack(ipady=5, ipadx=20, side="left")
    sil_entry = tk.Entry(sil_frame, bg="grey", fg="pink", font=("Arial", 20))
    sil_entry.pack(ipady=5, ipadx=50, side="left", padx=10)
    onay_btn = tk.Button(GörevEkleFrame, text="Görevi Sil", bg="skyblue", activebackground="grey", font=("Arial", 20), command=görevi_dosyadan_sil_f)
    onay_btn.pack(pady=15)   
    görev_label.pack_forget()
def çikiş_f():
    x=tk.Label(adnan,text="Hemen Çikiş Yabiliyor Efendi")
    x.pack()
    time.sleep(1)
    adnan.destroy()


def giriş_yap():
    global giriş_deneme
    if giriş_deneme<=0:
        return
    girilen_ad=kulanici.get()
    girilen_şifre=sifre.get()
    if  girilen_ad.strip() == "" or girilen_şifre.strip() =="":
        liste.config(text="lütfen tüm yerleri doldur veya 5'ten fazla gir")
        return
    giriş_başarili=False
    with open("kulanicilar.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            veriler=satir.strip().split(",")
            if len(veriler) == 2:
                dosyadaki_ad= veriler[0]
                dosyadaki_şifre= veriler[1]
                if girilen_ad.strip() == dosyadaki_ad and girilen_şifre.strip() == dosyadaki_şifre:
                    giriş_başarili=True
                    break
    if giriş_başarili :
        liste.place_forget()
        satir_kullanici.pack_forget() 
        şifre_giriş.pack_forget()
        butonlar.place_forget()
        seçenekler=tk.Frame()
        seçenekler.place(x=40,y=20)
        görevleri_listele=tk.Button(seçenekler,text="1.görevleri listele",bg="pink",activebackground="grey",font=("Times",30),command=görevleri_listele_f)
        görevleri_listele.pack(ipadx=18,ipady=25)
        görev_ekle=tk.Button(seçenekler,text="2.görev ekle",bg="pink",font=("Times",30),activebackground="grey",command=görev_ekle_f)
        görev_ekle.pack(ipadx=48,ipady=25,pady=25)
        görev_sil=tk.Button(seçenekler,text="3.görev sil",bg="pink",font=("Times",30),activebackground="grey",command=görev_sil_f)
        görev_sil.pack(ipadx=50,ipady=25)
        görev_çikiç=tk.Button(seçenekler,text="4.çikiş",bg="pink",font=("Times",30),activebackground="grey",command=çikiş_f)
        görev_çikiç.pack(ipadx=68,ipady=25,pady=25)

    else:
        giriş_deneme-=1
        if giriş_deneme<=0:
            satir_kullanici.pack_forget() 
            şifre_giriş.pack_forget()
            butonlar.place_forget()
            liste.place(x=0, y=0, relwidth=1, relheight=1)
            liste.config(text="3 Defa Hatalı Girdiniz!\nEkran Kilitlendi.", fg="red",bg="orange")
        else:
            liste.config(text=f"kulanici adi veya şifre yanliş,\n{giriş_deneme} hakiniz kaldi")
butonlar=tk.Frame(adnan)
butonlar.place(x=10,y=150)
kaydol_butonu= tk.Button(butonlar,text="Kaydol",bg="skyblue",activebackground="grey",font=("Arial",20),command=kaydol)
giris_yap_butonu= tk.Button(butonlar,text="Giriş Yap",bg="skyblue",activebackground="grey",font=("Arial",20),command=giriş_yap)
liste=tk.Label(adnan,text="",fg="black",font=("Arial",20))
liste.place(x=150,y=220)
kaydol_butonu.pack(side="left",padx=40)
giris_yap_butonu.pack(side="left")

adnan.mainloop()