# pursue-the-tracks

Luxx, leader of The Phreaks, immerses himself in the depths of his computer, tirelessly pursuing the secrets of a file he obtained accessing an opposing faction member workstation. 
With unwavering determination, he scours through data, putting together fragments of information trying to take some advantage on other factions. To get the flag, you need to answer the questions from the docker instance.

## Solution

```sh
nc 94.237.61.79 30337

file z.mft
# data

strings z.mft
# FILE0
# Random string for credentials
```

```sh
# https://andreafortuna.org/2017/07/18/how-to-extract-data-and-timeline-from-master-file-table-on-ntfs-filesystem/

pip3 install analyzeMFT
sudo apt-get install sleuthkit

git clone https://github.com/dkovar/analyzeMFT.git

python3 analyzeMFT/analyzeMFT.py -f z.mft -o mft.csv

python3 analyzeMFT/analyzeMFT.py -f z.mft -b test.txt

# open in openoffice

mactime -b mftparsero.txt > timeline.txt
```

```txt
Files are related to two years, which are those? (for example: 1993,1995)
2023,2024

There are some documents, which is the name of the first file written? (for example: randomname.pdf)
Final_Annual_Report.xlsx

Which file was deleted? (for example: randomname.pdf)
Marketing_Plan.xlsx

How many of them have been set in Hidden mode? (for example: 43)
1

Which is the filename of the important TXT file that was created? (for example: randomname.txt)
credentials.txt

A file was also copied, which is the new filename? (for example: randomname.pdf)
Financial_Statement_draft.xlsx

Which file was modified after creation? (for example: randomname.pdf)
Project_Proposal.pdf

What is the name of the file located at record number 45? (for example: randomname.pdf)
Annual_Report.xlsx

What is the size of the file located at record number 40? (for example: 1337) -> /documents/2023/Final_Project_Proposal.pdf
57344
```


https://github.com/kacos2000/MFT_Browser


## Post-CTF

https://youtu.be/EGItzKCxTdQ?si=lGL9WGcMdE0jDP0Y&t=9744

MFTEntryCarver - https://github.com/cyb3rfox/MFTEntryCarver
