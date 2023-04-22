import requests
import re
from bs4 import BeautifulSoup
from io import StringIO
from html.parser import HTMLParser
import json
import warnings
from tqdm import tqdm
warnings.filterwarnings("ignore")

URL ="https://www.nathdwara.in/mahaprabhu_baithakji.php"
page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "html.parser")

list = []
    # Get all the links from the main page and extract image and text from each link
for link in tqdm(soup.find_all('area')):
    if link.get('href') != "#":
        link = link.get('href')
        # print(link)
        # print("Processing Bethak " + link[:-4] + "\n")
        crouton = "https://www.nathdwara.in/" + link
        crouton = requests.get(crouton, verify=False)
        crouton = BeautifulSoup(crouton.content, "html.parser")
        gupt = False
        for line in (str(crouton)).splitlines():            
            if 'bethakji' in line:
                image = re.findall(r'"([^"]*)"', line)
                # image = "https://www.nathdwara.in/" + image[0]
                # print(list)
            if 'GUPT' in line:
                gupt = True

        # # download images
        # img_data = requests.get(image, verify=False).content
        # with open("./images/" + link[:-4] + '.gif', 'wb') as handler:
        #     handler.write(img_data)
        
        caption = ""
        # A lot of the text is not contained in paragraph tags, 
        # So if no text is found in paragraph then try to get any text containing "Vallabhacharya"
        matched_tags = crouton.find_all(lambda tag: len(tag.find_all()) == 0 and ("Vallabhacharya" in tag.text))
        for matched_tag in matched_tags:
            clean = re.sub('<[^<]+?>', '', str(matched_tag))
            caption += clean
        
        # caption = json.dumps(caption)
        bethak = {'name':link[:-4], 'url':link[:-4], 'gupt':gupt, "caption":caption}
        list.append(bethak)
         
json_bethak = (json.dumps(list, indent=2, default=str, ensure_ascii=True))
with open('baithakji_info.json', 'w', encoding='utf-8') as f:
    f.write(json_bethak)

