# Importing required libraries
from bs4 import BeautifulSoup
import requests
import json

# url = input('Please paste a MyAnimeList url for a voice actor')
url = 'https://myanimelist.net/people/8/Rie_Kugimiya'
headers_mobile = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'}
response = requests.get(url, headers = headers_mobile, timeout=5)
content = BeautifulSoup(response.content,"html.parser")

seiyuu = content.find('h1', attrs={'class':'title fs18 lh18'}).text
seiyuu = seiyuu.replace(', ','-')
fileName = '.\scraped-data\\' + seiyuu + '.json'

charList = []

for element in content.findAll('div', attrs={'class':'va-slider-item js-ajax-loading'}):

    charLink = element.find('a', attrs={'class':'img-link'}).get('href')
    charName = element.h3.text
    charFav = element.span.text
    if charFav[-1] == 's':
        charFav = charFav[:-5]
    else:
        charFav = charFav[:-4]

    charElement = {
    'name' : charName,
    'favs' : int(charFav),
    'link' : charLink
    }

    if charElement not in charList:
        charList.append(charElement)

print(f'{len(charList)} Characters found')

with open(fileName,'w') as outfile:
    json.dump(charList,outfile)
