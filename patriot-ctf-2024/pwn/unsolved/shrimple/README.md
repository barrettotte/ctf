# Not So Shrimple Is It 

Peel back the shell, unless you eat shrimp with the shell.

`nc chal.competitivecyber.club 8884`

## Solution

ghidra

```c
void main(void) {
  char buffer [64];
  undefined8 first;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined2 local_28;
  undefined local_26;
  
  puts("Welcome to the shrimplest challenge! It is so shrimple, we\'ll give you 3 shots.");
  for (i = 0; i < 3; i = i + 1) {
    printf("Remember to just keep it shrimple!\n>> ");
    fgets(buffer,0x32,stdin);
    
    puts("Adding shrimp...");
    first = 0x2079736165206f73; // so easy
    local_40 = 0x73206f7320646e61; // and so s
    local_38 = 0x2c656c706d697268; // hrimple,
    local_30 = 0x7566206576616820; // have fu
    local_28 = 0x216e;             // n!
    local_26 = 0;
    // so easy and so shrimple,have fun!

    strncat((char *)&first, buffer, 0x32);
    printf("You shrimped the following: %s\n", &first);
  }

  puts("That\'s it, hope you did something cool...");
  return;
}
```

have to call shrimp() func
0x32 - 50

gdb si, ni
