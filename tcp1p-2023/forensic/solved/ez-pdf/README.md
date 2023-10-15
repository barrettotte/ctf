# ez-pdf

I just downloaded this PDF file from a strange site on the internet....

## Solution

```sh
strings TCP1P-CTF.pdf | less
# obfuscated javascript
```

extracted obfuscated js to `pdf.js`

`pdf.js` ran in browser -> `_15N7_17_l3jaf9ci293m1d}`

```
SW4gdGhpcyBxdWVzdGlvbiwgdGhlIGZsYWcgaGFzIGJlZW4gZGl2aWRlZCBpbnRvIDMgcGFydHMuIFlvdSBoYXZlIGZvdW5kIHRoZSBmaXJzdCBwYXJ0IG9mIHRoZSBmbGFnISEgVENQMVB7RDAxbjlfRjAyM241MUM1
In this question, the flag has been divided into 3 parts. You have found the first part of the flag!! TCP1P{D01n9_F023n51C5
```

`TCP1P{D01n9_F023n51C5`

`TCP1P{D01n9_F023n51C5_15N7_17_l3jaf9ci293m1d}` ... nope

https://www.pdfforge.org/online/en/extract-images -> `_0N_pdf_f1L35_15_345y`

combined: `TCP1P{D01n9_F023n51C5_0N_pdf_f1L35_15_345y_15N7_17_l3jaf9ci293m1d}`

## Alternate Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Forensic/Ez%20PDF/writeup

- https://exif.tools/
- https://github.com/jesparza/peepdf

```sh
exiftool -Creator TCP1P-CTF.pdf | grep -oP '\w+$' | base64 -d
# In this question, the flag has been divided into 3 parts. You have found the first part of the flag!! TCP1P{D01n9_F023n51C5

pdf-parser.py -o 4 TCP1P-CTF.pdf | grep -oP '(?<=\().+(?=\))' | sed 's/= 1;/= 0;/g' > script.js
node script.js
# _15N7_17_l3jaf9ci293m1d}

mutool extract TCP1P-CTF.pdf
tesseract image-0010.png out
cat out.txt
# _ON_pdf_f1L35_15_345y
```
