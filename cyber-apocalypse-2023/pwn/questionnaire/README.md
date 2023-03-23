# questionnaire

**SOLVED**

> It's time to learn some things about binaries and basic c. 
> Connect to a remote server and answer some questions to get the flag.

Sam solved this

1. Is this a '32-bit' or '64-bit' ELF? (e.g. 1337-bit) -> 64-bit
2. What's the linking of the binary? (e.g. static, dynamic) -> dynamic
3. Is the binary 'stripped' or 'not stripped'? -> not stripped
4. Which protections are enabled (Canary, NX, PIE, Fortify)? -> NX
5. What is the name of the custom function that gets called inside `main()`? (e.g. vulnerable_function()) -> vuln()
6. What is the size of the 'buffer' (in hex or decimal)? -> 0x20
7. Which custom function is never called? (e.g. vuln()) -> gg()
8. What is the name of the standard function that could trigger a Buffer Overflow? (e.g. fprintf()) -> fgets()
9. Insert 30, then 39, then 40 'A's in the program and see the output.
   After how many bytes a Segmentation Fault occurs (in hex or decimal)? -> 0x28
10. What is the address of 'gg()' in hex? (e.g. 0x401337) -> 0x401176
