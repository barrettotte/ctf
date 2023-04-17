
# s = 'import os;os.getcwd()'
# s = "globals()['__builtins__'].__import__('os')"
s = "exec('import os; print(os.getcwd())')"

print(str(eval(s)))

# import os;os.getcwd()

s = "import os"
t = "os.getcwd()"

# print(str(eval(input())) + str(eval(input())))


# subprocess.Popen(input(), shell=True)

print(eval('globals()'))