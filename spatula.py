# main web scraper
# code guidance/syntax for scrape from: https://realpython.com/python-web-scraping-practical-introduction/

import settings
from urllib.request import urlopen




def init():
    accessWebPage(settings.url)


def accessWebPage(url):
    wp = urlopen(url)
    html_bytes = wp.read()
    html = html_bytes.decode("utf-8")