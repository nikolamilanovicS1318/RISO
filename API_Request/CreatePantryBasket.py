import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/1bd818d0-6686-4d0d-bc30-7018a55e16c9/basket/NoviBasket"

ListaPredmeta = ["RISO", "C# programiranje", "SQL programiranje", "PWA"]
SerializableListaPredmeta = json.dumps(ListaPredmeta).replace('"', "")

class Kontakt:
    adresa = "Kneza Mihaila VI"
    mesto = "Beograd"
    telefon = "123456789"

KNT = Kontakt()

payload = json.dumps({
  "id": "St1318",
  "ime": "Ime",
  "prezime": "Prezime",
  "smer": "IT",
  "predmeti": SerializableListaPredmeta,
  "prosek": 8.5,
  "kontakt": [KNT.adresa, KNT.mesto, KNT.telefon]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(payload)
print(response.text)
