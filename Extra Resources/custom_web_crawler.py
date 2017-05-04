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
    # text = text.split('\n')
    # data = []
    # time = 0
    # for line in text:
    #     line = line.split('\n')
    #     print(line)
    #     line = ' '.join(line)
    #     print(line)
    #     line = line.split()
    #     print(line)
    #     line = ' '.join(line)
    #     print(line)
    #     time += 1
    #     data.append(line)
    # text = '\n'.join(data)
    # print(text)
    text = '\n'.join(' '.join(line.split()) for line in text.split('\n'))
    text.strip()
    with open("Lesson {0}".format(title), "w+") as f:
        f.write(title)
        f.write(text)


getVideoNames(compSciUrl, "Adobe")
getVideoNames(compSciUrl, "Computer Programming")
getVideoNames(compSciUrl, "Banana")