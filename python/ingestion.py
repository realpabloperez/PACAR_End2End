import json
from pymongo import MongoClient 

myclient = MongoClient("mongodb://root:example@localhost:27017/?authSource=admin")

base_de_datos = myclient.Valenbisi
collection = base_de_datos["Paradas de Valenbisi"]

with open('output_json_files/record_1.json') as file:
    file_data = json.load(file)
	
if isinstance(file_data, list):
    collection.insert_many(file_data) 
else:
    collection.insert_one(file_data)

