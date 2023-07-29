import requests
import json
import os

os.system("cls")

veriUrl = "http://api.open-notify.org/astros.json"
veriler = requests.get(veriUrl)

kisiSayisi = veriler.json()["number"]

print(f"Uzaydaki Kişi Sayısı: {kisiSayisi}")

for kisi in veriler.json()["people"]:
    print("Kişi Tam Adı: " + kisi["name"])