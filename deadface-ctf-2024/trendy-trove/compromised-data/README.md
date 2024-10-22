# Compromised Data

Several victims provided credit card information to TrendyTrove. 
We believe DEADFACE kept this information on the web server somewhere. 
See if you can find the flag associated with this data.

Submit the flag as flag{flag-text}.

TrendyTrove

## Solution

So I guess I missed it, but log in as admin and eventually you can do PHP command injection.
Flag is in a csv on the filesystem...

## Attempt

```sh
sqlmap -u "https://trendytrove.deadface.io/login.php" --data "username=*&password=*" --os-shell "pwd"
```
