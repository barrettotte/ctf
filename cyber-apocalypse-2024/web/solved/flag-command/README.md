# flag-command

Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!

## Solution

94.237.49.116:51110

POST http://94.237.49.116:51110/api/monitor `{command: HEAD NORTH}`

```js
// main.js

if(data.message.includes('HTB{')) {
    playerWon();
    fetchingResponse = false;

    return;
}

if (currentCommand == 'HEAD NORTH') {
    currentStep = '2';
}
else if (currentCommand == 'FOLLOW A MYSTERIOUS PATH') {
    currentStep = '3'
}
else if (currentCommand == 'SET UP CAMP') {
    currentStep = '4'
}
```

GET http://94.237.49.116:51110/api/options

```sh
curl 'http://94.237.49.116:51110/api/options'
```

```json
{
  "allPossibleCommands": {
    "1": [
      "HEAD NORTH",
      "HEAD WEST",
      "HEAD EAST",
      "HEAD SOUTH"
    ],
    "2": [
      "GO DEEPER INTO THE FOREST",
      "FOLLOW A MYSTERIOUS PATH",
      "CLIMB A TREE",
      "TURN BACK"
    ],
    "3": [
      "EXPLORE A CAVE",
      "CROSS A RICKETY BRIDGE",
      "FOLLOW A GLOWING BUTTERFLY",
      "SET UP CAMP"
    ],
    "4": [
      "ENTER A MAGICAL PORTAL",
      "SWIM ACROSS A MYSTERIOUS LAKE",
      "FOLLOW A SINGING SQUIRREL",
      "BUILD A RAFT AND SAIL DOWNSTREAM"
    ],
    "secret": [
      "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"
    ]
  }
}
```

```sh
curl 'http://94.237.49.116:51110/api/monitor' \
  -X POST \
  -H 'content-type: application/json' \
  --data '{"command": "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"}'

# {
#   "message": "HTB{D3v3l0p3r_t00l5_4r3_b35t_wh4t_y0u_Th1nk??!}"
# }

```