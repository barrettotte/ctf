# Secret Note

I was told to never write down my passwords on a sticky note, so instead I wrote them down on my computer!

## Solution

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
