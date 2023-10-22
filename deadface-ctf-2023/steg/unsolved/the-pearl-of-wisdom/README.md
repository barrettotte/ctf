# the-pearl-of-wisdom

```
A word was secretly brought to me,my ears caught a whisper of it.
Amid disquieting dreams in the night,when deep sleep falls on men,fear and trembling seized meand made all my bones shake.
A spirit glided past my face,and the hair on my body stood on end.
It stopped,but I could not tell what it was.
A form stood before my eyes,and I heard a hushed voice:

‘Can a mortal be more righteous than God?
Can even a strong man be more pure than his Maker?
If God places no trust in his servants,if he charges his angels with error,how much more those who live in houses of clay,whose foundations are in the dust,who are crushed more readily than a moth!
Between dawn and dusk they are broken to pieces;unnoticed, they perish forever.
Are not the cords of their tent pulled up,so that they die without wisdom?'
```

## Solution

```sh
strings
# tinyurl link found -> perl script

# create wordlist from poem
grep -c E'\w+' poem.txt | sort -u -f > words.txt
```

then some sort of bruteforce solver

too much stuff to copy down here ...
