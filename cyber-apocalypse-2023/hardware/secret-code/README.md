# secret-code

**SOLVED**

> To gain access to the tomb containing the relic, you must find a way to open the door. 
> While scanning the surrounding area for any unusual signals, you come across a device that appears to be a fusion of various alien technologies.
> However, the device is broken into two pieces and you are unable to see the secret code displayed on it. 
> The device is transmitting a new character every second and you must decipher the transmitted signals in order to retrieve the code and gain entry to the tomb.

sal file and gerber files

## board

opened gerber files in kicad

`.grbjob`? https://www.ucamco.com/files/downloads/file_en/209/the-gerber-job-format-specification-technical-manual_en.pdf

seems to be an IC with 10 pins, two connectors 5 pins each routed to this IC

AVR ISP? https://telecnatron.com/reference/pinouts/avr-isp/index.html

Has 10 pins

MOSI,NC,RST,SCK,MISO,VCC,4 x GND ... so SPI?

https://en.wikipedia.org/wiki/Serial_Peripheral_Interface#Interface

NOPE

Top silkscreen confirmed 7 segment, channels labeled and orientation of seven segment shown

channel to 7 seg mapping

0. D (2)
1. DP (5) -> clk
2. A (7)
3. G (10)
4. C (4)
5. B (6)
6. E (1)
7. F (9)

## signal

opened sal file

channel 1 definitely clock

https://geekoder.com/category/ctf/#off-the-grid

I2C? SDA (data), SCL (clock)

"The device is transmitting a new character every second" - enable goes high once a second?

"However, the device is broken into two pieces and you are unable to see the secret code displayed on it." - its a display?

Seven segment display? https://media.parallax.com/wp-content/uploads/2020/07/13155129/350-00027a.png.webp
Seven signals - lines up

exported signal to csv

wrote python script to map/decode signals

omg "Things change for common cathode configuration." https://www.electronicsforu.com/resources/7-segment-display-pinout-understanding

