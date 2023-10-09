# house-of-sus

https://youtu.be/qA6ajf7qZtQ?si=b4dwg1Xyw5qzj6gK&t=2277

- given libc, linker, and bin file
- based on old/common heap expoitation technique called house of force
- `malloc()` is called with a size of our choosing
- libc version for this challenge is 227, an old version and is vulnerable to this exploit
- tool called `pwninit` - does magic to patch binary to use local libc library downloaded for challenge
- also given heap address leap on start of program
- gdb `vmmap` - how process is laid out, can find heap address
- with exploit we'll be able to create heap chunks such that we override the entire memory space
- then when heap memory read it will read memory from wherever we want such as the GOT
- gdb `vis_heap_chunks` -> visualize the heap
- top chunk - how much the heap thinks it has left
- override top chunk with 0xFFFFFFFFFFFF so that it thinks it has effectively unlimited size
- eventually causing addresses to wrap around

onegadgets? 1gadgets? - magic tool for getting `/bin/sh`

this was kind of insane, no way would I have figured this out right now...just watch video
