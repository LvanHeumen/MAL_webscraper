#TODO: Try pulling from mobile, saves having to send x additional requests.

# Importing required libraries
from bs4 import BeautifulSoup
import requests

url = 'https://myanimelist.net/people/8/Rie_Kugimiya'
headers_mobile = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'}
response = requests.get(url, headers = headers_mobile, timeout=5)
content = BeautifulSoup(response.content,"html.parser")

for element in content.findAll('div', attrs={'class':'va-slider-item js-ajax-loading'}):
    charName = element.h3.text
    charFav = element.span.text

    print(f'Character name: {charName}, Character favourites: {charFav}')


'''
charlist = {}
# This uses the desktop site, it's easier to index for the mobile site.
for character in content.findAll('h3', attrs={"class":"h3_character_name"}):
    charname = character.text
    charlink = character.find('a').get('href')
    if charname not in charlist.keys():
        charlist[charname] = charlink

print(charlist)
print(f'{len(charlist)} Characters found')
'''
