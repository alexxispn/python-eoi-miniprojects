import os

from PIL import Image

img = Image.new('RGB', (256, 256))
pixels = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        red, green, blue = x, y, int((x + y) / 2)
        pixels[x, y] = (red, green, blue)

assert pixels[13, 27] == (13, 27, 20)
img.save(os.path.join(os.path.dirname(__file__), 'color-ramp.png'))
