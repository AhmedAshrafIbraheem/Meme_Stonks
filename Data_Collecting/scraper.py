# SlamStonks
# initial practice with requests and didn't end up using beautifulsoup
# Pardon my formatting: I'm new to Python and it's expectations :D
# THERE IS ALMOST NO ERROR CHECKING/HANDLING!!!

import requests             # pulls html
import re                   # regular expressions

def scraper():
    # requests will use .get() to pull from marketwatch.com
    r = requests.get('http://www.marketwatch.com/tools/screener/short-interest')
    # r.raise_for_status() # will return error if http isn't up

    # saving scraped data into a local file
    open('market_watch_scrape.html', 'wb').write(r.content)

    top_10_stocks = []  # keeping out of with's scope below

    # opening file read-only mode and move through it line by line
    with open("market_watch_scrape.html", "rt") as saved_file:
        current_line = saved_file.readline()

        counter = 0  # will be used to jump out of the loop early

        while current_line and counter < 10:
            none_or_match = re.search("<div class=\"cell__content\">[A-Z]{3,5}</div>", current_line)

            if none_or_match is not None:
                temp_string = re.search("[A-Z]{3,5}", none_or_match.group(0))  # pulls string from match object
                top_10_stocks.append(temp_string.group(0))
                counter += 1

            current_line = saved_file.readline()

    return top_10_stocks
# END scraper.py
