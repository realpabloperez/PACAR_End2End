import urllib.request
import json

url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?"

response = urllib.request.urlopen(url)

data = response.read().decode('UTF-8')

file = open("archivos/datos.json", "w")
file.write(data)