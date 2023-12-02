import json
import os
from datetime import datetime

with open("archivos/datos.json", "r") as file:
    data = json.load(file)

records = data.get("results", [])

output_root_directory = "output_json_files"
os.makedirs(output_root_directory, exist_ok=True)

for index, record in enumerate(records, start=1):
    # Extract the timestamp from the 'updated_at' field, assuming it's in the format '02/12/2023 11:10:15'
    timestamp_str = record.get("updated_at", "")
    timestamp = datetime.strptime(timestamp_str, "%d/%m/%Y %H:%M:%S").strftime("%Y%m%d%H%M%S")

    # Create a directory with the date (e.g., 20231202) if it doesn't exist
    output_date_directory = os.path.join(output_root_directory, timestamp[:8])
    os.makedirs(output_date_directory, exist_ok=True)

    # Create a filename inside the date directory, e.g., record_20231202_1.json
    output_filename = os.path.join(output_date_directory, f'record_{timestamp}_{index}.json')

    with open(output_filename, 'w') as output_file:
        json.dump(record, output_file, indent=2)