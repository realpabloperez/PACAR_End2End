import collections
import json
with open('ejemplo.json') as data_file:
    data = json.load(data_file)
    for item in data['']:
        key = {"id": item['features']['id']}
        data = {"geo_type": item['features']['geo_type'],
                "location": item['features']['location'],
                "name": item['features']['name'],
                "primary_geo": item['features']['primary_geo'],
                "screen_name": item['features']['screen_name'],
                "tweets": item['features']['tweets']}
        collections.update(key, data, upsert=True)



