import requests
from bs4 import BeautifulSoup
import json

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

website = "www.stockx.com "
search_term = input("What is the name of the shoe? ")

query = website + search_term

url_variable = ''

for url in search(query, tld="com", num=1, stop=1, pause=1): 
    url_variable = url
    
#----------------------------------------------------------------------#

headers = {
    'pragma': 'no-cache',
    'x-app-hostname': 'https://stockx.com/',
    'dnt': '1',
    'x-app-version': '20190611t171116',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,mt;q=0.5',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'accept': 'application/json',
    'cache-control': 'no-cache',
    'authority': 'www.stockx.com',
    'referer': 'https://stockx.com/',
}

webpage_response = requests.get(str(url_variable), headers=headers)

webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")

data = (soup.find_all('script', type='application/ld+json'))
data2 = data[4]

get_json1 = json.loads(data2.text)
print(" ")
print(get_json1['name'])
print("Release Date: " + str(get_json1['releaseDate']))
print(" ")
get_json2 = json.loads(data2.text)['offers']['offers']

try:
    for x in range(20):
        print("Price: $" + str(get_json2[x]['price']), "Size: " + str(get_json2[x]['description']))
except:
    print("End of Script")


