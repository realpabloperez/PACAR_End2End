import requests
import json

url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20"

response = requests.get(url)

if response.ok:
    response.json()

data = response.read().decode