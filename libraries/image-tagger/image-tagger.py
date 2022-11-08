import os
import sys

from PIL import Image, ImageDraw

args = sys.argv[1:]

if len(args) < 1:
    print('Usage: python image-tagger.py <image.png>')
    sys.exit(1)

img = Image.open(args[0])
img_size = img.size
canvas = ImageDraw.Draw(img)

text = f'{img_size[0]} x {img_size[1]}'
text_size = canvas.textlength(text)
margin_px = 10
text_position = (
    img_size[0] - text_size - margin_px, img_size[1] - margin_px * 2)

canvas.text(text_position, text, fill='white')

tag = "-stamped"
name = os.path.splitext(args[0])[0]
ext = os.path.splitext(args[0])[1]
img.save(name + tag + ext)
