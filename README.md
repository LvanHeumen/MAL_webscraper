# MAL_Webscraper
A web scraper meant to pull all voice acting roles a voice actor has and rank them by member favourites on MyAnimeList.net 
This scraper requests the mobile site for a MAL entry, as those can be scraped of the necessary data in a single request.

## How to use:
This webscraper has currently only been tested on Windows 10.  

### Initialising virtual environment:
This webscraper was built using BeautifulSoup and requests libraries. If those have not been installed, the virtual environment that has can be invoked through the command line by navigating to the folder that includes the scripts and running `scraper-env\Scripts\activate`.

### Running the scraper script:
The scripts run through the Windows command line. With the environment active, simply invoke `webscraper.py` to start scraping data.  
`webscraper.py` asks for a user's input once. In order to find which page to scrape, either a full MyAnimeList URL or the number in said URL has to be input. Either of these will work for example:
- https://myanimelist.net/people/185/Kana_Hanazawa
- 185

The data from the scraper is then saved to a subfolder called scraped-data.

### Running the parser script:
Once you have acquired some data through the scraper script, invoke `parsedata.py` in the command line to start parsing the data.  
It will scan a subfolder called `scraped-data` to look for the data that has been scraped. All available data-sets are then listed in the terminal, and the user is asked to select one of them.  
The script then displays the number of characters in the scraped data, and asks the user how many of the top characters they want to display.

The output is a list of the top characters in the terminal.


## Error messages:
As this script asks for user input, there are a few more possible errors that can occur besides the usual server-side errors.  
For `webscraper.py`:
- **Invalid URL.** This is caused by a faulty URL. Please ensure a proper MAL url or number is put in.
- **Exception, Not a Voice Actor.** This exception is returned if the linked page connects to the MAL servers but returns a page that doesn't have voice acting roles on it.

For `parsedata.py`:
- **IndexError** or **ValueError** when selecting the data-set. Ensure you are entering only the _number_ of the set you want to parse.
- (Warning) **Too many characters** when selecting the amount of characters to show. In order to prevent an IndexError, the value will be set to the max instead.


## Output file layout:
Each file returned by the webscraper has the following layout when saved:
```py
[{'name': 'char1', 'favs': 3432, 'link': 'myanimelist.net/....'}, {'name': 'char2', 'favs': 2323, 'link': 'myanimelist.net/....'}, {'name': ...} ... ]
```
The character name and favourites are used in the parser. The link to the character page is currently included for use in future developments.
