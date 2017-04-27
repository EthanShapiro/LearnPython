import requests
from bs4 import BeautifulSoup


def cPlusPlusSpider(maxPages):
    page = 1
    while page <= maxPages:
        url = "https://thenewboston.com/forum/category.php?id=44&orderby=recent&page=" + str(page)
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('a', {'class': "title text-semibold"}):
            href = link.get('href')
            title = link.string
            # print(href)
            # print(str(title).strip())
            getPeopleNames(href)
        page += 1

def getPeopleNames(commentorNames):
    sourceCode = requests.get(commentorNames)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText)
    for commenterName in soup.findAll('a', {"class" : "user-name"}):
        print(commenterName.string)

cPlusPlusSpider(1)