# pdfify

My friend told me that he wants to build a PDF generator for our assignment, 
so we created this app. Could you please test it for me?

## Solution

```md
https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Web/PDFIFY/writeup/WRITEUP.md

# PDFIFY

There are 4 vulnerabilities in this challenge:

1. **SQL Injection (SQLI)** in the 'key' parameter of the Code Igniter ORM: We can exploit this to gain admin access.

2. **Server-Side Request Forgery (SSRF)** in the 'img' URL of the Knp\Snappy\Pdf module, which renders PDFs: We can use this to access the bot via a GET request.

3. **Another SSRF** in 'bot.js' that can be used to write files and bypass local file restrictions in code vulnerable to CVEs below.

4. **CVE** [GHSA-gq6w-q6wh-jggc](https://github.com/advisories/GHSA-gq6w-q6wh-jggc) that can be used to achieve Remote Code Execution (RCE).
```

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Web/PDFIFY/writeup/solver
