import dis
import binascii
import marshal

s = 'check.pyc'
s = './compile-check.cpython-311.pyc'

with open(s, 'rb') as f:
    f.seek(16)
    pyc_bytes = marshal.load(f)

dis.dis(pyc_bytes)

