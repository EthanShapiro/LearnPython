from bs4 import BeautifulSoup
import requests

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
rawData = requests.get(url)
soup = BeautifulSoup(rawData.text, "lxml")
seperatedText = soup.findAll('p')
for i in range(0, len(seperatedText)):
    if seperatedText[i].string != None:
        print(seperatedText[i].string)

