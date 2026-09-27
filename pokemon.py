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
