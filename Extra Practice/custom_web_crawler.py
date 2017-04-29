import requests
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
    with open("MyNewText.txt", "w+") as f:
        f.write(title)
        f.writelines(text)
        f.seek(0)
        for line in f.readlines():
            line = line.split()
            print(line)

getVideoNames(compSciUrl, "Adobe")