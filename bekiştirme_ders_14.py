# bb6d2fe8fab7d744847dc17d app.exchangerate

#ac9a6ba708b7312869aa706ecb963b3d home.openweatherm




# # # # # # # # # 200 => OK
# # # # # # # # # 201 => CREATE 

# # # # # # # # # 400 => BAD REPUEST
# # # # # # # # # 401 => UNAUTHORİZED yrtkisiz
# # # # # # # # # 404 => NOT FOUND 

# # # # # # # # # 500 => INTERNAL SERVER ERROR
# import requests
# yanit = requests.get(
# "https://api.exchangerate-api.com/v4/latest/USD",
# timeout=5
# )
# veri = yanit.json()
# print(veri["rates"]["TRY"])


import requests

# new_url = "https://jsonplaceholder.typicode.com/users"
# my_url="https://jsonplaceholder.typicode.com/todos"
# result = requests.get(new_url)
# result = result.json()
# # for i in result:
# #     if (i["userId"] == 7):
# #         print(f"{i["id"]} - {i["title"]}")


# print(result[0]["name"], result[0]["email"], result[0]["address"]["suite"])



# api = "bb6d2fe8fab7d744847dc17d"
# bozduracak_birim = input("para birimine donustureceksınız : ")#bozduracak birim
# cikaracak = input("neye olacak : ")#alınacak birimi
# ne_kadar = int(input("ne kadar : "))
# url_get = f"https://v6.exchangerate-api.com/v6/bb6d2fe8fab7d744847dc17d/latest/{bozduracak_birim}"
# url = requests.get(url_get)
# url = url.json()
# how = ne_kadar*url["conversion_rates"][cikaracak]
# print(F"{how:.2f}")


# cek_url = "https://jsonplaceholder.typicode.com/posts"
# adan = {"userId" : 1,
#         "id" : 0,
#         "title" : "ben adnan oglu",
#         "body" : "uzun guzel erkek oyu7ncu gider gelir oyle"}
# # ekle = requests.post(cek_url,json=adan)
# ekle = requests.get(cek_url,timeout=5)
# ekle = ekle.json()

# # if ekle.status_code == 200:
#     # print("basari ile kaydedildi .")
#     # gelen_cevap = ekle.json() 
#     # print("Sunucudan Dönen Kayıtlı Veri:", gelen_cevap)
# cek = ekle[99]
# print(cek["userId"],cek["body"])




# ditto = "https://pokeapi.co/api/v2/pokemon/ditto"
# olustur = requests.get(ditto)
# olustur = olustur.json()
# x = olustur["abilities"]
# # print(f"adi : ditto \nboyu : {olustur['height']} \nkilosu {olustur["weight"]}")

# # for i in x:
#     # print(f'gucu {i["ability"]["name"]}')
    
# eleman_bulma = input("karakterin adini giriniz : ").lower()
# if eleman_bulma in olustur["name"]:
#     print(f"elamninizin kilosu: {olustur[eleman_bulma]["height"]} ,gucu : {olustur["ability"]["name"]} ")
# else :
#     print("olmadi")



# params = {
#     "title" : "uzun adamim",
#     "body" : "adnan kara dutun her yeri kırmızı",
#     "userId" : 8
# }
# cek = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
# print("cek: ",cek.status_code)



# hava = requests.get("https://api.open-meteo.com/v1/forecast?latitude=35&longitude=38&hourly=temperature_2m,wind_speed_10m",timeout=5)

# if hava.status_code == 200 :
#     hava = hava.json()

#     saatlik = hava["hourly"]
#     zamanlar = saatlik["time"]
#     sicaklik = saatlik["temperature_2m"]
#     toprak = saatlik["wind_speed_10m"]
#     print(f"eylem : {hava["latitude"]} , boylam : {hava["longitude"]} ")
#     print(f"zaman : {hava["timezone"]}")
#     for i in range(1):
#         print(f"sicaklik : {sicaklik[i]} , toprak sialik : {toprak[i]} , zaman {zamanlar[i]}")
# else :
#     print(f"bir hata oldu {hava.status_code}")





import requests 

url_base = "https://api.pokeapi.co/api/v2" 

def bul(name):

    birleştir = f"{url_base}/pokemon/{name}"
    get_url = requests.get(url=birleştir)
    
    if get_url.status_code == 200:
        karakter = get_url.json()
        print(f"✅ {name.upper()} Başarıyla Çekildi ({get_url.status_code})")
        print(f"Adı: {karakter['name']} | Boyu: {karakter['height']} | Kilosu: {karakter['weight']}")
        print("-" * 40)
    else:
        print(f" '{name}' aranırken bir sorun oluştu! Kod: {get_url.status_code}")
        print("-" * 40)

test_listesi = ["squirtle", "pikachu", "uydurma_pokemon", "gengar"]

print("Toplu Pokemon sorgusu başlatılıyor...\n")
for pokemon in test_listesi:
    bul(pokemon)
