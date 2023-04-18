import requests
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

URL ="https://www.nathdwara.in/mahaprabhu_baithakji.php"
page = requests.get(URL)

print(page.text)pyth