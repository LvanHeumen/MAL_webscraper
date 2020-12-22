#TODO: Try pulling from mobile, saves having to send x additional requests.

# Importing required libraries
from bs4 import BeautifulSoup
import requests

url = 'https://myanimelist.net/people/8/Rie_Kugimiya'
headers_mobile = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'}
response = requests.get(url, headers = headers_mobile, timeout=5)
content = BeautifulSoup(response.content,"html.parser")

print(content.find('h1', attrs={'class':'title fs18 lh18'}).text)

charList = {}

for element in content.findAll('div', attrs={'class':'va-slider-item js-ajax-loading'}):
    charName = element.h3.text
    charFav = element.span.text
    if charFav[-1] == 's':
        charFav = charFav[:-5]
    else:
        charFav = charFav[:-4]

    if charName not in charList.keys():charList[charName] = int(charFav)

print(charList)
print(f'{len(charList)} Characters found')
