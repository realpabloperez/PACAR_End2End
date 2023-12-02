import urllib.request
import json

url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100"

response = urllib.request.urlopen(url)

data = response.read().decode('UTF-8')

file = open("archivos/datos.json", "w")
file.write(data)

new_data = json.loads(data)
get_results = new_data['results']
new_data_results = json.dumps(get_results)