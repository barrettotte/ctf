# another-discord

TCP1P has another discord server?
https://discord.gg/kzrryCUutP 

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Misc/Another%20Discord/writeup

Got two parts of the flag in my attempt, but had no idea we had to start doing API calls...probably should have guess...

1. Check voice chat
2. `curl https://discordapp.com/api/v6/guilds/1154468492259627008/roles -H "Authorization: something"`
3. Check event details
4. `curl https://discordapp.com/api/v6/guilds/1154468492259627008/channels -H "Authorization: something"`

https://discord.com/developers/docs/reference
