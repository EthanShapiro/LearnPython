from __future__ import print_function
from PIL import Image

im = Image.open("pillow-42-picture.jpg")
box = (100, 100, 400, 400)
region = im.crop(box)
im.paste(region, box)
im.show()
print(im.format, im.size, im.mode)
