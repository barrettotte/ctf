# https://gist.github.com/zhuowei/666c7e6d21d842dbb8b723e96164d9c3

import sys
import os
import zlib
with open(sys.argv[1], "rb") as infile:
  indata = infile.read()

magic = b"Playdate PDX\0\0\0\0"
magic_new = b"Playdate PDZ\0\0\0\0"

if not indata[0:len(magic)] in [magic, magic_new]:
  print("not a Playdate PDX/PDZ file")
  exit(1)

def readcstr(dat, off):
  return dat[off:dat.find(b"\0", off)]

# file outer header:
# 0: type:uint8 = 0x81
# 1: length:uint16? = length of inner header + contents
# 3: empty:uint8 = 0x0
# 4: filename:cstring
# aligned to 4
# followed by inner header + contents
# file inner header:
# 55 02 00 00
# contents: gzip data

off = 0x10
while off < len(indata):
  type = indata[off]
  if type == 0xe8:
    # EOF checksum?
    break
  if type != 0x81:
    print("invalid type", hex(off), hex(type))
    exit(1)
  innerlen = indata[off + 1] | (indata[off + 2] << 8)
  filename = readcstr(indata, off + 4)
  outerheadersize = 4 + len(filename) + 1
  outerheadersize = ((off + outerheadersize + 3) & ~3) - off
  zlibdata = indata[off + outerheadersize + 4: off + outerheadersize + innerlen]
  filename_s = filename.decode("utf-8")
  print(filename_s)
  if "/" in filename_s:
    os.makedirs(os.path.dirname(filename_s), exist_ok=True)
  with open(filename_s, "wb") as outfile:
    outfile.write(zlib.decompress(zlibdata))
  off += outerheadersize + innerlen
