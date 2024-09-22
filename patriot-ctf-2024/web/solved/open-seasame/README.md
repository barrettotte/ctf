# Open Seasame

Does the CLI listen to magic?

http://chal.competitivecyber.club:13336

Flag format: CACI{.*}

one of the admin ports is apparently open?

## Solution

http://chal.competitivecyber.club:13336/visit

```py
@app.route('/api/cal', methods=['GET'])
def get_cal():
    cookie = request.cookies.get('secret')

    if cookie == None:
        return '{"error": "Unauthorized"}'
    
    if cookie != SECRET:
        return '{"error": "Unauthorized"}'
    
    modifier = request.args.get('modifier','')
    
    return '{"cal": "'+subprocess.getoutput("cal "+modifier)+'"}'
```

```sh
curl -v --cookie "secret=Yes" http://chal.competitivecyber.club:13336/api/cal
```

https://webhook.site/#!/view/607eaea6-e5d5-4b19-9fed-a20c88b43f18

```sh
python3 solve.py

# enter api/stats/a4e1ff18-834a-401a-8060-75ab583b3e86 into prompt
# check webhook.site
# flag in query params

# CACI1_l0v3_c0mm4nd_1nj3ct10n
```
