import json

with open('geo_json_final.json') as f1:
    geo_json = json.load(f1)

for item in geo_json['features']:
    # image = 
    # print(image)
    item['properties']['image'] = "images/" + item['properties']['image']

json_bethak = (json.dumps(geo_json, indent=2, default=str, ensure_ascii=True))
with open('geo_json_test.json', 'w', encoding='utf-8') as f:
    f.write(json_bethak)
