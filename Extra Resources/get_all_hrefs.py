import requests
import re
from bs4 import BeautifulSoup

class Spider:

    def __init__(self, startUrl, searchDepth, keyword):
        self.startUrl = startUrl
        self.searchDepth = searchDepth
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

    def changeUrl(self, url):
        self.startUrl = url

    def search(self):
        hrefs = self.getAllHrefs(self.startUrl)
        for href in hrefs:
           hrefs.extend(self.getAllHrefs(href))

    def getAllHrefs(self, startHref):
        print(startHref)
        data = requests.get(startHref, headers=self.headers)
        rawText = data.text
        soup = BeautifulSoup(rawText, 'lxml')
        data = soup.find_all('a', attrs={'href': re.compile("^http://")})
        data.extend(soup.find_all('a', attrs={'href': re.compile("^https://")}))
        data = [x.get('href') for x in data]

        return data

spider1 = Spider("http://sethgodin.typepad.com/seths_blog/", 1, "years")
spider1.search()
