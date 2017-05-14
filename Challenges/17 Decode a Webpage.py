from bs4 import BeautifulSoup
import requests

titles = []

rawText = requests.get("https://www.nytimes.com/?WT.z_jog=1&hF=f&vS=undefined")
soup = BeautifulSoup(rawText.text, "lxml")
titles = soup.findAll("h2", {"class": "story-heading"})
print(titles)