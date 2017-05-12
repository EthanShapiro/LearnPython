import requests
from bs4 import BeautifulSoup
import re
import operator

def start(url):
    wordList = []
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, "lxml")
    for postText in soup.find_all('a', {"class": "title text-semibold"}):
        content = postText.string
        words = content.lower().split()
        wordList.extend(words)
    cleanUpList(wordList)

def cleanUpList(wordList):
    cleanWordList = []
    pattern = re.compile("[^0-9a-zA-Z]")
    for word in wordList:
        word = re.sub(pattern, "", word)
        if len(word) > 0:
            cleanWordList.append(word)
    occuranceDict(cleanWordList)


def occuranceDict(wordList):
    wordCount = {}
    wordCount = wordCount.fromkeys(wordList)
    for k in wordCount.keys():
        wordCount[k] = wordList.count(k)
    wordCount = sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)
    print(wordCount)

start("https://thenewboston.com/forum/")
