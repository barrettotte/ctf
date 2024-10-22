# 02

The SOC team managed to quarantine an executable we think was left behind by DEADFACE actors. 
Unfortunately, they didn’t tell us what the password to the sample was. 
Can you figure out what the password is so we can start analyzing?

Submit the flag as flag{flag-text}

Download File (20KB)
SHA1: 453c474856ee2ac50e184a8feba5526c7736116f

## Solution

look at unzipped folder, strings on RAT exe

https://www.totallynothackers.org

https://www.youtube.com/watch?v=WPUJG2jTw9s  (Nanowar Of Steel - The Call Of Cthulhu)

48 51 32 45 32 102 108 97 103 123 73 95 100 111 95 110 111 116 95 112 114 111 112 111 115 101 95 116 111 95 97 100 100 95 97 110 121 116 104 105 110 103 
95 116 111 95 119 104 97 116 95 104 97 115 95 97 108 114 101 97 100 121 95 98 101 101 110 95 119 114 105 116 116 101 110 125


```c
  local_80 = "lfaGV";
  local_88 = "50X3Rv";
  local_90 = "BmbGFn";
  local_98 = "=";
  local_a0 = "9u4oCZ";
  local_a8 = "dF93YW";
  local_b0 = "e0lfZG";
  local_b8 = "X3N0YX";
  local_c0 = "yZX0";
  local_c8 = "MDIgLS";
//   strcpy(local_78,local_50);
//   strcat(local_78,local_58);
  strcat(local_278,local_c8); //
  strcat(local_278,local_90); //
  strcat(local_278,local_b0); //
  strcat(local_278,local_a0); //
  strcat(local_278,local_a8); //
  strcat(local_278,local_88); //
  strcat(local_278,local_b8); //
  strcat(local_278,local_80); //
  strcat(local_278,local_c0); //
  strcat(local_278,local_98); //
```

MDIgLSBmbGFne0lfZG9u4oCZdF93YW50X3RvX3N0YXlfaGVyZX0=
02 - flag{I_don’t_want_to_stay_here}

For challenge 3...
03 - flag{I_do_not_propose_to_add_anything_to_what_has_already_been_written}
