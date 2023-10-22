# scamazon-1

DEADFACE is running a scam e-commerce website they’re using to target TGRI and Lytton Labs employees. 
The site consists of products that these companies frequently purchase. 
Based on Ghost Town, it looks like lilith built the site. 
She’s not known for her programming skills - maybe she left a flaw in the website’s design.

Find the flag associated with scamazon 1. Submit the flag as flag{flag_text}.

https://epicsales.deadface.io

## My Attempt

https://ghosttown.deadface.io/t/scam-azon-site-needed/124/12

registered

```txt
Traceback (most recent call last)

    File "/usr/lib/python3.11/site-packages/flask/app.py", line 2213, in __call__

    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    File "/usr/lib/python3.11/site-packages/flask/app.py", line 2193, in wsgi_app

    response = self.handle_exception(e)
               ^^^^^^^^^^^^^^^^^^^^^^^^

    File "/usr/lib/python3.11/site-packages/flask/app.py", line 2190, in wsgi_app

    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    File "/usr/lib/python3.11/site-packages/flask/app.py", line 1486, in full_dispatch_request

    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    File "/usr/lib/python3.11/site-packages/flask/app.py", line 1484, in full_dispatch_request

    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^

    File "/usr/lib/python3.11/site-packages/flask/app.py", line 1469, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    File "/app/website/auth.py", line 71, in sign_up

    login_user(user, remember=True)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    File "/usr/lib/python3.11/site-packages/flask_login/utils.py", line 180, in login_user

    if not force and not user.is_active:
                         ^^^^^^^^^^^^^^

    AttributeError: 'NoneType' object has no attribute 'is_active'

The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.

To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. From the text traceback you can also create a paste of it. For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

    dump() shows all variables in the frame
    dump(obj) dumps all that's known about the object


```

```sh
gobuster dir --url https://epicsales.deadface.io/ -w /usr/share/wordlists/dirb/common.txt
# /console              (Status: 200) [Size: 1563]
# /login                (Status: 200) [Size: 2936]
# /logout               (Status: 302) [Size: 229] [--> /login?next=%2Flogout]
# /products             (Status: 200) [Size: 9648]
# /register

nmap -v -p- epicsales.deadface.io
# too long 80,443

sudo nmap -v -sS epicsales.deadface.io
```

```
exec("print('RCE'); __import__('os').system('ls')")

sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.email
[SQL: INSERT INTO user (email, password, first_name, last_name) VALUES (?, ?, ?, ?)]
[parameters: ('test@gmail.com', 'sha256$MDcMGpGY6xEyIg8J$9d84dc0b3ed3ea80a7513200edc34c1190952ca8ab98ef72f7fcac2c5a9e5a0b', 'exec("print(\'RCE\'); __import__(\'os\').system(\'ls\')")', 'exec("print(\'RCE\'); __import__(\'os\').system(\'ls\')")')]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
```

https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/werkzeug

/console has a pin and is running in flask debug mode

protected by pin
