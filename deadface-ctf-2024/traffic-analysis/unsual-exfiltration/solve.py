from PIL import Image

with open('data.txt', 'r') as f:
    lines = f.readlines()

height, width = (len(lines), len(lines[0]))
img = Image.new('RGB', (width, height))

for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if char == 'R':
            img.putpixel((x, y), (0, 0, 0))
        elif char == 'Q':
            img.putpixel((x, y), (255, 255, 255))

img.save('qrcode.png')
