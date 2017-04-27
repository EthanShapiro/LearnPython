import random
import urllib.request

def downloadWebImage(url):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)

downloadWebImage("https://s-media-cache-ak0.pinimg.com/originals/14/aa/df/14aadf55f80c4751092d660581ae8bd2.jpg")