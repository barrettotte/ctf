# Forensics 3 - Halloween Invitation

```sh
file invitation.docm
# Microsoft Word 2007+

unzip invitation.docm
code .

# looking through files

# vbaData.xml
# vbaProject.bin

strings word/vbaProject.bin
# powershell -WindowStyle hidden -e
# WScript.Shell

hexdump -C word/vbaProject.bin
hexdump -C word/vbaProject.bin > vbaProject.dump


# https://github.com/decalage2/oletools
sudo -H pip3 install -U oletools-0.60.1.zip

olevba invitation.docm --decode > decoded.txt
# looks like a big mess of obfuscated hex

# https://github.com/decalage2/ViperMonkey
chmod +x /opt/ViperMonkey/docker/dockermonkey.sh
sudo opt/ViperMonkey/docker/dockermonkey.sh invitation.docm
unzip invitation.docm_artifacts.zip   # password=infected

cat root/invitation.docm_artifacts/history.bak | base64 --decode > macro.vba
# macro contains flag
```
