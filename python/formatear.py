import json
import os

with open("archivos/datos.json", "r") as file:
    data = json.load(file)

records = data.get("results", [])

output_directory = "output_json_files"
os.makedirs(output_directory, exist_ok=True)

for index, record in enumerate(records, start=1):
    output_filename = os.path.join(output_directory, f'record_{index}.json')
    with open(output_filename, 'w') as output_file:
        json.dump(record, output_file, indent=2)