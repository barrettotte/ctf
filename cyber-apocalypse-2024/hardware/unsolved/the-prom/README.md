# the-prom

After entering the door, you navigate through the building, evading guards, and quickly locate the server room in the basement. 
Despite easy bypassing of security measures and cameras, laser motion sensors pose a challenge. 
They're controlled by a small 8-bit computer equipped with AT28C16 a well-known EEPROM as its control unit. 
Can you uncover the EEPROM's secrets and deactivate the sensors.

## Attempt

AT28C16 EEPROM - http://cva.stanford.edu/classes/cs99s/datasheets/at28c16.pdf

READ: The AT28C16 is accessed like a Static RAM.
When CE and OE are low and WE is high, the data stored
at the memory location determined by the address pins is
asserted on the outputs. The outputs are put in a high
impedance state whenever CE or OE is high. This dual line
control gives designers increased flexibility in preventing
bus contention.

DEVICE IDENTIFICATION: An extra 32 bytes of
EEPROM memory are available to the user for device iden-
tification. By raising A9 to 12 ± 0.5V and using address
locations 7E0H to 7FFH the additional bytes may be written
to or read from in the same manner as the regular memory
array.

```sh
nc 94.237.48.205 36316
```

```txt
      AT28C16 EEPROMs
       _____   _____
      |     \_/     |
A7   [| 1        24 |] VCC
A6   [| 2        23 |] A8
A5   [| 3        22 |] A9
A4   [| 4        21 |] !WE
A3   [| 5        20 |] !OE
A2   [| 6        19 |] A10
A1   [| 7        18 |] !CE
A0   [| 8        17 |] I/O7
I/O0 [| 9        16 |] I/O6
I/O1 [| 10       15 |] I/O5
I/O2 [| 11       14 |] I/O4
GND  [| 12       13 |] I/O3
      |_____________|

> help

Usage:
  method_name(argument)

EEPROM COMMANDS:
  set_address_pins(address)  Sets the address pins to the specified values.
  set_ce_pin(volts)          Sets the CE (Chip Enable) pin voltage to the specified value.
  set_oe_pin(volts)          Sets the OE (Output Enable) pin voltage to the specified value.
  set_we_pin(volts)          Sets the WE (Write Enable) pin voltage to the specified value.
  set_io_pins(data)          Sets the I/O (Input/Output) pins to the specified data values.
  read_byte()                Reads a byte from the memory at the current address.
  write_byte()               Writes the current data to the memory at the current address.
  help                       Displays this help menu.

Examples: 
  set_ce_pin(3.5)
  set_io_pins([0, 5.1, 3, 0, 0, 3.1, 2, 4.2])
```

```
# try to read device ID based on manual

set_ce_pin(5)
set_oe_pin(5)
set_we_pin(0)

# 0x7E0  
set_address_pins([5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 0])
read_byte()

# 0x7FF  
set_address_pins([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
read_byte()
```

ran `solve.py`, but nothing in memory...all zeroes?



```
# test writing a byte, then reading it

set_ce_pin(5)
set_oe_pin(0)
set_we_pin(5)
set_address_pins([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5])
set_io_pins([5,5,5,5,5,5,5,5])
write_byte()

set_ce_pin(5)
set_oe_pin(5)
set_we_pin(0)
read_byte()
```

## Solution

https://youtu.be/EGItzKCxTdQ?si=IO1t_r1JiIkEyIEF&t=6405

Device Identification was it...

```
set_ce_pin(5)
set_oe_pin(5)
set_we_pin(0)
set_address_pins([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5])
read_byte()
```

read bytes from 0x7E0 to 0x7FF

address[1] should be 12, I think I was setting the wrong one

