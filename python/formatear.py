import json
import os
from datetime import datetime

with open("archivos/datos.json", "r") as file:
    data = json.load(file)

records = data.get("results", [])

output_directory = "output_json_files"
os.makedirs(output_directory, exist_ok=True)

# Split the original JSON file into multiple smaller JSON files
for index, record in enumerate(records, start=1):
    # Extract the timestamp from the 'updated_at' field, assuming it's in the format '02/12/2023 11:10:15'
    timestamp_str = record.get("updated_at", "")
    timestamp = datetime.strptime(timestamp_str, "%d/%m/%Y %H:%M:%S").strftime("%Y%m%d%H%M%S")

    # Create a filename with the timestamp, e.g., record_20231202111015.json
    output_filename = os.path.join(output_directory, f'{index}_{timestamp}.json')

    # Save each record individually
    with open(output_filename, 'w') as output_file:
        json.dump(record, output_file, indent=2)

print(f"{len(records)} records have been split into individual JSON files.")