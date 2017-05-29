from bs4 import BeautifulSoup
import requests

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

def getTextFromWebpage(url):
    rawData = requests.get(url)
    soup = BeautifulSoup(rawData.text, "lxml")
    seperatedText = soup.findAll('p')
    text = [line.string for line in seperatedText if line.string is not None]
    saveText(text, "writeToFile")

def saveText(text, fileName):
    with open(fileName+".txt", "w") as f:
        f.writelines("\n".join(text))

getTextFromWebpage(url)