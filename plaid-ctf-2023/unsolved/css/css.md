# css

- https://rinnnt.github.io/ctf/2023/04/16/plaidctf-2023-writeup.html#css-200-points-80-solves
- https://blog.snwo.kr/posts/(ctf)-plaid-ctf-2023/
- https://gist.github.com/SakiiR/700d2c5ca2eddb28123493498c584189
- https://rinnnt.github.io/ctf/2023/04/16/plaidctf-2023-writeup.html#css-200-points-80-solves

```txt
Time to put my cursed CSS write up
So I used browser console script to brute force "button" clicking for each 3 chars in the flag
Used OBS to record
and Python opencv to detect that pixel change at "correct"
each 3 of them takes about 10 min lol 

https://www.youtube.com/watch?v=hfQglE8QdkM
```

## Solve 1

`css-solve-1.js`

## Solve 2

```
CSS AutoClicker Script entirely in browser using the "share tab" feature:
(Prerequisite: split flag into 14 separate files (single triplets) + <canvas style="position:absolute;top:200px;"id="canv"></canvas> added at the bottom of the files)
```

`css-solve-2.js`
