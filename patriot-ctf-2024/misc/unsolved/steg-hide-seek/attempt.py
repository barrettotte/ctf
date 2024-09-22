import cv2
from pyzbar.pyzbar import decode
import os
import glob
from PIL import Image

def color_distance(color1, color2):
    """Calculate the Euclidean distance between two RGB colors."""
    return ((color1[0] - color2[0]) ** 2 +
            (color1[1] - color2[1]) ** 2 +
            (color1[2] - color2[2]) ** 2) ** 0.5

if not os.path.exists('qr_codes'):
    os.makedirs('qr_codes')
for f in glob.glob('qr_codes/*.bmp'):
    os.remove(f)

if not os.path.exists('raw'):
    os.makedirs('raw')
for f in glob.glob('raw/*.bmp'):
    os.remove(f)

image = Image.open("qr_mosaic.bmp")

square_size = 58
img_width, img_height = image.size
mosaic_rows = 25
mosaic_cols = 40

qr_detect = cv2.QRCodeDetector()
data = []

i = 0
for row in range(0, mosaic_rows):
    for col in range(0, mosaic_cols):
        left = col * square_size
        top = row * square_size
        right = left + square_size
        bottom = top + square_size
        
        qrcode = image.crop((left, top, right, bottom))
        qrcode.save(f'raw/img_{i}.bmp')

        # adjust colors to be high contrast
        background = qrcode.getpixel((0,0))
        tolerance = 52
        for x in range(0, qrcode.width):
            for y in range(0, qrcode.height):
                c = qrcode.getpixel((x, y))

                if color_distance(background, c) < tolerance:
                    qrcode.putpixel((x, y), (255,255,255))
                else:
                    qrcode.putpixel((x, y), (0,0,0))

        img_path = f'qr_codes/qr_{i}.bmp'
        qrcode.save(img_path)

        # read QR code data
        img = cv2.imread(img_path)
        decoded = decode(img)
        objects = [obj.data for obj in decoded]

        if len(objects) == 0:
            print('Error: Could not read data from QR code', i)
            exit(1)
        elif len(objects) > 1:
            print('Error: Unknown data format, should only have one piece of data per QR code')
            exit(2)

        data.append(objects[0])
        i += 1

with open('data.bin', 'wb') as f:
    f.write(b''.join(data))

with open('data.txt', 'w+') as f:
    f.write(b''.join(data).decode('utf-8'))


# rows = []
# with open('data-rows.txt', 'w+') as f:
#     row = []
#     i = 1
#     while i < len(data)+1:
#         row.append(data[i-1].decode('utf-8'))
        
#         if i % 8 == 0:
#             rows.append(row)
#             f.write(''.join(row) + '\n')
#             row = []
#         i += 1

# with open('data-cols.txt', 'w+') as f:
#     col = []
#     for row in rows:
#         f.write(row[0])


