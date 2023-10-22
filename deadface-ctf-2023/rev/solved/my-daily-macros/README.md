# my-daily-macros

DEADFACE has gotten hold of the HR departments contact list and has been distributing it with a macro in it. 
There is a phrase the RE team would like for you to pull out of the macro.

Submit the flag as flag{some_text}.

## Solution

```sh
strings
# vbaProject.bin

binwalk -e HR_List.xlsm

# vbaProject.bin
```

`flag{youll_never_find_this_}`
