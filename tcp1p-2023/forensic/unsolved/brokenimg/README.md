# brokenimg

why the picture like this

## Solution

wow...I fumbled at the last step...I missed the last couple letters of the octal string

in pdf:

```xml
<rdf:Description rdf:about=''
  xmlns:tiff='http://ns.adobe.com/tiff/1.0/'>
  <tiff:Artist>Maybe here : 150 164 164 160 163 72 57 57 146 151 154 145 163 56 144 157 170 142 151 156 56 147 147 57 157 63 126 144 162 115 160 164 56 160 156 147</tiff:Artist>
 </rdf:Description>
```

decode octal using cyberchef -> `https://files.doxbin.gg/o3VdrMpt.png`

```py
# Resize the image size to shift the pixel
from PIL import Image

image = Image.open('o3VdrMpt.png')
pixels = list(image.getdata())
image2 = Image.new('RGB', (497, 600))
image2.putdata(pixels)
image2.save('resized.png')
```

```sh
echo KZCU4UKNKZBDOY2HKJWVQMTHGBSGUTTGJZDDSUKNK5HDAZCYJF5FQMSKONSFQSTGJZDTK22YPJLG6TKXLIYGMULPHU====== | base32 -d | base64 -d
# TCP1P{pdf_h4v3_4_P1ctur3_blur_4nd_5h1ft}
```
