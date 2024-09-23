# Secret Note

I was told to never write down my passwords on a sticky note, so instead I wrote them down on my computer!

## Solution

Apparently since this was a mouse in a VM, the standard mouse coord conversion will not work...
It used absolute coordinates instead of relative coordinates.

"since it was in a VM and was considered a hub rather than a mouse, you had to write a custom parser and couldn't use ones from online"

```py
# solver
import subprocess
from PIL import Image

tshark = ["C:\\Program Files\\Wireshark\\tshark.exe", "-r", "capture.pcapng", "-Y", "usbhid.data", "-T", "fields", "-e", "usbhid.data"]
output = subprocess.run(tshark, stdout=subprocess.PIPE).stdout.splitlines()

img = Image.new('RGB', (5000, 5000), color='white')
canvas = img.load()
write = False

for i in output:
    a = i.decode()
    if a == '0100000000000000':
        write = True
    elif a == '0000000000000000':
        write = False
    # //10 helps file size stay smaller (not necessary, but may have to increase image size if removed)
    x = int(bytearray.fromhex(a[4:8])[::-1].hex(), 16)//10
    y = int(bytearray.fromhex(a[8:12])[::-1].hex(), 16)//10

    if write:
        # loops to make flag easier to read (not necessary)
        for i in range(5):
            for j in range(5):
                canvas[x + i, y + j] = (255, 0, 0)

img.save("flag.png")
exit()
```

also, definitely needed `0100000000000000` (mouse down), `0000000000000000` (mouse up) for correct drawing

```txt
Used my own tool: https://github.com/Nissen96/USB-HID-decoders
But the format was not what I've seen before, so had to make a few small modifications (drawing absolute instead of relative position)
```

## Attempt

USB data?

https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4

3.1.0 - virtual mouse
3.2.0 - virtual usb hub  (max packet size 8)
3.3.0 - virtual usb hub  (max packet size 64)

https://res260.medium.com/usb-pcap-forensics-graphics-tablet-nsec-ctf-2021-writeup-part-2-3-9c6265ca4c40

3.1.1 -> host has HID data?
right click HID Data, add as column

`usbhid.data != 0 && usb.src == "3.1.1"` export as CSV

https://wiki.osdev.org/USB_Human_Interface_Devices#Report_format_2

ex: 000085044a070000
- byte 1 `00` - button byte
- byte 2 `00` - x-axis movement
- byte 3 `85` - y-axis movement
- only relevant info needed (I think/hope)

note: 3.1.2 has a lot of `0100000000000000`, not sure if needed...this would be right clicks?

bInterfaceProtocol 0x00 means a custom device...
so do i just extract all the middle data?
