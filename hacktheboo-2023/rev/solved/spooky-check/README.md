# spooky-check

My new tool will check if your password is spooky enough for use during Halloween - but watch out for snakes...

## Solution


SUP3RS3CR3TK3Y

HTB{SUP3RS3CR3TK3Y} - nope

```sh
python3 -m compileall test.py
```

python 3.10 magic - 6f0d0d0a

```sh
hexedit check-copy.pyc
```

Magic number list - https://stackoverflow.com/questions/514371/whats-the-bad-magic-number-error/514395#514395
can be found in `Python/import.c` ... somewhere? https://github.com/python/cpython/blob/main/Python/import.c

python2 03f30d0a

`HTB{SUP3RS3CR3TK3Ys}` nope


chatgpt says 0xA70D0D0A is python 3.11 ?

`python3.11 check.pyc` - works!

https://docs.python.org/3/library/dis.html

`python3.11 -m pdb check.pyc`


(((((f+24)&255)^KEY)[i%14])-74)&255

got bytecode

https://docs.python.org/3.11/library/dis.html

```py
# trying to figure out how list comps disassemble

s = 'hello'
[(i,c) for (i,c) in enumerate(s)]
```

```txt
Bytcode for python snippet above

  0           0 RESUME                   0

  1           2 LOAD_CONST               0 ('hello')
              4 STORE_NAME               0 (s)

  4           6 LOAD_CONST               1 (<code object <listcomp> at 0x7fa51240e5d0, file "compile-check.py", line 4>)
              8 MAKE_FUNCTION            0
             10 PUSH_NULL
             12 LOAD_NAME                1 (enumerate)
             14 LOAD_NAME                0 (s)
             16 PRECALL                  1
             20 CALL                     1
             30 GET_ITER
             32 PRECALL                  0
             36 CALL                     0
             46 POP_TOP
             48 LOAD_CONST               2 (None)
             50 RETURN_VALUE

Disassembly of <code object <listcomp> at 0x7fa51240e5d0, file "compile-check.py", line 4>:
  4           0 RESUME                   0
              2 BUILD_LIST               0
              4 LOAD_FAST                0 (.0)
        >>    6 FOR_ITER                 9 (to 26)
              8 UNPACK_SEQUENCE          2
             12 STORE_FAST               1 (i)
             14 STORE_FAST               2 (c)
             16 LOAD_FAST                1 (i)
             18 LOAD_FAST                2 (c)
             20 BUILD_TUPLE              2
             22 LIST_APPEND              2
             24 JUMP_BACKWARD           10 (to 6)
        >>   26 RETURN_VALUE

```

`HTB{mod3rn_pyth0n_byt3c0d3}`
