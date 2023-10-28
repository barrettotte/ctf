# ghostly-templates

In the dark corners of the internet, a mysterious website has been making waves among the cybersecurity community. 
This site, known for its Halloween-themed templates, has sparked rumors of an eerie secret lurking beneath the surface. 
Will you delve into this dark and spooky webapp to uncover the hidden truth?

## Solution

hosted `custom.tpl` in a github gist

```html
failed:

{{ GetServerInfo "ls" }}
{{ exec.Command "sh" "-c" "ls" }}
{{ .GetServerInfo "ls" }}
```

https://www.onsecurity.io/blog/go-ssti-method-research/
