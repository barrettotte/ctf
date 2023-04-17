# cyber-apocalypse-2023

https://ctf.hackthebox.com/event/821

## Results

- team: OperationalStatus
- 42/74 flags
- 172/6482 team rank

## Flags (42/74)

One warmup flag and the following categories.

### pwn (5/10)

- [x] [initialize-connection](pwn/solved/init-connection/) - connection check
- [x] [questionnaire](pwn/solved/questionnaire/) - shell
- [x] [getting-started](pwn/solved/getting-started/) - buffer overflow
- [x] [labyrinth](pwn/solved/labyrinth/) - buffer overflow, ROP
- [x] [pandoras-box](pwn/solved/pandoras-box/) - buffer overflow, ROP, ret2plt
- [ ] [void](pwn/unsolved/void/) - buffer overflow, GOT rewrite
- [ ] [kana](pwn/unsolved/kana/)
- [ ] [control-room](pwn/unsolved/control-room/)
- [ ] [math-door](pwn/unsolved/math-door/)
- [ ] [runic](pwn/unsolved/runic/)

### web (6/9)

- [x] [trapped-source](web/solved/trapped-source/) - source
- [x] [gunhead](web/solved/gunhead/) - command injection
- [x] [drobots](web/solved/drobots/) - SQLi
- [x] [passman](web/solved/passman/) - IDOR, GraphQL
- [x] [orbital](web/solved/orbital/) - SQLi, path traversal
- [x] [didactic-octo-paddles](web/solved/didactic-octo-paddles/) - JWT none, jsrender SSTI
- [ ] [spybug](web/unsolved/spybug/) - pug SSTI, XSS
- [ ] [unearthly-shop](web/unsolved/unearthly-shop/) - mongoDB leak, PHP deserialization, auto load gadgets, RCE
- [ ] [traptrack](web/unsolved/traptrack/) - SSRF, gopher

### blockchain (2/3)

- [x] [navigating-the-unknown](blockchain/solved/navigating-the-unknown/) - smart contract transaction
- [x] [shooting-101](blockchain/solved/shooting-101/) - smart contract fallback and receive transactions
- [ ] [the-art-of-deception](blockchain/unsolved/art-of-deception/) - smart contract interaction

### hardware (4/5)

- [x] [timed-transmission](hardware/solved/timed-transmission/) - logic analyzer
- [x] [critical-flight](hardware/solved/critical-flight/) - kicad
- [x] [debug](hardware/solved/debug/) - logic analyzer, serial
- [x] [secret-code](hardware/solved/secret-code/) - kicad, logic analyzer, 7-segment display decoding
- [ ] [hm74](hardware/unsolved/hm74/) - Hamming (7,4) error correction

### reversing (5/10)

- [x] [shattered-tablet](reversing/solved/shattered-tablet/) - ghidra
- [x] [she-shells-c-shells](reversing/solved/she-shells-c-shells/) - ghidra
- [x] [needle-in-a-haystack](reversing/solved/needle-in-a-haystack/) - strings
- [x] [hunting-license](reversing/solved/hunting-license/) - strings, ghidra
- [x] [cave-system](reversing/solved/cave-system/) - angr
- [ ] [alien-saboteaur](reversing/solved/alien-saboteaur/)
- [ ] [gimmick-dsp](reversing/unsolved/gimmick-dsp/)
- [ ] [vessel-cartographer](reversing/unsolved/vessel-cartographer/)
- [ ] [somewhat-linear](reversing/unsolved/somewhat-linear/)
- [ ] [analogue-signal-processing](reversing/unsolved/analogue-signal-processing/)

### ml (3/7)

- [x] [reconfiguration](ml/solved/reconfiguration/) - orange
- [x] [mysterious-learnings](ml/solved/reconfiguration/) - tensorflow, base64 encoded
- [x] [last-hope](ml/solved/reconfiguration/) - Qiskit, QASM
- [ ] [on-the-rescue](ml/unsolved/on-the-rescue/)
- [ ] [vision-chip](ml/unsolved/vision-chip/)
- [ ] [reading-the-stars](ml/unsolved/reading-the-stars/)
- [ ] [the-trial-of-the-sky](ml/unsolved/the-trial-of-the-sky/)

### misc (7/8)

- [x] [persistence](misc/solved/persistence/) - web request
- [x] [hijack](misc/solved/hijack/) - python yaml deserialization
- [x] [restricted](misc/solved/restricted/) - ssh config
- [x] [remote-computation](misc/solved/remote-computation/) - parsing
- [x] [janken](misc/solved/janken/) - ghidra
- [x] [nehebkaus-trap](misc/solved/nehebkaus-trap/) - python exec()
- [x] [the-chasms-crossing-conundrum](misc/solved/the-chasms-crossing-conundrum/) - bridge and torch problem
- [ ] [calibrator](misc/unsolved/calibrator/)

### forensics (6/10)

- [x] [plaintext-treasure](forensics/solved/plaintext-treasure/) - wireshark
- [x] [alien-cradle](forensics/solved/alien-cradle/) - source
- [x] [extraterrestrial-persistence](forensics/solved/extraterrestrial-persistence/) - base64 decode
- [x] [roten](forensics/solved/roten/) - wireshark, obfuscated PHP
- [x] [packet-cyclone](forensics/solved/packet-cyclone/) - event logs, chainsaw
- [ ] [artifacts-of-dangerous-sightings](forensics/unsolved/artifacts-of-dangerous-sightings/)
- [x] [relic-maps](forensics/solved/relic-maps/) - obfuscated PowerShell, AES decrypt
- [ ] [bashic-ransomware](forensics/unsolved/bashic-ransomware/)
- [ ] [interstellar-c2](forensics/unsolved/interstellar-c2/)
- [ ] [pandoras-bane](forensics/unsolved/pandoras-bane/)

### crypto (3/11)

- [x] [ancient-encodings](crypto/solved/ancient-encodings/) - decode
- [x] [small-steps](crypto/solved/small-steps/) - textbook RSA, Chinese Remainder Theorem
- [x] [perfect-synchronization](crypto/solved/perfect-synchronization/) - AES ECB, Patristocrat cipher
- [ ] [multipage-recyclings](crypto/unsolved/multipage-recyclings/)
- [ ] [inside-the-matrix](crypto/unsolved/inside-the-matrix/)
- [ ] [colliding-heritage](crypto/unsolved/colliding-heritage/)
- [ ] [elliptic-labyrinth](crypto/unsolved/elliptic-labyrinth/)
- [ ] [elliptic-labyrinth-revenge](crypto/unsolved/elliptic-labyrinth-revenge/)
- [ ] [biased-heritage](crypto/unsolved/biased-heritage/)
- [ ] [converging-visions](crypto/unsolved/converging-visions/)
- [ ] [blokechain](crypto/unsolved/blokechain/)
