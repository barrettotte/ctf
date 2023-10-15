# hide-and-split

Explore this disk image file, maybe you can find something hidden in it.

## Solution

```sh
file challenge.ntfs
# challenge.ntfs: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS    ", sectors/cluster 8, 
# Media descriptor 0xf8, sectors/track 0, dos < 4.0 BootSector (0x80), FAT (1Y bit by descriptor); 
# NTFS, sectors 10239, $MFT start cluster 4, $MFTMirror start cluster 639, bytes/RecordSegment 2^(-1*246), 
# clusters/index block 1, serial number 01fe3c7444d0702ed

mkdir /media/ctf
sudo mount -t ntfs -o nls=utf8,umask=0222 challenge.ntfs /media/ctf
sudo umount /media/ctf
```

100 flag files that say

```txt
Unfortunately this is not the flag
The flag has been split and stored in the hidden part of the disk
```

alternate data streams?

```sh
sudo apt-get install ntfs-3g

sudo mount -t ntfs-3g challenge.ntfs /media/ctf

ntfsls -l challenge.ntfs

sudo mount -t ntfs-3g -o ro,streams_interface=xattr challenge.ntfs /media/ctf

sudo apt-get install attr
attr -l /media/ctf
getfattr /media/ctf
# nothing...

sudo mount -t ntfs-3g -o ro,streams_interface=windows challenge.ntfs /media/ctf
attr -g ntfs.streams.list /media/ctf
getfattr -n user.ntfs.streams.list /media/ctf
# nothing...
```

Couldn't figure out how to do this on linux...Extracted to windows using 7zip

```ps1
Get-Item *.txt -Stream *
Get-Content .\flag00.txt:flag0
```

```batch
dir /r
```

- ran `extract.ps1`
- loaded `blob.txt` into cyberchef. from hex -> render image (raw)
- QR code rendered
- scanned with phone to get flag

`TCP1P{hidden_flag_in_the_extended_attributes_fea73c5920aa8f1c}`

## Alternate Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Forensic/hide%20and%20split/writeup

```sh
sudo mount -t ntfs -o stream_interfaces=windows challenge.ntfs /tmp/mnt
getfattr -d /tmp/mnt/flag00.txt
```

Extract script similar to my powershell one:

```sh
#!/bin/bash

DISK_IMAGE=challenge.ntfs
MOUNT_POINT="/tmp/mnt"
OUTPUT_TXT="flag.txt"
OUTPUT_PNG="flag.png"

# For initializing the output files
> "$OUTPUT_TXT"

sudo mkdir -p "${MOUNT_POINT}"
sudo mount -t ntfs -o stream_interfaces=windows "${DISK_IMAGE}" "${MOUNT_POINT}"

for i in {0..99}; do
	FILENAME="flag$(printf "%02d" $i).txt"
	FULL_PATH="${MOUNT_POINT}/${FILENAME}"
	getfattr -d "$FULL_PATH" | awk -F'=' '{print $2}' | tr -d '\n' | sed 's/"//g' >> "$OUTPUT_TXT"
done

cat "${OUTPUT_TXT}" | xxd -r -p > "${OUTPUT_PNG}"
sudo umount "${MOUNT_POINT}"
echo "File save to ${OUTPUT_TXT} and ${OUTPUT_PNG}"
```
