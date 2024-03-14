# pet-companion

Embark on a journey through this expansive reality, where survival hinges on battling foes. In your quest, a loyal companion is essential. Dogs, mutated and implanted with chips, become your customizable allies. Tailor your pet's demeanor—whether happy, angry, sad, or funny—to enhance your bond on this perilous adventure.

## Solution

https://youtu.be/EGItzKCxTdQ?si=l9kzAIbmEodZCddS&t=1982

buffer overflow

```c
// buffer is 64 bytes

read(0, &buffer, 0x100); // 256 bytes
```

no canary, easy buffer overflow

no PIE, address of main is known

leak GOT entry, libc leak, jump to libc, ROP, system("/bin/sh")
