# Data parsing for the scraped data.

# Load relevant libraries
import json

# With our test data open, dump the contents into an array of dictionaries
fileName = '.\scraped-data\Kugimiya-Rie.json'

with open(fileName) as dataSource:
    dataScrape = json.load(dataSource)

dataScrape.sort(key = lambda i:i['favs'], reverse=True)

print(f'This voice actor has {len(dataScrape)} characters.')
topNum = int(input('How many of the top characters would you like to show?\n'))

for x in range(topNum): print(f"Character #{x+1}: {dataScrape[x]['name']} with {dataScrape[x]['favs']} favourites.")
