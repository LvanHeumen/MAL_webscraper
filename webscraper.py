#TODO: Try pulling from mobile, saves having to send x additional requests.

# Importing required libraries
from bs4 import BeautifulSoup
import requests

url = 'https://myanimelist.net/people/8/Rie_Kugimiya'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content,"html.parser")

charlist = {}

for character in content.findAll('h3', attrs={"class":"h3_character_name"}):
    charname = character.text
    charlink = character.find('a').get('href')
    if charname not in charlist.keys():
        charlist[charname] = charlink

print(charlist)
print(f'{len(charlist)} Characters found')
