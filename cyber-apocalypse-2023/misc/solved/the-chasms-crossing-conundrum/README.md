# the-chasms-crossing-conundrum

**SOLVED**

> As you and your trusty team of local pyramid experts stand at the precipice of the chasm, you catch a glimpse of the otherworldly relic glowing tantalizingly in the distance. 
> But the final obstacle looms ahead - a narrow, unstable bridge that threatens to send you all tumbling into the depths below. 
> It won't hold all of you at once. 
> Time is running out, and the charge on your flashlight is dwindling. 
> The chasm seems to be closing in, as if it's trying to swallow you whole. 
> With each step, you feel the weight of the task at hand. 
> The fate of your team, and perhaps even the world, rests on your shoulders. 
> Can you summon the courage and skill to make it across in time, and claim the relic that lies just beyond your grasp?

`nc 167.99.86.8 31543`

```
# instructions

   [*] The path ahead is treacherous.                                         ☠️
☠️  [*] You have to find a viable strategy to get everyone across safely.      ☠️
☠️  [*] The bridge can hold a maximum of two persons.                          ☠️
☠️  [*] The chasm lurks on either side of the bridge waiting for those         ☠️
☠️      who think they can get across in total darkness.                       ☠️
☠️  [*] If two persons get across, one must come back with the flashlight.     ☠️
☠️  [*] The flashlight has energy only for a limited amount of time.           ☠️
☠️  [*] The time required for two persons to cross, is dictated by the slower. ☠️
☠️  [*] The answer must be given in crossing and returning pairs. For example, ☠️
☠️      [1,2],[2],... . This means that persons 1 and 2 cross and 2 gets back  ☠️
☠️       with the flashlight so others can cross.
```

```
Person 1 will take 11 minutes to cross the bridge. 
Person 2 will take 36 minutes to cross the bridge. 
Person 3 will take 73 minutes to cross the bridge.
Person 4 will take 41 minutes to cross the bridge. 
Person 5 will take 6 minutes to cross the bridge.
Person 6 will take 16 minutes to cross the bridge.
The flashlight has charge for 176 minutes.

[5,1] -> 11   (165) (fastest, 2nd fastest)      2,3,4,6 | 5,1
[5]   -> 5    (160)                           2,3,4,5,6 | 1
[5,6] -> 16   (144) (fastest, 3rd fastest)        2,3,4 | 1,5,6
[5]   -> 5    (139)                             2,3,4,5 | 1,6
[5,2] -> 36   (103)                                 3,4 | 1,2,5,6
[5]   -> 5    (95)                                3,4,5 | 1,2,6
[4,3] -> 73   (22)                                    5 | 1,2,3,4,6
[1]   -> 11   (11)                                  1,5 | 2,3,4,6
[1,5] -> 11   (0)                                       | 1,2,3,4,5,6

```

- https://en.wikipedia.org/wiki/Bridge_and_torch_problem
- https://www.geeksforgeeks.org/puzzle-18-torch-and-bridge/
- https://srflp.github.io/bridge-and-torch-problem/

was too dumb to write, ripped code from https://github.com/murdesi/bridge-crossing

`python3 flag.py` (try until 6 person)

`HTB{4cro55_th3_br1dg3_4nd_th3_ch4sm_l13s_th3_tr34sur3}`
