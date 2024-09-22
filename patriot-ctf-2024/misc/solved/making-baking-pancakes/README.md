# Making Baking Pancakes

How many layers are on your pancakes?

`nc chal.pctf.competitivecyber.club 9001`

## Solution

```txt
Welcome to the pancake shop!
Pancakes have layers, we need you to get through them all to get our secret pancake mix formula.
This server will require you to complete 1000 challenge-responses.
A response can be created by doing the following:
1. Base64 decoding the challenge once (will output (encoded|n))
2. Decoding the challenge n more times.
3. Send (decoded|current challenge iteration)
Example response for challenge 485/1000: e9208047e544312e6eac685e4e1f7e20|485
Good luck!

Challenge: VmtkMGExSnRWbFpPVlZaVFlsaG9UMVZxUW1GaU1WSnlXa2RHYUZKVVJsWldNV2h6VkcxV2NrNVhPVlZXVmtwUFZGWmFjbVZXVm5Sa1JUVlhUVmQwTkZaSE1IaFNNa3BXVGxoR1ZsWkVRVGs9fDQ=
(0/1000) >>
```
