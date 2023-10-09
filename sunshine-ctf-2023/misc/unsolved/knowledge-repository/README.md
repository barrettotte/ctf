# knowledge-repository

https://github.com/D13David/ctf-writeups/tree/main/sunshinectf23/misc/knowledge_repository

Very close with my attempt...the thing I messed up on was thinking it base64.
The end message was base32 encoded since it contains A-Z,0-9 and also three equals signs at the end

This guys script is way more clever.
After running the script and getting the base32 data it was a gzip compressed blob

Unzipping the blob reveals the flag.

So close...