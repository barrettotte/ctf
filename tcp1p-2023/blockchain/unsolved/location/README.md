# location

Will you accept the invitation? If so, find the party location now!

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Blockchain/Location/Private/writeup.md

The concept of the challenge is to introduce player to Storage Allocation in Solidity called SLOT

https://medium.com/@flores.eugenio03/exploring-the-storage-layout-in-solidity-and-how-to-access-state-variables-bf2cbc6f8018

By default a SLOT is a 32 bytes.

| Data Type | Bytes Allocation |
| :---: | :---: |
| address | 20 bytes |
| uintX | X/8 bytes |
| bytesX | X bytes |
| bool | 1 byte |

A special case for "Immutable" data type or we can say "Constant" data-type, they won't be stored in SLOT, rather they'll be stored in the contract bytecodes.
