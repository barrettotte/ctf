import angr
import sys

target = angr.Project('./cave')
entry = target.factory.entry_state()
sim = target.factory.simgr(entry)

# The main binary is a position-independent executable. It is being loaded with a base address of 0x400000.
# target_address = 0x101aba
# fail_address = 0x101ac8
target_address = 0x401aba
fail_address = 0x401a8
sim.explore(find=target_address, avoid=fail_address)

if sim.found:
    solution = sim.found[0]
    print(solution.posix.dumps(sys.stdin.fileno()))
