# A scraper that pulls data from the mobile version of MyAnimeList Voice Actor pages

# Importing required libraries
import json
import os
import re
import requests

from bs4 import BeautifulSoup

class AnimeScraper():
    def __init__(self, url='https://myanimelist.net/people/8/Rie_Kugimiya'):
        self.url = url
        self.headers_mobile = {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36'}

        self.content = self.get_response()
        self.fileName = self.create_filename()
        self.charList = self.get_charlist()

    def get_response(self):
        response = requests.get(self.url, headers=self.headers_mobile, timeout=5)
        content = BeautifulSoup(response.content,'html.parser')

        if content.find('h2').text != 'Voice Acting Roles':
            raise Exception('Sorry, this is not a voice actor')
        else: print('Voice Actor found')

        return content

    def create_filename(self):
        seiyuu = self.content.find('h1', attrs={'class':'title fs18 lh18'}).text.replace(', ','-')
        fileName = os.path.join('.', 'scraped-data', f"{seiyuu}.json")

        return fileName


    def get_charlist(self):
        charList = []
        for element in self.content.findAll('div', attrs={'class':'va-slider-item js-ajax-loading'}):
            charLink = element.find('a', attrs={'class':'img-link'}).get('href')
            charName = element.h3.text
            charFavs = element.span.text
            numFavs = re.sub('\D','',charFavs)

            charElement = {
            'name': charName,
            'favs': int(numFavs),
            'link': charLink
            }

            if charElement not in charList:
                charList.append(charElement)

        return charList

    def save_charlist(self):
        with open(self.fileName,'w') as outfile:
            json.dump(self.charList,outfile)

if __name__ == '__main__':
    scraper = AnimeScraper()
    scraper.save_charlist()
