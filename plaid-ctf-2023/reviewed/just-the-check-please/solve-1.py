# gdb -q -x debug2.py
import gdb
import string

gdb.execute('file ./check')
gdb.execute("b*0x0000555555562c5f")

#found = [True, False, True, True, False, True, True, True, False, False, True, False, True, False, False, False]
found=[False]*16
flags = [
    "wat3rT1ghT-blAz3",
    #"m?t??T??????l???",
    # "??t??T??????b???",
    # "??t??T??????d???",
    # "??t??T??????B???",
    # "??t??T??????D???",
]
for i in range(len(found)):
    if flags[0][i]!="?":
        found[i]=True

with open("log2", "w") as f:
    f.write('')
def write(s):
    with open("log2", "a") as f:
        f.write(s + '\n')


for flag in flags:
    write('=== ' + flag + ' ===')
    for i in range(16):
        if not found[i]:
            none=""
            gdb.execute('r "' + flag[:i] + 'b' + flag[i+1:] + '"')
            r12_b = gdb.parse_and_eval("$r12")
            rax_b = gdb.execute("x/gx $rax",to_string=True).split(':')[1].strip()
            gdb.execute('r "' + flag[:i] + 'c' + flag[i+1:] + '"')
            r12_c = gdb.parse_and_eval("$r12")
            rax_c = gdb.execute("x/gx $rax",to_string=True).split(':')[1].strip()
            gdb.execute('r "' + flag[:i] + 'd' + flag[i+1:] + '"')
            r12_d = gdb.parse_and_eval("$r12")
            rax_d = gdb.execute("x/gx $rax",to_string=True).split(':')[1].strip()
            oridx=eval(gdb.execute("x/wx $rsp+0x20",to_string=True).split(':')[1].strip())
            if rax_b == rax_c and rax_c == rax_d:
                pass
                # continue
            write("start "+str(i) + ' ' + str(r12_b) + ' ' + str(r12_c) + ' ' + str(r12_d))
            for j in range(32, 127):
                if chr(j) == '"' or chr(j) == "'" or chr(j) == '\\' or chr(j) == '$':
                    continue
                # write(chr(i))
                cc=flag[:i] + chr(j) + flag[i+1:]
                try:
                    gdb.execute('r "' + cc + '"')
                except:
                    continue
                r12 = eval(str(gdb.parse_and_eval("$r12")))
                rax_real = eval(gdb.execute("x/gx $rax",to_string=True).split(':')[1].strip())
                # rax = gdb.execute("x/gx $rax",to_string=True).split(':')[1].strip()
                # print(r12_b)
                # print(r12_c)
                # print(r12_d)
                
                if r12_b == r12_c:
                    r12_cmp = r12_b
                elif r12_b == r12_d:
                    r12_cmp = r12_b
                elif r12_c == r12_d:
                    r12_cmp = r12_c
                else:
                    print("nothing")
                idx=eval(gdb.execute("x/wx $rsp+0x20",to_string=True).split(':')[1].strip())
                if idx > oridx:
                    write(cc + ' '+hex(rax_real)+' ' + str(r12_cmp) + ' ' + hex(r12))
                    write(hex(idx)+' vs '+hex(oridx))
write("end")