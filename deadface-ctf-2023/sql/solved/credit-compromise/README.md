# credit-compromise

How many credit cards were exposed in the Aurora database hack?

Submit the flag as flag{#}.

Use the database dump from Aurora Compromise.

## Solution

`../aurora-compromise/aurora.sql`

search for `),` in insert statement - 

10390+1 = 10391

`flag{10391}`
