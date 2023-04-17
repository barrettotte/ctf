# remote-computation

**SOLVED**

> The alien species use remote machines for all their computation needs. 
> Pandora managed to hack into one, but broke its functionality in the process. 
> Incoming computation requests need to be calculated and answered rapidly, in order to not alarm the aliens and ultimately pivot to other parts of their network. 
> Not all requests are valid though, and appropriate error messages need to be sent depending on the type of error. 
> Can you buy us some time by correctly responding to the next 500 requests?

`nc 159.65.62.241 31315`

```
# [2] Help

Results
---
All results are rounded
to 2 digits after the point.
ex. 9.5752 -> 9.58

Error Codes
---
* Divide by 0:
This may be alien technology,
but dividing by zero is still an error!
Expected response: DIV0_ERR

* Syntax Error
Invalid expressions due syntax errors.
ex. 3 +* 4 = ?
Expected response: SYNTAX_ERR

* Memory Error
The remote machine is blazingly fast,
but its architecture cannot represent any result
outside the range -1337.00 <= RESULT <= 1337.00
Expected response: MEM_ERR
```

```
# samples
[001]: 3 * 15 / 6 / 29 / 6 = ?
[001]: 19 / 12 + 15 + 18 + 7 / 10 + 23 * 30 = ?
[001]: 4 + 17 * 5 - 10 + 8 + 22 * 4 - 11 / 25 = ?
```

`HTB{d1v1d3_bY_Z3r0_3rr0r}`