# Forensics 4 - POOF

```sh
nc $TARGET_IP $TARGET_PORT

wget http://$ZIP_IP/forensics_poof.zip

unzip forensics_poof.zip.1
# candy_dungeon.pdf.boo
# mem.dmp
# poof_capture.pcap

wireshark poof_capture.pcap &
```

```txt
Which is the malicious URL that the ransomware was downloaded from? (for example: http://maliciousdomain/example/file.extension)

packet 4

[GET /packages/a5/61/caf3af6d893b5cb8eae9a90a3054f370a92130863450e3299d742c7a65329d94/pygaming-dev-13.37.tar.gz HTTP/1.1\r\n]

http://files.pypi-install.com/packages/a5/61/caf3af6d893b5cb8eae9a90a3054f370a92130863450e3299d742c7a65329d94/pygaming-dev-13.37.tar.gz
```

```sh
# https://www.synacktiv.com/en/publications/sharkyctf-ezdump-writeups-linux-forensics-introduction.html
# https://westoahu.hawaii.edu/cyber/forensics-weekly-executive-summmaries/memory-ctf-with-volatility-part-1/

grep -a "BOOT_IMAGE" mem.dmp
# BOOT_IMAGE=/vmlinuz-4.15.0-184-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv
# uh also like corrupted my terminal session ?

# Ubuntu zip has a volatility folder in it...I guess we use that?
# https://github.com/volatilityfoundation/volatility

git clone https://github.com/volatilityfoundation/volatility.git
chmod +x volatility/vol.py

sudo mv volatility /opt
sudo ln -s /opt/volatility/vol.py /usr/bin/vol.py

# was missing python2
sudo apt install python2
sudo ln -s /usr/bin/python2 /usr/bin/python

vol.py --info
# I think th ubuntu zip thing needs to be registered
# https://github.com/volatilityfoundation/profiles

sudo cp Ubuntu_4.15.0-184-generic_profile.zip /opt/volatility/volatility/plugins/overlays/linux
vol.py --info
# now shows linux ubuntu profile

# look for malicious process started via bash
vol.py --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_bash -f mem.dmp

# shows cd pygaming-dev-13.37/
# ./configure is only program ran, malicious ? yes
```

```sh
# ransomeware file was from zip, download from wireshark capture
wireshark poof_capture.pcap &
# file > export objects > http

mkdir pygaming
tar -xvf pygaming-dev-13.37.tar.gz

file configure
cat configure | md5sum
# 7c2ff873ce6b022663a1f133383194cc
```

```sh
# find programming language
strings configure

# found 2libpython3.6m.so.1.0
```

```sh
# find function name for encryption

# opened configure in ghidra
# hmm not sure

# https://github.com/extremecoders-re/pyinstxtractor
python3 pyinstxtractor/pyinstxtractor.py pygaming/pygaming-dev-13.37/configure

ls configure_extracted
# note: configure.pyc

# https://github.com/rocky/python-uncompyle6/
git clone git@github.com:rocky/python-uncompyle6.git
# not supported on python 3.10; not bothering

git clone https://github.com/zrax/pycdc
cmake .
make

pycdc/pycdc configure_extracted/configure.pyc > configure.py
# encrypt function => mv18jiVh6TJI9lzY
# key = vN0nb7ZshjAWiCzv
```

```python
def mv18jiVh6TJI9lzY(filename = None):
    data = open(filename, 'rb').read()
    key = 'vN0nb7ZshjAWiCzv'
    iv = b'ffTC776Wt59Qawe1'
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv)
    ct = cipher.encrypt(data)
    Pkrr1fe0qmDD9nKx(filename, ct)
```

```sh
# wrote decrypt.py using key/iv found
python3 decrypt.py

cat /home/barrett/Downloads/candy_dungeon.pdf | md5sum
# 3bc9f072f5a7ed4620f57e6aa8d7e1a1

# HTB{n3v3r_tru5t_4ny0n3_3sp3c14lly_dur1ng_h4ll0w33n}
```

