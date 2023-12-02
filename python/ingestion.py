import json
from pymongo import MongoClient 
import os

myclient = MongoClient("mongodb://root:example@localhost:27017/?authSource=admin")

base_de_datos = myclient.Valenbisi
collection = base_de_datos["Paradas de Valenbisi"]

i = 1
while True:
    file_path = f'output_json_files/record_{i}.json'
    if os.path.exists(file_path):
        with open(file_path) as file:
            file_data = json.load(file)
            
            if isinstance(file_data, list):
                collection.insert_many(file_data) 
            else:
                collection.insert_one(file_data)
                
        i += 1
    else:
        break


