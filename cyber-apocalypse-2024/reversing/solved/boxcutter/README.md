# boxcutter

You've received a supply of valuable food and medicine from a generous sponsor. There's just one problem - the box is made of solid steel! Luckily, there's a dumb automated defense robot which you may be able to trick into opening the box for you - it's programmed to only attack things with the correct label.

## Solution

```sh
strings cutter | less

strace ./cutter
# HTB{tr4c1ng_th3_c4ll5}
```