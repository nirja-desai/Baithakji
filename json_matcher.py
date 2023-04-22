import json
from fuzzywuzzy import fuzz

with open('baithakji.json') as f1:
    geo_json = json.load(f1)

with open('baithakji_info.json') as f2:
    info = json.load(f2)

name_dict = {item['name']: item['url'] for item in info}

# Define a function to perform fuzzy matching between two strings
def fuzzy_match(s1, s2):
    # Use the token sort ratio to calculate the fuzzy matching score
    return fuzz.token_sort_ratio(s1, s2)

counter = 0
for item in geo_json['features']:
    item['properties']['image'] = ""
    item['properties']['description'] = ""
    item['properties']['gupt'] = ""
    for object in info:
        name = object['name'].split("_")[0]
        geo_name = item['properties']['name'].split(" ")[0]
        geo_name = geo_name.lower()
        # print(geo_name)
        score = fuzzy_match(geo_name, name)
        # print(str(score))
        # print("The score for " + item['properties']['name'] + " and " + object['name'] + str(score))
        # item['properties']['image'] = ""
        if score >= 82:
            item['properties']['image'] = object['name'] + ".gif"
            item['properties']['description'] = object['caption']
            item['properties']['gupt'] = object['gupt']
            counter += 1
            
json_bethak = (json.dumps(geo_json, indent=2, default=str, ensure_ascii=True))
with open('geo_json_test.json', 'w', encoding='utf-8') as f:
    f.write(json_bethak)

print(str(counter) + " matches found")



    # matches = [(k, fuzzy_match(item['properties']['name'], k)) for k in name_dict.keys()]
    # matches.sort(key=lambda x: x[1], reverse=True)
    # if matches[0][1] >= 80:
    #     print(matches[0][1])
    #     name_dict[matches[0][0]]

    #     # If there is a match with a score of 80 or higher, add the image key-value pair to the matching object
    #     item['url'] = name_dict[matches[0][0]]
