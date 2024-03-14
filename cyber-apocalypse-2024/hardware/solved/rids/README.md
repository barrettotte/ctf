# rids

Upon reaching the factory door, you physically open the RFID lock and find a flash memory chip inside. 
The chip's package has the word W25Q128 written on it. 
Your task is to uncover the secret encryption keys stored within so the team can generate valid credentials to gain access to the facility.

## Solution

```sh
unzip -o ~/Downloads/hardware_rids.zip
```

usb_device_url = 'ftdi://ftdi:2232h/1'

FTDI? The simplest and most common use of FTDI devices is for the purpose of bridging USB ports to a UART peripheral interface

W25Q128 - some sort of flash memory ? 
https://www.digikey.com/en/products/base-product/winbond-electronics/256/W25Q128/339728

in `client.py` - `cs=0 # /CS on A*BUS3 (range: A*BUS3 to A*BUS7)`

```
The SPI Chip Select (/CS) pin enables and disables device operation. When /CS is high the device is
deselected and the Serial Data Output (DO, or IO0, IO1, IO2, IO3) pins are at high impedance. When
deselected, the devices power consumption will be at standby levels unless an internal erase, program
or write status register cycle is in progress. When /CS is brought low the device will be selected, power
consumption will increase to active levels and instructions can be written to and data read from the
device. After power-up, /CS must transition from high to low before a new instruction will be accepted.
The /CS input must track the VCC supply level at power-up and power-down (see “Write Protection” and
Figure 58). If needed a pull-up resister on the /CS pin can be used to accomplish this.
```

```sh
python3 client.py
# Received: [239, 64, 24]
```

```py
# Example command
jedec_id = exchange([0x9F], 3)
print(jedec_id)

# jedec? kind of a vendor name?
# page 25 of datasheet has this!
```

