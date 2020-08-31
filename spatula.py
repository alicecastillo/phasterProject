# main web scraper
# code guidance/syntax for scrape from: https://realpython.com/python-web-scraping-practical-introduction/

import settings
from urllib.request import urlopen




def init():
    #use settings.url
    print("Accessing NBCI website")
    accessWebPage(settings.url)


def accessWebPage(url):
    wp = urlopen(url)
    print("here")
    html_bytes = wp.read()
    html = html_bytes.decode("utf-8")
    print("decoding")
    print(html)