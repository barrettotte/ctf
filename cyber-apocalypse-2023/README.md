# cyber-apocalypse-2023

https://ctf.hackthebox.com/event/821

## Results

- team: OperationalStatus
- 42/74 flags
- 172/6482 team rank

## Flags (42/74)

One warmup flag and the following categories.

### pwn (5/10)

- [x] [initialize-connection](pwn/init-connection/) - connection check
- [x] [questionnaire](pwn/questionnaire/) - shell
- [x] [getting-started](pwn/getting-started/) - buffer overflow
- [x] [labyrinth](pwn/labyrinth/) - buffer overflow, ROP
- [x] [pandoras-box](pwn/pandoras-box/) - buffer overflow, ROP, ret2plt
- [ ] [void](pwn/void/) - buffer overflow, GOT rewrite TODO: review writeup
- [ ] [kana](pwn/kana/) TODO: review writeup
- [ ] [control-room](pwn/control-room/) TODO: review writeup
- [ ] [math-door](pwn/math-door/) - TODO: review writeup
- [ ] [runic](pwn/runic/) - TODO: review writeup

### web (6/9)

- [x] [trapped-source](web/trapped-source/) - source
- [x] [gunhead](web/gunhead/) - command injection
- [x] [drobots](web/drobots/) - SQLi
- [x] [passman](web/passman/) - IDOR, GraphQL
- [x] [orbital](web/orbital/) - SQLi, path traversal
- [x] [didactic-octo-paddles](web/didactic-octo-paddles/) - JWT none, jsrender SSTI
- [ ] [spybug](web/spybug/) - pug SSTI, XSS TODO: review writeup
- [ ] [unearthly-shop](web/unearthly-shop/) - mongoDB leak, PHP deserialization, auto load gadgets, remote code execution TODO: review writeup
- [ ] [traptrack](web/traptrack/) - SSRF, gopher TODO: review writeup

### blockchain (2/3)

- [x] [navigating-the-unknown](blockchain/navigating-the-unknown/) - smart contract transaction
- [x] [shooting-101](blockchain/shooting-101/) - smart contract fallback and receive transactions
- [ ] [the-art-of-deception](blockchain/art-of-deception/) - smart contract interaction TODO: review writeup

### hardware (4/5)

- [x] [timed-transmission](hardware/timed-transmission/) - logic analyzer
- [x] [critical-flight](hardware/critical-flight/) - kicad
- [x] [debug](hardware/debug/) - logic analyzer, serial
- [x] [secret-code](hardware/secret-code/) - kicad, logic analyzer, 7-segment display decoding
- [ ] [hm74](hardware/hm74/) - Hamming (7,4) error correction TODO: review writeup

### reversing (5/10)

- [x] [shattered-tablet](reversing/shattered-tablet/) - ghidra
- [x] [she-shells-c-shells](reversing/she-shells-c-shells/) - ghidra
- [x] [needle-in-a-haystack](reversing/needle-in-a-haystack/) - strings
- [x] [hunting-license](reversing/hunting-license/) - strings, ghidra
- [x] [cave-system](reversing/cave-system/) - angr
- [ ] [alien-saboteaur](reversing/alien-saboteaur/) - TODO: review writeup
- [ ] [gimmick-dsp](reversing/gimmick-dsp/) - TODO: find and review writeup
- [ ] [vessel-cartographer](reversing/vessel-cartographer/) - TODO: find and review writeup
- [ ] [somewhat-linear](reversing/somewhat-linear/) - TODO: review writeup
- [ ] [analogue-signal-processing](reversing/analogue-signal-processing/) - TODO: review writeup

### ml (3/7)

- [x] [reconfiguration](ml/reconfiguration/) - orange
- [x] [mysterious-learnings](ml/reconfiguration/) - tensorflow, base64 encoded
- [x] [last-hope](ml/reconfiguration/) - Qiskit, QASM
- [ ] [on-the-rescue](ml/on-the-rescue/) - TODO: review writeup
- [ ] [vision-chip](ml/vision-chip/) - TODO: find and review writeup
- [ ] [reading-the-stars](ml/reading-the-stars/) - TODO: find and review writeup
- [ ] [the-trial-of-the-sky](ml/the-trial-of-the-sky/) - TODO: find and review writeup

### misc (7/8)

- [x] [persistence](misc/persistence/) - web request
- [x] [hijack](misc/hijack/) - python yaml deserialization
- [x] [restricted](misc/restricted/) - ssh config
- [x] [remote-computation](misc/remote-computation/) - parsing
- [x] [janken](misc/janken/) - ghidra
- [x] [nehebkaus-trap](misc/nehebkaus-trap/) - python exec()
- [x] [the-chasms-crossing-conundrum](misc/the-chasms-crossing-conundrum/) - bridge and torch problem
- [ ] calibrator - TODO: review writeup

### forensics (6/10)

- [x] [plaintext-treasure](forensics/plaintext-treasure/) - wireshark
- [x] [alien-cradle](forensics/alien-cradle/) - source
- [x] [extraterrestrial-persistence](forensics/extraterrestrial-persistence/) - base64 decode
- [x] [roten](forensics/roten/) - wireshark, obfuscated PHP
- [x] [packet-cyclone](forensics/packet-cyclone/) - event logs, chainsaw
- [ ] [artifacts-of-dangerous-sightings](forensics/artifacts-of-dangerous-sightings/) - TODO: review writeup
- [x] [relic-maps](forensics/relic-maps/) - obfuscated PowerShell, AES decrypt
- [ ] [bashic-ransomware](forensics/bashic-ransomware/) - TODO: review writeup
- [ ] [interstellar-c2](forensics/interstellar-c2/) - TODO: find and review writeup
- [ ] [pandoras-bane](forensics/pandoras-bane/) - TODO: review writeup

### crypto (3/11)

- [x] [ancient-encodings](crypto/ancient-encodings/) - decode
- [x] [small-steps](crypto/small-steps/) - textbook RSA, Chinese Remainder Theorem
- [x] [perfect-synchronization](crypto/perfect-synchronization/) - AES ECB, Patristocrat cipher
- [ ] [multipage-recyclings](crypto/multipage-recyclings/) - TODO: find and review writeup
- [ ] [inside-the-matrix](crypto/inside-the-matrix/) - TODO: review writeup
- [ ] [colliding-heritage](crypto/colliding-heritage/) - TODO: review writeup
- [ ] [elliptic-labyrinth](crypto/elliptic-labyrinth/) - TODO: review writeup
- [ ] [elliptic-labyrinth-revenge](crypto/elliptic-labyrinth-revenge/) - TODO: review writeup
- [ ] [biased-heritage](crypto/biased-heritage/) - TODO: review writeup
- [ ] [converging-visions](crypto/converging-visions/) - TODO: review writeup
- [ ] [blokechain](crypto/blokechain/) - TODO: review writeup
