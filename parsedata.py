# Data parsing for the scraped data.

# Load relevant libraries
import json
import logging
import os
import time

# Logger setup
logging.basicConfig(level=logging.INFO, filename='parser.log', filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')

# Class definition
class DataParser:
    def __init__(self, fileName = './scraped-data/Kugimiya-Rie.json'):
        logging.info('Class initialised')
        self.fileName = fileName

        self.dataScrape = self.load_sort()
        self.topNum = self.request_top()

    def load_sort(self):
        with open(self.fileName) as dataSource:
            dataScrape = json.load(dataSource)

        logging.info(f'Opened {self.fileName}')

        dataScrape.sort(key = lambda i:i['favs'], reverse=True)
        return dataScrape

    def request_top(self):
        print(f'This voice actor has {len(self.dataScrape)} characters.')
        topNum = int(input(f'How many of the top characters would you like to show?{os.linesep}'))
        if topNum > len(self.dataScrape):
            print(f'{topNum} is too many characters, setting to {len(self.dataScrape)} instead.')
            time.sleep(1)
            logging.warning('Selected number exceeded length, setting to max length')
            topNum = len(self.dataScrape)
        return topNum

    def show_top(self):
        for x in range(self.topNum):
            print(f"Character #{x+1}: {self.dataScrape[x]['name']} with",
            f"{self.dataScrape[x]['favs']} favourites")

# Top-level functions:
def select_data():                    # Selects dataset from among scraped sets
    scrapedPath = os.path.join('.', 'scraped-data')
    scrapedList = []

    for file in os.listdir(scrapedPath):
        if file.endswith('.json'):
            scrapedList.append(file)

    print(f'{len(scrapedList)} data sets found:')
    for i in range(len(scrapedList)):
        print(f'{i+1}: {scrapedList[i].replace(".json","").replace("-"," ")}')

    setNum = int(input(f'Which data set would you like to use? {os.linesep}'))
    chosenData = os.path.join(scrapedPath,scrapedList[setNum-1])

    return chosenData

if __name__ == '__main__':
    toParse = select_data()
    parser = DataParser(toParse)
    parser.show_top()
