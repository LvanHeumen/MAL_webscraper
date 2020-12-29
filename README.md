# MAL_Webscraper
A web crawler meant to pull all voice acting roles a voice actor has and rank them by member favourites on MyAnimeList.net

## How to use:
This crawler has currently only been tested on Windows 10.  

### Initialising virtual environment:
This crawler was built using BeautifulSoup and requests libraries. If those have not been installed, the virtual environment that has can be invoked through the command line by navigating to the folder that includes the scripts and running `scraper-env\Scripts\activate`.

### Running the scripts:
The scripts run through the Windows command line. With the environment active, simply invoke `webscraper.py` to start scraping data.  
`webscraper.py` asks for a user's input once. In order to find which page to scrape, either a full MyAnimeList URL or the number in said URL has to be input. Either of these will work for example:
- https://myanimelist.net/people/185/Kana_Hanazawa
- 185

The data from the scraper is then saved to a subfolder called scraped-data.
