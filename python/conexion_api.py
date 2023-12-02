import urllib.request
import json
import time

def fetch_and_save_data():
    url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100"

    # Fetch data from the URL
    response = urllib.request.urlopen(url)
    data = response.read().decode('UTF-8')

    # Save the data to a file
    with open("archivos/datos.json", "w") as file:
        file.write(data)

    # Process the data if needed
    new_data = json.loads(data)
    get_results = new_data.get('results', [])
    new_data_results = json.dumps(get_results)
    # Add your processing logic here

# Run the script continuously with a 5-minute interval
while True:
    fetch_and_save_data()
    print("Data refreshed. Waiting for 5 minutes...")
    time.sleep(300)  # 300 seconds = 5 minutes