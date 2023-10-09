# low-effort-wav

```sh
file low_effort.wav
# low_effort.wav: PNG image data, 465 x 803, 8-bit/color RGBA, non-interlaced

strings low_effort.wav
```

```xml
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 12.59'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:GettyImagesGIFT='http://xmp.gettyimages.com/gift/1.0/'>
  <GettyImagesGIFT:OriginalFilename>Screenshot_20230319-223111.png</GettyImagesGIFT:OriginalFilename>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 12.59'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:GettyImagesGIFT='http://xmp.gettyimages.com/gift/1.0/'>
  <GettyImagesGIFT:OriginalFilename>Screenshot_20230319-223111.png</GettyImagesGIFT:OriginalFilename>
 </rdf:Description>
</rdf:RDF>
</x:xmpmeta>
<?xpacket end='r'?>

<!-- probably nothing... -->
```

https://github.com/exiftool/exiftool

```sh
exiftool low_effort.wav
# nothing of note

binwalk low_effort.wav

binwalk -Mre low_effort.wav

echo import binwalk; binwalk.scan('-B', 'low_effort.wav') | python3
```

```sh
dd if=low_effort.wav of=low_effort.png bs=1 skip=0 count=554

dd if=low_effort.wav of=low_effort.tiff bs=1 skip=554 count=118

dd if=low_effort.wav of=low_effort.zlib bs=1 skip=672
```

```sh
png-parser low_effort.png --text -d 

png-parser low_effort.png --all

png-parser low_effort.png --crc --length
# [00124719-00249496] (22)
# b'\x9a\x1a\x01 ':
# CRC : 00000000 : Incorrect must be ee8e1bd7
# Length : 124777
# Data size : 124770
```
