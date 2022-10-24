# Forensics 2


a bunch of DNS; also query and responses that kind of look base64 encoded

installed `tshark`

```sh
tshark -r capture.pcap -T fields

# dns && dns.flags.response == 0
```

Tried to make `exploit.py`, a lot of hex. Some file paths to Excel files...but can't figure out rest.

```sh
tshark -Y "dns && dns.flags.response == 0" -T fields -e "dns.qry.name" -r capture.pcap | cut -d '.' -f1

# https://en.wikipedia.org/wiki/List_of_file_signatures
# searched for 50 4B 03 04 => zip file format
# note: did see PK in exploit.py output...this matches

# https://blog.danniranderis.dk/2021/08/20/zipfil-ctf-challenge-gp-august-21/

tshark -Y "dns && dns.flags.response == 0" -T fields -e "dns.qry.name" -r capture.pcap | cut -d '.' -f1 > payload.zip

zipdetails payload.zip 
# No Central Directory records found

jar -xvf payload.zip
# zip END header not found

file -i payload.zip
# payload.zip: text/plain; charset=us-ascii

# revisited scan.py; /worksheets/_rels/sheet2.xml
# is this an xlsx file ?
tshark -Y "dns && dns.flags.response == 0" -T fields -e "dns.qry.name" -r capture.pcap | cut -d '.' -f1 > payload.xlsx

# tried xlsx in LibreOffice; failed
# tried docx in LibreOffice; failed
# tried jar again; failed

# I'm pretty sure its Office Open XML (OOXML)

# I'm not writing binary correctly, what?  
hexdump payload.docx | head -n3

# nice...Note: needed to unhexlify the bytearray before write...it was indeed an Excel file
```


