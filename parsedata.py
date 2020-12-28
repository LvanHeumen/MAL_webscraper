# Data parsing for the scraped data.

# Load relevant libraries
import json
import os

class DataParser:
    def __init__(self, fileName = '.\scraped-data\Kugimiya-Rie.json'):
        self.fileName = fileName

        self.dataScrape = self.load_sort()
        self.topNum = self.request_top()

    def load_sort(self):
        with open(self.fileName) as dataSource:
            dataScrape = json.load(dataSource)

        dataScrape.sort(key = lambda i:i['favs'], reverse=True)
        return dataScrape

    def request_top(self):
        print(f'This voice actor has {len(self.dataScrape)} characters.')
        topNum = int(input(f'How many of the top characters would you like to show?{os.linesep}'))
        if topNum > len(self.dataScrape):
            raise ValueError("Number exceeds length of character list.")
        return topNum

    def show_top(self):
        for x in range(self.topNum):
            print(f"Character #{x+1}: {self.dataScrape[x]['name']} with",
            f"{self.dataScrape[x]['favs']} favourites")

if __name__ == '__main__':
    parser = DataParser()
    parser.show_top()
