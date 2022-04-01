import httpx
from bs4 import BeautifulSoup
import sys

HEADER = {
    'cache-control': 'no-cache',
    'connection': 'keep-alive'
}


try:
    sys.argv[1]
except:
    exit(0)

if 'http://' in str(sys.argv[1]) or 'https://' in str(sys.argv[1]):
    from sys import exit
    exit(0)
else:
    pass

class Alexa_Browser():
    def __init__(self):
        with httpx.Client(http2=True, headers=HEADER)as client:
            self.scraper = client.get(f"https://www.alexa.com/siteinfo/{sys.argv[1]}", headers=HEADER)
            self.contentscraper = self.scraper.text

    def AlexaRanking(self):
        content_scraped = self.contentscraper
        htmlsoup = BeautifulSoup(content_scraped,'html.parser')
        ranking = htmlsoup.find('p', class_="big data").prettify()
        rankstr = str(ranking).strip('')
        getem = rankstr.split('\n')
        return getem[4].strip(' ')
