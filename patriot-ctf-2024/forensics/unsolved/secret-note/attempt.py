import csv
import json
from PIL import Image, ImageDraw

with open('usb.csv', 'r') as f:
    csv_reader = csv.reader(f)
    hid_data = []

    for i, row in enumerate(csv_reader):
        if i == 0:
            continue
        hid_data.append(row[7])

with open('temp.txt', 'w+') as f:
    for h in hid_data:
        # f.write(h[4:12])
        f.write(h + '\n')


events = []
for i,h in enumerate(hid_data):
    event = {
        'idx': i,
        'button': int(h[0:2], 16),
        'x': int(h[2:6], 16),
        'x_raw': h[2:6],
        'y': int(h[6:10], 16),
        'y_raw': h[6:10],
        'scroll': int(h[10:12], 16),
    }
    events.append(event)

with open('events.json', 'w+') as f:
    s = json.dumps(events, indent=2)
    f.write(s)

img = Image.new('RGB', (28000, 500), color='white')
canvas = img.load()
mouse_x = 10000
mouse_y = 250

for i, h in enumerate(hid_data):
    print('event', i)

    left_button_pressed = int.from_bytes(bytes.fromhex(h[0:2]), 'big', signed=True) & 0b00000001    
    y_offset = int.from_bytes(bytes.fromhex(h[2:6]), 'big', signed=True)
    x_offset = int.from_bytes(bytes.fromhex(h[6:10]), 'big', signed=True)

    mouse_x = round(x_offset)
    mouse_y = round(y_offset)

    try:
        if left_button_pressed:
            print('event', i, 'left click!')

        canvas[round(mouse_x), round(mouse_y)] = (255,0,0)

    except IndexError:
        print('Error: Mouse out of bounds')
        print('event', i)
        print('mouse_x =', mouse_x)
        print('mouse_y =', mouse_y)
        exit(1)

img.save('flag.png')
