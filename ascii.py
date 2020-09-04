"""
    WARNING: very bad code
"""

from PIL import Image


def pmap(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
scale = "# "
length = len(scale) - 1
out = ""

img = Image.open("42.png")
img = img.convert("LA")
new_width, new_height = width, height = img.size

if height > 183:
    new_width, new_height = int((width * 320) / height), 183
elif width > 320:
    new_width, new_height = 320, int((height * 320) / width)

img.thumbnail((new_width, new_height), Image.ANTIALIAS)

new_width, new_height = img.size

for y in range(0, new_height - 1, 2):
    for x in range(new_width - 1):
        color = img.getpixel((x, y))[0]
        out += scale[int(pmap(color, 0, 255, 0, length))]
    out += "\n"

with open("a.txt", "w") as f:
    f.write(out)
