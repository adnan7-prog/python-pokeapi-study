# class Deneme_yap:
#     def __init__(self,deger=int)->None:
#         self.veri=deger
#         self.sonraki=None
# one=Deneme_yap(40)
# two=Deneme_yap(80)
# three=Deneme_yap(120)                 LİNKED
# one.sonraki=two
# two.sonraki=three
# print("ilk int",one.veri)
# print("ilkten sonraki",one.sonraki.veri)
# print("ikinciden sonraki sey ",one.sonraki.sonraki.veri)


# tapaklar=[]
# tapaklar.append("kirmiz")
# tapaklar.append("turuncu")
# tapaklar.append("sari")               STACK
# print(tapaklar)
# tapaklar.pop()
# print(tapaklar)



# from collections import deque
# firin_=deque()
# firin_.append("adnan")
# firin_.append("kara")
# firin_.append("tiko")     FIFO
# for i in range(0,2):              DEqUE
#     print(firin_)
#     firin_.popleft()
# print(firin_)



# sayilar=[1,2,3,4,5,6,7,8,9]
# hedef=8
# solduvar=0
# sagduvar=len(sayilar) - 1
# while solduvar <= sagduvar:
#     orta_sayi=(solduvar + sagduvar) // 2
#     ortadaki_sayi=sayilar[orta_sayi]
#     if hedef == ortadaki_sayi:
#         print("sayi bulundu",ortadaki_sayi,"indexi: " ,orta_sayi)            Binary Search       
#         break
#     elif hedef <= ortadaki_sayi:
#         print("1::",ortadaki_sayi)
#         sagduvar = orta_sayi - 1
#     else:
#         print("2:: ",ortadaki_sayi)
#         solduvar = orta_sayi + 1


# Profesyonel ve hızlı kuyruk yapısı için kütüphanemizi çağırıyoruz
# from collections import deque

# print("=== 1. ADIM: ARRAY (DİZİ) MANTIĞI ===")
# # Raflardaki ürünler yan yana dizilmiştir. İndeksle erişim O(1) hızındadır.
# depo_raflari = ["Telefon", "Bilgisayar", "Kulaklık", "Saat"]
# # 2. indeksteki ürünü arıyoruz (Kulaklık)
# print(f"2 numaralı raftaki ürün: {depo_raflari[2]} (Erişim Hızı: O(1))")
# print("-" * 40)


# print("=== 2. ADIM: LINKED LIST (BAĞLI LİSTE) MANTIĞI ===")
# # Birbirine bağlanan kargo vagonları (Düğümler) oluşturuyoruz
# class Vagon:
#     def __init__(self, urun_adi):
#         self.urun = urun_adi
#         self.sonraki = None # Bir sonraki vagonun oku

# vagon1 = Vagon("Koli-A")
# vagon2 = Vagon("Koli-B")
# vagon1.sonraki = vagon2 # Vagonları bağladık: Koli-A -> Koli-B

# print(f"İlk vagon: {vagon1.urun}")
# print(f"İlk vagondan sonraki vagon: {vagon1.sonraki.urun} (Adres takibi yapıldı)")
# print("-" * 40)


# print("=== 3. ADIM: STACK (YIĞIN) MANTIĞI ===")
# # Üst üste dizilen kargo kutuları yığını (Son Gelen İlk Çıkar - LIFO)
# kargo_yigini = []
# kargo_yigini.append("Alt Kutu")
# kargo_yigini.append("Orta Kutu")
# kargo_yigini.append("En Üst Kutu") # En son bu geldi

# print(f"Mevcut koli yığını: {kargo_yigini}")
# # En üstteki kutuyu alıp kargoluyoruz (pop)
# kargolanan = kargo_yigini.pop()
# print(f"Banttan indirilen ve kargolanan kutu: {kargolanan} (Hız: O(1))")
# print(f"Yığında kalan kutular: {kargo_yigini}")
# print("-" * 40)


# print("=== 4. ADIM: QUEUE (KUYRUK) MANTIĞI ===")
# # Kapıdaki kargo kamyonları sırası (İlk Gelen İlk Çıkar - FIFO)
# # pop(0) yavaş olduğu için mülakat standardı olan 'deque' ve 'popleft' kullanıyoruz
# kamyon_kuyrugu = deque()
# kamyon_kuyrugu.append("1. Kamyon (Ahmet)") # İlk gelen
# kamyon_kuyrugu.append("2. Kamyon (Mehmet)")

# print(f"Kapıdaki kamyon sırası: {list(kamyon_kuyrugu)}")
# # İlk gelen kamyon yükünü aldı ve sıradan çıktı (popleft)
# giden_kamyon = kamyon_kuyrugu.popleft()
# print(f"Yükünü alıp sıradan ilk çıkan: {giden_kamyon} (Hız: O(1))")
# print(f"Kuyrukta bekleyen kalan kamyonlar: {list(kamyon_kuyrugu)}")


# class bir:
#     def __init__(self,veri:int) -> None:
#         self.veri=veri
#         self.sol=None
#         self.sag=None
# ilk_sayi=bir(84)

# sol=bir(10)
# sag=bir(70)

# ilk_sayi.sol=sol
# ilk_sayi.sag=sag 
# print("ilk sayi", ilk_sayi.veri)
# print("ilkten kucuk", ilk_sayi.sol.veri)
# print("ilkten buyuk",ilk_sayi.sag.veri)

        

# liste=[1,80,45,69,3]
 # sirala=sorted(liste)
# liste.sort()
# print(liste)

# def bul(dizi,hedef):
#     for i in range(len(dizi)):
#         if dizi[i] == hedef:
#             return "index ",i
#     return -1
# liste=[12,56,3,90,32,63]
# hedehim=3
# print(bul(liste,hedehim))


# def binary_search(dizi, hedef):
#     sol, sag = 0, len(dizi) - 1
#     while sol <= sag:
#         orta = (sol + sag) // 2
#         if dizi[orta] == hedef:
            
#             return orta
#         elif dizi[orta] < hedef:
#             sol = orta + 1
#         else:
#             sag = orta - 1
#     return -1
# liste=[12,43,67,5,86,3]
# print(binary_search(liste,86))

# def listeyi_dondur(liste):
#     uzunluk=len(liste)
#     for i in range(uzunluk):
#         for j in range(0,uzunluk - i - 1):
#             if liste[j] > liste[j + 1]:
#                 liste[j],liste[j + 1] = liste[j + 1] , liste[j]
#         print(f"adim {i+1} : {liste}")
#     return liste
# sayilar=[5,2,8,1,9]
# listeyi_dondur(sayilar)
    
# from collections import deque
# liste=deque()
# liste.append(16)
# liste.append(19)
# liste.append(1)
# print(liste)
# son_sil=liste.popleft()
# print("-",son_sil,liste)


# Quick Sort Örneği
def quick_sort(dizi):
    if len(dizi) <= 1:
        return dizi
    pivot = dizi[len(dizi) // 2]
    sol = [x for x in dizi if x < pivot]
    orta = [x for x in dizi if x == pivot]
    sag = [x for x in dizi if x > pivot]
    return quick_sort(sol) + orta + quick_sort(sag)

print("\n\nSıralı Dizi (Quick Sort):", quick_sort([3, 6, 8, 10, 1, 2, 1]))
