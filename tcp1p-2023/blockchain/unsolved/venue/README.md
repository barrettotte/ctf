# venue

Look at the Amazing Party Venue So do you wish to enter?

contract: 0x1AC90AFd478F30f2D617b3Cb76ee00Dd73A9E4d3

provider: https://eth-sepolia.g.alchemy.com/v2/SMfUKiFXRNaIsjRSccFuYCq8Q3QJgks8

Priv-Key: Please use your own private-key, if you need ETH for transact, You can either DM the Author, or get it by yourself at https://sepoliafaucet.com/

## Solution

https://sepoliafaucet.com/

Signed up free account - https://www.alchemy.com/

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Blockchain/Venue/Private/writeup.md

You have 2 choices here, either use the abi provided to call the "enterVenue()" function or straight up using cast to call the function.

```py
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/SMfUKiFXRNaIsjRSccFuYCq8Q3QJgks8')) 
contract_address = "0x56b95CD61857A806e7F6E3da73426D1CD6e87303"
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "initialFlag",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "initialMessage",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "enterVenue",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "goBack",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)
result = contract.functions.enterVenue().call()
print("Result of enterVenue():", result)
```

```sh
cast call --rpc-url https://eth-sepolia.g.alchemy.com/v2/SMfUKiFXRNaIsjRSccFuYCq8Q3QJgks8 "enterVenue()" | xxd -r -p
```
