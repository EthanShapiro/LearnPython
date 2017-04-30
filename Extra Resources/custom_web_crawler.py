import requests
import re
from bs4 import BeautifulSoup

compSciUrl = "https://thenewboston.com/videos.php"

def getVideoNames(url, titleName):
    data = requests.get(url)
    text = data.text
    soup = BeautifulSoup(text, "lxml")
    videoPanels = soup.find_all("div", class_="panel video-category-panel")

    for panel in videoPanels:
        if panel.contents[1].h2.contents[2].strip() == titleName:
            saveTextAndFormat(titleName, panel.contents[3].text)

def saveTextAndFormat(title, text):
    text = text.replace('\n\n', '\n')
    text = re.sub('[^a-zA-Z0-9_\s]', '-', text)
    text = text.split('\n')
    print(text)
    data = []
    for line in text:
        line = line.split('\n')
        print(line)
        line = ' '.join(line)
        line = line.split()
        line = ' '.join(line)
        data.append(line)
    text = data
    # print(text)
    # text = '\n'.join(' '.join(line.split()) for line in text.split('\n'))


    # with open("MyNewText.txt", "w+") as f:
    #     f.write(title)
    #     f.writelines(text)
    #     f.seek(0)
        # for line in f.readlines():
        #     line = re.sub("[^a-zA-Z0-9_ \t\n\r\f\v]", '', line)
        #     line = line.strip()
        #     line = ' '.join(line.split())


getVideoNames(compSciUrl, "Adobe")